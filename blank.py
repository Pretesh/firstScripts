index = 0
indent = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)
import time

while True:
    print(' ' * indent[index] + '*****')
    time.sleep(0.2)
    if index == len(indent)-1:
        index = 0
    else:
        index += 1

