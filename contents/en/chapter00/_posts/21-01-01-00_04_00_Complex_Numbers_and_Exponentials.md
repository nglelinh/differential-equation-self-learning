---
layout: post
title: "00-04-00 Complex Numbers and Complex Analysis"
chapter: '00'
order: 5
owner: Course Team
lang: en
categories:
- chapter00
lesson_type: required
---

This lesson develops the complex analysis foundations that are essential for solving differential equations and understanding advanced topics in mathematical physics.

> **Teaching Notes**: This lesson takes 2-3 class periods. Key activities: "Find the Error" (10 min), "Residue Hunt" (20 min). Formative assessment: derivation of Euler's formula (quiz), verify holomorphy using CR equations.

---

## Introduction

Complex numbers provide the natural language for describing oscillatory behavior in differential equations. When we solve linear ODEs with constant coefficients, the characteristic equation $$ r^2 + r + 1 = 0 $$ yields complex roots $$ r = -\frac{1}{2} \pm i\frac{\sqrt{3}}{2} $$, and the solutions $$ e^{rt} $$ become exponentials multiplied by sines and cosines. This connection, encapsulated in Euler's formula, is one of the most beautiful formulas in mathematics:

$$ e^{i\theta} = \cos\theta + i\sin\theta $$

Beyond this algebraic convenience, complex analysis offers powerful analytical tools: analytic functions satisfy the Cauchy-Riemann equations, contour integrals vanish for holomorphic functions on simply connected domains, and residues encode the behavior of singularities. These tools become essential when we study series solutions of differential equations, evaluate real integrals via complex contour integration, and understand the spectral theory of differential operators.

---

## 1. Complex Numbers as a Number System

### 1.1 Algebraic Operations

A complex number has the form $$ z = x + iy $$, where $$ x $$ and $$ y $$ are real numbers and $$ i^2 = -1 $$. The real part is $$ \operatorname{Re}(z) = x $$, and the imaginary part is $$ \operatorname{Im}(z) = y $$.

**Operations**:
- **Addition**: $$ (a + ib) + (c + id) = (a + c) + i(b + d) $$
- **Multiplication**: $$ (a + ib)(c + id) = (ac - bd) + i(ad + bc) $$

The complex conjugate of $$ z = x + iy $$ is $$ \bar{z} = x - iy $$. The modulus is $$\lvert z \rvert = \sqrt{z\bar{z}} = \sqrt{x^2 + y^2}$$, satisfying the triangle inequality $$\lvert z + w \rvert \leq \lvert z \rvert + \lvert w \rvert$$.

Division is given by $$\displaystyle \frac{1}{z} = \frac{\bar{z}}{\lvert z \rvert^2}$$ for $$ z \neq 0 $$.

> **Intuitive Analogy**: Complex numbers extend the number line into a number plane. Just as we could not solve $$ x + 1 = 0 $$ without negatives, we cannot solve $$ x^2 + 1 = 0 $$ without imaginaries.

> **Checkpoint**: Can students add and multiply complex numbers? Can they compute modulus and conjugate?

### 1.2 Geometric Interpretation: The Complex Plane

Visualize $$ z = x + iy $$ as the point $$ (x, y) $$ in the complex plane. The argument $$ \arg(z) = \theta $$ is the angle from the positive real axis.

This gives the polar form

$$
z = r(\cos\theta + i\sin\theta), \qquad r = \lvert z \rvert, \qquad \theta = \arg(z).
$$

Multiplication obeys $$\lvert zw \rvert = \lvert z \rvert \lvert w \rvert$$ and $$ \arg(zw) = \arg(z) + \arg(w) \pmod{2\pi} $$.

> **Visual**: Draw the complex plane with axes. Show the point $$ 3 + 2i $$ at $$ (3,2) $$. Show multiplication as rotation plus scaling.

### 1.3 Roots of Unity

The equation $$ z^n = 1 $$ has exactly $$ n $$ solutions, the $$ n $$-th roots of unity:

$$
z_k = e^{2\pi ik/n} = \cos\left(\frac{2\pi k}{n}\right) + i\sin\left(\frac{2\pi k}{n}\right), \qquad k = 0, 1, \ldots, n-1.
$$

