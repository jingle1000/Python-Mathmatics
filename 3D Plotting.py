from mpl_toolkits.mplot3d import Axes3D
from matplotlib.tri import Triangulation
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.integrate import ode
import numpy as np
import pandas as pd
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'qt')

'''start in 2d by drawing a basic circle'''

theta = np.linspace(0, 2*np.pi, 40)
#radius
r = np.sqrt(10)
#x and y coordinates
x = r*np.sin(theta)
y = r*np.cos(theta)

#plot the circle
plt.gca().set_aspect('equal')
plt.plot(x, y)
plt.show()


''' creating the cylinder'''

#mesh the data together
Xc, Yc = np.meshgrid(x, theta)
Yc, Zc = np.meshgrid(y, theta)

#plot the "cylinder" aka -> series of vertical lines in a circular pattern
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Xc, Yc, Zc,cmap='viridis', edgecolor='none')
plt.show()
# ax.scatter(x, y, z)

'''Visualizing a Möbius strip'''

theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.5, 0.5, 16)
w, theta = np.meshgrid(w, theta)
phi = 0.5 * theta

# radius in x-y plane
r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))

# triangulate in the underlying parametrization
tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles,
                cmap='viridis', linewidths=0.2)
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
plt.show()

"""Elipsoid"""
fig = plt.figure(figsize=plt.figaspect(1))  # Square figure
ax = fig.add_subplot(111, projection='3d')

coefs = (4, 2, 2)  # Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1 
# Radii corresponding to the coefficients:
rx, ry, rz = 1/np.sqrt(coefs)

# Set of all spherical angles:
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Cartesian coordinates that correspond to the spherical angles:
# (this is the equation of an ellipsoid):
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

# Plot:
ax.plot_surface(x, y, z, cmap="viridis")

# Adjustment of the axes, so that they all have the same span:
max_radius = max(rx, ry, rz)
for axis in 'xyz':
    getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))

plt.show()



