import matplotlib.pyplot as plt
import numpy as np

def log_spir(b = 0.1):
    f = np.arange(0, 25, 0.1)
    r = np.e ** (b * f)
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x, y, label='log_spir')
    plt.legend()
    plt.savefig('pic_5.png')

#log_spir()

def arh_spir(k = 0.1):
    f = np.arange(0, 25, 0.1)
    r = k * f 
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x, y, label='arh_spir')
    plt.legend()
    plt.savefig('pic_5.png')

#arh_spir()

def jez_spir(k = 0.1):
    f = np.arange(0, 25, 0.1)
    r = k * f
