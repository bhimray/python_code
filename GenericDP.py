import numpy as np

n= 3;
m= 2;
random_array = np.random.rand(n, n, m);
print(random_array, random_array[0,0,1]);

sm = np.sum(random_array, axis=0);
print(sm);