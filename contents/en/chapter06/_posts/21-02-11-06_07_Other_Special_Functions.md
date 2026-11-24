---
layout: post
title: "06-07 Other Special Functions"
chapter: '06'
order: 7
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: optional
---

Once you see how Legendre polynomials arise from a sphere and Bessel functions from a cylinder, a natural question strikes: is there a whole zoo of orthogonal polynomials, each secretly tailored to a different physical domain and weight function? The answer is a resounding yes. Put a quantum particle in a parabolic potential on $$ (-\infty, \infty) $$ and Hermite polynomials appear with Gaussian weight $$ e^{-x^2} $$. Place an electron in a Coulomb field on $$ [0, \infty) $$ and Laguerre polynomials emerge with exponential weight $$ e^{-x} $$. Minimize the worst-case polynomial approximation error on $$ [-1, 1] $$ and Chebyshev polynomials step forward with weight $$ (1 - x^2)^{-1/2} $$.

Even more remarkably, all of these classical families are unified under one master roof: second-order Sturm–Liouville ODEs and Gauss's hypergeometric function $$ {}_2F_1(a, b; c; z) $$.

## Background Knowledge Map: Classical Orthogonal Polynomials and Hypergeometric Unification

1. **Weight Functions and Domain Geometry (Hilbert Space Choice):** Each family is orthogonal in a weighted inner product $$ \langle f, g \rangle_w = \int_I f(x) g(x) w(x)\,dx $$ matched to its natural domain: Hermite on $$ (-\infty, \infty) $$ with $$ w(x) = e^{-x^2} $$, Laguerre on $$ [0, \infty) $$ with $$ w(x) = e^{-x} $$, and Chebyshev on $$ [-1, 1] $$ with $$ w(x) = (1 - x^2)^{-1/2} $$.
2. **Three-Term Recurrences and Rodrigues' Formulas (Unified Algebra):** Every classical orthogonal polynomial family satisfies a three-term recurrence $$ p_{n+1}(x) = (A_n x + B_n) p_n(x) - C_n p_{n-1}(x) $$ and a Rodrigues differentiation formula $$ p_n(x) = \frac{1}{c_n w(x)} \frac{d^n}{dx^n}[w(x) s(x)^n] $$, guaranteeing $$ n $$ simple real zeros inside the interval $$ I $$.
3. **Minimax Optimality of Chebyshev Polynomials (Numerical Analysis Link):** Because $$ T_n(\cos\theta) = \cos(n\theta) $$ oscillates equiripply between $$ -1 $$ and $$ +1 $$, the monic polynomial $$ 2^{1-n} T_n(x) $$ has the smallest possible $$ L^\infty([-1,1]) $$ norm among all monic degree-$$ n $$ polynomials—eliminating Runge's phenomenon in interpolation and spectral PDE solvers.
4. **Hypergeometric Master Function $$ {}_2F_1(a,b;c;z) $$ (Universal Parent):** Any second-order linear ODE with three regular singular points on the Riemann sphere can be mapped to Gauss's hypergeometric equation, making Legendre, Chebyshev, and Jacobi polynomials terminating cases of $$ {}_2F_1 $$, and Hermite/Laguerre limiting cases of the confluent hypergeometric function $$ {}_1F_1 $$.

### Step-by-Step Worked Example (Read Slowly): Hermite Orthogonality & Chebyshev Minimax Verification

**Problem:** (a) Use the Hermite ODE $$ y'' - 2xy' + 2ny = 0 $$ and Rodrigues' formula $$ H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n}(e^{-x^2}) $$ to compute $$ H_2(x) $$ and verify its orthogonality to $$ H_0(x) = 1 $$ under $$ w(x) = e^{-x^2} $$. (b) Compute $$ T_3(x) $$ from $$ T_n(\cos\theta) = \cos(n\theta) $$ and verify its Chebyshev ODE $$ (1-x^2)y'' - x y' + 9y = 0 $$.

1. **Compute $$ H_2(x) $$ via Rodrigues' formula:**
   - First derivative: $$ \frac{d}{dx}(e^{-x^2}) = -2x e^{-x^2} $$.
   - Second derivative: $$ \frac{d^2}{dx^2}(e^{-x^2}) = (-2 + 4x^2) e^{-x^2} $$.
   - Multiply by $$ (-1)^2 e^{x^2} $$:
     $$ H_2(x) = 4x^2 - 2. $$
2. **Verify Hermite's ODE for $$ n = 2 $$:**
   $$ H_2'(x) = 8x $$, $$ H_2''(x) = 8 $$. Plug into $$ y'' - 2x y' + 4y $$:
   $$ 8 - 2x(8x) + 4(4x^2 - 2) = 8 - 16x^2 + 16x^2 - 8 = 0. $$
