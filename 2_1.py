import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)
coord = np.array([50., 90.])
velocity = np.array([0., 0.])

def init():
    ax.set_xlim([0., 100.])
    ax.set_ylim([0., 100.])
    return circle,

g = 9.8
def Euler(coord,velocity, g):
    coord[1] = coord[1] + velocity[1] * 0.5
    velocity[1] = velocity[1] - g
    return coord

h = 3./6.
def RungeKutta(coord, velocity, h, g):
    k1 = velocity[1]
    k2 = velocity[1] - g
    coord[1] = coord[1] + h * (k1 + k2) * 0.5
    velocity[1] = velocity[1] - 9.8
    return coord

def newfig(frame):

    Euler(coord, velocity, g)
    #RungeKutta(coord, velocity, h, g)

    circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,

figure = animation.FuncAnimation(fig, newfig, frames=1000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()
