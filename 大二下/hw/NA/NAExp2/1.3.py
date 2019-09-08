import numpy as np
def g(x): return (1/(1+25*(x**2)) - (0.6694-2.3055*x**2+1.8689*x**4))**2  #定义两函数之差的平方为g(x)
n = 100                                                                   #在复合辛普森公式中取100个点
xs = np.arange(-1,1,2/(2*n))                                              #计算S
S = (2/(6*n))*(g(-1)+4*sum([g(xs[2*i-1]) for i in range(1,n+1)])+2*sum([g(xs[2*i]) for i in range(1,n)])+g(1))
print(np.sqrt(S))                                                         #sqrt(S) = 0.18349445771001033