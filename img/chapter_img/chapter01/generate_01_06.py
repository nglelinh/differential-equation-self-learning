#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-06: Existence and Uniqueness
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Existence vs Uniqueness Visualization
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Unique solution - y' = y
ax1 = axes1[0]
t = np.linspace(-1, 1, 500)

for C in [-1, -0.5, 0, 0.5, 1]:
    y = C * np.exp(t)
    ax1.plot(t, y, linewidth=2)

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.scatter([0], [1], color='red', s=100, zorder=5)
ax1.annotate('$(0,1)$', (0, 1), textcoords="offset points", xytext=(10, 5), fontsize=12)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.set_title('Tồn tại và duy nhất: $y\' = y$, $y(0)=1$\nMột nghiệm duy nhất qua mỗi điểm')
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-2, 3)

# Right: Non-unique solution - y' = y^(1/3)
ax2 = axes1[1]
t = np.linspace(0, 1, 500)

# Multiple solutions through (0,0): y = 0, y = (±t)^(3/2)
# y = 0
ax2.plot(t, np.zeros_like(t), 'b-', linewidth=2, label='$y = 0$')

# y = (t/√2)^3 for t>=0
t_pos = np.linspace(0, 1, 200)
y_pos = np.power(t_pos / np.sqrt(2), 3)
ax2.plot(t_pos, y_pos, 'r-', linewidth=2, label='$y = (t/\\sqrt{2})^3$')

y_neg = -np.power(t_pos / np.sqrt(2), 3)
ax2.plot(t_pos, y_neg, 'g-', linewidth=2, label='$y = -(t/\\sqrt{2})^3$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)
ax2.scatter([0], [0], color='red', s=100, zorder=5)
ax2.annotate('$y(0)=0$\nNhiều nghiệm!', (0, 0), textcoords="offset points", xytext=(10, -30), fontsize=11)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y$')
ax2.set_title('Không duy nhất: $y\' = y^{1/3}$, $y(0)=0$\n$\\partial f/\\partial y$ không Lipschitz tại $y=0$')
ax2.legend(loc='upper left')
ax2.set_xlim(-0.2, 1.2)
ax2.set_ylim(-0.5, 0.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_06_existence_uniqueness.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Lipschitz Condition Visualization
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Lipschitz (smooth) - f = y
ax1 = axes2[0]
y = np.linspace(-2, 2, 500)
f = y

ax1.plot(y, f, 'b-', linewidth=2)
ax1.plot(y, y + 1, 'r--', linewidth=1.5, alpha=0.7, label='$f(y) + L|y_1-y_2|$')
ax1.plot(y, y - 1, 'r--', linewidth=1.5, alpha=0.7)
ax1.fill_between(y, y-1, y+1, alpha=0.2, color='red')
ax1.set_xlabel('$y$')
ax1.set_ylabel('$f(y) = y$')
ax1.set_title(r'Điều kiện Lipschitz: $|y_1 - y_2| \leq L|y_1-y_2|$' + '\n' + r'$\partial f/\partial y = 1$ (bounded) $\to$ Lipschitz')
ax1.legend()
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-3, 3)

# Right: Non-Lipschitz - f = y^(1/3)
ax2 = axes2[1]
y_pos = np.linspace(0, 2, 500)
f_pos = np.power(y_pos, 1/3)

ax2.plot(y_pos, f_pos, 'b-', linewidth=2, label='$f(y) = y^{1/3}$')
ax2.set_xlabel('$y$')
ax2.set_ylabel('$f(y)$')
ax2.set_title('Không Lipschitz: $\\partial f/\\partial y = \\frac{1}{3}y^{-2/3}$\\nKhông bị chặn khi $y \\to 0$')
ax2.legend()
ax2.set_xlim(-0.2, 2.2)
ax2.set_ylim(0, 1.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_06_lipschitz.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-06:")
print("  01_06_existence_uniqueness.svg")
print("  01_06_lipschitz.svg")
