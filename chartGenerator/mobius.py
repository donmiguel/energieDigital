import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri



#====================================================================================
# Generates a möbius strip
# For more informations see here: https://en.wikipedia.org/wiki/M%C3%B6bius_strip
#====================================================================================

def mobius(start=-0.5, stop=-0.5, numSamples1=50, numSamples2=10, colored=True):
	fig = plt.figure()
	cmap = None

	# Make a mesh in the space of parameterisation variables u and v
	# num : Number of samples to generate. Default is 50. Must be non-negative.
	u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=numSamples1)
	v = np.linspace(start, stop, endpoint=True, num=numSamples2)
	u, v = np.meshgrid(u, v)
	u, v = u.flatten(), v.flatten()

	# This is the Mobius mapping, taking a u, v pair and returning an x, y, z
	# triple
	x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
	y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
	z = 0.5 * v * np.sin(u / 2.0)

	# Triangulate parameter space to determine the triangles
	tri = mtri.Triangulation(u, v)

	# Plot the surface.  The triangles in parameter space determine which x, y, z
	# points are connected by an edge.
	ax = fig.add_subplot(111, projection='3d')

	if colored:
		cmap = plt.cm.Spectral

	ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=cmap)
	ax.set_zlim(-1, 1)
	plt.show()