---
layout: post
title: "06-06 Legendre's Equation"
chapter: '06'
order: 6
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: required
---

In 1782, Adrien-Marie Legendre wanted to calculate the gravitational pull of a slightly flattened oblate planet—a problem that refused to yield to elementary geometry. When he expanded the inverse distance $$ |\mathbf{r} - \mathbf{r}'|^{-1} $$ in powers of $$ r'/r $$, the coefficients of $$ \cos\theta $$ turned out to be a remarkable sequence of polynomials $$ P_0(x), P_1(x), P_2(x), \dots $$ satisfying $$ (1 - x^2) y'' - 2x y' + n(n+1) y = 0 $$.

Why does the eigenvalue parameter take the exact quantized form $$ \lambda = n(n+1) $$? Because $$ x = \pm 1 $$ (the North and South Poles of a sphere!) are regular singular points: for any non-integer $$ \nu $$, *every* series solution blows up logarithmically at the poles. Only when $$ \lambda = n(n+1) $$ does the infinite series truncate into a finite polynomial $$ P_n(x) $$ that stays smooth everywhere on the sphere.

## Key ideas: Legendre's Equation and Spherical Symmetry

1. **Regular Singularities at the Poles $$ x = \pm 1 $$ (Quantization Mechanism):** Writing $$ y'' - \frac{2x}{1-x^2} y' + \frac{\lambda}{1-x^2} y = 0 $$, the origin $$ x = 0 $$ is an ordinary point with guaranteed radius $$ R = 1 $$. The singularities at $$ x = \pm 1 $$ force the infinite series to diverge at the endpoints *unless* $$ \lambda = n(n+1) $$, which kills the recurrence at index $$ n $$ and produces a polynomial.
2. **Self-Adjoint Form and $$ L^2([-1,1]) $$ Orthogonality:** Rewriting the ODE as $$ \frac{d}{dx}\bigl[(1 - x^2) y'\bigr] + n(n+1) y = 0 $$ reveals its Sturm–Liouville structure with unit weight $$ w(x) = 1 $$. Integration by parts immediately proves $$ \int_{-1}^{1} P_m(x) P_n(x)\,dx = \frac{2}{2n+1}\delta_{mn} $$.
3. **Rodrigues' Formula and Generating Function (Compact Engines):** Rather than re-solving recurrences every time, $$ P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n}\bigl[(x^2 - 1)^n\bigr] $$ and $$ (1 - 2xt + t^2)^{-1/2} = \sum_{n=0}^\infty P_n(x) t^n $$ package all orthogonality, normalization $$ P_n(1) = 1 $$, and three-term recurrence relations into two lines.
4. **Multipole & Quantum Angular Momentum Bridge:** Expanding a potential or wavefunction in $$ P_n(\cos\theta) $$ decomposes it into monopole ($$ n=0 $$), dipole ($$ n=1 $$), quadrupole ($$ n=2 $$), and higher spherical harmonics—the foundation of electrostatics, geodesy, and atomic orbitals.

### Worked example: Deriving $$ P_3(x) $$ from the Recurrence and Expanding $$ f(x) = x^3 $$

**Problem:** Derive $$ P_3(x) $$ from the ordinary-point recurrence of Legendre's equation with $$ n = 3 $$ (normalized so $$ P_3(1) = 1 $$), verify orthogonality $$ \int_{-1}^1 P_1(x) P_3(x)\,dx = 0 $$, and express $$ x^3 $$ as a linear combination of Legendre polynomials.

1. **Set up the recurrence for $$ (1 - x^2) y'' - 2x y' + n(n+1) y = 0 $$:**
   Substituting $$ y = \sum_{k=0}^\infty a_k x^k $$ yields
   $$ a_{k+2} = -\frac{(n - k)(n + k + 1)}{(k+2)(k+1)} a_k \qquad (k \ge 0). $$
2. **Specialize to $$ n = 3 $$ (odd branch $$ a_0 = 0 $$):**
   - For $$ k = 1 $$: $$ a_3 = -\frac{(3 - 1)(3 + 2)}{3 \cdot 2} a_1 = -\frac{2 \cdot 5}{6} a_1 = -\frac{5}{3} a_1 $$.
   - For $$ k = 3 $$: $$ a_5 = -\frac{(3 - 3)(3 + 4)}{5 \cdot 4} a_3 = 0 $$, so all higher odd coefficients vanish!
   Thus the polynomial solution is $$ y(x) = a_1 \left(x - \frac{5}{3} x^3\right) $$.
3. **Normalize by $$ P_3(1) = 1 $$:**
   $$ P_3(1) = a_1\left(1 - \frac{5}{3}\right) = -\frac{2}{3} a_1 = 1 \implies a_1 = -\frac{3}{2}. $$
   Therefore,
   $$ P_3(x) = \frac{1}{2}(5x^3 - 3x). $$
4. **Verify orthogonality against $$ P_1(x) = x $$:**
   $$ \int_{-1}^{1} x \cdot \frac{1}{2}(5x^3 - 3x)\,dx = \frac{1}{2}\left[x^5 - x^3\right]_{-1}^{1} = \frac{1}{2}\bigl[(1 - 1) - (-1 + 1)\bigr] = 0. $$
5. **Expand $$ f(x) = x^3 $$ in the Legendre basis:**
   Solving $$ P_3(x) = \frac{5}{2}x^3 - \frac{3}{2}P_1(x) $$ for $$ x^3 $$ gives immediately:
   $$ x^3 = \frac{2}{5} P_3(x) + \frac{3}{5} P_1(x). $$
   Check at $$ x = 1 $$: $$ \frac{2}{5}(1) + \frac{3}{5}(1) = 1 = 1^3 $$. Check at $$ x = \frac{1}{2} $$: $$ P_3(1/2) = \frac{1}{2}(5/8 - 3/2) = -\frac{7}{16} $$, so $$ \frac{2}{5}\left(-\frac{7}{16}\right) + \frac{3}{5}\left(\frac{1}{2}\right) = \frac{-14 + 24}{80} = \frac{10}{80} = \frac{1}{8} = \left(\frac{1}{2}\right)^3 $$. Exact!

This lesson introduces Legendre's equation and Legendre polynomials—the fundamental solutions for spherical symmetry. They appear in potential theory, quantum mechanics, and expand arbitrary functions on the sphere.

> **Teaching Notes**: Similar structure to Bessel but simpler (regular singular point at $$ x = \pm 1 $$). Show orthogonality—key for Fourier-Legendre expansions. Activity: "Verify Orthogonality" (15 min)—compute $$ \int_{-1}^1 P_m(x)P_n(x)dx $$ or show zeros interlace.

---

## Introduction

Legendre's equation of order $$ \ell $$ is:

$$ (1 - x^2) y'' - 2x y' + \ell(\ell + 1) y = 0 $$

This is the ODE for phenomena with **spherical symmetry**—gravitational potential, electrostatic potential, angular momentum in quantum mechanics. The parameter $$ \ell $$ is the angular momentum quantum number (nonnegative integer).

> **Intuitive**: Just as Bessel handles circles, Legendre handles spheres. The singularity at $$ x = \pm 1 $$ (not $$ x = 0 $$) corresponds to the "poles" of a sphere.

---

## 1. Physical Appearance

### 1.1 Where Legendre Appears

- **Gravitational/electrostatic potential**: $$ \Phi = \sum_\ell P_\ell(\cos\theta) r^{-\ell-1} $$
- **Quantum mechanics**: Angular momentum eigenstates
- **Geophysics**: Earth's gravitational field expansion
- **Expanding functions on a sphere**: Spherical harmonics involve Legendre polynomials $$ P_\ell $$

### 1.2 Why $$ \ell(\ell + 1) $$?

The $$ \ell(\ell + 1) $$ term comes from the angular part of Laplacian in spherical coordinates:
$$\nabla^2 u = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial u}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial u}{\partial \theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 u}{\partial \phi^2}$$

