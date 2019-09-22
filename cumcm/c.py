import numpy as np
from scipy import integrate
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
fig = plt.figure()

#####################   in  #########################
Aaa = 2.5**2 * math.pi
Aa = 0.7**2 * math.pi
omega = 0.11
p0 = 10
'''
When omega = 0.0445 and p0 = 100 , We will have average oil = -0.7888128422628126 Variance = 296.8055590776664
When omega = 0.055 and p0 = 10 , We will have average oil = -11.165893056647555 Variance = 234.27149260504498
When omega = 0.06 and p0 = 5 , We will have average oil = -12.53827327326307 Variance = 199.07614140826723
When omega = 0.08 and p0 = 0 , We will have average oil = -13.075589479119037 Variance = 155.3312421142647
When omega = 0.09 and p0 = 0 , We will have average oil = -11.908094180614148 Variance = 142.1443762712971
When omega = 0.11 and p0 = 5 , We will have average oil = -4.848550471253415 Variance = 132.67064087579712
'''
x = 5.5315
V = x * Aaa
m = 92.31943
rho0 = 0.85
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

storep += [0 for i in np.arange(0, theta / omega, dt)]
storet += [i for i in np.arange(0, theta / omega, dt)]
for t in np.arange(theta / omega, 1000, dt):
    if p < 100:
        tfinal = float(t)
        break
    dx = v(t) * dt
    x += dx
    dV = Aaa * dx
    V += dV
    dm = -Q(p - 100, rho0) * rho0 * dt
    m += dm
    mall += dm
    drho = dm / V - m * dV / V**2
    rho0 += drho
    dp = E(p) / rho0 * drho
    p += dp
    storep += [mall]
period = 2 * math.pi / omega
storep += [mall for i in np.arange(tfinal, period, dt)]
storep = np.array(storep)
repeatN = int(1000 / period) + 1
storet = np.array([i for i in np.arange(0, repeatN * period + dt, dt)])
storep = np.array([storep + i * mall for i in np.arange(0, repeatN)]).flatten()

print('mass in =', -mall)

##################################################

#########################  out 1  #########################

C = 0.85
vIn = 500 * 25 * math.pi
mIn = vIn * 0.85
p = 100
open = True
trange = 0.001
Ac = 0.7**2 * math.pi
storet = []


def q(A, dp, rho):
    if dp == rho == 0: return 0
    return C * A * math.sqrt(2 * dp / rho)


def rho(mIn):
    return (mIn / vIn)


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


pb = 0.1
mb = 0.8 * 10.74
trange = dt
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
print("mass out =", penchuqu)
pball = np.array([i * penchuqu + pball for i in range(10)]).flatten()

##################################################
shift_pball = np.append(np.arange(0, 50, trange), pball)
final = -(storep[:int(1000 / trange)] + pball +
          shift_pball[:int(1000 / trange)])

open2 = False
mass_out_per_dt = 20.02 * dt * rho0
plt.plot(np.arange(0, 1000, trange), final)
count = 0
final = np.array(final)
for i in tqdm(range(final.size)):
    if not open2 and final[i] > p0:
        open2 = True
    if open2 and final[i] < p0:
        open2 = False
    if open2:
        count += 1
        final[i:] -= mass_out_per_dt

print('When omega =', omega, 'and p0 =', p0, ', We will have average oil =',
      np.mean(final), 'Variance =', np.var(final))
plt.plot(np.arange(0, 1000, trange), final)
plt.show()
