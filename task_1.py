import numpy as np

g = 9.8
x0 = 0
y0 = 3
v0 = 5
alpha = 30 * np.pi / 180
vx0 = v0 * np.cos(alpha)
vy0 = v0 * np.cos(alpha)

t = np.arange(0, 5, 0.1)
x = x0 +vx0 *t
y = y0 + vy0 * t - g * t**2 / 2

coords =np.zeros((len(t), 3))
for i in range (len(t)):
  coords[i, 0] = t[i]
  coords[i, 1] = t[i]
  coords[i, 2] = t[i]

print(coords)