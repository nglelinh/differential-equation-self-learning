#!/usr/bin/env python3
"""
Generate educational images for Chapter 04 lessons
Lessons 04-01 to 04-10
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter04/'

# =============================================================================
# 04-01: Introduction to Systems
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: State space
ax1 = axes1[0]
t = np.linspace(0, 4*np.pi, 500)
x = np.sin(t)
y = np.cos(t)

ax1.plot(x, y, 'b-', linewidth=2)
ax1.scatter([0], [1], color='red', s=100, zorder=5)
ax1.annotate('$t=0$', (0, 1), textcoords="offset points", xytext=(10, 5), fontsize=11)
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Không gian trạng thái 2D\n$x_1\' = x_2, x_2\' = -x_1$')
ax1.set_aspect('equal')
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)

# Right: Higher order to first order
ax2 = axes1[1]
t = np.linspace(0, 5, 500)

# y'' + 2y' + y = 0 => x1 = y, x2 = y'
# x1' = x2, x2' = -2x2 - x1
from scipy.integrate import odeint

def sys(x, t):
    return [x[1], -2*x[1] - x[0]]

x0 = [1, 0]
sol = odeint(sys, x0, t)

ax2.plot(t, sol[:, 0], 'b-', linewidth=2, label='$y = x_1$')
ax2.plot(t, sol[:, 1], 'r-', linewidth=2, label='$y\' = x_2$')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$x_1, x_2$')
ax2.set_title('Hệ bậc 2 $\\to$ Hệ bậc 1\n$y\'\' + 2y\' + y = 0$')
ax2.legend()
ax2.set_xlim(-0.3, 5.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_01_introduction_systems.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-02: Matrices and Linear Systems
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Matrix representation
ax1 = axes2[0]
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

A = np.array([[1, 1], [1, -1]])
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax1.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=15)
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Trường vector tuyến tính\n$\\mathbf{x}\' = A\\mathbf{x}$')
ax1.set_aspect('equal')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Linear system solutions
ax2 = axes2[1]
t = np.linspace(0, 3, 500)

def sys(x, t):
    return [x[0] + x[1], x[0] - x[1]]

for x0 in [[1, 0], [0, 1], [1, 1]]:
    sol = odeint(sys, x0, t)
    ax2.plot(sol[:, 0], sol[:, 1], linewidth=2, label=f'$x_0={x0}$')

ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
ax2.set_title('Nghiệm với các điều kiên ban đầu khác nhau')
ax2.legend()
ax2.set_aspect('equal')
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_02_matrices_linear_systems.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-03: Real Distinct Eigenvalues
# =============================================================================
fig3, axes3 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Saddle point
ax1 = axes3[0]
A = np.array([[1, 0], [0, -1]])
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax1.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Điểm yên ngựa: $\\lambda_1=1, \\lambda_2=-1$\nEigenvalues thực, dấu khác nhau')
ax1.set_aspect('equal')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Node (both negative)
ax2 = axes3[1]
A = np.array([[-2, 0], [0, -1]])
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax2.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
ax2.set_title('Nút ổn định: $\\lambda_1=-2, \\lambda_2=-1$\nHai eigenvalue âm')
ax2.set_aspect('equal')
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_03_eigenvalue_real_distinct.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-04: Complex Eigenvalues
# =============================================================================
fig4, axes4 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Center (pure imaginary)
ax1 = axes4[0]
A = np.array([[0, 1], [-1, 0]])
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax1.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Tâm: $\\lambda = \\pm i$\nKhông cộng hưởng, dao động')
ax1.set_aspect('equal')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Spiral (complex with real part)
ax2 = axes4[1]
A = np.array([[-0.5, 1], [-1, -0.5]])
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax2.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
ax2.set_title('Xoắn ốc ổn định: $\\lambda = -0.5 \\pm i$\nPhần thực âm')
ax2.set_aspect('equal')
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_04_eigenvalue_complex.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-05: Repeated Eigenvalues
# =============================================================================
fig5, axes5 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Star node
ax1 = axes5[0]
A = np.array([[-1, 0], [0, -1]])
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax1.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_title('Nút sao: $\\lambda_1=\\lambda_2=-1$\nMa trận đơn vị')
ax1.set_aspect('equal')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Degenerate node
ax2 = axes5[1]
A = np.array([[-1, 1], [0, -1]])
X, Y = np.meshgrid(x, y)
U = A[0,0]*X + A[0,1]*Y
V = A[1,0]*X + A[1,1]*Y

ax2.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
ax2.set_title('Nút suy biến: $\\lambda=-1$ (bội)\nCần vector riêng thứ hai')
ax2.set_aspect('equal')
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_05_eigenvalue_repeated.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-06: Matrix Exponentials
# =============================================================================
fig6, axes6 = plt.subplots(1, 2, figsize=(14, 6))

# Left: e^(At)
ax1 = axes6[0]
t = np.linspace(0, 2, 500)
A = np.array([[0, 1], [-2, -3]])

for x0 in [[1, 0], [0, 1]]:
    sol = odeint(lambda x, t: A @ x, x0, t)
    ax1.plot(t, sol[:, 0], linewidth=2, label=f'$x_0={x0}$')

ax1.set_xlabel('$t$')
ax1.set_ylabel('$x(t)$')
ax1.set_title('Nghiệm: $\\mathbf{x}(t) = e^{At}\\mathbf{x}_0$\nMatrix exponential')
ax1.legend()
ax1.set_xlim(-0.2, 2.2)

# Right: e^(At) calculation
ax2 = axes6[1]
t = np.linspace(0, 2, 100)

# e^At = P diag(e^(lambda*t)) P^(-1)
# Use exact formula for A = [[0,1],[-1,-2]]
lam1 = -1
lam2 = -2

ax2.plot(t, np.exp(lam1*t), 'b-', linewidth=2, label='$e^{-t}$')
ax2.plot(t, np.exp(lam2*t), 'r-', linewidth=2, label='$e^{-2t}$')
ax2.set_xlabel('$t$')
ax2.set_ylabel('$e^{\\lambda t}$')
ax2.set_title('Thành phần eigenvalues\n$e^{At} = P e^{Dt} P^{-1}$')
ax2.legend()
ax2.set_xlim(-0.2, 2.2)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_06_matrix_exponentials.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-07: Phase Portraits
# =============================================================================
fig7, axes7 = plt.subplots(2, 3, figsize=(15, 10))

systems = [
    (np.array([[1, 0], [0, -1]]), 'Yên ngựa'),
    (np.array([[-2, 0], [0, -1]]), 'Nút ổn định'),
    (np.array([[2, 0], [0, 1]]), 'Nút không ổn định'),
    (np.array([[0, 1], [-1, 0]]), 'Tâm'),
    (np.array([[-0.5, 1], [-1, -0.5]]), 'Xoắn ốc ổn định'),
    (np.array([[0.5, 1], [-1, 0.5]]), 'Xoắn ốc không ổn định'),
]

for idx, (A, title) in enumerate(systems):
    ax = axes7[idx // 3, idx % 3]
    x = np.linspace(-2, 2, 15)
    y = np.linspace(-2, 2, 15)
    X, Y = np.meshgrid(x, y)
    U = A[0,0]*X + A[0,1]*Y
    V = A[1,0]*X + A[1,1]*Y
    ax.quiver(X, Y, U, V, np.sqrt(U**2+V**2), cmap='Blues', scale=20)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_07_phase_portraits.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-08: Nonhomogeneous Systems
# =============================================================================
fig8, axes8 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Forced system
ax1 = axes8[0]
t = np.linspace(0, 5, 500)

def sys(x, t):
    return [x[1], -x[0] + np.sin(t)]

x0 = [0, 0]
sol = odeint(sys, x0, t)

ax1.plot(t, sol[:, 0], 'b-', linewidth=2, label='$x_1(t)$')
ax1.plot(t, sol[:, 1], 'r-', linewidth=2, label='$x_2(t)$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$x(t)$')
ax1.set_title('Hệ có ngoại lực: $\\mathbf{x}\' = A\\mathbf{x} + \\mathbf{f}(t)$')
ax1.legend()
ax1.set_xlim(-0.3, 5.3)

# Right: Particular solution
ax2 = axes8[1]
# Homogeneous + particular
y_h = np.cos(t)
y_p = -0.5 * np.sin(t)

ax2.plot(t, y_h, 'b--', linewidth=2, alpha=0.7, label='$x_h$')
ax2.plot(t, y_p, 'g--', linewidth=2, alpha=0.7, label='$x_p$')
ax2.plot(t, y_h + y_p, 'r-', linewidth=2, label='$x = x_h + x_p$')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$x(t)$')
ax2.set_title('Nghiệm tổng: $\\mathbf{x} = \\mathbf{x}_h + \\mathbf{x}_p$')
ax2.legend()
ax2.set_xlim(-0.3, 5.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_08_nonhomogeneous_systems.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-09: Coupled Oscillators
# =============================================================================
fig9, axes9 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Two masses
ax1 = axes9[0]
t = np.linspace(0, 10, 500)

# Coupled: m1=x1'' = -k1*x1 + k2*(x2-x1), m2=x2'' = -k2*(x2-x1)
# With k1=k2=1, m1=m2=1
# System: x1'' = -2x1 + x2, x2'' = x1 - x2
# Transform: x' = v, v' = -2x + y, y' = w, w' = x - y

def sys(state, t):
    x1, v1, x2, v2 = state
    return [v1, -2*x1 + x2, v2, x1 - x2]

x0 = [1, 0, 0, 0]
sol = odeint(sys, x0, t)

ax1.plot(t, sol[:, 0], 'b-', linewidth=2, label='$x_1$')
ax1.plot(t, sol[:, 2], 'r-', linewidth=2, label='$x_2$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$x(t)$')
ax1.set_title('Dao động ghép: Hai khối\n$x_1\'\' = -2x_1 + x_2$')
ax1.legend()
ax1.set_xlim(-0.5, 10.5)

# Right: Normal modes
ax2 = axes9[1]
# Mode 1: both same direction (omega = sqrt(k/m))
# Mode 2: opposite direction (omega = sqrt((k+2k)/m))
t = np.linspace(0, 8, 500)
mode1 = np.cos(np.sqrt(1)*t)
mode2 = np.cos(np.sqrt(3)*t)

ax2.plot(t, mode1, 'b-', linewidth=2, label='Mode 1: $\\omega = 1$')
ax2.plot(t, mode2, 'r-', linewidth=2, label='Mode 2: $\\omega = \\sqrt{3}$')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$x(t)$')
ax2.set_title('Các mode riêng\nTần số tự nhiên')
ax2.legend()
ax2.set_xlim(-0.5, 8.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '04_09_coupled_oscillators.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 04-10: Compartment Models
# =============================================================================
fig10, axes10 = plt.subplots(1, 2, figsize=(14, 6))

# Left: 3 compartment
ax1 = axes10[0]
# 3 compartments: x1 -> x2 -> x3
# dx1/dt = -a12*x1
# dx2/dt = a12*x1 - a23*x2
# dx3/dt = a23*x2

t = np.linspace(0, 10, 500)
a12 = 0.5
a23 = 0.3

def comp(x, t):
    return [-a12*x[0], a12*x[0] - a23*x[1], a23*x[1]]

x0 = [100, 0, 0]
sol = odeint(comp, x0, t)

ax1.plot(t, sol[:, 0], 'b-', linewidth=2, label='$x_1$')
ax1.plot(t, sol[:, 1], 'r-', linewidth=2, label='$x_2$')
ax1.plot(t, sol[:, 2], 'g-', linewidth=2, label='$x_3$')
ax1.set_xlabel('$t$')
ax1.set_ylabel('$x(t)$')
ax1.set_title('Mô hình ngăn: $x_1 \\to x_2 \\to x_3$')
ax1.legend()
ax1.set_xlim(-0.5, 10.5)

# Right: Flow diagram
ax2 = axes10[1]
x = [0, 1, 2]
y = [0, 0, 0]
ax2.scatter(x, y, s=500, c=['blue', 'red', 'green'])
ax2.annotate('$x_1$', (0, 0), textcoords="offset points", xytext=(0, 20), fontsize=14, ha='center')
ax2.annotate('$x_2$', (1, 0), textcoords="offset points", xytext=(0, 20), fontsize=14, ha='center')
ax2.annotate('$x_3$', (2, 0), textcoords="offset points", xytext=(0, 20), fontsize=14, ha='center')
ax2.annotate('', (0.7, 0), (0.3, 0), arrowprops=dict(arrowstyle='->', lw=2))
ax2.annotate('', (1.7, 0), (1.3, 0), arrowprops=dict(arrowstyle='->', lw=2))
ax2.set_xlim(-0.5, 2.5)
ax2.set_ylim(-1, 1)
ax2.set_title('Sơ đồ dòng chảy\n$a_{12}, a_{23}$')
ax2.axis('off')

plt.tight_layout()
plt.savefig(IMG_PATH + '04_10_compartment_models.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 04:")
print("  04_01_introduction_systems.svg")
print("  04_02_matrices_linear_systems.svg")
print("  04_03_eigenvalue_real_distinct.svg")
print("  04_04_eigenvalue_complex.svg")
print("  04_05_eigenvalue_repeated.svg")
print("  04_06_matrix_exponentials.svg")
print("  04_07_phase_portraits.svg")
print("  04_08_nonhomogeneous_systems.svg")
print("  04_09_coupled_oscillators.svg")
print("  04_10_compartment_models.svg")