---
layout: post
title: "08-06 Parseval's Theorem"
chapter: '08'
order: 6
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: required
---

In Euclidean geometry, Pythagoras's theorem states that the squared length of a vector equals the sum of the squares of its orthogonal coordinates: $$ \|\mathbf{v}\|^2 = \sum c_k^2 $$. In 1799, Marc-Antoine Parseval discovered that this exact geometric law survives intact in infinite dimensions: the total energy of a signal measured in the *time/space domain* equals the sum of the squared amplitudes of its harmonics in the *frequency domain*.

Beyond physics and electrical engineering (where it guarantees conservation of signal power across a spectrum analyzer), Parseval's identity is a secret weapon in pure mathematics—effortlessly computing exact infinite sums like $$ \sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{90} $$ that defy elementary calculus!

## Background Knowledge Map: Infinite-Dimensional Pythagoras and Spectral Energy

1. **Bessel's Inequality vs. Parseval's Equality (Completeness Test):** For any orthonormal system, $$ \sum |c_n|^2 \le \|f\|^2 $$ (Bessel's inequality—the shadow cannot be longer than the vector). Equality holds for *all* $$ f \in L^2([-L, L]) $$ if and only if the trigonometric system is *complete* (no nonzero function is orthogonal to every mode).
2. **Real Parseval Formula on $$ [-L, L] $$:**
   $$ \frac{1}{L}\int_{-L}^{L} |f(x)|^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty} (a_n^2 + b_n^2). $$
   Watch the factor of $$ \frac{1}{2} $$ on $$ a_0^2 $$—because $$ \frac{a_0}{2} $$ is the constant term while $$ \frac{1}{L}\int_{-L}^L \left(\frac{a_0}{2}\right)^2 dx = \frac{a_0^2}{2} $$!
3. **Exact $$ L^2 $$ Truncation Error Accounting:** The mean-square error of the $$ N $$-th partial sum is literally the tail energy $$ \frac{1}{L}\|f - S_N\|_2^2 = \sum_{n=N+1}^\infty (a_n^2 + b_n^2) $$, giving engineers an exact criterion for how many harmonics are needed to capture 99% of a signal's power.
4. **Evaluating Zeta Values $$ \zeta(2k) $$:** Plugging polynomial functions ($$ x, x^2, |x| $$) into Parseval's identity instantly evaluates $$ \zeta(2) = \frac{\pi^2}{6} $$, $$ \zeta(4) = \frac{\pi^4}{90} $$, and higher even zeta values in three lines of arithmetic.

### Step-by-Step Worked Example (Read Slowly): Proving $$ \sum_{n=1}^{\infty} \frac{1}{n^4} = \frac{\pi^4}{90} $$ via Parseval's Theorem

**Problem:** Use the Fourier series of $$ f(x) = x^2 $$ on $$ [-\pi, \pi] $$ together with Parseval's identity to compute the exact sum $$ \sum_{n=1}^{\infty} \frac{1}{n^4} $$, and verify how much energy the first two terms ($$ a_0, a_1 $$) capture.

1. **Compute the Fourier coefficients of $$ f(x) = x^2 $$ on $$ [-\pi, \pi] $$:**
   Since $$ x^2 $$ is even, $$ b_n = 0 $$ for all $$ n \ge 1 $$.
   - $$ a_0 = \frac{2}{\pi}\int_0^\pi x^2\,dx = \frac{2\pi^2}{3} $$.
   - For $$ n \ge 1 $$, integrate by parts twice:
     $$ a_n = \frac{2}{\pi}\int_0^\pi x^2\cos(nx)\,dx = \frac{2}{\pi}\left[\frac{2x\cos(nx)}{n^2}\right]_0^\pi = \frac{4(-1)^n}{n^2}. $$
2. **Compute the left-hand side of Parseval's identity:**
   $$ \frac{1}{\pi}\int_{-\pi}^{\pi} (x^2)^2\,dx = \frac{2}{\pi}\int_0^\pi x^4\,dx = \frac{2}{\pi}\cdot\frac{\pi^5}{5} = \frac{2\pi^4}{5}. $$
