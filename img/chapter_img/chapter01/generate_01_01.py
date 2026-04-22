#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-01: Introduction to Differential Equations
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# =============================================================================
# Figure 1: Introduction to DEs - showing what is a differential equation
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Plot of y = Ce^(kt) for different C values
ax1 = axes1[0]
t = np.linspace(0, 3, 500)
k = 1.0

for C in [-2, -1, -0.5, 0, 0.5, 1, 2]:
    y = C * np.exp(k * t)
    ax1.plot(t, y, linewidth=2, label=f'$C = {C}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Nghiệm của phương trình $\\frac{dy}{dt} = y$\n$y(t) = Ce^{t}$')
ax1.legend(loc='upper left')
ax1.set_xlim(-0.3, 3.3)
ax1.set_ylim(-5, 10)

# Right: Different DEs and their solution families
ax2 = axes1[1]
t = np.linspace(0, 2, 500)

# y' = y => y = Ce^t (exponential growth)
for C in [0.5, 1, 1.5]:
    y = C * np.exp(t)
    ax2.plot(t, y, 'b-', linewidth=2, alpha=0.7)

# y' = -y => y = Ce^(-t) (exponential decay)
for C in [0.5, 1, 1.5]:
    y = C * np.exp(-t)
    ax2.plot(t, y, 'r--', linewidth=2, alpha=0.7)

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.text(0.1, 2.5, r'$\dfrac{dy}{dt} = y$ (tăng mũ)', color='blue', fontsize=11)
ax2.text(0.1, 0.5, r'$\dfrac{dy}{dt} = -y$ (giảm mũ)', color='red', fontsize=11)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Hai phương trình vi phân khác nhau\ncho hai họ nghiệm khác nhau')
ax2.set_xlim(-0.2, 2.2)
ax2.set_ylim(-0.5, 5)

plt.tight_layout()
plt.savefig('/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/01_01_introduction_to_des.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Order and Degree visualization
# =============================================================================
fig2, ax = plt.subplots(figsize=(10, 6))

# Create a visual comparison of different order ODEs
x = np.linspace(-3, 3, 500)

# First order: y' = x (linear)
ax.plot(x, x**2/2, 'b-', linewidth=2, label='Bậc 1: $y\' = f(x)$')

# Second order: y'' = 1 (constant second derivative)
ax.plot(x, x**2/2, 'r-', linewidth=2, label='Bậc 2: $y\'\' = f(x)$')

ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_title('So sánh các phương trình vi phân\ntheo bậc (order)')
ax.legend()
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2, 10)

plt.tight_layout()
plt.savefig('/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/01_01_order_degree.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-01:")
print("  01_01_introduction_to_des.svg")
print("  01_01_order_degree.svg")