3. **Verify weighted orthogonality $$ \int_{-\infty}^{\infty} H_0(x) H_2(x) e^{-x^2}\,dx = 0 $$:**
   Recall the Gaussian moments $$ \int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi} $$ and (by integration by parts) $$ \int_{-\infty}^{\infty} x^2 e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2} $$. Thus
   $$ \int_{-\infty}^{\infty} (4x^2 - 2) e^{-x^2}\,dx = 4\left(\frac{\sqrt{\pi}}{2}\right) - 2\sqrt{\pi} = 2\sqrt{\pi} - 2\sqrt{\pi} = 0. $$
4. **Compute $$ T_3(x) $$ and verify Chebyshev's ODE:**
   Using $$ \cos(3\theta) = 4\cos^3\theta - 3\cos\theta $$ with $$ x = \cos\theta $$ gives
   $$ T_3(x) = 4x^3 - 3x. $$
   Check $$ T_3'(x) = 12x^2 - 3 $$, $$ T_3''(x) = 24x $$. Plug into $$ (1 - x^2) y'' - x y' + 9y $$:
   $$ (1 - x^2)(24x) - x(12x^2 - 3) + 9(4x^3 - 3x) = (-24 - 12 + 36)x^3 + (24 + 3 - 27)x = 0. $$
   Collecting powers explicitly:
   - $$ x^3 $$ coefficient: $$ -24 - 12 + 36 = 0 $$.
   - $$ x $$ coefficient: $$ 24 + 3 - 27 = 0 $$.
   Both vanish identically, and the monic version $$ \frac{1}{4} T_3(x) = x^3 - \frac{3}{4}x $$ stays bounded by $$ \frac{1}{4} $$ everywhere on $$ [-1, 1] $$!

This lesson surveys other important special functions that appear in differential equations: Hermite, Laguerre, Chebyshev, and hypergeometric functions. These complete the "toolkit" of special functions for physics.

> **Teaching Notes**: Optional/survey lesson. Skip if running short on time. Show students there are many more functions available. Activity: "Identify the Function" (10 min)—match ODEs to their solutions.

---

## Introduction

Bessel and Legendre are the most common, but many other special functions appear in specific contexts. This lesson surveys the key ones and their applications.

> **Intuitive**: Special functions are "named polynomials" that solve important ODEs, just as Bessel and Legendre do. Each appears when a specific geometry or symmetry appears.

---

## 1. Hermite Polynomials

### 1.1 Equation

$$ y'' - 2x y' + 2\ell y = 0 $$

For integer $$ \ell = n $$ (nonnegative), solutions are polynomials.

### 1.2 Definition (Rodriguez)

$$ H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n}e^{-x^2} $$

Generating first few:
- $$ H_0(x) = 1 $$
- $$ H_1(x) = 2x $$
- $$ H_2(x) = 4x^2 - 2 $$
- $$ H_3(x) = 8x^3 - 12x $$

### 1.3 Physical Applications

- **Quantum harmonic oscillator**: Wavefunctions involve $$ H_n $$
- **Optics**: Hermite-Gaussian beams in lasers
- **Probability**: Wiener process expectations

### 1.4 Key Properties

- Orthogonal with weight $$ e^{-x^2} $$: $$ \int_{-\infty}^{\infty} H_m H_n e^{-x^2} dx = 0 $$ for $$ m \neq n $$
- Recurrence: $$ H_{n+1}(x) = 2xH_n(x) - 2nH_{n-1}(x) $$

---

## 2. Laguerre Polynomials

### 2.1 Equation

$$ x y'' + (1 - x) y' + n y = 0 $$

For integer $$ n \geq 0 $$, solutions are polynomials.

### 2.2 Definition (Rodriguez)

$$L_n(x) = \frac{e^x}{n!}\frac{d^n}{dx^n}(x^n e^{-x})$$

Generating:
- $$ L_0(x) = 1 $$
- $$ L_1(x) = 1 - x $$
- $$ L_2(x) = 1 - 2x + x^2/2 $$
- $$ L_3(x) = 1 - 3x + 3x^2/2 - x^3/6 $$

### 2.3 Physical Applications

- **Hydrogen atom**: Radial wavefunctions involve Laguerre
- **Quantum mechanics**: Associated Laguerre polynomials $$ L_n^k $$
- **Heat kernels**: Appearance in diffusion equations

### 2.4 Key Properties