These points divide the unit circle into $$ n $$ equal arcs.

**Example**: The cube roots of unity, for $$ n = 3 $$, are $$ z_0 = 1 $$, $$ z_1 = -\frac{1}{2} + i\frac{\sqrt{3}}{2} $$, and $$ z_2 = -\frac{1}{2} - i\frac{\sqrt{3}}{2} $$. They satisfy $$ z_0^3 = z_1^3 = z_2^3 = 1 $$ and $$ z_0 + z_1 + z_2 = 0 $$.

---

## 2. The Exponential Function and Euler's Formula

### 2.1 Euler's Formula

Euler's formula, proved by equating power series, states

$$ e^{i\theta} = \cos\theta + i\sin\theta. $$

**Proof via power series**:

$$
e^{i\theta}
= \sum_{n=0}^{\infty} \frac{(i\theta)^n}{n!}
= \sum_{k=0}^{\infty} \frac{(-1)^k\theta^{2k}}{(2k)!}
+ i\sum_{k=0}^{\infty} \frac{(-1)^k\theta^{2k+1}}{(2k+1)!}
= \cos\theta + i\sin\theta.
$$

> **Intuitive**: Euler's formula is the "Rosetta Stone" connecting exponentials and trigonometry. The identity $$ e^{i\pi} + 1 = 0 $$ connects $$ e $$, $$ i $$, $$ \pi $$, and $$ 1 $$.

> **Common Misconception**: Students often think $$ \sqrt{-1} $$ does not exist. Geometrically, it exists in $$ \mathbb{C} $$ just as negatives exist in $$ \mathbb{R} $$.

### 2.2 Complex Exponentials

For any complex number $$ \lambda = \alpha + i\beta $$,

$$
e^{\lambda t} = e^{(\alpha + i\beta)t} = e^{\alpha t}\bigl(\cos(\beta t) + i\sin(\beta t)\bigr).
$$

The absolute value is $$ \lvert e^{\lambda t} \rvert = e^{\alpha t} $$, and the oscillation frequency is determined by the imaginary part $$ \beta $$.

**Example**: The equation $$ y'' + y = 0 $$ has characteristic equation $$ r^2 + 1 = 0 $$ with roots $$ r = \pm i $$. Its solution can be written as $$y(t) = C_1 e^{it} + C_2 e^{-it} = A\cos t + B\sin t$$, which is pure oscillation with period $$ 2\pi $$.

> **Checkpoint**: Can students prove Euler's formula and use it to simplify expressions?

---

## 3. Analytic Functions

### 3.1 Holomorphy and the Cauchy-Riemann Equations

For $$ f(z) = u(x, y) + iv(x, y) $$, complex differentiability at $$ z $$ requires the Cauchy-Riemann equations:

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y},
\qquad
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.
$$

**Example**: If $$ f(z) = e^z = e^{x+iy} = e^x(\cos y + i\sin y) $$, then $$ u = e^x \cos y $$ and $$ v = e^x \sin y $$. We compute $$ u_x = e^x \cos y = v_y $$ and $$ u_y = -e^x \sin y = -v_x $$. Therefore $$ e^z $$ is holomorphic everywhere, and $$ f'(z) = f(z) $$.

> **Intuitive**: The Cauchy-Riemann equations are the stress test for complex differentiability. Without them, the derivative depends on direction.

> **Common Misconception**: Complex differentiation is not the same as real differentiation. For $$ f(z) = \bar{z} $$, the quotient $$ \bar{h}/h $$ gives different limits along different directions, so no complex derivative exists.

### 3.2 Harmonic Functions

If $$ f = u + iv $$ is holomorphic, then both $$ u $$ and $$ v $$ satisfy Laplace's equation:

$$
\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0,
\qquad
\nabla^2 v = 0.
$$

These are harmonic functions, which explains why complex analysis appears naturally in potential theory, fluid dynamics, and electrostatics.

---

## 4. Complex Integration

### 4.1 Contour Integrals

A contour is a piecewise smooth curve $$ \gamma: [a, b] \to \mathbb{C} $$. Its contour integral is

$$
\int_{\gamma} f(z)\,dz = \int_a^b f(\gamma(t))\gamma'(t)\,dt.
$$

