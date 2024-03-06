# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:17:21 2024

@author: fv-19
"""
import numpy as np

def combGainCalc(T, tau):
    # tau delay time
    # T reverberation time (RT60)
    return 1/(10**((3*tau)/T))

def TCalc(g, tau):
    return 3*tau / np.log10(np.abs(1/g))


def combGainCalcRT60(DelayMs,RT60):
    # calculate the com filters gains accoding to the RT60 rule
    return 10**(-3*DelayMs/RT60)

# tau = np.multiply((46, 37.98, 33.15, 30),1)
tau = np.multiply((16, 11, 7, 1.7),1)
T = 2

def delayLengthSamples(timeMs,R):
    # evaluates the delqylength in samples from a time given in ms and the sample
    # rate R
    return (timeMs/1000)*R

R = 44100 
rt60 = 500
for t in tau : 
    s =  delayLengthSamples(t,R)
    g = combGainCalcRT60(t,rt60)
    print ('s', t, '   g:', g, '\n')
    
for t in tau : 
    g = combGainCalc(rt60,t)
    print ('s', t, '   g:', g, '\n')
    
