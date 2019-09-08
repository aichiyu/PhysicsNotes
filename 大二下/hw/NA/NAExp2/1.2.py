import numpy as np
import sympy
import matplotlib.pyplot as plt
x,X,B = sympy.symbols('x'),np.empty([5,5]),np.empty([5,1])
def innerprod(x,f,g): return sympy.integrate(f*g,(x,-1,1))#定义两函数内积为二者乘积在[-1,1]的积分
for i in range(5):                 #分别为法方程中的两个矩阵X,B赋值
    for j in range(5): X[i][j] = innerprod(x,x**i,x**j) 
    B[i] = innerprod(x,1/(1+25*x**2),x**i)
C = np.matmul(np.mat(X).I,B).flat  #求解系数矩阵C=X^-1B
print(C)                           #C = [0.67,0,-2.3,0,1.87] 可以看到x,x^3项系数均为0.
x = np.arange(-1,1,0.01)           #定义绘图定义域为[-1,1]
P = C[0]+C[2]*x**2+C[4]*x**4       #计算定义域内P(x)
plt.plot(x,1/(1+25*x**2))          #绘制f(x)图像
plt.plot(x,P)                      #绘制P(x)图像
plt.legend(labels = ['f(x)','P(x)'])
plt.show()