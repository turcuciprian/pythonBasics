import random
import sys
import os

supervillains = {'Fiddler': 'Issac Bowin',
                 'Captain Cold': 'Leonard Snart',
                 'Mirrir Master': 'Sam Scudder',
                 'Pied Piper': 'Thomas Peterson',
                 }

print(supervillains['Captain Cold'])

del supervillains['Captain Cold']

print(supervillains.get('Pied Piper'))

print(supervillains.keys())

print(supervillains.values())
