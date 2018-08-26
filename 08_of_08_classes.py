#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:14:18 2018

@author: clayton
"""
# test

class Ph:
    def __init__(self):
        #Global variable
        self.y = 5
        #local Variable
        z = 7
    def printHam(self):
        print ("Ham")
x = Ph()
x.printHam()