- Orthogonal with weight $$ e^{-x} $$ on $$ [0, \infty) $$
- Recurrence: $$ (n+1)L_{n+1} = (2n+1-x)L_n - nL_{n-1} $$

---

## 3. Associated Laguerre Polynomials

### 3.1 Definition

For quantum hydrogen, need $$ L_n^k $$:

$$L_n^k(x) = \frac{x^{-k} e^x}{n!}\frac{d^n}{dx^n}(x^{n+k} e^{-x})$$

These appear in radial Schrödinger equation for hydrogen:
$$R_{n\ell}(r) \propto r^\ell e^{-r/(na_0)} L_{n-\ell-1}^{2\ell+1}\left(\frac{2r}{na_0}\right)$$

### 3.2 Physical Meaning

The quantum number $$ n $$ is the principal quantum number, $$ \ell $$ is the angular momentum quantum number.

---

## 4. Chebyshev Polynomials

### 4.1 Equation

$$ (1 - x^2) y'' - x y' + n^2 y = 0 $$

Solutions: $$ T_n(x) = \cos(n \arccos x) $$.

### 4.2 Definition

$$T_n(x) = \cos(n \arccos x) = \text{(polynomial of degree } n\text{)}$$

Generating:
- $$ T_0(x) = 1 $$
- $$ T_1(x) = x $$
- $$ T_2(x) = 2x^2 - 1 $$
- $$ T_3(x) = 4x^3 - 3x $$

### 4.3 Physical Applications

- **Approximation theory**: Minimax polynomial approximation
- **Spectral methods**: Collocation on $$ [-1, 1] $$
- **Signal processing**: DCT relates to Chebyshev

### 4.4 Key Properties

- Orthogonal with weight $$ (1-x^2)^{-1/2} $$ on $$ [-1, 1] $$
- $$ T_n(\cos\theta) = \cos(n\theta) $$
- Extremal property: Minimizes maximum deviation from zero among degree-$$ n $$ polynomials

---

## 5. Hypergeometric Functions

### 5.1 Equation

$$ x(1-x) y'' + [c - (a+b+1)x] y' - ab y = 0 $$

This is the **hypergeometric equation**, general enough to include many other special functions as special cases.

### 5.2 Solution

$$y = {}_2F_1(a, b; c; x) = \sum_{n=0}^{\infty} \frac{(a)_n (b)_n}{(c)_n n!} x^n$$

where $$ (q)_n = q(q+1)\cdots(q+n-1) $$ is the Pochhammer symbol.

### 5.3 Special Cases

Many functions reduce to $$ {}_2F_1 $$:
- **Legendre**: $$ P_\ell(x) = {}_2F_1(-\ell, \ell+1; 1; (1-x)/2) $$
- **Bessel**: Can be expressed via confluent hypergeometric
- **Hermite**: Related to parabolic cylinder functions

---

## 6. Confluent Hypergeometric Functions

### 6.1 Equation

$$ x y'' + (b - x) y' - a y = 0 $$

Solutions: $$ M(a,b;x) $$ and $$ U(a,b;x) $$.

### 6.2 Applications

- **Whittaker functions**: Coulomb wavefunctions
- **Incomplete gamma**: Related to probability functions

---

## 7. Summary Table

| Function | ODE Form | Key Property | Application |
|----------|--------|--------------|------------|
| Hermite $$ H_n $$ | $$ y'' - 2xy' + 2ny = 0 $$ | Orthogonal ($$ e^{-x^2} $$) | Quantum oscillator |
| Laguerre $$ L_n $$ | $$ xy'' + (1-x)y' + ny = 0 $$ | Orthogonal ($$ e^{-x} $$) | Hydrogen atom |
| Chebyshev $$ T_n $$ | $$ (1-x^2)y'' - xy' + n^2y = 0 $$ | $$ \cos(n\arccos x) $$ | Approximation |
| Hypergeometric $$ {}_2F_1 $$ | $$ x(1-x)y'' + ... $$ | Series | Many special cases |

---

## Conceptual Questions

1. **Why so many functions?** $$ \rightarrow $$ Each arises from a different geometry or boundary condition. The ODE's structure determines the solution's properties (orthogonality weight, singularities, etc.).

2. **How are they related?** $$ \rightarrow $$ Many are special cases of hypergeometric or confluent hypergeometric. Understanding this hierarchy helps navigate between them.

3. **When to use which?** $$ \rightarrow $$ Match the physics/geometry: cylindrical $$ \to $$ Bessel, spherical $$ \to $$ Legendre, harmonic oscillator $$ \to $$ Hermite, Coulomb $$ \to $$ Laguerre.

