#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-03: Linear First-Order Equations
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Linear First Order - Integrating Factor Visualization
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: y' + y = 1 (steady state solution)
ax1 = axes1[0]
t = np.linspace(0, 5, 500)

for C in [-2, -1, 0, 1, 2]:
    y = 1 + C * np.exp(-t)
    ax1.plot(t, y, linewidth=2, label=f'$C = {C}$')

ax1.axhline(y=1, color='red', linestyle='--', linewidth=2, label='$y = 1$ (steady state)')
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Nghiệm của $y\' + y = 1$\n$y = 1 + Ce^{-t}$')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.3, 5.3)
ax1.set_ylim(-3, 5)

# Right: y' + 2y = e^(-t)
ax2 = axes1[1]
t = np.linspace(0, 3, 500)

# Solution: y = e^(-t) + Ce^(-2t)
for C in [0, 1, 2, 3]:
    y = np.exp(-t) + C * np.exp(-2*t)
    ax2.plot(t, y, linewidth=2, label=f'$C = {C}$')

ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Nghiệm của $y\' + 2y = e^{-t}$\n$y = e^{-t} + Ce^{-2t}$')
ax2.legend(loc='upper right')
ax2.set_xlim(-0.3, 3.3)
ax2.set_ylim(0, 3)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_03_linear_first_order.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Integrating Factor Concept
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

t = np.linspace(0, 4, 500)

# Show p(t) and mu(t) relationship
# p(t) = t, mu(t) = e^(t^2/2)
ax.plot(t, t, 'b-', linewidth=2, label=r'$p(t) = t$')
ax.plot(t, np.exp(t**2/2), 'r-', linewidth=2, label=r'$\mu(t) = e^{\int p(t)dt} = e^{t^2/2}$')

ax.set_xlabel('$t$')
ax.set_ylabel('Value')
ax2 = ax.twinx()
ax2.plot(t, t**2/2, 'g--', linewidth=1.5, alpha=0.7, label=r'$\int p(t)dt = t^2/2$')

ax.set_title('Quan hệ giữa $p(t)$ và $\\mu(t)$\n$\\mu(t) = e^{\\int p(t)dt}$')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
ax.set_xlim(-0.3, 4.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_03_integrating_factor.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-03:")
print("  01_03_linear_first_order.svg")
print("  01_03_integrating_factor.svg")
