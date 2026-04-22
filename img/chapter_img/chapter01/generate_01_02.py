#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-02: Separable Equations
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Separable Equations - Separation of Variables Visualization
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Show dy/dx = y * sin(x) solution
ax1 = axes1[0]
x = np.linspace(0, 6, 500)

# Solution: y = Ce^(-cos(x))
for C in [0.5, 1, 1.5, 2]:
    y = C * np.exp(-np.cos(x))
    ax1.plot(x, y, linewidth=2, label=f'$C = {C}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('Nghiệm của $\\dfrac{dy}{dx} = y\\sin x$\n$y = Ce^{-\\cos x}$')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.3, 6.3)
ax1.set_ylim(0, 8)

# Right: Separable equation dy/dx = (1-y^2)
ax2 = axes1[1]
x = np.linspace(-2, 2, 500)

# Solutions: y = tanh(x + C), y = coth(x + C), y = ±1
x_plot = np.linspace(-2, 2, 500)

# y = tanh(x + C) for different C
for C in [-1, 0, 1]:
    y = np.tanh(x_plot + C)
    ax2.plot(x_plot, y, 'b-', linewidth=2, label=f'$y = \\tanh(x + {C})$')

# y = 1 and y = -1 (equilibrium solutions)
ax2.axhline(y=1, color='red', linestyle='--', linewidth=2, label='$y = \\pm 1$ (cân bằng)')
ax2.axhline(y=-1, color='red', linestyle='--', linewidth=2)

ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Nghiệm của $\\dfrac{dy}{dx} = 1 - y^2$\n$y = \\tanh(x+C)$, $y = \\pm 1$')
ax2.legend(loc='right')
ax2.set_xlim(-2.3, 2.3)
ax2.set_ylim(-3, 3)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_02_separable_equations.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Exponential Growth and Decay
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Exponential Growth
ax1 = axes2[0]
t = np.linspace(0, 5, 500)
k = 0.8

for C in [0.5, 1, 2]:
    y = C * np.exp(k * t)
    ax1.plot(t, y, linewidth=2, label=f'$y(0) = {C}$')

ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Tăng trưởng mũ: $\\dfrac{dy}{dt} = ky$, $k > 0$\n$y(t) = y(0)e^{kt}$')
ax1.legend()
ax1.set_xlim(-0.3, 5.3)
ax1.set_ylim(0, 25)

# Right: Exponential Decay
ax2 = axes2[1]
k = 0.8

for C in [5, 10, 15]:
    y = C * np.exp(-k * t)
    ax2.plot(t, y, linewidth=2, label=f'$y(0) = {C}$')

ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Giảm mũ: $\\dfrac{dy}{dt} = -ky$, $k > 0$\n$y(t) = y(0)e^{-kt}$')
ax2.legend()
ax2.set_xlim(-0.3, 5.3)
ax2.set_ylim(0, 20)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_02_growth_decay.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-02:")
print("  01_02_separable_equations.svg")
print("  01_02_growth_decay.svg")