import sys
import os
import random

test_file = open("test.txt",'wb')

print(test_file.mode)

print(test_file.name)


test_file.write(bytes('write me to the file\n','UTF-8'))

test_file.close()

test_file.open('text.txt','r+') # read and write

textInFile = test_file.read()

print(textInFile)

os.remove(test_file) #deleteing the file