3. **Equate to the right-hand side $$ \frac{a_0^2}{2} + \sum_{n=1}^\infty a_n^2 $$:**
   $$ \frac{2\pi^4}{5} = \frac{1}{2}\left(\frac{4\pi^4}{9}\right) + \sum_{n=1}^{\infty} \frac{16}{n^4} = \frac{2\pi^4}{9} + 16\sum_{n=1}^{\infty} \frac{1}{n^4}. $$
4. **Solve for $$ \sum_{n=1}^\infty \frac{1}{n^4} $$:**
   $$ 16\sum_{n=1}^{\infty} \frac{1}{n^4} = \left(\frac{2}{5} - \frac{2}{9}\right)\pi^4 = \frac{8}{45}\pi^4 \implies \sum_{n=1}^{\infty} \frac{1}{n^4} = \frac{\pi^4}{90} \approx 1.08232. $$
5. **Energy capture check:** Total normalized energy is $$ \frac{2\pi^4}{5} \approx 38.9636 $$. Just the DC term $$ \frac{a_0^2}{2} = \frac{2\pi^4}{9} \approx 21.6465 $$ plus the $$ n = 1 $$ mode $$ a_1^2 = 16 $$ gives $$ 37.6465 $$—capturing **96.6%** of the entire signal energy in just two terms!

## Learning Objectives

This lesson explains Parseval's theorem as an energy identity. Students should see that Fourier coefficients do not merely encode shape, but also distribute the total energy of a function among its harmonic modes.

## Prerequisites

Students should know the Fourier coefficient formulas and be comfortable with squared norms and basic integral interpretations of size or energy.

## Introduction

![Parseval's theorem]({{ site.imgurl }}/chapter_img/chapter08/06_parsevals_theorem.svg)

One of the deepest messages of Fourier analysis is that geometric size in the original variable corresponds to coefficient size in frequency space. Parseval's theorem makes this precise. It says that when a function is expanded in orthogonal harmonic modes, the total energy of the function is exactly the sum of the energies stored in those modes.

This is an extraordinary structural fact. It means that Fourier coefficients are not merely formal constants. They are quantitatively meaningful, and together they preserve the energy of the original function.

## Concept in Three Ways

### Intuitive View

A periodic signal can be thought of as a mixture of frequencies. Parseval's theorem says that the signal's total energy is exactly the sum of the energies of its frequency components.

### Visual View

Instead of looking at the graph of $$ f(x) $$ in physical space, we can look at the collection of coefficients in frequency space. Parseval's theorem says these two perspectives measure the same total squared size.

### Formal View

For a Fourier series,
$$
\frac{1}{L}\int_{-L}^{L} \lvert f(x)\rvert^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty} \left(a_n^2+b_n^2\right).
$$
This is the Fourier-series version of the Pythagorean theorem in an infinite-dimensional orthogonal space.

## Why the Theorem Matters

Parseval's theorem transforms Fourier analysis from a representation theory into a geometry of function space. It shows that orthogonal expansions preserve energy and that trigonometric coefficients behave like coordinates in a Hilbert-space setting.

This is crucial in PDEs. When solutions are expanded into Fourier modes, Parseval's theorem lets us estimate norms, compare energies, and understand how much each mode contributes to the total solution.

## Common Misconceptions

### "Parseval's theorem is just a fancy identity"

No. It expresses a deep conservation of norm between physical space and frequency space.

### "The theorem is only useful in pure analysis"

No. It appears everywhere in signal processing, quantum theory, acoustics, and PDE energy estimates.

### "Only the first few coefficients matter"

Not always. The contribution of higher modes depends on the function and the context.

## Suggested Learning Path

### Step 1: Recall orthogonality

Students should see Parseval's theorem as the infinite-dimensional analogue of adding squares of orthogonal components.

### Step 2: Compare with vectors

The analogy with Euclidean geometry makes the theorem more intuitive.

### Step 3: Apply the identity in examples

Concrete examples help students see the coefficient-energy relationship.

### Step 4: Connect to PDE applications

This is where the theorem begins to feel indispensable.

### Checkpoints

- Can students explain why Parseval resembles the Pythagorean theorem?
- Do they understand why squared coefficients represent energy contributions?
- Can they interpret the theorem physically for a signal or oscillating system?

## Worked Examples

### Example 1: Single Harmonic

If a function consists of only one sine or cosine mode, Parseval's theorem immediately reduces to the statement that the total energy equals the energy of that one mode.

