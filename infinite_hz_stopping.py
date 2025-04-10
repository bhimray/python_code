import numpy as np
import matplotlib.pyplot as plt

P = np.array(([1/4, 1/4, 1/4, 1/4], #interior
             [0, 1/3, 1/3, 1/3], #left
             [1/3, 0, 1/3, 1/3], #top
             [1/3, 1/3, 0, 1/3], #right
             [1/3, 1/3, 1/3, 0]) #bottom
             );
p_side = np.array(([1/3, 1/3, 1/3])) #bottom
p_corner = np.array(([1/2, 1/2])) #each corner
p_interior = np.array(([1/4, 1/4, 1/4, 1/4])) # interior

n = 20; #state 1D 
m = 2; # input space

#stage cost
g = np.zeros((n, n, m));
J = np.zeros((n, n));
pistart = np.zeros((n, n));

#initialize
X = np.zeros((n, n));
g_stop_coord = {(5, 5): -120, (17, 10):-70, (10, 15): -150}; #defined stage cost over coordinates
for coord, sc in g_stop_coord.items():
    g[coord[0], coord[1], 1] = sc; # stopping cost
    X[coord[0], coord[1]] = 1; #target state

g[:, :, 1] = 1; #waiting cost

t = 0; # number of iteration
J_next = np.random.random((n, n))
# dp for infinite horizon problem
while np.abs(J_next - J).all > np.exp(-5):
    t = t+1
    J = J_next
    for i in range(n):
        for j in range(n):
            for u in range(m): # 0 WAIT and 1 STOP
                if i == 0 and j > 0 and j < n-1: #bottom
                    J_next[i, j] = g[i, j, u] + p_side @ np.array([J[i, j-1], J[i+1, j], J[i, j+1]])
                elif j == 0 and i > 0 and i < n-1: #left
                    J_next[i, j] = g[i, j, u] + p_side @ np.array([J[i+1, j], J[i, j+1], J[i-1, j]])
                elif j > 0 and j < n-1 and i == n-1: #top
                    J_next[i, j] = g[i, j, u] + p_side @ np.array([J[i, j+1], J[i+1, j], J[i-1, j]])
                elif i == n-1 and j > 0 and j < n-1: #right
                    J_next[i, j] = g[i, j, u] + p_side @ np.array([J[i, j+1], J[i, j+1], J[i-1, j]])
                elif i == 0 and j == n-1:#bottom-right
                    J_next[i, j] = g[i, j, u] + p_corner @ np.array([J[i, j+1], J[i+1, j]])
                elif j == 0 and i == n-1: #top-left
                    J_next[i, j] = g[i, j, u] + p_corner @ np.array([J[i+1, j], J[i-1, j]])
                elif i == 0 and j == 0: #bottom-left
                    J_next[i, j] = g[i, j, u] + p_corner @ np.array([J[i+1, j], J[i, j+1]])
                elif i == n-1 and j == n-1: #top-right
                    J_next[i, j] = g[i, j, u] + p_corner @ np.array([J[i, j-1], J[i-1, j]])
                else: # interior
                    J_next[i, j] = g[i, j, u] + p_interior @ np.array([J[i, j-1], J[i+1, j], J[i, j+1], J[i-1, j]])
    t += 1;
    
print(J_next)




