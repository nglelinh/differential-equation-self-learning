#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-03: Constant Coefficients - Complex Roots
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Complex Roots - Oscillations
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Undamped oscillation (alpha = 0)
ax1 = axes1[0]
t = np.linspace(0, 4*np.pi, 500)
w = 1  # omega

for A, B in [(1, 0), (0, 1), (1, 1)]:
    y = A * np.cos(w*t) + B * np.sin(w*t)
    ax1.plot(t, y, linewidth=2, label=f'$A={A}, B={B}$')

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title(r'Dao động: $r = \pm i\omega$' + '\n$\\to$ $y = A\\cos(\\omega t) + B\\sin(\\omega t)$')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.5, 13)

# Right: Damped oscillation (alpha < 0)
ax2 = axes1[1]
alpha = -0.3  # negative alpha = damping
w = 1  # omega

for A, B in [(1, 0), (0, 1), (1, 1)]:
    y = np.exp(alpha*t) * (A * np.cos(w*t) + B * np.sin(w*t))
    ax2.plot(t, y, linewidth=2, label=f'$A={A}, B={B}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title(f'Dao động tắt dần: $r = {alpha} \\pm i{1}$\n$\\to$ $y = e^{{alpha t}}(A\\cos + B\\sin)$')
ax2.legend(loc='upper right')
ax2.set_xlim(-0.5, 13)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_03_constant_coeff_complex_roots.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Complex Plane
# =============================================================================
fig2, ax = plt.subplots(figsize=(8, 8))

# Plot complex roots in the complex plane
# For r^2 + w^2 = 0, roots are r = +/- i*w
theta = np.linspace(0, 2*np.pi, 500)
r_circle = 1

ax.plot(r_circle * np.cos(theta), r_circle * np.sin(theta), 'b--', linewidth=2, label='$|r| = \\omega$')
ax.scatter([0, 0], [1, -1], color='red', s=150, zorder=5, label='$r = \\pm i\\omega$')
ax.annotate('$i\\omega$', (0, 1), textcoords="offset points", xytext=(10, 5), fontsize=12)
ax.annotate('$-i\\omega$', (0, -1), textcoords="offset points", xytext=(10, -20), fontsize=12)

ax.axhline(y=0, color='black', linewidth=1)
ax.axvline(x=0, color='black', linewidth=1)
ax.set_xlabel('Re(r)')
ax.set_ylabel('Im(r)')
ax.set_title('Mặt phẳng phức: Nghiệm phức\n$\\alpha \\pm i\\omega$ → Dao động')
ax.legend(loc='upper right')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_03_complex_plane.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-03:")
print("  02_03_constant_coeff_complex_roots.svg")
print("  02_03_complex_plane.svg")