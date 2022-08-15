import numpy as np

row = int(input())

array_1 = np.array([input().split() for i in range(row)], dtype = int)

array_2 = np.array([input().split() for j in range(row)], dtype = int)

# the product of two vecotrs is the dot product
dot_product = np.dot(array_1, array_2)

print(dot_product)