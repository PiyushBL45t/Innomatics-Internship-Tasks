import numpy as np

row , column = map(int,input().split())

lista = [list(map(int,input().split())) for i in range(row)]

ar = np.array(lista)

max_val = max(np.min(ar, axis = 1))
print(max_val)



