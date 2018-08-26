"""
Let's Learn Python #11 - Overriding & File Mng. - OOP 2 of 3
"""

class BaseClass(object):
    def test(self):
        print ('ham')

class InClass(BaseClass):
    def test(self):
        print ("Hammer Time")

i = InClass()
i.test()
b = BaseClass()
b.test()
