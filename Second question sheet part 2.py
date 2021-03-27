# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:56:42 2020

@author: shari
"""

#Packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import integrate
import scipy.optimize
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
            
#Data arrays
s10 = np.asarray(s10)
s24 = np.asarray(s24)
s100 = np.asarray(s100)

#Time arrays
t10 = np.arange(10)
t24 = np.arange(24)
t100 = np.arange(100) 

#Distributions
def fn(x):
    return [np.exp(-1/2*i**2)/np.sqrt(2*np.pi) for i in x]

# #####################################################################################   Part b   #############################################################################################

# Finding the odds ratios for models 0,1,2

def z0(s):
    return np.prod(fn([x-B for x in s]))

def z1(s):
    b = lambda L_0: np.prod(fn(s-(B + L_0)))
    return integrate.quad(b, 0, 10)[0]/10
    
def z2(s, t):
    c = lambda A_0, tau: np.prod(fn(s-(B + A_0*np.exp(-t/tau))))
    return integrate.dblquad(c, 0, 100, lambda x: 0, lambda x: 10)[0]/1000

#Odds ratios
n = s100
m = t100

print("O_{} = {}".format({"1,0"}, z1(n)/z0(n)))
print("O_{} = {}".format({"2,0"}, z2(n, m)/z0(n)))
print("O_{} = {}".format({"2,1"}, z2(n, m)/z1(n)))

####################################################################################   Part C i   #############################################################################################

# #Finding P(L_0|D) for Model 1

#Posterior on L_0
def post(s, L):
    return np.prod(fn(s-(B + L)))/(10*z1(s))

L = np.linspace(0, 3, 1000)
PLD10 = []
PLD24 = []
PLD100 = []

for i in range(len(L)):
    PLD10.append(post(s10, L[i]))
    PLD24.append(post(s24, L[i]))
    PLD100.append(post(s100, L[i]))

#Finding the mode corresponding to the best fit of L_0
def mode(s):
    l = lambda L: -post(s, L)
    return scipy.optimize.fmin(l, 0)[0]
    
#Plotting for each dataset
p=40
fig1 = plt.figure(figsize=(15,10))

plt.plot(L, PLD10, label  = "10 hours")
plt.vlines(mode(s10), ymin = 0, ymax = post(s10, mode(s10)), label = r"$L_0 - 10hr$ = {}".format(round(mode(s10), 3)))

plt.plot(L, PLD24, label  = "24 hours")
plt.vlines(mode(s24), ymin = 0, ymax = post(s24, mode(s24)), label = r"$L_0 - 24hr$ = {}".format(round(mode(s24), 3)))

plt.plot(L, PLD100, label  = "100 hours")
plt.vlines(mode(s100), ymin = 0, ymax = post(s100, mode(s100)), label = r"$L_0 - 100hr$ = {}".format(round(mode(s100), 3)))

#Formatting
plt.title(r"Posterior probability distribution on $L_0$ for model 1", fontsize = p)
plt.ylabel(r"$P(L_0|D)$", fontsize = p)
plt.xlabel(r"$L_0$", fontsize = p)
plt.tick_params(axis='both', which='major', labelsize=p-20)
plt.legend(fontsize = p) 
plt.tight_layout()

# ####################################################################################   Part C ii   #############################################################################################

# #Finding P(A_0, tau|D) for Model 2

#Posterior on A_0 and tau
def post2(s, t, A_0, tau):
    return np.prod(fn(s-(B + A_0*np.exp(-t/tau))))/(1000*z2(s, t))

tau = np.linspace(0.1, 200, 1000)
A_0 = np.linspace(0, 2.5, 1000)
PAT10 = np.ndarray((len(tau),len(A_0)))
PAT24 = np.ndarray((len(tau),len(A_0)))
PAT100 = np.ndarray((len(tau),len(A_0)))

n = 0
while n < len(tau):
    m = 0
    while m < len(A_0):
        PAT10[n][m] = post2(s10, t10, A_0[m], tau[n])
        PAT24[n][m] = post2(s24, t24, A_0[m], tau[n])
        PAT100[n][m] = post2(s100, t100, A_0[m], tau[n])
        m+=1
    n+=1
    
# Here, the modal values corresponding to the best fit of A_0 and tau were found using np.argmax(PAT...). Taking the dimensionality of PAT... into consideration allows for the ith and jth 
# element to be found which corresponds to the best fit for A_0 and tau. This was done in the console on the right and the results can be found in the indicies of A_0 and tau in each 
# ax.scatter(....) line. 
# i.e the modal value for for PAT100 was found at the 178520th element, corresponding to the 178520//100 = 178th column (tau[178]) and 178520%1000 th = 520th row (A_0[520])

#Plotting for each dataset    
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 30}
mpl.rc('font', **font)
  
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex = True)

ax1.contour(A_0, tau, PAT10, label  = "10 hours")
ax1.scatter(A_0[450], tau[999], label = r"10 hr: $A_0$ = {}, $\tau$ = {}" .format(round(A_0[450], 3), round(tau[999], 3)), color = "red")
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

########################################################################################   Part d   #############################################################################################

#Plotting the models on the raw data

#Best fit values
L = mode(s100)
A = A_0[520]
tau = tau[178]

m0 = np.full(len(t100), B)
m1 = np.full(len(t100), B+L)
m2 = B + A*np.exp(-t100/tau)

#Plotting for each dataset
p=40
fig1 = plt.figure(figsize=(15,10))

plt.scatter(t100, s100, label  = "100h hour data", color = "k")
plt.errorbar(t100, s100, 1, fmt = "none", ecolor = "k", capsize = 5, elinewidth = 0.5, alpha = 0.3)
plt.plot(t100, m0, label  = "Model 0: L(t) = 5", color = "red", linewidth = 3)
plt.plot(t100, m1, label  = "Model 1, L(t) = 5 + {}".format(round(L, 3)), color = "green", linewidth = 3)
plt.plot(t100, m2, label  = r"Model 2: L(t) = 5 + {} * exp[-t/{}]".format(round(A, 3), round(tau, 3)), color = "blue", linewidth = 3)

#Formatting
plt.ylabel(r"Luminosity / $W$", fontsize = p)
plt.xlabel("time / hr", fontsize = p)
plt.tick_params(axis='both', which='major', labelsize=p-20)
plt.legend(fontsize = p) 
plt.tight_layout()