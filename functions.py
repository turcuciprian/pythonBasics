import random
import sys
import os


def addNumber(fNum, lNum):
    sumNum = fNum + lNum

    return sumNum

stringx = addNumber(1,4)
print(stringx)


print('what is your name?')

name = sys.stdin.readline()

print('hello', name)