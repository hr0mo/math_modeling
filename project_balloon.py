import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = '#17EEB3', label = 'Ball')
ax.set_xlim([2, 0.04])

scat = ax.scatter(1, 0)
y = np.linspace(2, 0.04) 
def animate(i):
    scat.set_offsets((y[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True, frames=len(y) - 1, interval=50)
ani.save('lec_8_project_animation.gif')