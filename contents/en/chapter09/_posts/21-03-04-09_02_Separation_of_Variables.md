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

At first sight, a partial differential equation like $$ u_t = \alpha u_{xx} $$ looks vastly harder than an ODE because $$ u(x, t) $$ varies across two coupled dimensions simultaneously. Yet Fourier discovered a disarmingly elegant divide-and-conquer strategy: ask whether there exist special "product" solutions $$ u(x, t) = X(x) T(t) $$ whose spatial shape stays frozen while its overall amplitude scales smoothly in time.

Once you plug $$ X(x)T(t) $$ into the heat equation, space and time pull apart onto opposite sides of the equals sign—reducing one PDE to two elementary ODEs linked only by a single separation constant $$ -\lambda $$!

## Background Knowledge Map: The Separation-of-Variables Engine

1. **The Product Ansatz & Separation Constant:** Substituting $$ u = X(x)T(t) $$ into $$ u_t = \alpha u_{xx} $$ and dividing by $$ \alpha X T $$ gives $$ \frac{T'(t)}{\alpha T(t)} = \frac{X''(x)}{X(x)} = -\lambda $$. Because a function of $$ t $$ alone can equal a function of $$ x $$ alone only if both equal a constant, the PDE splits cleanly into $$ X'' + \lambda X = 0 $$ and $$ T' + \alpha\lambda T = 0 $$.
2. **Spatial BVP Quantizes $$ \lambda_n $$:** Homogeneous boundary conditions on $$ X(x) $$ select the discrete eigenvalues $$ \lambda_n $$ and orthogonal eigenfunctions $$ X_n(x) $$, guaranteeing every mode satisfies the BCs automatically.
3. **Principle of Linear Superposition:** A single product solution $$ X_n(x) T_n(t) $$ almost never matches an arbitrary initial temperature $$ f(x) $$. Because the PDE and homogeneous BCs are linear, any convergent series $$ u(x, t) = \sum c_n X_n(x) e^{-\alpha \lambda_n t} $$ remains an exact solution.
4. **Initial Condition via Orthogonality:** Setting $$ t = 0 $$ gives $$ f(x) = \sum c_n X_n(x) $$, determining every coefficient $$ c_n $$ by a Fourier projection integral.

### Step-by-Step Worked Example (Read Slowly): Separating $$ u_t = 2 u_{xx} $$ on $$ [0, \pi] $$ with $$ u(0, t) = u(\pi, t) = 0 $$

**Problem:** Solve $$ u_t = 2 u_{xx} $$ on $$ 0 < x < \pi $$, $$ t > 0 $$, with $$ u(0, t) = u(\pi, t) = 0 $$ and $$ u(x, 0) = 5\sin(x) - 3\sin(4x) $$, and compute the ratio of the $$ n=4 $$ amplitude to the $$ n=1 $$ amplitude at $$ t = 0.1 $$.

1. **Separate variables $$ u(x, t) = X(x)T(t) $$:**
   $$ \frac{T'}{2T} = \frac{X''}{X} = -\lambda \implies \begin{cases} X'' + \lambda X = 0, & X(0) = X(\pi) = 0, \\ T' + 2\lambda T = 0. \end{cases} $$
2. **Solve the spatial and temporal ODEs:**
   - Spatial BVP gives $$ \lambda_n = n^2 $$, $$ X_n(x) = \sin(nx) $$ for $$ n = 1, 2, 3, \dots $$
   - Temporal ODE gives $$ T_n(t) = e^{-2n^2 t} $$.
   - General superposed solution: $$ u(x, t) = \sum_{n=1}^{\infty} b_n \sin(nx)\,e^{-2n^2 t} $$.
3. **Match the initial condition $$ u(x, 0) = 5\sin(x) - 3\sin(4x) $$:**
   By orthogonality of $$ \{\sin(nx)\} $$, we read off immediately $$ b_1 = 5 $$, $$ b_4 = -3 $$, and all other $$ b_n = 0 $$:
   $$ u(x, t) = 5\sin(x)\,e^{-2t} - 3\sin(4x)\,e^{-32t}. $$
4. **Verify the PDE and compare mode decay at $$ t = 0.1 $$:**
   - PDE check: $$ u_t = -10\sin(x)e^{-2t} + 96\sin(4x)e^{-32t} = 2\bigl[-5\sin(x)e^{-2t} + 48\sin(4x)e^{-32t}\bigr] = 2 u_{xx} $$. Exact!
   - At $$ t = 0.1 $$: mode 1 amplitude is $$ 5 e^{-0.2} \approx 4.0937 $$, while mode 4 amplitude is $$ 3 e^{-3.2} \approx 0.1223 $$. The ratio dropped from $$ 3/5 = 0.60 $$ at $$ t = 0 $$ down to $$ 0.030 $$—a 20-fold suppression of the higher ripple in just 0.1 seconds!

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

## Video tham khảo

- xem trước: [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, English. 3Blue1Brown separates variables and watches the Fourier modes of temperature decay.
- [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, English. Brunton's separation-of-variables method, practiced here on the heat equation.
- [(PT đạo hàm riêng) Bài 2: Phương Trình Truyền Nhiệt](https://www.youtube.com/watch?v=fFyhBMbUhLQ) — Học Toán Cùng Hải Sơn, Vietnamese. Học Toán Cùng Hải Sơn introduces the heat equation in Vietnamese.

## References

- Evans, Chapter 2.
- Haberman, Chapters 1-2.
