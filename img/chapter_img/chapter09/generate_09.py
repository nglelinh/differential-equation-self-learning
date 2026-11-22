#!/usr/bin/env python3
"""Generate images for Chapter 09 - Heat Equation."""

import matplotlib.pyplot as plt
import numpy as np

from plot_utils import AXIS, BLUE, GREEN, NAVY, PURPLE, RED, SLATE, TEAL, savefig, setup_axes


# 09-01 Derivation of the heat equation
fig1, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
u = 1 - 0.8 * x
flux = -np.gradient(u, x)
ax = axes[0]
ax.plot(x, u, color=NAVY, linewidth=2.4)
setup_axes(ax, '$x$', 'temperature $u(x)$', x_zero=False, y_zero=True)
ax.annotate('a negative gradient drives heat from hot to cold', xy=(0.8, 0.36), xytext=(0.35, 0.92),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.set_title('Temperature gradient along a rod')

ax = axes[1]
ax.plot(x, flux, color=RED, linewidth=2.4)
setup_axes(ax, '$x$', 'heat flux $q(x)$', x_zero=False, y_zero=True)
ax.annotate('Fourier\'s law converts spatial gradient into heat flux', xy=(0.65, flux[50]), xytext=(0.18, 0.55),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.2)
ax.set_title(r'Flux balance behind $u_t = \kappa u_{xx}$')
fig1.suptitle('09-01 Derivation of the Heat Equation: Conservation Plus Fourier\'s Law', fontsize=16, y=0.98)
savefig(fig1, '01_derivation_heat_equation.svg')


# 09-02 Separation of variables
fig2, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
t = np.linspace(0, 1.2, 400)
X = np.sin(np.pi * x)
T = np.exp(-np.pi**2 * t)
ax = axes[0]
ax.plot(x, X, color=NAVY, linewidth=2.4)
setup_axes(ax, '$x$', '$X(x)$', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 1.1)
ax.set_title('Spatial eigenfunction')

ax = axes[1]
ax.plot(t, T, color=TEAL, linewidth=2.4)
setup_axes(ax, '$t$', '$T(t)$', x_zero=True, y_zero=True)
ax.annotate('the separated time factor decays exponentially', xy=(0.55, 0.08), xytext=(0.18, 0.45),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.05)
ax.set_title('Temporal factor for the same mode')
fig2.suptitle('09-02 Separation of Variables: Heat Modes Factor into Space and Time', fontsize=16, y=0.98)
savefig(fig2, '02_separation_of_variables_heat.svg')


# 09-03 Homogeneous boundary conditions
fig3, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
ax = axes[0]
for n, color in [(1, NAVY), (2, TEAL), (3, RED)]:
    ax.plot(x, np.sin(n * np.pi * x), color=color, linewidth=2.2, label=fr'$n={n}$')
ax.scatter([0, 1], [0, 0], color=AXIS, s=32, zorder=4)
setup_axes(ax, '$x$', 'mode shape', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Dirichlet boundary conditions force zero endpoints')
ax.legend(loc='upper right')

ax = axes[1]
for n, color in [(0, NAVY), (1, TEAL), (2, RED)]:
    ax.plot(x, np.cos(n * np.pi * x), color=color, linewidth=2.2, label=fr'$n={n}$')
setup_axes(ax, '$x$', 'mode shape', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Neumann boundary conditions force zero slope at endpoints')
ax.legend(loc='upper right')
fig3.suptitle('09-03 Homogeneous Boundary Conditions: Boundary Type Selects the Mode Family', fontsize=16, y=0.98)
savefig(fig3, '03_homogeneous_bcs_heat.svg')


# 09-04 Nonhomogeneous problems
fig4, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
u_ss = 1 - x
u0 = np.sin(np.pi * x) + u_ss
t = np.linspace(0, 1.2, 400)
u_t = np.outer(np.exp(-np.pi**2 * t), np.sin(np.pi * x)) + u_ss
ax = axes[0]
ax.plot(x, u0, color=NAVY, linewidth=2.3, label='initial profile')
ax.plot(x, u_ss, color=RED, linewidth=2.3, linestyle='--', label='steady state')
setup_axes(ax, '$x$', '$u(x)$', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.4)
ax.set_title('Split into steady state plus transient')
ax.legend(loc='upper right')

ax = axes[1]
for idx, color in zip([0, 70, 180, 399], [NAVY, BLUE, TEAL, RED]):
    ax.plot(x, u_t[idx], color=color, linewidth=2.0)
setup_axes(ax, '$x$', '$u(x,t)$', x_zero=False, y_zero=True)
ax.annotate('subtracting the steady part reduces the problem to homogeneous boundary data',
            xy=(0.65, 0.5), xytext=(0.18, 1.1),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.4)
ax.set_title('Transient profiles relaxing toward equilibrium')
fig4.suptitle('09-04 Nonhomogeneous Heat Problems: Steady State Plus Decaying Transient', fontsize=16, y=0.98)
savefig(fig4, '04_nonhomogeneous_heat.svg')


# 09-05 Infinite domain
fig5, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-6, 6, 700)
times = [0.1, 0.4, 1.0]
ax = axes[0]
for tval, color in zip(times, [NAVY, TEAL, RED]):
    g = np.exp(-x**2 / (4 * tval)) / np.sqrt(4 * np.pi * tval)
    ax.plot(x, g, color=color, linewidth=2.2, label=fr'$t={tval}$')
setup_axes(ax, '$x$', 'heat kernel', x_zero=True, y_zero=True)
ax.set_xlim(-6, 6)
ax.set_ylim(0, 1)
ax.set_title('Fundamental Gaussian spreading on the line')
ax.legend(loc='upper right')

ax = axes[1]
variance = 2 * np.array(times)
ax.plot(times, variance, color=PURPLE, linewidth=2.4, marker='o')
setup_axes(ax, '$t$', 'variance', x_zero=False, y_zero=True)
ax.annotate(r'the width grows like $\sqrt{t}$ while total mass is preserved',
            xy=(0.7, 1.4), xytext=(0.2, 0.65),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 2.5)
ax.set_title('Diffusive spreading scale')
fig5.suptitle('09-05 Heat Equation on an Infinite Domain: Gaussian Smoothing', fontsize=16, y=0.98)
savefig(fig5, '05_heat_infinite_domain.svg')


# 09-06 Fundamental solution and Green's functions
fig6, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-4, 4, 700)
tvals = [0.15, 0.4, 1.0]
ax = axes[0]
for tval, color in zip(tvals, [NAVY, TEAL, RED]):
    G = np.exp(-x**2 / (4 * tval)) / np.sqrt(4 * np.pi * tval)
    ax.plot(x, G, color=color, linewidth=2.2, label=fr'$t={tval}$')
setup_axes(ax, r'$x-\xi$', r'$G(x,t;\xi)$', x_zero=True, y_zero=True)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.8)
ax.set_title('Fundamental solution as time-evolving impulse response')
ax.legend(loc='upper right')

