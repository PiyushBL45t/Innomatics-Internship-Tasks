import numpy as np
a, b, c = map(int,input().split())
arr_1 = np.array([input().split() for i in range(a)],int)
arr_2 = np.array([input().split() for j in range(b)],int)
result = np.concatenate((arr_1, arr_2), axis = 0)
print(result)