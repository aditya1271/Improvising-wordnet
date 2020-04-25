#!/usr/bin/env python3
import sys
import os

offset = int(sys.argv[1])
fd = open("/home/manan/nltk_data/corpora/wordnet/data.noun")
fd.seek(offset)
print(fd.readline())

