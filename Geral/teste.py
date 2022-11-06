import numpy as np

A = np.arange(24).reshape(4, 6)
print(A)

N = A.max(1) - A.min(1)

print (N)
print(A.min(1))

mini = np.repeat(A.min(1),6).reshape(4, 6)
norma = np.repeat(N,6).reshape(4, 6)

C = (A - mini)/norma

print(C)
