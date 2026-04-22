#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-02: Constant Coefficients - Distinct Real Roots
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Distinct Real Roots - Different Cases
# =============================================================================
fig1, axes1 = plt.subplots(1, 3, figsize=(16, 5))

# Left: Both negative (stable)
ax1 = axes1[0]
t = np.linspace(0, 4, 500)
# r^2 + 3r + 2 = 0 => r = -1, -2
for C1, C2 in [(1, 0), (0, 1), (1, 1)]:
    y = C1 * np.exp(-t) + C2 * np.exp(-2*t)
    ax1.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Hai nghiệm âm: $r_1=-1, r_2=-2$\n$\\to$ ổn định (decay)')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.3, 4.3)

# Middle: Both positive (unstable)
ax2 = axes1[1]
# r^2 - 3r + 2 = 0 => r = 1, 2
for C1, C2 in [(1, 0), (0, 1), (1, 1)]:
    y = C1 * np.exp(t) + C2 * np.exp(2*t)
    ax2.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Hai nghiệm dương: $r_1=1, r_2=2$\n$\\to$ không ổn định (grow)')
ax2.legend(loc='upper left')
ax2.set_xlim(-0.3, 2)

# Right: One pos, one neg
ax3 = axes1[2]
# r^2 - 1 = 0 => r = 1, -1
for C1, C2 in [(1, 0), (0, 1), (1, 1)]:
    y = C1 * np.exp(-t) + C2 * np.exp(t)
    ax3.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}$')

ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlabel('$t$')
ax3.set_ylabel('$y(t)$')
ax3.set_title('Một âm, một dương: $r = \\pm 1$\n$\\to$ yếu tố tăng trưởng chiếm ưu thế')
ax3.legend(loc='upper left')
ax3.set_xlim(-0.3, 3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_02_real_roots_cases.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Characteristic Equation Visualization
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

r = np.linspace(-3, 3, 500)
# Characteristic: r^2 + 3r + 2 = 0
char_eq = r**2 + 3*r + 2

ax.plot(r, char_eq, 'b-', linewidth=2)
ax.axhline(y=0, color='black', linewidth=1)
ax.axvline(x=0, color='black', linewidth=0.5)

# Mark roots
ax.scatter([-2, -1], [0, 0], color='red', s=150, zorder=5)
ax.annotate('$r_1 = -2$', (-2, 0), textcoords="offset points", xytext=(-30, 15), fontsize=12)
ax.annotate('$r_2 = -1$', (-1, 0), textcoords="offset points", xytext=(10, 15), fontsize=12)

ax.set_xlabel('$r$')
ax.set_ylabel('$r^2 + 3r + 2$')
ax.set_title('Phương trình đặc trưng: $ar^2 + br + c = 0$\nNghiệm = điểm cắt trục $r$')
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3, 10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_02_characteristic.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-02:")
print("  02_02_real_roots_cases.svg")
print("  02_02_characteristic.svg")