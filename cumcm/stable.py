import numpy as np
from scipy import integrate
import math
import matplotlib.pyplot as plt
fig = plt.figure()

C = 0.85
A = 0.7**2*math.pi
vIn = 500*25*math.pi
mIn = vIn*0.85
rho_at_160 = 1
p=100
ma = 8
open = True
trange = 0.001
ma_0 = 0
top = p
bottom = p
storet=[]
storep=[]
storetop = [p]
def q(dp,rho): return C*A*math.sqrt(2*dp/rho)
def rho(mIn): return(mIn/vIn)
def E(p): return(1495*math.exp(0.0039*p))
vb = 10000/100*44
sumt = vb/q(160-100,0.87)
tlist = [sumt/1000 for i in range(1000)]
def phi(t, tlist):
    y = 0
    temp = t%100
    if temp<0.2:
        y -= temp**2/2
    elif temp<2.2:
        y -= (2+(temp-0.2)*20)
    elif temp<2.4:



vb = 440
