import os

def mainFunc():
    for root, directories, files in os.walk('./'):
        for fileName in files:
                print(fileName)


mainFunc()