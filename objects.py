import sys
import random
import os


class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    # getters and setters
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = weight
        self.__weight = weight
        self.__sound = sound

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

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                      self.__height,
                                                                      self.__weight,
                                                                      self.__sound)


cat = Animal('Wiskers', 33, 10, 'miau')
print(cat.toString())


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print('Dog')

    def toString(self):
         return "{} is {} cm tall and {} kilograms and says {} and his owner is {}".format(self.get_name(),
                                                                                           self.get_height(),
                                                                                           self.get_weight(),
                                                                                           self.get_sound(),
                                                                                          self.__owner)

    def multiple_Sounds(self,howMany = None):
        if howMany is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*howMany)

spot = Dog('Spot', 53, 27,'Ruff','Cip')

print(spot.toString())

class AnimalTesting:
    def getType(self,animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.getType(spot)
test_animals.getType(cat)

spot.multiple_Sounds(4)
spot.multiple_Sounds()
