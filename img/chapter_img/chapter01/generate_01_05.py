#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-05: Substitution Methods
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Bernoulli Equation Visualization
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: y' + y = y^2 (Bernoulli with n=2)
ax1 = axes1[0]
t = np.linspace(0, 3, 500)

# Solutions: y = 1/(1 - Ce^t)
for C in [-2, -1, -0.5, 0]:
    y = 1 / (1 - C * np.exp(t))
    y = np.clip(y, -10, 10)
    ax1.plot(t, y, linewidth=2, label=f'$C = {C}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Nghiệm của $y\' + y = y^2$ (Bernoulli)\n$y = \\frac{1}{1 - Ce^{t}}$')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.3, 3.3)
ax1.set_ylim(-3, 5)

# Right: Homogeneous equation y' = 1 + y/t
ax2 = axes1[1]
t = np.linspace(0.1, 3, 500)

# Solution: y = t*ln|t| + Ct
for C in [-2, -1, 0, 1, 2]:
    y = t * np.log(np.abs(t)) + C * t
    y = np.clip(y, -10, 10)
    ax2.plot(t, y, linewidth=2, label=f'$C = {C}$')

ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Nghiệm của $y\' = 1 + y/t$ (thuần nhất)\n$y = t\\ln|t| + Ct$')
ax2.legend(loc='upper left')
ax2.set_xlim(-0.3, 3.3)
ax2.set_ylim(-5, 10)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_05_substitution_methods.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Substitution Pattern Visualization
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Show y/t ratio transformation
ax1 = axes2[0]
t = np.linspace(0.1, 3, 500)

for C in [0.5, 1, 2]:
    v = C + np.log(t)  # v = y/t
    y = t * v
    ax1.plot(t, y, linewidth=2, label=f'$v = C + \\ln t$, $y = vt$')

ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.set_title('Biến đổi $y=vt$ với $v = y/t$\nĐường cong thuần nhất bậc 1')
ax1.legend()
ax1.set_xlim(0, 3.3)
ax1.set_ylim(-2, 8)

# Right: u = y^(-1) substitution
ax2 = axes2[1]
y = np.linspace(0.1, 3, 500)
u = 1 / y

ax2.plot(y, u, 'b-', linewidth=2)
ax2.set_xlabel('$y$')
ax2.set_ylabel('$u = y^{-1}$')
ax2.set_title('Biến đổi Bernoulli: $u = y^{1-n} = y^{-1}$\nPhi tuyến tính $\\to$ tuyến tính')
ax2.set_xlim(0, 3.3)
ax2.set_ylim(0, 10)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_05_substitution_patterns.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-05:")
print("  01_05_substitution_methods.svg")
print("  01_05_substitution_patterns.svg")
