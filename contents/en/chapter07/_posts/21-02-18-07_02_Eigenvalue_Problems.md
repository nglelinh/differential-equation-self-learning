---
layout: post
title: "07-02 Eigenvalue Problems"
chapter: '07'
order: 2
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: required
---

Push down slowly on the top of a thin plastic ruler. At first it stays perfectly straight—the trivial equilibrium $$ y \equiv 0 $$. Keep increasing the compressive load $$ P $$, and at a razor-sharp critical force $$ P_{\text{crit}} $$, the ruler suddenly snaps sideways into a smooth arch. Leonhard Euler discovered in 1744 that this buckling instability is governed by a boundary value problem $$ y'' + \lambda y = 0 $$ where *only discrete special values* of $$ \lambda $$ allow a nonzero solution to fit between the endpoints.

Those special values are the **eigenvalues**, and the corresponding arches are the **eigenfunctions**. Just as matrix eigenvalues diagonalize finite-dimensional systems, differential eigenvalues unlock the natural resonant frequencies, buckling loads, and quantum energy levels of continuous physical systems.

## Key ideas: Differential Eigenvalue Problems

1. **Matrix vs. Differential Operator Analogy (Functional Analysis):** Writing $$ L[y] = -y'' $$, the problem $$ L[y] = \lambda y $$ with homogeneous BCs is the infinite-dimensional analogue of $$ A\mathbf{v} = \lambda \mathbf{v} $$. Crucially, the *boundary conditions are part of the operator's domain*: changing Dirichlet to Neumann changes the spectrum completely.
2. **Exhaustive Sign Analysis ($$ \lambda < 0, \lambda = 0, \lambda > 0 $$):** Because the characteristic roots of $$ y'' + \lambda y = 0 $$ change character across $$ \lambda = 0 $$ (hyperbolic exponentials for $$ \lambda < 0 $$, linear polynomials for $$ \lambda = 0 $$, trigonometric oscillations for $$ \lambda > 0 $$), every eigenvalue problem must be checked cleanly across all three regimes.
3. **Rayleigh Quotient Sign Check (Energy Intuition):** Multiplying $$ -y'' = \lambda y $$ by $$ y $$ and integrating by parts gives $$ \lambda = \frac{-[y y']_a^b + \int_a^b (y')^2\,dx}{\int_a^b y^2\,dx} $$. For Dirichlet or Neumann BCs, the boundary term vanishes, proving immediately that $$ \lambda \ge 0 $$ (and $$ \lambda > 0 $$ for Dirichlet)—zero guesswork!
4. **Discrete Spectrum and Nodal Counting:** As $$ n $$ increases, eigenvalues grow quadratically ($$ \lambda_n \sim (n\pi/L)^2 $$) and the $$ n $$-th eigenfunction has increasingly many interior zeros, forming the natural harmonic ladder of the domain.

### Worked example: Complete Spectrum of the Mixed Dirichlet–Neumann Problem

**Problem:** Find all eigenvalues $$ \lambda $$ and eigenfunctions $$ y(x) $$ of $$ y'' + \lambda y = 0 $$ on $$ [0, L] $$ subject to $$ y(0) = 0 $$ and $$ y'(L) = 0 $$, checking all three regimes $$ \lambda < 0 $$, $$ \lambda = 0 $$, and $$ \lambda > 0 $$.

1. **Case 1 ($$ \lambda = -\mu^2 < 0 $$ with $$ \mu > 0 $$):**
   General solution: $$ y(x) = c_1 \cosh(\mu x) + c_2 \sinh(\mu x) $$.
   - $$ y(0) = c_1 = 0 \implies y(x) = c_2 \sinh(\mu x) $$.
   - $$ y'(L) = c_2 \mu \cosh(\mu L) = 0 $$. Since $$ \mu > 0 $$ and $$ \cosh(\mu L) \ge 1 > 0 $$, we must have $$ c_2 = 0 $$.
   Thus **no negative eigenvalues** exist.
2. **Case 2 ($$ \lambda = 0 $$):**
   General solution: $$ y(x) = c_1 + c_2 x $$.
   - $$ y(0) = c_1 = 0 $$.
   - $$ y'(L) = c_2 = 0 $$.
   Only the trivial solution exists, so **$$ \lambda = 0 $$ is not an eigenvalue**.
3. **Case 3 ($$ \lambda = \mu^2 > 0 $$ with $$ \mu > 0 $$):**
   General solution: $$ y(x) = c_1 \cos(\mu x) + c_2 \sin(\mu x) $$.
   - $$ y(0) = c_1 = 0 \implies y(x) = c_2 \sin(\mu x) $$.
   - $$ y'(L) = c_2 \mu \cos(\mu L) = 0 $$. For a nontrivial solution ($$ c_2 \neq 0 $$), we require
     $$ \cos(\mu L) = 0 \implies \mu_n L = \left(n - \frac{1}{2}\right)\pi = \frac{(2n-1)\pi}{2}, \qquad n = 1, 2, 3, \dots $$
