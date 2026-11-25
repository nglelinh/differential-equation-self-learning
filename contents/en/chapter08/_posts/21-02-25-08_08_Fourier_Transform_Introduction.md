---
layout: post
title: "08-08 Fourier Transform: Introduction"
chapter: '08'
order: 8
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: optional
---

What happens to a Fourier series when a signal is no longer periodic—like a single drumbeat, a seismic shockwave, or a localized heat pulse on an infinite metal wire? Imagine stretching the period $$ [-L, L] $$ outward toward $$ (-\infty, \infty) $$. As $$ L \to \infty $$, the spacing between adjacent discrete frequencies $$ \Delta\omega = \frac{\pi}{L} $$ shrinks to zero, the discrete spectrum of harmonics melts into a *continuous spectrum* $$ \hat{f}(\omega) $$, and the Fourier sum becomes the **Fourier Transform** integral!

This limit is one of the most consequential bridges in all of mathematics: it converts differentiation on the whole real line into multiplication by $$ i\omega $$, turning PDEs on infinite domains into one-line algebraic equations.

## Key ideas: From Discrete Harmonics to Continuous Spectra

1. **The $$ L \to \infty $$ Riemann-Sum Limit:** Setting $$ \omega_n = \frac{n\pi}{L} $$ and $$ \Delta\omega = \frac{\pi}{L} $$, the complex Fourier series $$ \sum c_n e^{i\omega_n x} $$ becomes $$ \frac{1}{2\pi}\int_{-\infty}^\infty \hat{f}(\omega) e^{i\omega x}\,d\omega $$, where $$ \hat{f}(\omega) = \int_{-\infty}^\infty f(x) e^{-i\omega x}\,dx $$ (watch normalization conventions—some texts use $$ \frac{1}{\sqrt{2\pi}} $$ symmetrically).
2. **Differentiation & Convolution Theorems (PDE Superpower):** For functions decaying at infinity, $$ \widehat{f'}(\omega) = i\omega \hat{f}(\omega) $$ and $$ \widehat{f''}(\omega) = -\omega^2 \hat{f}(\omega) $$. Meanwhile, convolution $$ (f * g)(x) = \int_{-\infty}^\infty f(y)g(x-y)\,dy $$ transforms into pointwise multiplication $$ \widehat{f * g}(\omega) = \hat{f}(\omega)\hat{g}(\omega) $$.
3. **Plancherel's Theorem (Continuous Energy Conservation):** The Fourier transform is an isometry on $$ L^2(\mathbb{R}) $$: $$ \int_{-\infty}^\infty |f(x)|^2\,dx = \frac{1}{2\pi}\int_{-\infty}^\infty |\hat{f}(\omega)|^2\,d\omega $$.
4. **Time–Frequency Uncertainty Principle:** Scaling $$ f(ax) $$ scales its transform to $$ \frac{1}{|a|}\hat{f}(\omega/a) $$. Squeezing a pulse narrowly in space/time inevitably spreads its spectrum wide in frequency—a pure Fourier law that underlies both radar resolution and Heisenberg's uncertainty principle in quantum mechanics.

### Worked example: Fourier Transform of the Two-Sided Exponential $$ e^{-a|x|} $$ and Plancherel Check

**Problem:** Compute the Fourier transform $$ \hat{f}(\omega) = \int_{-\infty}^\infty e^{-a|x|} e^{-i\omega x}\,dx $$ for $$ a > 0 $$, check its scaling behavior as $$ a $$ doubles, and verify Plancherel's identity explicitly.

1. **Split the integral at $$ x = 0 $$:**
   $$ \hat{f}(\omega) = \int_{-\infty}^{0} e^{(a - i\omega)x}\,dx + \int_{0}^{\infty} e^{-(a + i\omega)x}\,dx. $$
2. **Evaluate both improper integrals (convergent since $$ a > 0 $$):**
   - Left half: $$ \left[\frac{e^{(a - i\omega)x}}{a - i\omega}\right]_{-\infty}^{0} = \frac{1}{a - i\omega} $$.
   - Right half: $$ \left[\frac{e^{-(a + i\omega)x}}{-(a + i\omega)}\right]_{0}^{\infty} = \frac{1}{a + i\omega} $$.
3. **Combine into a real Lorentzian spectrum:**
   $$ \hat{f}(\omega) = \frac{1}{a - i\omega} + \frac{1}{a + i\omega} = \frac{(a + i\omega) + (a - i\omega)}{a^2 + \omega^2} = \frac{2a}{a^2 + \omega^2}. $$
   Look at the uncertainty principle in action: doubling $$ a $$ makes $$ e^{-a|x|} $$ twice as narrow in $$ x $$, while the half-maximum width of $$ \frac{2a}{a^2 + \omega^2} $$ (at $$ \omega = \pm a $$) becomes twice as wide in $$ \omega $$!
4. **Verify Plancherel's identity $$ \int_{-\infty}^\infty |f(x)|^2\,dx = \frac{1}{2\pi}\int_{-\infty}^\infty |\hat{f}(\omega)|^2\,d\omega $$:**
   - Spatial energy: $$ \int_{-\infty}^\infty e^{-2a|x|}\,dx = 2\int_0^\infty e^{-2ax}\,dx = \frac{1}{a} $$.
   - Spectral energy (using $$ \omega = a\tan\theta \implies d\omega = a\sec^2\theta\,d\theta $$):
     $$ \frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{4a^2}{(a^2 + \omega^2)^2}\,d\omega = \frac{2a^2}{\pi}\int_{-\pi/2}^{\pi/2} \frac{a\sec^2\theta}{a^4\sec^4\theta}\,d\theta = \frac{2}{\pi a}\int_{-\pi/2}^{\pi/2} \cos^2\theta\,d\theta = \frac{2}{\pi a}\cdot\frac{\pi}{2} = \frac{1}{a}. $$
   Exact agreement!

## Learning Objectives

This lesson introduces the Fourier transform as the continuous analogue of Fourier series. Students should understand how passing from periodic domains to infinite domains turns discrete frequencies into a continuum.

## Prerequisites

Students should know Fourier series, complex exponentials, and the idea that periodicity corresponds to discrete harmonic modes.

## Introduction

![Fourier transform introduction]({{ site.imgurl }}/chapter_img/chapter08/08_fourier_transform_introduction.svg)

Fourier series decompose periodic functions into discrete harmonics. On an infinite domain, that harmonic picture remains, but the frequency set becomes continuous rather than discrete. This transition leads naturally to the Fourier transform.

The Fourier transform is one of the most powerful tools in modern analysis. It extends harmonic decomposition beyond periodic functions and becomes indispensable for PDEs on the whole line or whole space.

## Concept in Three Ways

### Intuitive View

Instead of asking which discrete harmonics appear in a periodic function, we ask how strongly each continuous frequency contributes to a nonperiodic signal.

### Visual View

In Fourier series, frequencies are spaced like isolated spikes. In the transform setting, the spectrum becomes a continuum. The function is described by a frequency density rather than a discrete list of amplitudes.

### Formal View

For a suitable function $$ f(x) $$ on the real line, the Fourier transform is formally written as
$$
\widehat{f}(\xi)=\int_{-\infty}^{\infty} f(x)e^{-i\xi x}\,dx.
$$
It is the continuous-frequency analogue of the complex Fourier-series coefficient formula.

## Why the Transform Matters

The Fourier transform allows whole-line PDEs to be solved in frequency space. Differentiation becomes multiplication, convolutions become products, and diffusion or wave propagation on unbounded domains becomes far more tractable.

Conceptually, the transform completes the story begun by Fourier series. The same harmonic philosophy survives, but without periodicity.

## Common Misconceptions

### "The Fourier transform is unrelated to Fourier series"

No. It is the natural limit of Fourier series as the period tends to infinity.

### "Only periodic functions can be studied spectrally"

False. The transform is precisely what extends spectral analysis to nonperiodic functions.

### "Continuous frequency means the transform is less structured"

No. The transform has deep algebraic and analytic structure.

## Suggested Learning Path

### Step 1: Recall the complex Fourier series

Students should see the transform as a generalization rather than a separate invention.

### Step 2: Let the period grow

The idea of discrete frequencies becoming continuous should be emphasized conceptually.

### Step 3: Introduce the transform formula

This should feel like a continuum version of Fourier coefficients.

### Step 4: Connect to PDEs

Whole-line heat and wave equations are the key motivation.

### Checkpoints

- Can students explain why infinite domains lead to continuous frequency variables?
- Do they understand the transform as a generalization of Fourier coefficients?
- Can they describe one reason the transform is useful in PDE analysis?

## Worked Examples

### Example 1: Gaussian Function

The Gaussian is one of the most important transform examples because it keeps essentially the same shape under the transform.

### Example 2: Compactly Supported Pulse

A localized pulse transforms into a continuous oscillatory frequency profile, illustrating the shift from time or space localization to frequency spread.

### Example 3: Exponential Mode

Complex exponentials remain central, but now they are integrated over a continuous frequency family rather than summed discretely.

## Conceptual Questions

1. Why does the frequency set become continuous on an infinite domain?
2. In what sense is the Fourier transform the limit of Fourier series?
3. Why is frequency-space analysis so useful for whole-line PDEs?

## Application Problems

1. Why is the Fourier transform natural for diffusion on the real line?
2. In signal analysis, why does a short pulse require a broad frequency spectrum?
3. Why do transform methods become more natural than series methods on unbounded domains?

## Interactive Teaching Strategies

- Compare discrete Fourier coefficients with a continuous frequency graph.
- Ask students to describe how periodic and nonperiodic cases differ conceptually.
- Use the phrase "discrete spectrum versus continuous spectrum" repeatedly.
- Tie the transform directly to later PDE chapters.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the conceptual transition from discrete to continuous frequency before worrying about transform identities.

### Challenge for Advanced Students

Advanced students can explore inversion ideas, transform pairs, and the transform of classical model functions.

## Summary

The Fourier transform extends the core idea of Fourier series beyond periodicity. It replaces discrete harmonics with a continuous spectrum and becomes the natural analytic tool for whole-line PDEs and signal analysis.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Diffraction and imaging
- Problem: Nonperiodic signals and infinite-domain structures require a continuous rather than discrete frequency description.
- Model:
$$
\hat{f}(\xi)=\int_{-\infty}^{\infty}f(x)e^{-i\xi x}\,dx.
$$
- Assumptions and limitations: The integral requires appropriate decay or an extended interpretation.
- Interpretation: The Fourier transform replaces a discrete harmonic spectrum by a continuous one.

#### Heat equation on the whole line
- Problem: Fourier series are no longer the right tool when the spatial domain is all of $$ \mathbb{R} $$.
- Model: The Fourier transform converts spatial derivatives into multiplication in frequency.
- Assumptions and limitations: The domain is infinite and the data are suitably well behaved.
- Interpretation: The Fourier transform is the continuous-spectrum analogue of complex Fourier series.

### 2. Additional Intuition and Connections

The Fourier transform appears when the period becomes infinitely large and the discrete frequency set becomes continuous. A common pitfall is to treat it as a completely unrelated formula. It is more natural to view it as the limiting form of Fourier series on longer and longer intervals.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 2000)
f = np.exp(-x**2)

dx = x[1] - x[0]
freq = np.fft.fftshift(np.fft.fftfreq(x.size, d=dx)) * 2 * np.pi
F = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(f))) * dx

plt.plot(freq, np.abs(F))
plt.xlabel("xi")
plt.ylabel("|F(xi)|")
plt.title("Approximate continuous spectrum of a Gaussian")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Fourier transform Gaussian visualization
- search: from Fourier series to Fourier transform
- search: continuous frequency spectrum animation

### 5. Worked Example

For
$$ f(x)=e^{-x^2}, $$
one of the most beautiful Fourier-analysis examples is
$$ \hat{f}(\xi)=\sqrt{\pi}\,e^{-\xi^2/4} $$
under a suitable normalization convention. The Gaussian is therefore stable under the Fourier transform and appears everywhere in diffusion, probability, and optics.

### 6. Difficulty Layering

**Undergraduate level.** Understand the Fourier transform as a continuous spectrum and learn a few core examples such as the Gaussian.

**Graduate level.** Connect to Schwartz space, Plancherel theory, distributions, and PDEs on unbounded domains.

## Video tham khảo

- xem trước: [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, English. 3Blue1Brown's visual introduction to the Fourier transform.
- [Solving the Heat Equation with the Fourier Transform](https://www.youtube.com/watch?v=7haZCrQDHpA) — Steve Brunton, English. Brunton uses the transform to solve the heat equation on the line.
- [The more general uncertainty principle, regarding Fourier transforms](https://www.youtube.com/watch?v=MBnnXbOM5S4) — 3Blue1Brown, English. The uncertainty principle as a property of the transform introduced here.

## References

- Haberman, Chapter 3: bridge from Fourier series to Fourier transforms.
- Evans, Appendix: concise transform-oriented viewpoint.
