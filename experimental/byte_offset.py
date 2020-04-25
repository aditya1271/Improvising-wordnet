#!/usr/bin/env python3
import sys
import os

offset = int(sys.argv[2])
newline = 1
with open(sys.argv[1]) as fd:
    fd.seek(offset)
    while True:
        try:
            byte = fd.read(1)
            if byte == '\n': newline+=1
            #print(byte)
            offset = offset - 1
            fd.seek(offset)
        except ValueError:
            break
print(newline)