4. **State the spectrum and verify $$ n = 1 $$:**
   $$ \lambda_n = \left(\frac{(2n-1)\pi}{2L}\right)^2, \qquad y_n(x) = \sin\!\left(\frac{(2n-1)\pi x}{2L}\right), \qquad n = 1, 2, 3, \dots $$
   Check $$ n = 1 $$: $$ y_1(x) = \sin\!\left(\frac{\pi x}{2L}\right) $$ satisfies $$ y_1(0) = 0 $$, $$ y_1'(L) = \frac{\pi}{2L}\cos\!\left(\frac{\pi}{2}\right) = 0 $$, and $$ y_1'' = -\left(\frac{\pi}{2L}\right)^2 y_1 $$. Notice its fundamental frequency is *half* that of a Dirichlet–Dirichlet string—matching a clarinet pipe closed at one end!

## Learning Objectives

This lesson introduces differential-equation eigenvalue problems as the bridge from ordinary BVPs to spectral theory. Students should learn what eigenvalues and eigenfunctions are in this setting, why only special parameter values permit nontrivial solutions, and how these solutions describe natural modes of a physical system.

## Prerequisites

Students should know two-point BVPs, second-order linear ODEs, and matrix eigenvalues from linear algebra. The strongest intuition comes from constant-coefficient model problems.

## Introduction

![Sturm-Liouville eigenvalue problem]({{ site.imgurl }}/chapter_img/chapter07/02_eigenvalue_problems.svg)

In an ordinary BVP we usually ask whether a solution exists for given forcing and given boundary conditions. In an eigenvalue problem, a parameter enters the equation and the question changes: for which parameter values does a nontrivial solution exist? This is the beginning of spectral theory.

The idea is closely parallel to matrix algebra. For a matrix $$ A $$, only special numbers $$ \lambda $$ allow a nonzero vector to satisfy
$$ A\mathbf{v}=\lambda \mathbf{v}. $$
For a differential operator, only special parameter values allow a nonzero function to satisfy the boundary conditions. Those values are eigenvalues, and the corresponding functions are eigenfunctions.

## Concept in Three Ways

### Intuitive View

Think of a string fixed at both ends. Not every frequency produces a natural standing wave. Only special frequencies fit perfectly with the boundary conditions. Those special frequencies are eigenvalues, and the corresponding standing-wave shapes are eigenfunctions.

### Visual View

The first mode has one arch, the next has two, then three, and so on. Each mode has its own number of nodes and its own characteristic frequency. The eigenvalue labels the mode and the eigenfunction shows its shape.

### Formal View

A typical differential eigenvalue problem has the form
$$ Ly=\lambda w(x)y, $$
with suitable boundary conditions. Here $$ L $$ is a differential operator and $$ w(x)>0 $$ is a weight. We seek values of $$ \lambda $$ such that there exists
$$ y\not\equiv 0 $$
satisfying both the differential equation and the boundary conditions.

## Common Misconceptions

- "Any parameter value that gives a solution counts as an eigenvalue." Not enough. The solution must be nontrivial.
- "Eigenfunctions are unimportant because they differ only by scaling." Wrong. Their shapes represent physically meaningful modes.
- "Differential eigenvalues are unrelated to matrix eigenvalues." Wrong. It is the same organizing idea in an infinite-dimensional setting.
- "The parameter is just another constant to plug in." Wrong. In this lesson the parameter is the unknown to be selected.

## Suggested Learning Path

### Step 1: Recall Matrix Eigenvalues

This analogy makes the new setting far less mysterious.

### Step 2: Study a Model BVP with a Parameter

The fixed-string problem is the standard first example.

### Step 3: Separate Cases

Students should examine the cases $$ \lambda<0 $$, $$ \lambda=0 $$, and $$ \lambda>0 $$.

### Step 4: Interpret the Result Physically

The main point is not only the formula for $$ \lambda_n $$, but the meaning of the corresponding modes.

### Checkpoints

- Can students explain why the trivial solution is excluded?
- Can students derive the sequence of eigenvalues in the model problem?
- Do students see the connection between eigenfunctions and natural vibration modes?

## Worked Examples

### Example 1: Fixed String

