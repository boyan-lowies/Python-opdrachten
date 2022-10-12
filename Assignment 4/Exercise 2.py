import numpy as np

A = np.zeros((5,5))

for i in range(np.size(A,0)):
    for j in range(np.size(A,1)):
        A[i,j] = 1

A = A + 1

for i in range(np.size(A,0)):
    A[i,i] = A[i,i] *2

A += 3*np.identity(5)

A[2,3] += + 4

print(A)