"""
Let's Learn Python #12 - Abstract Classes, Multiple Inheritance - OOP 3 of 3
Abstract base classes and multiple inheritance
"""

from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def printHam(self):
        pass

class InClass(BaseClass):
    def printHam(self):
        print ("ham")

#x = BaseClass() #error
x = InClass()
x.printHam()
