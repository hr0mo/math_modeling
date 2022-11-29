import numpy as np
def summa(a):
    b0 = 1
    for i in range(0, len(a), 1):
        b0 = b0 * a[i]
    print(b0)
a = np.array([7, 8, 9, 6])
summa(a)