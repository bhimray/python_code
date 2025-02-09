import numpy as np
import matplotlib.pyplot as plt

C = 6;
D = 2;

T = 25; #final time

P = [ 0.7, 0.2, 0.2 ];
x = np.zeros((T+1,1));
u = np.zeros((T, 1));
d = np.zeros((T,1));

x[0, 0] = C;

#recursion using markov chain
for eachTime in range(T):
    u[eachTime, 0] = (C-x(eachTime))*(int(x(eachTime)) <= 1 )
    d[eachTime, 0] = ()
