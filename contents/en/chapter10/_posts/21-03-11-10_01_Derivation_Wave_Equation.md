---
layout: post
title: "10-01 Derivation of the Wave Equation"
chapter: '10'
order: 1
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: required
---

## Learning Objectives

This lesson derives the wave equation from force balance and elasticity. Students should understand how local restoring forces and inertia produce propagation, why the second derivative in time appears, and how the wave speed is determined by physical parameters.

## Prerequisites

Students should know Newton's second law, partial derivatives, and the basic idea of small-slope approximations. Some physical intuition about a stretched string is especially helpful.

## Introduction

![Derivation of the wave equation]({{ site.imgurl }}/chapter_img/chapter10/01_derivation_wave_equation.svg)

The wave equation is one of the most important PDEs in mathematics and physics. It describes vibrations of strings, sound waves in air, electromagnetic radiation, elastic oscillations, and many other propagation phenomena. What distinguishes it from the heat equation is that it preserves oscillatory behavior rather than smoothing it away.

Its derivation is a beautiful example of mathematical modeling. A stretched string experiences tension, and when displaced, small pieces of the string feel a restoring force due to curvature. Newton's law then turns that force balance into a second-order PDE.

## Concept in Three Ways

### Intuitive View

If a string is plucked, one part moves and pulls on neighboring parts through tension. That disturbance does not simply stay where it began. It propagates. The string's inertia resists immediate acceleration, while tension tries to restore alignment. The balance of these two effects creates wave motion.

### Visual View

A displaced string bends. Where curvature is large, the restoring force is large. Regions of positive curvature accelerate one way, regions of negative curvature accelerate the other. The motion travels along the string rather than merely decaying in place.

### Formal View

For a string displacement $$ u(x,t) $$ under constant tension $$ T $$ and linear density $$ \rho $$, the small-slope derivation leads to
$$ u_{tt}=c^2u_{xx}, $$
where
$$ c^2=\frac{T}{\rho}. $$
The coefficient $$ c $$ is the wave speed.

## Why the Derivation Matters

The wave equation is not just another PDE form to memorize. Its structure directly reflects the physics:

- the second time derivative represents inertia,
- the second space derivative represents curvature and restoring force,
- the constant $$ c $$ encodes propagation speed.

This makes the equation far more interpretable than a formula learned in isolation.

## Common Misconceptions

### "The wave equation is just like the heat equation with one derivative changed"

No. That single change completely alters the qualitative behavior. Heat diffuses; waves propagate.

### "The spatial second derivative is merely a technical artifact"

No. It measures curvature, which is precisely what determines the restoring force on the string.

### "Wave speed is arbitrary"

No. It is determined by material and geometric parameters through $$ c^2=T/\rho $$.

### "The derivation requires large deformations"

Quite the opposite. The classical derivation depends on the small-slope approximation.

## Suggested Learning Path

### Step 1: Isolate a small string segment

Students should identify the forces acting on a tiny piece of string.

### Step 2: Resolve the vertical force balance

The vertical component of the tension is what drives the motion.

### Step 3: Use the small-slope approximation

This simplifies the geometry and turns the force difference into curvature.

### Step 4: Apply Newton's law

Mass times acceleration equals net force, yielding the PDE.

### Checkpoints

- Can students explain why curvature creates restoring force?
- Do they understand why the second derivative in time appears?
- Can they interpret the wave speed physically?

## Worked Examples

### Example 1: Flat String

If $$ u(x,t)=0 $$, then both sides of the wave equation vanish. The equilibrium string is a trivial solution.

### Example 2: Separated Harmonic Motion

Functions of the form
$$ u(x,t)=\sin(kx)\cos(ckt) $$
solve the wave equation. This already shows the connection between spatial modes and temporal oscillation.

### Example 3: Speed Dependence

If the tension increases while the density stays fixed, then $$ c $$ increases. Waves travel faster on a tighter string.

## Conceptual Questions

1. Why does a curved string accelerate while a straight one does not?
2. Why is the second derivative in time natural for a vibration model?
3. How does the physical meaning of the wave equation differ from the heat equation?

## Application Problems

1. How does changing string tension affect the pitch of a musical instrument?
2. Why do lighter strings support faster wave propagation?
3. In what sense are sound and electromagnetic waves modeled by related mathematical structures?

## Interactive Teaching Strategies

- Have students sketch the force components on a tiny string segment.
- Compare the derivation structure with the heat equation derivation: both begin from balance laws, but the constitutive story is different.
- Use musical examples to make wave speed and frequency physically vivid.
- Ask students to explain in words why waves travel rather than merely spread out.

## Differentiation

### Support for Struggling Students

Students needing support should focus first on the geometry of the string segment and the meaning of curvature before handling the full algebra.

### Challenge for Advanced Students

Advanced students can explore higher-dimensional membranes, nonlinear corrections, or the role of characteristics.

## Summary

The wave equation is the basic model for oscillatory propagation. Its derivation reveals the balance between inertia and restoring force, and its coefficient $$ c $$ gives a direct physical interpretation of wave speed. It is one of the great model equations of mathematical physics.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Vibrating guitar string
- Problem: After a guitar string is plucked, the disturbance travels along the string at finite speed.
- Model:
$$ u_{tt}=c^2u_{xx}, \qquad c=\sqrt{\frac{T}{\rho}}. $$
- Assumptions and limitations: Thin string, constant tension, small slopes, no damping.
- Interpretation: Curvature produces restoring force, while inertia produces propagation rather than immediate smoothing.

#### Longitudinal elastic wave in a bar
- Problem: A mechanical pulse travels through a metal rod or a one-dimensional seismic approximation.
- Model: The same wave equation, with $$ u(x,t) $$ interpreted as longitudinal displacement.
- Assumptions and limitations: Linear elasticity, homogeneous material, small strain.
- Interpretation: The same PDE structure appears across many elastic media.

### 2. Additional Intuition and Connections

The wave equation differs from the heat equation because it preserves oscillatory behavior. The second time derivative encodes inertia, while the second space derivative encodes curvature and therefore restoring force. A common misconception is that waves and diffusion differ only cosmetically; in fact they belong to very different dynamical classes.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
u = np.exp(-120 * (x - 0.5) ** 2)
uxx = np.gradient(np.gradient(u, x), x)

plt.plot(x, u, label="initial displacement")
plt.plot(x, -uxx / np.max(np.abs(uxx)), label="acceleration proportional to -u_xx")
plt.xlabel("x")
plt.title("Curvature generates acceleration in the wave equation")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: vibrating string wave equation animation
- search: derivation wave equation small angle approximation
- search: elastic wave equation string force balance

### 5. Worked Example

Consider a string element of length $$ \Delta x $$. The difference of the vertical tension components gives
$$
T u_x(x+\Delta x,t)-T u_x(x,t)\approx T u_{xx}\Delta x.
$$
Newton's second law then gives
$$ \rho \Delta x\, u_{tt}=T u_{xx}\Delta x, $$
so
$$ u_{tt}=c^2u_{xx}, \qquad c^2=\frac{T}{\rho}. $$
Physically, greater tension makes waves faster, while greater density makes them slower.

### 6. Difficulty Layering

**Undergraduate level.** Understand how restoring force plus inertia leads to the wave equation.

**Graduate level.** Connect to multidimensional elasticity, hyperbolicity, and finite speed of propagation.

## References

- Evans, Chapter 2.
- Haberman, Chapter 4.
