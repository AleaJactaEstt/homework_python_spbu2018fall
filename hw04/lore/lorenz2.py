import numpy as np
import scipy as sc

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint

matplotlib.style.use('ggplot')

def LorenzAttraktor(initialdata=[0.0,1.0,1.01], s=10, r=28, b=2.667):
    '''
    Идея в том, чтобы шагать на маленькую часть(зависит от dt) вектора градиента от начальных данных.
    '''
    def lorenz(x, y, z, s, r, b):
        x_ = s*(y-x)
        y_ = x*(r-z)-y
        z_ = x*y-b*z
        return x_, y_, z_
    
    n = 10**4
    dt = 10**-2
    x_dots = [initialdata[0]]
    y_dots = [initialdata[1]]
    z_dots = [initialdata[2]]
    
    for it in range(n):
        x_curr, y_curr, z_curr = lorenz(x_dots[it], y_dots[it], z_dots[it], s, r, b)
        x_dots.append(x_dots[it] + dt * x_curr)
        y_dots.append(y_dots[it] + dt * y_curr)      
        z_dots.append(z_dots[it] + dt * z_curr)
        
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.plot(x_dots, y_dots, z_dots, lw=0.5, label = r's = %f, r = %f, b = %f' % (s, r, b))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz Attractor")
    ax.legend()
    plt.show()