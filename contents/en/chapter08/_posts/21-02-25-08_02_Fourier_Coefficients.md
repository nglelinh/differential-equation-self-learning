---
layout: post
title: "08-02 Fourier Coefficients"
chapter: '08'
order: 2
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: required
---

Suppose a symphony orchestra plays a single sustained chord and you record the air pressure wave $$ f(t) $$. How can a single formula reach inside that tangled waveform and isolate the exact volume of the cello's $$ 3\omega $$ overtone without being contaminated by the flute, violin, or drums? The answer is Euler's projection trick: multiply $$ f(t) $$ by $$ \cos(n\pi t/L) $$ and integrate over one full period. Every other harmonic cancels out to *exact zero*, leaving only the $$ n $$-th coefficient standing alone.

Beyond mere formulas, the rate at which those coefficients $$ a_n, b_n $$ shrink as $$ n \to \infty $$ acts like an X-ray of the function's smoothness: jumps decay like $$ 1/n $$, corners decay like $$ 1/n^2 $$, and smooth analytic waves decay exponentially.

## Key ideas: Euler–Fourier Projection and Coefficient Decay

1. **Orthogonal Projection in $$ L^2([-L, L]) $$ (Geometric Meaning):** Just as $$ c_k = \frac{\mathbf{v}\cdot \mathbf{e}_k}{\|\mathbf{e}_k\|^2} $$ extracts coordinates in $$ \mathbb{R}^n $$, the Euler–Fourier integrals $$ a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\!\left(\frac{n\pi x}{L}\right)dx $$ and $$ b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\!\left(\frac{n\pi x}{L}\right)dx $$ project $$ f $$ onto each orthogonal axis of the Hilbert space $$ L^2([-L, L]) $$.
2. **Best Mean-Square Approximation Property:** Among all trigonometric polynomials of degree $$ \le N $$, the $$ N $$-th Fourier partial sum $$ S_N(x) $$ uniquely minimizes the mean-square error $$ \int_{-L}^L |f(x) - T_N(x)|^2\,dx $$.
3. **Smoothness Governs Decay Rate (Integration by Parts):** Each time you integrate by parts, a factor of $$ \frac{L}{n\pi} $$ drops into the denominator. Therefore, a jump discontinuity forces $$ |a_n|, |b_n| = O(1/n) $$, a continuous function with a jump in $$ f' $$ decays as $$ O(1/n^2) $$, and a $$ C^k $$ periodic function decays as $$ o(1/n^k) $$.
4. **Riemann–Lebesgue Lemma:** For any integrable function $$ f \in L^1([-L, L]) $$, $$ a_n \to 0 $$ and $$ b_n \to 0 $$ as $$ n \to \infty $$—high-frequency oscillations eventually average out any integrable profile.

### Worked example: Full Fourier Coefficients of the Ramp $$ f(x) = x $$ on $$ (-\pi, \pi) $$

**Problem:** Compute all Fourier coefficients $$ a_0, a_n, b_n $$ of the $$ 2\pi $$-periodic extension of $$ f(x) = x $$ on $$ (-\pi, \pi) $$, inspect the $$ O(1/n) $$ decay rate, and test the $$ N = 3 $$ partial sum at $$ x = \frac{\pi}{2} $$.

1. **Exploit symmetry to find $$ a_0 $$ and $$ a_n $$ immediately:**
   Since $$ f(x) = x $$ is odd on the symmetric interval $$ (-\pi, \pi) $$ and $$ \cos(nx) $$ is even, the product $$ x\cos(nx) $$ is odd, so
   $$ a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} x\,dx = 0, \qquad a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\cos(nx)\,dx = 0 \quad (n \ge 1). $$
2. **Compute $$ b_n $$ using integration by parts:**
   Because $$ x\sin(nx) $$ is even,
   $$ b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin(nx)\,dx = \frac{2}{\pi}\int_{0}^{\pi} x\sin(nx)\,dx. $$
   Set $$ u = x, dv = \sin(nx)\,dx \implies du = dx, v = -\frac{\cos(nx)}{n} $$:
   $$ \int_0^\pi x\sin(nx)\,dx = \left[-\frac{x\cos(nx)}{n}\right]_0^\pi + \frac{1}{n}\int_0^\pi \cos(nx)\,dx = -\frac{\pi(-1)^n}{n} + 0 = \frac{(-1)^{n+1}\pi}{n}. $$
   Multiply by $$ \frac{2}{\pi} $$:
   $$ b_n = \frac{2(-1)^{n+1}}{n} \implies f(x) \sim 2\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \sin(nx). $$
