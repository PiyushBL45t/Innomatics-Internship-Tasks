import numpy as np

def arrays(arr):
    arr = np.array(arr)
    float_arr = list(map(float, arr))
    float_arr = float_arr[::-1]
    
    np_float_arr = np.array(float_arr)
    return np_float_arr
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)