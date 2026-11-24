---
layout: post
title: "09-06 Fundamental Solution and Green's Functions"
chapter: '09'
order: 6
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: required
---

Imagine touching an infinitely thin, infinitely hot needle to a cold wire at position $$ y $$ at time $$ t = 0 $$—injecting exactly one unit of thermal energy into a single mathematical point, $$ u(x, 0) = \delta(x - y) $$. An instant later, that singular spike blossoms into a smooth bell curve: $$ \Phi(x - y, t) = \frac{1}{\sqrt{4\pi\alpha t}} e^{-(x - y)^2 / (4\alpha t)} $$.

That bell curve is the **fundamental solution** (or free-space Green's function) of the heat equation. Once you know how a single point of heat spreads, linearity plus **Duhamel's Principle** lets you solve *any* initial-value problem, *any* half-line boundary problem (via the method of images), and *any* forced heat equation $$ u_t - \alpha u_{xx} = F(x, t) $$!

## Background Knowledge Map: The Heat Kernel, Images, and Duhamel's Principle

1. **Fundamental Solution $$ \Phi(x, t) $$ as an Approximate Identity:** For $$ t > 0 $$, $$ \Phi(x, t) > 0 $$, $$ \Phi_t = \alpha \Phi_{xx} $$, and $$ \int_{-\infty}^\infty \Phi(x, t)\,dx = 1 $$. As $$ t \to 0^+ $$, all its mass concentrates at $$ x = 0 $$, realizing $$ \delta(x) $$ in the sense of distributions.
2. **Method of Images for the Half-Line $$ x > 0 $$:** To enforce $$ u(0, t) = 0 $$ (Dirichlet) on $$ x > 0 $$, place an opposite "cold image" at $$ -y $$, yielding $$ G_D(x, y, t) = \Phi(x - y, t) - \Phi(x + y, t) $$. To enforce $$ u_x(0, t) = 0 $$ (Neumann), place an identical "warm image" at $$ -y $$, yielding $$ G_N(x, y, t) = \Phi(x - y, t) + \Phi(x + y, t) $$.
3. **Duhamel's Principle (Superposing Impulses Across Time):** A continuous source $$ F(x, t) $$ acts like a sequence of infinitesimal heat injections $$ F(y, \tau)\,d\tau $$ released at time $$ \tau $$ and diffused for the remaining time $$ t - \tau $$:
   $$ u_{\text{forced}}(x, t) = \int_0^t \int_{-\infty}^{\infty} G(x, y, t - \tau) F(y, \tau)\,dy\,d\tau. $$
4. **Probabilistic Interpretation (Brownian Motion):** $$ \Phi(x - y, t) $$ is literally the transition probability density of a 1D Brownian particle starting at $$ y $$ and reaching $$ x $$ after time $$ t $$ with diffusion constant $$ D = \alpha $$!

### Step-by-Step Worked Example (Read Slowly): Method of Images on the Half-Line $$ x > 0 $$ with $$ u(0, t) = 0 $$

**Problem:** Construct the Dirichlet Green's function $$ G_D(x, y, t) $$ for $$ u_t = \alpha u_{xx} $$ on $$ x > 0 $$ with $$ u(0, t) = 0 $$, verify the boundary condition and PDE, and use it to solve for constant initial temperature $$ u(x, 0) = T_0 $$ ($$ x > 0 $$).

1. **Write the method-of-images Green's function:**
   $$ G_D(x, y, t) = \frac{1}{\sqrt{4\pi\alpha t}}\left[\exp\!\left(-\frac{(x - y)^2}{4\alpha t}\right) - \exp\!\left(-\frac{(x + y)^2}{4\alpha t}\right)\right]. $$
   Check BC at $$ x = 0 $$: $$ (-y)^2 = (+y)^2 \implies G_D(0, y, t) = 0 $$ identically for all $$ y > 0, t > 0 $$!
2. **Integrate against $$ f(y) = T_0 $$ on $$ (0, \infty) $$:**
   $$ u(x, t) = \frac{T_0}{\sqrt{4\pi\alpha t}}\left[\int_0^\infty e^{-\frac{(x - y)^2}{4\alpha t}}\,dy - \int_0^\infty e^{-\frac{(x + y)^2}{4\alpha t}}\,dy\right]. $$
3. **Change variables cleanly in both integrals:**
   - First integral: set $$ s = \frac{y - x}{\sqrt{4\alpha t}} $$ ($$ dy = \sqrt{4\alpha t}\,ds $$); limits $$ y \in [0, \infty) $$ map to $$ s \in \left[-\frac{x}{\sqrt{4\alpha t}}, \infty\right) $$.
   - Second integral: set $$ s = \frac{y + x}{\sqrt{4\alpha t}} $$; limits map to $$ s \in \left[\frac{x}{\sqrt{4\alpha t}}, \infty\right) $$.
   Subtracting cancels the entire tail $$ \left[\frac{x}{\sqrt{4\alpha t}}, \infty\right) $$, leaving only the symmetric center!
   $$ u(x, t) = \frac{T_0}{\sqrt{\pi}} \int_{-\frac{x}{\sqrt{4\alpha t}}}^{\frac{x}{\sqrt{4\alpha t}}} e^{-s^2}\,ds = T_0\,\operatorname{erf}\!\left(\frac{x}{\sqrt{4\alpha t}}\right). $$
4. **Physical sanity check:** At $$ x = 0 $$, $$ \operatorname{erf}(0) = 0 $$; as $$ x \to \infty $$, $$ \operatorname{erf}(\infty) = 1 \implies u \to T_0 $$; and as $$ t \to 0^+ $$ for any fixed $$ x > 0 $$, $$ \frac{x}{\sqrt{4\alpha t}} \to \infty \implies u \to T_0 $$. (Lord Kelvin famously used this exact $$ \operatorname{erf} $$ formula in 1862 to estimate the cooling age of the Earth!)

## Learning Objectives

This lesson introduces the heat kernel and the role of Green's functions. Students should understand the fundamental solution as the response to point-source initial data and see how general solutions arise by superposition.

## Prerequisites

Students should know the heat equation on the whole line and have some familiarity with transform methods and the idea of Green's functions from ODE or boundary-value settings.

## Introduction

![Fundamental solution and Green's functions]({{ site.imgurl }}/chapter_img/chapter09/06_fundamental_solution_greens_functions.svg)

Among the most beautiful objects in PDE theory is the fundamental solution of the heat equation, also called the heat kernel. It describes how a point-source concentration of heat spreads out over time. Once this response is known, more general initial data can be handled by superposition.

This is one of the moments where PDE theory becomes conceptually elegant. A complicated solution can be built by integrating point-source responses against the initial profile.

## Concept in Three Ways

### Intuitive View

If all the heat is initially concentrated at one point, diffusion immediately spreads it into a bell-shaped profile. That profile is the basic building block from which many other solutions can be constructed.

### Visual View

The kernel starts sharply concentrated and then broadens while lowering in amplitude. The total mass is preserved, but it becomes distributed over a wider region.

### Formal View

The fundamental solution of the one-dimensional heat equation is
$$
G(x,t)=\frac{1}{\sqrt{4\pi \alpha^2 t}}\exp\left(-\frac{x^2}{4\alpha^2 t}\right),
$$
for $$ t>0 $$. If the initial data are $$ u(x,0)=f(x) $$, then the solution is given by convolution:
$$ u(x,t)=\int_{-\infty}^{\infty} G(x-y,t)f(y)\,dy. $$

## Why the Kernel Matters

The heat kernel captures the essential behavior of diffusion in one explicit formula. It shows positivity, smoothing, spreading, and mass preservation all at once.

It also provides the simplest and most powerful example of a Green's-function representation for a PDE.

## Common Misconceptions

### "The fundamental solution is just one special explicit example"

No. It is the core building block for the whole solution theory on the line.

### "A point source is physically unrealistic, so the kernel is not important"

Wrong. Point sources are idealized, but they generate the superposition principle for general data.

### "The kernel only spreads outward; it does not preserve anything"

No. It preserves total mass while changing the shape.

## Suggested Learning Path

### Step 1: Motivate the point-source problem

Students should understand why a localized source is the most basic response to study.

### Step 2: Present the heat kernel

The Gaussian form should be emphasized visually and conceptually.

### Step 3: Build general solutions by convolution

This is the main structural step of the lesson.

### Step 4: Interpret the properties

Mass preservation, smoothing, and positivity should all be highlighted.

### Checkpoints

- Can students explain why the kernel is Gaussian?
- Do they understand how convolution builds general solutions?
- Can they identify the key qualitative features encoded by the kernel?

## Worked Examples

### Example 1: Point Source

The fundamental solution itself describes the evolution of a unit point source of heat.

### Example 2: Localized Bump Initial Data

The solution is obtained by averaging shifted kernels against the initial bump, producing a broader and smoother profile over time.

### Example 3: Conservation of Total Heat

Integrating the kernel over space gives 1, showing that the total mass of heat is preserved.

## Conceptual Questions

1. Why is the heat kernel Gaussian?
2. Why does convolution represent superposition of point-source responses?
3. Why is mass preservation consistent with diffusion?

## Application Problems

1. Why is the heat kernel a natural model of uncertainty spreading in probability?
2. How does the width of the Gaussian reflect the strength of diffusion?
3. Why is a Green's-function representation useful in PDE theory?

## Interactive Teaching Strategies

- Plot the Gaussian kernel at several times.
- Have students interpret each part of the formula qualitatively.
- Reinforce the idea that Green's functions are response kernels.
- Compare convolution here with earlier ODE Green's-function ideas.

## Differentiation

### Support for Struggling Students

Students needing support should focus first on the picture of a point source spreading into a Gaussian profile before working with convolution integrals.

### Challenge for Advanced Students

Advanced students can explore kernel derivations via Fourier transform and higher-dimensional generalizations.

## Summary

The heat kernel is one of the most important explicit solutions in PDE. It encodes diffusion, smoothing, and the propagation of initial data, and it provides the Green's-function framework for general whole-line heat solutions.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Instantaneous point source
- Problem: A pulse of heat is placed at a single point and allowed to diffuse.
- Model:
$$ u(x,t)=G(x,t)*u_0(x). $$
- Assumptions and limitations: Linear system and appropriate domain or Green's function.
- Interpretation: The fundamental solution is the heat equation's fingerprint in response to a point impulse.

#### Building general solutions from Green's functions
- Problem: An arbitrary initial state is reconstructed from point-source responses.
- Model:
$$ u(x,t)=\int_{\mathbb{R}}G(x-\xi,t)u_0(\xi)\,d\xi. $$
- Assumptions and limitations: The initial data are integrable or otherwise well behaved.
- Interpretation: The current temperature is a Gaussian-weighted average of the initial data.

### 2. Additional Intuition and Connections

The fundamental solution for the heat equation plays the role of a Green's function in space-time. A common pitfall is to see the kernel only as a formula. It actually encodes smoothing, mass conservation, and the infinite-speed propagation characteristic of diffusion models.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 800)
t = 0.2
G = (1 / np.sqrt(4 * np.pi * t)) * np.exp(-x**2 / (4 * t))

plt.plot(x, G)
plt.xlabel("x")
plt.ylabel("G")
plt.title("Fundamental solution of the heat equation")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: heat kernel Green function animation
- search: fundamental solution heat equation Gaussian
- search: convolution with heat kernel visualization

### 5. Worked Example

If
$$ u_0(x)=\mathbf{1}_{[-1,1]}(x), $$
then
$$ u(x,t)=\int_{-1}^{1}G(x-\xi,t)\,d\xi. $$
This shows explicitly how a box-shaped initial profile becomes instantly smooth for every $$ t>0 $$.

### 6. Difficulty Layering

**Undergraduate level.** Use the convolution formula and interpret the point-source solution.

**Graduate level.** Connect to semigroup theory, immediate regularization, and Green's functions on bounded domains.

## Video tham khảo

- xem trước: [Introducing Green's Functions for Partial Differential Equations (PDEs)](https://www.youtube.com/watch?v=xNqLZnM-PPY) — Faculty of Khan, English. Faculty of Khan introduces the Green's function for a PDE.
- [Solving the Heat Equation with the Fourier Transform](https://www.youtube.com/watch?v=7haZCrQDHpA) — Steve Brunton, English. The Gaussian fundamental solution appears as the inverse transform of the heat multiplier.
- [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, English. A point source and the response that is the fundamental solution.

## References

- Evans, Chapter 2.
