import numpy as np
def make_random_circuit(sn):
    np.random.seed(sn) 
    n = 10;         # number of nodes
    m = 14;         # number of edges
    ni = 4;         # number of current sources
    nv = 2;         # number of voltage sources
    Gpmin = 0.1;    # minimum value for line conductance
    Gpmax = 0.5;    # maximum value for line conductance
    I_ldmin = 1;    # minimum value of current source
    I_ldmax = 25;   # maximum value of current source
    Vsmin = 100;    # minimum value of voltage source
    Vsmax = 400;    # maximum value of voltage source
    Rsmin = 1;      # minimum internal resistance of voltage source
    Rsmax = 9;      # minimum internal resistance of voltage source

    Gp = Gpmin + (Gpmax-Gpmin)*np.random.rand(m,1);

    s = np.random.permutation(n);
    ld = s[0:ni];
    gen = s[ni:ni+nv];

    I_ld = I_ldmin + (I_ldmax-I_ldmin)*np.random.rand(ni,1);

    Vs = Vsmin + (Vsmax-Vsmin)*np.random.rand(nv,1);

    Rs = Rsmin + (Rsmax-Rsmin)*np.random.rand(nv,1);

    all_lines=[]
    for i in range(n):
        for j in range(i+1,n):
            all_lines.append([i,j])
    np.random.shuffle(all_lines)
    lines=np.asarray(all_lines[:m]) 
    return n,m,ld, gen, lines, Gp, I_ld, Vs, Rs
def find_node_voltages(n,m,ld, gen, lines, Gp, I_ld, Vs, Rs):
    
    I = np.zeros([n, 1])
    I[gen] = Vs[np.where(gen == gen)] / Rs[np.where(gen == gen)]
    I[ld] = I_ld[np.where(ld == ld)]

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
    

    inv_G = np.linalg.inv(G)
    V = inv_G@I
    return V

sn= 51
n,m,ld, gen, lines, Gp, I_ld, Vs, Rs = make_random_circuit(sn)


V = find_node_voltages(n,m,ld,gen,lines,Gp,I_ld, Vs, Rs)

print(gen, ld)
