import sys
import os
import random

test_file = open("test.txt",'wb')

print(test_file.mode)

print(test_file.name)


test_file.write(bytes('write me to the file\n','UTF-8'))