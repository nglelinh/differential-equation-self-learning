---
layout: post
title: "13-07 Finite Element Introduction"
chapter: '13'
order: 7
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: optional
---

> **Storytelling Hook:** Try laying a rigid rectangular finite-difference grid over a curved turbine blade or a human heart valve, and the staircase boundary errors ruin your physics. The **Finite Element Method (FEM)** flips the paradigm completely: instead of approximating derivatives on a square grid, it takes the **weak formulation** from Chapter 12 and projects it onto simple piecewise-polynomial "hat" functions draped over arbitrary triangles or tetrahedra.

## Learning Objectives

This lesson introduces the finite element method as a mesh-based variational discretization. Students should understand why weak formulations matter numerically, how basis functions are attached to a mesh, and why finite elements are especially powerful for complex geometries.

## Prerequisites

Students should know weak formulations from Chapter 12 and basic numerical PDE discretization ideas.

## Background Knowledge Map: From Weak Formulations to Galerkin Finite Elements

Four foundational pillars link Sobolev spaces directly to industrial-strength engineering software:

1. **Galerkin Projection onto Finite-Dimensional Subspaces $V_h \subset H_0^1(\Omega)$:** Replacing the infinite-dimensional test space $H_0^1(\Omega)$ by a finite-dimensional span of basis functions $\{\phi_1, \dots, \phi_N\}$ converts $a(u,v) = F(v)$ into the linear system $K\mathbf{c} = \mathbf{f}$ with stiffness matrix $K_{ij} = a(\phi_j, \phi_i)$.
2. **Local Hat Basis Functions and Sparsity:** Choosing piecewise-linear ($P_1$) hat functions supported only on elements touching node $i$ ensures $K_{ij} = 0$ whenever nodes $i$ and $j$ do not share an element, keeping $K$ ultra-sparse and symmetric positive definite.
3. **Galerkin Orthogonality and Céa's Lemma:** Because $a(u - u_h, v_h) = 0$ for all $v_h \in V_h$, the FEM solution $u_h$ is the **best possible approximation** in the energy norm: $\|u - u_h\|_{H^1} \le \frac{M}{\alpha}\inf_{v_h \in V_h}\|u - v_h\|_{H^1}$.
4. **Element-by-Element Assembly:** In practice, computers never integrate globally over $\Omega$; they compute tiny local element stiffness matrices on a reference triangle/interval and scatter-add them into the global matrix $K$.

## Introduction

![Finite element introduction]({{ site.imgurl }}/chapter_img/chapter13/07_finite_element_introduction.svg)

Finite differences are simple and powerful on structured grids, but many practical domains are irregular and geometrically complex. The finite element method addresses this by building the approximation space from local basis functions attached to a mesh.

The method is one of the most important bridges between functional analysis and numerical computation.

## Concept in Three Ways

### Intuitive View

Instead of approximating derivatives directly at points, finite elements approximate the whole solution by patching together simple functions on small mesh cells.

### Visual View

The mesh breaks the domain into triangles or intervals, and each node supports a local basis function. The global approximation is assembled from those local pieces.

### Formal View

The finite element method begins from a weak formulation and restricts the problem to a finite-dimensional trial space spanned by basis functions adapted to the mesh.

## Why the Method Matters

Finite elements are indispensable in modern engineering and scientific computation because they handle irregular domains, variational structure, and complex PDE systems naturally.

They also make clear why Chapter 12 matters numerically: weak formulations are not only theoretical tools, but computational starting points.

## Common Misconceptions

### "Finite elements are just more complicated finite differences"

No. They arise from a variational viewpoint rather than direct derivative replacement.

### "Weak formulations are only for pure theory"

No. They are the natural basis of finite element computation.

### "Basis functions are arbitrary local gadgets"

No. Their construction reflects the mesh and the approximation space.

## Suggested Learning Path

### Step 1: Recall weak formulations

Students should connect the method to variational thinking.

### Step 2: Build local basis functions

This is the core geometric idea of the method.

### Step 3: Assemble the global system

The transition from local cells to a global matrix problem should be emphasized.

### Step 4: Compare with finite differences

This clarifies why finite elements are so valuable.

### Checkpoints

- Can students explain why weak formulations matter numerically?
- Do they understand what a basis function attached to a node means?
- Can they describe one advantage of finite elements over finite differences?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Assembling and Solving a 1D $P_1$ Finite Element System

Solve $-u''(x) = 1$ on $(0,1)$ with $u(0) = u(1) = 0$ (exact solution $u(x) = \frac{1}{2}x(1-x)$) using $P_1$ linear hat functions on 3 uniform elements of length $h = 1/3$ (interior nodes $x_1 = 1/3$, $x_2 = 2/3$).

1. **Define the two interior hat basis functions:** $\phi_1(x)$ rises linearly from $0$ at $x=0$ to $1$ at $x=1/3$ (slope $+3$) and falls to $0$ at $x=2/3$ (slope $-3$); $\phi_2(x)$ rises on $[1/3, 2/3]$ (slope $+3$) and falls on $[2/3, 1]$ (slope $-3$).
2. **Compute the $2\times 2$ stiffness matrix $K_{ij} = \int_0^1 \phi_i'(x)\phi_j'(x)\,dx$:**
   - Diagonal entries: $K_{11} = \int_0^{1/3} 3^2\,dx + \int_{1/3}^{2/3} (-3)^2\,dx = 3 + 3 = 6$, and by symmetry $K_{22} = 6$.
   - Off-diagonal entries (overlap occurs only on $[1/3, 2/3]$ where $\phi_1' = -3$ and $\phi_2' = +3$):
     $$K_{12} = K_{21} = \int_{1/3}^{2/3} (-3)(+3)\,dx = -9 \cdot \frac{1}{3} = -3.$$
