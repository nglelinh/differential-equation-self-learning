---
layout: post
title: "05-11 Interactive Illustrations Gallery"
chapter: '05'
order: 11
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: optional
---

Nonlinear dynamics is the most visual chapter in all of differential equations: a single parameter slider can make two nullclines touch and annihilate a fishery, inflate a tiny equilibrium point into a pulsating limit cycle, or split two nearly identical initial conditions onto opposite wings of the Lorenz butterfly. This gallery lets you experiment directly with every qualitative phenomenon of Chapter 05.

## Key ideas: Four Visual Experiments to Run in This Gallery

As you interact with the simulations below, test these four theoretical predictions:

1. **Nullcline Intersection Dragging:** In the competing-species and predator–prey widgets, watch how tilting a nullcline switches the interior crossing from a globally attracting node (coexistence) to a saddle with a dramatic diagonal separatrix (founder control).
2. **Hopf Limit-Cycle Growth ($$r \propto \sqrt{\mu}$$):** Slide the bifurcation parameter $$\mu$$ gently past $$0$$; notice that the limit cycle radius grows rapidly at first (square-root slope!) and that trajectories starting both inside and outside snap onto the exact same closed loop.
3. **Lyapunov Level-Set Contours:** Overlay contour rings $$V(x,y) = c$$ on top of the damped pendulum phase portrait to see trajectories cross every ring strictly *inward*—visually confirming $$\dot{V} \le 0$$.
4. **Butterfly Effect Divergence:** Launch two trajectories $$10^{-4}$$ apart on the Lorenz attractor and watch them track each other closely for several loops before suddenly snapping onto opposite wings!

### Worked example: Measuring the Exact Limit-Cycle Radius and Frequency of a Hopf Bifurcation

Before moving the slider in the Hopf bifurcation widget, predict the exact limit cycle for
$$x' = \mu x - y - x(x^2 + y^2), \qquad y' = x + \mu y - y(x^2 + y^2)$$
at $$\mu = -0.25,\; 0,\; +0.25,\; +1.0$$.

1. **Convert to polar coordinates:**
   $$r' = r(\mu - r^2), \qquad \theta' = 1.$$
2. **Predict the exact radius $$r^*(\mu)$$ at each slider position:**
   - **$$\mu = -0.25$$:** $$r' = -r(0.25 + r^2) < 0$$ everywhere $$\implies$$ **no limit cycle**; origin is a stable spiral sink.
   - **$$\mu = 0$$:** $$r' = -r^3 < 0$$ $$\implies$$ slow algebraic spiral sink (critical Hopf point).
   - **$$\mu = +0.25$$:** $$r^* = \sqrt{0.25} = \mathbf{0.50}$$ (stable circle of radius $$0.5$$, period $$2\pi$$).
   - **$$\mu = +1.00$$:** $$r^* = \sqrt{1.00} = \mathbf{1.00}$$ (quadrupling $$\mu$$ only *doubles* the radius—exact $$\sqrt{\mu}$$ scaling!).
3. **Check the Jacobian at the origin:**
   $$J(0,0) = \begin{pmatrix} \mu & -1 \\ 1 & \mu \end{pmatrix} \implies \lambda(\mu) = \mu \pm i, \qquad \alpha'(0) = +1 \ne 0.$$
   The eigenvalues march horizontally across the imaginary axis at unit speed, birthing the exact circle $$r = \sqrt{\mu}$$!

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 05 in one place. It is intended as a visual companion to the chapter's geometric and qualitative analysis.

## What Is Included

- nonlinear phase planes, nullclines, and trajectories
- equilibria, linearization, and stability classification
- Lyapunov functions, limit cycles, and bifurcations
- predator-prey, competition, chaos, and SIR epidemiology

{% include interactive-frame.html
  title="Chapter 05 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 05 topics."
  path="interactives/chapter05/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [MAE5790-1 Course introduction and overview](https://www.youtube.com/watch?v=ycJEoqmQvwg) — Cornell MAE, English. The phase-space point of view the gallery is visualizing.
- [MAE5790-10 van der Pol oscillator](https://www.youtube.com/watch?v=O1lQrHemPsw) — Cornell MAE, English. A limit cycle to compare with the gallery's nonlinear portraits.
- [MAE5790-15 Chaotic waterwheel](https://www.youtube.com/watch?v=HljJv7Hf6Zo) — Cornell MAE, English. The Lorenz waterwheel as the chaotic picture in the set.
