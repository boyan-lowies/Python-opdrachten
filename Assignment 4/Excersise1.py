import numpy as np

a=np.zeros(5)
b =[2,4]
c= np.array([1, 3])   # should be an array
d= np.array([2, 4])   # should be an array

a[b] = [c[0]*d[0],c[1]*d[1]]

print(a)