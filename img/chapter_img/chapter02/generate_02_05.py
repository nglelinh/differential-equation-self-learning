#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-05: Method of Undetermined Coefficients
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Method of Undetermined Coefficients
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Forced oscillation
ax1 = axes1[0]
t = np.linspace(0, 6*np.pi, 500)
# y'' + y = cos(wt) - undamped forced
# Particular solution depends on w

# For w != 1: yp = A*cos(wt)
w = 2
A = 1 / (1 - w**2)
y_p = A * np.cos(w*t)
y_h = np.cos(t)  # homogeneous part

ax1.plot(t, y_p, 'r-', linewidth=2, label='$y_p$ (nghiệm riêng)')
ax1.plot(t, y_h, 'b--', linewidth=2, label='$y_h$ (thuần nhất)')
ax1.plot(t, y_p + 0.1*y_h, 'g-', linewidth=2, alpha=0.7, label='Tổ hợp')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title(f'Cộng hưởng: $y\'\' + y = \\cos({w}t)$\nNghiệm riêng với tần số khác')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.5, 19)

# Right: Resonance case
ax2 = axes1[1]
t_res = np.linspace(0, 10, 500)
# y'' + y = cos(t) => resonance, particular = t*sin(t)/2
y_p_res = 0.5 * t_res * np.sin(t_res)
y_h = np.cos(t_res)

ax2.plot(t_res, y_p_res, 'r-', linewidth=2, label='$y_p$ (cộng hưởng)')
ax2.plot(t_res, y_h, 'b--', linewidth=2, label='$y_h$')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Cộng hưởng: $y\'\' + y = \\cos(t)$\nBiên độ tăng tuyến tính!')
ax2.legend(loc='upper left')
ax2.set_xlim(-0.5, 10.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_05_undetermined_coefficients.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Trial Forms
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

t = np.linspace(0, 4, 500)

# y'' - y' - 2y = 2t^2 + 1
# Particular: yp = At^2 + Bt + C
# Solve: -2At^2 + ... let's just plot polynomial form
A, B, C = -1, -1, -0.5
y_p = A * t**2 + B * t + C

ax.plot(t, y_p, 'r-', linewidth=2, label='$y_p = At^2 + Bt + C$')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)
ax.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax.set_title('Dạng thử: Đa thức\nCho $f(t) = 2t^2 + 1$ → thử $At^2 + Bt + C$')
ax.legend(loc='upper left')
ax.set_xlim(-0.3, 4.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_05_trial_forms.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-05:")
print("  02_05_undetermined_coefficients.svg")
print("  02_05_trial_forms.svg")