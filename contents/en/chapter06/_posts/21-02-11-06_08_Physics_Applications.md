---
layout: post
title: "06-08 Applications in Physics"
chapter: '06'
order: 8
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: optional
---

This lesson shows how series solutions and special functions appear in physics applications: vibrating membranes, quantum mechanics, and heat conduction.

> **Teaching Notes**: Optional/ Applications lesson. Best as review/integration after completing series solutions. Activity: "Derive the Mode" (20 min)—find first vibrational mode of circular drum.

---

## Introduction

This lesson ties together the chapter by showing where the special functions actually appear in physics. Understanding these applications motivates why we study series solutions.

> **Intuitive**: The ODE is the "engine" that powers physical theories. Special functions are the "output"—the specific wave patterns, energy levels, and temperature profiles we measure.

---

## 1. Vibrating Circular Membrane

### 1.1 The Problem

A circular drumhead of radius $$ a $$ obeys the wave equation in polar coordinates $$ (r,\theta) $$. Separating variables $$ u(r,\theta,t) = R(r)\Theta(\theta)T(t) $$ gives:

- **Angular**: $$ \Theta'' = -m^2 \Theta $$ $$ \Rightarrow $$ $$ \Theta = \sin(m\theta), \cos(m\theta) $$ with integer $$ m $$
- **Radial**: $$ r^2 R'' + rR' + (k^2 r^2 - m^2)R = 0 $$ (Bessel's equation of order $$ m $$)
- **Temporal**: $$ T'' + \omega^2 T = 0 $$

Here $$ k^2 = \omega^2/c^2 $$ is the separation constant.

### 1.2 Solutions

The radial solutions are Bessel functions $$ J_m(kr) $$. The boundary condition $$ u(a,\theta,t) = 0 $$ requires:

$$ J_m(ka) = 0 $$

So $$ ka = j_{m,1}, j_{m,2}, \ldots $$ (zeros of $$ J_m $$). This gives quantized frequencies:

$$ \omega_{mn} = c \frac{j_{m,n}}{a} $$

### 1.3 The Modes

The $$ n $$-th radial mode with angular index $$ m $$ has shape $$ J_m(j_{m,n}r/a)\sin(m\theta) $$ or $$ J_m(j_{m,n}r/a)\cos(m\theta) $$.

The $$ m=0 $$ modes ($$ J_0 $$) are radially symmetric ("drumhead going up and down together").

> **Checkpoint**: Can students find the fundamental frequency of a drum of radius $$ a $$?

---

## 2. Hydrogen Atom

### 2.1 The Radial Equation

The time-independent Schrödinger equation in spherical coordinates separates into radial and angular parts. The angular part gives Legendre polynomials (for $$ \ell $$). The radial part is:

$$\frac{d^2 u}{dr^2} + \frac{2m}{\hbar^2}\left(E + \frac{Ze^2}{r} - \frac{\ell(\ell+1)\hbar^2}{2mr^2}\right)u = 0$$

For bound states ($$ E < 0 $$), this becomes associated Laguerre's equation.

### 2.2 Solutions

The radial wavefunctions are:

$$R_{n\ell}(r) = \frac{1}{a_0^{3/2}} \sqrt{\left(\frac{2}{n}\right)^3 \frac{(n-\ell-1)!}{2n[(n+\ell)!]}} \cdot \rho^\ell L_{n-\ell-1}^{2\ell+1}(\rho) e^{-\rho/2}$$

where $$ \rho = 2r/(na_0) $$ and $$ a_0 $$ is the Bohr radius.

### 2.3 Quantum Numbers

- **Principal $$ n $$**: Determines energy $$ E_n = -13.6 \text{ eV}/n^2 $$
- **Orbital $$ \ell $$**: Determines angular momentum (s, p, d, f,...)
- **Magnetic $$ m $$**: Orientation in space (from associated Legendre)

### 2.4 Selection Rules

Transitions between levels satisfy $$ \Delta \ell = \pm 1 $$ (dipole radiation).

---

## 3. Heat Conduction in Cylinders

### 3.1 The Problem

