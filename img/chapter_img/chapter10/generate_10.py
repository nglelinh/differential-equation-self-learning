#!/usr/bin/env python3
"""Generate images for Chapter 10 - Wave Equation."""

import matplotlib.pyplot as plt
import numpy as np

from plot_utils import AXIS, BLUE, GREEN, NAVY, PURPLE, RED, SLATE, TEAL, savefig, setup_axes


# 10-01 Derivation of the wave equation
fig1, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
y = 0.15 * np.sin(np.pi * x)
ax = axes[0]
ax.plot(x, y, color=NAVY, linewidth=2.4)
ax.plot(x, np.zeros_like(x), color=AXIS, linewidth=1.0)
setup_axes(ax, '$x$', 'displacement $u(x)$', x_zero=False, y_zero=True)
ax.annotate('local curvature creates restoring tension', xy=(0.5, y[250]), xytext=(0.18, 0.2),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 0.2)
ax.set_title('Bent string configuration')

ax = axes[1]
curv = -np.pi**2 * 0.15 * np.sin(np.pi * x)
ax.plot(x, curv, color=RED, linewidth=2.4)
setup_axes(ax, '$x$', 'acceleration proxy', x_zero=False, y_zero=True)
ax.annotate('Newton\'s law plus tension balance leads to $u_{tt}=c^2u_{xx}$',
            xy=(0.6, -1.0), xytext=(0.12, 0.2),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_title('Curvature drives transverse acceleration')
fig1.suptitle('10-01 Derivation of the Wave Equation: Geometry Plus Force Balance', fontsize=16, y=0.98)
savefig(fig1, '01_derivation_wave_equation.svg')


# 10-02 d'Alembert solution
fig2, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-4, 4, 800)
f = np.exp(-(x + 1.5) ** 2)
g = np.exp(-(x - 1.5) ** 2)
ax = axes[0]
ax.plot(x, f, color=NAVY, linewidth=2.3, label='left-moving part')
ax.plot(x, g, color=RED, linewidth=2.3, label='right-moving part')
setup_axes(ax, '$x$', 'wave profile', x_zero=True, y_zero=True)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 1.1)
ax.set_title('Two traveling waves at a fixed time')
ax.legend(loc='upper right')

ax = axes[1]
u = 0.5 * (f + g)
ax.plot(x, u, color=TEAL, linewidth=2.4)
setup_axes(ax, '$x$', '$u(x,t)$', x_zero=True, y_zero=True)
ax.annotate('d\'Alembert writes the solution as a superposition of two traveling profiles',
            xy=(0.0, 0.12), xytext=(-3.3, 0.75),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 1.1)
ax.set_title('Superposed displacement field')
fig2.suptitle('10-02 d\'Alembert Solution: Wave Motion Splits into Left and Right Propagation', fontsize=16, y=0.98)
savefig(fig2, '02_dalembert_solution.svg')


# 10-03 Separation of variables
fig3, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 1, 500)
t = np.linspace(0, 3, 500)
ax = axes[0]
for n, color in [(1, NAVY), (2, TEAL), (3, RED)]:
    ax.plot(x, np.sin(n * np.pi * x), color=color, linewidth=2.2, label=fr'$n={n}$')
setup_axes(ax, '$x$', '$X_n(x)$', x_zero=False, y_zero=True)
ax.set_xlim(0, 1)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Spatial standing-wave modes')
ax.legend(loc='upper right')

ax = axes[1]
ax.plot(t, np.cos(np.pi * t), color=NAVY, linewidth=2.2, label='mode 1')
ax.plot(t, np.cos(2 * np.pi * t), color=TEAL, linewidth=2.2, label='mode 2')
setup_axes(ax, '$t$', '$T_n(t)$', x_zero=True, y_zero=True)
ax.annotate('each spatial mode oscillates without diffusive decay',
            xy=(1.6, -0.5), xytext=(0.35, 0.8),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 3)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Time factors are oscillatory rather than decaying')
ax.legend(loc='upper right')
fig3.suptitle('10-03 Separation of Variables: Standing Modes and Oscillatory Time Factors', fontsize=16, y=0.98)
savefig(fig3, '03_separation_of_variables_wave.svg')


# 10-04 Higher dimensions
fig4, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-2, 2, 220)
y = np.linspace(-2, 2, 220)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(3 * R) * np.exp(-0.8 * R)
ax = axes[0]
cont = ax.contourf(X, Y, Z, levels=18, cmap='coolwarm')
fig4.colorbar(cont, ax=ax, fraction=0.046, pad=0.04)
setup_axes(ax, '$x$', '$y$')
ax.set_aspect('equal')
ax.set_title('Wave pattern in two spatial dimensions')

ax = axes[1]
r = np.linspace(0, 3, 500)
ax.plot(r, np.cos(3 * r) * np.exp(-0.8 * r), color=PURPLE, linewidth=2.4)
setup_axes(ax, '$r$', 'radial profile', x_zero=True, y_zero=True)
ax.annotate('higher-dimensional waves spread over expanding fronts',
            xy=(1.7, 0.1), xytext=(0.4, 0.75),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)
ax.set_title('Radial cross-section of the wave field')
fig4.suptitle('10-04 Higher-Dimensional Waves: Geometry Alters Propagation Patterns', fontsize=16, y=0.98)
savefig(fig4, '04_wave_higher_dimensions.svg')


