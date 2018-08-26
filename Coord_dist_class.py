#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:10:46 2018

@author: clayton
"""

class Coord(object):
    def __init__(self, x, y):    
        self.x = x
        self.y = y
        
    def distance(self, other):
        xdist = (self.x - other.x)**2
        ydist = (self.y - other.y)**2
        dist = (xdist + ydist)**(0.5)
        return (dist)
    
    def __str__(self):
        return ("<%d,%d>" %(self.x, self.y))
    
c = Coord(3,4)
zero = Coord(0,0)

"""
print(c.distance(zero))
is the same as
print(Coord.distance(c,zero))
"""

