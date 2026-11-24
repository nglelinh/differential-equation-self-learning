---
layout: post
title: "11-04 Poisson's Equation"
chapter: '11'
order: 4
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

> **Storytelling Hook:** Place a steady heat lamp over a cooled metal plate, or inject electric charge into a vacuum chamber, and the peaceful flatness of Laplace's equation breaks: the equilibrium surface must now bend upward or downward to carry away the newly generated flux. That inhomogeneous balance, $-\Delta u = f$, is **Poisson's equation**—the workhorse governing everything from gravitational fields inside planets to viscous Poiseuille flow through pipes.

## Learning Objectives

This lesson introduces Poisson's equation as the sourced version of Laplace's equation. Students should understand how forcing changes the elliptic problem and why Poisson models arise in gravitation, electrostatics, and diffusion equilibrium.

## Prerequisites

Students should know Laplace's equation, the meaning of steady-state equilibrium, and the idea that forcing or source terms alter balance laws.

## Background Knowledge Map: Sources, Compatibility, and Inhomogeneous Elliptic Theory

Understanding $-\Delta u = f$ requires connecting four core mathematical concepts:

1. **Superposition of Homogeneous and Particular Solutions:** Because $-\Delta$ is linear, any solution splits into $u = u_p + u_h$, where $-\Delta u_p = f$ absorbs the interior source and $\Delta u_h = 0$ adjusts the boundary values to match the prescribed data.
2. **Divergence Theorem and Neumann Compatibility:** Integrating $-\Delta u = f$ over $\Omega$ gives $-\int_{\partial\Omega} \frac{\partial u}{\partial n}\,dS = \int_\Omega f\,dx$. For a pure Neumann problem, a solution exists *only* if the total interior source balances the total boundary flux—and then it is unique only up to an additive constant.
3. **Eigenfunction Expansion of Sources:** Expanding both $u$ and $f$ in the Dirichlet eigenfunctions $\{\phi_k\}$ of $-\Delta$ (with eigenvalues $\lambda_k > 0$) turns the PDE into algebraic division $\hat{u}_k = \hat{f}_k / \lambda_k$, immediately revealing why the inverse operator $(-\Delta)^{-1}$ gains two derivatives of smoothness.
4. **Newtonian Potential and Fundamental Solutions:** On $\mathbb{R}^n$, convolving $f$ with the fundamental solution $\Phi(x)$ ($-\frac{1}{2\pi}\ln|x|$ in 2D, $\frac{1}{4\pi|x|}$ in 3D) produces an explicit particular solution $u(x) = (\Phi * f)(x)$.

## Introduction

![Poisson equation]({{ site.imgurl }}/chapter_img/chapter11/04_poisson_equation.svg)

Laplace's equation describes source-free equilibrium. But many physical systems are not source free. Charges generate electric potential, mass generates gravitational potential, and internal heating generates nontrivial equilibrium temperature distributions. In such cases, the correct elliptic model is Poisson's equation.

Poisson's equation is therefore the natural next step after Laplace's equation. It adds the effect of internal generation while preserving the basic elliptic equilibrium viewpoint.

## Concept in Three Ways

### Intuitive View

If there is an internal source inside the domain, the equilibrium state must reflect that source. The profile no longer balances as if the interior were empty.

### Visual View

A harmonic function has no internal source term, but a Poisson solution bends in response to the source distribution. The shape of the equilibrium profile reflects where the interior forcing is strongest.

### Formal View

Poisson's equation has the form
$$ -\Delta u = f, $$
or equivalently
$$ \Delta u = -f, $$
depending on convention. Here $$ f $$ represents the source density.

## Why the Equation Matters

Poisson's equation extends the central elliptic model from source-free balance to sourced equilibrium. This greatly enlarges the range of applications and introduces the core idea that the interior of the domain may actively shape the solution, not only the boundary.

It also prepares students for Green's functions and potential-theoretic representation formulas.

## Common Misconceptions

### "Poisson's equation is basically the same as Laplace's equation"

No. The source term fundamentally changes the interpretation and often the solution behavior.

### "Only the boundary matters in elliptic problems"

Not when a source term is present. The interior forcing also matters decisively.

### "The sign convention is the main issue"

No. The real issue is the presence of the source term, not which sign convention is chosen.

## Suggested Learning Path

### Step 1: Recall the source-free case

Students should first remember the meaning of Laplace's equation.

### Step 2: Introduce the source term

This should be interpreted physically rather than merely symbolically.

### Step 3: Compare harmonic and Poisson solutions

The effect of forcing should be visible in example profiles.

### Step 4: Prepare for Green's-function methods

This shows where the lesson is heading next.

### Checkpoints

- Can students explain the physical role of the source term?
- Do they understand how Poisson's equation differs conceptually from Laplace's equation?
- Can they identify application areas where sources naturally appear?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Viscous Pipe Flow / Uniformly Loaded Membrane on the Unit Disk

Solve Poisson's equation $-\Delta u = 2$ on the unit disk $B_1 = \{x^2 + y^2 < 1\}$ with zero Dirichlet boundary condition $u = 0$ on $\partial B_1$, and check both the differential equation and the total flux balance.

1. **Exploit rotational symmetry:** Both the domain $B_1$, the constant source $f \equiv 2$, and the boundary data $0$ are rotationally invariant, so we seek a radial solution $u = u(r)$. The polar Laplacian reduces to:
   $$-\frac{1}{r}\frac{d}{dr}\left(r\frac{du}{dr}\right) = 2 \implies \frac{d}{dr}\left(r\frac{du}{dr}\right) = -2r.$$