# 10-05 Energy and uniqueness
fig5, axes = plt.subplots(1, 2, figsize=(14, 6))
t = np.linspace(0, 8, 500)
energy = np.ones_like(t)
ax = axes[0]
ax.plot(t, energy, color=NAVY, linewidth=2.4)
setup_axes(ax, '$t$', 'energy', x_zero=True, y_zero=True)
ax.annotate('for the ideal wave equation, total energy is conserved',
            xy=(4.0, 1.0), xytext=(1.0, 1.2),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 8)
ax.set_ylim(0, 1.4)
ax.set_title('Constant energy in the undamped case')

ax = axes[1]
u1 = np.cos(np.pi * t)
u2 = np.cos(np.pi * t)
ax.plot(t, u1 - u2, color=RED, linewidth=2.3)
setup_axes(ax, '$t$', 'difference between two solutions', x_zero=True, y_zero=True)
ax.annotate('zero energy of the difference implies uniqueness',
            xy=(5.0, 0.0), xytext=(1.2, 0.45),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 8)
ax.set_ylim(-0.1, 0.6)
ax.set_title('Uniqueness through the energy method')
fig5.suptitle('10-05 Energy and Uniqueness: Conservation Principles Control Solutions', fontsize=16, y=0.98)
savefig(fig5, '05_energy_uniqueness.svg')


# 10-06 Reflection and transmission
fig6, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(-4, 4, 800)
incident = np.exp(-(x + 1.5) ** 2)
reflected = 0.6 * np.exp(-(x + 0.5) ** 2)
transmitted = 0.8 * np.exp(-(x - 1.5) ** 2)
ax = axes[0]
ax.plot(x, incident, color=NAVY, linewidth=2.2, label='incident')
ax.plot(x, reflected, color=RED, linewidth=2.2, label='reflected')
ax.plot(x, transmitted, color=TEAL, linewidth=2.2, label='transmitted')
ax.axvline(0, color=AXIS, linestyle='--', linewidth=1.2)
setup_axes(ax, '$x$', 'amplitude', x_zero=True, y_zero=True)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 1.1)
ax.set_title('Scattering at an interface')
ax.legend(loc='upper right')

ax = axes[1]
R = np.linspace(0, 1, 200)
T = 1 - R
ax.plot(R, T, color=PURPLE, linewidth=2.4)
setup_axes(ax, 'reflection coefficient', 'transmission coefficient', x_zero=False, y_zero=True)
ax.annotate('energy balance links reflection and transmission',
            xy=(0.6, 0.4), xytext=(0.18, 0.72),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('Partition of wave energy at the boundary')
fig6.suptitle('10-06 Reflection and Transmission: Interfaces Redistribute Wave Energy', fontsize=16, y=0.98)
savefig(fig6, '06_reflection_transmission.svg')


# 10-07 Dispersion and dissipation
fig7, axes = plt.subplots(1, 2, figsize=(14, 6))
t = np.linspace(0, 10, 600)
ax = axes[0]
disp1 = np.sin(3 * t)
disp2 = np.sin(3.6 * t)
ax.plot(t, disp1 + disp2, color=NAVY, linewidth=2.1)
setup_axes(ax, '$t$', 'wave packet amplitude', x_zero=True, y_zero=True)
ax.annotate('dispersion spreads a packet because different frequencies travel differently',
            xy=(6.0, 0.15), xytext=(1.2, 1.0),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 10)
ax.set_ylim(-2.2, 2.2)
ax.set_title('Beating and packet spreading')

ax = axes[1]
ax.plot(t, np.exp(-0.12 * t) * np.cos(3 * t), color=RED, linewidth=2.2)
setup_axes(ax, '$t$', 'wave amplitude', x_zero=True, y_zero=True)
ax.annotate('dissipation reduces amplitude while preserving the oscillatory character',
            xy=(6.0, 0.1), xytext=(1.2, 0.85),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 10)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Damping envelope in a dissipative medium')
fig7.suptitle('10-07 Dispersion and Dissipation: Shape Change vs Amplitude Loss', fontsize=16, y=0.98)
savefig(fig7, '07_dispersion_dissipation.svg')


# 10-08 Applications in acoustics and electromagnetics
fig8, axes = plt.subplots(1, 2, figsize=(14, 6))
x = np.linspace(0, 2 * np.pi, 600)
ax = axes[0]
pressure = np.sin(x)
velocity = np.sin(x - np.pi / 2)
ax.plot(x, pressure, color=NAVY, linewidth=2.2, label='pressure')
ax.plot(x, velocity, color=TEAL, linewidth=2.2, label='particle velocity')
setup_axes(ax, '$x$', 'acoustic field', x_zero=True, y_zero=True)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Acoustic wave fields')
ax.legend(loc='upper right')

ax = axes[1]
E = np.sin(x)
B = np.sin(x - np.pi / 2)
ax.plot(x, E, color=RED, linewidth=2.2, label='electric field')
ax.plot(x, B, color=PURPLE, linewidth=2.2, label='magnetic field')
setup_axes(ax, '$x$', 'field amplitude', x_zero=True, y_zero=True)
ax.annotate('wave-equation structure appears across physical media',
            xy=(4.4, -0.25), xytext=(1.0, 0.85),
            arrowprops=dict(arrowstyle='->', color=SLATE, linewidth=1.2), color=SLATE, fontsize=10)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)
ax.set_title('Electromagnetic wave fields')
ax.legend(loc='upper right')
fig8.suptitle('10-08 Applications: The Wave Equation Unifies Acoustics and Electromagnetics', fontsize=16, y=0.98)
savefig(fig8, '08_applications_acoustics_em.svg')


print('Generated Chapter 10 images')
