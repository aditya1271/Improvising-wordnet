##  Wordnet Improvisation
#### Trying to build a ***tool***( :octocat: ) that can create onotologies and improve wordnet by adding technial terms.

## :question: Questions

#### 1. How wordnet works?
* Lexical Database of semantic relations between words.
* The relations of a word depend on its pos tag for eg. noun , verb etc.
  * So it depends on what words we classify as **concepts** and what are thier **pos tag**

#### 2. How are words related?(So many! :open_mouth:)

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

* I think we will require only nouns and verb :smirk:, but for reference use the following link

:book: **[Documentation](https://wordnet.princeton.edu/documentation/wninput5wn)**

#### :bulb: 3. Which relations are we targetting to improve?
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

* Now evaluate **what types of words are selected by the parser?** :sweat:
 * They are basically nouns.

### 4. Exploring NLTK functions(all of the result in python notebook)
*  **Where is all the data?**
```bash
cd ~/nltk_data/corpora/wordnet
```

### 5. Methodology
* Now since we have every word picked and extracted from wikidata then all of them will be some form of noun.
* So what I am thinking is how would a relation converge into something like is a subclass of , is a word of.
* Python interface to wordnet will be using nltk
* [Relations](https://medium.com/parrot-prediction/dive-into-wordnet-with-nltk-b313c480e788)
### 6. Wordnet working
**[Very good study material](http://santini.se/teaching/sais/Ass1_PeerReviews/NeeleOnSegebladJesper_WordNet_V01.pdf):heart:**
* #### Structure
   * WordNet consists of three separate databases, one for nouns, one for verbs and one for adjectives
and adverbs.

   * ##### Synsets:
      * **Words are stores in the sense in which the appear**
   * The basic structure is synsets. These are **sets of synonyms, or more correct, near-synonyms**, since
there exists none to few true synonyms. Synsets contains a **set of lemmas, and these sets are tagged
with the sense they represent**. These senses can be said to be concepts, all of the lemmas (or words),
can be said to express the same concept. Word forms which have different meanings appear in
different synsets. For example the noun ***bank, has 10 different senses in WordNet, and thus it
appear in 10 different synsets. It also appear as verb in 8 different synsets.***

    * ##### Connection between synsets:
      * Each of these synsets are
also connected in some way to other synsets, expressing some kind of relation
