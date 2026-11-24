---
layout: post
title: "01-11 History of First-Order ODEs"
chapter: '01'
order: 11
owner: Course Team
lang: en
categories:
- chapter01
---

In 1695, Jacob Bernoulli published a public challenge in *Acta Eruditorum* daring the leading mathematicians of Europe to solve the nonlinear equation $$y' + p(x)y = q(x)y^n$$. Within months, Gottfried Wilhelm Leibniz and Johann Bernoulli fired back with rival substitutions that sparked both a bitter sibling feud and the birth of systematic ODE theory. Every method in Chapter 01 was forged in real scientific rivalries over hanging chains, brachistochrone curves, and planetary motion.

## Background Knowledge Map: Four Historical Milestones Behind Chapter 01

Tracing the timeline of first-order ODEs shows how practical geometry matured into modern analysis:

1. **Inverse Tangent Problems (1670s–1690s):** Before the term "differential equation" even existed, Newton and Leibniz asked: given a geometric property of a curve's tangent (like a constant subtangent), reconstruct the curve itself—producing separation of variables.
2. **The Bernoulli–Leibniz Substitution Era (1690s):** Solving the catenary, tractrix, and Bernoulli's equation introduced change-of-variable tricks and established differential equations as an autonomous branch of mathematics.
3. **Euler's Systematization and Integrating Factors (1730s–1760s):** Leonhard Euler unified exact differentials, integrating factors, and the first numerical stepping scheme (Euler's method), turning scattered tricks into a textbook discipline.
4. **Cauchy, Lipschitz, and Picard's Rigor (1820s–1890s):** Realizing that most ODEs have *no* elementary closed-form formula, nineteenth-century analysts shifted from "how do we integrate this?" to "does a unique solution exist?"—culminating in Picard's 1890 method of successive approximations.

### Step-by-Step Worked Example (Read Slowly): Solving Leibniz's 1690s "Inverse Tangent" Problem (The Tractrix)

A classic seventeenth-century challenge asked: what curve in the first quadrant has the property that the segment of its tangent line from the point of tangency $$(x, y)$$ to the $$x$$-axis always has constant length $$a$$?

1. **Translate the geometric condition into a first-order ODE:**
   The right triangle formed by the tangent segment (hypotenuse $$a$$), vertical height $$y$$, and horizontal subtangent $$s$$ satisfies $$s = \sqrt{a^2 - y^2}$$. Since the curve descends toward the $$x$$-axis as $$x$$ increases,
   $$\frac{dy}{dx} = -\frac{y}{\sqrt{a^2 - y^2}}, \qquad 0 < y \le a.$$
2. **Separate variables:**
   $$dx = -\frac{\sqrt{a^2 - y^2}}{y}\,dy.$$
3. **Evaluate the integral using $$y = a\operatorname{sech} u$$ (so $$\sqrt{a^2 - y^2} = a\tanh u$$ and $$dy = -a\operatorname{sech} u \tanh u\,du$$):**
   $$dx = -\frac{a\tanh u}{a\operatorname{sech} u}\bigl(-a\operatorname{sech} u \tanh u\,du\bigr) = a\tanh^2 u\,du = a(1 - \operatorname{sech}^2 u)\,du.$$
   Integrating with $$x = 0$$ at $$y = a$$ ($$u = 0$$):
   $$x = a(u - \tanh u) = a\ln\!\left(\frac{a + \sqrt{a^2 - y^2}}{y}\right) - \sqrt{a^2 - y^2}.$$
4. **Historical payoff:** Rotating this tractrix around the $$x$$-axis generates Beltrami's **pseudosphere**—the first concrete surface of constant negative Gaussian curvature, which later proved non-Euclidean hyperbolic geometry was consistent!

## Objectives
This lesson reconstructs the historical rise of first-order ordinary differential equations from mechanics, astronomy, population theory, and electrical engineering. Students should come away seeing Chapter 01 not as a list of techniques, but as the first organized answer to the problem of modeling change.

## Prerequisites
Students should know the mathematical language of Chapter 00 and the solution methods from Chapter 01. The purpose here is to understand who created those methods, why they were needed, and how modeling questions pushed theory forward.

## Introduction
First-order differential equations are the oldest gateway into the subject because they sit closest to the basic idea of rate of change. In the late seventeenth century, Newton studied motion through fluxions and Leibniz introduced the notation that still dominates modern analysis. During the eighteenth century, the Bernoullis, Euler, Clairaut, Riccati, and Lagrange turned scattered calculations into recognizable equation types. By the nineteenth century, Cauchy, Lipschitz, Picard, and Lindelof began asking not only how to solve an equation, but when a solution exists and whether it is unique.

