#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:44:14 2018

@author: clayton
"""

#args, kwargs - unlimited arguments or variables and unlimited keyword arguments


def Func(*args, **kwargs):
    for arg in args:
        print (arg)

l = [1,2,3,4]
Func(*l)
Func(l)