For separation $$ u(r,\theta) = R(r)\Theta(\theta) $$, the $$ \Theta $$ equation gives Legendre's equation with eigenvalue $$ \ell(\ell + 1) $$.

---

## 2. Legendre Polynomials

### 2.1 Definition

The **Legendre polynomials** $$ P_\ell(x) $$ are the solutions that are finite at $$ x = \pm 1 $$:

**Rodriguez formula**:
$$P_\ell(x) = \frac{1}{2^\ell \ell!}\frac{d^\ell}{dx^\ell}(x^2 - 1)^\ell$$

This generates polynomials of degree $$ \ell $$:

- $$ P_0(x) = 1 $$
- $$ P_1(x) = x $$
- $$ P_2(x) = \frac{1}{2}(3x^2 - 1) $$
- $$ P_3(x) = \frac{1}{2}(5x^3 - 3x) $$
- $$ P_4(x) = \frac{1}{8}(35x^4 - 30x^2 + 3) $$

### 2.2 Key Properties

1. **Orthogonality**: $$ \displaystyle \int_{-1}^1 P_m(x) P_n(x) \, dx = 0 $$ if $$ m \neq n $$
2. **Normalization**: $$\displaystyle \int_{-1}^1 [P_\ell(x)]^2 \, dx = \frac{2}{2\ell + 1}$$
3. **Recurrence**: $$(\ell + 1)P_{\ell+1}(x) = (2\ell + 1)xP_\ell(x) - \ell P_{\ell-1}(x)$$
4. **Parity**: $$ P_\ell(-x) = (-1)^\ell P_\ell(x) $$ (odd/even)

