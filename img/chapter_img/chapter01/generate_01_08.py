#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-08: Applications - Mechanics and Circuits
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Falling Body with Drag
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Velocity of falling body
ax1 = axes1[0]
t = np.linspace(0, 10, 500)

# m*dv/dt = mg - cv => v(t) = mg/c * (1 - e^(-c*t/m))
m = 1
g = 10
c = 2
v_term = m * g / c

v = v_term * (1 - np.exp(-c * t / m))

ax1.plot(t, v, 'b-', linewidth=2, label='$v(t)$')
ax1.axhline(y=v_term, color='red', linestyle='--', linewidth=2, label=f'$v_{{term}} = {v_term}$')
ax1.axhline(y=v_term*0.95, color='gray', linestyle=':', linewidth=1, alpha=0.7)
ax1.set_xlabel('$t$ (s)')
ax1.set_ylabel('$v(t)$ (m/s)')
ax1.set_title('Vật rơi có cản: $m\\frac{dv}{dt}=mg-cv$\n$v(t)=\\frac{mg}{c}(1-e^{-ct/m})$')
ax1.legend()
ax1.set_xlim(-0.5, 10.5)
ax1.set_ylim(0, 7)

# Right: Different drag coefficients
ax2 = axes1[1]
for c in [1, 2, 4]:
    v_term = m * g / c
    v = v_term * (1 - np.exp(-c * t / m))
    ax2.plot(t, v, linewidth=2, label=f'$c = {c}$')

ax2.axhline(y=10, color='red', linestyle='--', linewidth=2)
ax2.set_xlabel('$t$ (s)')
ax2.set_ylabel('$v(t)$')
ax2.set_title('Ảnh hưởng của hệ số cản\n$c$ lớn $\\to$ vận tốc giới hạn nhỏ hơn')
ax2.legend()
ax2.set_xlim(-0.5, 10.5)
ax2.set_ylim(0, 12)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_08_applications_mechanics_circuits.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: RC and RL Circuits
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: RC Circuit - capacitor charging
ax1 = axes2[0]
t = np.linspace(0, 10, 500)

# RC circuit: dq/dt + q/(RC) = E/R
R = 2
C = 1
E = 10
q_ss = E * C  # steady state charge

q = q_ss * (1 - np.exp(-t / (R * C)))

ax1.plot(t, q, 'b-', linewidth=2, label='$q(t)$')
ax1.axhline(y=q_ss, color='red', linestyle='--', linewidth=2, label=f'$q_{{ss}} = {q_ss}$')
ax1.set_xlabel('$t$')
ax1.set_ylabel('$q(t)$ (charge)')
ax1.set_title('Mạch RC: $R\\frac{dq}{dt}+\\frac{1}{C}q=E$\n$\\tau = RC$ (hằng số thời gian)')
ax1.legend()
ax1.set_xlim(-0.5, 10.5)
ax1.set_ylim(0, 12)

# Right: RL Circuit
ax2 = axes2[1]
# RL circuit: L*di/dt + Ri = E
R = 2
L = 1
E = 10
i_ss = E / R

i = i_ss * (1 - np.exp(-R * t / L))

ax2.plot(t, i, 'b-', linewidth=2, label='$i(t)$')
ax2.axhline(y=i_ss, color='red', linestyle='--', linewidth=2, label=f'$i_{{ss}} = {i_ss}$')
ax2.set_xlabel('$t$')
ax2.set_ylabel('$i(t)$ (current)')
ax2.set_title('Mạch RL: $L\\frac{di}{dt}+Ri=E$\n$\\tau = L/R$ (hằng số thời gian)')
ax2.legend()
ax2.set_xlim(-0.5, 10.5)
ax2.set_ylim(0, 7)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_08_circuits_detail.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-08:")
print("  01_08_applications_mechanics_circuits.svg")
print("  01_08_circuits_detail.svg")
