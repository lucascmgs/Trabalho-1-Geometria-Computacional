import data_structures as dt
import convexhull
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_values(numero_amostras, espalhamento):
    values = []
    for i in range(numero_amostras):
        value = random.random()*espalhamento
        values.append([value])
    return values

points_file = open('nuvem1.txt', 'r') 

lines = points_file.readlines()

points_x = []
points_y = []

for line in lines :
    elements = line.split('  ')
    elements[1] = elements[1].strip()
    points_x.append([float(elements[0])])
    points_y.append([float(elements[1])])


amostras = 400
espalhamento = 1000

#points_x = generate_random_values(amostras, espalhamento)
#points_y = generate_random_values(amostras, espalhamento)


stacked_points = np.column_stack((points_x, points_y))

points = []
for p in stacked_points:
    points.append(dt.Point(p[0], p[1]))

hull_points = convexhull.gift_wrap(points)
hull_x = []
hull_y = []

for p in hull_points:
    hull_x.append(p.x)
    hull_y.append(p.y)
    

plt.scatter(points_x, points_y, marker='.')
plt.plot(hull_x, hull_y, color='red')
plt.show()