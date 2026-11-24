---
layout: post
title: "10-05 Energy and Uniqueness"
chapter: '10'
order: 5
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: required
---

In Chapter 09, we proved uniqueness of the heat equation using the Maximum Principle. Try applying the Maximum Principle to a vibrating string and it fails completely—two small waves of height $$ 0.5 $$ can collide head-on and momentarily shoot up to height $$ 1.0 $$ in the interior! How, then, do we prove that the wave equation has at most one solution and that disturbances cannot travel faster than speed $$ c $$—even in complicated geometries or variable media where d'Alembert's formula does not exist?

The answer is the **Energy Method**: define the total mechanical energy $$ E(t) = \frac{1}{2}\int \bigl(u_t^2 + c^2 |\nabla u|^2\bigr)\,dx $$, differentiate in time, integrate by parts, and watch $$ \frac{dE}{dt} = 0 $$ prove uniqueness in three lines—and when integrated over a *shrinking light cone*, prove finite speed of propagation in any dimension!

## Background Knowledge Map: Energy Conservation and Light-Cone Uniqueness

1. **Kinetic + Potential Wave Energy:** For $$ u_{tt} = c^2 u_{xx} $$ on $$ [0, L] $$, the quadratic functional $$ E(t) = \frac{1}{2}\int_0^L \bigl(u_t^2 + c^2 u_x^2\bigr)\,dx $$ sums kinetic energy ($$ \frac{1}{2}u_t^2 $$) and elastic stretching energy ($$ \frac{1}{2}c^2 u_x^2 $$).
2. **Conservation Law via Integration by Parts:** Differentiating under the integral gives $$ E'(t) = \int_0^L \bigl(u_t u_{tt} + c^2 u_x u_{xt}\bigr)\,dx = \bigl[c^2 u_t u_x\bigr]_0^L + \int_0^L u_t(u_{tt} - c^2 u_{xx})\,dx = \bigl[c^2 u_t u_x\bigr]_0^L $$. Under Dirichlet ($$ u_t = 0 $$), Neumann ($$ u_x = 0 $$), or periodic BCs, the boundary flux vanishes identically, so $$ E(t) = E(0) $$ for all $$ t $$!
3. **Instant Proof of Uniqueness:** For the difference $$ w = u_1 - u_2 $$ of two solutions with identical initial and boundary data, $$ E_w(0) = 0 \implies E_w(t) = 0 $$ for all $$ t \ge 0 $$. Since $$ w_t^2 + c^2 w_x^2 \ge 0 $$, both $$ w_t \equiv 0 $$ and $$ w_x \equiv 0 $$, forcing $$ w \equiv 0 $$!
4. **Local Light-Cone Energy (Finite Speed of Propagation):** Integrating $$ \frac{1}{2}(u_t^2 + c^2 u_x^2) $$ over the shrinking interval $$ [x_0 - c(t_0 - t), x_0 + c(t_0 - t)] $$ yields $$ \frac{d}{dt} E_{\text{loc}}(t) \le 0 $$ via the Cauchy–Schwarz inequality $$ |2 c u_t u_x| \le u_t^2 + c^2 u_x^2 $$. Thus zero data on the base forces $$ u \equiv 0 $$ inside the entire backward light cone!

### Step-by-Step Worked Example (Read Slowly): Computing Exact Energy Conservation and Damped Energy Decay

**Problem:** (a) For the standing wave $$ u(x, t) = A \sin(kx)\cos(\omega t) $$ on $$ [0, \pi] $$ with $$ k = 2, c = 3, \omega = kc = 6 $$, compute the kinetic energy $$ K(t) = \frac{1}{2}\int_0^\pi u_t^2\,dx $$ and potential energy $$ P(t) = \frac{c^2}{2}\int_0^\pi u_x^2\,dx $$ explicitly, and verify $$ K(t) + P(t) $$ is strictly constant. (b) Show that adding friction $$ u_{tt} + \gamma u_t = c^2 u_{xx} $$ ($$ \gamma > 0 $$) forces $$ E'(t) \le 0 $$.

1. **Compute derivatives of $$ u(x, t) = A\sin(2x)\cos(6t) $$:**
   - $$ u_t = -6A \sin(2x)\sin(6t) $$.
   - $$ u_x = 2A \cos(2x)\cos(6t) $$.
