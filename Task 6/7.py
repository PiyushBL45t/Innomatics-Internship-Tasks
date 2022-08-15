import numpy as np

n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
addition = a + b
subtraction = a - b
multiplication = a*b
floor_division = a//b
modulus = a % b
power = a**b
print(addition)
print(subtraction)
print(multiplication)
print(floor_division)
print(modulus)
print(power)




