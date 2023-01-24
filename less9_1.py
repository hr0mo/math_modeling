import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(3, 100, 0.001)

def radio_function(col, t):
    dmdt = k * col
    return dmdt

col = 3

k = 1 / 20

col_t = odeint(radio_function, col, t)

plt.plot(t, col_t[:,0], color = 'Green', label='Размножение Бактерий')
plt.xlabel('разможение, секунды')
plt.ylabel('Функция размножения бактерий')
plt.title('размножение бактерий')
plt.legend()

plt.savefig('Bakterii.png')