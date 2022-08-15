import numpy as np

row, column = map(int, input().split())
array = np.array([input().split() for _ in range(row)],int)
summation = np.sum(array, axis = 0)
product = np.prod(summation, axis = 0)


print(product)



