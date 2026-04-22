---
layout: post
title: "06-05 Bessel's Equation"
chapter: '06'
order: 5
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: required
---

This lesson introduces Bessel's equation and Bessel functions—the fundamental solutions for cylindrical symmetry. They appear in wave propagation, heat conduction, and static potentials in circular geometries.

> **Teaching Notes**: Important for applications. Show connection to Frobenius (regular singular point at $$ x=0 $$). Emphasize physical interpretation (cylindrical waves). Activity: "Find the Zeros" (15 min)—students find first few zeros of $$ J_0(x) $$.

---

## Introduction

Bessel's equation of order $$ \nu $$ is:

$$ x^2 y'' + x y' + (x^2 - \nu^2) y = 0 $$

This is the ODE for phenomena with **cylindrical symmetry**—waves in circles, heat in cylinders, vibrations of drums. The parameter $$ \nu $$ is the order (often an integer or half-integer from angular momentum quantization).

> **Intuitive**: Just as $$ \sin x $$ and $$ \cos x $$ are the "natural" functions for linear/planar symmetry, Bessel functions are the "natural" functions for circular/cylindrical symmetry.

---

## 1. Physical Appearance

### 1.1 Where Bessel Appears

- **Circular membranes**: Vibrating drumhead obeys Bessel's equation
- **Heat conduction in cylinders**: Temperature profiles involve $$ J_0 $$
- **Electromagnetic waves in waveguides**: TE/TM modes involve Bessel functions
- **Quantum mechanics**: Angular momentum (integer $$ \ell $$) gives Bessel in radial Schrödinger equation

The key: when you separate variables in cylindrical coordinates, the radial equation is Bessel's equation.

### 1.2 Why $$ \nu^2 $$?

The $$ \nu^2 $$ term comes from the $$ \frac{\partial^2}{\partial \theta^2} $$ term in Laplacian in polar coordinates:
$$\nabla^2 u = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial u}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2}$$

For separation $$ u(r,\theta) = R(r)\Theta(\theta) $$, the $$ \Theta $$ equation gives $$ \Theta'' = -\nu^2 \Theta $$, requiring $$ \nu $$ integer for single-valuedness.

---

## 2. Bessel Functions of the First Kind

### 2.1 Definition

For $$ \nu \geq 0 $$:

$$J_\nu(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m! \, \Gamma(m + \nu + 1)} \left(\frac{x}{2}\right)^{2m+\nu}$$

This is the Frobenius series with $$ r = \nu $$:

- At lowest power: $$ a_0 x^\nu $$
- Recurrence from substitution gives the series

### 2.2 Key Properties

**Orthogonality**: $$ J_\nu $$ has an infinite number of real zeros. These zeros are the eigenvalues in boundary value problems.

**Recurrence**:
$$ J_{\nu-1}(x) - J_{\nu+1}(x) = 2 J_\nu'(x) $$
$$J_{\nu-1}(x) + J_{\nu+1}(x) = \frac{2\nu}{x} J_\nu(x)$$

> **Checkpoint**: Students can compute first few terms of $$ J_0(x) $$ and $$ J_1(x) $$?

---

## 3. Bessel Functions of the Second Kind

### 3.1 Definition

When $$ \nu $$ is not an integer, $$ J_{-\nu} $$ is linearly independent from $$ J_\nu $$:

$$Y_\nu(x) = \frac{J_\nu(x) \cos(\nu\pi) - J_{-\nu}(x)}{\sin(\nu\pi)}$$

For integer $$ \nu $$, this is the limit (indeterminate form).

### 3.2 The Integer Case

For integer $$ \nu = n $$, $$ J_{-n}(x) = (-1)^n J_n(x) $$, so they are NOT independent. We need $$ Y_n $$ (also written $$ N_n $$):

$$Y_n(x) = \lim_{m \to n} \frac{J_m(x) \cos(m\pi) - J_{-m}(x)}{\sin(m\pi)}$$

This has a $$ \ln x $$ term (from the repeated root case in Frobenius).

### 3.3 General Solution

For non-integer $$ \nu $$: $$ y = C_1 J_\nu(x) + C_2 J_{-\nu}(x) $$

For integer $$ \nu $$: $$ y = C_1 J_n(x) + C_2 Y_n(x) $$

---

## 4. Worked Examples

### Example 1: $$ J_0(x) $$ Series

From formula with $$ \nu = 0 $$:

