---
layout: post
title: "11-06 Green's Functions for Laplace"
chapter: '11'
order: 6
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

> **Storytelling Hook:** Imagine tapping a taut drumhead at a single point with a needle—an idealized unit impulse $\delta_y(x)$. If you record the static equilibrium shape $G(x,y)$ produced by that single needle poke while keeping the rim clamped at zero, then by linearity you can immediately compute the equilibrium for *any* distributed force or *any* rim height simply by integrating against $G(x,y)$.

## Learning Objectives

This lesson introduces Green's functions for elliptic problems. Students should understand the fundamental solution, boundary correction, and the method of images as core tools for Laplace and Poisson problems.

## Prerequisites

Students should know Poisson's equation, the idea of a point source, and earlier Green's-function concepts from ODE or heat-kernel contexts.

## Background Knowledge Map: Impulse Response and Integral Representation

Green's functions unify boundary-value problems into a single integral operator built on four pillars:

1. **Fundamental Solution of $-\Delta$ on $\mathbb{R}^n$:** The free-space response $\Phi(x-y)$ satisfies $-\Delta_x \Phi(x-y) = \delta_y(x)$, taking the form $-\frac{1}{2\pi}\ln|x-y|$ in $\mathbb{R}^2$ and $\frac{1}{4\pi|x-y|}$ in $\mathbb{R}^3$.
2. **Corrector Function and Boundary Cancellation:** On a bounded or half-space domain $\Omega$, we write $G(x,y) = \Phi(x-y) - h_y(x)$, where the smooth harmonic corrector $h_y$ solves $\Delta_x h_y = 0$ in $\Omega$ with $h_y(x) = \Phi(x-y)$ on $\partial\Omega$, forcing $G(\cdot,y) = 0$ on $\partial\Omega$.
3. **Green's Second Identity and Representation Formula:** Applying $\int_\Omega (u\Delta v - v\Delta u)\,dx = \int_{\partial\Omega}(u\frac{\partial v}{\partial n} - v\frac{\partial u}{\partial n})\,dS$ to $u$ and $v = G(x,\cdot)$ expresses any solution of $-\Delta u = f$, $u|_{\partial\Omega} = g$ as $u(x) = \int_\Omega G(x,y)f(y)\,dy - \int_{\partial\Omega} g(y)\frac{\partial G}{\partial n_y}(x,y)\,dS_y$.
4. **Method of Images and Reciprocity Symmetry:** For highly symmetric domains (half-spaces, spheres), $h_y$ is built by placing a mirror charge outside $\Omega$. Moreover, $G(x,y) = G(y,x)$ always holds—the response at $x$ to a source at $y$ equals the response at $y$ to a source at $x$.

## Introduction

