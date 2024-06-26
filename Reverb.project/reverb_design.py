# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:17:21 2024

@author: fv-19
"""
import numpy as np
import matplotlib.pyplot as plt

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
    

def conversion(x, minVal, maxVal):
    diff = (maxVal-minVal)
    print(diff)
    return (minVal + x * diff)

def dBtoLin( x):
    return 10**(2*(x-1))

def quartic2(value):
    value = value - 0.5
    value2 = value * value * 4.0
    value4 = value2 * value2 * 3.0
    value = value4
    return value 


def quartic(value):

    return value*value*value*value

x = np.linspace(0,1,100)

y =  dBtoLin(x)
yquartic = quartic(x)
plt.plot(x,y)
plt.plot(x,yquartic)
plt.show()

# =============================================================================
# Moorer reverb comb and APF structures
# =============================================================================

def oscAPFgainCalc(r,theta,m):
    # r is the decay rate
    # theta is the frequency
    # m is the number of samples between each pulse in the impulse response
    return r**2, -2*(r/1+r**2)*np.cos(theta/m)

def oscComb_gainCalc(r,theta,m):
    # r is the decay rate
    # theta is the frequency
    # m is the number of samples between each pulse in the impulse response
    return 2*r*np.cos(theta/m), -r**2