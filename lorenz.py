# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:22:37 2021

@author: grace
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

def lorenz(COMBINED, t, sigma, beta, rho):
    
    #get x, y, and z
    x,y,z = COMBINED
    
    #calculate dxdt, dydt, and dzdt
    dxdt = sigma * (y-x)
    dydt = (-x*z) + (rho * x) - y
    dzdt = (x*y) - (beta*z)
    
    #return dxdt, dydt, and dzdt
    return dxdt, dydt, dzdt

#initial conditions
x0 = 1.0
y0 = 1.0
z0 = 1.0

#constants
sigma = 10.0
beta = 2.667
rho = 28.0

#create XYZ variable
XYZ = x0,y0,z0

#create time
t = np.linspace(0,50,1500)

#utilize odeint
solution = odeint(lorenz, XYZ, t, args = (sigma,beta,rho))

#get xsol, ysol, and zsol from solution
xsol, ysol, zsol = solution.T

fig = plt.figure(figsize=(10,10))
fig.patch.set_visible(False)
ax = plt.axes(projection='3d')
ax.set_facecolor('black')

s = 10

cmap = plt.cm.plasma
for i in range(0,1500-s,s):
    xslice = xsol[i:i+s+1]
    yslice = ysol[i:i+s+1]
    zslice = zsol[i:i+s+1]
    
    ax.plot(xslice, yslice, zslice, color = cmap(i/1500), alpha = 0.6)

#just view the curve
ax.set_axis_off()
