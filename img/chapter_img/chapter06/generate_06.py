#!/usr/bin/env python3
"""
Generate images for Chapter 06 - Series Solutions
"""

import numpy as np
import matplotlib.pyplot as plt

IMG_PATH = '/Users/nguyenlelinh/teaching/differential-equation-self-learning/img/chapter_img/chapter06/'

# 06-01: Power Series Review - simple convergence
fig1, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-3, 3, 200)
for n in [1, 2, 3, 5]:
    y = x**n
    ax.plot(x, y, linewidth=1.5, label=f'n={n}')
ax.set_xlabel('x')
ax.set_ylabel('x^n')
ax.set_title('Power series: x^n')
ax.legend()
plt.savefig(IMG_PATH + '06_01_power_series_review.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-02: Ordinary Points
fig2, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-3, 3, 200)
y = np.sin(x)
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Sin as power series')
plt.savefig(IMG_PATH + '06_02_series_ordinary_points.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-03: Euler Equations
fig3, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0.1, 3, 200)
for r in [1, 2, -1]:
    y = x**r if r > 0 else x**(-1)
    ax.plot(x, y, linewidth=2, label=f'r={r}')
ax.set_xlabel('x')
ax.set_ylabel('x^r')
ax.set_title('Euler equation solutions x^r')
ax.legend()
plt.savefig(IMG_PATH + '06_03_euler_equations.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-04: Frobenius Method
fig4, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 3, 200)
for r in [1, 2, 3]:
    # y = x^(r+n) approx
    y = x**(r)
    ax.plot(x, y, linewidth=2, label=f'r={r}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Frobenius: y = sum(a_n x^(n+r))')
ax.legend()
plt.savefig(IMG_PATH + '06_04_frobenius_method.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-05: Bessel Equation
fig5, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0.1, 10, 200)
# Bessel J0 and J1 approximations
from scipy.special import jn
ax.plot(x, jn(0, x), 'b-', linewidth=2, label='J0')
ax.plot(x, jn(1, x), 'r-', linewidth=2, label='J1')
ax.set_xlabel('x')
ax.set_ylabel('J_n(x)')
ax.set_title('Bessel functions')
ax.legend()
plt.savefig(IMG_PATH + '06_05_bessel_equation.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-06: Legendre Equation
fig6, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-1, 1, 200)
from scipy.special import legendre
for n in [0, 1, 2, 3]:
    L = legendre(n)
    ax.plot(x, L(x), linewidth=2, label=f'n={n}')
ax.set_xlabel('x')
ax.set_ylabel('P_n(x)')
ax.set_title('Legendre polynomials')
ax.legend()
plt.savefig(IMG_PATH + '06_06_legendre_equation.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-07: Other Special Functions
fig7, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-5, 5, 200)
y = np.exp(-x**2)
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('x')
ax.set_ylabel('e^(-x^2)')
ax.set_title('Gaussian (hermite basis)')
plt.savefig(IMG_PATH + '06_07_other_special_functions.svg', dpi=150, bbox_inches='tight')
plt.close()

# 06-08: Physics Applications
fig8, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-1, 1, 200)
from scipy.special import legendre
L2 = legendre(2)
ax.plot(x, L2(x), 'b-', linewidth=2)
ax.set_xlabel('theta')
ax.set_ylabel('P2(cos theta)')
ax.set_title('Spherical harmonics: legendre')
plt.savefig(IMG_PATH + '06_08_physics_applications.svg', dpi=150, bbox_inches='tight')
plt.close()

print("Generated Chapter 06 images")