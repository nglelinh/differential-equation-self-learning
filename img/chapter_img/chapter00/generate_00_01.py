#!/usr/bin/env python3
"""
Generate educational images for Chapter 00 lessons
Lesson 00-01: Real Analysis Review - IVT and Weierstrass
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set up style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# =============================================================================
# Figure 1: Intermediate Value Theorem (IVT) visualization
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Function with f(a) < 0, f(b) > 0, showing root exists
ax1 = axes1[0]
x = np.linspace(0, 3, 500)
y = x**3 - x - 2  # f(x) = x^3 - x - 2
ax1.plot(x, y, 'b-', linewidth=2, label='$f(x) = x^3 - x - 2$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)

# Mark f(a) and f(b)
a, b = 1, 2
ax1.scatter([a, b], [a**3-a-2, b**3-b-2], color='red', s=100, zorder=5)
ax1.annotate(f'$f(1) = -2$', (a, a**3-a-2), textcoords="offset points", xytext=(10, 10), fontsize=11)
ax1.annotate(f'$f(2) = 4$', (b, b**3-b-2), textcoords="offset points", xytext=(10, -15), fontsize=11)
ax1.annotate('Có nghiệm $c$', (1.5, 0), textcoords="offset points", xytext=(0, -20), fontsize=12, 
             ha='center', arrowprops=dict(arrowstyle='->', color='green'), color='green')

ax1.set_xlabel('$x$')
ax1.set_ylabel('$f(x)$')
ax1.set_title('Định lý Giá trị Trung gian (IVT)\n$f(1) < 0 < f(2) \\Rightarrow \\exists c: f(c) = 0$')
ax1.set_xlim(-0.3, 3.3)
ax1.set_ylim(-3, 5)
ax1.legend(loc='upper left')

# Right: Counterexample - discontinuous function
ax2 = axes1[1]
x = np.linspace(0, 3, 500)
# Function with jump at x=1.5
y = np.where(x < 1.5, x**2, x**2 + 2)
ax2.plot(x, y, 'b-', linewidth=2)
ax2.scatter([1.5], [2.25], color='white', s=100, zorder=5, edgecolors='blue', linewidths=2)
ax2.scatter([1.5], [4.25], color='blue', s=100, zorder=5)

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=0, color='black', linewidth=0.5)

# Mark the jump
ax2.annotate('', xy=(1.5, 2.25), xytext=(1.5, 4.25),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax2.text(1.7, 3.25, 'Gián đoạn\nIVT không áp dụng', fontsize=10, color='red')

ax2.set_xlabel('$x$')
ax2.set_ylabel('$f(x)$')
ax2.set_title('Phản ví dụ: Hàm gián đoạn\nIVT không thỏa')
ax2.set_xlim(-0.3, 3.3)
ax2.set_ylim(-1, 7)

plt.tight_layout()
plt.savefig('00_01_01_real_analysis_ivt.svg', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_01_01_real_analysis_ivt.svg")

# =============================================================================
# Figure 2: Weierstrass Theorem - Max/Min on compact sets
# =============================================================================
fig2, ax = plt.subplots(figsize=(12, 6))

x = np.linspace(-2, 2, 500)
y = x**4 - 2*x**2 + 1

ax.plot(x, y, 'b-', linewidth=2, label='$f(x) = x^4 - 2x^2 + 1$')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)

# Mark max and min
min_points = [(-1, 0), (1, 0)]
max_point = (0, 1)

for px, py in min_points:
    ax.scatter([px], [py], color='green', s=150, zorder=5, marker='v')
    ax.annotate(f'Min: f={py}', (px, py), textcoords="offset points", 
                xytext=(10, -20), fontsize=11, color='green')

ax.scatter([0], [1], color='red', s=150, zorder=5, marker='^')
ax.annotate(f'Max: f=1', (0, 1), textcoords="offset points", 
            xytext=(10, 10), fontsize=11, color='red')

# Add interval labels
ax.axvline(x=-2, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=2, color='gray', linestyle='--', alpha=0.5)
ax.fill_between([-2, 2], -0.5, 2, alpha=0.1, color='blue')
ax.text(0, -0.3, 'Tập compact [-2, 2]', ha='center', fontsize=11, color='blue')

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_title('Định lý Weierstrass: Liên tục trên tập compact → đạt max và min')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.5, 2)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('00_01_02_weierstrass.svg', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_01_02_weierstrass.svg")