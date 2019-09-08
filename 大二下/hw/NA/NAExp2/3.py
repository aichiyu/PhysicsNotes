import numpy as np
x = np.array([1,11,12,21,31,41,43,52,62])
A = np.mat(np.c_[np.ones(9), 1/x])
y = np.array([297,1584,1640,1988,2189,2309,2309,2394,2439])
a, b = np.matmul(np.matmul(np.matmul(A.T, A).I, A.T), 1/y).flat
print(a, b, 1/(a+b/67))
