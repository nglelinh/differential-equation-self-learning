#!/usr/bin/env python3
"""
Generate educational images for Chapter 00 - Vector Calculus
Lesson 00-10: Gradient, Divergence, Curl + 3 Integral Theorems
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle
from matplotlib.collections import PatchCollection, LineCollection
import matplotlib.colors as mcolors

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter00/'

# =============================================================================
# Figure 1: Gradient - Direction of Steepest Ascent
# =============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 8))

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

contour = ax1.contour(X, Y, Z, levels=15, cmap='viridis', alpha=0.8)
ax1.clabel(contour, inline=True, fontsize=8, fmt='%.1f')

ax1.plot([0], [0], 'ko', markersize=10, label='Đỉnh núi $f = 0$')
ax1.plot([1.5], [1.5], 'ro', markersize=10, label='Điểm $P$')

ax1.annotate('', xy=(1.5, 1.5), xytext=(0.8, 0.8),
            arrowprops=dict(arrowstyle='->', color='red', lw=3))
ax1.text(1.1, 1.1, r'$\nabla f$', fontsize=16, color='red',
        fontweight='bold')

ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title(r'Gradient: $\nabla f$ chỉ hướng tăng nhanh nhất' + '\nCác đường đồng mức (level curves)')
ax1.set_xlim(-2.2, 2.2)
ax1.set_ylim(-2.2, 2.2)
ax1.set_aspect('equal')
ax1.legend(loc='upper right')

plt.tight_layout()
plt.savefig(IMG_PATH + '00_10_gradient.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Divergence - Source and Sink
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Positive divergence (source)
ax_left = axes2[0]
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
F = X, Y
U, V = X, Y

ax_left.quiver(X, Y, U, V, color='blue', scale=30, width=0.003)
ax_left.add_patch(Circle((0, 0), 0.3, fill=True, color='red', alpha=0.7))
ax_left.text(0, 0, 'Nguồn\n(+)', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
ax_left.set_xlabel('$x$')
ax_left.set_ylabel('$y$')
ax_left.set_title(r'Divergence > 0: Nguồn (Source)' + '\n$F = (x, y)$')
ax_left.set_xlim(-2.5, 2.5)
ax_left.set_ylim(-2.5, 2.5)
ax_left.set_aspect('equal')

# Right: Negative divergence (sink)
ax_right = axes2[1]
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
U = -X
V = -Y

ax_right.quiver(X, Y, U, V, color='blue', scale=30, width=0.003)
ax_right.add_patch(Circle((0, 0), 0.3, fill=True, color='green', alpha=0.7))
ax_right.text(0, 0, 'Bể\n(-)', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
ax_right.set_xlabel('$x$')
ax_right.set_ylabel('$y$')
ax_right.set_title(r'Divergence < 0: Bể (Sink)' + '\n$F = (-x, -y)$')
ax_right.set_xlim(-2.5, 2.5)
ax_right.set_ylim(-2.5, 2.5)
ax_right.set_aspect('equal')

plt.tight_layout()
plt.savefig(IMG_PATH + '00_10_divergence.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 3: Curl - Rotation/Vortex
# =============================================================================
fig3, ax3 = plt.subplots(figsize=(10, 8))

x = np.linspace(-2, 2, 25)
y = np.linspace(-2, 2, 25)
X, Y = np.meshgrid(x, y)
F = -Y, X
U, V = -Y, X

ax3.quiver(X, Y, U, V, color='purple', scale=30, width=0.003)

theta = np.linspace(0, 2*np.pi, 100)
r = 1.5
ax3.plot(r*np.cos(theta), r*np.sin(theta), 'r-', linewidth=3, label='Đườngcong kín')

ax3.annotate('', xy=(0, 1.5), xytext=(0.1, 1.4),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax3.text(0.2, 1.5, r'$\oint F\cdot dr \neq 0$', fontsize=12, color='red')

ax3.add_patch(Circle((0, 0), 0.15, fill=True, color='orange', alpha=0.8))
ax3.text(0, 0, 'Curl\n$\neq 0$', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

ax3.set_xlabel('$x$')
ax3.set_ylabel('$y$')
ax3.set_title(r'Curl: Hiện tượng xoáy' + '\n$F = (-y, x)$ — trường quay')
ax3.set_xlim(-2.5, 2.5)
ax3.set_ylim(-2.5, 2.5)
ax3.set_aspect('equal')
ax3.legend(loc='upper right')

plt.tight_layout()
plt.savefig(IMG_PATH + '00_10_curl.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 4: Green's Theorem - Line Integral around boundary
# =============================================================================
fig4, ax4 = plt.subplots(figsize=(10, 8))

theta = np.linspace(0, 2*np.pi, 100)
a, b = 1.5, 1.0
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)
ax4.plot(x_ellipse, y_ellipse, 'b-', linewidth=3, label='Đường cong kín $C$ (biên)')

ax4.fill(x_ellipse, y_ellipse, alpha=0.3, color='lightblue', label='Miền $D$')

ax4.annotate('', xy=(x_ellipse[30], y_ellipse[30]), 
            xytext=(x_ellipse[30]-0.3, y_ellipse[30]-0.2),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax4.text(-0.8, 0.5, '$\\oint_C P\\,dx + Q\\,dy$', fontsize=14, color='red', fontweight='bold')

ax4.text(0, 0, '$D$\n(miền 2D)', ha='center', va='center', fontsize=12)
ax4.text(1.6, 0, '$C$\n(biên 1D)', ha='left', va='center', fontsize=10)

ax4.set_xlabel('$x$')
ax4.set_ylabel('$y$')
ax4.set_title('Định lý Green: Từ đường biên $C$ đến miền $D$\n' + 
             r'$\oint_C P\,dx + Q\,dy = \iint_D (\partial Q/\partial x - \partial P/\partial y)\,dA$')
ax4.set_xlim(-2.5, 2.5)
ax4.set_ylim(-2, 2)
ax4.set_aspect('equal')
ax4.legend(loc='upper right')

plt.tight_layout()
plt.savefig(IMG_PATH + '00_10_green_theorem.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 5: Stokes' Theorem - Surface and boundary
# =============================================================================
fig5 = plt.figure(figsize=(12, 8))
ax5 = fig5.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, np.pi/2, 20)
U, V = np.meshgrid(u, v)
X = 1.5 * np.cos(U) * np.sin(V)
Y = 1.5 * np.sin(U) * np.sin(V)
Z = np.cos(V)

ax5.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis', edgecolor='blue', linewidth=0.5)

theta = np.linspace(0, 2*np.pi, 50)
x_boundary = 1.5 * np.cos(theta)
y_boundary = 1.5 * np.sin(theta)
z_boundary = np.zeros_like(theta)
ax5.plot(x_boundary, y_boundary, z_boundary, 'r-', linewidth=3, label='$\\partial S$')

ax5.plot(x_boundary, y_boundary, z_boundary + 0.05, 'r--', linewidth=2, alpha=0.5)

ax5.text(0, 0, 1.2, '$S$\n(mặt 2D)', ha='center', va='bottom', fontsize=12)
ax5.text(2, 0, 0, '$\partial S$\n(biên 1D)', ha='left', va='center', fontsize=10)

ax5.set_xlabel('$x$')
ax5.set_ylabel('$y$')
ax5.set_zlabel('$z$')
ax5.set_title('Định lý Stokes: Từ mặt $S$ đến biên $\partial S$\n' +
             r'$\oint_{\partial S} F\cdot dr = \iint_S (\nabla \times F)\cdot n\,dS$')
ax5.legend()

plt.tight_layout()
plt.savefig(IMG_PATH + '00_10_stokes_theorem.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 6: Gauss' Theorem - Volume and surface
# =============================================================================
fig6 = plt.figure(figsize=(12, 8))
ax6 = fig6.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, np.pi, 20)
phi, theta = np.meshgrid(u, v)
X = 1.5 * np.sin(theta) * np.cos(phi)
Y = 1.5 * np.sin(theta) * np.sin(phi)
Z = 1.5 * np.cos(theta)

ax6.plot_surface(X, Y, Z, alpha=0.5, cmap='coolwarm', edgecolor='blue', linewidth=0.5)

ax6.text(0, 0, 0, '$V$\n(thể tích 3D)', ha='center', va='center', fontsize=12)
ax6.text(2, 0, 0, '$\partial S$\n(mặt 2D)', ha='left', va='center', fontsize=10)

ax6.set_xlabel('$x$')
ax6.set_ylabel('$y$')
ax6.set_zlabel('$z$')
ax6.set_title('Định lý Gauss: Từ thể tích $V$ đến mặt $\partial S$\n' +
             r'$\iiint_V (\nabla \cdot F)\,dV = \iint_{\partial S} F\cdot n\,dS$')

plt.tight_layout()
plt.savefig(IMG_PATH + '00_10_gauss_theorem.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 00-10 Vector Calculus:")
print("  00_10_gradient.svg")
print("  00_10_divergence.svg")
print("  00_10_curl.svg")
print("  00_10_green_theorem.svg")
print("  00_10_stokes_theorem.svg")
print("  00_10_gauss_theorem.svg")