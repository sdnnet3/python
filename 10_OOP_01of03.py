"""
Object oriented programming - Creating a class and and inheriting class


#Create Base Class, with self-like object
class BaseClass(object):
    def printHam(self):
        print('ham')

#create a inheriting class that inherits from BaseClass
class InheritingClass(BaseClass):
    pass

x = InheritingClass()
x.printHam()
"""


"""
Creating a class that controlls inherited classes
"""


#object used in () so that other functions/classes can call the variables
#within this Character class

class Character(object):
    def __init__(self, name):
        self.health = 100
        self.name = name  #Secure name to instance of class
    def printName(self):  #simple function to print out it's own name
        print (self.name)



#InheritingClass, create consturctor __init__, 
class Blacksmith (Character):
    def __init__(self, name, forgeName):
        #name and forgeName are inherited functions
        #super calls from the base class __init__ method
        super(Blacksmith, self).__init__(name)
        self.forge = Forge(forgeName)
        #storing instance of forge class within the blacksmith himself



class Forge:
    def __init__(self, forgeName):
        #pass in the name and attach to this instance of the class
        self.name = forgeName


#create an instance of the blacksmith class
bs = Blacksmith("Bob", "Rick\'s Forge")
print (bs.health)
