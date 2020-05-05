#!/usr/bin/env python3
import re
from tqdm import tqdm
import os
import pickle
import networkx as nx
## Find out if adding duplicate words on the last will work in both the cases.

## make a inteprator that extracts the relevant information of what we want from the line of index2.noun

## make a generator that generates the reuired syntax of command for the file of data2.noun and index2.noun


## 4 cases
# Node exist but child does not exist--> create child , then it can be classified in the below case.
# Node exist , child exist , relationship not exist.
# Node not exist --> then it can be classified into above two cases.

## How to handle each case?
#  look up data in index2.noun file for the required version and can refer in data2.noun according to the offset values
#  desighn the command to be written in data2.noun file and calculate the offset corresponding to that and then write both of them
#  desighn the command to be written in index2.noun file for the node and the child according to their offset and write the file

## First make inteprator and genrator
#wagon n 5 4 @ ~ #p %p 5 2 04543158 03977966 09219858 04543509 02814533
my_dict = { }
current_offset = 15300278;
temp_offset = 0
def offset(str):
    global current_offset
    global temp_offset
    new_offset = 0
    fd = open("/home/manan/Research/Wordnet-Improvisation/improviser/data.txt",'a+')
    fd.write(str)
    fd.write("\n")

    while True:
     try:
      fd.seek(temp_offset)
      byte = fd.read(1)
      if byte == '\n': break
      temp_offset = temp_offset + 1
      new_offset = new_offset +1
     except ValueError:
      break
    temp_offset = temp_offset+1
    new_offset = new_offset+1
    current_offset = current_offset+new_offset
    return current_offset

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
    return string

  def write_command(self):##to be completed
    global current_offset
    command = self.make_command() ## to be made at current_offset
    #current_offset = current_offset + offset(command)
    filename = "/home/manan/nltk_data/corpora/wordnet/index2.noun" ##write
    fd = open(filename,'a+')
    fd.write(command)
    fd.write('\n')

class Data_object:
  def __init__(self, synset_offset , lex_filenum ,ss_type,w_cnt,words_lex_id,p_cnt,ptrs,hifen,definition):
    self.synset_offset = synset_offset
    self.lex_filenum = lex_filenum
    self.ss_type = ss_type
    self.w_cnt = w_cnt
    self.ptrs = ptrs
    self.words_lex_id = words_lex_id
    self.p_cnt = p_cnt
    self.hifen = hifen
    self.definition = definition

  def print(self):
    print("synset_offset : ",self.synset_offset)
    print("lex_filenum :",self.lex_filenum)
    print( "ss_type :",self.ss_type)
    print("w_cnt :",self.w_cnt)
    print("words_lex_id :",self.words_lex_id)
    print("p_cnt :",self.p_cnt)
    print("ptrs :",self.ptrs)
    print("hifen :",self.hifen)
    print("definition : ",self.definition)

  def make_command(self):
    temp_word_list = "";
    for i in self.words_lex_id:
        temp_word_list = temp_word_list + " " + i[0].decode("utf-8") + " " + i[1].decode("utf-8")
    temp_ptrs = "";

    for i in self.ptrs:
        temp_ptrs = temp_ptrs + " " + i[0].decode("utf-8") + " " + i[1].decode("utf-8") + " "+ i[2].decode("utf-8") + " " + i[3].decode("utf-8")
    print(type(self.synset_offset))
    print(type(self.lex_filenum.decode('utf-8')))
    print(type(self.ss_type.decode('utf-8')))
    print(type(self.w_cnt.decode('utf-8')))
    print(type(self.p_cnt))
    print(type(self.hifen.decode('utf-8')))
    print(type(self.hifen.decode('utf-8')))
    print(type(self.definition))

        #print(type(self.synset_offset))

    command = self.synset_offset + " "+ self.lex_filenum.decode('utf-8') +" "+ self.ss_type.decode('utf-8')+" "+self.w_cnt.decode('utf-8')+temp_word_list+" "+self.p_cnt+temp_ptrs+" "+self.hifen.decode('utf-8')+" "+self.definition
    print(command)
    return command

  def write_command(self):
    global current_offset
    #self.synset_offset = string(current_offset)
    command = self.make_command() ## to be made at current_offset
    current_offset = offset(command)
    print("reached")
    filename = "/home/manan/nltk_data/corpora/wordnet/data2.noun" ##write
    openfile = open(filename,'a+')
    openfile.write(command)
    openfile.write('\n')
#test_str_data = "04543158 06 n 02 wagon 0 waggon 0 013 @ 04576211 n 0000 %p 02765028 n 0000 ~ 02787120 n 0000 ~ 02970849 n 0000 ~ 03027505 n 0000 ~ 03122295 n 0000 ~ 03558841 n 0000 ~ 03690600 n 0000 ~ 03765467 n 0000 ~ 04468847 n 0000 %p 04543772 n 0000 ~ 04543924 n 0000 ~ 04563020 n 0000 | any of various kinds of wheeled vehicles drawn by an animal or a tractor"
#04556204 06 n 05 watchband 0 watchstrap 0 wristband 1 watch_bracelet 0 bracelet 1 001 @ 02784218 n 0000 | a band of cloth or leather or metal links attached to a wristwatch and wrapped around the wrist
#04556408 06 n 01 watch_cap 0 001 @ 02954340 n 0000 | a knitted dark blue wool cap worn by seamen in cold or stormy weather