3. **Compute the load vector $f_i = \int_0^1 1\cdot\phi_i(x)\,dx$:** Each hat is a triangle of base $2h = 2/3$ and height $1$, so its area is:
   $$f_1 = f_2 = \frac{1}{2}\left(\frac{2}{3}\right)(1) = \frac{1}{3}.$$
4. **Solve $K\mathbf{c} = \mathbf{f}$:**
   $$\begin{pmatrix} 6 & -3 \\ -3 & 6 \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 1/3 \\ 1/3 \end{pmatrix} \implies 3c_1 = \frac{1}{3} \implies c_1 = c_2 = \frac{1}{9}.$$
   Checking the exact solution at the nodes: $u(1/3) = \frac{1}{2}\left(\frac{1}{3}\right)\left(\frac{2}{3}\right) = \frac{1}{9}$ and $u(2/3) = \frac{1}{9}$—the $P_1$ Galerkin solution hits the exact values at both nodes!

### Example 1: Piecewise Linear Basis on an Interval

This is the simplest finite element example and introduces the idea of hat functions.

### Example 2: Weak Form to Matrix System

The bilinear form becomes a stiffness matrix after restriction to a finite-dimensional space.

### Example 3: Irregular Geometry Motivation

A nonrectangular domain shows why finite elements are often preferable to structured-grid methods.

## Conceptual Questions

1. Why is the weak formulation a natural starting point for finite elements?
2. Why do local basis functions make geometric flexibility possible?
3. How does the method connect analysis and computation?

## Application Problems

1. Why are finite elements widely used in structural mechanics?
2. Why do irregular domains favor finite elements over classical finite differences?
3. Why is the stiffness matrix a natural algebraic object in this method?

## Interactive Teaching Strategies

- Draw hat functions on a simple interval mesh.
- Show how local support leads to sparse matrices.
- Compare finite element and finite difference viewpoints explicitly.
- Tie the lesson back to Sobolev spaces and weak solutions.

## Differentiation

### Support for Struggling Students

Students needing support should focus on one-dimensional piecewise linear elements before any higher-dimensional generalization.

### Challenge for Advanced Students

Advanced students can explore Galerkin orthogonality, error estimates, or triangular mesh construction.

## Summary

Finite elements provide a variational, mesh-based approach to PDE computation. They connect weak formulation, geometry, and linear algebra in one of the most important frameworks of modern numerical analysis.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Structural mechanics and elasticity
- Problem: Complex geometries such as bridges, bones, and machine frames are difficult to handle with regular finite-difference grids.
- Model: Subdivide the domain into triangles or tetrahedra and search for an approximate solution in a finite-dimensional space.
- Assumptions and limitations: One must generate a mesh and choose basis functions carefully.
- Interpretation: FEM turns PDEs into energy problems on small elements.

#### Heat transfer in engineered components
- Problem: Curved boundaries, holes, and composite materials make finite differences less flexible.
- Model: Use the weak form and finite element spaces to approximate the solution.
- Assumptions and limitations: Mesh quality strongly affects error.
- Interpretation: FEM directly exploits the weak-solution structure from the previous chapter.

### 2. Additional Intuition and Connections

The finite element method does not begin with discrete derivatives, but with the weak form and a finite-dimensional approximation space. That is why it naturally fits Sobolev spaces and Lax-Milgram. A common pitfall is to see FEM as just a software technique; its analytical foundation is deep.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([0.0, 0.3, 0.55, 0.8, 1.0])
values = np.array([0.0, 0.6, 0.2, 0.5, 0.0])

xx = np.linspace(0, 1, 400)
yy = np.interp(xx, nodes, values)

plt.plot(xx, yy, label="piecewise linear FEM approximation")
plt.plot(nodes, values, "o", label="mesh nodes")
plt.legend()
plt.title("Linear basis behavior in 1D finite elements")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: finite element basis functions visualization
- search: triangulation PDE FEM intuition
- search: weak form to finite element method animation

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="Hat basis functions in 1D FEM" description="Adjust the number of mesh nodes and the selected basis function to see local support directly." path="interactives/chapter13/finite-element-basis-en.html" height="620px" %}

### 5. Worked Example

On $$ [0,1] $$, a piecewise linear finite element approximation has the form
$$ u_h(x)=\sum_{i=1}^N U_i \phi_i(x), $$
where the $$ \phi_i $$ are hat functions. Substituting into the weak form of
$$ -u''=f $$
produces a matrix system
$$ KU=F. $$
This is the direct discrete version of weak-solution thinking.

### 6. Difficulty Layering

**Undergraduate level.** Understand meshes, hat functions, and the 1D stiffness matrix.

**Graduate level.** Connect to Cea's lemma, adaptive refinement, and mixed methods.

## Video tham khảo

- xem trước: [MIT Numerical Methods for PDEs Lecture 17: FEM Error Analysis in Sobolev and L2 norms](https://www.youtube.com/watch?v=nj0fpJUOl64) — Aerodynamic CFD, English. An MIT numerical-PDE lecture on finite-element error in Sobolev and L^2 norms.
- [Lax-Milgram, application to Poisson equation.](https://www.youtube.com/watch?v=s5P3e1FhpTk) — Learn Maths with Dr Alex, English. The weak form of Poisson's equation that a finite-element method discretizes.
- [Lax-Milgram lemma](https://www.youtube.com/watch?v=w8QjyVug78M) — Numerical Analysis by Julian Roth, English. Lax-Milgram, the existence theorem behind that weak form.

## References

- Ascher & Petzold: useful entry point from numerical differential equations to broader discretization themes.
