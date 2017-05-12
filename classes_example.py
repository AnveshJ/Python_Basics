import random
import sys
import os

# remmeber : and indenting is a must in python for loops and if/else statements and for codnitions also.
# __ means private Object
class Animal:
	__name = ""
	__height = ""
	__weight = ""

	def set_name(self,name):
		self.__name = name

	def get_name(self):
		return self.__name

	def details(self):
		return "{} is {} tall and weighs {}".format(self.__name, self.__height, self.__weight)

	def __init__(self, name, height, wieght):
		self.__name = name
		self.__height = height
		self.__weight = wieght

	def get_type(self):
		print("Animal")

	
cat = Animal("Hi", 33, 10)



class Dog(Animal):
	__owner = ""

	def __init__(self, name,height,weight,owner):
		self.__owner = owner
		self.__name = name
		self.__height = height
		self.__weight = weight

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dog")

	def toString(self):
		return "{} is {} tall and weighs {} of {}".format(self.__name, self.__height, self.__weight, self.__owner)

	def multiple_sounds(self, how_many=None):
		if how_main is None:
			print(self.get_sound())
		else :
			print(self.get_sound()*how_many)

spot = Dog("Spot", 53, 26, "Derek")



class Animaltesting:
	def get_type(self, animal):
		animal.get_type()

test_animals = Animaltesting()

test_animals.get_type(cat)
test_animals.get_type(spot)