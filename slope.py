from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnchoredText
import matplotlib.markers as markers
import numpy as np

def f(x):
    return x**2

def derivera (a, h):
    slope = ((f(a + h) - f(a))/h)
    
    t = np.arange(a - 2*h, a+2*h, 0.00001)
    t2 = np.arange(a, a+h, h)
    s = f(t)
    s2 = f(t2)
    fig, ax = plt.subplots()
    ax.plot(t, s,)
    ax.plot([a, a+h], [f(a), f(a+h)], marker='.')
    ax.text(a-0.003,f(a)+0.03, 'a')
    ax.text(a+h-0.003,f(a+h)+0.03, 'h')
    ax.set(xlabel='x', ylabel='y',
            title='Slope approximator for the point a on the curve for the function f(x)')
    ax.grid(alpha=0.3)
    

    # if area<0:
    #     area *= -1
    texts = AnchoredText('Slope = ' + str(round(slope, 4)), loc=1)
    ax.add_artist(texts)
  #  ax.text(0, 0, 'Area = ' + str(round(area, 4)), horizontalalignment='left', verticalalignment='top')
    fig.savefig("slope.png")
    plt.show()
    return slope
derivera(2, 0.001)