ax = axes[1]
forcing = np.exp(-(x - 1.0)**2)
kernel = np.exp(-x**2 / (4 * 0.5)) / np.sqrt(4 * np.pi * 0.5)
response = np.convolve(forcing, kernel, mode='same') * (x[1] - x[0])
ax.plot(x, forcing / forcing.max(), color=RED, linewidth=2.0, label='initial heat packet')
ax.plot(x, response / response.max(), color=TEAL, linewidth=2.3, label='smoothed response')
setup_axes(ax, '$x$', 'normalized amplitude', x_zero=True, y_zero=True)
ax.annotate('the Green\'s function convolves local input into a globally smoothed profile',
            xy=(1.2, 0.88), xytext=(-2.8, 0.45),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 1.1)
ax.set_title('Green\'s function viewpoint on heat propagation')
ax.legend(loc='upper left')
fig6.suptitle('09-06 Fundamental Solution and Green\'s Functions: Heat as Convolution with a Kernel', fontsize=16, y=0.98)
savefig(fig6, '06_fundamental_solution_greens_functions.svg')


# 09-07 Maximum principles
fig7, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
t = np.linspace(0, 2, 200)
profiles = [np.exp(-np.pi**2 * tval) * np.sin(np.pi * x) for tval in [0, 0.3, 0.8, 1.5]]
ax = axes[0]
for prof, color in zip(profiles, [NAVY, BLUE, TEAL, RED]):
    ax.plot(x, prof, color=color, linewidth=2.1)