> **Checkpoint**: Can students generate $$ P_2, P_3 $$ from the recurrence or Rodrigues formula?

---

## 3. Legendre Functions of the Second Kind

### 3.1 Definition

For $$ \ell $$ (not integer), $$ Q_\ell(x) $$ is the second independent solution:

$$Q_\ell(x) = P_\ell(x) \int^x \frac{dt}{(1-t^2)[P_\ell(t)]^2}$$

This involves a logarithm and diverges at $$ x = \pm 1 $$.

### 3.2 The Integer Case

For integer $$ \ell $$, $$ Q_\ell(x) $$ behaves as $$ (x-1)^\ell $$ near $$ x = 1 $$ and blows up at $$ x = -1 $$.

### 3.3 General Solution

For non-integer $$ \ell $$: $$ y = C_1 P_\ell(x) + C_2 Q_\ell(x) $$

For integer $$ \ell $$: $$ y = C_1 P_\ell(x) + C_2 Q_\ell(x) $$

In physical problems, we typically keep only $$ P_\ell $$ because we require finite behavior at $$ x = \pm 1 $$.

---

## 4. Associated Legendre Functions

### 4.1 Definition

For integer $$ m $$ with $$ 0 \leq m \leq \ell $$:

$$P_\ell^m(x) = (-1)^m (1 - x^2)^{m/2} \frac{d^m}{dx^m} P_\ell(x)$$

These appear in spherical harmonics $$Y_\ell^m(\theta, \phi) = P_\ell^m(\cos\theta) e^{im\phi}$$.

### 4.2 Physical Meaning

The integer $$ m $$ corresponds to magnetic quantum number in quantum mechanics. The full angular momentum states are indexed by $$ \ell $$ (angular) and $$ m $$ (magnetic).

---

## 5. Worked Examples

### Example 1: Verify $$ P_2(x) $$ satisfies Legendre's equation with $$ \ell = 2 $$

$$ P_2(x) = \frac{1}{2}(3x^2 - 1) $$

Compute derivatives:
$$ P_2' = 3x $$, $$ P_2'' = 3 $$

Substitute into $$ (1 - x^2)y'' - 2xy' + \ell(\ell+1)y $$:
$$= (1-x^2)(3) - 2x(3x) + 2(3)( \frac{1}{2}(3x^2 - 1))$$
$$ = 3 - 3x^2 - 6x^2 + 3(3x^2 - 1) $$
$$ = 3 - 3x^2 - 6x^2 + 9x^2 - 3 = 0 $$

Check!

### Example 2: Compute $$ \int_{-1}^1 P_2(x) \, dx $$

Use orthogonality: equals 0 (since $$ P_0(x) = 1 $$ is orthogonal to $$ P_2(x) $$).

### Example 3: Find the expansion coefficient for $$ f(x) = x^2 $$ in Legendre basis

Since $$ x^2 = \frac{2}{3}P_2(x) + \frac{1}{3}P_0(x) $$:
$$\int_{-1}^1 x^2 \cdot P_2(x) \, dx \Big/ \int_{-1}^1 [P_2(x)]^2 \, dx = \frac{2}{3} \Big/ \frac{2}{5} = \frac{5}{3}$$

Actually, compute properly: $$ x^2 = \frac{2}{3}P_2 + \frac{1}{3}P_0 $$.

---

## 6. Generating Functions

### 6.1 The Generating Function

$$\frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{\ell=0}^{\infty} P_\ell(x) t^\ell$$

This is useful for deriving identities and understanding the polynomials as "moments" of the unit sphere.

### 6.2 Applications

This generating function appears in:
- Gravitational potential of a displaced sphere
- Multipole expansions in physics

---

## 7. Conceptual Questions

1. **Why polynomials?** $$ \rightarrow $$ The boundary conditions (finite at $$ x = \pm 1 $$) force $$ \ell $$ to be integer, otherwise solutions diverge.

2. **Why orthogonality?** $$ \rightarrow $$ Legendre polynomials are eigenfunctions of a Sturm-Liouville problem—self-adjoint operator with weight 1 on $$ [-1, 1] $$.

3. **What's the physical interpretation?** $$ \rightarrow $$ Legendre polynomials $$ P_\ell $$ are the spherical harmonics' radial parts—they encode how potential falls off with angle in spherical geometry.

