---
layout: post
title: "07-03 Sturm-Liouville Theory"
chapter: '07'
order: 3
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: required
---

At first glance, sine series, Legendre polynomials, Bessel functions, and Hermite polynomials look like completely unrelated mathematical species born in different centuries from different physical problems. Then, in 1836–1837, Jacques Charles François Sturm and Joseph Liouville proved one of the great unifying theorems of analysis: every one of them is an eigenfunction of a single self-adjoint differential operator $$ L[y] = -\frac{d}{dx}\bigl(p(x) y'\bigr) + q(x) y = \lambda w(x) y $$.

Just as the Spectral Theorem for symmetric matrices guarantees real eigenvalues and an orthogonal eigenbasis in $$ \mathbb{R}^n $$, Sturm–Liouville theory guarantees real eigenvalues, weighted orthogonality, and completeness in the infinite-dimensional Hilbert space $$ L^2_w([a, b]) $$.

## Background Knowledge Map: The Sturm–Liouville Spectral Machine

1. **Conversion to Self-Adjoint Form (Integrating Factor $$ \mu(x) $$):** Any second-order linear ODE $$ a_2(x) y'' + a_1(x) y' + (a_0(x) + \lambda \rho(x)) y = 0 $$ can be converted into $$ \bigl(p(x) y'\bigr)' + \bigl(q(x) + \lambda w(x)\bigr) y = 0 $$ by multiplying through by $$ \mu(x) = \frac{1}{a_2(x)} \exp\!\left(\int \frac{a_1(x)}{a_2(x)}\,dx\right) $$. This immediately reveals the hidden weight function $$ w(x) $$ under which eigenfunctions are orthogonal!
2. **Lagrange's Identity & Green's Formula (Why Self-Adjointness Works):** Integrating by parts twice yields $$ \int_a^b (u L[v] - v L[u])\,dx = -\bigl[p(x)(u v' - v u')\bigr]_a^b $$. Under separated regular BCs (or singular vanishing of $$ p $$ at endpoints), the boundary bracket vanishes identically—making $$ L $$ symmetric in $$ L^2_w([a, b]) $$.
3. **The Four Spectral Guarantees (Regular S–L Theorem):** For $$ p(x) > 0, w(x) > 0 $$ on $$ [a, b] $$: (i) all eigenvalues $$ \lambda_n $$ are real and simple; (ii) $$ \lambda_1 < \lambda_2 < \cdots \to \infty $$; (iii) eigenfunctions for $$ \lambda_m \neq \lambda_n $$ satisfy $$ \int_a^b y_m(x) y_n(x) w(x)\,dx = 0 $$; (iv) $$ y_n $$ has exactly $$ n - 1 $$ zeros inside $$ (a, b) $$ (Sturm oscillation).
4. **Completeness in $$ L^2_w([a, b]) $$:** The normalized eigenfunctions form a complete orthonormal basis of $$ L^2_w([a, b]) $$, legitimizing every eigenfunction expansion in PDEs and quantum mechanics.

### Step-by-Step Worked Example (Read Slowly): Converting Cauchy–Euler to Sturm–Liouville Form and Finding Its Exact Weight

**Problem:** Convert the Cauchy–Euler eigenvalue problem $$ x^2 y'' + x y' + \lambda y = 0 $$ on $$ [1, e] $$ with $$ y(1) = y(e) = 0 $$ into Sturm–Liouville form, identify $$ p(x), q(x), w(x) $$, find the eigenvalues/eigenfunctions, and explicitly verify weighted orthogonality between $$ y_1 $$ and $$ y_2 $$.

1. **Compute the integrating factor $$ \mu(x) $$:**
   Here $$ a_2(x) = x^2 $$, $$ a_1(x) = x $$, so
   $$ \mu(x) = \frac{1}{x^2} \exp\!\left(\int \frac{x}{x^2}\,dx\right) = \frac{1}{x^2} \cdot x = \frac{1}{x}. $$
2. **Multiply the ODE by $$ \frac{1}{x} $$:**
   $$ x y'' + y' + \frac{\lambda}{x} y = 0 \implies \frac{d}{dx}\bigl(x y'\bigr) + \lambda \frac{1}{x} y = 0. $$
   Thus $$ p(x) = x > 0 $$, $$ q(x) = 0 $$, and the orthogonality weight is $$ w(x) = \frac{1}{x} > 0 $$ on $$ [1, e] $$!
