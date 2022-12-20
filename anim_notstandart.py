import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation #модуль анимации

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='#17EEB3', label='Ball')
 
def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha) ** 2
    y = y0 + R*np.sin(alpha) ** 2
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))
ani = FuncAnimation(fig, animate, frames = 100, interval = 30)
ani.save('lec_7_complex_animation.gif')