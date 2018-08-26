from abc import ABCMeta, abstractmethod


class character(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def printName(self):
        print(self.name)

class Blacksmith(character):
    def __init__(self, name, forgeName):
        super(Blacksmith, self).__init__(name)
        self.forge = Forge(forgeName)

class Forge(object):
    def __init__(self, forgeName):
        self.name = forgeName


    
bs = Blacksmith("joe", "Joe\'s Forge")
print(bs.health)

class BaseClass(object):
    __metaclass__= ABCMeta

    @abstractmethod
    def printHam(self):
        pass

class InClass(BaseClass):
    def printHam(self):
        print("ham")

x = InClass()
x.printHam()
# x.BaseClass() doesn't work, because it's a decorator file