2. **Integrate kinetic and potential energy over $$ [0, \pi] $$ (using $$ \int_0^\pi \sin^2(2x)\,dx = \int_0^\pi \cos^2(2x)\,dx = \frac{\pi}{2} $$):**
   - Kinetic energy:
     $$ K(t) = \frac{1}{2}(36 A^2)\sin^2(6t)\cdot \frac{\pi}{2} = 9\pi A^2 \sin^2(6t). $$
   - Potential energy (with $$ c^2 = 9 $$):
     $$ P(t) = \frac{9}{2}(4 A^2)\cos^2(6t)\cdot \frac{\pi}{2} = 9\pi A^2 \cos^2(6t). $$
3. **Verify total energy conservation:**
   $$ E(t) = K(t) + P(t) = 9\pi A^2\bigl[\sin^2(6t) + \cos^2(6t)\bigr] = 9\pi A^2 \quad (\text{strictly constant!}). $$
   Energy sloshes rhythmically back and forth between kinetic and elastic form at frequency $$ 2\omega = 12 $$, without losing a single joule!
4. **Damped wave energy decay ($$ u_{tt} + \gamma u_t = c^2 u_{xx} $$ with Dirichlet BCs):**
   $$ E'(t) = \int_0^L u_t(u_{tt} - c^2 u_{xx})\,dx = -\gamma \int_0^L u_t^2\,dx \le 0. $$
   Thus $$ E(t) \le E(0) $$ immediately proves uniqueness for damped waves too!

## Learning Objectives

This lesson develops energy identities for the wave equation and uses them to prove uniqueness. Students should see why conserved quantities are both physically meaningful and mathematically powerful.

## Prerequisites

Students should know the wave equation, standing-wave solutions, and the general idea of multiplying an equation by a strategically chosen quantity to obtain an identity.

## Introduction

![Energy and uniqueness for wave equation]({{ site.imgurl }}/chapter_img/chapter10/05_energy_uniqueness.svg)

One of the great strengths of the wave equation is that it possesses a natural conserved energy. This energy combines kinetic and potential contributions and remains constant in time under appropriate boundary conditions. The resulting identity is not only physically elegant, but also mathematically powerful.

Energy methods provide one of the most robust tools in PDE analysis. Even when explicit formulas are unavailable, energy can still prove uniqueness and establish strong control over solutions.

## Concept in Three Ways

### Intuitive View

As a string vibrates, energy shifts back and forth between motion and deformation. The total amount remains constant if there is no damping or external forcing.

### Visual View

At some times the string may be nearly flat but moving quickly, so kinetic energy dominates. At other times it may be highly displaced but momentarily nearly still, so potential energy dominates. The total stays the same.

### Formal View

For the wave equation, one defines an energy involving $$ u_t $$ and $$ u_x $$ or their multidimensional analogues. Differentiating in time and using the PDE shows that the total energy is conserved under suitable conditions.

## Why Energy Methods Matter

Energy methods are among the most important general tools in modern PDE theory. They do not depend on explicit solutions and therefore survive in much more complicated settings.

For the wave equation, energy conservation makes the physical meaning of the PDE mathematically exact and immediately yields uniqueness of solutions with given data.

## Common Misconceptions

### "Energy identities are only for physicists"

No. They are central mathematical tools for PDE theory.

### "Uniqueness requires an explicit formula"

No. Energy methods often prove uniqueness without solving the equation explicitly.

### "Conserved energy means nothing changes"

Wrong. The form of the solution can change greatly while total energy remains constant.

## Suggested Learning Path

### Step 1: Identify the kinetic and potential parts

Students should connect these terms to physical intuition.

### Step 2: Differentiate the total energy

This is the algebraic heart of the method.

### Step 3: Use boundary conditions carefully

Boundary terms determine whether the energy is conserved.

### Step 4: Apply the result to uniqueness

This shows why the method is analytically powerful.

### Checkpoints

- Can students explain why wave energy has two components?
- Do they understand how the PDE leads to conservation?
- Can they see why uniqueness follows from the energy identity?

## Worked Examples

### Example 1: Conserved Energy on a Fixed String

