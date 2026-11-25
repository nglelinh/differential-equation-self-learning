---
layout: post
title: "11-10 History of Laplace and Poisson Equations"
chapter: '11'
order: 10
owner: Course Team
lang: en
categories:
- chapter11
---

> **Storytelling Hook:** In 1782, Pierre-Simon Laplace was not trying to invent a new branch of pure mathematics—he was trying to calculate the gravitational pull of oblate planets and Saturn's rings. Half a century later, a self-taught English miller named George Green published a private booklet in Nottingham that introduced the word *potential* and the integral kernels we still call Green's functions. Together, celestial mechanics and electricity forged the modern theory of elliptic PDEs.

## Objectives
This lesson explains how Laplace's equation, Poisson's equation, and classical potential theory developed from celestial mechanics, electrostatics, and fluid flow. Students should see Chapter 11 as a historical meeting place of geometry, physics, and analysis.

## Prerequisites
Students should know the main analytical content of Chapter 11: separation of variables, polar coordinates, harmonic functions, Green's functions, electrostatic applications, and potential flow.

## Key ideas: Four Historical Turning Points in Potential Theory

Tracing how potential theory matured from astronomy into functional analysis highlights four pivotal shifts:

1. **Laplace's Celestial Potential (1782–1799):** Replacing vector gravitational forces with a single scalar potential $V$ revealed that $V$ satisfies $\Delta V = 0$ outside attracting bodies, launching spherical harmonics and separation of variables in spherical coordinates.
2. **Poisson's Interior Source Correction (1813):** Siméon Denis Poisson discovered that inside a mass distribution of density $\rho$, Laplace's equation acquires a right-hand side, $\Delta V = 4\pi G\rho$, unifying interior and exterior potential theory.
3. **George Green's 1828 Nottingham Essay:** Introducing Green's identities and impulse-response kernels, Green converted boundary-value PDEs into integral representations—work nearly lost until William Thomson (Lord Kelvin) rediscovered it in 1845.
4. **Dirichlet's Principle, Weierstrass's Critique, and Hilbert's Rescue (1850–1900):** Riemann leaned heavily on minimizing Dirichlet's energy integral to prove existence of harmonic functions; Weierstrass showed in 1870 that energy minimization can fail in general variational problems; and Hilbert (1900) finally made Dirichlet's Principle rigorous, directly catalyzing modern Sobolev spaces.

## Introduction
If the heat equation models evolution and the wave equation models propagation, Laplace's equation models balance. It describes steady states, equilibrium configurations, and fields with no interior sources. Poisson's equation then appears as the sourced version of the same balance law.

The historical world behind these equations is the world of gravitational attraction, electric potential, and incompressible irrotational flow. Laplace, Poisson, Gauss, Green, Dirichlet, Riemann, Kelvin, and Maxwell all left deep marks on it.

## Historical Arc
Laplace introduced his equation in celestial mechanics and potential theory in the late eighteenth century. Poisson generalized it to include source terms in the early nineteenth century. Gauss transformed potential theory with integral methods, Green introduced boundary identities and kernels, and Dirichlet reframed existence through boundary data. Later the theory became one of the core training grounds for modern PDE and complex analysis.

## Topic-by-Topic Historical Map
1. **Introduction to Laplace's equation.** Harmonic functions first arose in gravitational and electrostatic settings where equilibrium fields satisfy local balance. Laplace's name marks this physical-mathematical synthesis.
2. **Separation of variables on rectangles.** Classical boundary problems on boxes and plates made rectangular coordinates natural. Fourier methods and eigenfunction expansions quickly entered the picture.
3. **Laplace in polar coordinates.** Circular and radial symmetry in astronomy, electrostatics, and membrane problems led naturally to polar and spherical forms. Geometry directly reshaped the equation.
4. **Poisson's equation.** Poisson introduced source terms to represent charge or mass density. The equation became the natural next step beyond source-free equilibrium.
5. **Mean value and maximum principle.** These properties captured the remarkable rigidity of harmonic functions. They later became central structural theorems of elliptic PDE.
6. **Green's functions.** Green's 1828 essay supplied a powerful way to encode boundary influence and source response. This viewpoint is one of the enduring triumphs of potential theory.
7. **Electrostatics.** Coulomb's law, Gauss's law, and Maxwell's synthesis made potentials and harmonic functions physically indispensable. Chapter 11 carries all of that history.
8. **Fluid flow.** Potential flow theory connected harmonic functions to incompressible irrotational motion. This gave the equations another major scientific life beyond electrostatics.

