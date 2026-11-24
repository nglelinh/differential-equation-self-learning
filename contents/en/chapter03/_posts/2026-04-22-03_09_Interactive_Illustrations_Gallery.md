---
layout: post
title: "03-09 Interactive Illustrations Gallery"
chapter: '03'
order: 9
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: optional
---

In the time domain, a damped wave, a rectangular switch, and a sharp hammer strike look completely unrelated; in the complex $$s$$-plane, they sit side by side as simple poles and exponential phase factors. This interactive gallery bridges both worlds visually so you can drag a pole across the imaginary axis and watch stability flip in real time, or slide two signals past each other to see convolution build an output curve point by point.

## Background Knowledge Map: Four Visual Bridges Between Time and the $$s$$-Plane

Look for these four visual correspondences as you manipulate the interactive widgets below:

1. **The $$s$$-Plane Pole–Behavior Map:** Horizontal position $$\sigma = \operatorname{Re}(s)$$ sets exponential decay ($$\sigma < 0$$) or blow-up ($$\sigma > 0$$); vertical height $$\omega = \operatorname{Im}(s)$$ sets oscillation speed; distance from the origin sets natural frequency $$\omega_n$$.
2. **Step & Impulse Response Comparison:** Because $$\delta(t) = u'(t)$$, the impulse response $$h(t)$$ is literally the derivative of the step response $$s(t)$$—visually, peaks of $$h(t)$$ align with the steepest slopes of $$s(t)$$, and zeros of $$h(t)$$ align with peaks/troughs of $$s(t)$$.
3. **Flip-and-Slide Convolution Geometry:** Watching $$g(\tau)$$ reflect to $$g(t - \tau)$$ and slide across $$f(\tau)$$ reveals why convolving two rectangular pulses produces a smooth triangle (one degree smoother!).
4. **Pole–Zero Geometry of Frequency Response:** Evaluating $$\lvert H(i\omega)\rvert$$ as $$i\omega$$ marches up the imaginary axis equals the product of distances to zeros divided by the product of distances to poles—explaining resonance peaks geometrically!

### Step-by-Step Worked Example (Read Slowly): Computing the Exact "Flip-and-Slide" Convolution of Two Unit Boxcars

Let $$f(t) = g(t) = u_0(t) - u_1(t)$$ (a unit pulse equal to $$1$$ on $$[0,1]$$ and $$0$$ elsewhere). Compute $$(f * g)(t)$$ analytically to match the sliding-overlap animation:

1. **Write the overlap integral:**
   $$(f * g)(t) = \int_0^t f(\tau)\,g(t - \tau)\,d\tau.$$
   The integrand equals $$1$$ precisely where *both* $$0 \le \tau \le 1$$ AND $$0 \le t - \tau \le 1 \iff t - 1 \le \tau \le t$$.
2. **Evaluate across the three overlap regimes:**
   - **Rising overlap ($$0 \le t \le 1$$):** Active interval is $$[0, t]$$, length $$t \implies (f * g)(t) = t$$.
   - **Falling overlap ($$1 < t \le 2$$):** Active interval is $$[t - 1, 1]$$, length $$1 - (t - 1) = 2 - t \implies (f * g)(t) = 2 - t$$.
   - **No overlap ($$t > 2$$):** Intervals are disjoint $$\implies (f * g)(t) = 0$$.
3. **Verify instantaneously in the $$s$$-domain:**
   $$F(s) = \frac{1 - e^{-s}}{s} \implies F(s)^2 = \frac{1 - 2e^{-s} + e^{-2s}}{s^2}.$$
   Inverting term by term gives $$t\,u_0(t) - 2(t - 1)u_1(t) + (t - 2)u_2(t)$$—the exact symmetric triangle peaking at $$(1, 1)$$!

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 03 in one place. It is meant to support intuition for transforms, inverse transforms, and systems viewpoints.

## What Is Included

- transform weighting and linearity
- elementary transform patterns and pole shifts
- inverse Laplace and partial fractions
- Laplace-based IVP solving, step inputs, impulses, convolution, and transfer functions

{% include interactive-frame.html
  title="Chapter 03 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 03 topics."
  path="interactives/chapter03/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [But what is a Laplace Transform?](https://www.youtube.com/watch?v=j0wJBEZdwLs) — 3Blue1Brown, English. A visual introduction to the transform before using the chapter's interactive frames.
- [The Laplace Transform - A Graphical Approach](https://www.youtube.com/watch?v=ZGPtPkTft8g) — Brian Douglas, English. Brian Douglas draws the Laplace transform, a picture to set beside the gallery.
- [Pole Diagrams | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=pUFSXhoazY8) — MIT OpenCourseWare, English. Poles and zeros as the graphic the gallery is helping students read.