setup_axes(ax, '$x$', '$u(x,t)$', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
ax.set_title('Interior peaks diminish over time')

ax = axes[1]
max_vals = np.exp(-np.pi**2 * np.array([0, 0.3, 0.8, 1.5]))
times_plot = np.array([0, 0.3, 0.8, 1.5])
ax.plot(times_plot, max_vals, color=PURPLE, linewidth=2.4, marker='o')
setup_axes(ax, '$t$', 'maximum value', x_zero=True, y_zero=True)
ax.annotate('the maximum principle prevents new interior maxima from forming',
            xy=(0.8, 0.04), xytext=(0.18, 0.42),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1.6)
ax.set_ylim(0, 1.05)
ax.set_title('Monotone decay of the profile maximum')
fig7.suptitle('09-07 Maximum Principles: Diffusion Smooths Rather Than Sharpens', fontsize=16, y=0.98)
savefig(fig7, '07_maximum_principles.svg')


# 09-08 Numerical methods: finite differences
fig8, axes = plt.subplots(1, 2, figsize=(14, 6))
x_nodes = np.linspace(0, 1, 8)
u_nodes = np.sin(np.pi * x_nodes)
ax = axes[0]
ax.plot(x_nodes, u_nodes, color=NAVY, linewidth=2.0, marker='o')
for i in range(1, len(x_nodes) - 1):
    ax.plot([x_nodes[i - 1], x_nodes[i], x_nodes[i + 1]], [u_nodes[i - 1], u_nodes[i], u_nodes[i + 1]], color=TEAL, alpha=0.35)
setup_axes(ax, '$x_i$', '$u_i$', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
ax.set_title('Grid values approximate the continuous temperature profile')

ax = axes[1]
r = np.linspace(0, 0.7, 200)
ax.plot(r, 1 - 2 * r, color=RED, linewidth=2.4)
ax.axhline(0, color=AXIS, linewidth=1.0)
ax.axvline(0.5, color=TEAL, linestyle='--', linewidth=1.2)
setup_axes(ax, 'mesh ratio $r$', 'amplification factor', x_zero=False, y_zero=True)
ax.annotate(r'explicit heat schemes require $r \leq 1/2$ for stability',
            xy=(0.5, 0.0), xytext=(0.12, 0.55),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 0.7)
ax.set_ylim(-0.5, 1.1)
ax.set_title('Stability condition for the explicit finite-difference method')
fig8.suptitle('09-08 Finite Differences: Discretization Introduces a Stability Constraint', fontsize=16, y=0.98)
savefig(fig8, '08_numerical_methods_heat_fd.svg')


# 09-09 Applications of diffusion
fig9, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-5, 5, 700)
times = [0.1, 0.5, 1.5]
ax = axes[0]
for tval, color in zip(times, [NAVY, TEAL, RED]):
    conc = np.exp(-x**2 / (4 * tval)) / np.sqrt(4 * np.pi * tval)
    ax.plot(x, conc, color=color, linewidth=2.2, label=fr'$t={tval}$')
setup_axes(ax, '$x$', 'concentration', x_zero=True, y_zero=True)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 1)
ax.set_title('Diffusive transport of a localized concentration')
ax.legend(loc='upper right')

ax = axes[1]
sigma = np.sqrt(2 * np.array(times))
ax.plot(times, sigma, color=GREEN, linewidth=2.4, marker='o')
setup_axes(ax, '$t$', r'spread scale $\sigma$', x_zero=False, y_zero=True)
ax.annotate(r'many diffusion processes share the same $\sqrt{t}$ spreading law',
            xy=(1.0, 1.2), xytext=(0.18, 0.55),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1.6)
ax.set_ylim(0, 2.0)
ax.set_title('Universal spreading scale for diffusion')
fig9.suptitle('09-09 Diffusion Applications: The Same PDE Models Many Smoothing Processes', fontsize=16, y=0.98)
savefig(fig9, '09_applications_diffusion.svg')


print('Generated Chapter 09 images')