Heat equation $$ \partial_t u = \alpha \nabla^2 u $$ in a cylinder. Separating $$ u(r,t) = R(r)T(t) $$:

- Radial: $$ r^2 R'' + rR' + \lambda^2 r^2 R = 0 $$ (Bessel)
- Temporal: $$ T' + \lambda^2 \alpha T = 0 $$

### 3.2 Solution Form

With insulated boundary $$ \partial_r u(R,t) = 0 $$ (Neumann), we get $$ J_0'(\lambda_n R) = 0 $$:

$$u(r,t) = \sum_{n=1}^{\infty} A_n J_0(\lambda_n r) e^{-\alpha \lambda_n^2 t}$$

The $$ \lambda_n $$ are zeros of $$ J_0' $$.

### 3.3 Physical Interpretation

Different modes decay at different rates. Higher modes ($$ \lambda_n $$ large) decay faster—initial sharp features smooth out.

---

## 4. Electromagnetic Waves in Waveguides

### 4.1 Waveguide Equation

In a rectangular waveguide with conducting walls, the modes satisfy Helmholtz equation with boundary conditions.

### 4.2 TE/TM Modes

Transverse electric (TE) and transverse magnetic (TM) modes involve Bessel functions for circular waveguides.

Cutoff frequencies are determined by zeros of Bessel functions.

---

## 5. Quantum Harmonic Oscillator

### 5.1 The Equation

$$-\frac{\hbar^2}{2m}\psi'' + \frac{1}{2}m\omega^2 x^2 \psi = E\psi$$

This is the Hermite equation with $$ \ell = E/(\hbar\omega) - 1/2 $$.

### 5.2 Energy Quantization

Solutions exist only when:

$$E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, \ldots$$

This is the famous result: energy levels are equally spaced!

### 5.3 Wavefunctions

$$\psi_n(x) = \frac{1}{\sqrt{2^n n!}}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4} H_n\left(\sqrt{\frac{m\omega}{\hbar}} x\right) e^{-m\omega x^2/(2\hbar)}$$

The $$ H_n $$ are Hermite polynomials.

---

## 6. Summary: Matching Physics to Functions

| Physical System | Geometry | Special Function |
|----------------|----------|-----------------|
| Vibrating drum | Circle | Bessel $$ J_m $$ |
| Hydrogen atom | Sphere | Laguerre $$ L_n^\ell $$ |
| Quantum oscillator | Line | Hermite $$ H_n $$ |
| Multipole expansion | Sphere | Legendre $$ P_\ell $$ |
| Circular waveguide | Circle | Bessel $$ J_m $$ |

---

## Conceptual Questions

1. **Why do quantized frequencies appear?** $$ \rightarrow $$ Boundary conditions (like $$ J_m(ka) = 0 $$) pick out discrete wavenumbers. This is the same mathematics as Sturm-Liouville theory: eigenvalues of differential operators.

2. **Why are energy levels equally spaced in harmonic oscillator?** $$ \rightarrow $$ The potential $$ x^2 $$ is symmetric enough that the differential operator has evenly spaced eigenvalues. This is unique to the harmonic oscillator.

3. **What's common to all these?** $$ \rightarrow $$ Separation of variables + boundary conditions → eigenvalue problem → special functions as eigenfunctions.

---

## Interactive Activities

### Activity: "Derive the Mode" (20 min)

**Problem**: Find the fundamental (lowest frequency) vibrational mode of a circular drum of radius $$ a $$.

**Solution**:
1. Wave equation in polar: $$ u_{tt} = c^2 \nabla^2 u $$
2. Separate: $$ R(r)T(t)\Theta(\theta) $$. For lowest mode, take $$ m = 0 $$ (axisymmetric), $$ T(t) = \cos(\omega t) $$
3. Radial equation: $$ r^2 R'' + rR' + \omega^2 r^2/c^2 R = 0 $$ = Bessel of order 0
4. Boundary: $$ R(a) = 0 $$ (fixed edge) $$ \Rightarrow $$ $$ J_0(\omega a/c) = 0 $$
5. First root: $$ J_0(j_{0,1}) = 0 $$ with $$ j_{0,1} = 2.405 $$
6. Frequency: $$ \omega_1 = c j_{0,1}/a $$

