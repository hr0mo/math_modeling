import matplotlib.pyplot as plt
import numpy as np
 
def circle_plotter(radius=10):
    
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.arange(-2*radius, 2*radius, 0.1)

    X, Y = np.meshgrid(x, y)
    fxy = (x**2 / a**2) + (y**2 / b**2) = 1

    plt.xlabel('Coord: x') # Подись оси ОХ
    plt.ylabel('Coord: y') # Подпись оси ОУ
    plt.title('circle') # Общая подпись графика
    plt.grid() # Подключение сетки
    plt.contour(X, Y, fxy, levels=[radius**2])
    plt.show()
    plt.savefig('pic_4.png')

circle_plotter()