### 4.2 Cauchy's Integral Theorem

If $$ f $$ is holomorphic on a simply connected domain $$ D $$ and continuous on $$ \bar{D} $$, then

$$ \oint_{\gamma} f(z)\,dz = 0. $$

> **Intuitive**: A closed contour contributes no net integral when the integrand has no singularities inside.

> **Common Misconception**: A closed-contour integral is not always zero. If a pole lies inside, the integral can be nonzero.

### 4.3 Cauchy's Integral Formula

If $$ f $$ is holomorphic inside and on a circle centered at $$ z_0 $$, then for any interior point $$ z $$,

$$
f(z) = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(\zeta)}{\zeta - z}\,d\zeta.
$$

Taking derivatives gives

$$
f^{(n)}(z) = \frac{n!}{2\pi i}\oint_{\gamma} \frac{f(\zeta)}{(\zeta - z)^{n+1}}\,d\zeta.
$$

This shows holomorphic functions are infinitely differentiable, a striking phenomenon that does not hold in general real-variable calculus.

---

## 5. The Residue Theorem

### 5.1 Isolated Singularities

An isolated singularity $$ z_0 $$ of $$ f $$ has three types:
- **Removable**: $$ \lim_{z \to z_0} f(z) $$ exists, for example $$ \frac{\sin z}{z} $$ at $$ z = 0 $$.
- **Pole**: $$ \lvert f(z) \rvert \to \infty $$ as $$ z \to z_0 $$.
- **Essential**: Neither of the previous two cases holds, for example $$ e^{1/z} $$ at $$ z = 0 $$.

### 5.2 The Residue

For a pole at $$ z_0 $$, the residue is the coefficient of $$ \frac{1}{z - z_0} $$ in the Laurent expansion:

$$
\operatorname{Res}(f; z_0) = \lim_{z \to z_0} (z - z_0)f(z).
$$

**Example**: For $$ f(z) = \frac{1}{z^2 + 1} $$, the poles at $$ z = \pm i $$ are simple. At $$ z = i $$,

$$
\operatorname{Res}(f; i)
= \lim_{z \to i} \frac{z - i}{z^2 + 1}
= \lim_{z \to i} \frac{z - i}{(z - i)(z + i)}
= \frac{1}{2i}.
$$

### 5.3 The Residue Theorem

Let $$ f $$ be holomorphic on $$ D $$ except for isolated singularities at $$ z_1, \ldots, z_n $$. For any closed contour $$ \gamma $$ around all singularities,

$$
\oint_{\gamma} f(z)\,dz = 2\pi i \sum_{k=1}^{n} \operatorname{Res}(f; z_k).
$$

> **Intuitive**: Residues act like local charges at singularities, and the contour integral measures their total contribution.

---

## 6. Applications to Differential Equations

1. Characteristic equations with complex roots produce oscillatory solutions through Euler's formula.
2. Contour integration is central in inverse Laplace transforms.
3. Frobenius series methods connect naturally with complex analysis.
4. Eigenvalues $$ \lambda = \alpha \pm i\beta $$ encode growth through $$ \alpha $$ and oscillation through $$ \beta $$.

The residues of transfer functions encode impulse responses, linking complex analysis to control theory.

---

## Worked Examples

### Example 1 (Basic): Compute $$ \left(3 + 4i\right)\left(1 - 2i\right) $$

$$
\left(3 + 4i\right)\left(1 - 2i\right) = 3 - 6i + 4i - 8i^2 = 11 - 2i.
$$

### Example 2 (Intermediate): Write $$ z = -1 - i\sqrt{3} $$ in polar form

We have $$ r = \sqrt{1 + 3} = 2 $$ and $$ \theta = \frac{4\pi}{3} $$, so $$ z = 2e^{i4\pi/3} $$. Its cube roots are

$$
2^{1/3} e^{i(4\pi/9 + 2\pi k/3)}, \qquad k = 0, 1, 2.
$$

### Example 3 (Intermediate): Use Euler's formula to simplify $$ \cos^3\theta $$

$$
\cos^3\theta = \left(\frac{e^{i\theta} + e^{-i\theta}}{2}\right)^3 = \frac{\cos(3\theta) + 3\cos\theta}{4}.
$$

