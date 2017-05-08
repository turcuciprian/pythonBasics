import random
import sys
import os

#
# def addNumber(fNum, lNum):
#     sumNum = fNum + lNum
#
#     return sumNum
#
# stringx = addNumber(1,4)
# print(stringx)
#
#
# print('what is your name?')
#
# name = sys.stdin.readline()
#
# print('hello', name)

longstring = "I'll catch you if you fall - the floor"

print(longstring[0:4]) # first 4 characters
print(longstring[-5:]) # the last 5 characters from a string
print(longstring[:-5]) # everything up to the last 5 characters
print(longstring[:4]+' be there') # concatenating a part of a string with another string
print('%c is my %s letter and my number %d number is %.5f' % ('X','favorite',1,.14))

print(longstring.capitalize())
print(longstring.swapcase())
print(longstring.find('floor'))
print('all characters are letters')
print(longstring.isalpha()) #all string characters are string letters - no spaces or special characters
print('there are numbers in the string')
print(longstring.isalnum()) # if there are only numbers in the string - nothing but numbers

print(len(longstring)) # length of the string
print(longstring.replace("floor",'ceiling')) # replacing strings

print(longstring.strip()) #stripping whitespace
