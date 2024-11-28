#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:09:50 2023

@author: juliovalenzuela
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas
from scipy.optimize import curve_fit
#import math

#%%

#clear all

#%%
#leer el archivo k_resorte_h
archivo=pandas.read_table(r'R_T.txt',delimiter=' ')

#%%

#datos
x=archivo.values[:,0]#temperatura en ˚C
y=archivo.values[:,1]# R in Ohms

##header
#xlab=x[0]
#ylab=y[0]

#convierte string to number
#x=np.asarray(x[1:],dtype=float)
#y=np.asarray(y[1:],dtype=float)


#%%

#print(x,y)

#grafica datos
fig, (ax)=plt.subplots(1,1)
ax.plot(x,y,'or',label='Datos')

plt.legend()



#%% beta  model

#se crea funcion para ajustar los datos

def funcion(x,R0,b):
    beta=R0*np.exp(b*(1/x-1/25))
    return beta

#condiciones iniciales
#T00 = 23
R00 = 1
b0=1
p0=np.array([R00,b0])

#utilza curve_fit para realizar el ajuste
popt,pcov = curve_fit(funcion,x,y,p0)

#T0=popt[0]
R0=popt[0]
b=popt[1]

#aa=str(popt[0])
#bb=str(popt[1])

#print(T0)
print('R_0 = ' + str(R0))
print('B = ' + str(b))


#%%

T=np.arange(19,50,1)
yaj=funcion(T,*popt)

ax.plot(T,yaj,'k-',label='ajuste')
plt.legend()

plt.xlabel('T (˚C)',size=15)
plt.ylabel('R (Ohm)',size=15)






#print(yaj)

plt.show()

