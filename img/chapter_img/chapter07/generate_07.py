#!/usr/bin/env python3
"""Generate images for Chapter 07 - Boundary Value Problems and Sturm-Liouville Theory."""

import matplotlib.pyplot as plt
import numpy as np

from plot_utils import AXIS, BLUE, GREEN, NAVY, PURPLE, RED, SLATE, TEAL, IMG_PATH, setup_axes


def savefig(fig, filename):
    fig.tight_layout()
    fig.savefig(IMG_PATH / filename, dpi=220, bbox_inches='tight')
    plt.close(fig)


# 07-01 Two-point BVPs
fig1, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 400)
ax = axes[0]
for c, color in [(-0.25, NAVY), (0.0, TEAL), (0.2, RED)]:
    y = x * (1 - x) + c * x * (1 - x) * (2 * x - 1)
    ax.plot(x, y, color=color, linewidth=2.2)
ax.scatter([0, 1], [0, 0], color=AXIS, s=35, zorder=4)
setup_axes(ax, '$x$', '$y(x)$', x_zero=False, y_zero=True)
ax.annotate('boundary conditions anchor the solution at both ends', xy=(1, 0), xytext=(0.45, 0.42),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 0.55)
ax.set_title('Two-point boundary conditions constrain the whole curve')

ax = axes[1]
y_family = [x * (1 - x), 2 * x * (1 - x), x * (1 - x) + 0.1]
styles = [(NAVY, 'BVP solution'), (RED, 'same interior law, wrong amplitude'), (PURPLE, 'violates boundary condition')]
for y, (color, label) in zip(y_family, styles):
    ax.plot(x, y, color=color, linewidth=2.2, label=label)
setup_axes(ax, '$x$', '$y(x)$', x_zero=False, y_zero=True)
ax.annotate('unlike an IVP, satisfying the differential equation is not enough',
            xy=(0.7, 0.16), xytext=(0.22, 0.45),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 0.65)
ax.set_title('Global boundary matching determines admissibility')
ax.legend(loc='upper right')
fig1.suptitle('07-01 Two-Point BVPs: Boundary Data Select Global Shapes', fontsize=16, y=0.98)
savefig(fig1, '01_two_point_bvps.svg')


# 07-02 Eigenvalue problems
fig2, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, np.pi, 500)
ax = axes[0]
for n, color in [(1, NAVY), (2, TEAL), (3, RED)]:
    ax.plot(x, np.sin(n * x), color=color, linewidth=2.2, label=fr'$n={n}$')
setup_axes(ax, '$x$', '$y_n(x)$', x_zero=False, y_zero=True)
ax.set_xlim(0, np.pi)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Only special mode shapes satisfy both the ODE and the boundary data')
ax.legend(loc='upper right')

ax = axes[1]
n = np.arange(1, 7)
lam = n**2
ax.scatter(n, lam, color=NAVY, s=45)
ax.plot(n, lam, color=NAVY, linewidth=1.5)
setup_axes(ax, 'mode index $n$', r'eigenvalue $\lambda_n$', x_zero=False, y_zero=True)
ax.annotate('the boundary conditions quantize the admissible spectrum',
            xy=(4, 16), xytext=(2.0, 28),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0.5, 6.5)
ax.set_ylim(0, 40)
ax.set_title('Discrete eigenvalues for the string problem')
fig2.suptitle('07-02 Eigenvalue Problems: Modes and Spectral Quantization', fontsize=16, y=0.98)
savefig(fig2, '02_eigenvalue_problems.svg')


