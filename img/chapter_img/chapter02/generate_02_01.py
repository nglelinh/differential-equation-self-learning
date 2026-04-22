#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-01: Second-Order Linear Equations Overview
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Second Order - Oscillatory vs Non-oscillatory
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Simple harmonic y'' + w^2*y = 0
ax1 = axes1[0]
t = np.linspace(0, 4*np.pi, 500)
w = 1

for A, B in [(1, 0), (0, 1), (1, 1)]:
    y = A * np.cos(w*t) + B * np.sin(w*t)
    ax1.plot(t, y, linewidth=2, label=f'$A={A}, B={B}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title(r'Dao động điều hòa: $y\'\' + \omega^2 y = 0$' + f'\n$y = A\\cos(\\omega t) + B\\sin(\\omega t)$')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.5, 13)

# Right: y'' - 3y' + 2y = 0 (distinct real roots)
ax2 = axes1[1]
# Characteristic: r^2 - 3r + 2 = 0 => r = 1, 2
for C1, C2 in [(1, 0), (0, 1), (1, 1)]:
    y = C1 * np.exp(t) + C2 * np.exp(2*t)
    ax2.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title(r'Nghiệm mũ: $y\'\' - 3y\' + 2y = 0$' + '\n$y = C_1e^{t} + C_2e^{2t}$')
ax2.legend(loc='upper left')
ax2.set_xlim(-0.5, 3)
ax2.set_ylim(-5, 20)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_01_second_order_overview.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: General Solution Structure
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Homogeneous + Particular
ax1 = axes2[0]
t = np.linspace(0, 6, 500)

y_h = np.exp(-t)  # homogeneous
y_p = 2 * np.ones_like(t)  # particular (constant)
y_total = y_h + y_p

ax1.plot(t, y_h, 'b--', linewidth=2, label='$y_h$ (nghiệm thuần nhất)')
ax1.plot(t, y_p, 'g:', linewidth=2, label='$y_p$ (nghiệm riêng)')
ax1.plot(t, y_total, 'r-', linewidth=2, label='$y = y_h + y_p$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Cấu trúc nghiệm: $y = y_h + y_p$\nTổng quát = Thuần nhất + Riêng')
ax1.legend(loc='right')
ax1.set_xlim(-0.5, 6.5)

# Right: Two initial conditions
ax2 = axes2[1]
# Solve y'' + y = 0 with y(0)=y0, y'(0)=v0
# y = y0*cos(t) + v0*sin(t)
for y0, v0 in [(1, 0), (0, 1), (1, 1)]:
    y = y0 * np.cos(t) + v0 * np.sin(t)
    ax2.plot(t, y, linewidth=2, label=f'$y(0)={y0}, y\'(0)={v0}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Hai điều kiên ban đầu\nXác định duy nhất một nghiệm')
ax2.legend(loc='upper right')
ax2.set_xlim(-0.5, 7)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_01_general_solution.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-01:")
print("  02_01_second_order_overview.svg")
print("  02_01_general_solution.svg")