3. **Check decay rate and evaluate at $$ x = \frac{\pi}{2} $$:**
   The periodic extension jumps from $$ +\pi $$ to $$ -\pi $$ at $$ x = \pm\pi $$, which explains why $$ |b_n| = \frac{2}{n} = O(1/n) $$.
   At $$ x = \frac{\pi}{2} $$, $$ \sin(n\pi/2) $$ is $$ 1, 0, -1, 0, 1, \dots $$, so
   $$ S_5\!\left(\frac{\pi}{2}\right) = 2\left(1 - \frac{1}{3} + \frac{1}{5}\right) = 2\left(\frac{13}{15}\right) = 1.7333 \quad \text{vs. exact } \frac{\pi}{2} \approx 1.5708. $$
   (And in the limit, $$ 2(1 - \frac{1}{3} + \frac{1}{5} - \cdots) = 2 \cdot \frac{\pi}{4} = \frac{\pi}{2} $$—recovering the famous Leibniz formula for $$ \pi $$!)

## Learning Objectives

This lesson explains how Fourier coefficients are computed and why orthogonality isolates each harmonic mode. Students should be able to derive coefficient formulas, interpret the coefficients as mode weights, and compute them for standard examples.

## Prerequisites

Students should already understand the basic Fourier-series idea, trigonometric orthogonality, and definite integration on symmetric intervals.

## Introduction

![Fourier coefficients]({{ site.imgurl }}/chapter_img/chapter08/02_fourier_coefficients.svg)

The brilliance of Fourier series is not only that periodic functions can be expanded into harmonic modes, but that the contribution of each mode can be extracted exactly. This works because the sine and cosine family is orthogonal on the fundamental interval.

That orthogonality acts like a filter. When we multiply by one mode and integrate, the other modes vanish. What remains is the coefficient we want. This makes the Fourier series one of the clearest examples in mathematics of how geometry, algebra, and analysis cooperate.

## Concept in Three Ways

### Intuitive View

Each Fourier coefficient measures how much of a specific harmonic is present in the function. A large coefficient means that mode contributes strongly; a small coefficient means it barely matters.

### Visual View

If we project a vector onto a coordinate axis, the projection tells us how much of the vector lies in that direction. Fourier coefficients do the same thing for functions: they project the function onto sine and cosine directions.

### Formal View

For period $$ 2L $$,
$$
a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos \frac{n\pi x}{L}\,dx,
$$
$$
b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin \frac{n\pi x}{L}\,dx,
$$
and
$$ a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\,dx. $$
These formulas follow because distinct trigonometric modes are mutually orthogonal.

## Why Coefficients Matter

The coefficients are the true data of the Fourier expansion. Once they are known, the periodic function has been translated into spectral form. This is exactly what makes Fourier analysis so useful in PDE: instead of working with the full function directly, we can work mode by mode.

Coefficient decay also carries information. Smooth functions typically have rapidly decaying coefficients, while rough or discontinuous functions have slower decay. This means that the coefficients not only reconstruct the function; they also reveal structural information about it.

## Common Misconceptions

### "The coefficient formulas are just memorized recipes"

No. They come directly from orthogonality and have a geometric meaning as projections.

### "The constant term is unimportant"

Wrong. The coefficient $$ a_0/2 $$ represents the average level of the function and is often physically meaningful.

### "All coefficients matter equally"

Not usually. Often the first few harmonics dominate the behavior, while higher modes contribute finer detail.

### "A difficult integral means the Fourier series idea has failed"

No. The method remains valid even when coefficient computation becomes technically challenging.

## Suggested Learning Path

### Step 1: Review orthogonality

Students should verify the basic integral identities for sine and cosine modes.

### Step 2: Derive the coefficient formulas

The derivation should feel like a projection argument, not a mysterious trick.

### Step 3: Compute coefficients in simple examples

Constant, linear, and piecewise functions are ideal first cases.

### Step 4: Interpret the results

Students should connect the size and pattern of coefficients to the visible shape of the function.

### Checkpoints

- Can students explain why multiplying by one mode and integrating isolates that coefficient?
- Do they understand the role of the average term $$ a_0/2 $$?
- Can they connect symmetry with vanishing coefficients when appropriate?

