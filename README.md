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
|Antonym                :heavy_check_mark:    |
|Holonym                :heavy_check_mark:    |
|Meronym                :heavy_check_mark:    |
|Attribute                  |
|Derivationally related form|
|Domain of synset-TOPIC    :heavy_check_mark: |
|Domain of synset - REGION :heavy_check_mark: |
|Domain of synset - USAGE  :heavy_check_mark:|
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
* Domain relations are not usefull to us , see this link **[Domans List](http://wndomains.fbk.eu/labels.html)**

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


### 7. How to add data locally.
 * All of the data is stored in ```data.noun``` file, understand how to read and process it and what does is indicate
 * it is basically sysnet id

 * #### Code to acess the word through sysnet id
    ![offset_id](offsetid.png)

```python
 from nltk.corpus import wordnet as wn
 wn.synset_from_pos_and_offset('n',4543158)
```
  * now think of doing the opposite work
###  8. Work left
  [wndb :heart:](https://wordnet.princeton.edu/documentation/wndb5wn)
  * id calculate :question:
    * calculate using the formula:
      **for the word "wagon"**


|lemma | pos  | synset_cnt | p_cnt | [ptr_symbol..]|sense_cnt|tagsense_cnt|synset_offset|  
|------|------|------------|-------|---------------|---------|------------|-------------|
|wagon | n    | 5          |4      |@ ~ #p %p      |5        |2           |04543158 03977966 09219858 04543509 02814533|

* ### How are the terms defined in index.noun file?
   * **synset_cnt :**
Number of synsets that lemma is in. This is the number of senses of the word in WordNet.

  * **p_cnt :**
   Number of different pointers that lemma has in all synsets containing it.
  * **synset_offset :**
Byte offset in data.pos file of a synset containing lemma . Each synset_offset in the list corresponds to a different sense of lemma in WordNet.
  * **sense_cnt :**
Same as sense_cnt above. This is redundant, but the field was preserved for compatibility reasons.
  * **ptr_symbol :**
A space separated list of p_cnt different types of pointers that lemma has in all synsets containing it.

  * **tagsense_cnt :**
Number of senses of lemma that are ranked according to their frequency of occurrence in semantic concordance texts.

* ### How are terms stored in data.noun file?
|synset_offset | lex_filenum |  ss_type | w_cnt | word | lex_id |[word  lex_id...]|p_cnt[ptr...][frames...]| gloss|
|------------- |-------------|----------|-------|------|--------|-----------------|------------------------|------|
|04543158| 06 |n |02 |wagon 0 waggon 0 013 @ 04576211 n 0000 %p 02765028 n 0000 ~ 02787120 n 0000 ~ 02970849 n 0000 ~ 03027505 n 0000 ~ 03122295 n 0000 ~ 03558841 n 0000 ~ 03690600 n 0000 ~ 03765467 n 0000 ~ 04468847 n 0000 %p 04543772 n 0000 ~ 04543924 n 0000 ~ 04563020 n 0000 | any of various kinds of wheeled vehicles drawn by an animal or a tractor

* linking new id :question:
    * add the id in the index.noun file and then add the relation in data.noun

* convert this data into db and then query using sql ?

* wikidata read and add ...