# 07-03 Sturm-Liouville theory
fig3, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-1, 1, 500)
ax = axes[0]
P1 = x
P2 = 0.5 * (3 * x**2 - 1)
ax.plot(x, P1, color=NAVY, linewidth=2.2, label='$P_1(x)$')
ax.plot(x, P2, color=RED, linewidth=2.2, label='$P_2(x)$')
setup_axes(ax, '$x$', 'eigenfunction value', x_zero=True, y_zero=True)
ax.annotate('self-adjoint structure produces orthogonal eigenfunctions',
            xy=(0.45, 0.1), xytext=(-0.9, 0.95),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(-1, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Representative Sturm-Liouville eigenfunctions')
ax.legend(loc='upper right')

ax = axes[1]
prod = P1 * P2
ax.plot(x, prod, color=PURPLE, linewidth=2.2)
ax.fill_between(x, 0, prod, where=prod >= 0, color=TEAL, alpha=0.3)
ax.fill_between(x, 0, prod, where=prod < 0, color=RED, alpha=0.3)
setup_axes(ax, '$x$', '$P_1(x)P_2(x)$', x_zero=True, y_zero=True)
ax.annotate('positive and negative contributions cancel in the weighted inner product',
            xy=(0.1, -0.08), xytext=(-0.95, 0.45),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(-1, 1)
ax.set_ylim(-0.3, 0.6)
ax.set_title('Orthogonality viewed through sign cancellation')
fig3.suptitle('07-03 Sturm-Liouville Theory: Self-Adjointness Creates Spectral Geometry', fontsize=16, y=0.98)
savefig(fig3, '03_sturm_liouville_theory.svg')


# 07-04 Eigenfunction expansions
fig4, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, np.pi, 500)
target = x * (np.pi - x)
partial_1 = (8 / np.pi**3) * np.sin(x)
partial_3 = partial_1 + (8 / np.pi**3) * (1 / 3**3) * np.sin(3 * x)
partial_5 = partial_3 + (8 / np.pi**3) * (1 / 5**3) * np.sin(5 * x)
ax = axes[0]
ax.plot(x, target, color=AXIS, linewidth=2.3, linestyle='--', label='target shape')
ax.plot(x, partial_1, color=NAVY, linewidth=1.8, label='1 mode')
ax.plot(x, partial_3, color=TEAL, linewidth=1.8, label='3 modes')
ax.plot(x, partial_5, color=RED, linewidth=1.8, label='5 modes')
setup_axes(ax, '$x$', 'function value', x_zero=False, y_zero=True)
ax.set_xlim(0, np.pi)
ax.set_title('More eigenfunctions improve the approximation')
ax.legend(loc='upper right')

ax = axes[1]
n = np.arange(1, 8)
coeffs = 1 / n**2
ax.bar(n, coeffs, color=BLUE, alpha=0.8)
setup_axes(ax, 'mode index $n$', 'coefficient magnitude', x_zero=False, y_zero=True)
ax.annotate('the expansion encodes the function by its mode amplitudes',
            xy=(4, 0.06), xytext=(2.2, 0.16),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0.5, 7.5)
ax.set_ylim(0, 1.1)
ax.set_title('Spectral coefficients in an eigenfunction basis')
fig4.suptitle('07-04 Eigenfunction Expansions: Generalized Fourier Coordinates', fontsize=16, y=0.98)
savefig(fig4, '04_eigenfunction_expansions.svg')


# 07-05 Green's functions
fig5, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
xi = 0.4
G = np.where(x <= xi, x * (1 - xi), xi * (1 - x))
ax = axes[0]
ax.plot(x, G, color=NAVY, linewidth=2.4)
ax.axvline(xi, color=RED, linestyle='--', linewidth=1.2)
setup_axes(ax, '$x$', r'$G(x,\xi)$', x_zero=False, y_zero=True)
ax.annotate('the source point creates a kink in the Green\'s function',
            xy=(xi, G.max()), xytext=(0.58, 0.28),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.35)
ax.set_title('Green\'s function for a simple two-point BVP')

ax = axes[1]
forcing = np.exp(-40 * (x - 0.7)**2)
response = np.cumsum(G * forcing) * (x[1] - x[0])
ax.plot(x, forcing / forcing.max(), color=RED, linewidth=2.1, label='localized forcing')
ax.plot(x, response / response.max(), color=TEAL, linewidth=2.3, label='induced response')
setup_axes(ax, '$x$', 'normalized amplitude', x_zero=False, y_zero=True)
ax.annotate('Green\'s function converts pointwise forcing into a global response profile',
            xy=(0.72, 0.85), xytext=(0.2, 0.38),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.set_title('Impulse-response interpretation of a BVP')
ax.legend(loc='upper left')
fig5.suptitle('07-05 Green\'s Functions: Boundary-Value Analog of Impulse Response', fontsize=16, y=0.98)
savefig(fig5, '05_greens_functions_bvp.svg')


# 07-06 Vibrating strings
fig6, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
ax = axes[0]
for n, color in [(1, NAVY), (2, TEAL), (3, RED)]:
    ax.plot(x, np.sin(n * np.pi * x), color=color, linewidth=2.2, label=fr'mode $n={n}$')
setup_axes(ax, '$x$', 'displacement shape', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Standing-wave mode shapes with fixed endpoints')
ax.legend(loc='upper right')

ax = axes[1]
t = np.linspace(0, 4, 500)
amp1 = np.cos(np.pi * t)
amp2 = 0.5 * np.cos(2 * np.pi * t)
ax.plot(t, amp1, color=NAVY, linewidth=2.2, label='mode 1 amplitude')
ax.plot(t, amp2, color=TEAL, linewidth=2.2, label='mode 2 amplitude')
setup_axes(ax, '$t$', 'time coefficient', x_zero=True, y_zero=True)
ax.annotate('each spatial mode oscillates with its own natural frequency',
            xy=(2.5, -0.5), xytext=(0.8, 0.8),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 4)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Temporal oscillation of separated modes')
ax.legend(loc='upper right')
fig6.suptitle('07-06 Vibrating Strings: Boundary Conditions Create Standing Waves', fontsize=16, y=0.98)
savefig(fig6, '06_vibrating_strings.svg')


# 07-07 Heat conduction
fig7, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
u0 = x * (1 - x)
u1 = np.exp(-1) * u0
u2 = np.exp(-3) * u0
ax = axes[0]
ax.plot(x, u0, color=NAVY, linewidth=2.3, label='$t=0$')
ax.plot(x, u1, color=TEAL, linewidth=2.3, label='$t=1$')
ax.plot(x, u2, color=RED, linewidth=2.3, label='$t=3$')
setup_axes(ax, '$x$', 'temperature $u(x,t)$', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.32)
ax.set_title('Profiles flatten as heat diffuses')
ax.legend(loc='upper right')

ax = axes[1]
t = np.linspace(0, 4, 500)
energy = np.exp(-2 * t)
ax.plot(t, energy, color=PURPLE, linewidth=2.4)
setup_axes(ax, '$t$', 'thermal energy proxy', x_zero=True, y_zero=True)
ax.annotate('heat flow dissipates gradients and lowers the energy over time',
            xy=(2.4, 0.07), xytext=(0.9, 0.5),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 4)
ax.set_ylim(0, 1.05)
ax.set_title('Monotone decay toward equilibrium')
fig7.suptitle('07-07 Heat Conduction: Diffusion Smooths the Spatial Profile', fontsize=16, y=0.98)
savefig(fig7, '07_heat_conduction.svg')


print('Generated Chapter 07 images')
