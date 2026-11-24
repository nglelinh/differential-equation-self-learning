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

> **Storytelling Hook:** Try imposing boundary temperatures around a circular silicon wafer using Cartesian $(x,y)$ coordinates and the boundary $x^2 + y^2 = R^2$ couples $x$ and $y$ inextricably. Switch to polar coordinates $(r,\theta)$, and the geometry clicks into place: the angular direction wraps around smoothly with $2\pi$-periodicity, while the radial direction obeys a classic Euler–Cauchy equation whose power laws $r^n$ filter out every boundary ripple as you approach the center.

## Learning Objectives

This lesson solves Laplace's equation on circular domains using polar coordinates. Students should understand why coordinate adaptation matters and how radial-angular separation works.

## Prerequisites

Students should know Laplace's equation, the basics of polar coordinates, and separation of variables in rectangular domains.

## Background Knowledge Map: Circular Symmetry and Polar Potential Theory

Mastering Laplace's equation on disks, annuli, and wedges relies on four structural pillars:

1. **Curvilinear Laplacian and Area Scaling:** Transforming $\Delta u = u_{xx} + u_{yy}$ to $(r,\theta)$ produces $u_{rr} + \frac{1}{r}u_r + \frac{1}{r^2}u_{\theta\theta} = 0$. The factor $1/r$ reflects the circumference $2\pi r$ growing linearly with radius, while $1/r^2$ converts angular change into arc length.
2. **Periodicity on $S^1$ and Full Fourier Series:** On a full disk or annulus, there are no side walls in $\theta$; instead, single-valuedness demands $u(r,\theta+2\pi) = u(r,\theta)$, yielding integer angular modes $\cos(n\theta)$ and $\sin(n\theta)$ ($n \ge 0$).
3. **Euler–Cauchy Radial Solutions and Regularity at the Origin:** Separating variables gives $r^2 R'' + r R' - n^2 R = 0$, whose solutions are $r^n$ and $r^{-n}$ (for $n \ge 1$), and $1, \ln r$ (for $n=0$). On an interior disk containing $r=0$, boundedness discards $r^{-n}$ and $\ln r$; on an exterior domain ($r > a$), decay at infinity discards $r^n$.
4. **Poisson's Integral Formula as a Geometric Kernel:** Summing the polar Fourier series in closed form yields $u(r,\theta) = \frac{1}{2\pi}\int_0^{2\pi} \frac{a^2 - r^2}{a^2 - 2ar\cos(\theta-\phi) + r^2} f(\phi)\,d\phi$, turning infinite series into a single positive averaging kernel.

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


### Step-by-Step Worked Example (Read Slowly): Solving the Disk Dirichlet Problem and Verifying Directly

Find the bounded harmonic function $u(r,\theta)$ on the disk $r < 2$ satisfying the boundary condition $u(2,\theta) = 4 + 6\cos(2\theta) - 2\sin(3\theta)$, and verify directly that the resulting formula satisfies the polar Laplace equation.

1. **Write the general bounded polar series on $r < a$ (here $a = 2$):** Rejecting the singular radial modes $\ln r$ and $r^{-n}$ at $r=0$ leaves:
   $$u(r,\theta) = A_0 + \sum_{n=1}^{\infty} \left(\frac{r}{2}\right)^n \big(A_n \cos(n\theta) + B_n \sin(n\theta)\big).$$
2. **Match boundary modes at $r = 2$:** Setting $r = 2$ makes $(r/2)^n = 1$, so we read off the Fourier coefficients directly:
   $$A_0 = 4, \qquad A_2 = 6, \qquad B_3 = -2,$$
   with all other $A_n, B_n = 0$.
3. **Assemble the explicit solution:**
   $$u(r,\theta) = 4 + 6\left(\frac{r}{2}\right)^2\cos(2\theta) - 2\left(\frac{r}{2}\right)^3\sin(3\theta) = 4 + \frac{3}{2}r^2\cos(2\theta) - \frac{1}{4}r^3\sin(3\theta).$$
4. **Verify the polar PDE on the $n=2$ mode $v(r,\theta) = \frac{3}{2}r^2\cos(2\theta)$:**
   $$v_r = 3r\cos(2\theta), \qquad v_{rr} = 3\cos(2\theta), \qquad v_{\theta\theta} = -6r^2\cos(2\theta).$$
   Substituting into the polar Laplacian gives:
   $$v_{rr} + \frac{1}{r}v_r + \frac{1}{r^2}v_{\theta\theta} = 3\cos(2\theta) + 3\cos(2\theta) - 6\cos(2\theta) = 0.$$
5. **Check the center value:** Evaluating at $r = 0$ yields $u(0,\theta) = 4$, which equals $\frac{1}{2\pi}\int_0^{2\pi} u(2,\theta)\,d\theta = 4$—confirming the Mean Value Property in one glance.

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

## Video tham khảo

- xem trước: [Laplace PDE on circular domain solved in polar coordinates](https://www.youtube.com/watch?v=Yybsq8qiK9I) — Daniel An, English. Laplace's equation on a disk, solved in polar coordinates.
- [10.1 General solution to Laplace's equation in polar coordinates](https://www.youtube.com/watch?v=fNSMMy9Q8Ls) — Daniel Nino, English. The general polar solution, including the logarithmic term.
- [The Laplacian in Polar Coordinates](https://www.youtube.com/watch?v=wlbZxa66ncg) — Mike, the Mathematician, English. The Laplacian written in polar coordinates before separation.

## References

- Evans, Chapter 2.
