#!/usr/bin/env python3
"""
Generate educational images for Chapter 00 lessons
Lesson 00-03: Derivatives and Multivariable Calculus
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# =============================================================================
# Figure 1: Gradient field visualization (2D)
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Surface f(x,y) = x^2 + y^2 - contour plot
ax1 = axes1[0]
X = np.linspace(-2, 2, 30)
Y = np.linspace(-2, 2, 30)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2

contour = ax1.contourf(X, Y, Z, levels=15, cmap='viridis')
plt.colorbar(contour, ax=ax1, label='$f(x,y)$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Đường đồng mức của $f(x,y) = x^2 + y^2$')

# Show gradient at specific points
test_points = [(0.5, 0.5), (1, 0), (0, 1), (-0.5, -0.5)]
for xp, yp in test_points:
    grad_x = 2*xp
    grad_y = 2*yp
    ax1.quiver(xp, yp, grad_x, grad_y, color='red', scale=8, width=0.005)
    ax1.scatter([xp], [yp], color='red', s=50, zorder=5)

ax1.annotate('$\\nabla f = (2x, 2y)$', xy=(1.2, 1.2), fontsize=11, color='white')

# Right: gradient direction
ax2 = axes1[1]
contour2 = ax2.contour(X, Y, Z, levels=10, cmap='viridis')
ax2.clabel(contour2, inline=True, fontsize=8)

# Gradient field arrows
step = 5
for i in range(0, 30, step):
    for j in range(0, 30, step):
        x_val, y_val = X[i, j], Y[i, j]
        grad_x = 2*x_val
        grad_y = 2*y_val
        norm = np.sqrt(grad_x**2 + grad_y**2)
        if norm > 0.1:
            ax2.quiver(x_val, y_val, grad_x, grad_y, color='red', alpha=0.7, scale=15, width=0.004)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Trường gradient: Mũi tên chỉ hướng tăng nhanh nhất\n$\\nabla f$ vuông góc với đường đồng mức')

plt.tight_layout()
plt.savefig('00_03_01_gradient_visualization.svg', dpi=150, 
            bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_03_01_gradient_visualization.svg")

# =============================================================================
# Figure 2: Chain rule visualization
# =============================================================================
fig2, ax = plt.subplots(figsize=(12, 6))

# Show chain rule: z = f(x,y), x = g(t), y = h(t)
t = np.linspace(0, 2*np.pi, 200)
x = np.sin(t)
y = np.cos(t)
z = x**2 + y**2  # = sin^2(t) + cos^2(t) = 1

# Plot x(t) and y(t)
ax.plot(t, x, 'b-', linewidth=2, label='$x(t) = \\sin(t)$')
ax.plot(t, y, 'g-', linewidth=2, label='$y(t) = \\cos(t)$')
ax.plot(t, z, 'r-', linewidth=3, label='$z(t) = x^2 + y^2 = 1$')

ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('$t$')
ax.set_ylabel('Giá trị')
ax.set_title('Quy tắc dây chuyền: $\\frac{dz}{dt} = \\frac{\\partial f}{\\partial x}\\frac{dx}{dt} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dt}$')
ax.legend()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Add annotation
ax.annotate('$z(t) = 1$ (hằng số)\nnên $z\'(t) = 0$', xy=(np.pi/2, 1), xytext=(3, 0.5),
            fontsize=10, arrowprops=dict(arrowstyle='->', color='red'))

plt.tight_layout()
plt.savefig('00_03_02_chain_rule.svg', dpi=150, 
            bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_03_02_chain_rule.svg")

# =============================================================================
# Figure 3: Jacobian as linear approximation
# =============================================================================
fig3, axes3 = plt.subplots(1, 2, figsize=(14, 6))

# Left: contour with tangent line
ax1 = axes3[0]
contour = ax1.contour(X, Y, Z, levels=10, cmap='viridis')
ax1.clabel(contour, inline=True, fontsize=8)

# Show gradient at (0.5, 0.5)
x0, y0 = 0.5, 0.5
grad_x, grad_y = 2*x0, 2*y0
ax1.quiver([x0], [y0], [grad_x], [grad_y], color='red', scale=6, width=0.006)
ax1.scatter([x0], [y0], color='red', s=100, zorder=5)

# Tangent line perpendicular to gradient
tangent_x = np.linspace(-0.5, 1.5, 50)
tangent_y = y0 - (grad_x/grad_y) * (tangent_x - x0)
ax1.plot(tangent_x, tangent_y, 'r--', linewidth=2, label='Tiếp tuyến')
ax1.set_xlim(-0.5, 1.5)
ax1.set_ylim(-0.5, 1.5)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Gradient tại $(x_0, y_0)$: vuông góc với đường tiếp tuyến')
ax1.legend()

# Right: Jacobian as transformation
ax2 = axes3[1]
theta = np.linspace(0, 2*np.pi, 100)
x_orig = np.cos(theta)
y_orig = np.sin(theta)

# Apply a linear transformation (Jacobian)
J = np.array([[1.5, 0.5], [0.5, 1.5]])
transformed = np.array([J @ [x, y] for x, y in zip(x_orig, y_orig)])

ax2.plot(x_orig, y_orig, 'b-', linewidth=2, label='Hình tròn đơn vị')
ax2.plot(transformed[:, 0], transformed[:, 1], 'r-', linewidth=2, label='Biến dạng bởi Jacobian')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Jacobian như phép biến đổi tuyến tính cục bộ')
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')
ax2.legend()
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig('00_03_03_jacobian.svg', dpi=150, 
            bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_03_03_jacobian.svg")

print("\nAll images generated successfully!")