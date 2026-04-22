---
layout: post
title: "11-03 Laplace's Equation in Polar Coordinates"
chapter: '11'
order: 3
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

## Learning Objectives

This lesson solves Laplace's equation on circular domains using polar coordinates. Students should understand why coordinate adaptation matters and how radial-angular separation works.

## Prerequisites

Students should know Laplace's equation, the basics of polar coordinates, and separation of variables in rectangular domains.

## Introduction

![Laplace equation in polar coordinates]({{ site.imgurl }}/chapter_img/chapter11/03_laplace_polar_coordinates.svg)

Rectangles are not the only natural domains in elliptic PDEs. Many important problems occur in disks, annuli, or radially symmetric settings. In such cases, Cartesian coordinates obscure the geometry, while polar coordinates reveal it immediately.

This lesson shows one of the most important principles in PDE analysis: choose coordinates that respect the domain symmetry. When the geometry is circular, polar coordinates turn the structure of Laplace's equation into something far more transparent.

## Concept in Three Ways

### Intuitive View

If the domain is circular, it makes sense to measure position by distance from the center and angle around the center rather than by horizontal and vertical coordinates.

### Visual View

The solution can be understood as a combination of radial behavior and angular oscillation. Different angular harmonics describe different rotational patterns.

### Formal View

In polar coordinates, Laplace's equation becomes
$$
u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}=0.
$$
Separation of variables then leads to coupled radial and angular ODEs whose solutions reflect circular symmetry.

## Why Polar Coordinates Matter

This lesson highlights that PDE difficulty often depends on coordinate choice. A poor coordinate system can hide the symmetry of the problem, while a natural one can make the structure almost inevitable.

It also introduces the first serious example where angular harmonic structure becomes central.

## Common Misconceptions

### "Changing coordinates only changes notation"

No. It can fundamentally change how transparent the solution structure becomes.

### "Polar coordinates are only for radial solutions"

No. They also support angularly varying solutions through harmonic angular modes.

### "Laplace's equation in polar form is just a harder version of the Cartesian case"

Not really. In circular domains, it is often the natural and simpler version.

## Suggested Learning Path

### Step 1: Motivate the coordinate change geometrically

Students should see why circular domains suggest polar coordinates.

### Step 2: Write the polar Laplacian

This is the key structural formula of the lesson.

### Step 3: Separate radial and angular dependence

The angular equation reveals harmonic periodicity, while the radial equation reveals growth or decay structure.

### Step 4: Interpret circular-domain solutions

Students should connect the formulas back to disks and annuli.

### Checkpoints

- Can students explain why polar coordinates are natural in circular domains?
- Do they understand the role of the angular mode number?
- Can they distinguish radial and angular contributions to the solution?

## Worked Examples

### Example 1: Purely Radial Harmonic Function

A radial solution depends only on $$ r $$ and gives a simple first illustration of the polar Laplacian.

### Example 2: Angular Harmonic Mode

Nontrivial angular dependence leads to trigonometric functions in $$ \theta $$ and power-type radial behavior.

### Example 3: Disk Boundary Data

Boundary data prescribed around a circle can be expanded in angular harmonics and extended inward by radial factors.

## Conceptual Questions

1. Why is the coordinate system part of the mathematics, not just the notation?
2. What does the angular mode number mean geometrically?
3. Why do circular domains naturally lead to polar harmonic expansions?

## Application Problems

1. Why are electrostatic problems in disks naturally treated in polar coordinates?
2. How does radial symmetry simplify elliptic PDE analysis?
3. Why do angular Fourier modes appear naturally in circular geometry?

## Interactive Teaching Strategies

- Compare the same circular-domain problem in Cartesian and polar coordinates conceptually.
- Use sketches of disks and angular modes.
- Emphasize the phrase "coordinates adapted to symmetry."
- Connect angular harmonics here to earlier Fourier-series ideas.

## Differentiation

### Support for Struggling Students

Students needing support should begin with radial-only solutions before adding angular dependence.

### Challenge for Advanced Students

Advanced students can study annular domains or connect polar harmonic expansions with complex-variable methods.

## Summary

Polar coordinates expose the symmetry of circular domains and make Laplace's equation far more transparent in those settings. The lesson shows how geometry, coordinates, and harmonic structure interact in elliptic PDEs.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Temperature around a cylindrical pipe
- Problem: We want the steady temperature field around a long circular pipe.
- Model:
$$
u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}=0.
$$
- Assumptions and limitations: Axial symmetry, steady state, ideal circular geometry.
- Interpretation: Polar coordinates match the symmetry and simplify the PDE.

#### Electric potential near a circular electrode
- Problem: Potential in a disk or annulus is naturally described in polar coordinates.
- Model: Laplace's equation in polar coordinates.
- Assumptions and limitations: No charge in the domain.
- Interpretation: Angular modes $$ \cos(n\theta) $$ and $$ \sin(n\theta) $$ encode the boundary symmetry.

### 2. Additional Intuition and Connections

Changing coordinates does not change the physics, but it can expose the underlying symmetry. A common pitfall is to remain in Cartesian coordinates too long and miss a much simpler formulation in circular geometry.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 1, 160)
theta = np.linspace(0, 2 * np.pi, 240)
R, Theta = np.meshgrid(r, theta)
U = R * np.cos(Theta)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

plt.contourf(X, Y, U, levels=20, cmap="coolwarm")
plt.colorbar(label="u")
plt.axis("equal")
plt.title("Harmonic solution in the disk: u(r,theta)=r cos(theta)")
plt.show()
```

### 4. Suggested Searches

- search: Laplace equation polar coordinates disk solution
- search: harmonic function disk boundary data animation
- search: electrostatic potential circular domain

### 5. Worked Example

In the unit disk, if the boundary data is
$$ u(1,\theta)=\cos\theta, $$
then the harmonic extension is
$$ u(r,\theta)=r\cos\theta. $$
This classical example shows how the first angular mode on the boundary propagates inward with a factor of $$ r $$.

### 6. Difficulty Layering

**Undergraduate level.** Recognize when polar coordinates are the natural choice.

**Graduate level.** Connect to the Poisson kernel on the disk and Fourier representations of harmonic functions.

## References

- Evans, Chapter 2.
