"""

Grassmannian Diffusion Maps
===========================

"""

import sys

import matplotlib.pyplot as plt
import numpy as np

from UQpy.dimension_reduction.diffusion_maps.DiffusionMaps import DiffusionMaps
from UQpy.dimension_reduction.grassmann_manifold import GrassmannOperations
from UQpy.dimension_reduction.grassmann_manifold.projections.SVDProjection import SVDProjection
from UQpy.utilities.kernels import ProjectionKernel

# %%
#
# Create the data
N = 3000
r = 2 * np.random.rand(N)
x = np.zeros((N, 3))
c = np.zeros(N)

phi = np.linspace(0, 2 * np.pi, N)
theta = np.arcsin(np.cos(phi) ** 2)

X = r * np.cos(phi) * np.sin(theta)
Y = r * np.sin(phi) * np.sin(theta)
Z = r * np.cos(theta)

c = X**2 + Y**2 + Z**2

fig = plt.figure()
plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams.update({"font.size": 18})
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X, Y, Z, c=c, cmap=plt.cm.Spectral)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("data")

plt.show()

# %%

# Recast the data into a matrix
data_matrix = np.concatenate([X.reshape(-1, 1), Y.reshape(-1, 1), Z.reshape(-1, 1)], axis=1)

# Convert each data point into a 2d array with shape (1, 3)
data = [data2dArray.reshape(1, -1).T for data2dArray in data_matrix]

# %%
#
# Project each data point onto the Grassmann manifold using SVD. Use only 300 points from the origonal data.
# Select the work with maximum rank (number of planes) from each data point (p=sys.maxsize).
# Use the matrix of left eigenvectors to calculate the kernel (KernelComposition.LEFT).

Grassmann_projection = SVDProjection(data=data[::10], p="max")
psi = Grassmann_projection.u

# %%
#
# Plot the projected data on the Grassmann (3, 1) which is a unit sphere.

Grassmann_data = np.zeros((len(psi), 3))
for i in range(len(psi)):
    Grassmann_data[i, :] = psi[i].data.reshape(1, -1)

fig = plt.figure()
plt.rcParams["figure.figsize"] = (8, 8)
plt.rcParams.update({"font.size": 18})
ax = fig.add_subplot(111, projection="3d")

u, v = np.mgrid[0 : 2 * np.pi : 60j, 0 : np.pi : 60j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
ax.plot_surface(x, y, z, rstride=1, cstride=1, color="c", alpha=0.2, linewidth=0)
ax.scatter(
    Grassmann_data[:, 0],
    Grassmann_data[:, 1],
    Grassmann_data[:, 2],
    c=c[: len(psi)],
    s=3,
    cmap=plt.cm.Spectral,
)
ax.set_title("Grassmann (3, 1)")


plt.show()

# %%
#
# Diffusion maps with Grassmann kernel
kernel = ProjectionKernel()
kernel.calculate_kernel_matrix(psi)


Gdmaps_UQpy = DiffusionMaps(
    alpha=1.0, n_eigenvectors=5, is_sparse=True, n_neighbors=250, kernel_matrix=kernel.kernel_matrix
)

# %%
#
# Plot the first and second eigenvectors
DiffusionMaps._plot_eigen_pairs(
    Gdmaps_UQpy.eigenvectors,
    pair_indices=[1, 2],
    color=Gdmaps_UQpy.eigenvectors[:, 1],
    figure_size=[5, 5],
    font_size=18,
)
DiffusionMaps._plot_eigen_pairs(
    Gdmaps_UQpy.eigenvectors,
    pair_indices=[1, 2],
    color=Gdmaps_UQpy.eigenvectors[:, 2],
    figure_size=[5, 5],
    font_size=18,
)

# %%
