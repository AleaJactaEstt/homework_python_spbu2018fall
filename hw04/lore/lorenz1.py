from scipy.integrate import odeint
import numpy as np
import scipy as sc

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint

def LorenzAttraktor(initialdata=[0.0,1.0,1.01], s=10, r=28, b=2.667):
    
    n = 10**4
    dt = 10**-2
    x_dots = np.empty(10**4)
    x_dots[0] = initialdata[0]
    
    y_dots = np.empty(10**4)
    y_dots[0] = initialdata[1]
    
    z_dots = np.empty(10**4)
    z_dots[0] = initialdata[2]
    
    for it in range(1, n):
        x_dots[it] =  x_dots[it-1] + dt * s*(y_dots[it-1] - x_dots[it-1])
        y_dots[it] = y_dots[it-1] + dt * (x_dots[it-1]*(r-z_dots[it-1]) - y_dots[it-1]) 
        z_dots[it] = z_dots[it-1] + dt * (x_dots[it-1]*y_dots[it-1]-b*z_dots[it-1])
        
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.plot(x_dots, y_dots, z_dots, lw=0.5, label = r's = %f, r = %f, b = %f' % (s, r, b))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz Attractor")
    ax.legend()
    plt.show()