3. **Solve for the eigenvalues and eigenfunctions:**
   Substitute $$ t = \ln x \in [0, 1] $$, transforming the ODE to $$ \frac{d^2 y}{dt^2} + \lambda y = 0 $$ with $$ y(0) = y(1) = 0 $$. This immediately gives
   $$ \lambda_n = (n\pi)^2, \qquad y_n(x) = \sin(n\pi \ln x), \qquad n = 1, 2, 3, \dots $$
4. **Verify weighted orthogonality directly for $$ y_1 $$ and $$ y_2 $$:**
   $$ \int_1^e y_1(x) y_2(x) w(x)\,dx = \int_1^e \sin(\pi \ln x)\sin(2\pi \ln x)\,\frac{dx}{x}. $$
   With $$ t = \ln x $$ ($$ dt = dx/x $$), this becomes
   $$ \int_0^1 \sin(\pi t)\sin(2\pi t)\,dt = \frac{1}{2}\int_0^1 \bigl[\cos(\pi t) - \cos(3\pi t)\bigr]\,dt = \frac{1}{2}\left[\frac{\sin(\pi t)}{\pi} - \frac{\sin(3\pi t)}{3\pi}\right]_0^1 = 0. $$
   Without the Sturm–Liouville weight $$ w(x) = 1/x $$, $$ \sin(\pi \ln x) $$ and $$ \sin(2\pi \ln x) $$ would *not* be orthogonal—the weight is the exact key!

## Learning Objectives

This lesson develops Sturm-Liouville theory as the structured framework behind differential eigenvalue problems. Students should understand the standard form, the role of self-adjointness, and the resulting properties of real eigenvalues and orthogonal eigenfunctions.

## Prerequisites

Students should know model eigenvalue problems, integration by parts, and some linear algebra intuition about orthogonality and real spectra.

## Introduction

![Self-adjoint structure of Sturm-Liouville problems]({{ site.imgurl }}/chapter_img/chapter07/03_sturm_liouville_theory.svg)

The fixed-string problem is only the beginning. Many important boundary value problems share a deeper common structure, and Sturm-Liouville theory is the framework that captures it. Once the problem is written in self-adjoint form, a remarkable collection of properties follows: real eigenvalues, orthogonality of eigenfunctions, and a clean mode expansion theory.

This lesson is important because it explains why the eigenfunction machinery works so well. The good spectral behavior is not an accident. It is a consequence of the operator structure and the boundary conditions.

## Concept in Three Ways

### Intuitive View

Sturm-Liouville theory identifies the class of boundary value problems whose modes behave as cleanly as possible. The theory tells us when mode shapes fit together without interfering and when the spectral data stay real and physically meaningful.

### Visual View

Different eigenfunctions oscillate in different patterns, but they are orthogonal with respect to a weight. In the weighted inner-product picture, they point in independent directions in function space.

### Formal View

