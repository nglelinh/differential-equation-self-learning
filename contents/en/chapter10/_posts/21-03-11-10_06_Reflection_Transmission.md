---
layout: post
title: "10-06 Reflection and Transmission"
chapter: '10'
order: 6
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: required
---

## Learning Objectives

This lesson studies how waves respond to boundaries and interfaces. Students should understand reflection, transmission, and the role of impedance mismatch or boundary constraints.

## Prerequisites

Students should know traveling-wave ideas, basic bounded-domain wave behavior, and the interpretation of wave speed in different media.

## Introduction

![Reflection and transmission]({{ site.imgurl }}/chapter_img/chapter10/06_reflection_transmission.svg)

When a wave encounters a boundary or a change in medium, it does not simply continue unchanged. Part of the wave may reflect, part may transmit, and the exact behavior depends on the physical matching conditions at the interface.

This is one of the most tangible wave phenomena in physics. Echoes, partial reflections, and transmitted signals all arise from this same mathematical structure.

## Concept in Three Ways

### Intuitive View

If a traveling pulse hits a boundary, it may bounce back. If it hits a new material, one part may continue forward while another part returns. The medium influences how much energy goes each way.

### Visual View

At an interface, the wave may split into reflected and transmitted pieces. Their amplitudes and shapes depend on continuity and flux-like matching conditions.

### Formal View

Reflection and transmission are described by solving the wave equation separately on each side of an interface and imposing compatibility conditions. These conditions determine the reflected and transmitted amplitudes.

## Why the Topic Matters

Reflection and transmission show how waves interact with structure. The wave is not only governed by a PDE in the bulk, but also by matching laws at boundaries and interfaces.

This lesson also connects directly to applications in acoustics, optics, and materials science.

## Common Misconceptions

### "A boundary always reflects everything"

No. Some boundaries or interfaces allow partial transmission.

### "Transmission means no reflection occurs"

Not necessarily. Both can happen simultaneously.

### "The interface only changes amplitude"

It can also affect phase, speed, and qualitative propagation behavior.

## Suggested Learning Path

### Step 1: Start from a traveling-wave picture

Students should first imagine a pulse meeting a boundary.

### Step 2: Introduce interface conditions

These determine how the incoming wave splits.

### Step 3: Compare reflected and transmitted components

Students should interpret them physically rather than only symbolically.

### Step 4: Connect to real applications

Echoes, acoustics, and optics make the mathematics vivid.

### Checkpoints

- Can students explain why an interface produces both reflection and transmission?
- Do they understand the role of matching conditions?
- Can they connect the mathematics to a physical example like echo or partial transmission?

## Worked Examples

### Example 1: Fixed Boundary Reflection

A wave hitting a rigid fixed boundary reflects back, often with a sign change depending on the physical setup.

### Example 2: Interface Between Two Media

An incoming pulse splits into reflected and transmitted parts whose amplitudes depend on the media properties.

### Example 3: Echo Interpretation

An echo is mathematically a reflected wave returning to the source region.

## Conceptual Questions

1. Why does a change in medium create partial transmission rather than full passage?
2. Why can reflection and transmission coexist?
3. What role do interface conditions play in determining amplitudes?

## Application Problems

1. Why do echoes arise in acoustics?
2. Why do waves reflect partially at material boundaries in optics or seismology?
3. How might engineers reduce unwanted reflections in design problems?

## Interactive Teaching Strategies

- Use simple pulse diagrams showing incoming, reflected, and transmitted waves.
- Connect the mathematics to familiar echoes or boundary reflections.
- Ask students to predict what happens when a wave enters a "harder" or "softer" medium.
- Reinforce that interfaces are mathematically active, not passive.

## Differentiation

### Support for Struggling Students

Students needing support should work with physical storytelling and diagrams before confronting formulas for reflection and transmission coefficients.

### Challenge for Advanced Students

Advanced students can explore impedance matching and energy balance across interfaces.

## Summary

Boundaries do not merely stop waves; they reshape them. Reflection and transmission are central effects in wave physics and engineering, and they show how PDE behavior is strongly influenced by interfaces and matching conditions.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Seismic waves crossing a material interface
- Problem: When a wave reaches the boundary between two geological layers, part reflects and part transmits.
- Model: Couple two wave equations with different impedances and impose interface continuity conditions.
- Assumptions and limitations: One-dimensional approximation, linear materials, flat interface.
- Interpretation: Material contrast controls reflection strength.

#### String with two densities joined together
- Problem: A pulse on a composite string does not pass through the junction unchanged.
- Model: Continuity of displacement and force at the junction.
- Assumptions and limitations: Ideal joint, equal tension, no losses at the interface.
- Interpretation: This is the simplest mechanical interface model.

### 2. Additional Intuition and Connections

Reflection and transmission occur because different media resist motion differently. The idea of impedance here is closely related to circuit theory, optics, and seismology. A common pitfall is to think boundaries only cause total reflection; in practice most interfaces produce a mixture of reflection and transmission.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.2, 4.0, 400)   # Z2 / Z1
R = (r - 1) / (r + 1)
T = 2 / (r + 1)

plt.plot(r, R, label="reflection coefficient")
plt.plot(r, T, label="transmission coefficient")
plt.axhline(0, color="black", linewidth=0.8)
plt.xlabel("Impedance ratio Z2/Z1")
plt.title("Reflection and transmission versus impedance contrast")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: reflection transmission wave interface animation
- search: seismic reflection coefficient tutorial
- search: string with density jump wave pulse

### 5. Worked Example

If the wave impedances are $$ Z_1 $$ and $$ Z_2 $$, the normalized reflection amplitude is often
$$ R=\frac{Z_2-Z_1}{Z_2+Z_1}. $$
When $$ Z_2=Z_1 $$, we get $$ R=0 $$, so there is no reflection. Large impedance contrast produces strong reflection. This principle lies at the heart of reflection seismology.

### 6. Difficulty Layering

**Undergraduate level.** Apply interface conditions and interpret reflected versus transmitted wave components.

**Graduate level.** Connect to scattering theory, multilayer transmission, and transfer matrices.

## References

- Haberman, Chapter 4.
