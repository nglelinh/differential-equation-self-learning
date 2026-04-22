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

## Purpose of This Companion Lesson

This lesson gathers the numerical-method visualizations of Chapter 13 into a single companion space. The main chapter develops discretization, local and global error, stiffness, stability regions, PDE finite-difference grids, finite-element intuition, and stochastic trajectories in a theorem-and-method sequence. The gallery gives these ideas a common visual setting so students can compare them without switching context from one lesson to another.

Numerical analysis becomes much easier to retain when its abstractions are tied to pictures. Stability is more memorable when one sees trajectories blow up or decay under different step sizes. A CFL restriction becomes more natural when the geometry of the computational stencil is visible. An SDE approximation is easier to interpret when deterministic drift and stochastic fluctuation are seen on the same axes.

## How to Use This Lesson

A good workflow is to revisit the gallery after reading a theorem or method from the main text. Use the visuals to ask what numerical quantity is actually being controlled: truncation error, amplification factor, stiffness response, mesh resolution, or weak versus strong approximation. This turns the gallery into a conceptual bridge between formulas and computational behavior.

The page is also useful as a review sheet before students move from ODE solvers to PDE discretization, since it keeps the language of consistency, convergence, and stability in one place.

## Embedded Interactive Gallery

{% include interactive-frame.html
  title="Chapter 13 Interactive Gallery"
  description="A companion space for Euler methods, Runge-Kutta schemes, multistep methods, stiffness, CFL stability, finite differences, finite elements, and stochastic differential equations."
  path="interactives/chapter13/index-en.html"
  height="980px"
%}

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