Consider
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
If $$ \lambda<0 $$ or $$ \lambda=0 $$, only the trivial solution exists. If $$ \lambda=\mu^2>0 $$, then
$$ y=A\cos(\mu x)+B\sin(\mu x). $$
The first boundary condition gives $$ A=0 $$, and the second gives
$$ B\sin(\mu L)=0. $$
To obtain a nontrivial solution we need
$$ \sin(\mu L)=0, $$
so
$$ \mu=\frac{n\pi}{L}. $$
Hence
$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad
y_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$

### Example 2: Physical Meaning

The eigenvalue $$ \lambda_n $$ determines the mode frequency, while the eigenfunction $$ y_n $$ gives the spatial shape of that mode. This is the simplest full illustration of the eigenvalue idea in differential equations.

## Conceptual Questions

1. Why must the trivial solution be excluded from the definition?
2. Why do eigenvalues appear as a discrete sequence in the fixed-string example?
3. What makes eigenfunctions physically meaningful rather than merely symbolic?

## Application Problems

1. In a quantum box, how are energy levels related to an eigenvalue problem?
2. In structural vibration, why do only special frequencies persist as natural modes?
3. How does changing the boundary conditions change the allowable modes?

## Interactive Teaching Strategies

- Ask students to compare the matrix and differential-operator eigenvalue problems side by side.
- Have them draw the first few eigenfunctions for the string model.
- Separate the three sign cases for $$ \lambda $$ in small groups and compare conclusions.
- Reinforce the physical language of frequency and mode shape.

## Differentiation

### Support for Struggling Students

Students who need support should repeatedly solve the fixed-end string model until the logic of the sign cases and boundary matching becomes automatic.

### Challenge for Advanced Students

Advanced students can ask how the sequence of eigenvalues changes when the boundary conditions change from Dirichlet to Neumann or mixed type.

## Summary

Eigenvalue problems are the spectral version of boundary value problems. They select special parameter values that support nontrivial mode shapes, and those modes become the building blocks of later theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Natural vibration of a string
- Problem: A fixed string vibrates only at certain special frequencies.
- Model:
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
- Assumptions and limitations: Thin string, uniform tension, small oscillations.
- Interpretation: Only
$$ \lambda_n=\left(\frac{n\pi}{L}\right)^2 $$
produce nontrivial modes.

#### Quantum bound states in a potential well
- Problem: A particle in a one-dimensional box has discrete stationary states.
- Model: After nondimensionalization, the boundary problem takes the form
$$ y''+\lambda y=0 $$
with vanishing boundary conditions.
- Assumptions and limitations: The infinite-well model is idealized.
- Interpretation: Eigenvalues are energy levels and eigenfunctions are stationary states.

### 2. Additional Intuition and Connections

An ODE eigenvalue problem is the infinite-dimensional analogue of the matrix eigenvalue problem. The key point is that we are not solving for every parameter value, but for special parameter values that allow nontrivial solutions. A common pitfall is to forget to exclude the trivial solution or to miss the physical meaning of the eigenfunctions as modes.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 400)

for n in range(1, 4):
    y = np.sin(n * np.pi * x / L)
    plt.plot(x, y, label=f"n={n}")

plt.xlabel("x")
plt.ylabel("mode shape")
plt.title("First three eigenfunctions for a fixed string")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: vibrating string eigenmodes boundary value problem
- search: eigenvalue problem ODE mode shapes
- search: quantum infinite well eigenfunctions

### 5. Worked Example

Solve
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
If $$ \lambda=\mu^2>0 $$, then
$$ y=A\cos(\mu x)+B\sin(\mu x). $$
The boundary condition at $$ x=0 $$ gives $$ A=0 $$, while the condition at $$ x=L $$ gives
$$ B\sin(\mu L)=0. $$
For a nontrivial solution we need
$$ \sin(\mu L)=0, $$
so
$$ \mu=\frac{n\pi}{L}. $$

### 6. Difficulty Layering

**Undergraduate level.** Solve the model problem and interpret eigenvalues and eigenfunctions as frequencies and mode shapes.

**Graduate level.** Connect the problem to spectral theory of self-adjoint operators on function spaces.

![Eigenvalue problems]({{ site.imgurl }}/chapter_img/chapter07/02_eigenvalue_problems.svg)

## Video tham khảo

- xem trước: [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, English. Eigenvalues and eigenfunctions of a differential operator with boundary conditions.
- [Sturm-Liouville Theorem and Proof](https://www.youtube.com/watch?v=_F0ck1JncLE) — Faculty of Khan, English. Faculty of Khan states and proves the Sturm-Liouville theorem.
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) — 3Blue1Brown, English. The finite-dimensional eigenvalue picture this differential problem extends.

## References

- Boyce & DiPrima, Chapter 10: standard model eigenvalue problems.
- Haberman, Chapter 5: strong physical interpretation of natural modes.
