---
layout: post
title: "06-09 Interactive Illustrations Gallery"
chapter: '06'
order: 9
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: optional
---

Reading a recurrence relation like $$ a_{k+2} = -\frac{a_k}{(k+2)(k+1)} $$ on paper tells you the algebra, but watching partial sums peel off the true curve at the exact radius of convergence $$ R $$—or seeing a circular drumhead snap between Bessel nodal circles—locks the geometry into intuition permanently. This gallery turns every static series and special function from Chapter 06 into a live visual laboratory.

## Key ideas: How to Read Chapter 06 Visuals

1. **Truncation Horizon vs. Radius of Convergence:** When exploring power-series plots, notice that adding more terms improves accuracy dramatically inside $$ |x - x_0| < R $$, yet causes catastrophic divergence outside $$ R $$—a direct visual signature of complex-plane singularities.
2. **Indicial Exponents at Regular Singular Points:** In Euler and Frobenius visualizations, watch the slope and curvature right at $$ x = 0^+ $$: fractional powers create vertical tangents, negative powers blow up algebraically, and repeated roots bend with a subtle $$ \ln x $$ twist.
3. **Zero Distribution and Oscillation Decay (Bessel & Legendre):** Observe how $$ J_n(x) $$ decays like $$ x^{-1/2} $$ with nearly $$ \pi $$-spaced zeros for large $$ x $$, while $$ P_n(x) $$ packs all $$ n $$ of its zeros inside $$ (-1, 1) $$ with denser clustering near the endpoints $$ \pm 1 $$.
4. **Spectral Mode Synthesis:** In the physics frames, see how complicated radial or angular profiles are assembled by superposing orthogonal Bessel or Legendre modes—previewing Sturm–Liouville and Fourier analysis in Chapters 07–08.

### Worked example: Predicting What the Truncation Slider Will Show for $$ \frac{1}{1+x^2} $$

**Problem:** Before moving the truncation slider $$ N $$ in the gallery, compute the $$ N = 4 $$ partial sum $$ S_4(x) = 1 - x^2 + x^4 $$ of $$ f(x) = \frac{1}{1+x^2} $$ at $$ x = 0.5 $$ (inside $$ R = 1 $$) and at $$ x = 1.2 $$ (outside $$ R = 1 $$), and compare with the exact values.

1. **At $$ x = 0.5 $$ (inside $$ |x| < 1 $$):**
   - Exact value: $$ f(0.5) = \frac{1}{1 + 0.25} = \frac{1}{1.25} = 0.8000 $$.
   - Partial sum: $$ S_4(0.5) = 1 - 0.25 + 0.0625 = 0.8125 $$.
   - Error: $$ |S_4(0.5) - f(0.5)| = 0.0125 $$, and because the series alternates, increasing $$ N $$ to $$ 6 $$ shrinks the error to $$ \le 0.5^6 = 0.0156 $$ (actual error $$ 0.003125 $$).
2. **At $$ x = 1.2 $$ (outside $$ |x| < 1 $$):**
   - Exact value: $$ f(1.2) = \frac{1}{1 + 1.44} = \frac{1}{2.44} \approx 0.4098 $$.
   - Partial sum: $$ S_4(1.2) = 1 - 1.44 + 2.0736 = 1.6336 $$.
   - Adding the next term ($$ -1.2^6 = -2.9860 $$) sends $$ S_6(1.2) = -1.3524 $$—wildly diverging!
3. **Takeaway for the gallery:** That sudden wall at $$ |x| = 1 $$ is invisible on the real graph of $$ \frac{1}{1+x^2} $$, yet completely governs the animation because of the complex poles at $$ z = \pm i $$.

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 06 in one place. It is intended as a visual companion to the chapter's recurrence methods, special functions, and applications.

## What Is Included

- power series convergence and truncation
- recurrence relations and ordinary-point series solutions
- Euler equations and the Frobenius method
- Bessel, Legendre, and other special-function families
- mode-shape and spectral viewpoints in physics applications

{% include interactive-frame.html
  title="Chapter 06 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 06 topics."
  path="interactives/chapter06/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [Taylor series | Chapter 11, Essence of calculus](https://www.youtube.com/watch?v=3d6DsjIBzJ4) — 3Blue1Brown, English. Taylor polynomials as the pictures a series gallery is approximating.
- [Advanced Engineering Mathematics, Lecture 2.7: Bessel's equation](https://www.youtube.com/watch?v=lcvWAgrdFn0) — Professor Macauley, English. Bessel functions to compare with the special-function frames.
- [Intro to Legendre Polynomials](https://www.youtube.com/watch?v=djlUmwbPw20) — Physics and Math Lectures, English. Legendre polynomials as the other family drawn in the gallery.
