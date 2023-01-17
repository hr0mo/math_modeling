x0 = vx0 * time 
    y0 = vy0 * time 
    alpha = np.arange(0, 2*np.pi, 0.1) 
    x = 12*np.cos(time)+8*np.cos(1.5*time) 
    y = 12*np.sin(time)-8*np.sin(1.5*time) 
    return x, y 
  
def circle_move(X, Y, time): 
    t = t * np.pi / 180 
    X = x *np.cos(time) + y *np.cos(time) 
    Y = y*np.sin(time)+x*np.sin(time) 
    return X, Y 
     
  
edge = 25 
plt.axis('equal') 
ax.set_xlim(-edge, edge) 
ax.set_ylim(-edge, edge) 
  
def animate(i): 
  sta.set_data(circle_move( time=i)) 
    ball.set_data(star_of_future(R=0.5, vx0=0.01, vy0=0.01, time=i)) 
  
ani = animation.FuncAnimation(fig, 
                              animate, 
                              frames=180, 
                              interval=30 
                              ) 
  
ani.save('lec_7_3nomer.gif')