$$J_0(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{(m!)^2} \left(\frac{x}{2}\right)^{2m} = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \cdots$$

### Example 2: $$ J_1(x) $$ Series

With $$ \nu = 1 $$:

$$J_1(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m! \, \Gamma(m+2)} \left(\frac{x}{2}\right)^{2m+1} = \frac{x}{2} - \frac{x^3}{16} + \frac{x^5}{384} - \cdots$$

### Example 3: Using Recurrence

Find $$ J_2(x) $$ from $$ J_0 $$ and $$ J_1 $$:

$$ J_2(x) = J_0(x) - \frac{2}{x} J_1(x) $$

This gives $$ J_2(x) = \frac{x^2}{8} - \frac{x^4}{96} + \cdots $$

---

## 5. Modified Bessel Functions

### 5.1 Equation

$$ x^2 y'' + x y' - (x^2 + \nu^2) y = 0 $$

This has solutions $$ I_\nu(x) $$ and $$ K_\nu(x) $$—the modified Bessel functions.

### 5.2 Physical Meaning

$$ I_\nu $$ grows exponentially (for diffusion/heat in cylinders with source)
$$ K_\nu $$ decays exponentially (for static potentials with cylindrical symmetry)

These are important when the spatial equation has $$ -x^2 $$ instead of $$ +x^2 $$.

---

## 6. Zeros and Applications

### 6.1 The Zeros

$$ J_0(x) $$ has zeros at approximately $$ x = 2.405, 5.520, 8.654, \ldots $$

These zeros are the eigenvalues for:
- Vibrating circular drum (boundary condition $$ y(L) = 0 $$)
- Heat conduction in cylinders

### 6.2 The Eigenvalue Problem

For $$ y'' + \frac{1}{x}y' + \lambda y = 0 $$ in $$ 0 < x < L $$:
- Substitute $$ y(x) = u(x)/\sqrt{x} $$, get Bessel equation
- Boundary conditions give quantization of $$ \lambda $$
- The zeros of $$ J_0 $$ determine the modes

---

## 7. Conceptual Questions

1. **Why are there two kinds of Bessel functions?** $$ \rightarrow $$ Second independent solution needed when the first doesn't span the solution space. For integer $$ \nu $$, $$ J_{-n} $$ is not independent, so we construct $$ Y_n $$.

2. **Why do zeros matter?** $$ \rightarrow $$ In boundary value problems, the zeros become the eigenvalues (quantized frequencies/wavenumbers). A drum can only vibrate at certain frequencies.

3. **What's the physical interpretation?** $$ \rightarrow $$ Bessel functions describe circular/wave behavior—like $$ \sin/\cos $$ for linear problems, but the "edges" (boundaries) force quantization.

---

## Interactive Activities

### Activity: "Find the Zeros" (15 min)

Using any method (series, calculator, tables), students find first 3 zeros of $$ J_0(x) $$:

| Zero | Approximate Value |
|------|-----------------|
| $$ j_{0,1} $$ | 2.4048 |
| $$ j_{0,2} $$ | 5.5201 |
| $$ j_{0,3} $$ | 8.6537 |

Discuss: What frequencies can a circular drum of radius $$ L $$ produce? $$ \omega_n = c j_{0,n}/L $$

---

## Summary

| Function | Behavior at $$ x=0 $$ | Uses |
|----------|-------------------|------|
| $$ J_\nu(x) $$ | $$ x^\nu $$ | Finite at origin for $$ \nu \geq 0 $$ |
| $$ Y_\nu(x) $$ | $$ x^{-\nu} $$ | Singular at origin |
| $$ I_\nu(x) $$ | $$ x^\nu $$ | Grows exponentially |
| $$ K_\nu(x) $$ | $$ x^{-\nu} $$ | Decays exponentially |

> **One-Liner**: Bessel functions are the eigenfunctions of cylindrical symmetry—$$ J_\nu $$ for waves, $$ Y_\nu $$ for singular behavior, modified $$ I_\nu, K_\nu $$ for exponential cases.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Circular drum modes
- Problem: Radial vibration modes of a drumhead satisfy Bessel's equation.
- Model:
$$ r^2 R''+rR'+(\lambda r^2-n^2)R=0. $$
- Assumptions and limitations: Ideal circular geometry and fixed boundary.
- Interpretation: Zeros of $$ J_n $$ quantize the allowed vibration frequencies.

#### Heat flow in a cylinder
- Problem: Radial temperature profiles in a cylinder after separation of variables satisfy
$$ r^2 R''+rR'+\lambda r^2 R=0. $$
- Assumptions and limitations: Homogeneous material and cylindrical symmetry.
- Interpretation: Regularity at $$ r=0 $$ selects $$ J_0 $$ instead of the singular solution $$ Y_0 $$.

#### Electromagnetic waveguides
- Problem: TE and TM modes in circular waveguides have Bessel radial profiles.
- Model: The same Bessel structure together with boundary conditions on the waveguide wall.
- Assumptions and limitations: Idealized perfectly conducting geometry.
- Interpretation: Zeros of $$ J_n $$ or its derivative determine cutoff modes.

### 2. Additional Intuition and Connections

Bessel functions play the role in circular geometry that sines and cosines play on an interval. Regularity at the origin eliminates $$ Y_\nu $$ in many physical models. A common pitfall is to treat $$ J_\nu $$ as a table entry rather than as a mode shape whose zeros and asymptotics carry direct physical meaning.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jn_zeros

x = np.linspace(0, 15, 600)
z = jn_zeros(0, 3)

plt.plot(x, jv(0, x), label="J0(x)")
for root in z:
    plt.axvline(root, color="gray", ls="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("J0(x)")
plt.title("First zeros of the Bessel function J0")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Bessel function zeros drumhead modes
- search: cylindrical heat conduction Bessel equation
- search: waveguide modes Bessel functions

### 5. Worked Example

For a drum of radius $$ a $$, the radial boundary condition for the lowest rotational mode is
$$ J_0(\sqrt{\lambda}\,a)=0. $$
If $$ j_{0,1} $$ is the first zero of $$ J_0 $$, then
$$ \sqrt{\lambda}=\frac{j_{0,1}}{a}. $$
So the fundamental frequency is set by the first Bessel zero.

### 6. Difficulty Layering

**Undergraduate level.** Recognize Bessel's equation, distinguish $$ J_\nu $$ from $$ Y_\nu $$, and interpret the role of zeros.

**Graduate level.** Use orthogonality, asymptotics, and Sturm-Liouville structure for Bessel-type operators.

![Bessel equation]({{ site.imgurl }}/chapter_img/chapter06/06_05_bessel_equation.svg)

## References

- Boyce & DiPrima, Section 5.5: Bessel equation
- Haberman, *Applied PDEs*: Bessel in cylindrical problems
- Abramowitz & Stegun: Bessel function tables
