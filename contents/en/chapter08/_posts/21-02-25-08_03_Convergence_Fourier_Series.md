---
layout: post
title: "08-03 Convergence of Fourier Series"
chapter: '08'
order: 3
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: required
---

In 1898, Albert Michelson built a mechanical harmonic analyzer capable of summing 80 Fourier modes and fed it a simple square wave. To his astonishment, no matter how many terms he added, a stubborn horn-shaped overshoot refused to vanish near the jump—always peaking about 9% above the cliff! Josiah Willard Gibbs proved in 1899 that Michelson's machine wasn't broken: the overshoot is a permanent mathematical artifact of approximating a discontinuity with continuous waves.

This lesson separates three distinct modes of convergence—pointwise, uniform, and mean-square ($$ L^2 $$)—so you know *exactly* what a Fourier series converges to at smooth points, at jumps, and in energy norm.

## Background Knowledge Map: Pointwise, Uniform, and Mean-Square Convergence

1. **Dirichlet's Pointwise Theorem (Midpoint Rule at Jumps):** If $$ f $$ is piecewise smooth on $$ [-L, L] $$, its Fourier series converges at every point $$ x $$ to the symmetric average $$ \frac{1}{2}\bigl[f(x^+) + f(x^-)\bigr] $$. At points of continuity this equals $$ f(x) $$; at jump discontinuities it lands squarely halfway up the cliff.
2. **Uniform Convergence Criterion (Continuity + Periodicity):** If $$ f $$ is continuous *everywhere* on $$ \mathbb{R} $$ (including matching endpoints $$ f(-L) = f(L) $$) and piecewise smooth, then $$ \sum (|a_n| + |b_n|) < \infty $$, so by the Weierstrass M-test the Fourier series converges *uniformly*—no Gibbs horns!
3. **The Gibbs Phenomenon (Universal $$ \approx 8.95\% $$ Overshoot):** Near a jump of height $$ \Delta = f(x_0^+) - f(x_0^-) $$, the $$ N $$-th partial sum overshoots by $$ \frac{1}{\pi}\int_0^\pi \frac{\sin t}{t}\,dt - \frac{1}{2} \approx 0.08949 $$ times $$ \Delta $$. As $$ N \to \infty $$, the spike gets narrower (width $$ O(1/N) $$) but never shorter!
4. **Mean-Square ($$ L^2 $$) Convergence (Energy Disappears):** Even with Gibbs horns, the *area* under the squared spike shrinks as $$ O(1/N) \to 0 $$, so $$ \|f - S_N\|_{L^2} \to 0 $$ for *every* $$ f \in L^2([-L, L]) $$.

### Step-by-Step Worked Example (Read Slowly): Computing Dirichlet's Midpoint Limit and Quantifying the Gibbs Peak

**Problem:** Consider the $$ 2\pi $$-periodic square wave defined on $$ (-\pi, \pi) $$ by $$ f(x) = -1 $$ for $$ -\pi < x < 0 $$ and $$ f(x) = +1 $$ for $$ 0 < x < \pi $$, whose Fourier series is $$ \frac{4}{\pi}\sum_{k=0}^\infty \frac{\sin((2k+1)x)}{2k+1} $$. (a) Find the exact pointwise limit of the series at $$ x = 0 $$ and $$ x = \pi $$. (b) Compute the peak value of $$ S_3(x) = \frac{4}{\pi}\bigl[\sin x + \frac{1}{3}\sin(3x)\bigr] $$ at $$ x = \frac{\pi}{4} $$ and measure its percentage overshoot relative to the jump $$ \Delta = 2 $$.

1. **Apply Dirichlet's theorem at the discontinuities $$ x = 0 $$ and $$ x = \pi $$:**
   - At $$ x = 0 $$: $$ f(0^-) = -1 $$, $$ f(0^+) = +1 \implies \frac{1}{2}(-1 + 1) = 0 $$. Check series directly: $$ \sin(0) = 0 $$ for every term, summing to $$ 0 $$.
   - At $$ x = \pi $$: $$ f(\pi^-) = +1 $$, $$ f(\pi^+) = f(-\pi^+) = -1 \implies \frac{1}{2}(1 - 1) = 0 $$. Check series: $$ \sin((2k+1)\pi) = 0 $$, summing to $$ 0 $$.
