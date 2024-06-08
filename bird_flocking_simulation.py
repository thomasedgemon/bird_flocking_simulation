import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

width, height = 250, 250

def wrap_around(point, width, height):
    x, y = point
    x = x % width
    y = y % height
    return [x, y]

leader_weight = 1
cohesion_weight = 1
alignment_weight = 1

num_birds = 20
# Make leader
leader = [(random.randint(25, 75), random.randint(25, 75))]
leader_angle = np.random.rand() * 2 * np.pi  # Initial random direction for the leader

# Make flock
flock = [(random.randint(0, 250), random.randint(0, 250)) for _ in range(num_birds)]

def distance_and_angle(point1, point2):
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]
    angle_radians = math.atan2(delta_y, delta_x)
    return np.linalg.norm(np.array(point2) - np.array(point1)), angle_radians

def move_bird(distance=1):
    for i in range(len(flock)):
        total_dx, total_dy = 0, 0
        for j in range(len(flock)):
            if i != j:
                dist, angle = distance_and_angle(flock[i], flock[j])
                if dist < 5:
                    opposite_angle = angle + math.pi
                    total_dx += math.cos(opposite_angle)
                    total_dy += math.sin(opposite_angle)
                else:
                    total_dx += math.cos(angle)
                    total_dy += math.sin(angle)
        
        # Move towards the leader
        dist_to_leader, angle_to_leader = distance_and_angle(flock[i], leader[0])
        total_dx += leader_weight * math.cos(angle_to_leader)
        total_dy += leader_weight * math.sin(angle_to_leader)
        
        new_x = flock[i][0] + distance * total_dx
        new_y = flock[i][1] + distance * total_dy
        flock[i] = wrap_around((new_x, new_y), width, height)

# Move lead bird, but restrict to being generally forward via angle limit
def move_leader():
    global leader_angle
    move_increment = 2.0 
    angle_limit = np.pi / 6  # Limit to 30 degrees change in direction
    angle_change = (np.random.rand() - 0.5) * angle_limit
    leader_angle += angle_change
    
    new_x = leader[0][0] + move_increment * math.cos(leader_angle)
    new_y = leader[0][1] + move_increment * math.sin(leader_angle)
    leader[0] = wrap_around((new_x, new_y), width, height)

# Initialize plot
fig, ax = plt.subplots()
scat = ax.scatter([x[0] for x in flock], [x[1] for x in flock], c='blue')
scat_leader = ax.scatter([leader[0][0]], [leader[0][1]], c='red')

def animate(frame):
    move_leader()
    move_bird()
    scat.set_offsets(flock)
    scat_leader.set_offsets([leader[0]])

ani = animation.FuncAnimation(fig, animate, frames=200, interval=100)
plt.xlim(0, width)
plt.ylim(0, height)
plt.show()
