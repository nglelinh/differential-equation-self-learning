---
layout: post
title: "13-10 History of Numerical Methods"
chapter: '13'
order: 10
owner: Course Team
lang: en
categories:
- chapter13
---

> **Storytelling Hook:** Long before electronic computers existed, Leonhard Euler computed lunar orbits by hand using tangent steps, and in 1928 Richard Courant, Kurt Friedrichs, and Hans Lewy proved their famous CFL theorem *not* to run code, but as a pure-mathematics proof that PDEs have solutions! Only when ENIAC and weather-forecasting rooms arrived in the 1940s–1950s did those paper theorems become the survival manual of modern scientific computing.

## Objectives
This lesson traces the history of numerical differential equations from Euler's first step method to finite elements, stiff solvers, and stochastic simulation. Students should see Chapter 13 as a history of approximation becoming a mathematical science in its own right.

## Prerequisites
Students should know the main ideas of Chapter 13: Euler's method, Runge-Kutta methods, multistep schemes, stiffness, finite differences, stability, CFL thinking, finite elements, and stochastic differential equations.

## Key ideas: Four Historical Revolutions in Scientific Computing

Tracing numerical differential equations from quill pens to supercomputers highlights four defining breakthroughs:

1. **Hand-Computed Celestial Mechanics (Euler 1768, Adams 1855, Runge–Kutta 1895–1901):** Early ODE algorithms were engineered to minimize human arithmetic during astronomical ephemeris and artillery calculations.
2. **The 1928 CFL Paper and Lax Equivalence (1956):** Courant, Friedrichs, and Lewy discovered that discrete PDE grids fail to converge unless the numerical domain of dependence encloses the physical one; Peter Lax and Robert Richtmyer later crystallized this into the general Equivalence Theorem.
3. **Stiffness and Dahlquist's Stability Theory (1952–1963):** Curtiss and Hirschfelder identified stiff chemical kinetics in 1952, prompting Germund Dahlquist to formalize zero-stability, A-stability, and the famous order barriers for multistep methods.
4. **Finite Elements and Stochastic Numerics (Courant 1943, Turner–Clough 1956, Itô–Maruyama 1955):** Structural engineers and mathematicians converged on the Finite Element Method for complex geometries, while Gisiro Maruyama translated Kiyosi Itô's stochastic integral into the first numerical SDE scheme.

## Introduction
For much of the history of differential equations, numerical work was what scientists did when exact formulas failed. Over time that practical necessity turned into a deep theory of approximation, stability, consistency, and convergence. Numerical analysis did not replace exact mathematics; it developed its own rigorous concepts and its own forms of insight.

This chapter also reveals how strongly computation and theory shaped one another. New machines created new numerical ambitions, but new equations also created new notions of error, instability, and algorithmic design.

## Historical Arc
Euler introduced one of the earliest systematic discrete methods in the eighteenth century. Runge and Kutta refined one-step accuracy around 1900. Adams-type multistep ideas extended the story. In the twentieth century, Dahlquist clarified stability barriers, Curtiss and Hirschfelder highlighted stiffness, Courant-Friedrichs-Lewy explained propagation constraints, and Courant's finite element idea opened a new geometric path. Ito and Maruyama later brought stochastic equations into the numerical fold.

## Topic-by-Topic Historical Map
1. **Euler's method.** Euler's discrete stepping idea is the ancestor of nearly every time-marching method. It turned the differential equation into an iterative computational rule.
2. **Runge-Kutta methods.** Runge and Kutta improved accuracy without requiring higher derivatives. Their schemes became classics because they balance cost, order, and flexibility.
3. **Multistep methods.** Adams-Bashforth and Adams-Moulton families used several past values to gain efficiency. These methods reveal that memory can be computationally valuable.
4. **Stiff equations.** Chemical kinetics and reaction models exposed situations where naive explicit methods are ineffective or unstable. Stiffness became a defining twentieth-century concept.
5. **Finite differences for PDE.** Richardson, Lax, and many others formalized grid-based approximations for spatial derivatives. PDE numerics became a major field rather than a side calculation.
6. **Stability, convergence, and CFL.** The CFL condition from 1928 taught a fundamental lesson: discrete propagation must respect physical propagation. Stability theory gave numerical analysis its own rigor.
7. **Finite element introduction.** Courant's 1943 piecewise-linear approximation idea eventually grew into the finite element method. Geometry, variational structure, and computation met in one framework.
8. **Stochastic differential equations.** Ito's calculus and Maruyama's 1955 Euler-type scheme brought randomness into numerical differential equations. Simulation became essential in finance, physics, and biology.
9. **The chapter's interactive and computational culture.** Modern visual experiments and solver libraries continue the long history of computation as a form of mathematical understanding.

