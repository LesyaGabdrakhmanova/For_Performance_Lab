import sys
import math
Centr = []
R = 0
with open(sys.argv[1]) as file:
    for line in file:
        if len(line) > 1:
            try:
                Centr.append(line.split())
            except ValueError:
                sys.exit()
        else:
            R = float(line.rstrip('\n'))
x = []
with open(sys.argv[2]) as file:
    for line in file:
        x.extend(line.split())
Centr_x = [float(coord) for coord in Centr[0]]
x_values = [float(coord) for coord in x]
r = math.sqrt((Centr_x[0] - x_values[0]) ** 2 + (Centr_x[1] - x_values[1]) ** 2)
if R > r:
    print('1')
elif R == r:
    print('0')
else:
    print('2')