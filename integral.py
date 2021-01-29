from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnchoredText
import numpy as np

def f(x):
    # Example function, enter your own to compute definite integrals for different functions
    return (x**4+4*x**3)

# Divides the interval [a,b] into 2^N rectangles and calculates the total area under the curve
def integera (N, a, b):
    rects = 2**N
    langd = b - a

    baseForN = langd / rects

    area = 0
    
    t = np.arange(a, b, 0.01)
    s = f(t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='x', ylabel='y',
            title='Numerical approximation for the integral of f(x) between a and b')
    ax.grid(alpha=0.3)
    
    for j in range(0, rects):
        d = -1 + (2 * (j + 1))
        midp = a + d * baseForN / 2

        area += baseForN * f(midp)
        rec = patches.Rectangle((a + j * (baseForN), 0), baseForN, f(midp), edgecolor='black', facecolor='r', linewidth=1.5, alpha=0.25)
        ax.add_patch(rec)
        pass
    texts = AnchoredText('Area = ' + str(round(area, 4)), loc=1)
    ax.add_artist(texts)
    fig.savefig("integral.png")
    plt.show()
    return area
# Define your own values of N, a and b in order to compute the desired integral
integera(14,5,10)
