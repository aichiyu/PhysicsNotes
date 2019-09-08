import numpy as np
import matplotlib.pyplot as plt
def f(x): return 1/(1+25*x**2)        #定义f(x)=1/(1+25x^2)
def l(x,j,k,xs):                      #定义l(x)
    prod = 1                          
    for i in range(k+1):              #当i不等于j时, 乘以(x-xi)/(xj-xi)
        if i != j:prod *= (x-xs[i])/(xs[j]-xs[i])
    return prod                       
def L(x,k,xs,ys):                    #定义L(x)
    suml = 0                         #将所有l(x)相加
    for j in range(k+1): suml += ys[j]*l(x,j,k,xs)
    return suml
x = np.arange(-1.1,-0.9,0.001)             #定义域设为[-5,5]
plt.plot(x,f(x),marker="x")          #绘制f(x)图像
for k in range(1,8):                 #把k=2-6的几种情况绘图
    xs = np.arange(-1, 1, 2/(k+1))
    ys = f(xs)
    fig = plt.plot(x,L(x,k,xs,ys))
plt.legend(labels = ['f(x)','k=1','k=2', 'k=3', 'k=4', 'k=5', 'k=6', 'k=7', 'k=8', 'k=9'])
plt.show()