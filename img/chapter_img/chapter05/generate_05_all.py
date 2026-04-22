#!/usr/bin/env python3
"""
Generate educational images for Chapter 05 lessons
Lessons 05-01 to 05-10: Nonlinear ODEs and Stability
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter05/'

# =============================================================================
# 05-01: Autonomous Phase Plane
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Phase plane with nullclines
ax1 = axes1[0]
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

# dx/dt = y - x, dy/dt = 1 - x^2 - y^2 (Duffing-like)
U = Y - X
V = 1 - X**2 - Y**2

ax1.streamplot(x, y, U, V, density=1.5, color='blue', linewidth=1)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Mặt phẳng pha tự chủ\n$\\dot{x} = f(x,y), \\dot{y} = g(x,y)$')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Trajectories
ax2 = axes1[1]
def sys(state, t):
    x, y = state
    return [y - x, 1 - x**2 - y**2]

for x0 in [[-1, -1], [-1, 1], [1, -1], [1, 1], [0, 0.5]]:
    sol = odeint(sys, x0, np.linspace(0, 5, 500))
    ax2.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'$x_0={x0}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Quỹ đạo trong mặt phẳng pha\nNhiều điều kiên ban đầu')
ax2.legend(loc='upper right', fontsize=8)
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_01_autonomous_phase_plane.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-02: Equilibria and Linearization
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Equilibrium points
ax1 = axes2[0]
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

# Example: Lotka-Volterra
U = X * (1 - Y)
V = Y * (X - 0.5)

ax1.streamplot(x, y, U, V, density=1.2, color='blue', linewidth=1)
ax1.scatter([0, 0.5, 1], [0, 0, 1], color='red', s=100, zorder=5)
ax1.annotate('(0,0)', (0, 0), textcoords="offset points", xytext=(5, -15), fontsize=10)
ax1.annotate('(0.5,0)', (0.5, 0), textcoords="offset points", xytext=(5, -15), fontsize=10)
ax1.annotate('(1,1)', (1, 1), textcoords="offset points", xytext=(5, -15), fontsize=10)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Các điểm cân bằng\n$\\dot{x} = x(1-y), \\dot{y} = y(x-0.5)$')
ax1.set_xlim(-0.5, 2)
ax1.set_ylim(-0.5, 2)

# Right: Linearization
ax2 = axes2[1]
# Show Jacobian at equilibrium
x = np.linspace(-1, 1.5, 200)
y = np.linspace(-1, 1.5, 200)
X, Y = np.meshgrid(x, y)

# Linearized at (1,1): A = [[-1, -1], [1, 0]]
U = -X - Y + 2
V = X - 1

ax2.streamplot(x, y, U, V, density=1.2, color='blue', linewidth=1)
ax2.scatter([1], [1], color='red', s=100, zorder=5)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title(r'Tuyến tính hóa: dx = A dx')
ax2.set_xlim(-0.5, 1.5)
ax2.set_ylim(-0.5, 1.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_02_equilibria_linearization.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-03: Stability Classification
# =============================================================================
fig3, axes3 = plt.subplots(2, 3, figsize=(15, 10))

systems = [
    (np.array([[-1, 0], [0, -1]]), 'Ổn định (Sink)', 'blue'),
    (np.array([[1, 0], [0, 1]]), 'Không ổn định (Source)', 'red'),
    (np.array([[-1, 0], [0, 1]]), 'Yên ngựa (Saddle)', 'green'),
    (np.array([[0, 1], [-1, 0]]), 'Trung tâm (Center)', 'blue'),
    (np.array([[-0.3, 1], [-1, -0.3]]), 'Xoắn ốc ổn định', 'blue'),
    (np.array([[0.3, 1], [-1, 0.3]]), 'Xoắn ốc không ổn định', 'red'),
]

for idx, (A, title, color) in enumerate(systems):
    ax = axes3[idx // 3, idx % 3]
    x = np.linspace(-2, 2, 15)
    y = np.linspace(-2, 2, 15)
    X, Y = np.meshgrid(x, y)
    U = A[0,0]*X + A[0,1]*Y
    V = A[1,0]*X + A[1,1]*Y
    ax.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap=color, scale=20)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_03_stability_classification.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-04: Lyapunov Stability
# =============================================================================
fig4, axes4 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Lyapunov function
ax1 = axes4[0]
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

V = X**2 + Y**2
contour = ax1.contour(X, Y, V, levels=10, cmap='viridis')
ax1.clabel(contour, inline=True, fontsize=8, fmt='%.1f')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Hàm Lyapunov: $V(x,y) = x^2 + y^2$\n$\\dot{V} \\leq 0$')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: V decreasing
ax2 = axes4[1]
def sys(state, t):
    x, y = state
    return [-y - x*(x**2 + y**2), x - y*(x**2 + y**2)]

t = np.linspace(0, 5, 500)
sol = odeint(sys, [1, 1], t)
V = sol[:, 0]**2 + sol[:, 1]**2

ax2.plot(t, V, 'b-', linewidth=2)
ax2.axhline(y=0, color='red', linestyle='--', linewidth=1)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$V(x,y)$')
ax2.set_title('$V$ giảm dần theo thời gian\n$\\Rightarrow$ ổn định')
ax2.set_xlim(-0.5, 5.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_04_lyapunov_stability.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-05: Limit Cycles
# =============================================================================
fig5, axes5 = plt.subplots(1, 2, figsize=(14, 6))

# Van der Pol oscillator
ax1 = axes5[0]
def vdp(state, t):
    x, y = state
    return [y, mu*(1 - x**2)*y - x]

for mu in [0.5, 1, 2]:
    t = np.linspace(0, 10, 500)
    sol = odeint(vdp, [2, 0], t)
    ax1.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'$\mu = {mu}$')

ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Dao động Van der Pol\nChu trình giới hạn')
ax1.legend()
ax1.set_xlim(-3, 3)
ax1.set_ylim(-4, 4)

# Limit cycle formation
ax2 = axes5[1]
t = np.linspace(0, 20, 1000)
for x0 in [[0.1, 0], [0.5, 0], [1, 0], [2, 0], [3, 0]]:
    sol = odeint(vdp, x0, t)
    ax2.plot(sol[:, 0], sol[:, 1], linewidth=1.5, alpha=0.7)

ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Hội tụ về chu trình giới hạn\nTừ nhiều điều kiên ban đầu')
ax2.set_xlim(-3, 3)
ax2.set_ylim(-4, 4)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_05_limit_cycles.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-06: Bifurcations
# =============================================================================
fig6, axes6 = plt.subplots(1, 3, figsize=(15, 5))

# Saddle-node
ax1 = axes6[0]
mu_vals = [-1, 0, 1]
for mu in mu_vals:
    x = np.linspace(-2, 2, 200)
    y = mu - x**2
    ax1.plot(x, y, linewidth=2, label=f'$\mu = {mu}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$x$')
ax1.set_ylabel('dx/dt')
ax1.set_title('Điểm rẽ yên-ngựa\n$\dot{x} = \mu - x^2$')
ax1.legend()

# Transcritical
ax2 = axes6[1]
for mu in mu_vals:
    x = np.linspace(-2, 2, 200)
    y = mu*x - x**2
    ax2.plot(x, y, linewidth=2, label=f'$\mu = {mu}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$\dot{x}$')
ax2.set_title('Điểm rẽ xuyên suốt\n$\dot{x} = \mu x - x^2$')
ax2.legend()

# Pitchfork
ax3 = axes6[2]
for mu in mu_vals:
    x = np.linspace(-2, 2, 200)
    y = mu*x - x**3
    ax3.plot(x, y, linewidth=2, label=f'$\mu = {mu}$')

ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlabel('$x$')
ax3.set_ylabel('$\dot{x}$')
ax3.set_title('Điểm rẽ nhánh ba\n$\dot{x} = \mu x - x^3$')
ax3.legend()

plt.tight_layout()
plt.savefig(IMG_PATH + '05_06_bifurcations.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-07: Predator-Prey
# =============================================================================
fig7, axes7 = plt.subplots(1, 2, figsize=(14, 6))

# Lotka-Volterra
ax1 = axes7[0]
def lv(state, t):
    x, y = state
    return [x*(1 - 0.5*y), y*(0.5*x - 1)]

t = np.linspace(0, 10, 500)
for x0 in [[0.5, 0.5], [1, 1], [2, 2]]:
    sol = odeint(lv, x0, t)
    ax1.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'$x_0={x0}$')

ax1.set_xlabel('Con mồi ($x$)')
ax1.set_ylabel('Kẻ săn mồi ($y$)')
ax1.set_title('Mô hình Lotka-Volterra\nDao động tuần hoàn')
ax1.legend()
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)

# With damping
ax2 = axes7[1]
def lv_damped(state, t):
    x, y = state
    return [x*(1 - 0.5*y) - 0.1*x, y*(0.5*x - 1) - 0.1*y]

for x0 in [[0.5, 0.5], [1, 1], [2, 2]]:
    sol = odeint(lv_damped, x0, t)
    ax2.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'$x_0={x0}$')

ax2.set_xlabel('Con mồi ($x$)')
ax2.set_ylabel('Kẻ săn mồi ($y$)')
ax2.set_title('Với damping\nHướng tới điểm cân bằng')
ax2.legend()
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_07_predator_prey.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-08: Competing Species
# =============================================================================
fig8, axes8 = plt.subplots(1, 2, figsize=(14, 6))

# Competition model
ax1 = axes8[0]
def comp(state, t):
    x, y = state
    return [x*(1 - x - 0.5*y), y*(1 - 0.5*x - y)]

for x0 in [[0.2, 0.2], [0.5, 0.5], [1, 0.2], [0.2, 1]]:
    sol = odeint(comp, x0, t)
    ax1.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'$x_0={x0}$')

ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Cạnh tranh: $\\dot{x}_1 = x_1(1-x_1-0.5x_2), \\dot{x}_2 = x_2(1-0.5x_1-x_2)$')
ax1.legend()
ax1.set_xlim(0, 1.5)
ax1.set_ylim(0, 1.5)

# Phase portrait
ax2 = axes8[1]
x = np.linspace(0, 1.5, 100)
y = np.linspace(0, 1.5, 100)
X, Y = np.meshgrid(x, y)
U = X*(1 - X - 0.5*Y)
V = Y*(1 - 0.5*X - Y)

ax2.streamplot(x, y, U, V, density=1.5, color='blue', linewidth=1)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
ax2.set_title('Trường vector cạnh tranh\nHai loài cạnh tranh')
ax2.set_xlim(0, 1.5)
ax2.set_ylim(0, 1.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_08_competing_species.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-09: Introduction to Chaos
# =============================================================================
fig9, axes9 = plt.subplots(1, 2, figsize=(14, 6))

# Lorenz system
ax1 = axes9[0]
def lorenz(state, t):
    x, y, z = state
    sigma = 10
    rho = 28
    beta = 8/3
    return [sigma*(y - x), x*(rho - z) - y, x*y - beta*z]

t = np.linspace(0, 10, 2000)
sol = odeint(lorenz, [1, 1, 1], t)

ax1.plot(sol[:, 0], sol[:, 2], 'b-', linewidth=0.5)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$z$')
ax1.set_title('Hỗn loạn Lorenz\nQuỹ đạo hỗn loạn')
ax1.set_xlim(-20, 20)
ax1.set_ylim(0, 50)

# Sensitivity
ax2 = axes9[1]
for eps in [0.01, 0.001]:
    sol1 = odeint(lorenz, [1, 1, 1], t)
    sol2 = odeint(lorenz, [1+eps, 1, 1], t)
    diff = np.sqrt((sol1[:, 0]-sol2[:, 0])**2 + (sol1[:, 1]-sol2[:, 1])**2 + (sol1[:, 2]-sol2[:, 2])**2)
    ax2.semilogy(t, diff, linewidth=2, label=f'$\epsilon = {eps}$')

ax2.set_xlabel('$t$')
ax2.set_ylabel('Khoảng cách')
ax2.set_title('Nhạy cảm với điều kiên ban đầu\nHiệu ứng cánh bướm')
ax2.legend()

plt.tight_layout()
plt.savefig(IMG_PATH + '05_09_introduction_chaos.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 05-10: SIR Epidemiology
# =============================================================================
fig10, axes10 = plt.subplots(1, 2, figsize=(14, 6))

# SIR model
ax1 = axes10[0]
def sir(state, t):
    S, I, R = state
    beta = 0.5
    gamma = 0.2
    return [-beta*S*I, beta*S*I - gamma*I, gamma*I]

t = np.linspace(0, 30, 500)
sol = odeint(sir, [99, 1, 0], t)

ax1.plot(t, sol[:, 0], 'b-', linewidth=2, label='$S$ (Susceptible)')
ax1.plot(t, sol[:, 1], 'r-', linewidth=2, label='$I$ (Infectious)')
ax1.plot(t, sol[:, 2], 'g-', linewidth=2, label='$R$ (Recovered)')
ax1.set_xlabel('$t$')
ax1.set_ylabel('Dân số')
ax1.set_title('Mô hình SIR\n$\dot{S} = -\\beta SI, \\dot{I} = \\beta SI - \\gamma I, \\dot{R} = \\gamma I$')
ax1.legend()
ax1.set_xlim(-1, 31)

# Phase plane S-I
ax2 = axes10[1]
ax2.plot(sol[:, 0], sol[:, 1], 'b-', linewidth=2)
ax2.set_xlabel('$S$')
ax2.set_ylabel('$I$')
ax2.set_title('Mặt phẳng pha S-I\nDịch bệnh')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 50)

plt.tight_layout()
plt.savefig(IMG_PATH + '05_10_sir_epidemiology.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 05:")
print("  05_01_autonomous_phase_plane.svg")
print("  05_02_equilibria_linearization.svg")
print("  05_03_stability_classification.svg")
print("  05_04_lyapunov_stability.svg")
print("  05_05_limit_cycles.svg")
print("  05_06_bifurcations.svg")
print("  05_07_predator_prey.svg")
print("  05_08_competing_species.svg")
print("  05_09_introduction_chaos.svg")
print("  05_10_sir_epidemiology.svg")