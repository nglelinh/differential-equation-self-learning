#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-04: Reduction of Order
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Reduction of Order - Repeated Root
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Repeated root solutions
ax1 = axes1[0]
t = np.linspace(0, 3, 500)
r = -1  # repeated root

for C1, C2 in [(1, 0), (0, 1), (1, 1)]:
    y = np.exp(r*t) * (C1 + C2*t)
    ax1.plot(t, y, linewidth=2, label=f'$C_1={C1}, C_2={C2}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Nghiệm bội: $r = -1$\n$y = (C_1 + C_2t)e^{rt}$')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.3, 3.3)

# Right: Compare with distinct roots
ax2 = axes1[1]
# Distinct roots r = -1, -2
for C1, C2 in [(1, 1)]:
    y_distinct = C1 * np.exp(-t) + C2 * np.exp(-2*t)
    ax2.plot(t, y_distinct, 'b-', linewidth=2, label='Distinct: $e^{-t} + e^{-2t}$')

# Repeated root
y_repeated = np.exp(-t) * (1 + t)
ax2.plot(t, y_repeated, 'r--', linewidth=2, label='Repeated: $(1+t)e^{-t}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('So sánh: Nghiệm bội vs phân biệt\nTỷ lệ suy giảm khác nhau')
ax2.legend(loc='upper right')
ax2.set_xlim(-0.3, 3.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_04_reduction_of_order.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Method Visualization
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

t = np.linspace(0, 4, 500)
y1 = np.exp(-t)  # known solution

# Second solution: y2 = v(t) * y1, where v' = W/y1^2
# For y'' + 2y' + y = 0, y1 = e^(-t), try y2 = v*e^(-t)
y2 = t * np.exp(-t)

ax.plot(t, y1, 'b-', linewidth=2, label='$y_1 = e^{-t}$ (đã biết)')
ax.plot(t, y2, 'r-', linewidth=2, label='$y_2 = te^{-t}$ (tìm được)')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('$t$')
ax.set_ylabel('$y(t)$')
ax.set_title('Phương pháp giảm bậc: Tìm $y_2$\n$y_2 = v(t) \\cdot y_1(t)$')
ax.legend(loc='upper right')
ax.set_xlim(-0.3, 4.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_04_method.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-04:")
print("  02_04_reduction_of_order.svg")
print("  02_04_method.svg")