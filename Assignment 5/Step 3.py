import numpy as np
n = 4                   #nodes
m = 5                   #branches
lines = np.array([[0, 1],
                  [0, 2],
                  [0, 3],
                  [1, 2],
                  [1, 3]])
gen = np.array([0, 1])
ld = np.array([3])

Gp   = np.array([0.3,0.4,0.3,0.4,0.2])[:,np.newaxis] # 2D array of shape (5,1)
I_ld = np.array([[6]]); # 2D array of shape (1,1)
Vs   = np.array([380, 200])[:,np.newaxis] # 2D array of shape (2,1)
Rs   = np.array([5, 4])[:,np.newaxis] # 2D array of shape (2,1)

def make_I(n, ld, gen, I_ld, Vs, Rs):
    I = np.zeros([n, 1])
    I[gen] = Vs[np.where(gen == gen)] / Rs[np.where(gen == gen)]
    I[ld] = I_ld[np.where(ld == ld)]
    return(I)

def make_G(n, gen, lines, Gp):
    G = np.zeros([n, n])
    for x in gen:
        G[x,x] += 1 / Rs[np.where(gen == x)]
    
    for y in range(len(lines)):
        p1 = lines[y][0]
        p2 = lines[y][1]
        G[p1,p1] += Gp[y]
        G[p2,p2] += Gp[y]
        G[p1,p2] -= Gp[y]
        G[p2,p1] -= Gp[y]
    return G


I = make_I(n, ld, gen, I_ld, Vs, Rs)
G = make_G(n, gen, lines, Gp)
inv_G = np.linalg.inv(G)
V = inv_G@I
print(V)