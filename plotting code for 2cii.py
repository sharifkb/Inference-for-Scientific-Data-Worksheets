# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:06:09 2020

@author: shari
"""
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

########################################## Part b ##########################################################

#Data from question

B = 5
dat10= "PAT10.txt"
dat24= "PAT24.txt"
dat100= "PAT100.txt"
            
PAT10 = np.genfromtxt(dat10, dtype=None)
PAT24 = np.genfromtxt(dat24, dtype=None)
PAT100 = np.genfromtxt(dat100, dtype=None)

t10 = np.arange(10)
t24 = np.arange(24)
t100 = np.arange(100) 

########################################## Part c ii ##########################################################

#Finding P(A_0, tau|D) for Model 2

tau = np.linspace(0.1, 200, 1000)
A_0 = np.linspace(0, 2.5, 1000)



font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 30}

mpl.rc('font', **font)
  
p=40
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex = True)

ax1.contour(A_0, tau, PAT10, label  = "10 hours")
ax1.scatter(A_0[450], tau[999], label = r"10 hr: $A_0$ = {}, $\tau$ > {}" .format(round(A_0[450], 3), round(tau[999], 3)), color = "red")
ax1.set_ylabel(r"$\tau$", fontsize = 40.0)
ax1.legend()

ax2.contour(A_0, tau, PAT24, label  = "24 hours")
ax2.scatter(A_0[486], tau[265], label = r"24 hr: $A_0$ = {}, $\tau$ = {}" .format(round(A_0[486], 3), round(tau[265], 3)), color = "red")
ax2.set_ylabel(r"$\tau$", fontsize = 40.0)
ax2.legend()

ax3.contour(A_0, tau, PAT100, label  = "100 hours")
ax3.scatter(A_0[520], tau[178], label = r"100 hr: $A_0$ = {}, $\tau$ = {}" .format(round(A_0[520], 3), round(tau[178], 3)), color = "red")
ax3.set_ylabel(r"$\tau$", fontsize = 40.0)
ax3.set_xlabel(r"$A_0$", fontsize = 40.0)
ax3.legend()

plt.show()
