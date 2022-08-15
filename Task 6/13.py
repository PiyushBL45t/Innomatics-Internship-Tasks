import numpy as np

array_1 = np.array(input().split(), int)
array_2 = np.array(input().split(), int)

inner = np.inner(array_1, array_2)
outer = np.outer(array_1, array_2)

print(inner)
print(outer)
