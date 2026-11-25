---
layout: post
title: "Chapter 00 Illustration Gallery"
chapter: '00'
order: 12
owner: Course Team
lang: en
categories:
- chapter00
lesson_type: optional
---

A formula like $$e^{At}$$ or $$\lvert f(x) - f(y)\rvert \le L\lvert x - y\rvert$$ can look dry on paper, yet each one encodes a vivid geometric picture: a cone bounding slopes, a vector field twisting space into eigen-axes, or a complex spiral pulsing in the plane. This gallery brings those invisible mental models into view so that when you meet Picard iteration, phase portraits, and Laplace poles in later chapters, you recognize their geometry immediately.

## Key ideas: Four Visual Languages of Mathematical Foundations

As you explore the interactive figures below, connect each visual to the analytical pillar it represents:

1. **$$\varepsilon$$–$$\delta$$ Boxes and Lipschitz Cones (Real Analysis):** Visualizes continuity as trapping a curve inside a horizontal $$\varepsilon$$-band and Lipschitz continuity as restricting the graph inside a double cone of fixed slope $$\pm L$$.
2. **Tangent Planes and Gradient Fields (Multivariable Calculus):** Shows how a nonlinear map looks locally like its Jacobian matrix and why gradient arrows always cross level sets orthogonally.
3. **Invariant Lines and Eigen-Deformations (Linear Algebra):** Reveals eigenvectors as the rare directions that a linear map stretches without rotating—the straight-line trajectories of linear ODE systems.
4. **Unit-Circle Rotation and Spirals (Complex Exponentials):** Maps $$\alpha + i\beta$$ directly to radial growth/decay ($$\alpha$$) and angular frequency ($$\beta$$), turning abstract complex roots into immediate motion.

### Worked example: Reading Four Foundational Quantities from One Visual Model

Consider the planar linear map $$\mathbf{F}(x,y) = (x - 2y,\; 2x + y)$$, which combines every pillar in this gallery:

1. **Matrix and Jacobian representation:** Since $$\mathbf{F}$$ is linear, its Jacobian everywhere is
   $$A = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}.$$
2. **Complex-number identification:** Identifying $$(x,y) \leftrightarrow z = x + iy$$, notice that
   $$(1 + 2i)(x + iy) = (x - 2y) + i(2x + y).$$
   So the matrix $$A$$ is literally multiplication by the complex number $$1 + 2i$$!
3. **Polar geometry (scaling + rotation):** Compute modulus and argument:
   $$r = \sqrt{1^2 + 2^2} = \sqrt{5} \approx 2.236, \qquad \theta = \arctan(2) \approx 63.43^\circ.$$
   Every vector in the plane is scaled by $$\sqrt{5}$$ and rotated counterclockwise by $$63.43^\circ$$.
4. **Lipschitz constant and uniform continuity:** Because $$\|\mathbf{F}(\mathbf{u}) - \mathbf{F}(\mathbf{v})\|_2 = \sqrt{5}\,\|\mathbf{u} - \mathbf{v}\|_2$$ for all $$\mathbf{u}, \mathbf{v} \in \mathbb{R}^2$$, the map is globally Lipschitz with exact Lipschitz constant $$L = \sqrt{5}$$, and its continuous-time counterpart $$\mathbf{x}' = A\mathbf{x}$$ produces outward spirals $$e^{t}\bigl(\cos 2t + i\sin 2t\bigr)z_0$$.

## Purpose of This Companion Lesson

This lesson gathers the currently published Chapter 00 illustrations into one visual review space. Mathematical foundations can feel fragmented when they are taught as separate prerequisite topics, but the entire course depends on them as one connected language. The gallery helps students see that continuity, multivariable calculus, linear algebra, and complex numbers are not isolated preliminaries. They are the infrastructure behind later existence theorems, phase-space models, spectral ideas, and solution formulas.

Because the English Chapter 00 sequence is still only partially published in this workspace, this gallery follows the lessons that are currently available on the English side and keeps the visual thread intact for those core topics.

## How to Use This Lesson

Work through the gallery in lesson order and ask what later differential-equation idea each foundation supports. Real analysis supports existence and compactness arguments; multivariable calculus supports Jacobians and linearization; linear algebra supports systems and eigenmodes; complex numbers support oscillation and exponential solutions. The goal is to make Chapter 00 feel like the hidden skeleton of the rest of the course.

## Embedded Gallery

{% include interactive-frame.html
  title="Chapter 00 Illustration Gallery"
  description="A visual companion for the currently published mathematical foundations lessons in Chapter 00."
  path="interactives/chapter00/index-en.html"
  height="980px"
%}

## Suggested Study Prompts

1. Which foundational topics later reappear most directly in ODE chapters, and which become more important in PDE and functional analysis?
2. Where do qualitative ideas such as compactness and continuity sit beside algebraic ideas such as eigenvectors and complex exponentials?
3. How do these early concepts change meaning when they move from finite-dimensional examples to infinite-dimensional spaces later in the course?

## Lesson Links

- [00.01 Real Analysis Review]({{ site.baseurl }}/contents/en/chapter00/00_01_00_Real_Analysis_Review/)
- [00.02 Continuity and Uniform Continuity]({{ site.baseurl }}/contents/en/chapter00/00_01_01_Continuity_and_Uniform_Continuity/)
- [00.03 Derivatives and Multivariable Calculus]({{ site.baseurl }}/contents/en/chapter00/00_01_02_Derivatives_and_Multivariable_Calculus/)
- [00.04 Linear Algebra Essentials]({{ site.baseurl }}/contents/en/chapter00/00_03_00_Linear_Algebra_Essentials/)
- [00.05 Complex Numbers and Exponentials]({{ site.baseurl }}/contents/en/chapter00/00_04_00_Complex_Numbers_and_Exponentials/)

## Video tham khảo

- xem trước: [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) — 3Blue1Brown, English. The visual tour of what a differential equation is, matching the pictures this gallery is for.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, English. Animated calculus that makes the derivative and integral pictures in the gallery easier to read.
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) — 3Blue1Brown, English. Eigenvectors drawn as stretching directions, the picture behind the linear-algebra frames of this chapter.