## Landmark Works and Events
- Euler's discrete method inaugurated systematic ODE approximation.
- Runge and Kutta made higher-order one-step methods practical.
- Dahlquist gave stability theory a sharp conceptual form.
- CFL analysis changed how numerical PDE is understood.
- Courant's finite element idea transformed approximation on complex domains.

## Why This History Matters
Chapter 13 teaches that approximation is not merely second best. Numerical methods reveal structure, test models, and make entire classes of equations accessible that would otherwise remain inert on the page.

It also reminds students that a good algorithm must respect the mathematics of the problem. Stability, conservation, stiffness, and geometry are not afterthoughts; they are the history of the field written into method design.

### Worked example: Reconstructing the 1928 CFL Domain-of-Dependence Argument

Reproduce the classic geometric argument of Courant, Friedrichs, and Lewy for the 1D wave equation $u_{tt} = c^2 u_{xx}$ discretized by the explicit leapfrog stencil
$$U_j^{n+1} = 2U_j^n - U_j^{n-1} + \left(\frac{c\Delta t}{\Delta x}\right)^2 (U_{j+1}^n - 2U_j^n + U_{j-1}^n).$$

1. **Find the physical domain of dependence at $(x_0, T)$:** By d'Alembert's formula, the exact value $u(x_0, T)$ depends on all initial data in the interval $[x_0 - cT,\; x_0 + cT]$ of half-width $cT$.
2. **Find the numerical domain of dependence after $N = T / \Delta t$ steps:** Each time step reaches at most one grid point left ($j-1$) and one right ($j+1$). Tracing backward $N$ steps from $(x_0, T)$ reaches only the interval $[x_0 - N\Delta x,\; x_0 + N\Delta x]$ of half-width $N\Delta x$.
3. **Impose the CFL inclusion test:** Suppose $N\Delta x < cT$, i.e., $\frac{c\Delta t}{\Delta x} > 1$. Then we could modify the initial data $u(x,0)$ strictly inside $[x_0 - cT,\; x_0 - N\Delta x)$, which changes the true solution $u(x_0, T)$ while leaving the numerical solution $U_0^N$ completely untouched!
4. **Conclude the necessary CFL condition:** For convergence to be possible for all initial data, we must have:
   $$N\Delta x \ge cT = c N\Delta t \iff \frac{c\Delta t}{\Delta x} \le 1.$$
   Even without computing a single eigenvalue, pure causality forbids an explicit scheme from outrunning its own stencil.

## Discussion Prompts
1. Why does Euler's simple method still matter historically and pedagogically?
2. Why was stability theory such a major conceptual advance?
3. Why do finite elements represent more than just another discretization trick?

## Suggested Answers to the Discussion Prompts
1. Euler's method still matters because it is the first transparent bridge from a continuous differential law to a step-by-step computational algorithm. Students can literally watch a derivative become an update rule.
2. Stability theory was a major conceptual advance because a numerical method cannot be judged by local error alone. One must know whether the discretization respects the problem's dynamics or instead amplifies noise and invents behavior that was never present in the original model.
3. Finite elements represent more than another discretization trick because they are tied to weak formulations, geometry, and the assembly of local information into a global solution space. That blend of analysis, linear algebra, and geometric flexibility made them a dominant language of computational PDE.

## References
- Ascher and Petzold, *Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations*. A strong modern guide to much of the chapter.
- Quarteroni, Sacco, and Saleri, *Numerical Mathematics*. Helpful broader context.
- Kloeden and Platen, *Numerical Solution of Stochastic Differential Equations*. Essential for the stochastic branch of the story.
