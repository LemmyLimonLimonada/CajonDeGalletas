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
ax.plot(y,x,'or',label='Datos')

plt.legend()



#%% beta  model

#se crea funcion para ajustar los datos

def funcion(x,A,B,C):
    cubic=1/(A+B*np.log(x)+C*(np.log(x))**3)
    return cubic

#condiciones iniciales
#T00 = 23
A0=1
B0=1
C0=1
p0=np.array([A0,B0,C0])

#utilza curve_fit para realizar el ajuste
popt,pcov = curve_fit(funcion,y,x,p0, maxfev=10000)

A=popt[0]
B=popt[1]
C=popt[2]

#aa=str(popt[0])
#bb=str(popt[1])

print('A = ' + str(A))
print('B = ' + str(B))
print('C = ' + str(C))


#%%

R=np.arange(1000,10000,100)
yaj=funcion(R,*popt)

ax.plot(R,yaj,'k-',label='ajuste')
plt.legend()

plt.ylabel('T (˚C)',size=15)
plt.xlabel('R (Ohm)',size=15)






#print(yaj)

plt.show()

