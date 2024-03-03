# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:17:21 2024

@author: fv-19
"""
import numpy as np

def combGainCalc(T, tau):
    return 1/(10**((3*tau)/T))

def TCalc(g, tau):
    return 3*tau / np.log10(np.abs(1/g))

tau = np.multiply((45,38,32,30),1e-3)
T = 2

for t in tau : 
    g = combGainCalc(T, t)
    print (g, '\n')