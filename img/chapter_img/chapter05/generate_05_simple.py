#!/usr/bin/env python3
"""
Generate educational images for Chapter 05 - Simple version
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter05/'

# 05-01: Autonomous Phase Plane - simple trajectories
fig1, ax = plt.subplots(figsize=(8, 6))
t = np.linspace(0, 5, 500)

def sys(state, t):
    x, y = state
    return [y - x, 1 - x**2 - y**2]

for x0 in [[1, 1], [-1, 1], [-1, -1], [1, -1], [0, 0.5]]:
    sol = odeint(sys, x0, t)
    ax.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'({x0[0]}, {x0[1]})')

ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Quy dao trong mat phang pha tu chu')
ax.legend()
plt.savefig(IMG_PATH + '05_01_autonomous_phase_plane.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-02: Equilibria - simple
fig2, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-1, 2, 15)
y = np.linspace(-1, 2, 15)
X, Y = np.meshgrid(x, y)
U = X * (1 - Y)
V = Y * (X - 0.5)
ax.streamplot(x, y, U, V, density=1.2)
ax.scatter([0, 0.5, 1], [0, 0, 1], color='red', s=100, zorder=5)
ax.set_xlabel('x (prey)')
ax.set_ylabel('y (predator)')
ax.set_title('Diem can bang Lotka-Volterra')
plt.savefig(IMG_PATH + '05_02_equilibria_linearization.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-03: Stability - simple quiver
fig3, ax = plt.subplots(figsize=(8, 6))
A = np.array([[-1, 0], [0, 1]])
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y
ax.quiver(X, Y, U, V)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Yen ngua (Saddle)')
ax.set_aspect('equal')
plt.savefig(IMG_PATH + '05_03_stability_classification.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-04: Lyapunov - simple decreasing energy
fig4, ax = plt.subplots(figsize=(8, 6))
t = np.linspace(0, 5, 500)
def sys(state, t):
    x, y = state
    return [-y - x*(x**2+y**2), x - y*(x**2+y**2)]
sol = odeint(sys, [1, 1], t)
V = sol[:,0]**2 + sol[:,1]**2
ax.plot(t, V, 'b-', linewidth=2)
ax.set_xlabel('t')
ax.set_ylabel('V(x,y)')
ax.set_title('Ham Lyapunov giam dan')
plt.savefig(IMG_PATH + '05_04_lyapunov_stability.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-05: Limit cycles - Van der Pol
fig5, ax = plt.subplots(figsize=(8, 6))
def vdp(state, t):
    x, y = state
    mu = 1
    return [y, mu*(1-x**2)*y - x]
t = np.linspace(0, 10, 500)
for x0 in [[0.1, 0], [1, 0], [2, 0], [3, 0]]:
    sol = odeint(vdp, x0, t)
    ax.plot(sol[:, 0], sol[:, 1], linewidth=1.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Van der Pol - Chu trinh gioi han')
plt.savefig(IMG_PATH + '05_05_limit_cycles.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-06: Bifurcations
fig6, axes6 = plt.subplots(1, 3, figsize=(14, 5))
mu_vals = [-1, 0, 1]

# Saddle-node
ax1 = axes6[0]
for mu in mu_vals:
    x = np.linspace(-2, 2, 200)
    y = mu - x**2
    ax1.plot(x, y, linewidth=2, label=f'mu={mu}')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('x')
ax1.set_ylabel('dx/dt')
ax1.set_title('Saddle-node')
ax1.legend()

# Transcritical
ax2 = axes6[1]
for mu in mu_vals:
    x = np.linspace(-2, 2, 200)
    y = mu*x - x**2
    ax2.plot(x, y, linewidth=2, label=f'mu={mu}')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('x')
ax2.set_ylabel('dx/dt')
ax2.set_title('Transcritical')
ax2.legend()

# Pitchfork
ax3 = axes6[2]
for mu in mu_vals:
    x = np.linspace(-2, 2, 200)
    y = mu*x - x**3
    ax3.plot(x, y, linewidth=2, label=f'mu={mu}')
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlabel('x')
ax3.set_ylabel('dx/dt')
ax3.set_title('Pitchfork')
ax3.legend()

plt.tight_layout()
plt.savefig(IMG_PATH + '05_06_bifurcations.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-07: Predator-Prey
fig7, ax = plt.subplots(figsize=(8, 6))
def lv(state, t):
    x, y = state
    return [x*(1-0.5*y), y*(0.5*x-1)]
t = np.linspace(0, 10, 500)
for x0 in [[0.5, 0.5], [1, 1], [2, 2]]:
    sol = odeint(lv, x0, t)
    ax.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'S={x0}')
ax.set_xlabel('Con moi (S)')
ax.set_ylabel('Ke san moi (R)')
ax.set_title('Lotka-Volterra')
ax.legend()
plt.savefig(IMG_PATH + '05_07_predator_prey.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-08: Competing Species
fig8, ax = plt.subplots(figsize=(8, 6))
def comp(state, t):
    x, y = state
    return [x*(1-x-0.5*y), y*(1-0.5*x-y)]
t = np.linspace(0, 10, 500)
for x0 in [[0.2, 0.2], [1, 0.2], [0.2, 1]]:
    sol = odeint(comp, x0, t)
    ax.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'({x0[0]},{x0[1]})')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Canh tranh hai loai')
ax.legend()
plt.savefig(IMG_PATH + '05_08_competing_species.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-09: Chaos - Lorenz
fig9, ax = plt.subplots(figsize=(8, 6))
def lorenz(state, t):
    x, y, z = state
    sigma, rho, beta = 10, 28, 8/3
    return [sigma*(y-x), x*(rho-z)-y, x*y-beta*z]
t = np.linspace(0, 10, 2000)
sol = odeint(lorenz, [1, 1, 1], t)
ax.plot(sol[:, 0], sol[:, 2], 'b-', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('Lorenz attractor')
plt.savefig(IMG_PATH + '05_09_introduction_chaos.svg', dpi=150, bbox_inches='tight')
plt.close()

# 05-10: SIR
fig10, ax = plt.subplots(figsize=(8, 6))
def sir(state, t):
    S, I, R = state
    beta, gamma = 0.5, 0.2
    return [-beta*S*I, beta*S*I-gamma*I, gamma*I]
t = np.linspace(0, 30, 500)
sol = odeint(sir, [99, 1, 0], t)
ax.plot(t, sol[:, 0], 'b-', linewidth=2, label='S')
ax.plot(t, sol[:, 1], 'r-', linewidth=2, label='I')
ax.plot(t, sol[:, 2], 'g-', linewidth=2, label='R')
ax.set_xlabel('t')
ax.set_ylabel('Population')
ax.set_title('SIR model')
ax.legend()
plt.savefig(IMG_PATH + '05_10_sir_epidemiology.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated Chapter 05 images")