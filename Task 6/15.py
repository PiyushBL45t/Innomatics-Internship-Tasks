import numpy as np
from numpy.linalg import det

row = int(input())
array = np.array([input().split() for i in range(row)], float)

np.set_printoptions(legacy='1.13')

determinant = det(array)

print(determinant)