## Landmark Works and Events
- Laplace's work in celestial mechanics founded classical potential theory.
- Poisson extended the equilibrium equation to include source terms.
- Gauss and Green transformed the subject through integral identities and boundary methods.
- Dirichlet's principle reshaped existence questions in the nineteenth century.
- Maxwell and Kelvin carried potential theory deep into physics.

## Why This History Matters
Chapter 11 is historically important because it turns equilibrium into geometry. Solutions are constrained not only by local differential laws but by global boundary structure and rigid qualitative principles.

It also explains why elliptic PDE feel different from heat and wave equations. Instead of evolution or propagation, the governing idea is compatibility across space.

### Worked example: Reconstructing Laplace's 1782 Calculation for Newton's Potential

Let us reproduce Laplace's landmark verification that the 3D Newtonian potential $\Phi(x,y,z) = \frac{1}{r}$ (where $r = \sqrt{x^2 + y^2 + z^2} > 0$) satisfies $\Delta \Phi = 0$ away from the origin, and then compute its boundary flux to see why Poisson's source term appears at $r = 0$.

1. **Differentiate $r^{-1}$ once with respect to $x$:** Since $\frac{\partial r}{\partial x} = \frac{x}{r}$,
   $$\frac{\partial}{\partial x}(r^{-1}) = -r^{-2}\frac{x}{r} = -x r^{-3}.$$
2. **Differentiate a second time with respect to $x$:** By the product rule,
   $$\frac{\partial^2}{\partial x^2}(r^{-1}) = -r^{-3} - x(-3 r^{-4})\frac{x}{r} = -r^{-3} + 3x^2 r^{-5}.$$
3. **Sum symmetrically over $x, y, z$:**
   $$\Delta(r^{-1}) = \big(-r^{-3} + 3x^2 r^{-5}\big) + \big(-r^{-3} + 3y^2 r^{-5}\big) + \big(-r^{-3} + 3z^2 r^{-5}\big) = -3r^{-3} + 3(x^2+y^2+z^2)r^{-5} = -3r^{-3} + 3r^{-3} = 0.$$
4. **Integrate the flux over a sphere $S_R$ of radius $R$ centered at the origin:** On $S_R$, $\nabla(r^{-1}) = -\frac{\mathbf{x}}{r^3} = -R^{-2}\mathbf{n}$, so:
   $$\iint_{S_R} \nabla(r^{-1}) \cdot \mathbf{n}\,dS = \iint_{S_R} (-R^{-2})\,dS = (-R^{-2})(4\pi R^2) = -4\pi.$$
   Because this flux equals $-4\pi$ for *every* radius $R > 0$—even as $R \to 0$—the Divergence Theorem reveals a concentrated point mass at the origin: $-\Delta\left(\frac{1}{4\pi r}\right) = \delta_0$.

## Discussion Prompts
1. Why did potential theory become such a fertile meeting ground for physics and analysis?
2. Why are the maximum principle and mean value property historically so revealing?
3. Why does geometry play such a visible role in Laplace and Poisson problems?

## Suggested Answers to the Discussion Prompts
1. Potential theory became a fertile meeting ground because gravitational, electrostatic, and steady-state physical problems all kept producing the same mathematical structure. That gave analysis a strong reason to investigate harmonic functions and Poisson sources in depth.
2. The maximum principle and mean value property are historically revealing because they show how rigid harmonic functions are. From a few elegant statements, one sees that the equation imposes remarkably strong global behavior through local structure.
3. Geometry plays such a visible role because the domain and its boundary are not just scenery but part of the data that determine the solution. The shape of space directly leaves its mark on the behavior of harmonic and Poisson problems.

## References
- Evans, *Partial Differential Equations*. A strong modern guide to elliptic structure.
- Kellogg, *Foundations of Potential Theory*. A classic historical and mathematical source.
- Green's 1828 essay and Maxwell's writings remain foundational background documents for the subject.
