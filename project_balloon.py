import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = '#17EEB3', label = 'Ball')
xdata, ydata = [], []
ax.set_xlim(2, 2*np.pi) 
ax.set_ylim(0, 10)
def update(frame): 
    xdata.append(frame) 
    ydata.append(np.sin(frame)) 
    anim_object.set_data(xdata, ydata) 
    return anim_object,
ani = FuncAnimation(fig, update, frames=np.arange(0,2*np.pi, 0.1), interval = 100) 
ani.save('project.gif')
