import sys
import random
import os

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0
# getters and setters

#     name
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    # height
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
    # weight
    def set_weight(self, weight):
        self.__weight = weight
    def get_weight(self):
        return self.__weight
    # sound
    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound