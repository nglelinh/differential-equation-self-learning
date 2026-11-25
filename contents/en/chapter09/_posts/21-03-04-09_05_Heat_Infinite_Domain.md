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

Remove the walls completely and imagine an infinitely long metal wire stretching from $$ -\infty $$ to $$ +\infty $$. With no boundary conditions to quantize spatial wavelengths, there are no discrete eigenvalues $$ \lambda_n $$ and no Fourier series. Instead, every continuous wavenumber $$ \omega \in \mathbb{R} $$ participates simultaneously via the Fourier Transform—and when you invert the Gaussian damping factor $$ e^{-\alpha \omega^2 t} $$ back into physical space, out pops one of the most famous formulas in analysis: convolution with the **Gaussian Heat Kernel**!

## Key ideas: Fourier Transform Solution and Infinite Speed of Propagation

1. **Fourier Transform Diagonalization on $$ \mathbb{R} $$:** Transforming $$ u_t = \alpha u_{xx} $$ in $$ x $$ turns $$ \partial_{xx} $$ into $$ -\omega^2 $$, yielding the elementary ODE $$ \hat{u}_t(\omega, t) = -\alpha \omega^2 \hat{u}(\omega, t) \implies \hat{u}(\omega, t) = \hat{f}(\omega) e^{-\alpha \omega^2 t} $$.
2. **Gaussian Heat Kernel (Inverse Transform of $$ e^{-\alpha\omega^2 t} $$):** Because the inverse Fourier transform of a Gaussian is another Gaussian, convolution gives
   $$ u(x, t) = \frac{1}{\sqrt{4\pi\alpha t}} \int_{-\infty}^{\infty} e^{-\frac{(x - y)^2}{4\alpha t}} f(y)\,dy \qquad (t > 0). $$
3. **Instantaneous Smoothing & Infinite Propagation Speed:** Even if $$ f(x) $$ is a discontinuous step function supported only on $$ [-1, 1] $$, for *every* $$ t > 0 $$ (even $$ t = 10^{-100} $$!), $$ u(x, t) $$ is $$ C^\infty $$ smooth and strictly positive everywhere on $$ \mathbb{R} $$. Heat mathematically travels with infinite speed (though exponentially tiny far away).
4. **Error Function $$ \operatorname{erf}(z) $$ & Similarity Variable $$ \eta = \frac{x}{\sqrt{4\alpha t}} $$:** For step initial data, the Gaussian integral reduces directly to the error function $$ \operatorname{erf}(z) = \frac{2}{\sqrt{\pi}}\int_0^z e^{-s^2}\,ds $$, revealing that temperature depends only on the self-similar ratio $$ x / \sqrt{4\alpha t} $$.

### Worked example: Evolving a Gaussian Initial Pulse Exactly on $$ (-\infty, \infty) $$

**Problem:** Solve $$ u_t = \alpha u_{xx} $$ on $$ -\infty < x < \infty $$, $$ t > 0 $$, with Gaussian initial temperature $$ u(x, 0) = e^{-x^2 / (4\sigma^2)} $$ ($$ \sigma > 0 $$), and compute the exact time $$ t_{1/2} $$ at which the peak temperature at $$ x = 0 $$ drops to half its initial height.

1. **Use the known Gaussian Fourier transform $$ \mathcal{F}\bigl\{e^{-a x^2}\bigr\}(\omega) = \sqrt{\frac{\pi}{a}} e^{-\omega^2 / (4a)} $$:**
   Here $$ a = \frac{1}{4\sigma^2} $$, so $$ \frac{1}{4a} = \sigma^2 $$ and
   $$ \hat{f}(\omega) = 2\sigma\sqrt{\pi}\,e^{-\sigma^2 \omega^2}. $$
2. **Multiply by the heat-equation spectral damping factor $$ e^{-\alpha \omega^2 t} $$:**
   $$ \hat{u}(\omega, t) = 2\sigma\sqrt{\pi}\,e^{-(\sigma^2 + \alpha t)\omega^2}. $$
   Notice how the variance simply adds linearly in time: $$ \sigma^2 \mapsto \sigma^2 + \alpha t $$!
3. **Invert the Gaussian Fourier transform immediately:**
   Matching $$ \sqrt{\frac{\pi}{A}} e^{-\omega^2/(4A)} $$ with $$ \frac{1}{4A} = \sigma^2 + \alpha t \implies A = \frac{1}{4(\sigma^2 + \alpha t)} $$ gives
   $$ u(x, t) = \frac{\sigma}{\sqrt{\sigma^2 + \alpha t}} \exp\!\left(-\frac{x^2}{4(\sigma^2 + \alpha t)}\right). $$
4. **Verify total thermal mass conservation and find $$ t_{1/2} $$:**
   - Total integral: $$ \int_{-\infty}^\infty u(x, t)\,dx = \frac{\sigma}{\sqrt{\sigma^2 + \alpha t}} \cdot 2\sqrt{\pi(\sigma^2 + \alpha t)} = 2\sigma\sqrt{\pi} $$ (independent of $$ t $$!).
   - Peak at $$ x = 0 $$: $$ u(0, t) = \frac{\sigma}{\sqrt{\sigma^2 + \alpha t}} = \frac{1}{2} \implies \sigma^2 + \alpha t_{1/2} = 4\sigma^2 \implies t_{1/2} = \frac{3\sigma^2}{\alpha} $$.
   As the Gaussian spreads wider, its peak falls like $$ t^{-1/2} $$ so total heat stays strictly conserved!

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

## Video tham khảo

- xem trước: [Solving the Heat Equation with the Fourier Transform](https://www.youtube.com/watch?v=7haZCrQDHpA) — Steve Brunton, English. The Fourier transform solves the heat equation on the whole line.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, English. The same decay of frequencies, now without a finite bar of modes.
- [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, English. The transform used as the change of coordinate in that calculation.

## References

- Evans, Chapter 2.