The chapter's applied themes also have deep historical roots. Newton's cooling law, Malthusian growth, Verhulst's logistic correction, mixing problems from chemistry and hydraulics, and Kirchhoff's circuit laws all helped transform first-order ODEs from pure technique into a universal modeling language.

## Historical Arc
The earliest first-order equations appeared implicitly in mechanics and geometry. Once calculus existed, mathematicians quickly noticed that certain forms could be separated, integrated, or rewritten through clever substitutions. The eighteenth century was therefore an age of method-building. The nineteenth century added rigor and qualitative interpretation. The twentieth century then taught scientists to see first-order ODEs everywhere: ecology, epidemiology, circuits, control, and chemical kinetics.

## Topic-by-Topic Historical Map
1. **Introduction to differential equations.** Newton and Leibniz created the conceptual framework, but Euler's textbooks made classification by order and type more systematic. The very phrase "differential equation" became common as calculus matured.
2. **Separable equations.** This is one of the oldest methods because early analysts could often rearrange variables and integrate directly. Bernoulli family papers and Euler's expositions helped standardize the technique.
3. **Linear first-order equations.** The integrating-factor method emerged from eighteenth-century work by Euler and Lagrange and later became a standard textbook procedure. It showed that some equations can be solved not by guesswork but by structural transformation.
4. **Exact equations.** Clairaut and later Pfaffian theory clarified when a differential expression comes from a hidden potential function. Exactness linked ODEs to geometry and total differentials, foreshadowing later differential forms.
5. **Substitution methods.** Bernoulli equations, homogeneous substitutions, Clairaut equations, and Riccati equations each preserve some recognizable algebraic pattern. Their history shows how mathematicians learned to classify equations by symmetry and reducibility.
6. **Existence and uniqueness.** Cauchy framed the initial-value problem clearly in the early nineteenth century. Lipschitz introduced the condition that now bears his name, and Picard with Lindelof showed how successive approximations establish existence and uniqueness.
7. **Population and mixing models.** Malthus's 1798 population law produced pure exponential growth, while Verhulst's papers of 1838 and 1845 introduced the logistic equation to model saturation. Tank-mixing problems grew out of chemical engineering and practical flow systems.
8. **Mechanics and circuits.** Newtonian drag models gave first-order equations for falling bodies and cooling. Kirchhoff's nineteenth-century circuit laws and later electrical engineering made the linear first-order equation central to RC and RL systems.
9. **Autonomous equations and phase lines.** Poincare's qualitative theory in the 1880s taught mathematicians to study equilibrium and long-term behavior without explicit formulas. That was a major conceptual leap beyond mere symbolic solution.

## Landmark Works and Events
- Newton's *Principia* (1687) and Leibniz's differential papers created the language of rates of change.
- Bernoulli and Euler papers in the eighteenth century organized early equation-solving methods.
- Riccati's work gave rise to one of the classical nonlinear first-order equations.
- Cauchy's lectures and Picard's approximation method turned IVPs into a rigorous theory.
- Verhulst's logistic model made first-order ODEs central to population dynamics.

## Why This History Matters
Chapter 01 can feel deceptively elementary because the formulas are short. Historically, however, this chapter is where mathematics first learned to encode a law of change instead of merely a static relation. It is the moment when models began to evolve in time on paper.

The chapter also teaches an enduring lesson: theory and applications grew together. Solution methods were invented because concrete problems in astronomy, mechanics, fluids, chemistry, and demography demanded them.

## Discussion Prompts
1. Why did first-order equations appear so quickly after the invention of calculus?
2. Which was the deeper breakthrough: learning to solve more equation types, or learning to prove existence and uniqueness?
3. Why does the logistic equation mark a conceptual advance over simple exponential growth?

## Suggested Answers to the Discussion Prompts
1. As soon as calculus existed, mathematicians had a way to encode local laws of motion, cooling, mixing, and growth. First-order equations are the most immediate form of the idea that the present rate of change depends on the present state.
2. Learning to solve more classes of equations was a major technical gain, but existence and uniqueness were the deeper conceptual breakthrough. They answer whether a model actually determines an evolution and whether initial data really pick out one physical trajectory rather than many competing ones.
3. The logistic equation goes beyond exponential growth because it builds feedback and finite resources into the law itself. It shows that growth can regulate itself and approach an equilibrium instead of increasing forever at the same relative rate.

## References
- Boyce and DiPrima, *Elementary Differential Equations and Boundary Value Problems*. Good for connecting the modern Chapter 01 curriculum with its classical roots.
- Ross, *Differential Equations*. Concise on first-order methods and their modeling background.
- Ivor Grattan-Guinness, *The Rainbow of Mathematics*. Useful historical context on eighteenth- and nineteenth-century analysis.
