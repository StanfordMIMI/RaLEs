import numpy as np
import random
import torch
import tqdm
import sys

from .base import Base
from .validator import Validator
from .utils import CheckpointSaver, create_model, create_data_loader


class InitTrainor(Base):
    def __init__(self, opts):
        super().__init__(opts)
        self.seed = self.set_seed()

        # Checkpoints
        self.saver = CheckpointSaver(root=self.ckpt_dir, seed=self.seed)

        # Dataloader
        self.dl = create_data_loader(self.opts, 'train', self.ckpt_dir)

        # Model
        self.model = create_model(self.opts)
        self.model.cuda()
        print('\033[1m\033[91mModel {} created \033[0m'.format(type(self.model).__name__))
        print(self.model)
        # self.model = torch.nn.DataParallel(self.model)
        assert hasattr(self.model, "eval_func")

        # Optimizer
        self.optimizer = self.create_optimizer()

        # Hyper
        self.lr = self.opts.lr
        self.early_stop_metric = self.opts.early_stop_metric
        self.eval_start = self.opts.eval_start

        # Validator is None at init
        self.evaluator: Validator = None


    def set_seed(self, seed=None):
        if seed is None:
            seed = int(random.randint(0, 9999999))
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        return seed

    def create_optimizer(self):
        if self.opts.optimizer is not None:
            optimizer = self.opts.optimizer
        else:
            optimizer = 'adam'

        params = self.model.parameters()

        if optimizer.lower() == 'sgd':
            optimizer = torch.optim.SGD(params, lr=self.opts.lr, weight_decay=self.opts.weight_decay)
        elif optimizer.lower() == 'adam':
            optimizer = torch.optim.Adam(params, lr=self.opts.lr, weight_decay=self.opts.weight_decay)
        else:
            raise Exception("Unknown optimizer {}.".format(optimizer))

        return optimizer


class Trainor(InitTrainor):
    def __init__(self, opts):
        super().__init__(opts=opts)

    def start(self):
        lr_patience = 0
        early_stop = 0

        for epoch in range(0, self.opts.epochs + 1):
            self.model.train()
            iteration = 0
            losses = []

            pbar = tqdm.tqdm(self.dl, total=len(self.dl))
            for batch in pbar:
                self.optimizer.zero_grad()
                loss = self.model(**batch)['loss']
                loss.backward()
                self.optimizer.step()
                losses.append(loss.item())
                iteration += 1
                pbar.set_description(
                    'Epoch {}, Lr {}, Loss {:.2f}, {} {:.2f}, ES {}'.format(
                        epoch + 1,
                        self.lr,
                        sum(losses) / iteration,
                        self.early_stop_metric,
                        self.evaluator.mean_eval_metric,
                        early_stop,
                    ))

                # if self.iteration == 100:
                #     break

            # self.update_lr()
            if epoch > self.eval_start - 1:
                self.evaluator.epoch = epoch
                self.evaluator.start()

                # Fetch eval score and compute early stop
                mean_eval_metric = np.mean([s[self.early_stop_metric] for s in self.evaluator.scores])
                if mean_eval_metric > self.evaluator.mean_eval_metric:
                    self.saver.save(model=self.model.state_dict(), tag=mean_eval_metric, current_step=epoch)
                    self.evaluator.mean_eval_metric = mean_eval_metric
                    early_stop = 0
                    lr_patience = 0
                else:
                    early_stop += 1
                    lr_patience += 1
                    self.update_lr_plateau(lr_patience)
                    self.check_early_stop(early_stop)

    def update_lr_plateau(self, lr_patience):
        if self.lr == self.opts.lr_min:
            return

        # Apply decay if applicable
        if lr_patience % self.opts.lr_decay_patience == 0:
            lr = self.lr * self.opts.lr_decay_factor
            for param_group in self.optimizer.param_groups:
                param_group['lr'] = lr
            self.lr = lr

    def check_early_stop(self, early_stop):
        if early_stop == self.opts.early_stop:
            print("Early stopped reached")
            sys.exit()
