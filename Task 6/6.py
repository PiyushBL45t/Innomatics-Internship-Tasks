import numpy as np
arr = np.eye(*map(int,input().split()))
arr = str(arr).replace('1',' 1').replace('0',' 0')
print(arr)


