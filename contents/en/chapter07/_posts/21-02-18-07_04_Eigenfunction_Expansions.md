---
layout: post
title: "07-04 Eigenfunction Expansions"
chapter: '07'
order: 4
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: required
---

## Learning Objectives

This lesson helps students understand eigenfunction expansions as generalized Fourier series, compute expansion coefficients in simple settings, and interpret arbitrary states as superpositions of boundary-adapted modes.

## Prerequisites

Students should know orthogonality, basic Fourier series, and the eigenvalue problems of the previous lessons.

## Introduction

![Eigenfunction expansion as generalized Fourier analysis]({{ site.imgurl }}/chapter_img/chapter07/04_eigenfunction_expansions.svg)

Once we have a family of orthogonal eigenfunctions, we can do more than classify modes. We can expand general functions in terms of those modes. This is the natural extension of Fourier series from sine and cosine to operator-adapted bases.

This idea is central because it turns many PDEs into decoupled scalar equations for coefficients. The initial or boundary data are projected onto eigenmodes, and each mode then evolves independently according to its own parameter.

## Concept in Three Ways

### Intuitive View

An arbitrary shape may look complicated, but if the problem has a natural mode basis, we can break the shape into simple building blocks. Each building block is an eigenfunction adapted to the geometry and boundary conditions.

### Visual View

A function expansion looks like a sum of waves or shapes whose amplitudes are chosen to match the target profile. In the correct weighted inner product, the coefficients measure how much of each mode is present.

### Formal View

Given orthogonal eigenfunctions $$ \{\phi_n\} $$, we write
$$ f(x)=\sum_{n=1}^{\infty} c_n \phi_n(x), $$
with coefficients
$$
c_n=\frac{\langle f,\phi_n\rangle_w}{\langle \phi_n,\phi_n\rangle_w}.
$$
This is the generalized Fourier formula.

## Common Misconceptions

- "Eigenfunction expansion is just ordinary Fourier series with different notation." It is broader than that, although Fourier series are a special case.
- "The coefficients are chosen arbitrarily." Wrong. Orthogonality determines them.
- "The basis always consists of sines and cosines." Wrong. The basis depends on the operator and the boundary conditions.
- "Formal series expansion automatically means pointwise convergence everywhere." Not necessarily; convergence depends on the function space and regularity.

## Suggested Learning Path

### Step 1: Revisit Fourier Series

Students should see the new theory as a generalization, not a replacement.

### Step 2: Use Orthogonality to Derive the Coefficients

This is the essential computational step.

### Step 3: Work a Simple Expansion

The fixed-string sine basis is the most transparent first example.

### Step 4: Connect to PDE Solutions

Students should understand why expansion is the natural output of separation of variables.

### Checkpoints

- Can students derive the coefficient formula from orthogonality?
- Can students explain why the basis depends on the boundary conditions?
- Do students understand that convergence questions are subtle?

## Worked Examples

### Example 1: Fourier Sine Expansion

On $$ [0,L] $$ with Dirichlet boundary conditions,
$$
f(x)=\sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right),
$$
where
$$
c_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$
This is the classical prototype of an eigenfunction expansion.

### Example 2: Why the Weight Matters

In a general Sturm-Liouville problem, the orthogonality relation includes the weight function:
$$
\int_a^b \phi_m(x)\phi_n(x)w(x)\,dx=0,\qquad m\ne n.
$$
So the correct coefficients must use the same weighted inner product.

## Conceptual Questions

1. Why are eigenfunction expansions the natural analogue of Fourier series?
2. How does orthogonality determine the coefficients?
3. Why must the boundary conditions be built into the basis?

## Application Problems

1. In the heat equation, why is an eigenfunction expansion the natural way to encode initial temperature?
2. In wave motion, what physical meaning do the coefficients of an expansion carry?
3. Why is a geometry-adapted mode basis more useful than an arbitrary basis?

## Interactive Teaching Strategies

- Compare a Fourier sine expansion with a generalized eigenfunction expansion term by term.
- Have students compute the first few coefficients for a simple profile such as $$ x(1-x) $$.
- Emphasize the projection viewpoint: coefficient equals overlap with a mode.
- Connect every expansion to a later PDE application.

## Differentiation

### Support for Struggling Students

Students who need support should begin with the sine-series case and master the coefficient formula there before moving to weighted problems.

### Challenge for Advanced Students

Advanced students can explore convergence in $$ L^2 $$ versus pointwise convergence and the meaning of completeness.

## Summary

Eigenfunction expansions generalize Fourier series to the mode bases selected by boundary-value operators. They are one of the main tools that make separation of variables work.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Initial temperature profile in a rod
- Problem: An arbitrary starting temperature can be decomposed into spatial eigenmodes.
- Model:
$$ u(x,0)=\sum_{n=1}^{\infty} c_n \phi_n(x). $$
- Assumptions and limitations: We need a complete eigenfunction family and an appropriate function space.
- Interpretation: Eigenfunction expansion is generalized Fourier analysis adapted to the operator and boundary conditions.

#### Initial shape of a vibrating string
- Problem: A string's initial displacement must be decomposed into standing-wave modes.
- Model:
$$
f(x)=\sum_{n=1}^{\infty} c_n \phi_n(x),\qquad
c_n=\frac{\langle f,\phi_n\rangle_w}{\langle \phi_n,\phi_n\rangle_w}.
$$
- Assumptions and limitations: Convergence behavior depends on regularity of the function and the problem setting.
- Interpretation: A complicated initial state becomes a superposition of simple modes.

### 2. Additional Intuition and Connections

Eigenfunction expansions are the natural generalization of Fourier series. The basis is no longer automatically sine and cosine, but the operator's own eigenmodes. A common misconception is that this is merely a formal trick. In reality, it is the standard language for solving many linear PDEs by separation of variables.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
f = x * (1 - x)

series = np.zeros_like(x)
for n in range(1, 6):
    cn = 2 * np.trapz(f * np.sin(n * np.pi * x), x)
    series += cn * np.sin(n * np.pi * x)

plt.plot(x, f, label="f(x)", color="black")
plt.plot(x, series, "--", label="5-mode expansion")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Eigenfunction expansion on [0,1]")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: eigenfunction expansion generalized Fourier series
- search: vibrating string Fourier sine expansion
- search: Sturm Liouville completeness visualization

### 5. Worked Example

On $$ [0,L] $$ with Dirichlet boundary conditions,
$$
f(x)=\sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right),
$$
where
$$
c_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$
This is the classical example of an eigenfunction expansion and the template for the weighted general case.

### 6. Difficulty Layering

**Undergraduate level.** Compute coefficients and interpret the expansion as a mode decomposition.

**Graduate level.** Discuss completeness, convergence in $$ L^2_w $$, and the spectral resolution viewpoint.

![Eigenfunction expansions]({{ site.imgurl }}/chapter_img/chapter07/04_eigenfunction_expansions.svg)

## References

- Boyce & DiPrima, Chapter 11: classical eigenfunction expansion methods.
- Haberman, Chapter 5: strong connection to PDE applications.