2. **Locate the first maximum of $$ S_3(x) = \frac{4}{\pi}\bigl[\sin x + \frac{1}{3}\sin(3x)\bigr] $$:**
   Differentiate and set to zero:
   $$ S_3'(x) = \frac{4}{\pi}\bigl[\cos x + \cos(3x)\bigr] = \frac{8}{\pi}\cos(2x)\cos x = 0. $$
   The first positive critical point is $$ 2x = \frac{\pi}{2} \implies x = \frac{\pi}{4} $$.
3. **Evaluate $$ S_3(\pi/4) $$ and measure the overshoot:**
   Since $$ \sin(\pi/4) = \frac{\sqrt{2}}{2} $$ and $$ \sin(3\pi/4) = \frac{\sqrt{2}}{2} $$:
   $$ S_3\!\left(\frac{\pi}{4}\right) = \frac{4}{\pi}\left(\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{6}\right) = \frac{4}{\pi}\cdot \frac{2\sqrt{2}}{3} = \frac{8\sqrt{2}}{3\pi} \approx \frac{11.3137}{9.4248} \approx 1.2004. $$
   The overshoot above $$ +1 $$ is $$ 0.2004 $$, which is $$ \frac{0.2004}{2} \approx 10.02\% $$ of the total jump $$ \Delta = 2 $$ (and as $$ N \to \infty $$, this peak moves closer to $$ x = 0^+ $$ and settles strictly at $$ 8.95\% $$ of $$ \Delta $$, never hitting $$ 0\% $$!).

## Learning Objectives

This lesson studies when and how Fourier series converge. Students should distinguish pointwise, uniform, and mean-square convergence, understand why discontinuities create special behavior, and appreciate that convergence questions are essential rather than peripheral.

## Prerequisites

Students should know the definition of a Fourier series and how coefficients are computed. Some prior familiarity with continuity and limits is also helpful.

## Introduction

![Convergence of Fourier series]({{ site.imgurl }}/chapter_img/chapter08/03_convergence_fourier_series.svg)

Writing a Fourier series is only the beginning. The deeper question is whether the series actually reproduces the original function, and in what sense it does so. This is one of the first places in analysis where students encounter the idea that different notions of convergence matter.

The issue becomes especially striking near discontinuities. A Fourier series may still represent the function meaningfully, but not always in the naive point-by-point sense students first expect.

## Concept in Three Ways

### Intuitive View

A Fourier series tries to rebuild the original function from harmonics. If the function is smooth, the reconstruction usually behaves very well. If the function has jumps, the reconstruction still works in an important sense, but with visible oscillatory artifacts near the jumps.

### Visual View

Partial sums often look excellent away from discontinuities, while near a jump they produce overshoots and oscillations. These do not disappear completely as more terms are added; they become more localized. This is the famous Gibbs phenomenon.

### Formal View

For a piecewise smooth periodic function, the Fourier series converges at each point to the midpoint of the one-sided limits:
$$ \frac{f(x^-)+f(x^+)}{2}. $$
At points of continuity, this equals $$ f(x) $$. At jump discontinuities, the series converges to the average of the left and right values.

## Why Convergence Matters

Without convergence theory, a Fourier series is only a formal expression. Convergence tells us what the expansion really means and when it may be trusted as a representation of the function.

This is particularly important in PDEs. When a solution is written as an infinite series, we need to know whether the series converges, how it converges, and whether term-by-term differentiation is legitimate.

## Common Misconceptions

### "If a Fourier series exists, it must converge to the function everywhere"

No. Convergence can fail at some points, or converge to an averaged value at discontinuities.

### "Gibbs phenomenon means Fourier series are broken"

No. It means convergence near jumps is subtle. The method remains powerful and valid.

### "Uniform convergence is the only convergence that matters"

No. Pointwise and mean-square convergence are also important, especially in analysis and PDE applications.

### "Convergence is just a technical appendix"

Wrong. It determines whether the representation is mathematically meaningful.

## Suggested Learning Path

### Step 1: Compare smooth and discontinuous examples

Students should first observe the different visual behavior of the partial sums.

### Step 2: Introduce the midpoint rule at jumps

This is one of the most memorable facts of Fourier theory.

### Step 3: Discuss different notions of convergence

Pointwise, uniform, and mean-square convergence should be clearly separated.

### Step 4: Connect convergence to applications

Students should see why these issues matter in PDE solution theory.

### Checkpoints

- Can students explain why jumps lead to averaged convergence values?
- Do they understand what Gibbs phenomenon looks like?
- Can they distinguish pointwise and uniform convergence?

## Worked Examples

### Example 1: Smooth Periodic Function

For a smooth trigonometric polynomial, convergence is immediate because only finitely many coefficients are nonzero.

