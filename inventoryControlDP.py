import numpy as np
import matplotlib.pyplot as plt

C = 6;
D = 2;
T = 50;

p = [0.7, 0.2, 0.1]; #70% of time demand will be zero, 20% of time demand will be 1, 10% of time demand will be 2

x = C;
J = np.zeros((T+1, x)); # optimal cost to go 
Pi = np.zeros((T+1, x)); # optimal policy
currentCost = np.zeros((T+1, x));

def stageCost(x, u):
    return 0.1*x + 1 if u > 0 else 0.1*x;

def optimalProgramming(t, x, u):
    return currentCost[t, u] + p * J[t+1, x];



