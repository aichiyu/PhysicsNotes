import numpy as np
y = np.log([29.72,30.61,31.51,32.13,32.34,32.85,33.56,34.2,34.83])
A = np.mat(np.c_[np.ones(9),np.arange(1960,1969)])
a,b = np.matmul(np.matmul(np.matmul(A.T,A).I,A.T),y).flat
print(a,b,np.exp(a+b*2018),np.exp(a+b*2019))
