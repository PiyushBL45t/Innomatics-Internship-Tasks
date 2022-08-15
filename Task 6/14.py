import numpy as np

num_1 = list(map(float,input().split()));
num_2 = int(input())

ployval = np.polyval(num_1, num_2)
print(ployval)
