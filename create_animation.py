	
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation #модуль анимации

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], [] # координаты анимации

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У
 
def update(frame): # Функция подстановки координат в объект анимации
    xdata.append(frame) # Рассщет координаты Х
    ydata.append(np.sin(frame)) # Рассщет координаты У
    anim_object.set_data(xdata, ydata) # передача координат
    return anim_object,
ani = FuncAnimation(fig, update, frames=np.arange(0,2*np.pi, 0.1), interval = 100)

ani.save('lec_7_create_animation.gif')
