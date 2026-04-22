#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-09: Autonomous Equations and Phase Lines
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Phase Line and Solutions
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Phase line for logistic equation
ax1 = axes1[0]
y = np.linspace(-1, 11, 500)
f = 0.5 * y * (1 - y/10)  # logistic: dy/dt = 0.5*y*(1 - y/10)

ax1.plot(y, f, 'b-', linewidth=2)
ax1.axhline(y=0, color='black', linewidth=1)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.axvline(x=10, color='black', linewidth=0.5)

# Mark equilibria
ax1.scatter([0, 10], [0, 0], color='red', s=150, zorder=5)
ax1.annotate('Cân bằng\n(không ổn định)', (0, 0), textcoords="offset points", xytext=(-60, 20), fontsize=10, ha='center')
ax1.annotate('Cân bằng\n(ổn định)', (10, 0), textcoords="offset points", xytext=(15, 20), fontsize=10, ha='center')

# Arrows on phase line
ax1.annotate('', xy=(5, 0.3), xytext=(2, 0.3), arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax1.annotate('', xy=(8, 0.3), xytext=(9.5, 0.3), arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax1.annotate('', xy=(2, -0.3), xytext=(0.5, -0.3), arrowprops=dict(arrowstyle='<-', color='red', lw=2))

ax1.set_xlabel('$y$')
ax1.set_ylabel('$f(y) = 0.5y(1-y/10)$')
ax1.set_title('Đường pha cho phương trình logistic\n$y\' = 0.5y(1-y/10)$')
ax1.set_xlim(-1, 11)
ax1.set_ylim(-2, 3)
ax1.set_aspect('equal', adjustable='box')

# Right: Solution curves
ax2 = axes1[1]
t = np.linspace(0, 15, 500)

# Logistic solutions
K = 10
r = 0.5
for y0 in [1, 3, 5, 8, 11, 15]:
    y = K / (1 + ((K-y0)/y0) * np.exp(-r*t))
    ax2.plot(t, y, linewidth=2, label=f'$y(0) = {y0}$')

ax2.axhline(y=10, color='red', linestyle='--', linewidth=2, alpha=0.7)
ax2.axhline(y=0, color='red', linestyle='--', linewidth=2, alpha=0.7)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Nghiệm của phương trình logistic\n$Hướng tới $K=10$')
ax2.legend(loc='right')
ax2.set_xlim(-1, 16)
ax2.set_ylim(0, 18)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_09_autonomous_equations.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Different Stability Types
# =============================================================================
fig2, axes2 = plt.subplots(1, 3, figsize=(16, 5))

# Left: Stable (sink)
ax1 = axes2[0]
y = np.linspace(-1, 3, 500)
f = -y + 1  # dy/dt = 1 - y (stable at y=1)

ax1.plot(y, f, 'b-', linewidth=2)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=1, color='red', linewidth=2)
ax1.scatter([1], [0], color='red', s=150, zorder=5)
ax1.annotate('Ổn định\n(sink)', (1, 0), textcoords="offset points", xytext=(15, 15), fontsize=11)
ax1.set_xlabel('$y$')
ax1.set_ylabel('$y\'$')
ax1.set_title(r'$\ y\' = 1 - y$ (ổn định)')
ax1.set_xlim(-0.5, 2.5)
ax1.set_ylim(-2, 2)

# Middle: Unstable (source)
ax2 = axes2[1]
f = y - 1  # dy/dt = y - 1 (unstable at y=1)

ax2.plot(y, f, 'b-', linewidth=2)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=1, color='red', linewidth=2)
ax2.scatter([1], [0], color='red', s=150, zorder=5)
ax2.annotate('Không ổn định\n(source)', (1, 0), textcoords="offset points", xytext=(15, 15), fontsize=11)
ax2.set_xlabel('$y$')
ax2.set_ylabel('$y\'$')
ax2.set_title(r'$y\' = y - 1$ (không ổn định)')
ax2.set_xlim(-0.5, 2.5)
ax2.set_ylim(-2, 2)

# Right: Semi-stable
ax3 = axes2[2]
f = (y - 1)**2  # dy/dt = (y-1)^2 (semi-stable)

ax3.plot(y, f, 'b-', linewidth=2)
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.axvline(x=1, color='red', linewidth=2)
ax3.scatter([1], [0], color='red', s=150, zorder=5)
ax3.annotate('Bán ổn định', (1, 0), textcoords="offset points", xytext=(15, 15), fontsize=11)
ax3.set_xlabel('$y$')
ax3.set_ylabel('$y\'$')
ax3.set_title(r'$y\' = (y-1)^2$ (bán ổn định)')
ax3.set_xlim(-0.5, 2.5)
ax3.set_ylim(-0.5, 2)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_09_stability_types.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-09:")
print("  01_09_autonomous_equations.svg")
print("  01_09_stability_types.svg")