def inteprator_data(offset):
 fd = open("/home/manan/nltk_data/corpora/wordnet/data2.noun",'rb')
 fd.seek(offset)
 str = fd.readline()
 #print(str)
 get_parts = str.split()
 print(get_parts)
 synset_offset = get_parts[0]
 lex_filenum = get_parts[1]
 ss_type = get_parts[2]
 w_cnt = get_parts[3]
 words_lex_id = []
 temp_num = 4
 for i in range(int(w_cnt)):
     words_lex_id.append([get_parts[temp_num],get_parts[temp_num+1]])
     temp_num = temp_num+2
 p_cnt = get_parts[temp_num]
 uptillnow = temp_num
 ptrs = []
 #print(uptillnow)

 print(p_cnt)
 for i in range(int(p_cnt)):
     ptrs.append([get_parts[uptillnow+1],get_parts[uptillnow+2],get_parts[uptillnow+3],get_parts[uptillnow+4]])
     uptillnow = uptillnow+4
 hifen = get_parts[uptillnow+1]
 #print(hifen)
 def_count = len(get_parts) - (uptillnow+1)
 def_count = def_count - 1
 definition = ""
 print(get_parts[uptillnow+2])
 for i in range(def_count):
     definition = definition + " "+ get_parts[i+uptillnow+2].decode("utf-8")
     #print(get_parts[uptillnow+2+i])
 p2 = Data_object(synset_offset , lex_filenum ,ss_type,w_cnt,words_lex_id,p_cnt,ptrs,hifen,definition)
 return p2
 #p2.print()
 #p2.make_command()
 #print(p2.words_lex_id)



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
  file_location = "/home/manan/nltk_data/corpora/wordnet/index2.noun"
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



# Hyponym--->child
#Hypernym ---> parent
##node checking can be done using dict
def node_found_child_found_relationship_not_found(node,child):
    global current_offset
    child_node = my_dict[child]
    print("1")#running
    synset_offset_child = child_node.synset_offset[0]
    print("1")#running
    print(int(synset_offset_child))
    child_data_node = inteprator_data(int(synset_offset_child))
    print("1")#running
    child_data_node.synset_offset = str(current_offset)
    print("1")#running
    child_data_node.p_cnt = str(int(child_data_node.p_cnt)+1)

    print("1")#running
    child_data_node.ptrs.append([b'@',bytes(my_dict[node].synset_offset[0].encode('utf-8')),b'n',b'0000'])
    print("1")#running
    child_data_node.make_command()
    print("1")#running
    child_node.synset_cnt = str(int(child_node.synset_cnt) + 1)
    child_node.sense_cnt = str(int(child_node.sense_cnt)+1)
    child_node.synset_offset.append(str(current_offset))
    print("1")#running
    my_dict[child] = child_node
    print("1")#running
    child_node.make_command()
    print("1")#running
    child_node.write_command()
    print("1")#running
    child_data_node.write_command()
    print("1")
    parent_node = my_dict[node]
    print("1")
    synset_offset = my_dict[node].synset_offset[0]
    print("1")
    parent_data_node = inteprator_data(int(synset_offset))
    parent_data_node.synset_offset = str(current_offset)
    parent_data_node.p_cnt = str(int(parent_data_node.p_cnt)+1)
    parent_data_node.ptrs.append([b'~',(my_dict[child].synset_offset[0]).encode('utf-8'),b'n',b'0000'])
    parent_data_node.make_command()
    parent_node.synset_cnt = str(int(parent_node.synset_cnt) + 1)
    parent_node.sense_cnt = str(int(parent_node.sense_cnt)+1)
    parent_node.synset_offset.append(str(current_offset))
    parent_data_node.write_command()
    parent_node.make_command()
    parent_node.write_command()
    return 0


def node_found_child_not_found(node,child):
    #def __init__(self, synset_offset , lex_filenum ,ss_type,w_cnt,words_lex_id,p_cnt,ptrs,hifen,definition):
    ptrs = ['@', '~']
    offset_list = [str(current_offset)]
    child_index_data  = Index_object(child,'n','1','2',ptrs,'1','2',offset_list)
    #make data and index object
    my_dict[child] = child_index_data
    #command = self.synset_offset + " "+ self.lex_filenum.decode('utf-8') +" "+ self.ss_type.decode('utf-8')+" "+self.w_cnt.decode('utf-8')+temp_word_list+" "+self.p_cnt+temp_ptrs+" "+self.hifen.decode('utf-8')+" "+self.definition
    #string = child + " " + "0"
    wordlist = [[child.encode('utf-8'),b'0']]
    temp_ptrs = []
    child_data = Data_object(str(current_offset),b'06',b'n',b'1',wordlist,'0',temp_ptrs,b'|','custom')
    #write information
    child_data.make_command()
    child_index_data.make_command()
    child_index_data.write_command()
    child_data.write_command()

    #call the previous function
    node_found_child_found_relationship_not_found(node,child)
    print("done")
    return 0


load_file()
dg=nx.DiGraph()

with open("/home/manan/Research/Wordnet-Improvisation/improviser/edgelist.txt",'rb') as f:
    dg = pickle.load(f)
print(dg)
for x in dg.nodes():
   val=nx.predecessor(dg,x)
   for child in val:
     if len(val[child]) != 0:
       parent=val[child][0].replace(" ","_")
       child=child.replace(" ","_")
       if parent in my_dict:
         if child in my_dict:
           node_found_child_found_relationship_not_found(parent,child)
         else:
            node_found_child_not_found(parent,child)
node_found_child_not_found("computer_science","computer_thingy")
node_found_child_found_relationship_not_found("computer_science","artificial_intelligence")
node_found_child_found_relationship_not_found("computer_science","robotics")
node_found_child_found_relationship_not_found("computer_science","data_structure")
