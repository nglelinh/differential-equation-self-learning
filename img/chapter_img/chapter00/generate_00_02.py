#!/usr/bin/env python3
"""
Generate educational images for Chapter 00 lessons
Lesson 00-02: Uniform Continuity
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# =============================================================================
# Figure 1: f(x) = x^2 - NOT uniformly continuous on R
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: f(x) = x^2 on R
ax1 = axes1[0]
x = np.linspace(-3, 3, 500)
y = x**2
ax1.plot(x, y, 'b-', linewidth=2, label='$f(x) = x^2$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)

# Show that as x increases, the slope increases
ax1.annotate('', xy=(2, 4), xytext=(1, 1),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax1.annotate('', xy=(2.5, 6.25), xytext=(1.5, 2.25),
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax1.text(1.5, 3, 'Độ dốc tăng\nkhi x tăng', fontsize=10, color='darkred')

ax1.set_xlabel('$x$')
ax1.set_ylabel('$f(x)$')
ax1.set_title('Hàm $f(x) = x^2$ trên $\mathbb{R}$\nKHÔNG liên tục đều')
ax1.set_xlim(-3.5, 3.5)
ax1.set_ylim(-1, 10)
ax1.legend()

# Right: Why not uniformly continuous - proof by contradiction
ax2 = axes1[1]
# Show two points close together far from origin
x1, x2 = 10, 10.1
ax2.plot(x, y, 'b-', linewidth=2, label='$f(x) = x^2$')
ax2.scatter([x1, x2], [x1**2, x2**2], color='red', s=100, zorder=5)
ax2.hlines(y=x1**2, xmin=-3, xmax=x1, colors='red', linestyles='--', alpha=0.5)
ax2.hlines(y=x2**2, xmin=-3, xmax=x2, colors='green', linestyles='--', alpha=0.5)

# Show the difference
dy = x2**2 - x1**2
ax2.annotate(f'$|x_1 - x_2| = 0.1$\n$|f(x_1)-f(x_2)| = {dy:.1f}$', 
            xy=(x1, x1**2), textcoords="offset points", xytext=(-80, 30), fontsize=10)

ax2.set_xlabel('$x$')
ax2.set_ylabel('$f(x)$')
ax2.set_title('Tại x=10, cần $\delta$ rất nhỏ\nđể |f(x+δ)-f(x)| < 1')
ax2.set_xlim(-1, 12)
ax2.set_ylim(90, 130)
ax2.legend()

plt.tight_layout()
plt.savefig('00_02_01_uniform_continuity_counterexample.svg', dpi=150, 
            bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_02_01_uniform_continuity_counterexample.svg")

# =============================================================================
# Figure 2: f(x) = sqrt(x) - uniformly continuous on [0,1]
# =============================================================================
fig2, ax = plt.subplots(figsize=(12, 6))

x = np.linspace(0, 1, 500)
y = np.sqrt(x)
ax.plot(x, y, 'b-', linewidth=2, label='$f(x) = \\sqrt{x}$')

# Show that the slope decreases
x1, x2 = 0.1, 0.2
dy = np.sqrt(x2) - np.sqrt(x1)
dx = x2 - x1
slope = dy/dx

ax.scatter([x1, x2], [np.sqrt(x1), np.sqrt(x2)], color='red', s=80, zorder=5)
ax.plot([x1, x2], [np.sqrt(x1), np.sqrt(x2)], 'r--', linewidth=1)
ax.annotate(f'Độ dốc ≈ {slope:.2f}\n(Nhỏ khi x lớn)', 
            xy=(x1, np.sqrt(x1)), textcoords="offset points", xytext=(10, 20), fontsize=10)

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax2 = ax

# Show that we can find a single delta for any epsilon
# For epsilon = 0.3, delta = epsilon^2 = 0.09 works everywhere
epsilon = 0.3
delta = epsilon**2
x0 = 0.5
ax.fill_between([x0-delta, x0+delta], 0, 1.2, alpha=0.2, color='green', 
                label=f'$\\delta = {delta:.2f}$ works for all $x$')
ax.axhline(y=np.sqrt(x0)-epsilon, color='red', linestyle='--', alpha=0.5)
ax.axhline(y=np.sqrt(x0)+epsilon, color='red', linestyle='--', alpha=0.5)
ax.axhline(y=np.sqrt(x0), color='gray', linestyle=':', alpha=0.5)
ax.axvline(x=x0, color='gray', linestyle=':', alpha=0.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_title('Hàm $f(x) = \\sqrt{x}$ trên $[0,1]$\nLIÊN TỤC ĐỀU (vì tập compact)')
ax.set_xlim(-0.05, 1.1)
ax.set_ylim(-0.05, 1.1)
ax.legend()

plt.tight_layout()
plt.savefig('00_02_02_uniform_continuity_positive.svg', dpi=150, 
            bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_02_02_uniform_continuity_positive.svg")

# =============================================================================
# Figure 3: Heine-Cantor Theorem visualization
# =============================================================================
fig3, ax = plt.subplots(figsize=(12, 6))

# Show compact interval [a,b]
a, b = -2, 3
x = np.linspace(a, b, 500)
y = np.sin(x**2)  # Continuous function on [a,b]

ax.plot(x, y, 'b-', linewidth=2, label='$f(x) = \\sin(x^2)$')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.fill_between([a, b], -1.5, 1.5, alpha=0.1, color='blue')

# Mark the interval
ax.axvline(x=a, color='red', linewidth=2)
ax.axvline(x=b, color='red', linewidth=2)
ax.text(a, -1.3, 'a', fontsize=12, ha='center', color='red')
ax.text(b, -1.3, 'b', fontsize=12, ha='center', color='red')
ax.text((a+b)/2, -1.3, 'Tập compact [a,b]', ha='center', fontsize=11, color='blue')

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_title('Định lý Heine-Cantor: Liên tục trên tập compact → Liên tục đều')
ax.set_xlim(a-0.5, b+0.5)
ax.set_ylim(-1.5, 1.5)
ax.legend()

plt.tight_layout()
plt.savefig('00_02_03_heine_cantor.svg', dpi=150, 
            bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Generated: 00_02_03_heine_cantor.svg")