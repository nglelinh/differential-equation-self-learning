---
layout: post
title: "10-03 Separation of Variables"
chapter: '10'
order: 3
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: required
---

On an infinite string, d'Alembert's traveling waves glide away forever without ever turning back. Pin both ends of the string to a violin bridge and nut at $$ x = 0 $$ and $$ x = L $$, and those traveling waves reflect back and forth endlessly—interfering with themselves to form crisp, stationary **standing waves** (normal modes).

Remarkably, separation of variables and d'Alembert's traveling-wave picture are two sides of the exact same coin: every standing wave $$ \sin(k_n x)\cos(\omega_n t) $$ is literally the sum of two opposite traveling waves $$ \frac{1}{2}\sin(k_n(x - ct)) + \frac{1}{2}\sin(k_n(x + ct)) $$!

## Background Knowledge Map: Standing Waves, Boundary Conditions, and Normal Modes

1. **Temporal Oscillator vs. Parabolic Decay:** Separating $$ u_{tt} = c^2 u_{xx} $$ gives $$ X'' + \lambda X = 0 $$ and $$ T'' + c^2\lambda T = 0 $$. Unlike the heat equation's decaying exponential $$ e^{-\alpha\lambda t} $$, here $$ T_n(t) = A_n \cos(c\sqrt{\lambda_n} t) + B_n \sin(c\sqrt{\lambda_n} t) $$ oscillates forever with conserved amplitude!
2. **Two Initial Conditions Require Two Fourier Series:** Because the wave equation is second-order in time, $$ u(x, 0) = f(x) $$ fixes the cosine coefficients $$ A_n $$, while $$ u_t(x, 0) = g(x) $$ fixes the sine coefficients $$ B_n $$ (note the crucial $$ \frac{1}{c\sqrt{\lambda_n}} $$ factor when differentiating $$ \sin(c\sqrt{\lambda_n} t) $$!).
3. **Dirichlet vs. Neumann Standing Modes:** Fixed ends ($$ u(0,t)=u(L,t)=0 $$) produce $$ \sin(n\pi x/L) $$ with $$ \omega_n = n\pi c/L $$; free/sliding ends ($$ u_x(0,t)=u_x(L,t)=0 $$) include the rigid-body zero mode $$ \lambda_0 = 0 \implies A_0 + B_0 t $$ (uniform translation/drift!).
4. **Trigonometric Equivalence to Odd-Periodic d'Alembert:** Using $$ \sin A \cos B = \frac{1}{2}[\sin(A - B) + \sin(A + B)] $$ converts the Fourier sine standing-wave series directly into d'Alembert's formula applied to the odd $$ 2L $$-periodic extensions of $$ f $$ and $$ g $$.

### Step-by-Step Worked Example (Read Slowly): Solving a Struck String with Both Initial Shape and Velocity

**Problem:** Solve $$ u_{tt} = 9 u_{xx} $$ on $$ 0 < x < \pi $$, $$ t > 0 $$, with $$ u(0, t) = u(\pi, t) = 0 $$, $$ u(x, 0) = 2\sin(x) $$, and $$ u_t(x, 0) = 6\sin(2x) $$, and verify $$ u(x, t) $$ at $$ x = \frac{\pi}{4}, t = \frac{\pi}{12} $$.

1. **Identify parameters and Dirichlet eigenmodes:**
   Here $$ c^2 = 9 \implies c = 3 $$ and $$ L = \pi $$. The Dirichlet eigenmodes are $$ \sin(nx) $$ with angular frequencies $$ \omega_n = c n = 3n $$, so
   $$ u(x, t) = \sum_{n=1}^{\infty} \bigl[A_n \cos(3nt) + B_n \sin(3nt)\bigr] \sin(nx). $$
2. **Match $$ u(x, 0) = 2\sin(x) $$:**
   Setting $$ t = 0 $$ gives $$ \sum A_n \sin(nx) = 2\sin(x) \implies A_1 = 2 $$ and all other $$ A_n = 0 $$.
3. **Match $$ u_t(x, 0) = 6\sin(2x) $$ (watch the $$ 3n $$ chain-rule factor!):**
   Differentiate in $$ t $$ and set $$ t = 0 $$:
   $$ u_t(x, 0) = \sum_{n=1}^{\infty} (3n B_n) \sin(nx) = 6\sin(2x). $$
   Matching the $$ n = 2 $$ mode gives $$ 3(2) B_2 = 6 \implies 6 B_2 = 6 \implies B_2 = 1 $$, and all other $$ B_n = 0 $$.
4. **Write the exact solution and verify at $$ x = \frac{\pi}{4}, t = \frac{\pi}{12} $$:**
   $$ u(x, t) = 2\cos(3t)\sin(x) + \sin(6t)\sin(2x). $$
   - Check PDE: $$ u_{tt} = -18\cos(3t)\sin(x) - 36\sin(6t)\sin(2x) = 9\bigl[-2\cos(3t)\sin(x) - 4\sin(6t)\sin(2x)\bigr] = 9 u_{xx} $$. Exact!
   - Evaluate at $$ x = \frac{\pi}{4}, t = \frac{\pi}{12} $$: $$ 3t = \frac{\pi}{4} $$, $$ 6t = \frac{\pi}{2} $$, so
     $$ u\!\left(\frac{\pi}{4}, \frac{\pi}{12}\right) = 2\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{2}}{2}\right) + (1)(1) = 1 + 1 = 2. $$

## Learning Objectives

This lesson develops standing-wave solutions for bounded domains. Students should understand how fixed boundaries quantize the admissible modes and create normal frequencies.

## Prerequisites

Students should know separation of variables from the heat equation and basic eigenvalue problems from earlier chapters.

## Introduction

