

from scipy.integrate import odeint
import numpy as np
import scipy as sc

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint

def LorenzAttraktor(initialdata=[0.0,1.0,1.01], s=10, r=28, b=2.667):
    def RHS(y,t):
        return np.array([s*(y[1]-y[0]), y[0]*(r-y[2])-y[1],y[0]*y[1] - b*y[2]])
    
    time = np.array([i*10**-2 for i in range(10**4)])
    y = odeint(RHS, initialdata, time)
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.plot(y[:,0], y[:,1], y[:,2], lw=0.5, label = r's = %f, r = %f, b = %f' % (s, r, b))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz Attractor")
    ax.legend()
    plt.show()
