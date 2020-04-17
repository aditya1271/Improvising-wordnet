## Wordnet Improvisation
**Trying to build a tool that can create onotologies and improve wordnet by adding technial terms.**

## :question: Questions?

#### 1. How wordnet works?
* Lexical Database of semantic relations between words.
* The relations of a word depend on its pos tag for eg. noun , verb etc.
  * So it depends on what words we classify as **concepts** and what are thier **pos tag**

#### 2. How are words related?

* **For Nouns:**

|       Relations           |
| ------------------------  |
|Antonym                    |
|Holonym                    |
|Meronym                    |
|Attribute                  |
|Derivationally related form|
|Domain of synset-TOPIC     |
|Domain of synset - REGION  |
|Domain of synset - USAGE   |
|Member of this Domain-TOPIC|
|Member of this Domain-REGION|
|Member of this Domain-USAGE|

* **For Verbs:**


| Relations                           |
| ------------------------------------|
|   Antonym                           |
|   Hypernym                          |
|    Hyponym                          |
|    Entailment                       |
|    Cause                            |
|   Also see                          |
|    Verb Group                       |
|    Derivationally related form      |    
|    Domain of synset - TOPIC         |
|    Domain of synset - REGION        |
|    Domain of synset - USAGE         |

* I think we will require only nouns and verb , but for reference use the following link

:book:**[Documentation](https://wordnet.princeton.edu/documentation/wninput5wn)**

#### 3. Which relations are we targetting to improve?
* This depends on the concepts we have formed.
* Our regexParser is the indicative of what words we are selecting to form the Relations.
```python
chunkGram = r"""Chunk:{<JJ.?>{0,2}<VBG>{0,1}<NN.?>{1,2}<VBG>{0,1}<NN..?>{0,2}<VBG>{0,1}}"""
chunkParser = nltk.RegexpParser(chunkGram)
```
* What **relations** are we extracting from ***wikidata***?

|Code |Relations       |
|---- |----------      |
|P279 |is a subclass of|
|P361 |is a part of    |

* Now evaluate **what types of words are selected by the parser?**

#### 4. How can we add relation through python in wordnet?
