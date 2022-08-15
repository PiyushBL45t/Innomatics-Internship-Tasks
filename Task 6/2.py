import numpy as np


def change_shape(array):
    reshaped_arr = array.reshape(3,3)
    print(reshaped_arr)
    

array = np.array(input().split(),int)
change_shape(array)