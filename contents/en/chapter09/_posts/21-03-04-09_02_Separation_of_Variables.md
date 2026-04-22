---
layout: post
title: "09-02 Separation of Variables"
chapter: '09'
order: 2
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: required
---

## Learning Objectives

This lesson applies separation of variables to the heat equation. Students should see how product solutions reduce the PDE to coupled ODE problems and why eigenvalue structure controls the solution modes.

## Prerequisites

Students should know the derivation of the heat equation, ordinary differential equations, and the basic idea of eigenvalue problems from earlier chapters.

## Introduction

![Separation of variables for heat equation]({{ site.imgurl }}/chapter_img/chapter09/02_separation_of_variables_heat.svg)

Once the heat equation has been derived, the next major question is how to solve it. One of the most beautiful classical methods is separation of variables. The idea is to search for solutions whose dependence on space and time factors into separate pieces. This turns the PDE into two ODE problems linked by a separation constant.

What makes the method so important is not only that it gives explicit solutions, but that it reveals the modal structure of diffusion. Each spatial eigenfunction evolves in time by exponential decay, and the full solution is a superposition of those decaying modes.

## Concept in Three Ways

### Intuitive View

Instead of trying to solve the whole PDE at once, we look for simple modes that evolve independently. Each mode has a fixed spatial shape and a time factor that tells how quickly it decays.

### Visual View

The initial temperature profile can be decomposed into spatial harmonics. Over time, each harmonic decays at its own exponential rate, and the higher modes usually disappear faster.

### Formal View

For the heat equation
$$ u_t = \alpha^2 u_{xx}, $$
we try a product solution
$$ u(x,t)=X(x)T(t). $$
Substituting gives
$$ X(x)T'(t)=\alpha^2 X''(x)T(t), $$
so after division,
$$ \frac{T'}{\alpha^2 T} = \frac{X''}{X} = -\lambda. $$
This yields two ODEs:
$$ X''+\lambda X=0,
\qquad
T'+\alpha^2 \lambda T=0. $$

## Why the Method Matters

Separation of variables is one of the central techniques of classical PDE theory. It converts a PDE into a spectral problem in space and a decay problem in time. This is exactly why Fourier methods become essential.

The method also makes the physical behavior transparent. Each mode is smoothed by diffusion, and higher-frequency modes decay faster. This explains why rough initial data become smoother over time.

## Common Misconceptions

### "Separation of variables always solves the whole problem immediately"

No. It first produces separated modes. The full solution usually requires superposing many such modes to match initial data.

### "The separation constant is arbitrary"

No. Boundary conditions determine the allowable eigenvalues.

### "All modes decay at the same rate"

No. Different eigenvalues produce different decay rates.

## Suggested Learning Path

### Step 1: Try the product ansatz

Students should see why the guess $$ u=XT $$ is natural.

### Step 2: Separate the variables

The PDE becomes two linked ODEs with a separation constant.

### Step 3: Solve the spatial eigenvalue problem

Boundary conditions determine the admissible spatial modes.

### Step 4: Solve the temporal decay equation

Each mode decays exponentially in time.

### Checkpoints

- Can students explain why the separation constant appears?
- Do they understand that the spatial equation is an eigenvalue problem?
- Can they describe the physical meaning of the time factor?

## Worked Examples

### Example 1: Dirichlet Boundary Conditions

For a rod with both ends held at zero temperature, the spatial equation gives sine eigenfunctions and a discrete set of eigenvalues.

### Example 2: Mode Decay

Each separated mode has time dependence
$$ T_n(t)=e^{-\alpha^2 \lambda_n t}, $$
showing that larger eigenvalues decay faster.

### Example 3: Superposition

A general initial profile is reconstructed by adding many separated modes with appropriate Fourier coefficients.

## Conceptual Questions

1. Why does a product ansatz reduce the PDE to ODEs?
2. Why do boundary conditions determine the allowed eigenvalues?
3. Why do higher modes decay faster in diffusion problems?

## Application Problems

1. In a rod with sharply varying initial temperature, why do fine-scale features disappear quickly?
2. Why is separation of variables especially natural on finite intervals?
3. How does the spectral viewpoint help organize the full solution?

## Interactive Teaching Strategies

- Have students derive the separated ODEs themselves before solving them.
- Compare the spatial eigenvalue problem with earlier Sturm-Liouville examples.
- Ask students to interpret the temporal factor as a decay law rather than just a formula.
- Reinforce the phrase "mode-by-mode decay."

## Differentiation

### Support for Struggling Students

Students needing support should focus on the algebra of the separation step and the physical meaning of the product ansatz.

### Challenge for Advanced Students

Advanced students can explore how the method changes under different boundary conditions or in higher dimensions.

## Summary

Separation of variables converts the heat equation into a spectral expansion problem. It reveals diffusion as a superposition of decaying modes and becomes one of the main analytic engines of classical PDE theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Rod with fixed endpoint temperatures
- Problem: We want the full time-dependent temperature when the endpoints are held at fixed values.
- Model:
$$ u_t=\alpha^2 u_{xx},\qquad u(0,t)=u(L,t)=0. $$
- Assumptions and limitations: Homogeneous boundary conditions and one-dimensional geometry.
- Interpretation: Separation of variables produces spatial eigenmodes and exponentially decaying time factors.

#### Decay of thermal modes
- Problem: An arbitrary initial profile decays as a sum of heat modes.
- Model:
$$
u(x,t)=\sum_{n=1}^{\infty}b_n e^{-\alpha^2 \lambda_n t}\phi_n(x).
$$
- Assumptions and limitations: We need an appropriate eigenfunction expansion.
- Interpretation: High-frequency modes decay faster because they carry larger eigenvalues.

### 2. Additional Intuition and Connections

Separation of variables for the heat equation is where Sturm-Liouville theory returns in a vivid way. Each spatial eigenmode decays at its own exponential rate. A common pitfall is to treat separated solutions as an isolated technique rather than as spectral decomposition of the PDE.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for t in [0.0, 0.02, 0.08]:
    u = np.sin(np.pi * x) * np.exp(-np.pi**2 * t) + 0.4 * np.sin(3 * np.pi * x) * np.exp(-9 * np.pi**2 * t)
    plt.plot(x, u, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Decay of heat modes")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: separation of variables heat equation animation
- search: eigenmode decay heat equation
- search: Fourier sine series heat equation

### 5. Worked Example

Set
$$ u(x,t)=X(x)T(t). $$
Then
$$ \frac{T'}{\alpha^2 T}=\frac{X''}{X}=-\lambda. $$
This yields
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0, $$
so
$$
X_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
T_n(t)=e^{-\alpha^2 (n\pi/L)^2 t}.
$$

### 6. Difficulty Layering

**Undergraduate level.** Carry out separation of variables and write the eigenmode series solution.

**Graduate level.** Interpret the solution through semigroups and the generator of heat flow.

## References

- Evans, Chapter 2.
- Haberman, Chapters 1-2.
