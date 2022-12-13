import matplotlib.pyplot as plt
import numpy as np
 
def giperbola_plotter(k=1, title='Giperbola plotter'):
    x = np.arange(0.1, 10, 0.01)
    y = k/x
    x1 = np.arange(-0.1, -10, -0.01)
    y1 = k/x1

    plt.plot(x, y, label='my giperbola')
    plt.plot(x1, y1, label='my giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig('pic_3.png')

giperbola_plotter()