#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-04: Exact Equations
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Exact Equation - Potential Function Contours
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: F(x,y) = x^2 + y^2 = C (circles)
ax1 = axes1[0]
x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

contour = ax1.contour(X, Y, Z, levels=[1, 2, 4, 9, 16], cmap='viridis')
ax1.clabel(contour, inline=True, fontsize=10, fmt='C=%1.0f')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Nghiệm của $2xdx + 2ydy = 0$\n$F(x,y) = x^2 + y^2 = C$')
ax1.set_aspect('equal')
ax1.set_xlim(-3.5, 3.5)
ax1.set_ylim(-3.5, 3.5)

# Right: F(x,y) = x^2 - y^2 = C (hyperbolas)
ax2 = axes1[1]
Z2 = X**2 - Y**2

contour2 = ax2.contour(X, Y, Z2, levels=[-4, -2, 0, 2, 4], cmap='coolwarm')
ax2.clabel(contour2, inline=True, fontsize=10, fmt='C=%1.0f')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Nghiệm của $2xdx - 2ydy = 0$\n$F(x,y) = x^2 - y^2 = C$')
ax2.set_aspect('equal')
ax2.set_xlim(-3.5, 3.5)
ax2.set_ylim(-3.5, 3.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_04_exact_equations.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Exact vs Non-Exact visualization
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Exact equation field
ax1 = axes2[0]
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# For M = 2x, N = 2y (exact), direction is radially outward/inward
U = 2*X
V = 2*Y
M = np.sqrt(U**2 + V**2)
U_norm = U / (M + 0.001)
V_norm = V / (M + 0.001)

ax1.quiver(X, Y, U_norm, V_norm, M, cmap='Blues', scale=25)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Trường vector cho phương trình chính xác\n$M=2x, N=2y$: $\\partial M/\\partial y = \\partial N/\\partial x = 0$')
ax1.set_aspect('equal')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Non-exact (show why it fails)
ax2 = axes2[1]
# For M = y, N = x (not exact, since dM/dy = 1, dN/dx = 1 actually exact!)
# Let's use M = y^2, N = x*y (not exact: dM/dy = 2y, dN/dx = y)
U = y**2
V = X*Y
M2 = np.sqrt(U**2 + V**2 + 0.001)
U2_norm = U / (M2 + 0.001)
V2_norm = V / (M2 + 0.001)

ax2.quiver(X, Y, U2_norm, V2_norm, M2, cmap='Reds', scale=25)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Trường vector cho phương trình không chính xác\n$M=y^2, N=xy$: $\\partial M/\\partial y = 2y \\neq \\partial N/\\partial x = y$')
ax2.set_aspect('equal')
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_04_exact_vs_nonexact.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-04:")
print("  01_04_exact_equations.svg")
print("  01_04_exact_vs_nonexact.svg")
