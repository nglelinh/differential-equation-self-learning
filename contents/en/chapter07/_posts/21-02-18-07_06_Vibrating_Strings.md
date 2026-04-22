---
layout: post
title: "07-06 Applications: Vibrating Strings"
chapter: '07'
order: 6
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: required
---

## Learning Objectives

This lesson connects the whole chapter to the classical vibrating-string model. Students should understand how boundary conditions, eigenvalues, eigenfunctions, and mode superposition all arise naturally in the analysis of standing waves.

## Prerequisites

Students should know BVPs, eigenvalue problems, and eigenfunction expansions. Some physical intuition about waves on strings is also helpful.

## Introduction

![Standing-wave modes of a vibrating string]({{ site.imgurl }}/chapter_img/chapter07/06_vibrating_strings.svg)

The vibrating string is the canonical physical model behind much of boundary-value spectral theory. Fixed endpoints create a spatial boundary value problem, and that BVP selects a discrete family of standing-wave modes. Once those modes are known, arbitrary initial displacements and velocities can be expanded in that basis.

This lesson is valuable because it unifies the whole chapter. The string problem is where boundary conditions, eigenvalues, orthogonality, and generalized Fourier series all become physically transparent.

## Concept in Three Ways

### Intuitive View

A string fixed at both ends cannot vibrate arbitrarily. Only certain spatial shapes fit the two endpoints. Those shapes are the standing modes, and each has its own characteristic frequency.

### Visual View

The first mode has one arch, the second has two, the third has three, and so on. These shapes do not change form in time; only their amplitudes oscillate.

### Formal View

For the wave equation
$$ u_{tt}=c^2u_{xx},\qquad 0<x<L, $$
with
$$ u(0,t)=u(L,t)=0, $$
separation of variables gives
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0. $$
Hence
$$
X_n(x)=\sin\left(\frac{n\pi x}{L}\right),\qquad
\omega_n=c\frac{n\pi}{L}.
$$

## Common Misconceptions

- "Any initial shape is itself a single standing mode." Usually not; it is a superposition of many modes.
- "The eigenfunctions are just algebraic artifacts." Wrong. They are the observable standing-wave patterns.
- "Boundary conditions only adjust constants." Wrong. They determine the allowable mode family.
- "The time dependence is the hard part." In the separated problem, the spatial boundary-value problem is the decisive structural step.

## Suggested Learning Path

### Step 1: Derive the Spatial BVP

Students should see exactly how the wave equation leads to the eigenvalue problem.

### Step 2: Solve for Standing Modes

The sine family is the central result.

### Step 3: Connect Modes to Frequencies

Students should translate eigenvalues into physical oscillation frequencies.

### Step 4: Expand General Initial Data

This is where the full chapter machinery comes together.

### Checkpoints

- Can students derive the fixed-end eigenfunctions?
- Do they understand why the frequencies are discrete?
- Can they explain what mode superposition means physically?

## Worked Examples

### Example 1: First Three Modes

For a string of length $$ L $$,
$$
X_1(x)=\sin\left(\frac{\pi x}{L}\right),\qquad
X_2(x)=\sin\left(\frac{2\pi x}{L}\right),\qquad
X_3(x)=\sin\left(\frac{3\pi x}{L}\right).
$$
These are the first three standing-wave patterns.

### Example 2: Frequency Formula

The corresponding frequencies satisfy
$$ \omega_n=c\frac{n\pi}{L}. $$
So higher modes oscillate faster and have more internal nodes.

### Example 3: General Solution

The full string displacement is
$$
u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cos(\omega_n t)+B_n\sin(\omega_n t)\right)\sin\left(\frac{n\pi x}{L}\right).
$$
The coefficients are determined from the initial displacement and velocity.

## Conceptual Questions

1. Why do fixed endpoints force a discrete frequency spectrum?
2. What is the difference between a standing mode and a general motion?
3. Why is the sine basis the natural spatial basis for this problem?

## Application Problems

1. In musical acoustics, why do string instruments produce harmonic overtones?
2. In mechanical engineering, how can mode analysis help prevent resonance damage?
3. How would changing one endpoint from fixed to free alter the spatial eigenfunctions?

## Interactive Teaching Strategies

- Plot and discuss the first few standing modes before deriving formulas.
- Relate the mode shapes to musical harmonics or physical strings.
- Ask students to describe a general initial profile as a mixture of modes.
- Use both static mode plots and time-varying interpretation.

## Differentiation

### Support for Struggling Students

Students who need support should focus on the first few modes and the core idea that general motion is built from mode superposition.

### Challenge for Advanced Students

Advanced students can compare fixed-fixed, free-free, and fixed-free boundary conditions and study how the spectrum changes.

## Summary

The vibrating string is the archetypal boundary-value spectral problem. Its standing modes, frequencies, and expansions illustrate nearly every major idea of the chapter in a physically vivid way.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Fixed string vibration
- Problem: Find the standing-wave modes and natural frequencies of a string fixed at both ends.
- Model:
$$ u_{tt}=c^2 u_{xx},\qquad u(0,t)=u(L,t)=0. $$
After separation:
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0. $$
- Assumptions and limitations: Thin string, uniform tension, small oscillations.
- Interpretation: The eigenmodes are sines and the eigenvalues determine the frequency spectrum.

#### One-dimensional acoustic or elastic resonator
- Problem: A tube or bar supports standing modes that depend on boundary conditions.
- Model: The same Sturm-Liouville structure with Dirichlet, Neumann, or mixed conditions.
- Assumptions and limitations: One-dimensional and undamped.
- Interpretation: Changing the boundary conditions changes the admissible resonances immediately.

### 2. Additional Intuition and Connections

The vibrating string is the physical prototype for the whole chapter: a BVP produces eigenvalues, eigenvalues produce modes, and modes combine into the full solution. A common pitfall is to think of sines and cosines as merely familiar formulas; here they are eigenfunctions of the spatial operator with fixed-end boundary conditions.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 500)

fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, n in zip(axes, [1, 2, 3]):
    y = np.sin(n * np.pi * x / L)
    ax.plot(x, y)
    ax.set_title(f"Mode {n}")
    ax.set_ylim(-1.1, 1.1)
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: vibrating string standing wave modes
- search: fixed ends string eigenmodes animation
- search: boundary conditions standing waves

### 5. Worked Example

From
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0, $$
we obtain
$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$
Therefore the full vibrating-string solution can be written as
$$
u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cos(\omega_n t)+B_n\sin(\omega_n t)\right)X_n(x),
$$
with
$$ \omega_n=c\frac{n\pi}{L}. $$

### 6. Difficulty Layering

**Undergraduate level.** Focus on standing waves, natural frequencies, and mode superposition.

**Graduate level.** Connect to spectral theory of the wave operator, energy, and orthogonal bases in Hilbert spaces.

![Vibrating strings]({{ site.imgurl }}/chapter_img/chapter07/06_vibrating_strings.svg)

## References

- Boyce & DiPrima, Chapters 10-11: standing-wave derivation and mode expansion.
- Haberman, Chapter 5: excellent PDE and physical context.
