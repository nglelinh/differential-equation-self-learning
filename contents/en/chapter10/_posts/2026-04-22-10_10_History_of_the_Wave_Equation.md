---
layout: post
title: "10-10 History of the Wave Equation"
chapter: '10'
order: 10
owner: Course Team
lang: en
categories:
- chapter10
---

The wave equation holds a unique place in the history of science: it was the **very first partial differential equation ever written down** (d'Alembert, 1747), and the fierce argument it sparked between d'Alembert, Euler, and Daniel Bernoulli over what counts as a "legitimate function" launched two centuries of modern analysis. A century later, Maxwell discovered that light itself obeys the 3D wave equation, and in 1916 Einstein showed that ripples in spacetime curvature—gravitational waves, finally detected by LIGO in 2015—obey the exact same hyperbolic PDE!

## Background Knowledge Map: Four Historical Landmarks of Wave Theory

1. **D'Alembert, Euler & Bernoulli (1747–1755):** D'Alembert derived $$ u_{tt} = c^2 u_{xx} $$ and solved it via $$ F(x - ct) + G(x + ct) $$; Euler generalized it to arbitrary drawn shapes; Bernoulli insisted every vibration is a sum of harmonic sines—setting up the grand synthesis of Fourier analysis.
2. **Huygens, Fresnel & Kirchhoff (1690–1882):** Christiaan Huygens explained optical wavefronts as envelopes of secondary spherical wavelets; Augustin-Jean Fresnel added interference; Gustav Kirchhoff derived the exact 3D integral solution proving why sharp wave propagation holds in odd dimensions $$ d \ge 3 $$ but fails in 2D!
3. **Maxwell's Electromagnetic Synthesis (1865):** James Clerk Maxwell unified electricity, magnetism, and light by deriving $$ \mathbf{E}_{tt} = c^2\nabla^2\mathbf{E} $$ from his four field equations—predicting radio waves two decades before Heinrich Hertz built the first transmitter in 1887.
4. **Relativity & Gravitational Waves (1905–2015):** The invariance of the wave operator $$ \frac{1}{c^2}\partial_{tt} - \nabla^2 $$ under Lorentz transformations inspired Einstein's Special Relativity, and linearized General Relativity predicts transverse spacetime ripples traveling at $$ c $$, directly observed from colliding black holes in 2015.

### Step-by-Step Worked Example (Read Slowly): Reproducing Maxwell's 1865 Speed-of-Light Calculation

**Problem:** Starting from Faraday's law $$ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} $$ and the Ampère–Maxwell law in vacuum $$ \nabla \times \mathbf{B} = \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} $$ (with $$ \nabla\cdot\mathbf{E} = 0 $$), derive the wave equation for $$ \mathbf{E} $$ and compute $$ c = 1/\sqrt{\mu_0\varepsilon_0} $$ using $$ \mu_0 = 4\pi \times 10^{-7}\text{ N/A}^2 $$ and $$ \varepsilon_0 = 8.854 \times 10^{-12}\text{ F/m} $$.

1. **Take the curl of Faraday's law:**
   $$ \nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t}(\nabla \times \mathbf{B}) = -\mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}. $$
2. **Apply the vector identity $$ \nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} $$ with $$ \nabla\cdot\mathbf{E} = 0 $$:**
   $$ -\nabla^2 \mathbf{E} = -\mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} \implies \frac{\partial^2 \mathbf{E}}{\partial t^2} = \frac{1}{\mu_0 \varepsilon_0} \nabla^2 \mathbf{E}. $$
3. **Compute $$ c = (\mu_0 \varepsilon_0)^{-1/2} $$:**
   $$ \mu_0 \varepsilon_0 = (1.2566 \times 10^{-6})(8.854 \times 10^{-12}) \approx 1.1126 \times 10^{-17}\text{ s}^2/\text{m}^2. $$
   $$ c = \frac{1}{\sqrt{1.1126 \times 10^{-17}}} \approx \frac{1}{3.3356 \times 10^{-9}} \approx 2.998 \times 10^8\text{ m/s}. $$
   Pure benchtop measurements of capacitors ($$ \varepsilon_0 $$) and magnets ($$ \mu_0 $$) predicted the speed of starlight to four significant figures!

## Objectives
This lesson reconstructs the history of the wave equation from vibrating strings to acoustics, optics, and electromagnetism. Students should see Chapter 10 as the chapter where PDE begins to model propagation, signal travel, and finite speed.

