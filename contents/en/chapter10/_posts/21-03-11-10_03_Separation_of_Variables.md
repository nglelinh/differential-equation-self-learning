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

## References

- Haberman, Chapter 4.
