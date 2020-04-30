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
    temp_ptr_symbols = ""
    temp_sysnet_offset = ""
    for i in self.ptr_symbol:
        temp_ptr_symbols = temp_ptr_symbols + " " + i
    for i in self.synset_offset:
        temp_sysnet_offset = temp_sysnet_offset + " " + i
    string = self.word + " " + self.pos + " " + self.synset_cnt + " " + self.p_cnt + temp_ptr_symbols + " "+ self.sense_cnt + " " + self.tagsense_cnt + temp_sysnet_offset
    print(string)

  def write_command(self):##to be completed
    filename = ""

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
    temp_ptr_symbols = ""
    temp_sysnet_offset = ""
    for i in self.ptr_symbol:
        temp_ptr_symbols = temp_ptr_symbols + " " + i
    for i in self.synset_offset:
        temp_sysnet_offset = temp_sysnet_offset + " " + i
    string = self.word + " " + self.pos + " " + self.synset_cnt + " " + self.p_cnt + temp_ptr_symbols + " "+ self.sense_cnt + " " + self.tagsense_cnt + temp_sysnet_offset
    print(string)

  def write_command(self):##to be completed
    filename = ""



#04543158 06 n 02 wagon 0 waggon 0 013 @ 04576211 n 0000 %p 02765028 n 0000 ~ 02787120 n 0000 ~ 02970849 n 0000 ~ 03027505 n 0000 ~ 03122295 n 0000 ~ 03558841 n 0000 ~ 03690600 n 0000 ~ 03765467 n 0000 ~ 04468847 n 0000 %p 04543772 n 0000 ~ 04543924 n 0000 ~ 04563020 n 0000 | any of various kinds of wheeled vehicles drawn by an animal or a tractor
#04556204 06 n 05 watchband 0 watchstrap 0 wristband 1 watch_bracelet 0 bracelet 1 001 @ 02784218 n 0000 | a band of cloth or leather or metal links attached to a wristwatch and wrapped around the wrist
#04556408 06 n 01 watch_cap 0 001 @ 02954340 n 0000 | a knitted dark blue wool cap worn by seamen in cold or stormy weather

def inteprator_data(offset):
 fd = open("/home/manan/nltk_data/corpora/wordnet/data.noun")
 fd.seek(offset)
 str = fd.readline()
 get_parts = str.split()
 synset_offset = get_parts[0]
 lex_filenum = get_parts[1]
 ss_type = get_parts[2]
 w_cnt = get_parts[3]
 words_lex_id = []
 for i in range(int(w_cnt)):
     words_lex_id.append([get_parts[4+i],get_parts[5+i]])
 p_cnt = get_parts[6+int(w_cnt)]
 uptillnow = 6 + int(w_cnt)
 ptrs = []
 #print(uptillnow)
 #print(get_parts[9])
 #print(p_cnt)
 for i in range(int(p_cnt)):
     ptrs.append([get_parts[uptillnow+1],get_parts[uptillnow+2],get_parts[uptillnow+3],get_parts[uptillnow+4]])
     uptillnow = uptillnow+4
 hifen = get_parts[uptillnow+1]
 def_count = len(get_parts) - (uptillnow+1)
 def_count = def_count - 1
 defination = ""
 for i in range(def_count):
     defination = defination + " "+get_parts[i+uptillnow+2]
 #print(defination)


def inteprator_index(str):

 get_parts = str.split();
 word = get_parts[0];
 pos = get_parts[1];
 synset_cnt = get_parts[2];
 p_cnt = get_parts[3];
 temp_count = 0
 temp_sysnet_count =0
 temp_count = int(p_cnt)
 temp_sysnet_count = int(synset_cnt)
 ptr_symbol = []
 for i in range(temp_count):
  ptr_symbol.append(get_parts[4+i])

 sense_cnt = get_parts[4+temp_count]
 tagsense_cnt = get_parts[5+temp_count]
 synset_offset = []
 for i in range(temp_sysnet_count):
    synset_offset.append(get_parts[6+temp_count+i])
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





test_str = "wagon n 5 4 @ ~ #p %p 5 2 04543158 03977966 09219858 04543509 02814533"
load_file()
my_dict["wagon"].make_command()
print(test_str)
offset = 0
offset = int(my_dict["wagon"].synset_offset[0])
print(offset)
inteprator_data(offset)
##print(my_dict)
