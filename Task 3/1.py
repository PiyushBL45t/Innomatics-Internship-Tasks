from cmath import phase
z = input() # take the input for complex number x + jy
absolute_val = abs(complex(z))
phase_val = phase(complex(z))

print(absolute_val)
print(phase_val)