![Separation of variables for wave equation]({{ site.imgurl }}/chapter_img/chapter10/03_separation_of_variables_wave.svg)

On a bounded interval, wave motion no longer looks like unrestricted traveling pulses. Fixed endpoints impose constraints, and only certain spatial shapes are compatible with those constraints. These shapes are standing-wave modes.

Separation of variables is the method that reveals them. It transforms the wave equation into a boundary-value eigenproblem in space and an oscillatory ODE in time.

## Concept in Three Ways

### Intuitive View

If a string is fixed at both ends, it cannot vibrate with arbitrary shapes. Only specific mode shapes fit the endpoints, and each mode oscillates with its own natural frequency.

### Visual View

The first mode has one arch, the second has two, the third has three, and so on. These are standing waves: the shape remains fixed while the amplitude oscillates in time.

### Formal View

For the bounded wave equation, we try
$$ u(x,t)=X(x)T(t). $$
This leads to a spatial eigenvalue problem and a temporal oscillation equation. The eigenvalues determine the frequencies of the standing modes.

## Why Separation Matters Here

In the wave equation, separation of variables reveals the discrete spectral structure imposed by the boundary. Instead of continuous traveling frequencies, we now get quantized normal modes.

This is one of the clearest mathematical examples of how geometry and boundary conditions shape physical behavior.

## Common Misconceptions

### "Standing waves are the same as traveling waves"

No. Standing waves oscillate in place, while traveling waves move through space.

### "Any frequency can appear on a bounded string"

No. The boundary conditions allow only discrete normal frequencies.

### "Separation of variables is just a computational convenience"

No. It reveals the true spectral structure of the system.

## Suggested Learning Path

### Step 1: Apply the product ansatz

Students should see the same structural method used in the heat equation.

### Step 2: Solve the spatial eigenvalue problem

The boundary conditions select sine-like modes.

### Step 3: Solve the temporal equation

Each spatial mode oscillates in time with its own frequency.

### Step 4: Interpret the resulting standing waves

The mathematics should be connected directly to the physical picture of a vibrating string.

### Checkpoints

- Can students explain why the frequencies become discrete?
- Do they understand the difference between standing and traveling waves?
- Can they connect eigenvalues to natural frequencies?

## Worked Examples

### Example 1: First Mode

The simplest standing wave has a single arch and corresponds to the lowest nonzero frequency.

### Example 2: Higher Modes

Higher eigenvalues correspond to higher-frequency oscillations with more nodes.

### Example 3: Superposition

A general bounded-string motion is built as a superposition of standing modes.

## Conceptual Questions

1. Why do fixed boundaries lead to quantized frequencies?
2. Why are standing waves naturally described by eigenfunctions?
3. How does the wave equation differ from the heat equation in the time factor after separation?

## Application Problems

1. Why do musical strings have characteristic natural frequencies?
2. How do higher modes affect the tone quality of an instrument?
3. Why are standing waves a natural bridge between PDEs and spectral theory?

## Interactive Teaching Strategies

- Draw the first few standing-wave shapes in class.
- Compare the separated time factor here with the decaying time factor for the heat equation.
- Ask students to connect node count with mode number.
- Emphasize that spectral structure becomes audible in physical examples.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the first few standing-wave shapes and their physical meaning before engaging the full mode expansion.

### Challenge for Advanced Students

Advanced students can study normal-mode superposition and the relationship between bounded and whole-line wave solutions.

## Summary

On bounded intervals, wave motion is naturally expressed through standing modes. Separation of variables turns geometry into spectral structure and shows how fixed boundaries quantize the possible frequencies of vibration.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Natural frequencies of a fixed string
- Problem: We want the normal modes of a violin string or an idealized cable fixed at both ends.
- Model:
$$ u_{tt}=c^2u_{xx}, \qquad u(0,t)=u(L,t)=0. $$
- Assumptions and limitations: Perfectly fixed ends, ideal string, small oscillations.
- Interpretation: Separation of variables produces discrete standing-wave modes.

#### Resonance in structural elements
- Problem: A cable or beam driven near a natural frequency can respond with large amplitude.
- Model: The solution is expanded in normal modes compatible with the boundary conditions.
- Assumptions and limitations: Linear regime, no geometric nonlinearity.
- Interpretation: Modal analysis is central to resonance avoidance in design.

### 2. Additional Intuition and Connections

Separation of variables converts one PDE into two coupled ODEs sharing a separation constant. Physically, this means we are looking for spatial shapes that oscillate in time with their own characteristic frequency. A common pitfall is to think every initial condition is a single mode; most are superpositions of many modes.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for n in [1, 2, 3]:
    plt.plot(x, np.sin(n * np.pi * x), label=f"mode {n}")

plt.xlabel("x")
plt.ylabel("shape")
plt.title("First three normal modes of a fixed string")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: standing waves fixed string modes
- search: separation of variables wave equation string
- search: resonance normal modes string animation

### 5. Worked Example

If
$$
u(x,0)=\sin\!\left(\frac{\pi x}{L}\right), \qquad u_t(x,0)=0,
$$
then only the fundamental mode is excited and the solution is
$$
u(x,t)=\cos\!\left(\frac{\pi c t}{L}\right)\sin\!\left(\frac{\pi x}{L}\right).
$$
This shows that an initial shape matching an eigenfunction oscillates without changing its spatial profile.

### 6. Difficulty Layering

**Undergraduate level.** Set up separation of variables and interpret natural frequencies.

**Graduate level.** Connect to Sturm-Liouville theory, orthogonality, and eigenfunction expansion convergence.

## Video tham khảo

- xem trước: [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, English. Separation of variables on a finite string, with the musical modes.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, English. The equation being separated, derived before the series.
- [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, English. The Fourier series that packages those spatial modes.

## References

- Haberman, Chapter 4.