2. **Integrate once:**
   $$r\frac{du}{dr} = -r^2 + C_1 \implies \frac{du}{dr} = -r + \frac{C_1}{r}.$$
3. **Enforce regularity at the origin $r = 0$:** To avoid a logarithmic singularity $\ln r$ (which would introduce an unwanted Dirac delta point source at the origin), we must set $C_1 = 0$.
4. **Integrate a second time and apply $u(1) = 0$:**
   $$u(r) = -\frac{1}{2}r^2 + C_2, \qquad u(1) = 0 \implies C_2 = \frac{1}{2}.$$
   In Cartesian coordinates, the exact solution is the paraboloid:
   $$u(x,y) = \frac{1 - x^2 - y^2}{2}.$$
5. **Double-check PDE and flux balance:** Compute $u_{xx} = -1$ and $u_{yy} = -1$, so $-\Delta u = -(-1 - 1) = 2$ everywhere. On $\partial B_1$, the outward normal derivative is $\frac{\partial u}{\partial r}\big|_{r=1} = -1$, so the boundary flux is $-\oint_{\partial B_1} \frac{\partial u}{\partial r}\,ds = 2\pi$, which matches $\iint_{B_1} 2\,dA = 2(\pi \cdot 1^2) = 2\pi$ exactly.

### Example 1: Constant Source

A constant source term produces a solution that bends more strongly than a harmonic one, reflecting persistent interior generation.

### Example 2: Point Source Heuristic

A highly localized source motivates the later Green's-function viewpoint.

### Example 3: Electrostatic Potential

Charge density acts as the source term in the Poisson equation for electrostatics.

## Conceptual Questions

1. Why does adding a source term change the meaning of equilibrium?
2. Why are Poisson problems still elliptic even though they are not harmonic?
3. Why is Poisson's equation central in potential theory?

## Application Problems

1. In electrostatics, what quantity acts as the source in Poisson's equation?
2. In steady-state heat conduction, how does internal heating alter the equilibrium profile?
3. Why is Poisson's equation a better model than Laplace's equation when the interior is active?

## Interactive Teaching Strategies

- Compare one harmonic example and one Poisson example side by side.
- Ask students to describe what the source term means physically in several applications.
- Reinforce the phrase "source-free versus sourced equilibrium."
- Use simple sketches showing how forcing changes curvature.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the physical distinction between no source and source present before worrying about more abstract theory.

### Challenge for Advanced Students

Advanced students can begin thinking about Green's functions and representation formulas for Poisson problems.

## Summary

Poisson's equation extends harmonic theory to include sources. It is the natural equilibrium model when internal generation is present, and it plays a central role in electrostatics, gravitation, heat balance, and later elliptic PDE theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Plate with distributed heat source
- Problem: A thin plate is heated internally, so the steady state is governed by Poisson rather than Laplace.
- Model:
$$ -\Delta u=f. $$
- Assumptions and limitations: Source term $$ f $$ is known, homogeneous material, steady state.
- Interpretation: The right-hand side measures internal forcing away from pure equilibrium.

#### Static membrane deflection under load
- Problem: The static deflection of a membrane or elastic surface under distributed load can be modeled elliptically.
- Model: A Poisson-type equation with $$ f $$ representing load.
- Assumptions and limitations: Small deformation, known loading.
- Interpretation: Unlike Laplace's equation, Poisson includes internal forcing.

### 2. Additional Intuition and Connections

If Laplace represents pure equilibrium, Poisson represents equilibrium with internal forcing. Positive or negative sources generate corresponding average curvature in the solution. A common pitfall is to lose track of sign conventions and therefore misread the physical effect of the source term.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
u = 0.5 * x * (1 - x)

plt.plot(x, u)
plt.xlabel("x")
plt.ylabel("u")
plt.title("1D solution of -u'' = 1 with u(0)=u(1)=0")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Poisson equation source term interpretation
- search: membrane deflection Poisson equation
- search: steady state heat equation with source

### 5. Worked Example

On $$ 0<x<1 $$, solve
$$ -u''=1, \qquad u(0)=u(1)=0. $$
Integrating twice gives
$$ u(x)=\frac{1}{2}x(1-x). $$
The graph bends upward because of the positive uniform source. This is the simplest model of loaded equilibrium.

### 6. Difficulty Layering

**Undergraduate level.** Clearly distinguish Laplace from Poisson through the role of the source.

**Graduate level.** Connect to weak formulations, elliptic regularity, and maximum principles with forcing.

## Video tham khảo

- xem trước: [mod08lec73 - The Poisson's Equation: Green's function solution](https://www.youtube.com/watch?v=hiHWwZb2AVU) — NPTEL-NOC IITM, English. NPTEL solves Poisson's equation with a Green's function.
- [Laplace's Equation and Poisson's Equation](https://www.youtube.com/watch?v=nmvs0vrBT18) — Steve Brunton, English. How Poisson's equation differs from Laplace's by a source term.
- [Lecture 4: Electrostatic potential, Poisson's Equation, Laplace's Equation, Green's functions](https://www.youtube.com/watch?v=Z0-AkSfMJYU) — rkingery, English. Electrostatic potential, Poisson, and Laplace in one lecture.

## References

- Evans, Chapters 2 and 6.
