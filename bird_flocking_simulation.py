import random
import matplotlib.pyplot as plt
from matplotlib import animation

#to consider: alignment (direction of travel: same as neighbors), spacing between individuals, steering to avoid neighbors
    #recursion? useful? necessary?
    
    
##do not directly use boids algorithm

#instantiate 100 "birds" randomly in a 1000x1000 frame
    #save coords to array


#first idea: have a single bird which starts the flocking behavior. choose it at random. 
    # it's travel is not purely brownian (how to code this??...
    # three forward motions, then one to the L or R, three forward etc. what happens if it goes off the screen? come onto the opposite side of the screen.)
    #toggle between moving lead bird, and moving all others in response.
    #for each iteration:
        #move lead bird
        #calculate center of flock (average x value of all birds, average y value of all birds, make coordinate pair.)
        #iteratively move birds one unit in that direction(how to do???)
        
        #when/how to adjust for spacing? how to detect when a bird is too close to another without going through the list/array iteratively?
        #moving a bird further away from one neighbor may put it closer to another.
        
#second idea: birds all move same amount with each iteration



def create_birds():
    x_val_array = []
    y_val_array = []
    birds = []

    while len(x_val_array) < 100:
        i = random.randint(0,101)
        if i not in x_val_array:
            x_val_array.append(i)
    while len(y_val_array) < 100:
        i = random.randint(0,101)
        if i not in y_val_array:
            y_val_array.append(i)
        
    birds = list(zip(x_val_array, y_val_array))   
    
    #print(birds)
    x, y = zip(*birds)
    plt.scatter(x,y)
    plt.show()

create_birds()
    #birds would have to be instantiated randomly. how to render?
    #but how to determine what direction they move in?
    #same potential issue of spacing iteratively
    