# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:15:52 2020

@author: shari
"""
import numpy as np

x = [1.1, 1.01, 0.99, 0.98, 1, 1.3]
s = [0.05, 0.01, 0.01, 0.01, 0.02, 0.4]

def err(x, s):
    n = 0
    l = []
    g = []
    while n < 6:
        l.append(s[n]**(-2))
        g.append(x[n]/s[n]**2)
        n+=1
        
    p = sum(g)/sum(l)
    m = 1/np.sqrt(sum(l))
    return p,m
    

print(err(x, s))
