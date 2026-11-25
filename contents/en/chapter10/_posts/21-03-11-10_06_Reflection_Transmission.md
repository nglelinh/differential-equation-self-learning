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

Toss a stone into a canal and watch the ripple hit a concrete wall—it bounces right back. Now tie a thin silk thread to a heavy climbing rope and send a pulse down the thread toward the knot: part of the pulse bounces *upside down* back along the thread, while a shorter, slower pulse keeps marching forward into the heavy rope! This exact interface physics governs anti-reflective coatings on eyeglasses, ultrasound medical imaging of organs, seismic waves bouncing off Earth's mantle, and impedance matching in RF cables.

Everything boils down to two simple continuity rules at the junction $$ x = 0 $$—and one magic number called the **characteristic impedance** $$ Z = \rho c $$!

## Key ideas: Boundaries, Interfaces, and Impedance Matching

1. **Method of Images on the Half-Line (Fixed vs. Free Reflection):**
   - *Fixed wall ($$ u(0, t) = 0 $$):* Extend initial data **oddly** across $$ x = 0 $$. An incoming crest hits the wall and reflects **inverted** as a trough!
   - *Free ring ($$ u_x(0, t) = 0 $$):* Extend initial data **evenly** across $$ x = 0 $$. An incoming crest reflects **upright** (momentarily doubling height to $$ 2A $$ right at the free end!).
2. **Interface Continuity Conditions at $$ x = 0 $$:** Where two media with speeds $$ c_1, c_2 $$ and tensions/impedances meet, the string cannot tear ($$ u(0^-, t) = u(0^+, t) $$) and the massless knot cannot suffer infinite acceleration ($$ T_1 u_x(0^-, t) = T_2 u_x(0^+, t) $$).
3. **Reflection & Transmission Coefficients ($$ R $$ and $$ T_{\text{tr}} $$):** For a string of uniform tension $$ T $$ with densities $$ \rho_1, \rho_2 $$ (so $$ c_1 = \sqrt{T/\rho_1}, c_2 = \sqrt{T/\rho_2} $$), solving the two interface equations yields
   $$ R = \frac{c_2 - c_1}{c_2 + c_1} = \frac{Z_1 - Z_2}{Z_1 + Z_2}, \qquad T_{\text{tr}} = \frac{2c_2}{c_2 + c_1} = \frac{2Z_1}{Z_1 + Z_2}. $$
   Notice $$ 1 + R = T_{\text{tr}} $$, and if $$ Z_2 > Z_1 $$ (entering a heavier medium), $$ R < 0 $$ (phase inversion)!
4. **Energy Flux Conservation ($$ |R|^2 + \frac{Z_2}{Z_1}|T_{\text{tr}}|^2 = 1 $$):** Even when $$ T_{\text{tr}} > 1 $$ (entering a lighter rope!), energy is never created—the transmitted power fraction $$ \frac{Z_2}{Z_1} T_{\text{tr}}^2 $$ plus reflected power fraction $$ R^2 $$ always sums to *exact* $$ 1 $$!

### Worked example: Pulse Crossing from a Light Rope to a Heavy Rope (Energy Balance Check)

**Problem:** A uniform tension $$ T $$ joins a light rope ($$ x < 0 $$, wave speed $$ c_1 = 30\text{ m/s} $$) to a heavier rope ($$ x > 0 $$, wave speed $$ c_2 = 10\text{ m/s} $$). An incident pulse of amplitude $$ A_i = 1.0\text{ cm} $$ travels rightward from $$ x < 0 $$. Compute the reflected amplitude $$ A_r $$, the transmitted amplitude $$ A_t $$, and verify that reflected + transmitted power equals 100% of incident power.

1. **Compute the reflection and transmission ratios $$ R $$ and $$ T_{\text{tr}} $$:**
   Using $$ c_1 = 30, c_2 = 10 $$ (so the heavy rope has $$ \rho_2 / \rho_1 = (c_1/c_2)^2 = 9 $$ and impedance ratio $$ Z_2 / Z_1 = c_1 / c_2 = 3 $$):
   $$ R = \frac{c_2 - c_1}{c_2 + c_1} = \frac{10 - 30}{10 + 30} = -\frac{20}{40} = -\frac{1}{2}, \qquad T_{\text{tr}} = \frac{2c_2}{c_2 + c_1} = \frac{20}{40} = +\frac{1}{2}. $$
2. **Compute physical amplitudes and check knot continuity:**
   - Reflected pulse: $$ A_r = R A_i = -0.5\text{ cm} $$ (inverted!).
   - Transmitted pulse: $$ A_t = T_{\text{tr}} A_i = +0.5\text{ cm} $$ (upright, squeezed to $$ \frac{1}{3} $$ the spatial width since $$ c_2 = c_1/3 $$!).
   - Continuity check at $$ x = 0 $$: $$ A_i + A_r = 1.0 - 0.5 = 0.5\text{ cm} = A_t $$. Exact!
3. **Verify exact power conservation:**
   - Reflected power fraction: $$ R^2 = \left(-\frac{1}{2}\right)^2 = \frac{1}{4} = 25\% $$.
   - Transmitted power fraction: $$ \frac{c_1}{c_2} T_{\text{tr}}^2 = 3 \cdot \left(\frac{1}{2}\right)^2 = \frac{3}{4} = 75\% $$.
   - Total: $$ 25\% + 75\% = 100\% $$! Zero energy lost at the junction!

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

## Video tham khảo

- xem trước: [Strings: reflection and transmission of an incoming wave at a discontinuity.](https://www.youtube.com/watch?v=Zokrkuc2EgU) — Mooc Bogazici, English. Reflection and transmission of a wave at a discontinuity in the string.
- [Reflection and Transmission of Transverse Waves](https://www.youtube.com/watch?v=L5-RuMtXDyo) — Physics Ninja, English. Physics Ninja on reflection and transmission of a transverse wave.
- [PDE 10 | Wave equation: d'Alembert's formula](https://www.youtube.com/watch?v=j2G91naZ8bo) — commutant, English. d'Alembert's right- and left-going waves, the objects that reflect.

## References

- Haberman, Chapter 4.
