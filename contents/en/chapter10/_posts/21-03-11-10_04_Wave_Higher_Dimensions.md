---
layout: post
title: "10-04 Wave Equation in Higher Dimensions"
chapter: '10'
order: 4
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: required
---

Clap your hands in an open field (3D) and the sound arrives as a crisp snap followed by dead silence. Now drop a pebble into a still pond (2D) and watch: after the leading circular crest passes a floating leaf, the leaf keeps bobbing up and down in a lingering tail! Why does 3D space transmit crisp, echo-free speech and radio signals, whereas 2D flatland would leave every spoken word smeared in a muddled afterglow?

The answer is **Huygens' Principle**, one of the deepest dimensional surprises in mathematical physics: Kirchhoff's formula in 3D depends *only* on the spherical surface $$ |\mathbf{y} - \mathbf{x}| = ct $$, whereas Hadamard's method of descent to 2D integrates over the entire filled disk $$ |\mathbf{y} - \mathbf{x}| \le ct $$!

## Key ideas: Higher-Dimensional Waves and Huygens' Principle

1. **Multi-Dimensional Laplacian & Rectangular Degeneracy:** On a 2D rectangular membrane $$ [0, a] \times [0, b] $$, separating $$ u_{tt} = c^2(u_{xx} + u_{yy}) $$ yields modes $$ \sin(m\pi x/a)\sin(n\pi y/b) $$ with frequencies $$ \omega_{mn} = c\pi\sqrt{\frac{m^2}{a^2} + \frac{n^2}{b^2}} $$. On a square ($$ a = b $$), distinct pairs like $$ (1, 2) $$ and $$ (2, 1) $$ share the exact same frequency—creating *degenerate* nodal patterns (Chladni figures)!
2. **Spherical Symmetry Reduction (3D Reduces to 1D!):** For a radially symmetric 3D wave $$ u(r, t) $$, setting $$ w(r, t) = r\,u(r, t) $$ transforms $$ u_{tt} = c^2\left(u_{rr} + \frac{2}{r}u_r\right) $$ identically into the 1D wave equation $$ w_{tt} = c^2 w_{rr} $$, revealing the exact $$ 1/r $$ geometric amplitude decay of spherical waves!
3. **Kirchhoff's Formula (3D — Sharp Huygens' Principle):** In $$ \mathbb{R}^3 $$, $$ u(\mathbf{x}, t) $$ depends *solely* on initial data on the thin spherical shell $$ \partial B(\mathbf{x}, ct) $$. Once the trailing edge of a localized pulse passes, $$ u $$ returns to *exact zero*.
4. **Poisson's Formula via Method of Descent (2D — Lingering Tail):** Viewing a 2D wave as a $$ z $$-independent 3D wave projects the spherical shell onto the *entire interior* of the 2D disk $$ B(\mathbf{x}, ct) $$ with kernel $$ \frac{1}{\sqrt{c^2 t^2 - |\mathbf{x} - \mathbf{y}|^2}} $$, creating a permanent decaying wake behind every 2D wavefront!

### Worked example: Degenerate Chladni Modes on a Square Membrane and 3D Radial Decay

**Problem:** (a) On a square membrane $$ [0, \pi] \times [0, \pi] $$ with $$ c = 1 $$ and clamped edges, verify that $$ u_{12}(x,y) = \sin(x)\sin(2y) $$ and $$ u_{21}(x,y) = \sin(2x)\sin(y) $$ share the same frequency $$ \omega $$, and find the nodal line of their superposition $$ v(x, y) = u_{12}(x, y) - u_{21}(x, y) $$. (b) Verify directly that $$ u(r, t) = \frac{f(r - ct)}{r} $$ satisfies the 3D radial wave equation $$ u_{tt} = c^2(u_{rr} + \frac{2}{r}u_r) $$.

