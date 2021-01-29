from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnchoredText
import numpy as np

def f(x):
    return (x**4+4*x**3)

def integera (N, a, b):
    rects = 2**N
    langd = b - a
    #print('längd: ' + str(langd))
    baseForN = langd / rects

    #print('bas: ' + str(baseForN))
    area = 0
    # for c in range(0, rects):
    #     d = -1 + (2 * (c + 1))
    #     midp = (c + 1) * baseForN / 2
    # #    print('midpoint = ' + str(midp))
    #     vall = baseForN * (f(midp))
    # #    print('vall= ' + str(vall))
    #     area += vall
    
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
    # if area<0:
    #     area *= -1
    texts = AnchoredText('Area = ' + str(round(area, 4)), loc=1)
    ax.add_artist(texts)
  #  ax.text(0, 0, 'Area = ' + str(round(area, 4)), horizontalalignment='left', verticalalignment='top')
    fig.savefig("integral.png")
    plt.show()
    return area
integera(14,5,10)