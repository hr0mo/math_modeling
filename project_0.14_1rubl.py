import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 

fig, ax = plt.subplots() 

anim_object, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []
ax.yaxis.set_major_formatter('₽{x:1.2f}')

ax.yaxis.set_tick_params(which='major', labelcolor='green', labelleft=False, labelright=True)

ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 5) 
 
def update(frame): 
    xdata.append(frame) 
    ydata.append(np.sin(frame)) 
    anim_object.set_data(xdata, ydata) 
    return anim_object,
ani = FuncAnimation(fig, update, frames=np.arange(0,2*np.pi, 0.1), interval = 100)

ani.save('FuncRub.gif')
