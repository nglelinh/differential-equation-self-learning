---
layout: post
title: "11-01 Laplace's Equation: Introduction"
chapter: '11'
order: 1
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

> **Storytelling Hook:** Dip a bent copper wire loop into soapy water and lift it into the air. Almost instantaneously, the shimmering soap film snaps into a surface of astonishing smoothness—no bumps, no creases, no wasted area. Every interior point negotiates an exact truce with its immediate neighbors, dictated solely by the wire frame along the rim. That silent, timeless negotiation is **Laplace's equation**, $\Delta u = 0$, the mathematical voice of equilibrium across heat conduction, electrostatics, gravity, and ideal fluid mechanics.

## Learning Objectives

This lesson introduces Laplace's equation as the prototype steady-state elliptic PDE. Students should understand harmonic functions, equilibrium interpretation, and why Laplace's equation differs qualitatively from the heat and wave equations.

## Prerequisites

Students should know partial derivatives, basic boundary conditions, and the idea of steady state from earlier heat-equation examples. Some familiarity with separation of variables is also helpful.

## Key ideas: Foundations of Harmonic Equilibrium

To appreciate why $\Delta u = 0$ behaves so differently from time-evolution PDEs, anchor your intuition in four connected mathematical pillars:

1. **Divergence, Flux, and Conservation Laws (Vector Calculus):** In steady-state physics, the flux $\mathbf{J} = -k\nabla u$ satisfies $\nabla \cdot \mathbf{J} = 0$ in any source-free region. The Laplacian $\Delta u = \nabla \cdot (\nabla u)$ measures the net outward flux of the gradient; setting it to zero declares that inflow and outflow balance identically at every infinitesimal control volume.
2. **Dirichlet Energy and Calculus of Variations:** Harmonic functions are the critical points (in fact, unique minimizers) of the Dirichlet energy $E[u] = \frac{1}{2}\int_\Omega |\nabla u|^2\,dx$ among all functions matching prescribed boundary data. Equilibrium is literally the path of least total gradient tension.
3. **Complex Analysis and Harmonic Conjugates:** In two dimensions, the real and imaginary parts of any holomorphic function $f(z) = u(x,y) + i v(x,y)$ automatically satisfy $\Delta u = \Delta v = 0$ via the Cauchy–Riemann equations. This link gives 2D potential theory extraordinary rigidity and conformal invariance.
4. **Elliptic Well-Posedness and Global Coupling:** Unlike hyperbolic waves that travel at finite speed, elliptic equations couple the entire domain instantaneously. Changing the boundary temperature at a single point alters the equilibrium value at every interior point, yet simultaneously smooths away boundary roughness.

## Introduction

![Laplace equation introduction]({{ site.imgurl }}/chapter_img/chapter11/01_laplace_equation_introduction.svg)

Laplace's equation sits at the center of classical PDE theory. It governs equilibrium temperature distributions, electrostatic potentials, gravitational potentials in source-free regions, and idealized incompressible irrotational flow. Unlike the heat equation or the wave equation, it has no time variable. It describes a state that has already settled into balance.

This makes Laplace's equation the natural next step after time-dependent PDEs. Once transient dynamics have died away, the remaining configuration often satisfies an elliptic equilibrium equation. The mathematics becomes less about evolution and more about global structure, rigidity, and boundary influence.

## Concept in Three Ways

### Intuitive View

Imagine a metal plate held at fixed temperatures along its boundary. After enough time, the temperature no longer changes. The interior settles into the unique arrangement compatible with those boundary values. That equilibrium profile is governed by Laplace's equation.

### Visual View

A harmonic function has no interior spikes or pits unless forced by the boundary. Its values are balanced by their surroundings. The graph of a harmonic function tends to look smooth and globally constrained rather than locally erratic.

### Formal View

Laplace's equation is
$$ \Delta u = 0. $$
In two variables this means
$$ u_{xx}+u_{yy}=0. $$
Solutions are called harmonic functions. They satisfy powerful qualitative properties such as the mean value property and the maximum principle.

## Why the Equation Matters

Laplace's equation is one of the most rigid PDEs in mathematics. Boundary data strongly control the interior solution. This makes the equation ideal for proving uniqueness, understanding geometric constraints, and developing potential theory.

