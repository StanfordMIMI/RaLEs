We provide details on the data preprocessing for each of the datasets available here.

## Data format

After preprocessing, all the datasets will be formatted like the [SciERC dataset](http://nlp.cs.washington.edu/sciIE/). After downloading the data, you can look at `data/scierc/processed_data/json/train.json` as an example. Each line in the dataset is a JSON representation of a document (technically, the files should be given the `.jsonl` extension since each line is a JSON object, sorry for the confusion).

Each line has (at least some of) the following items:

- `doc_key`: A unique string identifier for the document.
- `sentences`: The senteces in the document, written as a nested list of tokens. For instance,
  ```json
  [
    ["Seattle", "is", "a", "rainy", "city", "."],
    ["Jenny", "Durkan", "is", "the", "city's", "mayor", "."],
    ["She", "was", "elected", "in", "2017", "."]
  ]
  ```
- `ner`: The named entities in the document, written as a nested list - one sublist per sentence. Each list entry is of the form `[start_tok, end_tok, label]`. The `start_tok` and `end_tok` token indices are with respect to the _document_, not the sentence. For instance the entities in the sentence above might be:
  ```json
  [
    [[0, 0, "City"]],
    [[6, 7, "Person"], [9, 10, "City"]],
    [[13, 13, "Person"], [17, 17, "Year"]]
  ]
  ```
  These entity types are just an example; they don't reflect an entity schema for an actual dataset.
- `relations`: The relations in the document, also one sublist per sentence. Each list entry is of the form `[start_tok_1, end_tok_1, start_tok_2, end_tok_2, label]`.
   ```json
   [
     [],
     [[6, 7, 9, 10, "Mayor-Of"]],
     [[13, 13, 17, 17, "Elected-In"]]
   ]
   ```
- `clusters`: The coreference clusters. This is a nested list, but here each sublist gives the spans of each mention in the coreference cluster. Clusters can cross sentence boundaries. For instance, the first cluster in this example is for Seattle and the second is for the mayor.
  ```json
  [
    [
      [0, 0], [9, 10]
    ],
    [
      [6, 7], [13, 13]
    ]
  ]
  ```

The SciERC dataset does not have any event data. To see an example of event data, run the ACE event preprocessing steps described in the [README](README.md) and look at one of the files in `data/ace-event/processed-data`. You will see the following additional field:
- `events`: The events in the document, with one sublist per sentence. An event with `N` arguments will be written as a list of the form `[[trigger_tok, event_type], [start_tok_arg1, end_tok_arg1, arg1_type], [start_tok_arg2, end_tok_arg2, arg2_type], ..., [start_tok_argN, end_tok_argN, argN_type]]`. Note that in ACE, event triggers can only be a single token. For instance,
  ```json
  [
    [],
    [],
    [
      [
        [15, "Peronnel.Election"],
        [13, 13, "Person"],
        [17, 17, "Date"]
      ]
    ]
  ]
  ```
There may also be a `sentence_start` field indicating the token index of the start of each sentence with respect to the document. This can be ignored.

The `Dataset` class in `dygie/data/dataset_readers/data_structures.py` provides some convenience functions to view the annotations. This class isn't "officially supported", but here's an example.

```python
from dygie.data.dataset_readers.data_structures import Dataset

data = Dataset("data/scierc/processed_data/json/train.json")
print(data[0])  # Print the first document.
print(data[0][1].ner)  # Print the named entities in the second sentence of the first document.
```

## SciERC

The [SciERC dataset](http://nlp.cs.washington.edu/sciIE/) contains entity, relation, and coreference annotations for abstracts from computer science research papers.

No preprocessing is required for this data. Run the script `./scripts/data/get_scierc.sh`, and the data will be downloaded and placed in a folder.


## GENIA

The [GENIA dataset](https://orbit.nlm.nih.gov/browse-repository/dataset/human-annotated/83-genia-corpus/visit) contains entity, relation, and event annotations for abstracts from biomedical research papers. Entities can be nested over overlapping. Our preprocessing code converts entity and coreference links to our JSON format. Event shave a complex hierarchical structure, and are left to future work.

To download the GENIA data and preprocess it into the form used in our paper, run the script `./scripts/data/get_genia.sh`.

We followed the preprocessing and train / dev / test split from the [https://gitlab.com/sutd_nlp/overlapping_mentions/tree/master/data/GENIA](SUTD NLP group's) work on overlapping entity mention detection for GENIA. We added some additional scripts to convert their named entity data to our JSON format, and to merge in the GENIA coreference data. Some documents were named slightly differently in the entity and coreference data, and we did our best to stitch the annotations back together.

In GENIA, coreference annotations are labeled one of `IDENT, NONE, RELAT, PRON, APPOS, OTHER, PART-WHOLE, WHOLE-PART`. We preprocess two versions of the data; `json-coref-all` has all coreference annotations, while `json-coref-ident-only` uses only `IDENT` coreferences. We use the `ident-only` version in our experiments.


## ACE

TODO


## WLPC

TODO
