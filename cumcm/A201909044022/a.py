import numpy as np
from scipy import integrate
import math
import matplotlib.pyplot as plt
fig = plt.figure()

C = 0.85
A = 0.7**2 * math.pi
vIn = 500 * 25 * math.pi
mIn = vIn * 0.85
rho_at_160 = 0.87
p = 100
ma = 7.31  #2000ms - 7.31mg --- 5000ms - 5.04mg --- 10000ms - 4.31mg
open = True
trange = 0.001
ma_0 = 0
top = p
bottom = p
storet = []
storep = []
storetop = [p]


def q(dp, rho):
    return C * A * math.sqrt(2 * dp / rho)


def rho(mIn):
    return (mIn / vIn)


def E(p):
    return (1495 * math.exp(0.0039 * p))


last_in_oil_time = 0
opentime = 0
storeopentime = []
for ti in np.arange(1, 15000, trange):
    if p > 150: break

    rho0 = rho(mIn)
    temp = ti % 100
    if temp < trange: top = p
    if temp < 0.2:
        mIn -= trange * (temp * 10) * rho(mIn)
    elif temp < 2.2:
        mIn -= 20 * trange * rho(mIn)
    elif temp < 2.4:
        mIn -= (2.4 - temp) * trange * 10 * rho(mIn)
        bottom = p
    else:
        pass

    if (ti - last_in_oil_time) >= 10 and not open:
        mIn_last_open = mIn
        opentime = ti
        open = True
    if open:
        ma_0 += trange * q(160 - p, rho_at_160)
        mIn += trange * q(160 - p, rho_at_160)
        if ma_0 >= ma:
            open = False
            last_in_oil_time = ti
            ma_0 = 0
            storeopentime += [ti - opentime]
    drho = rho(mIn) - rho0
    p += E(p) / rho(mIn) * drho
    storet += [ti]
    storep += [p]
    if ti % 100 < 2.4:
        storetop += [storetop[-1]]
    else:
        storetop += [(top + bottom) / 2]
print('ma =', ma, 'ti =', ti)
plt.xlabel("Time (ms)")
plt.ylabel("Presure (MPa)")
plt.plot(storet, storep)
plt.plot(storet, storetop[1:])
plt.show()
fig = plt.figure()
plt.plot(storeopentime[3:])
plt.xlabel("the $N_{th}$ injection")
plt.ylabel("time for every injection (ms)")
plt.show()
