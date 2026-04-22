#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-08: Mechanical Vibrations
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: Damped Vibrations
# =============================================================================
fig1, axes1 = plt.subplots(1, 3, figsize=(16, 5))

# Underdamped
ax1 = axes1[0]
t = np.linspace(0, 10, 500)
zeta = 0.2  # underdamped
w0 = 2
wd = w0 * np.sqrt(1 - zeta**2)

for A in [1, 0.5]:
    y = A * np.exp(-zeta*w0*t) * np.cos(wd*t)
    ax1.plot(t, y, linewidth=2, label=f'$A={A}$')
    ax1.plot(t, A*np.exp(-zeta*w0*t), 'r--', alpha=0.5)
    ax1.plot(t, -A*np.exp(-zeta*w0*t), 'r--', alpha=0.5)

ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Thiếu cản ($\\zeta < 1$)\nDao động tắt dần')
ax1.legend(loc='upper right')
ax1.set_xlim(-0.5, 10.5)

# Critically damped
ax2 = axes1[1]
zeta = 1.0
for A in [1, 0.5]:
    y = A * (1 + w0*t) * np.exp(-w0*t)
    ax2.plot(t, y, linewidth=2, label=f'$A={A}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Cản tới hạn ($\\zeta = 1$)\n Quay về cân bằng nhanh nhất')
ax2.legend(loc='upper right')
ax2.set_xlim(-0.5, 10.5)

# Overdamped
ax3 = axes1[2]
zeta = 2.0
r1 = -w0 * (zeta + np.sqrt(zeta**2 - 1))
r2 = -w0 * (zeta - np.sqrt(zeta**2 - 1))

for A in [1, 0.5]:
    y = A * (np.exp(r1*t) - np.exp(r2*t)) * r2 / (r2-r1)
    y = np.clip(y, -10, 10)
    ax3.plot(t, y, linewidth=2, label=f'$A={A}$')

ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlabel('$t$')
ax3.set_ylabel('$y(t)$')
ax3.set_title('Quá cản ($\\zeta > 1$)\n Quay về không dao động')
ax3.legend(loc='upper right')
ax3.set_xlim(-0.5, 10.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_08_mechanical_vibrations.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Forced Vibration & Resonance
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Beat phenomenon
ax1 = axes2[0]
t = np.linspace(0, 30, 1000)
w1 = 1.0
w2 = 1.2

y = np.cos(w1*t) + np.cos(w2*t)
y_beat = 2 * np.cos((w2-w1)*t/2) * np.cos((w1+w2)*t/2)

ax1.plot(t, y_beat, 'b-', linewidth=1.5, label='Biên độ đập')
ax1.plot(t, 2*np.cos((w2-w1)*t/2), 'r--', alpha=0.7)
ax1.plot(t, -2*np.cos((w2-w1)*t/2), 'r--', alpha=0.7)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Hiện tượng đập: $\\omega_1 \\approx \\omega_2$\nBiên độ thay đổi chậm')
ax1.legend()
ax1.set_xlim(-1, 31)

# Resonance
ax2 = axes2[1]
# y'' + y = cos(wt) with different w
for w in [0.5, 1.0, 1.5]:
    if abs(w - 1.0) < 0.01:  # resonance
        y = 0.5 * t * np.sin(t)
    else:
        A = 1 / (1 - w**2)
        y = A * np.cos(w*t)
    ax2.plot(t[:300], y[:300], linewidth=2, label=f'$\\omega = {w}$')

ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Cộng hưởng: $\\omega = 1$\nBiên độ tăng vô hạn!')
ax2.legend()
ax2.set_xlim(-1, 10)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_08_resonance.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-08:")
print("  02_08_mechanical_vibrations.svg")
print("  02_08_resonance.svg")