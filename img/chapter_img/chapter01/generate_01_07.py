#!/usr/bin/env python3
"""
Generate educational images for Chapter 01 lessons
Lesson 01-07: Applications - Population and Mixing
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter01/'

# =============================================================================
# Figure 1: Population Models
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Exponential vs Logistic Growth
ax1 = axes1[0]
t = np.linspace(0, 10, 500)
P0 = 1

# Exponential: P = P0*e^(rt)
P_exp = P0 * np.exp(0.5 * t)

# Logistic: P = K / (1 + ((K-P0)/P0)*e^(-rt))
K = 10
r = 0.5
P_log = K / (1 + ((K-P0)/P0) * np.exp(-r*t))

ax1.plot(t, P_exp, 'r--', linewidth=2, label='Mũ: $P = e^{0.5t}$')
ax1.plot(t, P_log, 'b-', linewidth=2, label='Logistic: $K=10$')
ax1.axhline(y=K, color='green', linestyle=':', linewidth=2, label='$K$ (carrying capacity)')
ax1.set_xlabel('$t$')
ax1.set_ylabel('$P(t)$')
ax1.set_title('Tăng trưởng dân số: Mũ vs Logistic')
ax1.legend(loc='right')
ax1.set_xlim(-0.5, 10.5)
ax1.set_ylim(0, 25)

# Right: Logistic with different K
ax2 = axes1[1]
for K in [5, 10, 20]:
    P_log = K / (1 + ((K-P0)/P0) * np.exp(-r*t))
    ax2.plot(t, P_log, linewidth=2, label=f'$K = {K}$')

ax2.axhline(y=10, color='green', linestyle=':', linewidth=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$P(t)$')
ax2.set_title('Mô hình Logistic với các sức chở khác nhau')
ax2.legend()
ax2.set_xlim(-0.5, 10.5)
ax2.set_ylim(0, 25)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_07_applications_population_mixing.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# Figure 2: Mixing Problem
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Mixing tank concentration
ax1 = axes2[0]
t = np.linspace(0, 20, 500)

# dA/dt = r_in*c_in - r_out*A/V
# A(t) = A_ss + (A0 - A_ss)*e^(-rt)
V = 10  # volume
r = 2   # flow rate
c_in = 3  # input concentration
A0 = 0   # initial amount
A_ss = V * c_in  # steady state

A = A_ss + (A0 - A_ss) * np.exp(-r*t/V)

ax1.plot(t, A, 'b-', linewidth=2, label='$A(t)$ (lượng muối)')
ax1.axhline(y=A_ss, color='red', linestyle='--', linewidth=2, label=f'$A_{{ss}} = {A_ss}$')
ax1.axhline(y=A_ss * 0.95, color='gray', linestyle=':', linewidth=1, alpha=0.7)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$A(t)$ (amount of salt)')
ax1.set_title('Bể trộn: $\\dfrac{dA}{dt} = r_{in}c_{in} - r_{out}A/V$\n$Hướng tới trạng thái cân bằng$')
ax1.legend()
ax1.set_xlim(-1, 21)
ax1.set_ylim(0, 35)

# Right: Mixing with different flow rates
ax2 = axes2[1]
for r in [1, 2, 4]:
    A = A_ss + (A0 - A_ss) * np.exp(-r*t/V)
    ax2.plot(t, A, linewidth=2, label=f'$r = {r}$')

ax2.axhline(y=A_ss, color='red', linestyle='--', linewidth=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$A(t)$')
ax2.set_title('Ảnh hưởng của tốc độ dòng chảy\n$Tốc độ lớn \\to$ hội tụ nhanh')
ax2.legend()
ax2.set_xlim(-1, 21)
ax2.set_ylim(0, 35)

plt.tight_layout()
plt.savefig(IMG_PATH + '01_07_mixing_detail.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 01-07:")
print("  01_07_applications_population_mixing.svg")
print("  01_07_mixing_detail.svg")
