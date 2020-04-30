#!/usr/bin/env python3
import sys
import os

offset = 0
fd = open("/home/manan/Research/Wordnet-Improvisation/experimental/input.txt")
while True:
 try:
  fd.seek(offset)
  byte = fd.read(1)
  if byte == '\n': break  
  offset = offset + 1   
 except ValueError:
   break
print(offset)


