#!/usr/bin/env python3
"""
Generate educational images for Chapter 02 lessons
Lesson 02-09: RLC Circuits
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter02/'

# =============================================================================
# Figure 1: RLC Circuit Response
# =============================================================================
fig1, axes1 = plt.subplots(1, 3, figsize=(16, 5))

# Underdamped RLC
ax1 = axes1[0]
t = np.linspace(0, 10, 500)
R = 0.5
L = 1
C = 1
alpha = R/(2*L)
w0 = 1/np.sqrt(L*C)
wd = np.sqrt(w0**2 - alpha**2)

y = np.exp(-alpha*t) * np.cos(wd*t)
ax1.plot(t, y, 'b-', linewidth=2)
ax1.plot(t, np.exp(-alpha*t), 'r--', alpha=0.7)
ax1.plot(t, -np.exp(-alpha*t), 'r--', alpha=0.7)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$q(t)$')
ax1.set_title('RLC thiếu cản\nDao động tắt dần')
ax1.set_xlim(-0.5, 10.5)

# Critically damped
ax2 = axes1[1]
R = 2
alpha = R/(2*L)

y = (1 + alpha*t) * np.exp(-alpha*t)
ax2.plot(t, y, 'b-', linewidth=2)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$q(t)$')
ax2.set_title('RLC cản tới hạn\nQuay về nhanh nhất')
ax2.set_xlim(-0.5, 10.5)

# Overdamped
ax3 = axes1[2]
R = 5
alpha = R/(2*L)
r1 = -alpha + np.sqrt(alpha**2 - w0**2)
r2 = -alpha - np.sqrt(alpha**2 - w0**2)

y = (np.exp(r1*t) - np.exp(r2*t))
ax3.plot(t, y, 'b-', linewidth=2)
ax3.axhline(y=0, color='black', linewidth=0.5)
ax3.set_xlabel('$t$')
ax3.set_ylabel('$q(t)$')
ax3.set_title('RLC quá cản\nKhông dao động')
ax3.set_xlim(-0.5, 10.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_09_rlc_circuits.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Analogy with Mechanical
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Voltage response
ax1 = axes2[0]
t = np.linspace(0, 8*np.pi, 500)
# Series RLC with sinusoidal input
R = 0.3
L = 1
C = 1
w = 0.5
V0 = 1

# Steady state: I = V0/sqrt(R^2 + (wL-1/wC)^2) * sin(wt - phi)
# Just show simple damped oscillation
alpha = R/(2*L)
wd = np.sqrt(1/L/C - alpha**2)

i = np.exp(-alpha*t) * np.cos(wd*t) + 0.3 * np.sin(w*t)

ax1.plot(t, i, 'b-', linewidth=2, label='$i(t)$')
ax1.plot(t, np.exp(-alpha*t), 'r--', alpha=0.5, label='Envelope')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$i(t)$')
ax1.set_title('Dòng điện trong mạch RLC\nTương tự dao động cơ học')
ax1.legend()
ax1.set_xlim(-0.5, 25)

# Phase shift
ax2 = axes2[1]
w = np.linspace(0.1, 3, 500)
phi = np.arctan((w*L - 1/(w*C))/R)

ax2.plot(w, phi, 'b-', linewidth=2)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axhline(y=np.pi/2, color='red', linestyle='--', alpha=0.7)
ax2.set_xlabel('$\\omega$')
ax2.set_ylabel('$\\phi$ (phase)')
ax2.set_title('Độ lệch pha\n$\\phi = \\arctan\\frac{\\omega L - 1/\\omega C}{R}$')
ax2.set_xlim(0, 3.2)

plt.tight_layout()
plt.savefig(IMG_PATH + '02_09_rlc_response.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 02-09:")
print("  02_09_rlc_circuits.svg")
print("  02_09_rlc_response.svg")