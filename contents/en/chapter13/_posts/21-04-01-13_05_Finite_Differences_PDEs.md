---
layout: post
title: "13-05 Finite Differences for PDEs"
chapter: '13'
order: 5
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: required
---

> **Storytelling Hook:** Replace a continuous metal rod or 2D plate with a discrete lattice of evenly spaced nodes, and suddenly every partial derivative becomes a simple weighted combination of neighboring node values. The infinite-dimensional PDE collapses into a sparse linear system $A\mathbf{U} = \mathbf{b}$ that a computer can solve in microseconds.

## Learning Objectives

This lesson introduces finite-difference discretization for PDEs such as the heat, wave, and Laplace equations. Students should understand how spatial and temporal derivatives are replaced on grids and why PDE discretization leads to structured algebraic systems.

## Prerequisites

Students should know basic finite differences for ODEs and the PDE models from earlier chapters.

## Background Knowledge Map: Turning PDEs into Sparse Grid Algebra

Four structural concepts govern finite-difference discretizations of elliptic, parabolic, and hyperbolic PDEs:

1. **Centered Stencils and Taylor Cancellation:** The 3-point stencil $\frac{u(x+h) - 2u(x) + u(x-h)}{h^2} = u''(x) + \frac{h^2}{12}u^{(4)}(\xi)$ cancels odd derivatives by symmetry, achieving $O(h^2)$ accuracy; in 2D, summing $x$ and $y$ stencils yields the classic 5-point discrete Laplacian.
2. **Sparse Matrix Structure and M-Matrices:** Discretizing $-u'' = f$ produces a symmetric, positive-definite tridiagonal matrix with diagonal $2/h^2$ and off-diagonals $-1/h^2$. Its inverse has strictly positive entries—preserving a **discrete maximum principle** directly mirroring the continuous PDE.
3. **Boundary Condition Implementation:** Dirichlet values enter directly into the right-hand side $\mathbf{b}$, whereas Neumann conditions ($\partial_n u = g$) are handled via one-sided differences or second-order **ghost points** just outside the boundary.
4. **Method of Lines (Semi-Discretization):** For time-dependent PDEs like $u_t = \nu u_{xx}$, discretizing space first produces a stiff ODE system $\mathbf{U}'(t) = \nu L_h \mathbf{U}(t)$ whose eigenvalues scale like $-\nu/h^2$, directly linking PDE grids to Chapter 13's ODE solvers.

## Introduction

![Finite differences for PDEs]({{ site.imgurl }}/chapter_img/chapter13/05_finite_differences_pdes.svg)

Partial differential equations describe variation in both space and time, so numerical approximation must now discretize more than one independent variable. Finite differences provide the most direct route: replace derivatives by local grid formulas and compute on a mesh.

This lesson extends the numerical viewpoint from ODE stepping to full grid-based PDE computation.

## Concept in Three Ways

### Intuitive View

A PDE on a domain is replaced by a network of nearby interactions between grid points. Each derivative becomes a rule comparing neighboring values.

### Visual View

On a rectangular mesh, each interior point interacts with nearby grid points through a stencil. Different PDEs produce different stencil patterns.

### Formal View

The first and second derivatives are approximated by finite differences, turning PDEs into algebraic update laws or linear systems depending on whether the problem is time-dependent or steady.

## Why the Topic Matters

Finite differences are one of the most practical and widely used entry points into numerical PDEs. They show how analytical PDE structure is translated into computable matrix problems.

They also connect directly to the earlier chapters: the same PDEs studied analytically can now be simulated numerically.

## Common Misconceptions

### "PDE discretization is just ODE discretization with more indices"

Not entirely. The geometry of the mesh and the structure of the spatial operator become central.

### "A finer grid automatically guarantees a better simulation"

Not without considering stability, consistency, and boundary treatment.

### "All PDE stencils behave the same way"

No. Heat, wave, and elliptic equations lead to different computational behavior.

## Suggested Learning Path

### Step 1: Build the mesh

Students should understand the grid as the computational domain.

### Step 2: Derive standard stencils

This is the basic translation from calculus to algebra.

### Step 3: Distinguish time-dependent and steady problems

Parabolic/hyperbolic equations lead to stepping schemes, while elliptic equations lead to linear systems.

### Step 4: Connect to boundary conditions

Boundary treatment is part of the numerical method, not an afterthought.

### Checkpoints

- Can students explain what a finite-difference stencil is?
- Do they understand why elliptic problems lead to linear systems rather than time stepping?
- Can they compare the grid treatment of heat, wave, and Laplace equations?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Solving the 1D Discrete Poisson System by Hand

Discretize the BVP $-u''(x) = 2$ on $(0,1)$ with $u(0) = u(1) = 0$ using centered second differences on a uniform grid with $h = 1/4$ (interior nodes $x_1 = 1/4, x_2 = 1/2, x_3 = 3/4$), and compare with the exact solution $u(x) = x(1-x)$.

1. **Assemble the $3\times 3$ finite-difference system:** At each interior node $j \in \{1,2,3\}$, $\frac{-U_{j-1} + 2U_j - U_{j+1}}{h^2} = 2$ with $U_0 = U_4 = 0$ and $h^2 = 1/16$:
   $$16\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}\begin{pmatrix} U_1 \\ U_2 \\ U_3 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} \iff \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}\begin{pmatrix} U_1 \\ U_2 \\ U_3 \end{pmatrix} = \begin{pmatrix} 1/8 \\ 1/8 \\ 1/8 \end{pmatrix}.$$
