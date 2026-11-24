---
layout: post
title: "10-02 d'Alembert's Solution"
chapter: '10'
order: 2
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: required
---

Before Fourier series even existed, Jean le Rond d'Alembert factored the 1D wave operator like a difference of squares: $$ \partial_{tt} - c^2 \partial_{xx} = (\partial_t - c\partial_x)(\partial_t + c\partial_x) = 0 $$. That single algebraic factorization revealed a breathtaking geometric truth: on an infinite string, *every* solution is just the sum of one rigid shape sliding right at speed $$ c $$ and another rigid shape sliding left at speed $$ c $$, $$ u(x, t) = F(x - ct) + G(x + ct) $$!

Even more profoundly, d'Alembert's formula introduces the relativistic-looking geometry of **characteristics**, **domains of dependence**, and **ranges of influence**—proving that disturbances in the wave equation strictly obey a finite speed limit $$ c $$.

## Background Knowledge Map: Characteristics, Causality, and d'Alembert's Formula

1. **Characteristic Coordinates ($$ \xi = x - ct, \eta = x + ct $$):** Changing variables from $$ (x, t) $$ to the moving wave frames $$ (\xi, \eta) $$ collapses $$ u_{tt} - c^2 u_{xx} = 0 $$ into the trivial mixed-derivative PDE $$ u_{\xi\eta} = 0 $$, whose general solution is immediately $$ F(\xi) + G(\eta) $$.
2. **D'Alembert's Closed-Form Cauchy Solution:** Matching $$ u(x, 0) = f(x) $$ and $$ u_t(x, 0) = g(x) $$ gives
   $$ u(x, t) = \frac{1}{2}\bigl[f(x - ct) + f(x + ct)\bigr] + \frac{1}{2c}\int_{x - ct}^{x + ct} g(s)\,ds. $$
   An initial displacement splits cleanly into two half-height twins racing left and right; an initial velocity creates a flat-topped expanding plateau!
3. **Domain of Dependence & Finite Speed of Propagation:** The value $$ u(x_0, t_0) $$ depends *only* on initial data inside the closed interval $$ [x_0 - c t_0, x_0 + c t_0] $$. Nothing happening outside that light-cone base can influence $$ (x_0, t_0) $$!
4. **Persistence of Singularities:** Unlike the heat equation, d'Alembert's formula does *not* smooth away corners or kinks—they travel intact along the characteristic lines $$ x \pm ct = \text{const} $$ forever.

### Step-by-Step Worked Example (Read Slowly): Tracking a Pluck + Hammer Impulse via d'Alembert's Formula

**Problem:** An infinite string with wave speed $$ c = 2 $$ starts with zero initial displacement $$ f(x) = 0 $$ and localized boxcar initial velocity $$ g(x) = 4 $$ for $$ |x| < 1 $$ and $$ g(x) = 0 $$ for $$ |x| > 1 $$. Use d'Alembert's formula to compute the exact string displacement $$ u(x, t) $$ at $$ t = 1 $$ for $$ x = 0, 2, 4 $$, and sketch the expanding plateau!

1. **Simplify d'Alembert's formula for $$ f \equiv 0, c = 2 $$:**
   $$ u(x, t) = \frac{1}{2(2)}\int_{x - 2t}^{x + 2t} g(s)\,ds = \frac{1}{4}\int_{x - 2t}^{x + 2t} g(s)\,ds. $$
   Notice $$ u(x, t) $$ is simply $$ \frac{1}{4} $$ times the area of the boxcar $$ g(s) $$ (height $$ 4 $$, support $$ [-1, 1] $$) lying inside the domain of dependence $$ [x - 2t, x + 2t] $$!
