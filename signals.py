# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:12:39 2024

@author: gbulb
"""
import numpy as np
import matplotlib.pyplot as plt

#################################
#Continuous time & Analog Signal#
#################################
t = np.linspace(-0.02, 0.05, 1000)
amp = 325 # Amplitude
f = 50
x_cont = amp * np.sin(2 * np.pi * f * t)
#####################################################################
# Discrete time & Analog Signal - Continuous time & Digital Signal  #
#####################################################################
n = np.arange(50)
dt = 0.07/50
ndT=n*dt
x_disc = np.sin(2 * np.pi * f * n * dt)
##########################
################################
#Discrete time & Digital Signal#
################################
n_ = range(-2, 6, 1)
y_ = []
for i in range(len(n_)):
    temp = (1 if n_[i]>=0 else 0)
    y_.append(temp)
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(t, x_cont, linewidth=3, label='Continuous time Analog Signal')
plt.xlim([-0.02, 0.05])
plt.xlabel('t', fontsize=15)
plt.ylabel('x(t)', fontsize=15)
plt.legend(fontsize=8, loc='lower left')

plt.subplot(2, 2, 2)
plt.stem(ndT,x_disc,label='Continuous time Digital Signal')
plt.xlabel('ndT', fontsize=15)
plt.ylabel('z(ndT)', fontsize=15)
plt.legend(fontsize=8, loc='lower left')

plt.subplot(2, 2, 3)
plt.stem(n, x_disc,label='Discrete time Analog Signal')
plt.xlabel('n', fontsize=15)
plt.ylabel('x(n)', fontsize=15)
plt.legend(fontsize=8, loc='lower left')

plt.subplot(2, 2, 4)
plt.stem(n_, y_,label='Discrete time Digital Signal')
plt.xlabel('n', fontsize=15)
plt.ylabel('y(n)', fontsize=15)
plt.xlim([-2.1, 5.1])
plt.ylim([-0.1, 1.2])
plt.legend(fontsize=8, loc='upper left')
plt.tight_layout()