---
layout: post
title: "01-10 Interactive Illustrations Gallery"
chapter: '01'
order: 10
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: optional
---

Solving a first-order ODE algebraically gives you a formula, but watching a family of solution curves flow through a slope field gives you physical intuition you can trust under pressure. This interactive gallery lets you drag initial conditions, adjust parameters, and see instantly why trajectories never cross when Lipschitz conditions hold—and why phase-line equilibria act like invisible magnets or cliffs.

## Key ideas: Connecting Visual Geometry to Chapter 01 Techniques

Each interactive visualization in this gallery illuminates a core analytical tool from Chapter 01:

1. **Direction Fields and Isoclines:** Curves of constant slope $$f(t,y) = m$$ (isoclines) organize the slope field; sketching solutions means weaving curves tangent to every arrow they touch.
2. **Exact-Equation Contour Maps:** Viewing $$M\,dx + N\,dy = 0$$ as level curves $$\Psi(x,y) = C$$ turns implicit solutions into topographic maps where singular points appear as saddles or peaks.
3. **Phase Lines and Basin Boundaries:** Dragging an initial condition across an unstable equilibrium on an autonomous phase line dramatically illustrates tipping points and basins of attraction.
4. **Uniqueness Breakdown vs. Finite-Time Blow-Up:** Comparing $$y' = y^2$$ (smooth, unique, yet blows up in finite time) against $$y' = 3y^{2/3}$$ (curves merge and branch at $$y = 0$$) makes Picard–Lindelöf's hypotheses unforgettable.

### Worked example: Sketching Solutions of $$y' = y - t$$ Using Isoclines

Before touching a computer, use three isoclines to predict the exact geometry of $$y' = y - t$$:

1. **Compute the isoclines $$y - t = m$$ (lines of constant slope $$m$$):**
   - Zero-slope isocline ($$m = 0$$): $$y = t$$ (every trajectory crosses this diagonal horizontally).
   - Unit-slope isocline ($$m = 1$$): $$y = t + 1$$. Notice that the line $$y(t) = t + 1$$ itself has slope $$1$$ everywhere—so it is an **exact straight-line solution**!
   - Slope $$-1$$ isocline ($$m = -1$$): $$y = t - 1$$.
2. **Compute the second derivative along any trajectory to find concavity:**
   $$y'' = \frac{d}{dt}(y - t) = y' - 1 = (y - t) - 1 = y - (t + 1).$$
3. **Read the global behavior directly from the sign of $$y''$$:**
   - Above the straight-line solution $$y = t + 1$$: $$y'' > 0$$ (concave up), so trajectories bend sharply upward toward $$+\infty$$.
   - Below $$y = t + 1$$: $$y'' < 0$$ (concave down), so trajectories cross $$y = t$$ horizontally and plunge toward $$-\infty$$.
4. **Verify against the exact linear solution:**
   Using $$\mu(t) = e^{-t}$$ gives $$y(t) = t + 1 + C e^t$$. For $$C > 0$$ curves flare upward; for $$C = 0$$ we get the exact separatrix $$y = t + 1$$; for $$C < 0$$ curves plunge downward—100% predicted by isoclines alone!

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 01 in one place. It is designed for visual review, experimentation with parameters, and quick classroom demonstration.

## What Is Included

- slope fields and initial value problems
- exact versus numerical solution comparisons
- separable, linear, exact, and autonomous first-order models
- population, mixing, mechanics, and circuit applications

{% include interactive-frame.html
  title="Chapter 01 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 01 topics."
  path="interactives/chapter01/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [The Geometric Meaning of Differential Equations // Slope Fields, Integral Curves & Isoclines](https://www.youtube.com/watch?v=ccDMpj2UK_M) — Dr. Trefor Bazett, English. Slope fields and integral curves, the pictures the chapter gallery lets students manipulate.
- [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) — 3Blue1Brown, English. A visual overview of first-order models before opening the interactive frames.
- [Direction Fields | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=jOBBwI4CYjM) — MIT OpenCourseWare, English. MIT's direction-field recitation, a companion to the slope-field applet.
