import numpy as np

G = np.array([[2,-2,-1],
              [1, 0,-1],
              [1, 4, 1]],
              dtype="d")
I = np.array([[0],
              [12],
              [0]],
              dtype="d" )

inv_G =np.linalg.inv(G)
V = inv_G@I

print(V)