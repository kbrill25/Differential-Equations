# -*- coding: utf-8 -*-
"""
First Order Linear Differential Equation Initial Value Problem

Grace Brill
Original Problem
dy/dx + y = e^x
Initial Condition: y(1.0) = 0.1
"""
#import necessary packages
import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#function to calculate the derivative (dy/dx) for the problem
#IMPORTANT: y must come before x in order for function to work with odeint
def dy_dx(y,x):
    dydx = np.exp(x) - y
    return dydx

#variables
xaxis = np.linspace(1.0,5.0)   #derived from initial conditions
yinitial = 0.1  #derived from initial conditions

#determine the yaxis
yaxis = odeint(dy_dx,yinitial,xaxis)

#visualization
plt.plot(xaxis,yaxis)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("dy/dx")
plt.show()

#solve using first order linear ODE methods
#calculate constant based on initial conditions
constant= (2*0.1*math.exp(1))/math.exp(2)

#calculate numerator and denominator to get the actual values
numerator = (np.exp(2*xaxis)) + constant
denominator = 2*np.exp(xaxis)
yval = numerator/denominator

plt.plot(xaxis,yval)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Calculations")
plt.show()

#calculate differences between dy/dx and yval
yhat = yaxis - yval

#graph
plt.plot(xaxis,yaxis,"+",color="red",linewidth=50)   #denote with red + to distinguish
plt.plot(xaxis,yhat,linewidth=0.5)                      #adjust linewidth 
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Comparison of dy/dx to calculations")
plt.show()






    



    