### Example 2: Square Wave

The square wave is the standard example showing averaged convergence at jump discontinuities and the visible Gibbs overshoot.

### Example 3: Piecewise Linear Function

A piecewise linear periodic function converges well, but the corners slow coefficient decay and make convergence behavior more interesting than in the smooth case.

## Conceptual Questions

1. Why does a Fourier series converge to an average value at a jump?
2. Why is Gibbs phenomenon not actually a failure of the method?
3. Why should PDE students care about different convergence notions?

## Application Problems

1. In signal processing, why are sharp transitions difficult to capture with only a few harmonics?
2. In PDE boundary data, how might discontinuities influence series solutions?
3. Why does smoother data generally yield better-behaved spectral expansions?

## Interactive Teaching Strategies

- Plot partial sums for continuous and discontinuous functions side by side.
- Ask students to predict where overshoot will appear before seeing the graph.
- Use the midpoint value at jumps as a recurring anchor example.
- Reinforce the distinction between visual approximation and rigorous convergence language.

## Differentiation

### Support for Struggling Students

Students needing support should focus on graphical intuition and a few concrete examples before handling formal convergence statements.

### Challenge for Advanced Students

Advanced students can compare convergence in $$ L^2 $$ versus pointwise convergence and begin asking how smoothness affects coefficient decay.

## Summary

Convergence theory tells us what a Fourier series really means. It is the bridge between formal harmonic expansion and mathematically justified representation, and it becomes essential in later PDE applications.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Reconstructing nonsmooth signals
- Problem: A periodic signal with corners or jumps is approximated by a finite sum of harmonics.
- Model:
$$
S_N(x)=\frac{a_0}{2}+\sum_{n=1}^{N}\left(a_n\cos(nx)+b_n\sin(nx)\right).
$$
- Assumptions and limitations: Pointwise convergence depends on regularity and jump structure.
- Interpretation: Fourier series may converge extremely well in energy even when pointwise convergence near discontinuities is delicate.

#### Signal and image edge behavior
- Problem: We want to understand why truncating high-frequency modes creates ringing near sharp edges.
- Model: Analyze convergence and the Gibbs phenomenon for discontinuous data.
- Assumptions and limitations: One-dimensional examples only illustrate the higher-dimensional phenomenon.
- Interpretation: High modes remain important near jumps, even when the overall approximation is good.

### 2. Additional Intuition and Connections

Fourier convergence is not a single yes-or-no question. It depends on the sense of convergence: pointwise, uniform, or $$ L^2 $$. A common pitfall is to assume that continuity automatically implies uniform convergence. This lesson prepares the way for Parseval and the Fourier transform by clarifying what it means for a harmonic expansion to represent a function.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 2000)
f = np.sign(x)

def partial_sum(x, N):
    s = np.zeros_like(x)
    for k in range(1, N + 1, 2):
        s += (4 / (np.pi * k)) * np.sin(k * x)
    return s

plt.plot(x, f, color="black", label="target")
for N in [3, 9, 25]:
    plt.plot(x, partial_sum(x, N), label=f"N={N}")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gibbs phenomenon near a jump")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Gibbs phenomenon Fourier series
- search: pointwise vs L2 convergence Fourier
- search: Dirichlet theorem Fourier series visualization

### 5. Worked Example

For the square wave from the previous lesson, the Fourier series converges at the jump point $$ x=0 $$ to
$$ \frac{f(0^-)+f(0^+)}{2}=0, $$
not to either one-sided value $$ \pm 1 $$. This is the standard example of Dirichlet convergence at discontinuities.

### 6. Difficulty Layering

**Undergraduate level.** Learn the basic Dirichlet convergence picture: convergence to the function at continuous points and to the midpoint of the jump at discontinuities.

**Graduate level.** Discuss convergence in $$ L^2 $$, smoothness versus coefficient decay, and advanced convergence theorems.

## Video tham khảo

- xem trước: [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, English. Watch the partial sums and the Gibbs ringing, the convergence picture of this lesson.
- [Lec 16 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=xWa5_OXI6VM) — MIT OpenCourseWare, English. Mattuck continues the Fourier series with more general periods and convergence questions.
- [Lec 15 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=EWWw0jryj1A) — MIT OpenCourseWare, English. The MIT lecture that introduces the series whose convergence is at stake.

## References

- Haberman, Chapter 3: standard convergence results with illustrations.
- Evans, Appendix: useful conceptual discussion of convergence modes.
