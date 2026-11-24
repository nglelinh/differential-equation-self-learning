---
layout: post
title: "Chapter 15 Interactive Gallery"
chapter: '15'
order: 10
owner: Course Team
lang: en
categories:
- chapter15
lesson_type: optional
---

> **Storytelling Hook:** Microlocal analysis lives in **phase space** $(x,\xi)$—twice the dimension of physical space—where singularities become sharp directional arrows, wave packets glide along classical orbits, and quantum eigenstates tile energy ellipses in discrete quantized rings. This interactive gallery lets you visualize and manipulate those phase-space phenomena directly.

## Purpose of This Companion Lesson

This lesson gathers the visual and interactive companions of Chapter 15 into one place. Microlocal analysis is conceptually demanding because it asks students to think simultaneously in physical space, frequency space, and phase space. The gallery helps by presenting wave front sets, propagation of singularities, semiclassical concentration, and spectral growth in a more geometric form.

The main lessons establish the definitions and theorems. This companion lesson helps students see what those theorems are trying to say. A bicharacteristic flow, for instance, is easier to remember when it is not only defined symbolically but also seen as a transport law for singular structure. Likewise, a semiclassical wave packet becomes more intuitive when one watches localization in position and frequency evolve together.

## How to Use This Lesson

The best use of this gallery is comparative. After studying a formal concept such as the wave front set or microlocal ellipticity, return to the interactive visualizations and ask which geometric feature is being encoded: localization, directional nonsmoothness, Hamiltonian transport, or high-frequency asymptotics. This helps students translate notation into mechanism.

The page also serves as a bridge between the advanced chapter text and later research reading, where the geometric viewpoint is usually assumed rather than explained from scratch.

## Background Knowledge Map: Navigating Phase-Space Visualizations in Chapter 15

Keep four visual cues in focus as you interact with the widgets in this gallery:

1. **Conormal Arrows for $\operatorname{WF}(u)$:** Notice how every sharp edge in physical space spawns phase-space arrows strictly *perpendicular* to the edge, whereas an isolated point singularity spawns a full $360^\circ$ fan of arrows.
2. **Bicharacteristic Rays vs. Caustics:** Watch how rays that cross and form bright cusps (caustics) in physical space $(x,y)$ never intersect when lifted into phase space $(x,y,\xi,\eta)$—their Lagrangian manifold stays completely smooth.
3. **Semiclassical Phase-Space Area Quantization:** In the harmonic oscillator and billiard widgets, each new quantum energy level encloses an extra $2\pi\hbar$ of phase-space area, visually proving Weyl's Law before your eyes.
4. **Limited-Angle Tomography Artifacts:** Restricting sensor angles in the inverse-problem widget visibly blurs only those edges whose normal vectors lie outside the scanned angular wedge.

## Embedded Interactive Gallery

{% include interactive-frame.html
  title="Chapter 15 Interactive Gallery"
  description="A visual companion for wave front sets, propagation of singularities, semiclassical wave packets, Weyl asymptotics, and other microlocal themes."
  path="interactives/chapter15/index-en.html"
  height="980px"
%}

### Step-by-Step Worked Example (Read Slowly): Checking Bohr–Sommerfeld Area Quantization for the Harmonic Oscillator

In the semiclassical phase-space widget for the 1D quantum harmonic oscillator $\hat{H} = -\frac{d^2}{dx^2} + x^2$ ($\hbar = 1$, classical symbol $H(x,\xi) = \xi^2 + x^2$), verify that the phase-space circle $H(x,\xi) \le E_n$ at the $n=2$ exact eigenvalue $E_2 = 2(2) + 1 = 5$ satisfies Bohr–Sommerfeld area quantization $\frac{\operatorname{Area}}{2\pi} = n + \frac{1}{2}$.

1. **Identify the classical energy contour at $E = 5$:**
   $$\xi^2 + x^2 = 5$$
   is a circle in the $(x,\xi)$ phase plane centered at $(0,0)$ of radius $R = \sqrt{5} \approx 2.236$.
2. **Compute its enclosed phase-space area:**
   $$\operatorname{Area}\big(\{(x,\xi) : \xi^2 + x^2 \le 5\}\big) = \pi R^2 = 5\pi.$$
3. **Divide by Planck's phase-space cell $2\pi\hbar = 2\pi$:**
   $$\frac{\operatorname{Area}}{2\pi} = \frac{5\pi}{2\pi} = \frac{5}{2} = 2 + \frac{1}{2} = n + \frac{1}{2} \quad (n = 2).$$
4. **Visual connection:** Because the harmonic oscillator is quadratic, Bohr–Sommerfeld quantization is *exact* for every $n = 0, 1, 2, \dots$: each successive energy ring in the interactive gallery adds an annulus of exact area $2\pi$!

## Suggested Study Prompts

1. Which interactive elements are about localization in space, and which are about directional information in cotangent space?
2. Where do the graphics suggest propagation laws rather than pointwise smoothness statements?
3. How does the gallery reinforce the shift from solving equations to reading the geometry of singularities?

## Lesson Links

- [15.00 Preparatory Review]({{ site.baseurl }}/contents/en/chapter15/15_00_Microlocal_Prerequisite_Review/)
- [15.01 Wave Front Sets]({{ site.baseurl }}/contents/en/chapter15/15_01_Wave_Front_Sets/)
- [15.02 Propagation of Singularities]({{ site.baseurl }}/contents/en/chapter15/15_02_Propagation_Singularities/)
- [15.03 Fourier Integral Operators]({{ site.baseurl }}/contents/en/chapter15/15_03_Fourier_Integral_Operators/)
- [15.04 Semiclassical Analysis]({{ site.baseurl }}/contents/en/chapter15/15_04_Semiclassical_Analysis/)
- [15.05 Spectral Asymptotics]({{ site.baseurl }}/contents/en/chapter15/15_05_Spectral_Asymptotics/)
- [15.06 Inverse Problems]({{ site.baseurl }}/contents/en/chapter15/15_06_Inverse_Problems/)
- [15.07 Quantum Mechanics]({{ site.baseurl }}/contents/en/chapter15/15_07_Quantum_Mechanics/)
- [15.08 Current Research Directions]({{ site.baseurl }}/contents/en/chapter15/15_08_Current_Research_Directions/)
- [15.09 Microlocal Elliptic Theory]({{ site.baseurl }}/contents/en/chapter15/15_09_Microlocal_Elliptic_Theory/)

## Video tham khảo

- xem trước: [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, English. The lecture whose phase-space pictures the gallery is sketching.
- [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, English. Fourier space, the second coordinate of a wavefront set.
- [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), English. A research talk to show the pictures in use.