1. **Compute frequencies and Chladni nodal lines on $$ [0, \pi]^2 $$:**
   - Eigenvalues: $$ \lambda_{12} = 1^2 + 2^2 = 5 $$ and $$ \lambda_{21} = 2^2 + 1^2 = 5 $$, so both vibrate at $$ \omega = \sqrt{5} $$!
   - Factor the superposition $$ v(x, y) = \sin(x)\sin(2y) - \sin(2x)\sin(y) $$ using $$ \sin(2\theta) = 2\sin\theta\cos\theta $$:
     $$ v(x, y) = 2\sin(x)\sin(y)\bigl[\cos(y) - \cos(x)\bigr]. $$
   - Inside $$ (0, \pi)^2 $$, $$ \sin x > 0 $$ and $$ \sin y > 0 $$, so $$ v(x, y) = 0 \iff \cos y = \cos x \iff y = x $$!
   While $$ u_{12} $$ has a horizontal nodal line ($$ y = \pi/2 $$) and $$ u_{21} $$ has a vertical one ($$ x = \pi/2 $$), their equal-frequency combination snaps onto the **diagonal** $$ y = x $$!
2. **Verify the 3D outgoing spherical wave $$ u(r, t) = \frac{f(r - ct)}{r} $$:**
   Let $$ w(r, t) = r u(r, t) = f(r - ct) $$. Compute:
   - $$ w_r = u + r u_r \implies w_{rr} = 2 u_r + r u_{rr} = r\left(u_{rr} + \frac{2}{r}u_r\right) $$.
   - $$ w_{tt} = r u_{tt} $$.
   Since $$ w = f(r - ct) $$ satisfies $$ w_{tt} = c^2 f''(r - ct) = c^2 w_{rr} $$, dividing by $$ r > 0 $$ gives $$ u_{tt} = c^2\left(u_{rr} + \frac{2}{r}u_r\right) $$ identically!

## Learning Objectives

This lesson extends wave analysis to two and three dimensions. Students should understand how geometry affects wave propagation and why radial or domain-specific coordinates become important.

## Prerequisites

Students should know the one-dimensional wave equation, d'Alembert's formula conceptually, and separation of variables on bounded intervals.

## Introduction

![Wave equation in higher dimensions]({{ site.imgurl }}/chapter_img/chapter10/04_wave_higher_dimensions.svg)

Waves in one dimension already show propagation, superposition, and finite speed. In higher dimensions, the same basic PDE ideas remain, but geometry becomes far more important. Disturbances may spread in circles, spheres, or domain-dependent patterns, and symmetry now plays a central role in choosing coordinates and methods.

This lesson is where students begin to see that PDEs are deeply shaped by geometry. The underlying equation may look similar, but the spatial setting changes everything about the natural solution structure.

## Concept in Three Ways

### Intuitive View

A sound pulse emitted from a point in space does not move left and right like a string vibration. It spreads outward in all directions. The shape of that spreading depends on the surrounding geometry.

### Visual View

In two dimensions, a localized wave may expand as a circular front. In three dimensions, it may expand as a spherical shell. Boundaries and obstacles can reshape the wave dramatically.

### Formal View

The higher-dimensional wave equation is
$$ u_{tt}=c^2 \Delta u, $$
where $$ \Delta $$ is the Laplacian in two or three spatial dimensions. The choice of coordinates often depends on domain symmetry, such as Cartesian coordinates for rectangles and radial coordinates for circular or spherical settings.

## Why Higher Dimensions Matter

Real physical waves almost never live in one dimension alone. Sound, light, water waves, and elastic waves all propagate in higher-dimensional spaces. This lesson therefore marks the shift from simplified models to more realistic geometries.

It also shows that PDEs are not just equations but equations on spaces, and the geometry of the domain becomes mathematically decisive.

## Common Misconceptions

### "Higher-dimensional waves are just one-dimensional waves with extra variables"

No. The geometry changes the nature of propagation, symmetry, and solution methods.

### "If the PDE looks similar, the behavior must be essentially identical"

Not true. Geometry strongly shapes what the solutions look like.

### "Coordinate changes are just technical conveniences"

No. They often reveal the natural symmetry of the physical problem.

## Suggested Learning Path

### Step 1: Recall one-dimensional propagation

Students should begin by contrasting the line with the plane or space.

### Step 2: Interpret the Laplacian geometrically

The multidimensional spatial operator should be understood as the core generalization.

### Step 3: Match coordinates to symmetry

This shows why circles and spheres naturally suggest polar or spherical coordinates.

### Step 4: Interpret propagation fronts

Students should see how the disturbance shape depends on dimension and geometry.

### Checkpoints

- Can students explain why geometry matters more in higher dimensions?
- Do they understand why radial symmetry suggests adapted coordinates?
- Can they compare propagation on the line with propagation in the plane or space?

