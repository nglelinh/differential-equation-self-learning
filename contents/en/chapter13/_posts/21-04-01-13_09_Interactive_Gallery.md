---
layout: post
title: "Chapter 13 Interactive Gallery"
chapter: '13'
order: 9
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: optional
---

> **Storytelling Hook:** Nothing teaches numerical stability faster than dragging a step-size slider across the critical threshold and watching a smooth wave or orbit shatter into chaos in real time. This interactive gallery lets you experiment directly with Euler spirals, RK4 accuracy, CFL cones, and stochastic paths.

## Purpose of This Companion Lesson

This lesson gathers the numerical-method visualizations of Chapter 13 into a single companion space. The main chapter develops discretization, local and global error, stiffness, stability regions, PDE finite-difference grids, finite-element intuition, and stochastic trajectories in a theorem-and-method sequence. The gallery gives these ideas a common visual setting so students can compare them without switching context from one lesson to another.

Numerical analysis becomes much easier to retain when its abstractions are tied to pictures. Stability is more memorable when one sees trajectories blow up or decay under different step sizes. A CFL restriction becomes more natural when the geometry of the computational stencil is visible. An SDE approximation is easier to interpret when deterministic drift and stochastic fluctuation are seen on the same axes.

## How to Use This Lesson

A good workflow is to revisit the gallery after reading a theorem or method from the main text. Use the visuals to ask what numerical quantity is actually being controlled: truncation error, amplification factor, stiffness response, mesh resolution, or weak versus strong approximation. This turns the gallery into a conceptual bridge between formulas and computational behavior.

The page is also useful as a review sheet before students move from ODE solvers to PDE discretization, since it keeps the language of consistency, convergence, and stability in one place.

## Background Knowledge Map: What to Watch in Numerical Simulation Widgets

Keep four diagnostic signatures in mind as you manipulate the interactive controls:

1. **Stability Regions in the Complex $z = h\lambda$ Plane:** Oscillatory systems place $z$ on the imaginary axis ($z = i\omega h$), while dissipative systems place $z$ on the negative real axis; a method's shaded stability region immediately tells you which physics it can handle.
2. **Phase Error vs. Amplitude Error (Dispersion vs. Dissipation):** On wave and oscillator widgets, notice whether the numerical curve shrinks/grows in height (amplitude error) or drifts ahead/behind the exact wave (phase dispersion).
3. **CFL Cone Violation:** When a hyperbolic Courant number exceeds $1$, watch how high-frequency grid-scale zigzags erupt first—because the stencil cannot "see" the physical information arriving from upstream.
4. **Ensemble Mean vs. Sample Path Noise in SDEs:** Increasing the number of Monte Carlo trajectories shrinks the sampling error of the mean like $1/\sqrt{M}$, while each individual trajectory retains its full Brownian roughness.

## Embedded Interactive Gallery

{% include interactive-frame.html
  title="Chapter 13 Interactive Gallery"
  description="A companion space for Euler methods, Runge-Kutta schemes, multistep methods, stiffness, CFL stability, finite differences, finite elements, and stochastic differential equations."
  path="interactives/chapter13/index-en.html"
  height="980px"
%}

### Step-by-Step Worked Example (Read Slowly): Testing Energy Conservation on the Imaginary Axis ($z = i\omega h$)

Before experimenting with the oscillator widget, test three classic integrators on the undamped rotation $y' = i\omega y$ (whose exact solution $|y(t)| = |y_0|$ conserves energy forever) by computing $|R(i\theta)|$ where $\theta = \omega h > 0$.

1. **Forward Euler ($R(z) = 1 + z$):**
   $$|R(i\theta)| = |1 + i\theta| = \sqrt{1 + \theta^2} > 1 \quad \text{for every } \theta > 0.$$
   No matter how tiny $h$ is, forward Euler spirals **outward**, pumping artificial energy into the oscillator!
2. **Backward Euler ($R(z) = \frac{1}{1 - z}$):**
   $$|R(i\theta)| = \frac{1}{|1 - i\theta|} = \frac{1}{\sqrt{1 + \theta^2}} < 1 \quad \text{for every } \theta > 0.$$
   Backward Euler is unconditionally stable, yet it spirals **inward**, artificially damping a frictionless oscillator.
3. **Crank–Nicolson / Trapezoidal Rule ($R(z) = \frac{1 + z/2}{1 - z/2}$):**
   $$|R(i\theta)| = \frac{|1 + i\theta/2|}{|1 - i\theta/2|} = \frac{\sqrt{1 + \theta^2/4}}{\sqrt{1 + \theta^2/4}} = 1 \quad \text{for every } \theta > 0.$$
   Crank–Nicolson preserves $|y_n| = |y_0|$ **identically** at every step—which is why you will see its phase-space orbit stay locked on the exact unit circle in the interactive gallery!

## Suggested Study Prompts

1. Which visualizations are primarily about accuracy, and which are primarily about stability?
2. Where do you see the difference between a geometric ODE intuition and a genuinely discrete numerical phenomenon?
3. How do the PDE and SDE examples broaden the meaning of numerical approximation beyond the classical initial-value problem?

## Lesson Links

- [13.00 Preparatory Review]({{ site.baseurl }}/contents/en/chapter13/13_00_Discretization_and_Stability_Review/)
- [13.01 Euler's Method]({{ site.baseurl }}/contents/en/chapter13/13_01_Eulers_Method/)
- [13.02 Runge-Kutta Methods]({{ site.baseurl }}/contents/en/chapter13/13_02_Runge_Kutta_Methods/)
- [13.03 Multistep Methods]({{ site.baseurl }}/contents/en/chapter13/13_03_Multistep_Methods/)
- [13.04 Stiff Equations]({{ site.baseurl }}/contents/en/chapter13/13_04_Stiff_Equations/)
- [13.05 Finite Differences for PDEs]({{ site.baseurl }}/contents/en/chapter13/13_05_Finite_Differences_PDEs/)
- [13.06 Stability and Convergence (CFL)]({{ site.baseurl }}/contents/en/chapter13/13_06_Stability_Convergence_CFL/)
- [13.07 Finite Element Introduction]({{ site.baseurl }}/contents/en/chapter13/13_07_Finite_Element_Introduction/)
- [13.08 Stochastic Differential Equations]({{ site.baseurl }}/contents/en/chapter13/13_08_Stochastic_Differential_Equations/)

## Video tham khảo

- xem trước: [Runge-Kutta Integrator Overview:  All Purpose Numerical Integration of Differential Equations](https://www.youtube.com/watch?v=HOWJp8NV5xU) — Steve Brunton, English. Runge-Kutta, one of the schemes the gallery is comparing.
- [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, English. Euler steps, the other scheme on the same pictures.
- [Chaotic Dynamical Systems](https://www.youtube.com/watch?v=PDeN3iCtyNY) — Steve Brunton, English. Chaotic dynamics, where a stable scheme still cannot predict far ahead.