A Sturm-Liouville problem is typically written as
$$ -(p(x)y')'+q(x)y=\lambda w(x)y, $$
with suitable boundary conditions and weight $$ w(x)>0 $$. Under the self-adjoint setting, the eigenvalues are real and eigenfunctions corresponding to different eigenvalues are orthogonal with respect to
$$ \langle f,g\rangle_w=\int_a^b f(x)g(x)w(x)\,dx. $$

## Common Misconceptions

- "Sturm-Liouville theory is just another way to write the same ODE." Wrong. The form matters because it reveals self-adjointness.
- "Orthogonality is a lucky coincidence in the sine example." Wrong. It is a structural consequence of the theory.
- "The weight function is a technical nuisance." Wrong. It determines the correct inner product.
- "Real eigenvalues are obvious." Not without the self-adjoint framework.

## Suggested Learning Path

### Step 1: Learn the Standard Form

Students should recognize when a problem has Sturm-Liouville structure.

### Step 2: Use Integration by Parts

This is the algebraic heart of the self-adjoint property.

### Step 3: Prove Orthogonality

The classical proof is short and highly instructive.

### Step 4: Interpret the Weight

The weight is part of the geometry of function space.

### Checkpoints

- Can students identify the coefficient functions $$ p,q,w $$?
- Can students explain the meaning of weighted orthogonality?
- Do students know why the self-adjoint form is the source of the spectral properties?

## Worked Examples

### Example 1: The Standard String Problem

The problem
$$ y''+\lambda y=0,\qquad y(0)=y(L)=0 $$
can be rewritten as
$$ -(1\cdot y')'=\lambda (1)\,y. $$
Here
$$ p(x)=1,\qquad q(x)=0,\qquad w(x)=1. $$
So the fixed-string problem is a Sturm-Liouville problem.

### Example 2: Orthogonality Proof

Suppose
$$ Ly=\lambda_m w y,\qquad Lz=\lambda_n w z. $$
Multiply the first equation by $$ z $$ and the second by $$ y $$, subtract, and integrate. The boundary terms vanish in the self-adjoint setting, leaving
$$ (\lambda_m-\lambda_n)\int_a^b y(x)z(x)w(x)\,dx=0. $$
If $$ \lambda_m\ne \lambda_n $$, then
$$ \int_a^b y(x)z(x)w(x)\,dx=0. $$

## Conceptual Questions

1. Why is the self-adjoint form more than a cosmetic rewriting?
2. Why must the weight be included in the inner product?
3. How does orthogonality in function space mirror orthogonality of vectors?

## Application Problems

1. In vibration theory, why is it useful that different modes are orthogonal?
2. In PDE separation of variables, why are real eigenvalues essential?
3. In heterogeneous media, how does the weight function reflect physical nonuniformity?

## Interactive Teaching Strategies

- Ask students to rewrite several differential equations into Sturm-Liouville form.
- Walk through the orthogonality proof line by line and highlight where boundary conditions matter.
- Compare ordinary Euclidean dot products with weighted function inner products.
- Use the fixed-string problem as the recurring concrete anchor.

## Differentiation

### Support for Struggling Students

Students who need support should focus first on identifying the standard form and understanding the classical orthogonality proof.

### Challenge for Advanced Students

Advanced students can connect the topic to self-adjoint operators on Hilbert spaces and the beginnings of the spectral theorem.

## Summary

Sturm-Liouville theory is the structural backbone of boundary-value spectral theory. Its self-adjoint form explains why the eigenvalues are real and why the eigenfunctions are orthogonal building blocks.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Nonuniform string vibration
- Problem: A string with varying density leads to a weighted eigenvalue problem.
- Model:
$$ -(p(x)y')'+q(x)y=\lambda w(x)y. $$
- Assumptions and limitations: Linear, regular boundary conditions, positive weight.
- Interpretation: Sturm-Liouville theory explains why the eigenvalues are real and the eigenfunctions are orthogonal.

#### Heat or diffusion in nonuniform media
- Problem: Separation of variables in heterogeneous materials leads naturally to self-adjoint differential operators.
- Model:
$$
\frac{d}{dx}\left(p(x)\frac{dy}{dx}\right)+(\lambda w(x)-q(x))y=0.
$$
- Assumptions and limitations: Appropriate regularity and boundary conditions are required.
- Interpretation: Self-adjointness is the deep reason the mode structure behaves so well.

### 2. Additional Intuition and Connections

Sturm-Liouville theory is where boundary value problems become spectral theory. Self-adjointness is the source of real eigenvalues and orthogonality. A common pitfall is to memorize the theorems as a list of properties rather than seeing that they all come from integration by parts and the boundary conditions.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
y1 = np.sin(np.pi * x)
y2 = np.sin(2 * np.pi * x)

plt.plot(x, y1, label="phi1")
plt.plot(x, y2, label="phi2")
plt.fill_between(x, y1 * y2, alpha=0.3, color="orange", label="phi1 * phi2")
plt.xlabel("x")
plt.ylabel("value")
plt.title("Orthogonality of eigenfunctions")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Sturm Liouville orthogonality visualization
- search: self adjoint operator boundary value problem
- search: weighted orthogonality eigenfunctions

### 5. Worked Example

For the simple problem
$$ y''+\lambda y=0,\qquad y(0)=y(L)=0, $$
the eigenfunctions are
$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right). $$
They satisfy
$$ \int_0^L \phi_m(x)\phi_n(x)\,dx=0\qquad (m\ne n). $$
This is the model example of orthogonality in Sturm-Liouville theory.

### 6. Difficulty Layering

**Undergraduate level.** Understand the standard form, real spectrum, and orthogonality.

**Graduate level.** Discuss self-adjoint operators, weighted Hilbert spaces, and the spectral theorem viewpoint.

![Sturm-Liouville theory]({{ site.imgurl }}/chapter_img/chapter07/03_sturm_liouville_theory.svg)

## Video tham khảo

- xem trước: [Sturm-Liouville Theorem and Proof](https://www.youtube.com/watch?v=_F0ck1JncLE) — Faculty of Khan, English. Self-adjoint form, real eigenvalues, and orthogonal eigenfunctions.
- [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, English. A full lecture developing the theory from the differential expression.
- [Sturm-Liouville Theory](https://www.youtube.com/watch?v=12d15vI52b8) — Nathan Kutz, English. Nathan Kutz's computational and theoretical overview.

## References

- Boyce & DiPrima, Chapters 10-11: standard development of Sturm-Liouville theory.
- Haberman, Chapter 5: helpful application-based perspective.