![Green's functions for Laplace equation]({{ site.imgurl }}/chapter_img/chapter11/06_greens_functions_laplace.svg)

Green's functions provide one of the most powerful ways to solve elliptic PDEs. Instead of solving directly for the full field, we first ask: what is the response to a point source? Once that response is known, more general sources and boundary data can be assembled from it.

This idea is one of the great unifying themes of mathematical physics. The solution of a complicated boundary-value problem is reconstructed from the response to idealized elementary inputs.

## Concept in Three Ways

### Intuitive View

A Green's function tells how the system reacts to a unit point source placed at one location. By adding up such responses, we recover the solution for a general source distribution.

### Visual View

The fundamental solution captures the raw point-source behavior, while the full Green's function adjusts that response so the boundary conditions are also satisfied.

### Formal View

For an elliptic operator, the Green's function is a kernel that converts the PDE into an integral representation. In Laplace and Poisson problems, it combines singular source behavior with boundary correction.

## Why Green's Functions Matter

Green's functions turn PDEs into integral formulas. This is powerful both analytically and conceptually: local differential structure is replaced by a global response kernel.

They also make source terms far more intuitive. Instead of treating a forcing term as an abstract function, we interpret it as a superposition of point-source effects.

## Common Misconceptions

### "The Green's function is just another explicit solution"

No. It is a response kernel that generates many solutions.

### "The fundamental solution already solves the boundary-value problem"

Not usually. Boundary correction is often required.

### "Green's functions only matter in highly advanced theory"

No. They are conceptually natural and practically useful even in introductory elliptic problems.

## Suggested Learning Path

### Step 1: Recall the point-source idea

Students should connect Green's functions to the notion of response to a localized input.

### Step 2: Distinguish fundamental solution from boundary-adjusted Green's function

This is the central conceptual distinction.

### Step 3: Use integral representation

Students should see how the kernel reconstructs the solution.

### Step 4: Introduce the method of images

This gives a concrete and memorable example of boundary correction.

### Checkpoints

- Can students explain what a Green's function means physically?
- Do they understand why the boundary usually forces correction beyond the raw fundamental solution?
- Can they describe how a source term is reconstructed from point-source responses?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Method of Images and the 3D Half-Space Poisson Kernel

Construct the Dirichlet Green's function $G(\mathbf{x},\mathbf{y})$ for the upper half-space $\mathbb{R}^3_+ = \{(x_1,x_2,x_3) : x_3 > 0\}$, derive its boundary Poisson kernel, and verify that the kernel integrates to $1$.

1. **Place the mirror image:** For a source at $\mathbf{y} = (y_1, y_2, y_3)$ with $y_3 > 0$, reflect across the plane $y_3 = 0$ to define the image point $\mathbf{y}^* = (y_1, y_2, -y_3) \notin \mathbb{R}^3_+$. Set:
   $$G(\mathbf{x},\mathbf{y}) = \frac{1}{4\pi|\mathbf{x}-\mathbf{y}|} - \frac{1}{4\pi|\mathbf{x}-\mathbf{y}^*|}.$$
2. **Verify boundary cancellation and PDE:** When $x_3 = 0$, $(x_3 - y_3)^2 = (-y_3)^2 = (x_3 + y_3)^2$, so $|\mathbf{x}-\mathbf{y}| = |\mathbf{x}-\mathbf{y}^*|$ and $G(\mathbf{x},\mathbf{y}) = 0$. Inside $\mathbb{R}^3_+$, $\mathbf{y}^*$ lies outside the domain, so $-\Delta_{\mathbf{x}} G(\mathbf{x},\mathbf{y}) = \delta_{\mathbf{y}}(\mathbf{x}) - 0 = \delta_{\mathbf{y}}(\mathbf{x})$.
3. **Compute the outward normal derivative on $y_3 = 0$:** The outward unit normal to $\mathbb{R}^3_+$ points downward, so $\frac{\partial}{\partial n_{\mathbf{y}}} = -\frac{\partial}{\partial y_3}$. Differentiating with respect to $y_3$:
   $$\frac{\partial}{\partial y_3}\Big(|\mathbf{x}-\mathbf{y}|^{-1}\Big) = \frac{x_3 - y_3}{|\mathbf{x}-\mathbf{y}|^3}, \qquad \frac{\partial}{\partial y_3}\Big(|\mathbf{x}-\mathbf{y}^*|^{-1}\Big) = \frac{-(x_3 + y_3)}{|\mathbf{x}-\mathbf{y}^*|^3}.$$
   Evaluating at $y_3 = 0$ (where both denominators equal $R^3$ with $R = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2 + x_3^2}$), the two terms add:
   $$P(\mathbf{x}; y_1, y_2) = -\frac{\partial G}{\partial n_{\mathbf{y}}}\bigg|_{y_3=0} = \frac{\partial G}{\partial y_3}\bigg|_{y_3=0} = \frac{1}{4\pi}\left(\frac{x_3}{R^3} - \frac{-x_3}{R^3}\right) = \frac{x_3}{2\pi\big((x_1-y_1)^2 + (x_2-y_2)^2 + x_3^2\big)^{3/2}}.$$
4. **Verify unit total mass (reproducing constant boundary data $g \equiv 1$):** Shift to polar coordinates $\rho = \sqrt{(y_1-x_1)^2 + (y_2-x_2)^2}$ on $\mathbb{R}^2$:
   $$\iint_{\mathbb{R}^2} P(\mathbf{x}; y_1, y_2)\,dy_1\,dy_2 = \frac{x_3}{2\pi}\int_0^{2\pi}\int_0^\infty \frac{\rho\,d\rho\,d\theta}{(\rho^2 + x_3^2)^{3/2}} = x_3\left[-\frac{1}{\sqrt{\rho^2 + x_3^2}}\right]_0^\infty = x_3\left(0 + \frac{1}{x_3}\right) = 1.$$