### Example 2: Two Harmonics

For a sum of two orthogonal modes, the total energy is the sum of the two separate energies. The cross terms vanish because of orthogonality.

### Example 3: Infinite Expansion

For a more complicated periodic function, Parseval's theorem expresses the full energy as an infinite coefficient sum, showing how energy is distributed across frequencies.

## Conceptual Questions

1. Why does Parseval's theorem resemble the Pythagorean theorem?
2. Why do orthogonal functions allow energy to separate into independent pieces?
3. Why is frequency-space energy important in PDEs and signal analysis?

## Application Problems

1. In acoustics, what does it mean for most energy to be concentrated in low frequencies?
2. In a PDE solution, why is an energy estimate often easier in coefficient form?
3. In data compression, why are small coefficients often discarded first?

## Interactive Teaching Strategies

- Use vector geometry analogies before writing the theorem formally.
- Ask students to interpret coefficient squares as mode energies.
- Compare a function whose energy is concentrated in one mode with another distributed across many modes.
- Reinforce the phrase "energy in physical space equals energy in frequency space."

## Differentiation

### Support for Struggling Students

Students needing support should focus on finite-dimensional orthogonality analogies before confronting the infinite-series identity.

### Challenge for Advanced Students

Advanced students can connect Parseval's theorem to Hilbert spaces, orthonormal bases, and later transform theory.

## Summary

Parseval's theorem is an energy balance between physical space and frequency space. It is one of the central structural results of Fourier analysis and one of the key reasons orthogonal expansions are so powerful in PDE theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Signal-energy conservation
- Problem: We want to know how the total energy of a signal is distributed across harmonics.
- Model:
$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert f(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$
- Assumptions and limitations: The correct natural setting is $$ L^2 $$; pointwise convergence is not the main issue here.
- Interpretation: The total signal energy equals the sum of the modal energies.

#### Truncation error in simulation
- Problem: We need to know how much energy is lost when high-frequency modes are omitted.
- Model:
$$
\lVert f-S_N\rVert_{L^2}^2
=
\pi\sum_{n=N+1}^{\infty}(a_n^2+b_n^2).
$$
- Assumptions and limitations: The error is measured in the energy norm.
- Interpretation: The tail of the spectrum is exactly the remaining energy error.

### 2. Additional Intuition and Connections

Parseval's theorem shows that Fourier analysis preserves energy, not merely shape. A common pitfall is to see the squares of the coefficients as a technical artifact. In fact they are precisely the modal energy contributions. This is also the natural bridge from Fourier series to Fourier transforms and Plancherel theory.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 21)
energy = 4 / n**2

plt.bar(n, energy)
plt.xlabel("n")
plt.ylabel("mode energy")
plt.title("Mode energy for f(x)=x")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Parseval theorem signal energy visualization
- search: Fourier mode energy spectrum
- search: truncation error Parseval Fourier series

### 5. Worked Example

For
$$ f(x)=x,\qquad -\pi<x<\pi, $$
we have
$$ b_n=\frac{2(-1)^{n+1}}{n},\qquad a_n=0. $$
Applying Parseval gives
$$
\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\,dx
=
\sum_{n=1}^{\infty}\frac{4}{n^2},
$$
and therefore
$$ \sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}. $$

### 6. Difficulty Layering

**Undergraduate level.** State Parseval, use it to compute classical sums, and interpret truncation error.

**Graduate level.** Emphasize $$ L^2 $$ isometry, Plancherel theory, and Hilbert-space geometry.

## Video tham khảo

- xem trước: [Parseval's Theorem](https://www.youtube.com/watch?v=ML0eYMyhqOs) — Steve Brunton, English. Steve Brunton on Parseval's theorem and the energy in the coefficients.
- [Parseval's Identity, Fourier Series, and Solving this Classic Pi Formula](https://www.youtube.com/watch?v=WPeU34jndSw) — Dr. Trefor Bazett, English. Trefor Bazett uses Parseval's identity on a classical series for pi.
- [Parseval's Theorem (Fourier series engineering mathematics)](https://www.youtube.com/watch?v=1qkqCTwYoqU) — blackpenredpen, English. A direct computation of Parseval's relation for a Fourier series.

## References

- Haberman, Chapter 3: energy interpretation and examples.
