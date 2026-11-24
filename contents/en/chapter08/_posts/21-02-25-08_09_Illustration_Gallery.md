---
layout: post
title: "Chapter 08 Illustration Gallery"
chapter: '08'
order: 9
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: optional
---

Seeing a square wave assemble itself harmonic by harmonic—watching the flat plateau tighten while the tiny Gibbs horns refuse to shrink—teaches more about Fourier convergence in ten seconds than a page of inequalities. This companion gallery brings every core concept of Chapter 08 to life: partial-sum synthesis, even/odd reflections, Parseval energy bars, and the continuous frequency limit of the Fourier transform.

## Background Knowledge Map: Reading the Chapter 08 Visual Lab

1. **Harmonic Addition & Gibbs Persistence:** As you increase $$ N $$ in the partial-sum frames, verify that smooth regions converge rapidly while the peak overshoot next to a jump stays stubbornly locked at $$ \approx 8.95\% $$ of the jump height.
2. **Even vs. Odd Half-Range Extensions:** Toggle between sine and cosine extensions on $$ [0, L] $$ and look at the endpoints $$ x = 0 $$ and $$ x = L $$—watch how artificial jumps in the odd extension slow convergence compared to a continuous even reflection.
3. **Spectral Decay vs. Regularity:** Compare the bar-chart heights of $$ |a_n|, |b_n| $$ across a square wave ($$ 1/n $$), a triangle wave ($$ 1/n^2 $$), and a smooth periodic bump (exponential decay).
4. **Discrete-to-Continuous Spectrum Morphing:** In the Fourier transform frame, stretch the period $$ 2L $$ and watch the discrete vertical spectral lines pack together into a smooth continuous envelope $$ \hat{f}(\omega) $$.

### Step-by-Step Worked Example (Read Slowly): Predicting the First Three Harmonics of a Triangle Wave Before Moving the Slider

**Problem:** For the $$ 2\pi $$-periodic triangle wave $$ f(x) = |x| $$ on $$ [-\pi, \pi] $$, we found $$ f(x) = \frac{\pi}{2} - \frac{4}{\pi}\bigl(\cos x + \frac{1}{9}\cos 3x + \frac{1}{25}\cos 5x + \cdots\bigr) $$. Compute the maximum error of the $$ 2 $$-harmonic approximation $$ S_1(x) = \frac{\pi}{2} - \frac{4}{\pi}\cos x $$ at the corner $$ x = 0 $$ and at $$ x = \frac{\pi}{2} $$.

1. **At the sharp corner $$ x = 0 $$ (where $$ f(0) = 0 $$):**
   $$ S_1(0) = \frac{\pi}{2} - \frac{4}{\pi} \approx 1.5708 - 1.2732 = 0.2976. $$
   Adding just the $$ n = 3 $$ term subtracts $$ \frac{4}{9\pi} \approx 0.1415 $$, dropping the corner error in half to $$ 0.1561 $$.
2. **At the smooth midpoint $$ x = \frac{\pi}{2} $$ (where $$ f(\pi/2) = \frac{\pi}{2} $$):**
   Since $$ \cos((2k+1)\pi/2) = 0 $$ for *every* odd harmonic, $$ S_1(\pi/2) = \frac{\pi}{2} $$ is already **exact** (error $$ = 0 $$)!
3. **What to check in the gallery:** Watch how the error concentrates exclusively at the sharp corners $$ x = 0, \pm\pi $$—and notice zero Gibbs overshoot because $$ |x| $$ is continuous!

## Purpose of This Companion Lesson

This lesson gathers the Chapter 08 illustrations into one visual study space so students can move back and forth between the formal theory of Fourier series and a more geometric intuition. Instead of reading each figure only in isolation inside a single lesson, the gallery lets us compare periodic extension, coefficient decay, convergence behavior, symmetry, half-range constructions, Parseval energy balance, complex modes, and the transition from Fourier series to the Fourier transform on one page.

The aim is not to replace the main lessons. It is to give students a visual laboratory for Chapter 08. A Fourier series often becomes much clearer when one can see several partial sums, spectra, and symmetry patterns side by side.

## How to Use the Gallery

Work through the gallery in the same order as the chapter lessons. After revisiting a specific figure, return to the corresponding lesson and ask what analytical statement the image is trying to encode. For example, a bar chart of coefficients should suggest orthogonality and projection, while overshoot near a jump should lead naturally to the Gibbs phenomenon and questions of pointwise convergence.

Students can also use this page for review before moving into the heat equation, wave equation, and transform methods, since those chapters rely heavily on the same visual instincts developed here.

## Embedded Gallery

{% include interactive-frame.html
  title="Chapter 08 Illustration Gallery"
  description="A visual companion for Fourier series, orthogonal expansions, convergence, symmetry, Parseval's theorem, and the introductory Fourier transform viewpoint."
  path="interactives/chapter08/index-en.html"
  height="980px"
%}

## Suggested Study Prompts

1. Which figures are about approximation in physical space, and which are about organization in frequency space?
2. In which images do symmetry assumptions reduce computational complexity?
3. How does the visual language of Chapter 08 prepare the ground for PDE chapters where eigenfunctions and transforms become solution tools?

## Lesson Links

- [08.01 Periodic Functions and Fourier Series]({{ site.baseurl }}/contents/en/chapter08/08_01_Periodic_Functions_Fourier_Series/)
- [08.02 Fourier Coefficients]({{ site.baseurl }}/contents/en/chapter08/08_02_Fourier_Coefficients/)
- [08.03 Convergence of Fourier Series]({{ site.baseurl }}/contents/en/chapter08/08_03_Convergence_Fourier_Series/)
- [08.04 Even and Odd Functions]({{ site.baseurl }}/contents/en/chapter08/08_04_Even_Odd_Functions/)
- [08.05 Half-Range Expansions]({{ site.baseurl }}/contents/en/chapter08/08_05_Half_Range_Expansions/)
- [08.06 Parseval's Theorem]({{ site.baseurl }}/contents/en/chapter08/08_06_Parsevals_Theorem/)
- [08.07 Complex Fourier Series]({{ site.baseurl }}/contents/en/chapter08/08_07_Complex_Fourier_Series/)
- [08.08 Fourier Transform: Introduction]({{ site.baseurl }}/contents/en/chapter08/08_08_Fourier_Transform_Introduction/)

## Video tham khảo

- xem trước: [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, English. The circle-drawing animation this gallery is echoing.
- [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, English. The transform pictures to set beside the gallery frames.
- [Complex Fourier Series](https://www.youtube.com/watch?v=4cfctnaHyFM) — Steve Brunton, English. The complex series as rotating phasors, another gallery picture.