It also marks a conceptual shift in the course. For heat and wave equations, we asked how a system evolves. For Laplace's equation, we ask which global equilibrium configurations are possible.

## Common Misconceptions

### "Laplace's equation means nothing happens"

Wrong. It means the system has reached equilibrium, and describing that equilibrium is often the main mathematical problem.

### "The boundary is a minor detail"

Wrong. In elliptic problems, the boundary often determines everything.

### "A harmonic function can have an isolated interior maximum"

No. The maximum principle says this cannot happen unless the function is constant.

### "Laplace's equation is only about temperature"

No. It appears across electrostatics, gravity, fluid flow, and many other equilibrium theories.

## Suggested Learning Path

### Step 1: Start from equilibrium intuition

Students should first see Laplace's equation as the natural steady-state limit of diffusion.

### Step 2: Write the operator explicitly

The Laplacian should be interpreted as a measure of local imbalance.

### Step 3: Emphasize harmonic behavior

Solutions are not arbitrary smooth functions; they satisfy strong average and extremum properties.

### Step 4: Connect to boundary-value structure

The equation belongs naturally to a boundary-value setting rather than an initial-value setting.

### Checkpoints

- Can students explain why Laplace's equation models equilibrium?
- Do they understand why boundary values play such a dominant role?
- Can they distinguish elliptic behavior from parabolic and hyperbolic behavior?

## Worked Examples


### Worked example: Verifying Harmonicity, Zero Net Flux, and Dirichlet Energy

Let us test all three pillars of Laplace's equation—pointwise vanishing Laplacian, zero net boundary flux, and finite Dirichlet energy—on the canonical saddle function $u(x,y) = x^2 - y^2$ over the unit disk $B_1 = \{(x,y) : x^2 + y^2 < 1\}$.

1. **Check the PDE directly:** Compute the pure second partial derivatives:
   $$u_x = 2x \implies u_{xx} = 2, \qquad u_y = -2y \implies u_{yy} = -2.$$
   Summing gives $\Delta u = u_{xx} + u_{yy} = 2 + (-2) = 0$ everywhere on $\mathbb{R}^2$. Notice that $u$ bends upward along the $x$-axis and downward by the exact same curvature along the $y$-axis—a hallmark of harmonic functions.
2. **Verify zero net flux across the boundary circle $\partial B_1$:** On the unit circle $(x,y) = (\cos\theta, \sin\theta)$, the outward unit normal is $\mathbf{n} = (\cos\theta, \sin\theta)$ and the gradient is $\nabla u = (2\cos\theta, -2\sin\theta)$. Their dot product is:
   $$\nabla u \cdot \mathbf{n} = 2\cos^2\theta - 2\sin^2\theta = 2\cos(2\theta).$$
   Integrating around the circle gives the total flux:
   $$\oint_{\partial B_1} \nabla u \cdot \mathbf{n}\,ds = \int_0^{2\pi} 2\cos(2\theta)\,d\theta = \big[\sin(2\theta)\big]_0^{2\pi} = 0.$$
   Heat enters through the arcs near $\theta = 0, \pi$ and exits in exact balance through $\theta = \pm \pi/2$.
3. **Compute the Dirichlet energy on $B_1$:** Since $|\nabla u|^2 = (2x)^2 + (-2y)^2 = 4(x^2 + y^2) = 4r^2$, integrating in polar coordinates yields:
   $$E[u] = \frac{1}{2}\iint_{B_1} |\nabla u|^2\,dA = \frac{1}{2}\int_0^{2\pi}\int_0^1 4r^2 \cdot r\,dr\,d\theta = 2(2\pi)\left[\frac{r^4}{4}\right]_0^1 = \pi.$$
   By Dirichlet's Principle, *every* other $C^1$ function $v$ on $\overline{B_1}$ satisfying $v(\cos\theta,\sin\theta) = \cos(2\theta)$ has strictly larger energy $E[v] > \pi$.

### Example 1: Linear Function

If
$$ u(x,y)=ax+by+c, $$
then $$ u_{xx}=u_{yy}=0 $$, so $$ u $$ is harmonic. This shows that affine functions are simple equilibrium profiles.

### Example 2: Quadratic Balance

