#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-07: Higher Order Equations
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Higher Order Characteristic
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Third order roots
ax1 = axes1[0]
# r^3 - 6r^2 + 11r - 6 = 0 => r = 1, 2, 3
t = np.linspace(0, 3, 500)
for C1, C2, C3 in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]:
    y = C1*np.exp(t) + C2*np.exp(2*t) + C3*np.exp(3*t)
    ax1.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}, C_3={C3}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Phương trình bậc 3: $r=1,2,3$\n$y = C_1e^{t} + C_2e^{2t} + C_3e^{3t}$')
ax1.legend(loc='upper left')
ax1.set_xlim(-0.3, 3.3)

# Right: Complex roots in higher order
ax2 = axes1[1]
# r^3 + r = 0 => r(r^2+1) = 0 => r=0, r=±i
t = np.linspace(0, 4*np.pi, 500)
# y = C1 + C2*cos(t) + C3*sin(t)
for C1, C2, C3 in [(0, 1, 0), (0, 0, 1), (1, 1, 1)]:
    y = C1 + C2*np.cos(t) + C3*np.sin(t)
    ax2.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}, C_3={C3}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Bậc 3 với nghiệm phức: $r=0, \\pm i$\n$y = C_1 + C_2\\cos(t) + C_3\\sin(t)$')
ax2.legend(loc='upper right')
ax2.set_xlim(-0.5, 13)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_07_higher_order_equations.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-07:")
print("  02_07_higher_order_equations.svg")