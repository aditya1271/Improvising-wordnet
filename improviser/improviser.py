import re
from tqdm import tqdm
import os
## Find out if adding duplicate words on the last will work in both the cases.

## make a inteprator that extracts the relevant information of what we want from the line of index.noun

## make a generator that generates the reuired syntax of command for the file of data.noun and index.noun


## 4 cases
# Node exist but child does not exist--> create child , then it can be classified in the below case.
# Node exist , child exist , relationship not exist.
# Node not exist --> then it can be classified into above two cases.

## How to handle each case?
#  look up data in index.noun file for the required version and can refer in data.noun according to the offset values
#  desighn the command to be written in data.noun file and calculate the offset corresponding to that and then write both of them
#  desighn the command to be written in index.noun file for the node and the child according to their offset and write the file

## First make inteprator and genrator
#wagon n 5 4 @ ~ #p %p 5 2 04543158 03977966 09219858 04543509 02814533
my_dict = { }

class Index_object:
  def __init__(self, word, pos,synset_cnt,p_cnt,ptr_symbol,sense_cnt,tagsense_cnt,synset_offset):
    self.word = word
    self.pos = pos
    self.synset_cnt = synset_cnt
    self.p_cnt = p_cnt
    self.ptr_symbol = ptr_symbol
    self.sense_cnt = sense_cnt
    self.tagsense_cnt = tagsense_cnt
    self.synset_offset = synset_offset

  def print(self):
    print("word : ",self.word)
    print("pos :",self.pos)
    print( "synset_cnt :",self.synset_cnt)
    print("p_cnt :",self.p_cnt)
    print("ptr_symbol :",self.ptr_symbol)
    print("sense_cnt :",self.sense_cnt)
    print("tagsense_cnt :",self.tagsense_cnt)
    print("synset_offset : ",self.synset_offset)

 def make_command(self):
     string = self.word + " " + self.pos + 

def inteprator_index(str):

 get_parts = str.split();
 word = get_parts[0];
 pos = get_parts[1];
 synset_cnt = int(get_parts[2]);
 p_cnt = int(get_parts[3]);
 ptr_symbol = []
 for i in range(p_cnt):
  ptr_symbol.append(get_parts[4+i])

 sense_cnt = get_parts[4+p_cnt]
 tagsense_cnt = get_parts[5+p_cnt]
 synset_offset = []
 for i in range(synset_cnt):
    synset_offset.append(get_parts[6+p_cnt+i])
    #print(get_parts[6+p_cnt+i])
 p2 = Index_object(word, pos,synset_cnt,p_cnt,ptr_symbol,sense_cnt,tagsense_cnt,synset_offset)
 #p2.print();
 my_dict[word] = p2

def load_file():
  file_location = "/home/manan/nltk_data/corpora/wordnet/index.noun"
  total_size = os.path.getsize(file_location)
  print(total_size)
  pbar = tqdm(total = total_size)
  openfile = open(file_location)
  str = " "
  while(str!=""):
   str = openfile.readline()
   pbar.update(len(str))
   if str!="":
    inteprator_index(str)





#str = "wagon n 5 4 @ ~ #p %p 5 2 04543158 03977966 09219858 04543509 02814533"
load_file()
#inteprator_index(str)
##print(my_dict)
