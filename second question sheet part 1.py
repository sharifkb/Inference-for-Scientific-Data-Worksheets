# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:00:11 2020

@author: shari
"""
#Packages
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import integrate
import scipy.optimize
mpl.rc('font', family='serif')

####################################      Part 1      ######################################################

#Data from question
n1 = 5

#Normalisation constant
a = lambda s: np.exp(-s)*s**n1/(100*math.factorial(n1))
norm = integrate.quad(a, 0, 100)[0]

#Poisson Distribution    
def fn(s):
    return np.exp(-s)*s**n1/(100*math.factorial(n1))/norm

#Producing the arrays for the plot
s = np.linspace(0,100,num =100001)
y_1 = []
n = 0
while n<len(s):
    y_1.append(fn(s[n])) 
    n+=1

#Finding the mean
b = lambda s: fn(s)*s
mean =  integrate.quad(b, 0, 100)[0]

#Finding the mode
l = lambda s: -fn(s)
max_x = scipy.optimize.fmin(l, 0)[0]

#################################   Incourperating the new data   ##############################################

#Data from question
n2 = 7.7
sig = 0.3

#Normalisation constant
c = lambda s: fn(s)*np.exp(-(s-n2)**2/(2*sig**2))/np.sqrt(2*np.pi*sig**2)
norm2 = integrate.quad(c, 0, 100)[0]

#New Distribution 
def fn2(s):
    return fn(s)*np.exp(-(s-n2)**2/(2*sig**2))/np.sqrt(2*np.pi*sig**2)/norm2

#Producing the arrays for the plot
y_2 = []
n = 0
while n<len(s):
    y_2.append(fn2(s[n])) 
    n+=1
    
#Finding the mean
d = lambda s: fn2(s)*s
mean2 =  integrate.quad(d, 0, 100)[0]

#finding the mode
m = lambda s: -fn2(s)
max_x2 = scipy.optimize.fmin(m, 0)[0]


################################     Plotting the functions     ############################################
p=40
fig1 = plt.figure(figsize=(15,10))

#Q2
plt.plot(s, y_1, label = r"$P(S|n_1)$", color = "red")
plt.vlines(max_x, ymin = 0, ymax = fn(max_x), color = "red", label = r"$Mode_1$ = {}".format(round(max_x, 5)))
plt.vlines(mean, ymin = 0, ymax = fn(mean), color = "red", label = r"$Mean_1$ = {}".format(mean))

#Q3
plt.plot(s, y_2, label = r"$P(S|n_1, n_2)$", color = "black")
plt.vlines(max_x2, ymin = 0, ymax = fn2(max_x2), color = "black", label = r"$Mode_{}$ = {}".format("{1,2}", round(max_x2, 5)))
plt.vlines(mean2, ymin = 0, ymax = fn2(mean2), color = "black", label = r"$Mean_{}$ = {}".format("{1,2}", round(mean2, 5)))

#Formatting
plt.ylim(0, 1.4)
plt.xlim(0, 15)
plt.ylabel("Probability Density", fontsize = p)
plt.xlabel(r"S", fontsize = p)
plt.tick_params(axis='both', which='major', labelsize=p-20)
plt.legend(fontsize = p) 
plt.tight_layout()