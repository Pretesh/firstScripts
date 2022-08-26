m = []
width = 60
height = 20
alive = "#"
dead = " "
for i in range(width):
    new = []
    for x in range(height):
        new.append(dead)
    m.append(new)
import random

m[random.randint(0, width)][random.randint(0, height)] = alive
for i in enumerate(m):
    try:
        x = i[1].index(alive)
        originW = i[0]
        originH = x
    except:
        continue
adjustment = [0, -1, 1]
for i in range(15):
    m[originW + random.choice(adjustment)][originH + random.choice(adjustment)] = alive

# import numpy as np
# import pandas as pd
# x=pd.DataFrame(m)
# display(x)
'''
hits = ()
positionW = []
positionH = []
for i in enumerate(m):
    numberAlive = i[1].count("#")
    if numberAlive >= 1:
        # x = i[1].index(alive)
        # positionW.append(i[0])
        # positionH.append(x)
        # elif numberAlive > 1:
        hits = (idx for idx, value in enumerate(i[1]) if value == alive)
        for y in hits:
            positionW.append(i[0])
            positionH.append(y)
    else:
        continue
'''
import copy
new = copy.deepcopy(m)
while True:
    for i in range(width):
        for x in range(height):
            counter = 0
            for y in range(-1,2):
                for s in range(-1,2):
                    try:
                        if m[(i+y)%width][(x+s)%height] == alive:
                            counter += 1
                    except:
                        None
            if counter == 3 and m[i][x] != alive:
                new[i][x] = alive
            elif m[i][x] == alive and (counter == 4 or counter == 3):
                new[i][x] == alive
            else:
                new[i][x] = dead
    m = copy.deepcopy(new)
    for y in range(height):
        for x in range(width):
            print(m[x][y], end='')
        print()
    # x=pd.DataFrame(m)
    # display(x)
    input()

