from nltk.corpus import wordnet as wn
syn = wn.synsets("chess")
for i in syn:
 print(i.hypernyms())
 print(i.hyponyms())
