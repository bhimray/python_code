import numpy as np

n= 3;
m= 2;
T = 50;

P = np.array(n,n, m); #transition matrix

#normalizing to get the row stochastic matrix
#TODO

G = np.random.rand(n,m,T); #stage cost
GT = np.random.rand(n,1); #terminal cost

# Dynamic Programming