2. **Solve using symmetry ($U_1 = U_3$):** The first two equations reduce to:
   $$2U_1 - U_2 = \frac{1}{8}, \qquad -2U_1 + 2U_2 = \frac{1}{8}.$$
   Adding the two equations eliminates $U_1$ immediately:
   $$U_2 = \frac{1}{8} + \frac{1}{8} = \frac{1}{4} = 0.25.$$
   Back-substituting into $2U_1 = U_2 + \frac{1}{8} = \frac{3}{8}$ gives:
   $$U_1 = U_3 = \frac{3}{16} = 0.1875.$$
3. **Compare with the exact solution $u(x) = x(1-x)$:**
   $$u(1/4) = \frac{3}{16}, \qquad u(1/2) = \frac{1}{4}, \qquad u(3/4) = \frac{3}{16}.$$
   The discrete solution is **exact** at every node! Why? Because the truncation error is $\frac{h^2}{12}u^{(4)}(\xi)$, and for a quadratic polynomial $u^{(4)} \equiv 0$.

### Example 1: Heat Equation Grid Update

The heat equation leads to a local averaging type stencil with stability restrictions.

### Example 2: Wave Equation Leapfrog Structure

The wave equation typically requires a two-level time structure reflecting second-order time derivatives.

### Example 3: Laplace Equation Five-Point Stencil

The standard two-dimensional Laplace discretization gives one of the most important elliptic linear systems in numerical analysis.

## Conceptual Questions

1. Why does a PDE stencil encode local interaction on the grid?
2. Why do different PDE types lead to different numerical behaviors?
3. Why are boundary conditions inseparable from PDE discretization?

## Application Problems

1. Why are finite-difference PDE solvers useful in engineering and physics?
2. Why does grid geometry matter in multidimensional simulation?
3. Why is a numerical Laplace solver fundamentally a linear algebra problem?

## Interactive Teaching Strategies

- Draw standard stencils on the board repeatedly.
- Compare heat, wave, and Laplace discretizations structurally.
- Ask students to derive one stencil from a Taylor expansion.
- Reinforce the phrase "PDE to mesh to algebraic system."

## Differentiation

### Support for Struggling Students

Students needing support should focus on one PDE at a time and master a small set of basic stencil formulas.

### Challenge for Advanced Students

Advanced students can compare stencil accuracy, anisotropy, and multidimensional consistency.

## Summary

Finite differences for PDEs translate continuous spatial-temporal models into mesh-based algebraic systems. They are one of the most important gateways from PDE theory to practical computation.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Heat equation simulation
- Problem: We want to approximate
$$ u_t=\alpha u_{xx} $$
on a grid to simulate heat diffusion.
- Model: Use centered differences for $$ u_{xx} $$ and explicit or implicit time stepping.
- Assumptions and limitations: Uniform grid; accuracy and stability depend on $$ \Delta t $$ and $$ \Delta x $$.
- Interpretation: The continuous PDE becomes a large time-dependent linear algebra problem.

#### Vibrating string or wave propagation
- Problem: We track amplitudes at grid points for the wave equation.
- Model: Use finite-difference formulas for time and space derivatives.
- Assumptions and limitations: Poor grid choices can cause numerical reflection or instability.
- Interpretation: Finite differences are the most direct bridge from PDE to code.

### 2. Additional Intuition and Connections

Finite differences replace each derivative by nearby grid differences. This builds a discrete microscopic version of the PDE. A common pitfall is to think local accuracy of the stencil is enough; for PDEs, boundary conditions and global stability are just as important.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

nx = 80
x = np.linspace(0, 1, nx)
dx = x[1] - x[0]
dt = 0.4 * dx**2
r = dt / dx**2
u = np.sin(np.pi * x)

for _ in range(120):
    un = u.copy()
    u[1:-1] = un[1:-1] + r * (un[2:] - 2 * un[1:-1] + un[:-2])
    u[0] = 0.0
    u[-1] = 0.0

plt.plot(x, np.sin(np.pi * x), label="initial")
plt.plot(x, u, label="after many steps")
plt.legend()
plt.title("Finite differences for the heat equation")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: finite difference heat equation animation
- search: wave equation finite difference grid visualization
- search: PDE stencil intuition

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="Finite differences for the heat equation" description="A space-time heatmap of the explicit heat scheme, with a slider for r to show the shift from smoothing to instability." path="interactives/chapter13/finite-differences-pde-en.html" height="660px" %}

### 5. Worked Example

For the explicit heat scheme,
$$
u_j^{n+1}=u_j^n+r\left(u_{j+1}^n-2u_j^n+u_{j-1}^n\right),
$$
where
$$ r=\frac{\alpha \Delta t}{\Delta x^2}. $$
Physically, the new temperature at node $$ j $$ equals the old value plus a diffusion correction from neighboring nodes.

### 6. Difficulty Layering

**Undergraduate level.** Build a stencil and implement a simple grid scheme.

**Graduate level.** Connect to consistency, matrix form, and numerical dissipation/dispersion.

## Video tham khảo

- xem trước: [PDE | Finite differences: introduction](https://www.youtube.com/watch?v=g3Xw1r7QGOE) — commutant, English. commutant introduces finite-difference grids for PDEs.
- [Finite Difference Method for PDES: Solution of Heat Equation](https://www.youtube.com/watch?v=ACduEf-K9qk) — Easy Mathematics, English. The heat equation discretized in space and time.
- [Numerical Differentiation with Finite Difference Derivatives](https://www.youtube.com/watch?v=9fGaTU1-f-0) — Steve Brunton, English. Finite-difference derivatives, the building block of those grids.

## References

- Ascher & Petzold: numerical discretization principles for differential equations.
