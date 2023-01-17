import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
 
fig, ax = plt.subplots() 
babock, = plt.plot([], [], '-', color= 'DeepPink', label = 'Butr') 

def babock_move(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5) 
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5) 
    return x, y 

plt.axis('equal') 
ax.set_xlim(-5, 5) 
ax.set_ylim(-5, 5) 
 
x = []
y = []

def animate(i): 
    x.append(babock_move(t = i)[0])
    x.append(babock_move(t = i)[1])
    babock.set_data(x, y) 

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0.1, 2*np.pi, 0.1), interval= 30) 
 
ani.save('lec7_task3_1.gif') 
 
# fig, ax = plt.subplots() 
# serd, = plt.plot([], [], 'o', color='DeepPink') 
 
# def serd_move2(t): 
#     x = 16 * np.sin(t)**3 
#     y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t) 
#     return x, y 
 
# plt.axis('equal') 
# ax.set_xlim(-20, 20) 
# ax.set_ylim(-20, 20) 
 
# def animate2(i): 
#     serd.set_data(serd_move2(t = np.arange(0, 2*np.pi, 0.01))) 
     
# ani = animation.FuncAnimation(fig, animate2, frames= 100, interval=30) 
# ani.save('lec7_task3_2.gif')