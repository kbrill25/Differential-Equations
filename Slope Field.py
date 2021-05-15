#another plt.quiver# -*- coding: utf-8 -*-
"""
Slope Fields: Basic Plotting
"""

#import necessary packages
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#x = 2cosx
def fx(x):
    return np.cos(x) * 2

#y = siny
def fy(y):
    return np.sin(y)

#establish ranges for x and y
xrange = np.linspace(-1 * np.pi,np.pi,20)
yrange = np.linspace(-1 * np.pi,np.pi,20)

#utilize meshgrid and get f(x) and f(y)
x,y = np.meshgrid(xrange,yrange)
fofx, fofy = fx(x), fy(y)

#visualization using plt.quiver
plt.quiver(x,y,fofx,fofy)
plt.show()

#improved plt.quiver
magnitude = np.sqrt(fofx**2 + fofy**2)
plt.imshow(magnitude,cmap='winter',extent = (-1 * np.pi,np.pi,-1 * np.pi,np.pi))
plt.quiver(x,y,fofx,fofy,color = 'gray')
plt.show()

#visualization using plt.streamplot
plt.streamplot(x,y,fofx,fofy)
plt.show()