**Check**: Students get $$ \omega_1 \approx 2.405c/a $$.

---

## Summary

| Application | Function | Key Output |
|-------------|-----------|------------|
| Circular membrane | Bessel $$ J_m $$ | Eigenfrequencies $$ j_{m,n}/a $$ |
| Hydrogen atom | Laguerre $$ L_n^\ell $$ | Energy levels $$ -13.6/n^2 $$ eV |
| Heat in cylinder | Bessel $$ J_0 $$ | Mode decay rates $$ \lambda_n^2 $$ |
| Quantum oscillator | Hermite $$ H_n $$ | Energy $$ (\hbar\omega)(n + 1/2) $$ |
| Spherical potential | Legendre $$ P_\ell $$ | Multipole moments |

> **One-Liner**: The physics determines the geometry, geometry gives the ODE, ODE's boundary conditions yield eigenvalues, and eigenvalues produce the special functions.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Vibrating circular membranes
- Problem: The wave equation on a disk leads to radial mode shapes governed by Bessel functions.
- Model:
$$ u_{tt}=c^2 \nabla^2 u, $$
with the radial factor satisfying a Bessel equation after separation.
- Assumptions and limitations: Ideal homogeneous membrane with fixed boundary.
- Interpretation: Bessel mode shapes and their zeros determine the allowed frequencies.

#### Quantum harmonic oscillator
- Problem: The one-dimensional stationary Schrodinger equation for a quadratic potential leads to Hermite functions.
- Model:
$$ -\psi''+x^2\psi=E\psi. $$
- Assumptions and limitations: Written in nondimensional form.
- Interpretation: Normalizability forces the series to terminate, producing discrete energy levels.

#### Exterior fields around nearly spherical bodies
- Problem: Laplace's equation in spherical coordinates produces Legendre angular factors.
- Model:
$$ \nabla^2 u=0. $$
- Assumptions and limitations: The geometry is close to spherical symmetry.
- Interpretation: Each Legendre mode corresponds to a multipole contribution.

### 2. Additional Intuition and Connections

The real strength of the chapter is that special functions do not appear randomly. They are footprints of geometry and boundary conditions after separation of variables. A common pitfall is to memorize Bessel, Legendre, and Hermite separately instead of seeing them as structured eigenfunctions of different operators.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, eval_legendre, eval_hermite

r = np.linspace(0, 10, 400)
x = np.linspace(-1, 1, 400)
z = np.linspace(-3, 3, 400)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(r, jv(0, r))
axes[0].set_title("Bessel J0")
axes[1].plot(x, eval_legendre(2, x))
axes[1].set_title("Legendre P2")
axes[2].plot(z, np.exp(-z**2 / 2) * eval_hermite(2, z))
axes[2].set_title("Hermite mode")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: drumhead Bessel mode animation
- search: Legendre multipole visualization
- search: quantum harmonic oscillator Hermite wavefunctions

### 5. Worked Example

For the nondimensional oscillator
$$ \psi''+(2E-x^2)\psi=0, $$
write
$$ \psi(x)=e^{-x^2/2}H(x). $$
Then $$ H $$ satisfies a Hermite-type equation. Requiring $$ \psi $$ not to blow up as $$ \lvert x\rvert\to\infty $$ forces the series for $$ H $$ to terminate, which is the origin of discrete energy levels.

### 6. Difficulty Layering

**Undergraduate level.** Recognize which geometry or physical symmetry leads to which special function.

**Graduate level.** Connect the chapter to self-adjoint operators, orthogonal mode expansions, and spectral theory in PDE.

![Physics applications]({{ site.imgurl }}/chapter_img/chapter06/06_08_physics_applications.svg)

## References

- Jackson, *Classical Electrodynamics*: multipole expansions
- Griffiths, *Introduction to Quantum Mechanics*: hydrogen and oscillator
- Haberman, *Applied PDEs*: heat and waves in cylinders
