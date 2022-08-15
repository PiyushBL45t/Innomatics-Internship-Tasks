from numpy import mean
from numpy import var
from numpy import std
import numpy as np


# taking the input for row and column
row, column = map(int, input().split())

# taking the input for array elements
my_arr = np.array([input().split() for i in range(row)],dtype = int)

np.set_printoptions(legacy = '1.12')


# measures of statistic funcitons
average = mean(my_arr,axis=1)
variance = var(my_arr, axis = 0)
standard_deviation = round(std(my_arr), 11)

print(average)
print(variance)
print(standard_deviation)