The function
$$ u(x,y)=x^2-y^2 $$
is harmonic because
$$ u_{xx}=2,
\qquad
u_{yy}=-2, $$
so their sum is zero.

### Example 3: Radial Nonexample

The function
$$ u(x,y)=x^2+y^2 $$
is not harmonic because
$$ u_{xx}+u_{yy}=4. $$
This is a useful contrast with Poisson's equation, which will appear next.

## Conceptual Questions

1. Why is Laplace's equation naturally associated with equilibrium rather than evolution?
2. Why do harmonic functions resist interior maxima and minima?
3. Why is the boundary especially important for elliptic equations?

## Application Problems

1. In electrostatics, what physical quantity corresponds to a harmonic function in a charge-free region?
2. In heat conduction, why does steady state eliminate the time derivative but keep the spatial structure?
3. In fluid flow, why do incompressibility and irrotationality lead naturally to harmonic potentials?

## Interactive Teaching Strategies

- Ask students to compare the roles of time in the heat, wave, and Laplace equations.
- Use equilibrium temperature examples on plates or rectangles to make the boundary-value viewpoint concrete.
- Let students test simple candidate functions and classify them as harmonic or not.
- Reinforce the phrase "global equilibrium shaped by the boundary."

## Differentiation

### Support for Struggling Students

Students needing support should work with simple polynomial examples and steady-state heat interpretations before confronting more abstract properties.

### Challenge for Advanced Students

Advanced students can begin exploring mean value formulas, conformal ideas in two dimensions, or the connection between Laplace's equation and complex analysis.

## Summary

Laplace's equation describes equilibrium without sources. It is the central model of elliptic PDE theory and potential theory, and it marks a major conceptual shift from time evolution to globally constrained steady-state structure.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Steady temperature in a plate
- Problem: We want the temperature distribution after the system has reached equilibrium.
- Model:
$$ \Delta u=0. $$
- Assumptions and limitations: No time dependence, no internal heat source.
- Interpretation: Harmonic functions describe spatial equilibrium states.

#### Electrostatic potential
- Problem: In a charge-free region, electric potential satisfies an elliptic PDE.
- Model: With no charge present, the potential $$ \phi $$ satisfies $$ \Delta \phi=0 $$.
- Assumptions and limitations: Homogeneous medium, electrostatic regime, idealized boundaries.
- Interpretation: The same PDE models both thermal and electrostatic equilibrium.

### 2. Additional Intuition and Connections

Laplace's equation is the equilibrium version of many physical processes. If the heat equation describes the approach to equilibrium, Laplace's equation describes the state after equilibrium has been reached. A common pitfall is to treat $$ \Delta u=0 $$ as abstract symbolism; physically it says there is no local imbalance left inside the domain.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 160)
y = np.linspace(-1, 1, 160)
X, Y = np.meshgrid(x, y)
U = X**2 - Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, U, cmap="coolwarm")
ax.set_title("Example harmonic function: u = x^2 - y^2")
plt.show()
```

### 4. Suggested Searches

- search: harmonic function surface plot
- search: Laplace equation steady state temperature simulation
- search: electrostatic potential Laplace equation visualization

### 5. Worked Example

For a one-dimensional bar at steady state with no internal heat source,
$$ u''(x)=0. $$
Hence
$$ u(x)=Ax+B. $$
If $$ u(0)=T_0 $$ and $$ u(L)=T_L $$, the solution is the linear interpolation between the endpoints. This is the simplest model of equilibrium without sources.

### 6. Difficulty Layering

**Undergraduate level.** Understand Laplace's equation as a model of spatial equilibrium.

**Graduate level.** Connect to ellipticity, regularity, and the maximum principle.

## Video tham khảo

- xem trước: [Laplace's Equation and Poisson's Equation](https://www.youtube.com/watch?v=nmvs0vrBT18) — Steve Brunton, English. Brunton places Laplace's equation next to Poisson's equation.
- [Laplace's Equation and Potential Flow](https://www.youtube.com/watch?v=zN0zDrQimXU) — Steve Brunton, English. Laplace's equation as the potential of an incompressible flow.
- [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, English. Separation of variables as the first solution method for the equation.

## References

- Evans, Chapters 2 and 6.
- Haberman, Chapters 6-7.