For appropriate boundary conditions, the total energy remains constant in time.

### Example 2: Uniqueness via Difference of Solutions

The difference of two solutions with the same data has zero initial energy. Conservation then implies it remains zero, forcing the difference to vanish.

### Example 3: Contrast with Heat Equation

Unlike the wave equation, the heat equation dissipates rather than conserves energy. This helps students distinguish hyperbolic from parabolic behavior.

## Conceptual Questions

1. Why is energy conservation natural for the wave equation but not for the heat equation?
2. Why is uniqueness easier to prove once an energy identity is available?
3. Why do boundary terms matter in energy calculations?

## Application Problems

1. Why does damping destroy strict energy conservation?
2. In engineering models, why are energy estimates valuable even without explicit solutions?
3. Why is energy one of the most robust notions of control in PDE analysis?

## Interactive Teaching Strategies

- Ask students to interpret the two terms in the energy physically.
- Compare energy conservation with the decay behavior of the heat equation.
- Have them prove uniqueness for the difference of two solutions in groups.
- Reinforce that energy methods remain useful beyond exactly solvable cases.

## Differentiation

### Support for Struggling Students

Students needing support should focus first on the physical interpretation of kinetic and potential energy before working through the algebra.

### Challenge for Advanced Students

Advanced students can explore energy flux through boundaries or higher-dimensional versions of the argument.

## Summary

Energy methods are among the most robust tools in PDE. For the wave equation, they encode both physical conservation and rigorous uniqueness, and they provide a conceptual framework that extends far beyond explicit solution formulas.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Verifying vibration simulations
- Problem: In structural simulations, energy conservation is a key diagnostic for solver quality.
- Model:
$$
E(t)=\frac{1}{2}\int_0^L \left(u_t^2+c^2u_x^2\right)\,dx.
$$
- Assumptions and limitations: No damping and compatible boundary conditions.
- Interpretation: Total energy trades between kinetic and elastic potential forms but remains constant.

#### Uniqueness of the physical response
- Problem: If two models have the same initial and boundary data, can they produce different solutions?
- Model: Apply the energy method to the difference of two candidate solutions.
- Assumptions and limitations: Linear problem, sufficiently smooth solutions.
- Interpretation: Energy conservation leads directly to uniqueness.

### 2. Additional Intuition and Connections

The energy method is powerful because it does not rely on an explicit formula. It gives a global physical law from which uniqueness and stability follow. This point of view returns repeatedly throughout PDE theory.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)
kinetic = np.sin(t) ** 2
potential = np.cos(t) ** 2

plt.plot(t, kinetic, label="kinetic")
plt.plot(t, potential, label="potential")
plt.plot(t, kinetic + potential, label="total", linewidth=2)
plt.xlabel("t")
plt.title("Energy exchange in a single wave mode")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: wave equation energy conservation animation
- search: uniqueness proof wave equation energy method
- search: numerical wave solver energy drift

### 5. Worked Example

For a fixed string, differentiate
$$
E(t)=\frac{1}{2}\int_0^L \left(u_t^2+c^2u_x^2\right)\,dx
$$
with respect to time and integrate by parts. The boundary terms vanish, so $$ E'(t)=0 $$. If the difference of two solutions has zero initial data, its energy remains zero, and therefore the difference must be identically zero. That proves uniqueness.

### 6. Difficulty Layering

**Undergraduate level.** Interpret energy as the sum of kinetic and elastic potential contributions.

**Graduate level.** Extend to energy estimates, weak stability, and hyperbolic equations with variable coefficients.

## Video tham khảo

- xem trước: [Energy Methods for the Wave Equation](https://www.youtube.com/watch?v=fOmON6ubkTM) — Mike, the Mathematician, English. The energy method for the wave equation.
- [Lecture 5.4: Qualitative analysis of Wave equation - Uniqueness by Energy method](https://www.youtube.com/watch?v=Sq7DQpaVFbc) — NPTEL IIT Bombay, English. NPTEL uses the energy identity to prove uniqueness.
- [Energy Method](https://www.youtube.com/watch?v=-8_nuZFVAMQ) — Dr Peyam, English. Dr Peyam on the energy method as a uniqueness argument.

## References

- Evans, Chapter 2.
