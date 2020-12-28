import numpy as np
from scipy.linalg import lu 

#matrix = np.array([[3., -1., 2., -1.],
#                   [1., 1., 1., 8.],
#                   [2., 0., 1., 5.]])

matrix = np.array([[7., 2., 0., 24.],
                   [4., 10., 1., 27.],
                   [5., -2., 8., 27.]])

p, l, u = lu(matrix)  # transforming it into a triangular matrix
for i in range(len(u)):  # diagonal to 1
    u[i] -= (1 - 1 / u[i][i]) * u[i]

u[1]=u[1]-u[2]*u[1][2]
u[0]=u[0]-u[2]*u[0][2]
u[0]=u[0]-u[1]*u[0][1]

print(u)

