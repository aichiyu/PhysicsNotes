import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签  
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
############   第一题 1   ##################
def f(y): return -50*y
for h in [0.05,0.04,0.03]:
    x,y = np.arange(0,1,h),np.arange(0,1,h)
    y[0]=100
    for i in range(0,x.size-1): y[i+1] = y[i] +h*f(y[i])
    plt.plot(x,y)
plt.plot(x,100*np.exp(-50*x))
plt.legend(labels = ['h=0.05', 'h=0.04', 'h=0.03', 'Exact'], loc = 'best')
plt.show()
############   第一题 2   ##################
for h in [0.05,0.04,0.03]:
    x,y = np.arange(0,1,h),np.arange(0,1,h)
    y[0]=100
    for i in range(0,x.size-1): y[i+1] = y[i]/(1+50*h)
    plt.plot(x,y)
plt.plot(x,100*np.exp(-50*x))
plt.legend(labels = ['h=0.05', 'h=0.04', 'h=0.03', 'Exact'], loc = 'best')
plt.show()
############   第二题   ##################
h=0.1
A = np.matrix([[0,9/2],[-2,0]])
def main(B):
    r = list(np.arange(0,10,h))
    r[0] = np.matrix([[3],[2]])
    for i in range(0,len(r)-1): r[i+1] = B*r[i]
    r = np.array(r).T
    plt.subplot(221)
    plt.plot(np.arange(0,10,h),r[0][0])
    plt.subplot(222)
    plt.plot(np.arange(0,10,h),r[0][1])
    plt.subplot(223)
    plt.plot(r[0][0],r[0][1])
main((np.eye(2)-A*h/2)**(-1)*(np.eye(2)+A*h/2)) #梯形法
main(np.eye(2)+h*A) #显式Euler法
main((np.eye(2)-h*A)**(-1)) #隐式Euler法
def RK4(rn): #Runge-Kutta法
    k1 = A*rn
    k2 = A*(rn+h*k1/2)
    k3 = A*(rn+h*k2/2)
    k4 = rn + h*k3
    return rn+h*(k1+2*k2+2*k3+k4)/6
r = list(np.arange(0,10,h))
r[0] = np.matrix([[3],[2]])
for i in range(0,len(r)-1): r[i+1] = RK4(r[i])
r = np.array(r).T
plt.subplot(221)
plt.title('x-t')
plt.plot(np.arange(0,10,h),r[0][0])
plt.legend(labels = ['梯形法','显式Euler法','隐式Euler法','Runge-Kutta法'], loc = 'best')
plt.subplot(222)
plt.title('y-t')
plt.plot(np.arange(0,10,h),r[0][1])
plt.subplot(223)
plt.title('x-y')
plt.plot(r[0][0],r[0][1])
plt.show()
############   第三题   ##################
h,ep,t = 0.02,1.e-10,100
def euler(xn,yn):# Euler 法
    global h,ep
    x1,y1,x2,y2 = xn,yn,-1,-1
    while abs(x2-x1)>ep or abs(y2-y1)>ep:
        x1,y1 = x2,y2
        x2,y2 = xn + h*yn-h*h*np.sin(x1),yn -h*np.sin(xn+h*y1)
    return (x2,y2)
def ech(xn,yn):# 梯形法
    global h,ep
    x1,y1,x2,y2 = xn,yn,-1,-1
    while abs(x2-x1)>ep or abs(y2-y1)>ep:
        x1,y1 = x2,y2
        x2,y2 = xn + 0.5*h*(2*yn-0.5*h*(np.sin(xn)+np.sin(x1))),yn - 0.5*h*(np.sin(xn)+np.sin(xn+0.5*h*(yn+y1)))
    return (x2,y2)
for func in [euler, ech]:
    r = list(np.arange(0,t,h))
    r[0] = [np.pi/3,-0.5]
    for i in range(0,len(r)-1): r[i+1] = func(r[i][0], r[i][1])
    r = np.array(r).T
    plt.subplot(211)
    plt.plot(np.arange(0,t,h),r[0])
    plt.subplot(212)
    plt.title('能量')
    plt.plot(np.arange(0,t,h),0.5*r[1]*r[1]-np.cos(r[0]))
plt.legend(labels = ['Euler法','梯形法'], loc = 'best')
plt.show()