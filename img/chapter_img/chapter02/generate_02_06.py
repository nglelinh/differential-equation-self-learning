#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-06: Variation of Parameters
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Variation of Parameters Concept
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Wronskian visualization
ax1 = axes1[0]
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
X, Y = np.meshgrid(x, y)

# Wronskian of cos(t), sin(t) = 1 (constant)
wronskian = np.ones_like(X)
contour = ax1.contourf(X, Y, wronskian, levels=20, cmap='Blues')
plt.colorbar(contour, ax=ax1, label='$W = 1$')

ax1.set_xlabel('$y_1$')
ax1.set_ylabel('$y_2$')
ax1.set_title('Wronskian $W(y_1, y_2) = 1$\nHệ số không đổi → Dễ tính nghiệm riêng')
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)

# Right: Variation of parameters formula
ax2 = axes1[1]
t = np.linspace(0, 4, 500)

# y'' + y = sec(t) (non-constant RHS)
# yp = y1*u1 + y2*u2 where u1' = -y2*g/W, u2' = y1*g/W
# For g = 1 (constant), u1' = -sin(t), u2' = cos(t)
# u1 = cos(t), u2 = sin(t)
# yp = cos(t)*cos(t) + sin(t)*sin(t) = 1
y_p = np.ones_like(t)

ax2.plot(t, y_p, 'r-', linewidth=2, label='$y_p = 1$')
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y_p(t)$')
ax2.set_title('Công thức biến thiên tham số\n$y_p = y_1u_1\' + y_2u_2\'$')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.legend()
ax2.set_xlim(-0.3, 4.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_06_variation_of_parameters.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: General Method
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

# Show that variation of parameters works for any g(t)
t = np.linspace(0, 3, 500)

# Example: y'' + y = 1/t (has singularity)
# Near t=0, use L'Hopital
y_p = np.ones_like(t)  # as particular solution

ax.plot(t, y_p, 'b-', linewidth=2, label='Nghiệm riêng $y_p$')
ax.set_xlabel('$t$')
ax2.set_ylabel('$y_p(t)$')
ax.set_title('Biến thiên tham số cho mọi $g(t)$\nKhông cần đoán dạng!')
ax2.legend()
ax2.set_xlim(-0.3, 3.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_06_method.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-06:")
print("  02_06_variation_of_parameters.svg")
print("  02_06_method.svg")