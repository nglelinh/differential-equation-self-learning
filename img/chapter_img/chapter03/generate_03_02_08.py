#!/usr/bin/env python3
"""
Generate educational images for Chapter 03 lessons
Lessons 03-02 to 03-08
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter03/'

# =============================================================================
# 03-02: Elementary Functions
# =============================================================================
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 6))

# Left: sin(at), cos(at)
ax1 = axes1[0]
t = np.linspace(0, 4*np.pi, 500)

ax1.plot(t, np.sin(t), 'b-', linewidth=2, label='$\\sin t$')
ax1.plot(t, np.cos(t), 'r-', linewidth=2, label='$\\cos t$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$f(t)$')
ax1.set_title('$\\mathcal{L}\\{\\sin at\\} = \\frac{a}{s^2+a^2}$, $\\mathcal{L}\\{\\cos at\\} = \\frac{s}{s^2+a^2}$')
ax1.legend()
ax1.set_xlim(-0.3, 13)

# Right: t^n
ax2 = axes1[1]
t = np.linspace(0, 3, 500)

for n in [1, 2, 3]:
    ax2.plot(t, t**n, linewidth=2, label=f'$t^{n}$')

ax2.set_xlabel('$t$')
ax2.set_ylabel('$t^n$')
ax2.set_title('$\\mathcal{L}\\{t^n\\} = \\frac{n!}{s^{n+1}}$')
ax2.legend()
ax2.set_xlim(-0.3, 3.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_02_elementary_functions.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 03-03: Inverse Laplace
# =============================================================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Partial fractions
ax1 = axes2[0]
s = np.linspace(0.1, 5, 500)

# F(s) = 1/(s(s+1)) = 1/s - 1/(s+1)
f1 = 1/s
f2 = 1/(s+1)
f_total = f1 - f2

ax1.plot(s, f_total, 'b-', linewidth=2)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$s$')
ax1.set_ylabel('$F(s)$')
ax1.set_title('Phân rã phân số: $\\frac{1}{s(s+1)} = \\frac{1}{s} - \\frac{1}{s+1}$')
ax1.set_xlim(-0.3, 5.3)

# Right: s-division
ax2 = axes2[1]
s = np.linspace(0.1, 4, 500)

# F(s) = s/(s^2+1) => f(t) = cos(t)
ax2.plot(s, s/(s**2+1), 'b-', linewidth=2)
ax2.set_xlabel('$s$')
ax2.set_ylabel('$F(s) = \\frac{s}{s^2+1}$')
ax2.set_title('$\\mathcal{L}^{-1}\\{\\frac{s}{s^2+1}\\} = \\cos t$')
ax2.set_xlim(-0.3, 4.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_03_inverse_laplace.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 03-04: Solving IVPs
# =============================================================================
fig3, axes3 = plt.subplots(1, 2, figsize=(14, 6))

# Left: IVP solution
ax1 = axes3[0]
t = np.linspace(0, 5, 500)

# y'' + y = 0, y(0)=1, y'(0)=0 => y = cos(t)
y = np.cos(t)

ax1.plot(t, y, 'b-', linewidth=2, label='$y = \\cos t$')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.scatter([0], [1], color='red', s=100, zorder=5)
ax1.annotate('$y(0)=1$', (0, 1), textcoords="offset points", xytext=(10, 5), fontsize=11)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
ax1.set_title('Giải IVP: $y\'\' + y = 0$, $y(0)=1, y\'(0)=0$\n$\\to y = \\cos t$')
ax1.legend()
ax1.set_xlim(-0.3, 5.3)

# Right: Laplace method
ax2 = axes3[1]
t = np.linspace(0, 5, 500)

# y'' + 2y' + y = 1, y(0)=0, y'(0)=0
# Using Laplace: Y(s)(s^2+2s+1) = 1/s
# Y(s) = 1/(s(s+1)^2) => y = 1 - e^(-t) - t*e^(-t)
y = 1 - np.exp(-t) - t*np.exp(-t)

ax2.plot(t, y, 'b-', linewidth=2)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axhline(y=1, color='red', linestyle='--', alpha=0.7)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Phương pháp Laplace\n$y\'\' + 2y\' + y = 1$')
ax2.set_xlim(-0.3, 5.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_04_solving_ivps.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 03-05: Step Functions
# =============================================================================
fig4, axes4 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Unit step
ax1 = axes4[0]
t = np.linspace(-1, 3, 500)
u = np.where(t >= 0, 1, 0)

ax1.plot(t, u, 'b-', linewidth=2)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.axvline(x=0, color='red', linewidth=1)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$u(t)$')
ax1.set_title('Hàm bước đơn vị $u(t)$\n$\\mathcal{L}\\{u(t-a)\\} = \\frac{e^{-as}}{s}$')
ax1.set_xlim(-1.5, 3.5)
ax1.set_ylim(-0.2, 1.5)

# Right: Shifted step
ax2 = axes4[1]
t = np.linspace(-1, 4, 500)

# f(t) = u(t-1)*t
f = np.where(t >= 1, t-1, 0)
ax2.plot(t, f, 'b-', linewidth=2)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.axvline(x=1, color='red', linewidth=1)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$u(t-1)$')
ax2.set_title('Bước trễ: $u(t-a)f(t-a)$\n$\\to e^{-as}F(s)$')
ax2.set_xlim(-1.5, 4.5)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_05_step_functions.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 03-06: Impulse Functions
# =============================================================================
fig5, axes5 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Delta function approximation
ax1 = axes5[0]
t = np.linspace(-2, 2, 500)

# Approximate delta with narrow Gaussian
for width in [0.5, 0.2, 0.1]:
    delta = (1/(width*np.sqrt(2*np.pi))) * np.exp(-t**2/(2*width**2))
    ax1.plot(t, delta, linewidth=2, label=f'$\\delta_\\epsilon, \\epsilon={width}$')

ax1.set_xlabel('$t$')
ax1.set_ylabel('$\\delta_\\epsilon(t)$')
ax1.set_title('Xấp xỉ hàm Dirac $\\delta(t)$\n$\\int_{-\\infty}^{\\infty} \\delta(t) dt = 1$')
ax1.legend()
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(0, 5)

# Right: Impulse response
ax2 = axes5[1]
t = np.linspace(0, 5, 500)

# Response to delta: y'' + 2y' + y = delta(t)
# y = t*e^(-t) * u(t)
y = t * np.exp(-t)

ax2.plot(t, y, 'b-', linewidth=2)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Phản ứng xung: $\\mathcal{L}\\{\\delta(t)\\} = 1$\n$y\'\' + 2y\' + y = \\delta(t)$')
ax2.set_xlim(-0.3, 5.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_06_impulse_functions.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 03-07: Convolution
# =============================================================================
fig6, axes6 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Convolution visualization
ax1 = axes6[0]
tau = np.linspace(-2, 4, 500)

# f(t) = g(t) * h(t)
# Show f(tau) and g(t-tau) overlap
f = np.exp(-np.abs(tau))
g = np.where((tau >= 0) & (tau <= 2), 1, 0)

ax1.plot(tau, f, 'b-', linewidth=2, label='$f(\\tau)$')
ax1.plot(tau, g, 'r-', linewidth=2, label='$g(t-\\tau)$')
ax1.fill_between(tau, 0, f*g, alpha=0.3)
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('$f(\\tau), g(t-\\tau)$')
ax1.set_title('Tích chập: $(f*g)(t) = \\int_0^t f(\\tau)g(t-\\tau)d\\tau$\n$\\mathcal{L}\\{f*g\\} = F(s)G(s)$')
ax1.legend()
ax1.set_xlim(-2.5, 4.5)

# Right: Convolution example
ax2 = axes6[1]
t = np.linspace(0, 4, 500)

# Convolution of step with exp: (1 * e^(-t)) = 1 - e^(-t)
y = 1 - np.exp(-t)

ax2.plot(t, y, 'b-', linewidth=2)
ax2.set_xlabel('$t$')
ax2.set_ylabel('$(1 * e^{-t})(t)$')
ax2.set_title('Ví dụ tích chập\n$(1 * e^{-t}) = 1 - e^{-t}$')
ax2.set_xlim(-0.3, 4.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_07_convolution.svg', dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 03-08: Transfer Functions
# =============================================================================
fig7, axes7 = plt.subplots(1, 2, figsize=(14, 6))

# Left: Block diagram
ax1 = axes7[0]
t = np.linspace(0, 5, 500)

# Input: step
u = np.ones_like(t)
# Output: response
y = 1 - np.exp(-t)

ax1.plot(t, u, 'b--', linewidth=2, alpha=0.7, label='$u(t)$ (input)')
ax1.plot(t, y, 'r-', linewidth=2, label='$y(t)$ (output)')
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_xlabel('$t$')
ax1.set_ylabel('Signal')
ax1.set_title('Hàm truyền: $Y(s) = G(s)U(s)$\n$Hệ thống LTI')
ax1.legend()
ax1.set_xlim(-0.3, 5.3)

# Right: Frequency response
ax2 = axes7[1]
w = np.linspace(0.1, 5, 500)

# G(s) = 1/(s+1), |G(iw)| = 1/sqrt(w^2+1)
G = 1/np.sqrt(w**2 + 1)

ax2.plot(w, G, 'b-', linewidth=2)
ax2.set_xlabel('$\\omega$')
ax2.set_ylabel('$|G(i\\omega)|$')
ax2.set_title('Đáp ứng tần số\n$G(s) = \\frac{1}{s+1}$')
ax2.set_xlim(0, 5.3)

plt.tight_layout()
plt.savefig(IMG_PATH + '03_08_transfer_functions.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated images for Chapter 03:")
print("  03_02_elementary_functions.svg")
print("  03_03_inverse_laplace.svg")
print("  03_04_solving_ivps.svg")
print("  03_05_step_functions.svg")
print("  03_06_impulse_functions.svg")
print("  03_07_convolution.svg")
print("  03_08_transfer_functions.svg")