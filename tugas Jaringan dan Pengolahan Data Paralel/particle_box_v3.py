# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:41:58 2018

@author: imanursar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import uniform
from matplotlib.lines import Line2D

#number of particle
n = 1000

# Create an empty array
x = np.empty(n)
y = np.empty(n)
t = np.empty(n)
g = np.empty(n)
s = np.empty(n)
vx = np.empty(n)
vy = np.empty(n)
k = np.empty(100000)
dt = 0.25
k = 0
s[0] = 0
g[0] = 0

# Random float in [0.0, 1.0)
np.random.seed(19680801)
for i in range(0, n):
    vx[i] = dt*uniform(0,1)
    vy[i] = dt*uniform(0,1)
    x[i] = uniform(0,10)
    y[i] = uniform(0,10)
    t[i] = uniform(0, 2*np.pi)

#set up the plotting area
fig, ax = plt.subplots(figsize=(10, 10))
ax.set(xlim=(-2.5, 22.5), ylim=(-5, 15))
ax2 = fig.add_axes([0.6, 0.3, 0.27, 0.4])
ax2.set(xlim=(0, 1000), ylim=(600, 1300))

#draw lines
line1 = Line2D([-0.12,-0.12], [10.12, 0], linewidth = 3, color = [0,0,0], zorder = 1, transform = ax.transData)
line2 = Line2D([10.12,10.12], [10.12, 0], linewidth = 3, color = [0,0,0], zorder = 1, transform = ax.transData)
line3 = Line2D([-0.12,10.12], [10.1,10.12], linewidth = 3, color = [0,0,0], zorder = 1, transform = ax.transData)
line4 = Line2D([4,-0.12], [-0.12,-0.12 ], linewidth = 3, color = [0,0,0], zorder = 1, transform = ax.transData)
line5 = Line2D([10.12,6], [-0.12,-0.12 ], linewidth = 3, color = [0,0,0], zorder = 1, transform = ax.transData)
#x2,x1 - y2,y1

#display lines
ax.lines.append(line1)
ax.lines.append(line2)
ax.lines.append(line3)
ax.lines.append(line4)
ax.lines.append(line5)

#first draw
scat = ax.scatter(x,y)
scat1 = ax2.scatter(g,s)
#scat1 = ax2.plot(g, s)

#animation
def animate(i):
    global s
    s[i] = s[i-1] + 1
    for j in range(0, n):
        x[j] = round(x[j] + vx[j]*np.cos(t[j]),2)
        y[j] = round(y[j] + vy[j]*np.sin(t[j]),2)

        # bawah kiri
        if (y[j]<=0 and y[j]>=-0.5 and 0<=x[j]<=4):
            y[j] = -(y[j])
            t[j] = -t[j]
        #bawah kanan
        if (y[j]<=0 and y[j]>=-0.5 and 6<=x[j]<=10):
            y[j] = -(y[j])
            t[j] = -t[j]
        #atas
        if (y[j]>10):
            y[j] = y[j] - 2*(y[j]-10)
            t[j] = -t[j]
        #kiri
        if (x[j]<=0 and x[j]>=-0.5 and y[j]>=-0.5):
            x[j] = -(x[j])
            t[j] = t[j] - np.pi
        #kanan
        if (x[j]>10 and y[j]>=-0.5):
            x[j] = x[j] - 2*(x[j]-10)
            t[j] = -t[j] + np.pi

        #count
        if (y[j] < -2.5):
            global k
            y[j] = -999
            k = ((y == -999).sum())#/1000
            ax.set_title('rasio partikel = ' + str(k))

    ax.set_ylabel('Time (s): ' + str(i/5))
    scat.set_offsets(np.c_[x,y])
    global g
    g[i] = n - k
    scat1.set_offsets(np.c_[s[:i], g[:i]])
    #line.set_data(s[:i], g[:i])

anim = FuncAnimation(
    fig, animate, interval=50, frames=len(t)-1)
#anim.save('double_pendulum.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

plt.draw()
plt.show()
