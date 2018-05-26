import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)
#начальная точка (исходные координата и скорость)
coord = np.array([5000.,9000.])
velocity = np.array([0.,0.])
#диапазон
def init():
    ax.set_xlim([0., 10000.])
    ax.set_ylim([0., 10000.])
    return circle,

g = 9.8

def newfig(frame):
    # приращение координаты
    coord[1] = coord[1] + velocity[1] - 0.5 * g
    velocity[1] = velocity[1] - g
    if coord[1] <= 0.:
        # упругий удар
        velocity[1] = -velocity[1]
    circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,
"""
def newfig(frame):
    # приращение координаты
    coord[1] = coord[1] + velocity[1] * 0.5
    velocity[1] = velocity[1] - g
    if coord[1] <= 200.:
        #неупругий удар
        coord[1] = 200
        circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,
"""
figure = animation.FuncAnimation(fig, newfig, frames=1000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()