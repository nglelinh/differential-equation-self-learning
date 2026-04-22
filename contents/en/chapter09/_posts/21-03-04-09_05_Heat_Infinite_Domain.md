---
layout: post
title: "09-05 Heat Equation on Infinite Domain"
chapter: '09'
order: 5
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: required
---

## Learning Objectives

This lesson studies the heat equation on the whole line and introduces transform-based methods. Students should understand why infinite domains call for Fourier analysis rather than discrete series expansions.

## Prerequisites

Students should know Fourier series, the idea of separation on bounded intervals, and the basic distinction between finite and infinite domains.

## Introduction

![Heat equation on an infinite domain]({{ site.imgurl }}/chapter_img/chapter09/05_heat_infinite_domain.svg)

On a finite rod, separation of variables leads to discrete eigenmodes. On the whole real line, the situation changes completely. There are no endpoint boundary conditions to quantize the frequencies, so the harmonic structure becomes continuous instead of discrete.

This is where the Fourier transform enters naturally. The infinite-domain heat equation is one of the clearest and most important examples of transform-based PDE solution.

## Concept in Three Ways

### Intuitive View

Without boundaries, heat spreads freely in both directions. There are no special standing modes imposed by endpoints. Instead, the solution is built from a continuum of frequencies.

### Visual View

A localized heat pulse broadens over time while its height decreases. The profile does not bounce, reflect, or quantize. It simply spreads outward continuously.

### Formal View

For
$$ u_t=\alpha^2 u_{xx}, \qquad -\infty < x < \infty, $$
one applies the Fourier transform in space, turning differentiation into multiplication by frequency. The PDE becomes an ODE in time for each frequency component.

## Why the Infinite-Domain Case Matters

This lesson shows the transition from Fourier series to Fourier transforms in a concrete PDE setting. It reveals that bounded and unbounded domains require different spectral languages.

It also gives one of the most natural examples of why transform methods are so powerful: they diagonalize the PDE in frequency space.

## Common Misconceptions

### "The whole-line problem is just a limit of the finite-interval problem with no conceptual change"

No. The spectral picture changes from discrete to continuous.

### "Without boundaries, the problem is simpler in every way"

Not necessarily. It is simpler geometrically, but it requires transform methods rather than series methods.

### "Diffusion on the line still has standing modes"

No. The infinite line supports continuous-frequency components rather than discrete standing eigenmodes.

## Suggested Learning Path

### Step 1: Contrast finite and infinite domains

Students should see why boundaries create discrete modes.

### Step 2: Introduce the Fourier transform viewpoint

This provides the continuous-frequency replacement for Fourier series.

### Step 3: Solve the transformed ODE

Each frequency component decays separately.

### Step 4: Interpret the spreading behavior

The solution should be understood physically as diffusion on an unbounded domain.

### Checkpoints

- Can students explain why the spectrum becomes continuous?
- Do they understand why the Fourier transform is natural on $$ \mathbb{R} $$?
- Can they describe the qualitative spreading of a localized pulse?

## Worked Examples

### Example 1: Localized Initial Pulse

A concentrated initial profile spreads outward and flattens over time, illustrating the basic behavior of diffusion on the line.

### Example 2: Frequency-Space Decay

Each transformed mode decays exponentially in time, with faster decay for higher frequencies.

### Example 3: Smoothing Effect

Even rough initial data become smoother as time evolves, a hallmark of the parabolic character of the equation.

## Conceptual Questions

1. Why do finite intervals lead to discrete modes while the whole line leads to continuous frequencies?
2. Why are higher frequencies suppressed more rapidly in the heat equation?
3. Why does diffusion on the line smooth and spread localized data?

## Application Problems

1. Why is the whole-line heat equation a good model for local diffusion far from boundaries?
2. In probability, how is heat spreading related to random motion?
3. Why is the Fourier transform especially natural for translation-invariant problems?

## Interactive Teaching Strategies

- Compare the bounded-interval and infinite-line heat problems explicitly.
- Use sketches of localized pulses at successive times.
- Emphasize the transition from discrete to continuous spectrum.
- Connect the transform solution to the Gaussian kernel that will appear next.

## Differentiation

### Support for Struggling Students

Students needing support should focus first on the conceptual difference between finite and infinite domains before handling transform formulas.

### Challenge for Advanced Students

Advanced students can investigate explicit transform inversion and the emergence of the heat kernel.

## Summary

On an infinite interval, the harmonic picture becomes continuous. The Fourier transform becomes the natural language for diffusion on the whole line, and the heat equation reveals one of the clearest examples of transform-based PDE analysis.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Diffusion on the whole line
- Problem: Material spreads through an unbounded medium with no finite boundaries.
- Model:
$$ u_t=\alpha^2 u_{xx},\qquad x\in \mathbb{R}. $$
- Assumptions and limitations: Infinite domain and sufficiently decaying data.
- Interpretation: A continuous spectrum replaces the discrete mode families of finite intervals.

#### Localized heat packet
- Problem: Heat starts concentrated near one location and then spreads.
- Model: Solve using the Fourier transform or the heat kernel.
- Assumptions and limitations: No reflecting boundaries or external forcing.
- Interpretation: The temperature profile widens and lowers while total heat is conserved.

### 2. Additional Intuition and Connections

An infinite domain destroys the discrete sine-cosine mode picture and replaces it with a continuous frequency spectrum. A common pitfall is to try to keep the finite-interval Fourier-series intuition unchanged. The right language here is the Fourier transform and the heat kernel.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 800)
for t in [0.05, 0.2, 0.8]:
    G = (1 / np.sqrt(4 * np.pi * t)) * np.exp(-x**2 / (4 * t))
    plt.plot(x, G, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("G(x,t)")
plt.title("Heat kernel on the infinite line")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: heat equation infinite domain Gaussian kernel
- search: diffusion on whole line animation
- search: Fourier transform heat equation solution

### 5. Worked Example

For delta initial data at the origin, the heat equation on $$ \mathbb{R} $$ has the solution
$$
G(x,t)=\frac{1}{\sqrt{4\pi \alpha^2 t}}\exp\left(-\frac{x^2}{4\alpha^2 t}\right).
$$
This Gaussian is the fundamental spreading profile of heat on an unbounded domain.

### 6. Difficulty Layering

**Undergraduate level.** Understand why the Gaussian appears and how the profile spreads in time.

**Graduate level.** Emphasize the heat semigroup on $$ \mathbb{R}^n $$ and the role of the Fourier transform.

## References

- Evans, Chapter 2.
