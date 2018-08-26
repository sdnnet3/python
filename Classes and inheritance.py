#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 08:26:45 2018

@author: clayton
Title: Classes and inheritance
Group different objects together sometimes, same attributes based
data attributes and procedural attributes.
use getter method
use setter method

"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return ("animal: %s:%d" %(self.name, self.age))

"""
create new types of animal
"""

class Cat(Animal):
    def speak(self):
        print("meow")
#overwrite __str__ function
    def __str__(self):
        return ("cat: %s:%d" %(self.name, self.age))

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello:")
    def age_diff(self, other):
        diff = self.age - other.age
        print (abs(diff), "year differnce")
    def __str__(self):
        return("person: %s:%d" %(self.name, self.age))