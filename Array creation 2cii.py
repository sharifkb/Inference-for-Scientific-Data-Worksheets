# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:55:45 2020

@author: shari
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:56:42 2020

@author: shari
"""

#Packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font', family='serif')

#Data from question
B = 5
dat10= "data_10hr.txt"
dat24= "data_24hr.txt"
dat100= "data_100hr.txt"

s10 = []
s24 = []
s100 = []
with open(dat10, 'r') as f:
    for line in f:
        if line:
            s10.append(float(line.strip()))

with open(dat24, 'r') as f:
    for line in f:
        if line:
            s24.append(float(line.strip()))
            
with open(dat100, 'r') as f:
    for line in f:
        if line:
            s100.append(float(line.strip()))
            
s10 = np.asarray(s10)
s24 = np.asarray(s24)
s100 = np.asarray(s100)

t10 = np.arange(10)
t24 = np.arange(24)
t100 = np.arange(100) 

########################################## Part c ii ##########################################################

#Finding P(A_0, tau|D) for Model 2

tau = np.linspace(0.1, 200, 1000)
A_0 = np.linspace(0, 2.5, 1000)

PAT10 = np.ndarray((len(tau),len(A_0)))
PAT24 = np.ndarray((len(tau),len(A_0)))
PAT100 = np.ndarray((len(tau),len(A_0)))

n = 0
while n < len(tau):
    m = 0
    while m < len(A_0):
        PAT10[n][m] = np.prod([np.exp(-1/2*i**2)/np.sqrt(2*np.pi) for i in s10-(B + A_0[m]*np.exp(-t10/tau[n]))])/(1000*1.7543147682951875*10**(-7))
        PAT24[n][m] = np.prod([np.exp(-1/2*i**2)/np.sqrt(2*np.pi) for i in s24-(B + A_0[m]*np.exp(-t24/tau[n]))])/(1000*3.1948672152518007*10**(-15))
        PAT100[n][m] = np.prod([np.exp(-1/2*i**2)/np.sqrt(2*np.pi) for i in s100-(B + A_0[m]*np.exp(-t100/tau[n]))])/(1000*2.605132350097278*10**(-63))
        m+=1
    n+=1

np.savetxt("PAT10.txt", PAT10)
np.savetxt("PAT24.txt", PAT24)
np.savetxt("PAT100.txt", PAT100)