## Worked Examples

### Example 1: Radial Disturbance

A localized pulse in a symmetric medium may produce circular or spherical wave fronts, showing how symmetry simplifies the analysis.

### Example 2: Rectangular Domain

In a rectangular membrane, separation of variables in Cartesian coordinates leads to mode families indexed by more than one integer.

### Example 3: Circular Domain

In a disk, polar coordinates reveal radial and angular structure much more naturally than Cartesian coordinates.

## Conceptual Questions

1. Why do wave fronts in higher dimensions depend strongly on geometry?
2. Why is the Laplacian the natural spatial operator in multidimensional wave equations?
3. Why do adapted coordinates often simplify PDE analysis so dramatically?

## Application Problems

1. Why does sound spread outward from a source rather than only in one direction?
2. How does a drum membrane differ mathematically from a vibrating string?
3. Why are circular and spherical geometries common in wave applications?

## Interactive Teaching Strategies

- Compare string vibrations with drum or acoustic wave examples.
- Ask students to sketch propagation fronts in one, two, and three dimensions.
- Use symmetry arguments before writing formulas.
- Reinforce the phrase "geometry shapes propagation."

## Differentiation

### Support for Struggling Students

Students needing support should focus on visual propagation patterns and symmetry before confronting multidimensional formulas.

### Challenge for Advanced Students

Advanced students can examine radial reductions or modal structures in circular and spherical domains.

## Summary

Higher-dimensional wave equations reveal how geometry shapes propagation. Domains, coordinates, and symmetry become central analytic features, and the study of waves begins to merge naturally with geometry and spectral theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Vibrating drumhead
- Problem: The oscillation of a two-dimensional membrane determines the sound of a drum.
- Model:
$$ u_{tt}=c^2\Delta u. $$
- Assumptions and limitations: Thin membrane, uniform tension, small displacement.
- Interpretation: In higher dimensions, total spatial curvature is measured by the Laplacian.

#### Acoustic waves in a room
- Problem: Sound pressure in a room reflects and forms spatial resonance patterns.
- Model: A multidimensional wave equation with boundary conditions determined by wall behavior.
- Assumptions and limitations: Linear acoustics, homogeneous medium, idealized geometry.
- Interpretation: The geometry of the domain shapes the resonant frequencies.

### 2. Additional Intuition and Connections

In higher dimensions, disturbances do not merely move left and right; they spread through many directions. Geometry therefore becomes essential. This is a natural bridge to spectral theory of domains and eigenvalue problems for the Laplacian.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 120)
y = np.linspace(0, 1, 120)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi * X) * np.sin(2 * np.pi * Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("A membrane mode on a rectangular domain")
plt.show()
```

### 4. Suggested Searches

- search: drumhead mode animation wave equation
- search: 2D wave equation membrane simulation
- search: room acoustics standing modes visualization

### 5. Worked Example

On the rectangle $$ 0<x<a $$, $$ 0<y<b $$, a normal mode has the form
$$
u(x,y,t)=\sin\!\left(\frac{m\pi x}{a}\right)\sin\!\left(\frac{n\pi y}{b}\right)\cos(\omega_{mn} t),
$$
where
$$
\omega_{mn}=c\pi\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}}.
$$
The mode numbers and the geometry together determine the frequency.

### 6. Difficulty Layering

**Undergraduate level.** Recognize the Laplacian as the spatial curvature operator in higher dimensions.

**Graduate level.** Connect to spectral geometry, Laplacian eigenfunctions, and domain-dependent spectra.

## Video tham khảo

- xem trước: [Vibrating Circular Membranes - Partial Differential Equations | Lecture 31](https://www.youtube.com/watch?v=DeG6dq4vlO4) — Jason Bramburger, English. A circular membrane: Bessel functions in the radial wave eigenvalue problem.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, English. The one-dimensional derivation this higher-dimensional equation extends.
- [Deriving the Heat Equation in 2D & 3D (& in N Dimensions!) with Control Volumes and Vector Calculus](https://www.youtube.com/watch?v=lBZIxv1bZDo) — Steve Brunton, English. Brunton's control-volume derivation in 2D and 3D, the same balance in higher dimension.

## References

- Evans, Chapter 2.
