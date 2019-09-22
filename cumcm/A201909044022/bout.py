import numpy as np
import math
import matplotlib.pyplot as plt
fig = plt.figure()

C = 0.85
vIn = 500 * 25 * math.pi
mIn = vIn * 0.85
p = 100
open = True
trange = 0.001
Ac = 0.7**2 * math.pi
storet = []
storep = []


def q(A, dp, rho):
    if dp == rho == 0: return 0
    return C * A * math.sqrt(2 * dp / rho)


def rho(mIn):
    return (mIn / vIn)


def E(p):
    return (1495 * math.exp(0.0039 * p))


def distance(t):
    if t <= 0.45:
        return 2.225 / (1 + 537.9 * math.exp(-19.3 * t))
    elif t <= 2:
        return 2
    elif t <= 2.45:
        return 2.267 / (1 + 456.4 * math.exp(18.63 * (t - 2.45)))
    elif t <= 100:
        return 0
    else:
        print("Error")


def Ab(t):
    return ((distance(t) + 7.95775) * 9 * math.pi /
            180)**2 * math.pi - 1.25**2 * math.pi


print(distance(1e-3), Ab(1e-3))

pb = 0.1
mb = 0.8 * 10.74
trange = 1e-3
penchuqu = 0
rho0 = rho(mIn)
pball = []
rhob0 = 0.8
rhob = 0.8

for ti in np.arange(0, 100, trange):
    vb = math.pi * (distance(ti) + (7.95775 - 4.45634)) / 3 * (
        ((distance(ti) + 7.95775) * 9 * math.pi / 180)**2 + .7**2 + .7 *
        ((distance(ti) + 7.95775) * 9 * math.pi / 180))
    rhob0 = rhob
    if pb >= p:
        rhob = rho0
        mb = rho0 * vb
        pb = 100
    elif pb < 0.1 or rhob < 0.8:
        pb = 0.1
        rhob = 0.8
        rhob0 = 0.8
    else:
        #print(q(Ab(ti), p - pb, rho0))
        mb += q(Ab(ti), p - pb, rho0) * trange * rho0
        penchuqu += q(Ab(ti), p - pb, rho0) * trange * rho0
        rhob = mb / vb
        pb += E(p) / rhob * (rhob - rhob0)
    if pb < 0.1 or rhob < 0.8:
        pb = 0.1
        rhob = 0.8
        rhob0 = 0.8
    rhob0 = rhob
    #print(pb,rhob)
    mb -= q(Ac, pb, rhob) * trange * rhob
    pball += [penchuqu]
    if mb < 0.8 * vb:
        mb = 0.8 * vb
        pb = 0.1
    rhob = mb / vb
    if rhob != 0.8:
        pb -= E(pb) / rhob * (rhob0 - rhob)
    if pb < 0.1:
        pb = 0.1
    rhob0 = rhob
pball = np.array(pball)
print("penchuqu =", penchuqu)
pball = np.array([i * penchuqu + pball for i in range(10)]).flat
np.savetxt('D:\\Onedrive\\prog\\PhysicsNotes\\cumcm\\pball.txt', pball)
np.savetxt('D:\\Onedrive\\prog\\PhysicsNotes\\cumcm\\time.txt',
           np.arange(0, 1000, trange))
plt.plot(np.arange(0, 1000, trange), pball)
plt.xlabel('time (ms)')
plt.ylabel('mass out (mg)')
plt.show()
# 每次喷出 26.99 mg