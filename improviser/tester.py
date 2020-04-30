from nltk.corpus import wordnet as wn
syn = wn.synsets("wagon")
for i in syn:
 print(i.hypernyms())
 print(i.hyponyms())
