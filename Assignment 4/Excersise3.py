import numpy as np
B = np.array([
 [ 0,  5,  0, -1,  5],
 [ 0,  3, -3,  3, -1],
 [ 0, -2,  2,  4,  5],
 [-3,  6, 0,  3,  1]],
 dtype="d")

C = np.mean(B,1)

for i in range(np.size(B,0)):
    B[i] = B[i] - C[i]

for i in range(np.size(B,0)):
    for j in range(np.size(B,1)):
        if B[i,j] < 0:
            B[i,j] = 0


print(B)