### Example 4 (Advanced): Verify that $$ f(z) = e^z $$ is holomorphic and find $$ f'(z) $$

Let $$ u = e^x \cos y $$ and $$ v = e^x \sin y $$. Since $$ u_x = v_y $$ and $$ u_y = -v_x $$, the Cauchy-Riemann equations hold everywhere. Therefore $$ e^z $$ is holomorphic, and $$ f'(z) = e^z $$.

### Example 5 (Advanced): Evaluate $$ \oint_{\lvert z \rvert = 2} \frac{z}{z^2 - 1}\,dz $$

The poles at $$ z = \pm 1 $$ are both inside the contour. Their residues are $$ \frac{1}{2} $$ and $$ \frac{1}{2} $$, so the integral is

$$
2\pi i \left(\frac{1}{2} + \frac{1}{2}\right) = 2\pi i.
$$

---

## Conceptual Questions

1. Why do we need complex numbers? They provide solutions to polynomial equations with no real roots, such as $$ x^2 + 1 = 0 $$, and they reveal oscillatory structure in differential equations.
2. Why are the Cauchy-Riemann equations necessary? They ensure the complex derivative exists in every direction.
3. Why does Cauchy's theorem hold? Holomorphy imposes enough structure to force the closed-contour integral to vanish when no singularities are enclosed.

---

## Application Problems

1. Solve $$ y'' + 4y = 0 $$ using complex exponentials and rewrite the answer in real form.
2. Evaluate $$ \int_0^{2\pi} \frac{d\theta}{5 + 3\cos\theta} $$ using complex integration.
3. For $$ \mathbf{x}' = A\mathbf{x} $$ with eigenvalues $$ \lambda = \alpha \pm i\beta $$, determine stability from the sign of $$ \alpha $$.

---

## Interactive Activities

### Activity 1: "Find the Error" (10 min)

Present common mistakes. Students identify and correct them:

- Error: $$ (i)^2 = i^2 $$. Correction: $$ (i)^2 = -1 $$.
- Error: $$ \arg(zw) = \arg(z)\arg(w) $$. Correction: $$ \arg(zw) = \arg(z) + \arg(w) $$.
- Error: $$ \oint \frac{dz}{z} = 0 $$. Correction: $$ \oint \frac{dz}{z} = 2\pi i $$.

### Activity 2: "Residue Hunt" (20 min)

Groups compute residues and contour integrals:

- Group 1: $$ \frac{z}{z^2 - 4} $$ on the circle $$ \lvert z \rvert = 3 $$.
- Group 2: $$ \frac{1}{z^2 + 1} $$ on the circle $$ \lvert z \rvert = 2 $$.

---

## Summary

- Euler's formula: $$ e^{i\theta} = \cos\theta + i\sin\theta $$. Remember it as the bridge between exponentials and trigonometry.
- Complex exponential: $$e^{(\alpha + i\beta)t} = e^{\alpha t}(\cos(\beta t) + i\sin(\beta t))$$. The real part controls growth; the imaginary part controls oscillation.
- Cauchy-Riemann equations: $$ u_x = v_y $$ and $$ u_y = -v_x $$. They are the test for holomorphy.
- Cauchy's theorem: $$ \oint f(z)\,dz = 0 $$ for holomorphic integrands on suitable domains.
- Residue theorem: $$ \oint f(z)\,dz = 2\pi i \sum \operatorname{Res} $$. A contour integral becomes a sum over poles.

> **One-Liner**: Complex analysis extends real calculus to two dimensions, where Euler's formula turns exponentials into spirals, the Cauchy-Riemann equations enforce a two-dimensional derivative, and residues turn difficult integrals into pole counting.

---

## References

- Saff & Snider — *Fundamentals of Complex Analysis*
- Churchill & Brown — *Complex Variables and Applications*
- Boyce & DiPrima, Section 3.3 (ODE context)
- Zill, Appendix (computational background)

---

*This lesson provides the foundation for understanding complex analysis in differential equations. Next lessons on metric spaces, normed spaces, and inner product spaces extend these ideas to infinite-dimensional settings.*
