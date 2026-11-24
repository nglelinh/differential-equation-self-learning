---
layout: post
title: "Chapter 11 Illustration Gallery"
chapter: '11'
order: 9
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: optional
---

> **Storytelling Hook:** Before a single theorem is proved in potential theory, its truth is already visible in the geometry of a plot: harmonic surfaces always curve like saddles, equipotentials cross flux lines at exact right angles, and jagged boundary data melts into silk-smooth contours just millimeters inside the domain. This gallery turns those visual signatures into geometric intuition.

## Purpose of This Companion Lesson

This lesson gathers the Chapter 11 illustrations into one visual review space. Laplace and Poisson equations introduce the elliptic worldview in its clearest classical form: equilibrium replaces evolution, boundary data control the interior, and qualitative structure becomes just as important as explicit formulas. The gallery helps students keep those themes connected across the full chapter.

The main lessons move through geometry, source terms, qualitative principles, representation formulas, and applications. This companion lesson makes it easier to compare those pieces at a glance: rectangles versus disks, source-free versus sourced problems, averaging behavior versus extremum control, and abstract harmonic theory versus concrete physical fields. That overview is especially useful before the course turns toward functional analysis and weak formulations.

## How to Use This Lesson

Work through the gallery in lesson order. After each figure, return to the corresponding lecture and ask what mathematical structure the image is emphasizing: boundary control, coordinate adaptation, forcing, harmonic rigidity, Green-function response, or physical interpretation. This turns the page into a bridge between formal elliptic theory and geometric understanding.

The lesson also serves as a good review before Chapter 12, because it clarifies what aspects of elliptic PDEs will later be reformulated in functional-analytic language.

## Background Knowledge Map: Reading the Visual Signatures of Elliptic PDEs

Every diagram in this chapter encodes a deep analytical theorem; four visual principles help you decode them immediately:

1. **Saddle Curvature and Absence of Peaks:** Since $u_{xx} + u_{yy} = 0$, positive curvature in one direction forces equal negative curvature in the orthogonal direction. Visually, harmonic surfaces cannot form isolated domes or bowls inside the domain—every interior critical point is a saddle.
2. **Orthogonal Equipotential–Streamline Nets:** For conjugate harmonic pairs $(u,v)$, $\nabla u \cdot \nabla v = 0$ and $|\nabla u| = |\nabla v|$, meaning their level sets tile the plane into tiny curvilinear squares (conformal grids).
3. **Exponential Interior Smoothing:** High-frequency oscillations on $\partial\Omega$ decay like $r^n$ (on a disk) or $e^{-n\pi d/a}$ (in a rectangle) as distance $d$ from the boundary grows, visually erasing sharp corners and ripples inside the domain.
4. **Logarithmic and $1/r$ Singular Spikes of Green's Functions:** Green's function plots display a sharp funnel centered at the source $y$ that smoothly flattens to zero on $\partial\Omega$, illustrating how boundary geometry distorts the free-space impulse response.

## Embedded Gallery

{% include interactive-frame.html
  title="Chapter 11 Illustration Gallery"
  description="A visual companion for harmonic functions, boundary-value structure, Poisson forcing, Green-function methods, and the main applications of Laplace and Poisson equations."
  path="interactives/chapter11/index-en.html"
  height="980px"
%}

### Step-by-Step Worked Example (Read Slowly): Quantifying Visual Harmonic Smoothing on the Unit Disk

When you look at the gallery plots of harmonic functions on a disk, boundary ripples seem to vanish almost instantly toward the center. Let us put an exact number on that visual phenomenon by comparing a low-frequency boundary wave $f_1(\theta) = \cos(\theta)$ against a high-frequency ripple $f_{10}(\theta) = \cos(10\theta)$ on the unit disk $r \le 1$.

1. **Write the exact harmonic extensions:** By polar separation of variables,
   $$u_1(r,\theta) = r\cos(\theta), \qquad u_{10}(r,\theta) = r^{10}\cos(10\theta).$$
   On the boundary $r = 1$, both functions have identical peak amplitude $1$.
2. **Evaluate peak amplitudes halfway to the center ($r = 0.5$):**
   $$\max_\theta |u_1(0.5,\theta)| = 0.5 = 50\%, \qquad \max_\theta |u_{10}(0.5,\theta)| = (0.5)^{10} = \frac{1}{1024} \approx 0.000977 \; (< 0.1\%).$$
3. **Evaluate at $r = 0.8$ (still close to the rim):**
   $$\max_\theta |u_1(0.8,\theta)| = 0.800, \qquad \max_\theta |u_{10}(0.8,\theta)| = (0.8)^{10} \approx 0.1074.$$
4. **Geometric takeaway:** Even 20% of the way inside the disk, the $n=10$ ripple has already lost nearly 90% of its amplitude, and halfway in it is invisible to the naked eye—which is why interior contour plots of harmonic functions are dominated by only their lowest Fourier modes.

## Suggested Study Prompts

1. Which figures emphasize explicit solution structure, and which emphasize qualitative control without solving the PDE completely?
2. Where do geometry and boundary data most clearly determine the interior behavior?
3. How do the application figures reinterpret the same elliptic framework in different physical settings?

## Lesson Links

- [11.01 Laplace's Equation: Introduction]({{ site.baseurl }}/contents/en/chapter11/11_01_Laplace_Equation_Introduction/)
- [11.02 Separation of Variables in Rectangles]({{ site.baseurl }}/contents/en/chapter11/11_02_Separation_of_Variables_Rectangles/)
- [11.03 Laplace's Equation in Polar Coordinates]({{ site.baseurl }}/contents/en/chapter11/11_03_Laplace_Polar_Coordinates/)
- [11.04 Poisson's Equation]({{ site.baseurl }}/contents/en/chapter11/11_04_Poisson_Equation/)
- [11.05 Mean Value Property and Maximum Principle]({{ site.baseurl }}/contents/en/chapter11/11_05_Mean_Value_Maximum_Principle/)
- [11.06 Green's Functions for Laplace]({{ site.baseurl }}/contents/en/chapter11/11_06_Greens_Functions_Laplace/)
- [11.07 Applications: Electrostatics]({{ site.baseurl }}/contents/en/chapter11/11_07_Applications_Electrostatics/)
- [11.08 Applications: Fluid Flow]({{ site.baseurl }}/contents/en/chapter11/11_08_Applications_Fluid_Flow/)

## Video tham khảo

- xem trước: [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, English. A rectangular Laplace solution to compare with the gallery.
- [Laplace's Equation and Potential Flow](https://www.youtube.com/watch?v=zN0zDrQimXU) — Steve Brunton, English. Potential-flow pictures.
- [Divergence and curl:  The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) — 3Blue1Brown, English. The vector-calculus fields the frames are drawing.
