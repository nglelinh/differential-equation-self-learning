---
layout: post
title: "04-11 Interactive Illustrations Gallery"
chapter: '04'
order: 11
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: optional
---

A $$2\times 2$$ matrix is just four numbers in brackets, yet those four numbers sculpt an entire vector field across the plane: stretching one axis, squashing another, or twisting every point into a logarithmic vortex. This interactive gallery lets you tweak matrix entries and watch eigenvectors snap together, vanish into complex spirals, or transform two coupled masses into pure synchronous modes.

## Key ideas: Four Geometric Signatures to Spot in the Gallery

Connect every interactive slider below to its underlying Chapter 04 theorem:

1. **Invariant Eigenspaces:** In any real-distinct phase portrait, look for the exact two straight lines through the origin where velocity arrows point strictly along the line—every other trajectory curves between them, departing parallel to the larger eigenvalue and arriving tangent to the smaller one.
2. **Crossing the Discriminant Parabola ($$\tau^2 = 4\Delta$$):** Watch the two straight eigen-lines scissor closer together as $$\tau^2 - 4\Delta \to 0^+$$; at the exact moment they collide (defective repeated eigenvalue), only *one* straight line survives, and an instant later both vanish into a spiral!
3. **Matrix Exponential Deformation:** Tracking a unit circle of initial conditions $$\{\mathbf{x}_0 : \|\mathbf{x}_0\| = 1\}$$ under $$e^{At}$$ turns the circle into a rotating, stretching ellipse whose area grows at the exact Liouville rate $$e^{\operatorname{tr}(A)t}$$.
4. **Normal-Mode Superposition:** Toggling individual mode amplitudes in the coupled-oscillator widget shows immediately how adding just two pure cosines produces complex beating patterns.

### Worked example: Predicting an Ellipse's Area and Axes Under $$e^{At}$$

Let $$A = \begin{pmatrix} -1 & 3 \\ 0 & -2 \end{pmatrix}$$ act on the unit disk $$D_0 = \{\mathbf{x} \in \mathbb{R}^2 : \|\mathbf{x}\| \le 1\}$$ (initial area $$\pi$$) from $$t = 0$$ to $$t = 1$$.

1. **Predict the exact area at $$t = 1$$ via Liouville's formula—before computing $$e^{At}$$:**
   $$\operatorname{tr}(A) = -1 + (-2) = -3 \implies \text{Area}(D_1) = \pi\,e^{\operatorname{tr}(A)\cdot 1} = \pi\,e^{-3} \approx \mathbf{0.1564}.$$
   The unit disk shrinks to just $$4.98\%$$ of its original area in one second!
2. **Find the exact eigen-lines (the straight highways in the phase portrait):**
   - $$\lambda_1 = -1$$ (slow mode): $$(A + I)\mathbf{v}_1 = \begin{pmatrix} 0 & 3 \\ 0 & -1 \end{pmatrix}\mathbf{v}_1 = \mathbf{0} \implies \mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ (the $$x_1$$-axis).
   - $$\lambda_2 = -2$$ (fast mode): $$(A + 2I)\mathbf{v}_2 = \begin{pmatrix} 1 & 3 \\ 0 & 0 \end{pmatrix}\mathbf{v}_2 = \mathbf{0} \implies \mathbf{v}_2 = \begin{pmatrix} -3 \\ 1 \end{pmatrix}$$.
3. **Compute $$e^{At}$$ and confirm $$\det(e^{At}) = e^{-3t}$$:**
   With $$P = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$$ and $$P^{-1} = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$$:
   $$e^{At} = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} e^{-t} & 0 \\ 0 & e^{-2t} \end{pmatrix}\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{-t} & 3(e^{-t} - e^{-2t}) \\ 0 & e^{-2t} \end{pmatrix}.$$
   Check determinant: $$\det(e^{At}) = e^{-t}\cdot e^{-2t} = e^{-3t}$$—exact match with Liouville!

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 04 in one place. It is intended to reinforce the chapter's geometric systems viewpoint.

## What Is Included

- matrix form, vector fields, and eigendirections
- real, complex, and repeated eigenvalue behavior
- matrix exponentials, phase portraits, and nonhomogeneous systems
- coupled oscillators and compartment models

{% include interactive-frame.html
  title="Chapter 04 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 04 topics."
  path="interactives/chapter04/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [Phase Portraits | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=zmzyW1rP-hk) — MIT OpenCourseWare, English. The phase portraits this gallery is asking students to recognize.
- [Trace-Determinant Diagram | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=oEskbXrhkkk) — MIT OpenCourseWare, English. Trace and determinant as the controls behind those pictures.
- [How (and why) to raise e to the power of a matrix | DE6](https://www.youtube.com/watch?v=O85OWBJ2ayo) — 3Blue1Brown, English. The matrix exponential as the motion that draws a linear trajectory.
