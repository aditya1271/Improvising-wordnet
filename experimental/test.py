from nltk.corpus import wordnet as wn 
from nltk.corpus.reader import CorpusReader
wn.__init__("/wordnet",CorpusReader)
syn = wn.synsets('computer_science')
print(syn)