2. **Evaluate at $$ t = 1 $$ (so the integration window has width $$ 4 $$: $$ [x - 2, x + 2] $$):**
   - **At $$ x = 0 $$:** Window is $$ [-2, 2] $$, which completely swallows $$ [-1, 1] $$ (overlap length $$ 2 $$):
     $$ u(0, 1) = \frac{1}{4}\int_{-1}^{1} 4\,ds = \frac{1}{4}(8) = 2. $$
   - **At $$ x = 2 $$:** Window is $$ [0, 4] $$, whose overlap with $$ [-1, 1] $$ is $$ [0, 1] $$ (overlap length $$ 1 $$):
     $$ u(2, 1) = \frac{1}{4}\int_{0}^{1} 4\,ds = \frac{1}{4}(4) = 1. $$
   - **At $$ x = 4 $$:** Window is $$ [2, 6] $$, completely disjoint from $$ [-1, 1] $$ (overlap length $$ 0 $$):
     $$ u(4, 1) = 0. $$
3. **Physical wake insight:** Notice that even after the wavefront has passed $$ x = 0 $$ (for all $$ t > \frac{1}{2} $$), $$ u(0, t) = 2 $$ stays permanently lifted! In 1D, a velocity impulse leaves behind a permanent wake—a striking contrast with 3D sound waves (Huygens' principle)!

## Learning Objectives

This lesson introduces d'Alembert's formula for the one-dimensional wave equation on the whole line. Students should understand traveling waves, left- and right-moving components, and the role of characteristics.

## Prerequisites

Students should know the derivation of the wave equation and be comfortable with partial derivatives and basic coordinate changes.

## Introduction

![d'Alembert solution]({{ site.imgurl }}/chapter_img/chapter10/02_dalembert_solution.svg)

One of the most elegant explicit formulas in PDE theory is d'Alembert's solution of the one-dimensional wave equation on the whole line. It shows that wave motion can be understood as a superposition of profiles traveling left and right without changing shape.

This formula immediately distinguishes wave propagation from diffusion. Instead of smoothing out a profile, the wave equation transports information at finite speed.

## Concept in Three Ways

### Intuitive View

If a string is displaced locally, the disturbance splits and travels outward in opposite directions. Each part carries the initial information along the string.

### Visual View

An initial bump does not merely broaden. It breaks into translated copies moving at speed $$ c $$ to the left and right.

### Formal View

For the wave equation
$$ u_{tt}=c^2u_{xx}, $$
the solution with suitable initial data can be written in d'Alembert form as a combination of left- and right-moving waves. The formula expresses the solution directly in terms of translated initial profiles.

## Why d'Alembert's Formula Matters

This solution is one of the clearest demonstrations of finite propagation speed. It shows that disturbances move along characteristic directions rather than influencing the entire domain instantly.

It also provides a conceptual model for more advanced wave theory: transport, characteristics, and propagation of signals are fundamental ideas far beyond this one formula.

## Common Misconceptions

### "Wave propagation means every point feels the disturbance immediately"

No. The wave equation has finite propagation speed.

### "The profile must decay as it moves"

Not in the undamped whole-line model. The traveling pieces preserve shape.

### "d'Alembert's formula is just a special trick"

No. It expresses the essential transport structure of the one-dimensional wave equation.

## Suggested Learning Path

### Step 1: Introduce the characteristic variables

Students should see why the combinations $$ x-ct $$ and $$ x+ct $$ are natural.

### Step 2: Derive the traveling-wave form

This reveals the left- and right-moving decomposition.

### Step 3: Incorporate initial data

The explicit formula becomes meaningful when matched to displacement and velocity data.

### Step 4: Interpret finite propagation

This is one of the central conceptual outcomes.

### Checkpoints

- Can students explain why traveling profiles naturally solve the wave equation?
- Do they understand the roles of left- and right-moving pieces?
- Can they describe finite propagation speed clearly?

## Worked Examples

### Example 1: Pure Traveling Wave

A function of the form $$ f(x-ct) $$ is a right-moving wave, while $$ g(x+ct) $$ is left-moving.

### Example 2: Initial Bump

An initially localized displacement splits into two traveling pieces moving in opposite directions.

### Example 3: Zero Initial Velocity

When the initial velocity is zero, the left- and right-moving parts are balanced symmetrically.

## Conceptual Questions

1. Why do the variables $$ x\pm ct $$ arise naturally in the wave equation?
2. Why does d'Alembert's formula demonstrate finite propagation speed?
3. Why is wave transport fundamentally different from diffusion?

## Application Problems

1. Why does a plucked string send disturbances in two directions?
2. How does finite propagation speed matter in acoustics?
3. Why is the one-dimensional wave equation a transport model as much as an oscillation model?

## Interactive Teaching Strategies

- Use diagrams of moving pulses to illustrate the formula.
- Ask students to predict what happens to a localized bump after a short time.
- Compare d'Alembert propagation with diffusive spreading.
- Reinforce the language of characteristics and finite signal speed.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the picture of left- and right-moving waves before handling the explicit formula in full detail.

### Challenge for Advanced Students

Advanced students can connect d'Alembert's formula to characteristic coordinates and later hyperbolic PDE theory.

## Summary

d'Alembert's formula gives one of the clearest explicit PDE solutions in mathematics. It shows that wave motion is fundamentally transport of profiles with finite speed, and it provides a template for understanding propagation more generally.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Pulse on an infinite string
- Problem: A localized initial displacement on an infinite string splits and travels away from its source.
- Model:
$$
u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.
$$
- Assumptions and limitations: Infinite domain, constant wave speed, no boundaries.
- Interpretation: Initial data moves without changing shape in the idealized setting.

#### Electrical signal on a lossless transmission line
- Problem: Voltage along a long cable can be approximated by left-moving and right-moving waves.
- Model: After normalization, the voltage satisfies a one-dimensional wave equation with d'Alembert form.
- Assumptions and limitations: Negligible resistance and losses, uniform line parameters.
- Interpretation: d'Alembert's formula is fundamental in both mechanics and electrical engineering.

### 2. Additional Intuition and Connections

d'Alembert's formula shows that initial data does not instantly disperse; it splits into pieces moving left and right. This makes finite propagation speed completely explicit, in sharp contrast with the immediate smoothing effect of the heat equation.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 800)

for t in [0.0, 0.8, 1.6]:
    u = 0.5 * np.exp(-((x - t) + 1.5) ** 2) + 0.5 * np.exp(-((x + t) + 1.5) ** 2)
    plt.plot(x, u, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("An initial pulse splitting into two traveling waves")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: dAlembert solution animation pulse splitting
- search: transmission line lossless wave equation
- search: finite propagation speed wave equation

### 5. Worked Example

If the initial velocity is zero and the initial displacement is
$$ u(x,0)=e^{-x^2}, $$
then
$$
u(x,t)=\frac{1}{2}e^{-(x-ct)^2}+\frac{1}{2}e^{-(x+ct)^2}.
$$
A symmetric initial pulse splits into two identical pulses traveling in opposite directions. This is the standard physical picture for waves on an infinite string.

### 6. Difficulty Layering

**Undergraduate level.** Understand how initial data generates left-moving and right-moving waves.

**Graduate level.** Connect to fundamental solutions of hyperbolic operators and domains of dependence.

## Video tham khảo

- xem trước: [PDE 10 | Wave equation: d'Alembert's formula](https://www.youtube.com/watch?v=j2G91naZ8bo) — commutant, English. commutant derives d'Alembert's formula for the infinite string.
- [D'Alembert Solution to the Wave Equation](https://www.youtube.com/watch?v=Sc21aPg2RyE) — Faculty of Khan, English. Faculty of Khan on the same d'Alembert solution.
- [The Method of Characteristics and the Wave Equation](https://www.youtube.com/watch?v=eI2x99SxJgU) — Steve Brunton, English. The method of characteristics, which is where d'Alembert's formula comes from.

## References

- Evans, Chapter 2.