## Prerequisites
Students should know the major analytical and physical ideas of Chapter 10: derivation, d'Alembert's formula, separation of variables, higher-dimensional waves, energy, reflection, dispersion, and applications.

## Introduction
The wave equation entered mathematics through one of the most famous controversies in the subject: the vibrating-string problem. What began as a question about music and mechanics turned into a debate about admissible functions, general solutions, and the meaning of superposition. Later the same equation appeared in acoustics, elasticity, optics, and electromagnetism.

The chapter therefore has both a classical and a modern face. It belongs to the eighteenth-century birth of PDE, but it also points forward to signal transmission, scattering, relativistic field theory, and geometric analysis.

## Historical Arc
d'Alembert derived the one-dimensional wave equation in 1747 and gave the famous traveling-wave formula. Euler, Daniel Bernoulli, and Lagrange then debated its interpretation and generality. In the nineteenth century, Poisson, Kirchhoff, and later Hadamard extended understanding in higher dimensions. Fresnel, Helmholtz, Maxwell, Stokes, and many others carried wave ideas into optics, acoustics, and electromagnetism.

## Topic-by-Topic Historical Map
1. **Derivation of the wave equation.** The vibrating string offered the first great derivation: force balance plus small-slope assumptions lead to a PDE for transverse displacement.
2. **d'Alembert's solution.** The formula $$ u(x,t) = f(x-ct) + g(x+ct) $$ introduced the modern idea of traveling waves. It showed that propagation has direction, memory, and finite speed.
3. **Separation of variables.** On bounded domains, Fourier-type mode expansions became natural. The wave equation therefore shares deep history with Chapter 08.
4. **Higher-dimensional waves.** Poisson's formula, Kirchhoff's representation, and later Hadamard's work clarified how geometry changes propagation in multiple dimensions.
5. **Energy and uniqueness.** Conservation of energy became one of the central structural features of the equation. Energy methods later became standard tools for hyperbolic PDE.
6. **Reflection and transmission.** Physical studies of optics and acoustics, especially in the work of Fresnel and others, forced mathematicians to consider interfaces and matching conditions.
7. **Dispersion and dissipation.** Real media do not always behave like the ideal classical wave equation. Stokes, Kelvin, and later engineering models introduced refined effects such as damping and frequency-dependent propagation.
8. **Applications in acoustics and electromagnetics.** Helmholtz's acoustics and Maxwell's electromagnetic theory made wave propagation a universal scientific theme, not merely a string problem.

## Landmark Works and Events
- d'Alembert's 1747 work inaugurated the classical wave equation.
- The vibrating-string controversy sharpened the meaning of general solutions.
- Poisson, Kirchhoff, and Hadamard extended the theory to higher dimensions and more geometric settings.
- Fresnel and Helmholtz connected wave ideas to optics and acoustics.
- Maxwell made wave propagation central to electromagnetic theory.

## Why This History Matters
Chapter 10 teaches students that not all PDE smooth out like the heat equation. Some propagate information sharply, preserve energy, and carry singularities. That distinction is one of the deepest structural divisions in PDE.

Historically, the wave equation also made mathematics more physical and more geometric at once. It linked derivation, experiment, representation formulas, and propagation phenomena in a single narrative.

## Discussion Prompts
1. Why was the vibrating-string controversy so important for the history of functions?
2. Why is d'Alembert's formula historically more than just a clever exact solution?
3. What does the contrast between heat flow and wave propagation teach about PDE classes?

## Suggested Answers to the Discussion Prompts
1. The vibrating-string controversy mattered because it forced mathematicians to ask whether a function had to be smooth or analytic, or whether it could simply describe an arbitrary initial shape of a string. A concrete mechanics problem ended up expanding the meaning of function for all of analysis.
2. d'Alembert's formula is historically larger than a clever exact solution because it reveals the essence of wave motion: two disturbances traveling in opposite directions at finite speed. It offered a new conceptual picture of PDE behavior, not merely a successful calculation.
3. The contrast between heat and waves teaches that PDE classes differ in kind, not only in notation. Heat diffuses and smooths instantly, while waves preserve oscillatory structure and transport information at finite speed.

## References
- Evans, *Partial Differential Equations*. Excellent for the structural viewpoint on hyperbolic equations.
- Haberman, *Applied Partial Differential Equations*. Helpful on classical derivations and physical applications.
- Darrigol, *Worlds of Flow*. Valuable broader context for waves, fluids, and nineteenth-century physics.
