import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

num_birds = 5
flock = []

def make_flock():
    global flock
    flock = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_birds)]

def distance(point1, point2):
    x_diff = (point2[0] - point1[0]) ** 2
    y_diff = (point2[1] - point1[1]) ** 2
    diff_total = x_diff + y_diff
    distance_final = numpy.sqrt(diff_total)

def move():
    
    


def animate(i):
    #update_flock()
    ax.clear()
    x_vals, y_vals = zip(*flock)
    ax.scatter(x_vals, y_vals)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title('A Flock of Seagulls')

# Initialize the flock
make_flock()

# Create a plot
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Animate the plot
ani = animation.FuncAnimation(fig, animate, frames=200, interval=100, repeat=False)

# Show the plot
plt.show()
