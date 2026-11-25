---
layout: post
title: "07-08 Interactive Illustrations Gallery"
chapter: '07'
order: 8
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: optional
---

Boundary value problems come alive the moment you can drag a shooting slope, slide an eigenvalue parameter $$ \lambda $$, or move a point-load position $$ s $$ along a beam. Instead of memorizing why $$ \lambda_n = (n\pi/L)^2 $$ or why a Green's function has a corner at $$ x = s $$, this interactive gallery lets you *see* the boundary mismatch vanish at each eigenvalue and watch eigenfunction partial sums converge in real time.

## Key ideas: What to Watch in the Chapter 07 Gallery

1. **Shooting-Method Sensitivity:** As you sweep $$ \lambda $$ in the BVP frames, watch the right-endpoint value $$ y(L; \lambda) $$ cross zero repeatedly—each zero crossing is an exact eigenvalue where a nontrivial standing wave locks between the walls.
2. **Sturm Oscillation & Nodal Interlacing:** Compare consecutive eigenfunctions $$ \phi_n $$ and $$ \phi_{n+1} $$: count the interior zeros ($$ n-1 $$ vs. $$ n $$) and verify Sturm's separation theorem—between any two zeros of $$ \phi_n $$, there is always a zero of $$ \phi_{n+1} $$.
3. **Green's Function Tent Geometry:** Move the impulse location $$ s $$ across $$ [0, L] $$ and watch the kink track $$ x = s $$ while the slope jump stays fixed at $$ -1/p(s) $$, keeping the graph symmetric under $$ x \leftrightarrow s $$.
4. **Wave vs. Heat Time Evolution:** Contrast the vibrating string animation (energy conserved, sharp features persist) with the heat rod animation (higher modes evaporate exponentially, leaving a single smooth arch).

### Worked example: Predicting the Sturm Nodal Interlacing on $$ [0, 1] $$

**Problem:** For the Dirichlet eigenfunctions $$ \phi_n(x) = \sin(n\pi x) $$ on $$ [0, 1] $$, list the exact interior zeros of $$ \phi_3(x) $$ and $$ \phi_4(x) $$ and verify Sturm's interlacing property before testing it in the gallery.

1. **Find interior zeros of $$ \phi_3(x) = \sin(3\pi x) $$ in $$ (0, 1) $$:**
   $$ 3\pi x = k\pi \implies x = \frac{1}{3}, \frac{2}{3} \quad (\text{exact count: } 3 - 1 = 2 \text{ interior zeros}). $$
2. **Find interior zeros of $$ \phi_4(x) = \sin(4\pi x) $$ in $$ (0, 1) $$:**
   $$ 4\pi x = k\pi \implies x = \frac{1}{4}, \frac{1}{2}, \frac{3}{4} \quad (\text{exact count: } 4 - 1 = 3 \text{ interior zeros}). $$
3. **Verify strict interlacing:**
   $$ 0 < \frac{1}{4} < \frac{1}{3} < \frac{1}{2} < \frac{2}{3} < \frac{3}{4} < 1. $$
   Between $$ \frac{1}{3} $$ and $$ \frac{2}{3} $$ sits $$ \frac{1}{2} $$; between $$ 0 $$ and $$ \frac{1}{3} $$ sits $$ \frac{1}{4} $$; between $$ \frac{2}{3} $$ and $$ 1 $$ sits $$ \frac{3}{4} $$. Every pair of zeros of $$ \phi_3 $$ strictly brackets a zero of $$ \phi_4 $$!

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 07 in one place. It is intended as a visual companion to the chapter's boundary-value and spectral ideas.

## What Is Included

- geometry of two-point boundary conditions
- eigenvalue selection and eigenfunction nodal structure
- weighted orthogonality and Sturm-Liouville intuition
- eigenfunction expansions and Green's functions
- applications to vibrating strings and steady heat conduction

{% include interactive-frame.html
  title="Chapter 07 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 07 topics."
  path="interactives/chapter07/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, English. Heat modes decaying, a picture the gallery is making interactive.
- [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, English. String modes to set beside the vibrating-string frames.
- [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, English. The Green's function impulse the boundary-value frames are illustrating.