### Example 1: Fundamental Solution in Free Space

The free-space fundamental solution describes the response to a point source without boundary constraints.

### Example 2: Method of Images

In domains with simple boundaries, image sources can enforce boundary conditions by symmetry.

### Example 3: Poisson Representation

A distributed source can be represented by integrating the Green's function against the source density.

## Conceptual Questions

1. Why is a point-source response the right basic building block?
2. Why does the presence of a boundary require correction of the fundamental solution?
3. Why are Green's functions a natural bridge from differential equations to integral formulas?

## Application Problems

1. Why is the method of images so useful in electrostatics near flat boundaries?
2. How does a Green's function help solve Poisson's equation with distributed charge or heating?
3. Why do engineers and physicists often think in terms of impulse or point-source response?

## Interactive Teaching Strategies

- Use point-source pictures to motivate the whole method.
- Compare the free-space response with the boundary-corrected response.
- Reinforce the idea of PDE-to-integral conversion.
- Connect this lesson to earlier Green's-function and kernel ideas from the heat equation.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the physical meaning of point-source response before engaging more formal representations.

### Challenge for Advanced Students

Advanced students can explore symmetry-based image constructions and domain dependence of Green's functions.

## Summary

Green's functions convert elliptic problems into integral representations built from point-source responses. They are among the most powerful methods in classical potential theory and provide a conceptual bridge between sources, boundaries, and solutions.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Response to a point source
- Problem: We want to know how a concentrated source at one point influences the whole domain.
- Model: Green's function $$ G(x,\xi) $$ satisfies the PDE with a Dirac delta source.
- Assumptions and limitations: Linear problem, domain and boundary conditions known.
- Interpretation: Green's function is the impulse response of the elliptic operator.

#### Method of images in electrostatics
- Problem: Potential near a conducting plane can be computed by replacing boundary conditions with image charges.
- Model: Construct a Green's function adapted to the boundary.
- Assumptions and limitations: Special geometry, ideal boundary conditions.
- Interpretation: Green's functions turn boundary-value problems into integral representations.

### 2. Additional Intuition and Connections

For PDEs, Green's functions play a role very similar to transfer functions or impulse responses in ODEs and systems theory. A common misconception is that Green's functions are mysterious formulas; really they just encode how the system responds to a point source and then superposes those responses.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 1.0, 400)
G = x * (1 - 0.6) * (x <= 0.6) + 0.6 * (1 - x) * (x > 0.6)

plt.plot(x, G)
plt.xlabel("x")
plt.ylabel("G(x, 0.6)")
plt.title("1D Green function on [0,1]")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Greens function Laplace equation intuition
- search: method of images electrostatics animation
- search: Green function boundary value problem visualization

### 5. Worked Example

On $$ 0<x<1 $$ with homogeneous Dirichlet conditions, the Green function for $$ -u''=f $$ is
$$
G(x,\xi)=
\begin{cases}
x(1-\xi), & x\le \xi, \\
\xi(1-x), & x\ge \xi.
\end{cases}
$$
Then the solution is
$$ u(x)=\int_0^1 G(x,\xi)f(\xi)\,d\xi. $$
This compact example is an excellent first model for Green's function thinking before moving to two-dimensional domains.

### 6. Difficulty Layering

**Undergraduate level.** Understand Green's functions as kernels that build solutions from sources.

**Graduate level.** Connect to distributions, fundamental solutions, and boundary integral representations for elliptic operators.

## Video tham khảo

- xem trước: [Introducing Green's Functions for Partial Differential Equations (PDEs)](https://www.youtube.com/watch?v=xNqLZnM-PPY) — Faculty of Khan, English. Faculty of Khan builds a Green's function for a PDE.
- [mod08lec73 - The Poisson's Equation: Green's function solution](https://www.youtube.com/watch?v=hiHWwZb2AVU) — NPTEL-NOC IITM, English. The Green's function solution of Poisson's equation.
- [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, English. The point-source idea behind that kernel.

## References

- Evans, Chapter 2.
