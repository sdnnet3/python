#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:23:39 2018

@author: clayton
"""

def filter_list(l):


    new_l = [x for x in l if isinstance(x, int)]
