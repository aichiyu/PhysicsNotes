import numpy as np
import math
import matplotlib.pyplot as plt
fig = plt.figure()
Aaa = 2.5**2 * math.pi
Aa = 0.7**2 * math.pi
omega = 0.3
x = 5.5315
V = x * Aaa
m = 92.31943
rho = 0.85
p = 100
theta = .515075
dt = 1e-4
C = 0.85
storep = []
storet = []


def Q(dp, rho):
    return C * Aa * math.sqrt(2 * dp / rho)


def E(p):
    return 1495 * math.exp(0.0039 * p)


def v(t):
    return -omega * 2.413 * math.sin(omega * t)


mall = 0

storep += [p]
storet += [theta / omega]
for t in np.arange(theta / omega, 1000, dt):
    if p < 100:
        break
    dx = v(t) * dt
    x += dx
    dV = Aaa * dx
    V += dV
    dm = -Q(p - 100, rho) * rho * dt
    m += dm
    mall += dm
    drho = dm / V - m * dV / V**2
    rho += drho
    dp = E(p) / rho * drho
    p += dp
    storep += [p]
    storet += [t]
plt.plot(storet, storep)
plt.xlabel('time (ms)')
plt.ylabel('Pressure (MPa)')
plt.show()
print(mall)
