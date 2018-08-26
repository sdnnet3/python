"""
Used to create only one of anything
"""

#The long way

class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance

#create instance
x = MySingleton()

#print value in singleton saved as x variable
print (x.y)

#reset the value in singleton to 20
x.y = 20

#create a new variable with singleton, which will only reference original
z = MySingleton()

#should print 20
print (z.y)
