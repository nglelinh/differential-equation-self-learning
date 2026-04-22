#!/usr/bin/env python3
"""
Generate educational images for Chapter 03 lessons
Lesson 03-01: Definition and Basic Properties
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter03/'

# =============================================================================
# Figure 1: Laplace Transform Definition
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: f(t) = 1
ax1 = axes1[0]
t = np.linspace(0, 5, 500)
f = np.ones_like(t)

ax1.plot(t, f, 'b-', linewidth=2)
ax1.fill_between(t, 0, f, alpha=0.3)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$f(t) = 1$')
ax1.set_title('$\\mathcal{L}\\{1\\} = \\int_0^\\infty e^{-st} \\cdot 1 \\, dt = \\frac{1}{s}$')
ax1.set_xlim(-0.3, 5.3)
ax1.set_ylim(0, 1.5)

# Right: f(t) = e^(at)
ax2 = axes1[1]
a = 1.5
f = np.exp(a*t)

ax2.plot(t, f, 'b-', linewidth=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel(f'$f(t) = e^{{{a}t}}$')
ax2.set_title(r'$\mathcal{L}\{e^{at}\} = \int_0^\infty e^{-st}e^{at}dt = \frac{1}{s-a}$')
ax2.set_xlim(-0.3, 3)
ax2.set_ylim(0, 50)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_01_definition_properties.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Exponential Shifting
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: e^(at)f(t) <=> F(s-a)
ax1 = axes2[0]
t = np.linspace(0, 4, 500)

# f(t) = 1, so L{1} = 1/s
# e^(at)*1 => L = 1/(s-a)
for a in [0.5, 1, 1.5]:
    f = np.exp(a*t)
    ax1.plot(t, f, linewidth=2, label=f'$a = {a}$')

ax1.set_xlabel('$t$')
ax1.set_ylabel('$e^{at}$')
ax1.set_title('Dịch chuyển trong miền $t$: $e^{at}f(t)$\n$\\to$ Dịch sang phải trong miền $s$: $F(s-a)$')
ax1.legend()
ax1.set_xlim(-0.3, 4.3)

# Right: Visualize s parameter
ax2 = axes2[1]
t = np.linspace(0, 5, 500)
f = np.exp(-t)

for s in [0.5, 1, 2, 3]:
    weighted = np.exp(-s*t) * f
    ax2.plot(t, weighted, linewidth=2, label=f'$s = {s}$')

ax2.set_xlabel('$t$')
ax2.set_ylabel('$e^{-st}f(t)$')
ax2.set_title('Ảnh hưởng của tham số $s$\n$s$ lớn $\\to$ hội tụ nhanh')
ax2.legend()
ax2.set_xlim(-0.3, 5.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_01_shifting.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 03-01:")
print("  03_01_definition_properties.svg")
print("  03_01_shifting.svg")