---

## Interactive Activities

### Activity: "Identify the Function" (10 min)

Match ODEs to their solutions:

| ODE | Solution Type |
|-----|--------------|
| $$ x^2y'' + xy' + (x^2 - \nu^2)y = 0 $$ | Bessel $$ J_\nu $$ |
| $$ (1-x^2)y'' - 2xy' + \ell(\ell+1)y = 0 $$ | Legendre $$ P_\ell $$ |
| $$ y'' - 2xy' + 2\ell y = 0 $$ | Hermite $$ H_\ell $$ |
| $$ xy'' + (1-x)y' + ny = 0 $$ | Laguerre $$ L_n $$ |

---

## Summary

Many special functions exist—Bessel, Legendre, Hermite, Laguerre, Chebyshev, hypergeometric. They each emerge from specific ODEs with physical/geometric significance, and are connected through the hypergeometric hierarchy.

> **One-Liner**: Special functions are named solutions to named ODEs—match the physics (symmetry/boundary conditions) to find the right function.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Quantum harmonic oscillator
- Problem: Normalizable spatial modes of the oscillator satisfy Hermite's equation after factoring out a Gaussian envelope.
- Model:
$$ y''-2x y'+2n y=0. $$
- Assumptions and limitations: The equation is already nondimensionalized and simplified.
- Interpretation: Hermite polynomials label discrete energy levels.

#### Hydrogen radial states
- Problem: After separation and rescaling, part of the radial hydrogen problem satisfies a Laguerre-type equation.
- Model:
$$ x y''+(1-x)y'+n y=0. $$
- Assumptions and limitations: This is a reduced form, not the full physical equation.
- Interpretation: Laguerre polynomials control the nodal structure of the radial states.

#### Spectral approximation and signal processing
- Problem: Stable polynomial bases are needed for interpolation and spectral methods.
- Model:
$$ (1-x^2)y''-x y'+n^2 y=0 $$
for the Chebyshev family.
- Assumptions and limitations: Here the emphasis is numerical rather than purely physical.
- Interpretation: Chebyshev polynomials provide a highly effective approximation basis on $$ [-1,1] $$.

### 2. Additional Intuition and Connections

Special functions are not isolated formula tables. Each family arises as the natural solution of an operator with its own geometry, weight, and boundary conditions. A common pitfall is to memorize families separately instead of seeing the shared eigenfunction structure behind them.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite, eval_laguerre, eval_chebyt

x1 = np.linspace(-3, 3, 400)
x2 = np.linspace(0, 8, 400)
x3 = np.linspace(-1, 1, 400)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(x1, eval_hermite(3, x1))
axes[0].set_title("Hermite H3")
axes[1].plot(x2, eval_laguerre(3, x2))
axes[1].set_title("Laguerre L3")
axes[2].plot(x3, eval_chebyt(4, x3))
axes[2].set_title("Chebyshev T4")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: Hermite polynomials quantum harmonic oscillator
- search: Laguerre polynomials hydrogen atom
- search: Chebyshev polynomials spectral methods

### 5. Worked Example

Hermite's equation
$$ y''-2x y'+2n y=0 $$
has polynomial solutions when $$ n $$ is a nonnegative integer. For $$ n=2 $$,
$$ H_2(x)=4x^2-2. $$
In quantum mechanics, the degree is directly tied to the energy level.

### 6. Difficulty Layering

**Undergraduate level.** Recognize a few classical families and the physical settings where they arise.

**Graduate level.** Relate the families to Sturm-Liouville theory, weighted orthogonality, and spectral approximation methods.

![Special functions]({{ site.imgurl }}/chapter_img/chapter06/06_07_other_special_functions.svg)

## Video tham khảo

- xem trước: [The Gamma Function, its Properties, and Application to Bessel Functions](https://www.youtube.com/watch?v=PwCl7vVyXwY) — Faculty of Khan, English. The gamma function, which normalizes several of the families in this lesson.
- [Hermite and Laguerre Polynomials | Differential Equations](https://www.youtube.com/watch?v=1WlTe-DzO5E) — The Cynical Philosopher, English. Hermite and Laguerre polynomials as the other classical orthogonal families.
- [Intro to the Gamma Function](https://www.youtube.com/watch?v=c7_F4P71E2E) — Physics and Math Lectures, English. The gamma integral that appears in the coefficients of those families.

## References

- Abramowitz & Stegun: *Handbook of Mathematical Functions*—the bible
- NIST Digital Library of Mathematical Functions (dlmf.nist.gov)—modern replacement
- Arfken & Weber: *Mathematical Methods for Physicists*
