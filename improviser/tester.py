from nltk.corpus import wordnet as wn
syn = wn.synsets("computer_science")
for i in syn:
 print(i.hypernyms())
 print(i.hyponyms())