---

## Interactive Activities

### Activity: "Verify Orthogonality" (15 min)

Students compute integrals:

$$\int_{-1}^1 P_2(x)P_0(x)dx = \int_{-1}^1 \frac{1}{2}(3x^2-1) \cdot 1 \, dx = \frac{1}{2}[x^3]_{-1}^1 - \frac{1}{2}[x]_{-1}^1 = 0$$

Also verify: $$\int_{-1}^1 [P_2(x)]^2 dx = \frac{2}{2\cdot2+1} = \frac{2}{5}$$.

---

## Summary

| Property | Formula |
|----------|----------|
| Rodriguez | $$P_\ell(x) = \frac{1}{2^\ell\ell!}\frac{d^\ell}{dx^\ell}(x^2-1)^\ell$$ |
| Orthogonality | $$ \int_{-1}^1 P_m P_n = 0 $$ for $$ m \neq n $$ |
| Norm | $$ \int_{-1}^1 P_\ell^2 = \frac{2}{2\ell+1} $$ |
| Recurrence | $$(\ell+1)P_{\ell+1} = (2\ell+1)xP_\ell - \ell P_{\ell-1}$$ |
| Parity | $$ P_\ell(-x) = (-1)^\ell P_\ell(x) $$ |

> **One-Liner**: Legendre polynomials $$ P_\ell(x) $$ are the eigenfunctions of spherical symmetry—finite at poles, orthogonal on $$ [-1,1] $$, forming complete basis for expansions.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Electrostatics and gravitation around spheres
- Problem: After separation of variables in spherical coordinates, the angular equation becomes Legendre's equation.
- Model:
$$ (1-x^2)y''-2x y'+n(n+1)y=0,\qquad x=\cos\theta. $$
- Assumptions and limitations: This describes problems with spherical symmetry and simple azimuthal behavior.
- Interpretation: Legendre polynomials encode multipole structure of the field.

#### Quantum angular momentum
- Problem: The angular part of the hydrogen atom wavefunction leads to the associated Legendre family.
- Model: The case $$ m=0 $$ reduces to the ordinary Legendre equation.
- Assumptions and limitations: This is only the simplest slice of the full spherical harmonic theory.
- Interpretation: Boundedness on $$ [-1,1] $$ forces discrete angular modes.

### 2. Additional Intuition and Connections

Legendre functions are natural on spherical geometry. When the parameter is exactly $$ n(n+1) $$, the bounded solution becomes a polynomial, which is a first sign of mode quantization. A common pitfall is to assume every parameter value produces a polynomial or a bounded solution.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

x = np.linspace(-1, 1, 400)
for n in range(5):
    plt.plot(x, eval_legendre(n, x), label=f"P{n}")

plt.xlabel("x")
plt.ylabel("Pn(x)")
plt.title("First Legendre polynomials")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Legendre polynomials spherical harmonics
- search: electrostatics multipole Legendre
- search: quantum angular equation Legendre

### 5. Worked Example

Find a bounded solution of
$$ (1-x^2)y''-2xy'+6y=0. $$
Since $$ 6=2\cdot 3 $$, this is the case $$ n=2 $$, so the bounded polynomial solution is
$$ P_2(x)=\frac{1}{2}(3x^2-1). $$
In electrostatics, this is the standard quadrupole angular mode.

### 6. Difficulty Layering

**Undergraduate level.** Learn the basic Legendre equation, Rodrigues' formula, and the first few polynomials.

**Graduate level.** Connect orthogonality on $$ [-1,1] $$ to self-adjoint operators and spherical harmonics.

![Legendre equation]({{ site.imgurl }}/chapter_img/chapter06/06_06_legendre_equation.svg)

## Video tham khảo

- xem trước: [Intro to Legendre Polynomials](https://www.youtube.com/watch?v=djlUmwbPw20) — Physics and Math Lectures, English. What Legendre polynomials are and why the equation produces a polynomial for special degrees.
- [Lecture 42 part 3 (Orthogonality of Legendre Polynomials)](https://www.youtube.com/watch?v=gwTmJN8mucE) — Daniel Maxin, English. Orthogonality of the Legendre polynomials on [-1,1].
- [Legendre Polynomial | Orthogonal Properties of Legendre Polynomial](https://www.youtube.com/watch?v=RDU7FTqgx7s) — Dr.Gajendra Purohit, English. A further lecture on the orthogonality relations used in expansions.

## References

- Boyce & DiPrima, Section 5.6: Legendre polynomials
- Arfken & Weber: spherical harmonics details
- Jackson, *Classical Electrodynamics*: multipole expansions
