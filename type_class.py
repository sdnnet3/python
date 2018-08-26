
class MyClass(object):
    def __init__(self):
        self.x = 5

"""
Example:
TypeClass = type("TypeClass", (), {"x":5})
TypeClass         TypeClass    -   these should be the same
                              (object,) - comma defaults to a tuple
                              (object, BaseClass, etc)
                              
"""

TypeClass = type("TypeClass", (object,), {"x":5})

m = MyClass()
t = TypeClass()

print (t.x, m.x)
