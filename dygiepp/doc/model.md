# Model

We include some notes and common modeling issues here.

## Table of Contents
- [Debugging](#debugging)
- [Batching and batch size](#batching-and-batch-size)
- [Multi-dataset training](#multi-dataset-training)


## Debugging

Debugging by running `allennlp train` or `allennlp predict` isn't optimal, because the model takes more than 10 seconds just to initialize. To speed up the debugging loop, there's a script [debug_forward_pass.py](../scripts/debug/debug_forward_pass.py) that will run a forward pass for you without doing all the initialization logic, and without loading in the BERT embeddings. See the script for usage information.

### Common problems encountered during debugging

- `nan`'s in gradients or parameters: This may be due to characters that the tokenizer doesn't recognize. See [this issue](https://github.com/allenai/allennlp/issues/4612) for more details. Before doing any more extensive debugging, check your input documents for weird unicode characters.


## Batching and batch size

AllenNLP has a data structure to represent an [Instance](https://guide.allennlp.org/reading-data#1), which it defines as "the atomic unit of prediction in machine learning". For example, in sentiment classification, an `Instance` would usually be a single sentence.

`Instance`s are slighly awkward for DyGIE++, because
three tasks (named entity tagging, relation extraction, event extraction) are *within-sentence*, making a sentence the natural unit for an `Instance`. However, coreference resolution is *cross-sentence*, making a *document* the natural unit for an `Instance`.

The choice we have made is to model an `Instance` as a *document*. By default, we use a batch size of 1, which means that each minibatch during training is a single *document*. We make this choice because it's conceptually the simplest, but it is not optimal in some circumstances. We describe these and offer some solutions. These solutions mostly involve doing data preprocessing *outside the modeling code*; this keeps the (already somewhat confusing) modeling code as simple as possible.

--------------------

- **Problem**: If you're not doing coreference resolution, then it's wasteful to have minibatches with sentences of widely varying lengths. Instead, you should create minibatches of similar-length sentences from different documents.
- **Solution**: Our solution is as follows:
  - "Collate" the dataset into "psuedo-documents" containing sentences of similar length. Keep track of the original document that each sentence came from. Users may write their own script, or use [collate.py](../scripts/data/shared/collate.py) to accomplish this.
  - Run training / prediction / whatever else.
  - For prediction, "un-collate" the predictions to recover the original documents using [uncollate.py](../scripts/data/shared/uncollate.py)
- **Details**: It's up to the user to collate the sentences in a way that makes good use of GPU memory. The `collate` script has two options to help control this.
  - `max_spans_per_doc`: In general, GPU usage for DyGIE++ scales with the number of spans in the document, which scales as the *square* of the sentence length. Thus, `collate.py` takes `max_spans_per_doc` as input. We calculate the number of spans per doc as `n_sentences * (longest_sentence_length ** 2)`. We've found that setting `max_spans_per_doc=50000` creates batches that utilize GPU effectively. However, we have not explored this exhaustively and we welcome feedback and PR's.
  - `max_sentences_per_doc`
    - **If If you're training a model**, you probably want to avoid the creation of pseudo-documents containg hundreds of short sentences - even if they'd fit in GPU. Having wildly varying numbers of sentences per batch seemed to do weird things during training, though this is anecdotal. To avoid this, set `max_sentences_per_doc` to some reasonable value. The default of 16 seems safe, though bigger might be OK too.
    - **If you're using an existing model to make predictions**: Just set this to a big number to make the best use of your GPU.


--------------------

- **Problem**: You're doing coreference resolution, but the documents in your dataset are short; using a batch size of 1 wastes GPU memory.
- **Solution**: We're working on writing a data loader that will handle this for you.

--------------------

- **Problem**: You're doing coreference resolution, and your documents are too long to fit in memory.
- **Solution**: Split the documents as a preprocessing step, run the model, and merge in post-processing. We have a script [normalize.py](../scripts/data/shared/normalize.py) that splits long documents into shorter ones, but it doesn't deal with coref annotations. I'd welcome a PR that does this.


## Multi-dataset training

DyGIE is capable of performing multi-task learning for 4 tasks:
- Named entity recognition (NER)
- Relation extraction
- Event extraction
- Coreference resolution

There may be instances where it is desirable to train different tasks on multiple different datasets - for instance, a coreference resolution model trained on OntoNotes could be used to improve NER predictions on the ACE dataset. It may even be useful to train multiple named entity recognition models sharing the same underlying span representations.

Multi-dataset training with DyGIE is implemented as follows. Each line in the [data](data.md) input to the model must have a `dataset` field. We make the following assumptions:

- The NER, relation, and event label namespaces for different `dataset`s are _disjoint_. A separate model is trained for each dataset.
- The coreference labels for different `dataset`s are _shared_. A single coreference resolution model is trained on all datasets.

As a concrete example: suppose you've decided to train a scientific information extraction model on:

- SciERC (NER, relation, coref)
- GENIA (NER, coref)

The model will create the following label namespaces:

- `scierc__ner`
- `genia__ner`
- `scierc__relation`
- `coref`

Namespaces are named like `[dataset]__[task]`.

A separate module will be created to make predictions for each namespace. All modules will share the same span representations, but will have different task-specific and namespace-specific weights. The model will compute different performance metrics for each namespace, for instance

- `scierc__ner_precision`
- `scierc__ner_recall`
- `scierc__ner_f1`
- `genia__ner_precision`
- `genia__ner_recall`
- `genia__ner_f1`
- etc.

For each task, it will also compute average performance by averaging over the namespaces:

- `MEAN__ner_precision`
- `MEAN__ner_recall`
- `MEAN__ner_f1`

At prediction time, you may request that the model output predictions for all available label namespaces, or only a subset of them (TODO I still need to implement this).
