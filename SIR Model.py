# -*- coding: utf-8 -*-
"""
Grace Brill
SIR Model for Epidemiology
"""
#import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def SIR(yvector, t, N, b, k, s):
    st, it, rt, et = yvector
    
    #calculate dSdt
    dSdt = -1 * (b * st * it)
    
    #calculate dEdt
    dEdt = b * st * it - (s*et)
    
    #calculate dIdt
    dIdt = (s*et) - (k * it)
    
    #calculate dRdt
    dRdt = k * it
    
    return dSdt, dIdt, dRdt, dEdt


def graphSIR(s,i,r,t,N):
    plt.plot(t,infected, label = 'Infectious')
    plt.plot(t,susceptible, label = 'Susceptible')
    plt.plot(recovered, label = 'Recovered')
    plt.plot(exposed, label = 'Exposed')
    plt.xlabel("Time (in days)")
    plt.ylabel("Number of People")
    plt.title("SEIR Model")
    plt.legend()
    plt.show()


#N represents population size
N = 100

#I0 represents initial number of infected
I0 = 1

#R0 represents initial number of recovered
R0 = 0

#E0 represents the initial number of exposed
E0 = 0

#S0 represents initial number of susceptible
S0 = N -I0 - R0 - E0

#constants
b = 0.33
k = 0.1
s = 0.2

#initial conditions
Y0 = S0, I0, R0, E0

#variable for time (1 year)
timeDays = np.linspace(0,16,16)

#integrate using the odeint
solution = odeint(SIR, Y0, timeDays, args=(N,b,k,s))

#get data for each from sol
susceptible, infected, recovered, exposed = solution.T

#call graphing function
graphSIR(susceptible, infected, recovered, timeDays,N)