## Worked Examples

### Example 1: Constant Function

If $$ f(x)=1 $$ on $$ [-L,L] $$, then all oscillatory coefficients vanish and only the average term remains. This confirms that a constant function contains no nonzero harmonic oscillation.

### Example 2: A Single Cosine Mode

If $$ f(x)=\cos(2\pi x/L) $$, then only one cosine coefficient is nonzero. This is the cleanest illustration that the coefficient formulas correctly identify individual modes.

### Example 3: A Piecewise Function

For a square-wave-type function, many coefficients are nonzero. The computation is more involved, but it reveals that nonsmooth periodic functions require many harmonics.

## Conceptual Questions

1. Why do Fourier coefficients behave like projections?
2. Why does orthogonality make the coefficient formulas possible?
3. What can the size of coefficients tell us about the structure of a function?

## Application Problems

1. In acoustics, how do Fourier coefficients encode timbre?
2. In PDE solutions, why is solving mode-by-mode often easier than solving directly in physical space?
3. In signal analysis, why might a sparse coefficient set indicate a simple underlying signal?

## Interactive Teaching Strategies

- Have students derive the coefficient formulas from orthogonality in groups.
- Use geometric projection analogies from vectors to functions.
- Let students compute one easy coefficient by hand and then interpret it physically.
- Compare coefficient patterns for smooth and discontinuous functions.

## Differentiation

### Support for Struggling Students

Students needing support should spend extra time on orthogonality integrals and on the analogy with vector projections.

### Challenge for Advanced Students

Advanced students can explore coefficient decay rates and begin connecting them to smoothness and convergence questions.

## Summary

Fourier coefficients are the coordinates of a periodic function in the trigonometric basis. Computing them is the first major technical skill of the chapter, and understanding them conceptually prepares students for convergence theory, half-range expansions, and PDE mode analysis.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Audio spectrum analysis
- Problem: We want to know how much of each harmonic is present in a sound signal.
- Model:
$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,\qquad
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
$$
- Assumptions and limitations: The data are treated as one representative period or as a periodic extension.
- Interpretation: Fourier coefficients measure how strongly the signal overlaps each harmonic basis mode.

#### Forced periodic motion
- Problem: A complicated periodic forcing term can be separated into harmonic components.
- Model: Use the Fourier coefficients to write the forcing as a sum of sine and cosine modes.
- Assumptions and limitations: The forcing is idealized as periodic and sufficiently integrable.
- Interpretation: Large coefficients identify the harmonics that dominate the response.

### 2. Additional Intuition and Connections

Fourier coefficients are coordinates of a function in the orthogonal sine-cosine basis. A common misconception is that the formulas must simply be memorized. It is more useful to see them as orthogonal projections, exactly parallel to the coefficient formulas in Sturm-Liouville expansions.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 2000)
f = x

bn = []
N = 12
for n in range(1, N + 1):
    coeff = (1 / np.pi) * np.trapz(f * np.sin(n * x), x)
    bn.append(coeff)

plt.stem(range(1, N + 1), bn)
plt.xlabel("n")
plt.ylabel("b_n")
plt.title("Fourier spectrum of f(x)=x on (-pi,pi)")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Fourier coefficients spectrum visualization
- search: odd function sine coefficients example
- search: harmonic amplitudes bar chart signal processing

### 5. Worked Example

For
$$ f(x)=x,\qquad -\pi<x<\pi, $$
the function is odd, so $$ a_n=0 $$. Then
$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x\sin(nx)\,dx
=\frac{2(-1)^{n+1}}{n}.
$$
Hence
$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

### 6. Difficulty Layering

**Undergraduate level.** Compute $$ a_n $$ and $$ b_n $$ for even, odd, and piecewise simple functions.

**Graduate level.** Interpret the coefficients as orthogonal projections in Hilbert space and connect them to spectral energy content.

## Video tham khảo

- xem trước: [Computing Fourier Series | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=jzzpxqVohhI) — MIT OpenCourseWare, English. MIT computes the Fourier coefficients from the integral formulas.
- [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, English. Why those integrals are inner products against sines and cosines.
- [Manipulating Fourier Series | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=v4YcejwdQC0) — MIT OpenCourseWare, English. How to manipulate a series once the coefficients are known.

## References

- Haberman, Chapter 3: clear derivation and many computational examples.
