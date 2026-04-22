#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-10: Wronskian and Linear Independence
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Wronskian Visualization
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Linearly independent functions
ax1 = axes1[0]
t = np.linspace(-2, 2, 500)

y1 = np.exp(t)
y2 = np.exp(-t)

ax1.plot(t, y1, 'b-', linewidth=2, label='$y_1 = e^t$')
ax1.plot(t, y2, 'r-', linewidth=2, label='$y_2 = e^{-t}$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y$')
ax1.set_title('Độc lập tuyến tính: $e^t, e^{-t}$\n$W = -2 \\neq 0$')
ax1.legend()
ax1.set_xlim(-2.5, 2.5)

# Right: Linearly dependent
ax2 = axes1[1]
t = np.linspace(-2, 2, 500)

y1 = np.exp(t)
y2 = 2*np.exp(t)

ax2.plot(t, y1, 'b-', linewidth=2, label='$y_1 = e^t$')
ax2.plot(t, y2, 'r--', linewidth=2, label='$y_2 = 2e^t$')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y$')
ax2.set_title('Phụ thuộc tuyến tính: $e^t, 2e^t$\n$y_2 = 2y_1$')
ax2.legend()
ax2.set_xlim(-2.5, 2.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_10_wronskian.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Wronskian Calculation
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

# Show Wronskian as area between solution curves
t = np.linspace(-1, 1, 200)
y1 = np.cos(t)
y2 = np.sin(t)

ax.plot(t, y1, 'b-', linewidth=2, label='$y_1 = \\cos t$')
ax.plot(t, y2, 'r-', linewidth=2, label='$y_2 = \\sin t$')
ax.fill_between(t, y1, y2, alpha=0.3, color='green')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('$t$')
ax.set_ylabel('$y$')
ax.set_title('Wronskian cho $\\cos t, \\sin t$: $W = 1$\nDiện tích giữa hai đường cong')
ax.legend()
ax.set_xlim(-1.5, 1.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_10_wronskian_calc.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-10:")
print("  02_10_wronskian.svg")
print("  02_10_wronskian_calc.svg")