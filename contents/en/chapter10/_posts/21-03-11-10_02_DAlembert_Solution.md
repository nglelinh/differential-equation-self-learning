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

## References

- Evans, Chapter 2.
