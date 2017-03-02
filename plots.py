
# BEGIN CODE FOR PLOTTING 2D DIAGRAMS

"""
import pylab

"""

"""test = Growth()
for i in range(15): #generate the shape at iteration n
	test.grow()

points = list(test.get_shape()) # get points in shape, store them into x and y coordinates
x_coords = []
y_coords = []
for point in points:
	x_coords.append(point[0])
	y_coords.append(point[1])

pylab.plot(x_coords, y_coords, 'ko') # plot the points colored black

points_edge = list(test.get_edges()) # gets the edge points and stores them into x and y coordiantes
x_coords_edge = []
y_coords_edge = []
for point in points_edge:
	x_coords_edge.append(point[0])
	y_coords_edge.append(point[1])

pylab.plot(x_coords_edge, y_coords_edge, 'ro') # plots the edge points in red





# Plots various lines to outline the nice symmetry properties for X_32

pylab.plot([-33,33],[0,0], 'r')
pylab.plot([0,0],[-33,33], 'r')

pylab.plot([-16,0],[0,16],'r')
pylab.plot([-16,0],[0,-16],'r')
pylab.plot([0,16],[16,0],'r')
pylab.plot([0,16],[-16,0],'r')

pylab.plot([0,16],[0,16],'r')
pylab.plot([0,16],[0,-16],'r')
pylab.plot([16,32],[16,0],'r')
pylab.plot([16,32],[-16,0],'r')

pylab.plot([-16,0],[16,32],'r')
pylab.plot([-16,0],[16,0],'r')
pylab.plot([0,16],[32,16],'r')
pylab.plot([0,16],[0,16],'r')

pylab.plot([-32,-16],[0,16],'r')
pylab.plot([-32,-16],[0,-16],'r')
pylab.plot([-16,0],[16,0],'r')
pylab.plot([-16,0],[-16,0],'r')

pylab.plot([-16,0],[-16,0],'r')
pylab.plot([-16,0],[-16,-32],'r')
pylab.plot([0,16],[0,-16],'r')
pylab.plot([0,16],[-32,-16],'r')"""

pylab.axis([-15, 15, -15, 15]) # creates the axes (with specified lenghts) of the plot
pylab.show() # shows the plot



# END CODE FOR 2D DIAGRAMS



#BEGIN CODE FOR 3D DIAGRAMS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


test = Growth()
for i in range(4): # generate the shape at iteration n
	test.grow()

fig = plt.figure() # initialize the figure
ax = fig.add_subplot(111, projection='3d')


points = list(test.get_shape()) # get a list of the points in X_n

x_coords = []
y_coords = []
z_coords = []
for point in points: # separate the points into three lists of x, y, and z coordinates, respectively
	x_coords.append(point[0])
	y_coords.append(point[1])
	z_coords.append(point[2])

ax.scatter(x_coords, y_coords, z_coords) # makes the scatter plot
plt.show()  # displays the plot






