---
layout: post
title: "09-08 Numerical Methods: Finite Differences"
chapter: '09'
order: 8
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: optional
---

Try stepping the heat equation forward in time on a computer using the most natural explicit finite-difference formula, $$ u_j^{n+1} = u_j^n + r(u_{j+1}^n - 2u_j^n + u_{j-1}^n) $$, where $$ r = \frac{\alpha \Delta t}{(\Delta x)^2} $$. With $$ r = 0.49 $$, your simulation glides smoothly to the true physical curve. Nudge the time step up by a hair to $$ r = 0.51 $$, and within twenty steps your screen explodes into jagged $$ \pm 10^{12} $$ sawtooth oscillations!

Why does $$ r = \frac{1}{2} $$ act like a razor-sharp cliff between stability and numerical catastrophe? Understanding von Neumann Fourier stability analysis—and how implicit schemes like Backward Euler and Crank–Nicolson abolish the $$ \Delta t \le \frac{(\Delta x)^2}{2\alpha} $$ barrier—is essential for every scientist who simulates PDEs.

## Background Knowledge Map: Discretization, Stability Cliffs, and Implicit Solvers

1. **FTCS (Explicit) Scheme & Discrete Maximum Principle:** Rewriting $$ u_j^{n+1} = r u_{j-1}^n + (1 - 2r) u_j^n + r u_{j+1}^n $$ reveals a weighted average of three neighbors *if and only if* $$ 1 - 2r \ge 0 \iff r \le \frac{1}{2} $$. The moment $$ r > \frac{1}{2} $$, the center weight turns negative and alternating oscillations amplify every step!
2. **Von Neumann Stability Analysis (Fourier Mode Amplification):** Substituting a discrete spatial wave $$ u_j^n = G^n e^{i k j \Delta x} $$ yields the amplification factor $$ G(k) = 1 - 4r \sin^2\!\left(\frac{k\Delta x}{2}\right) $$. Stability requires $$ |G(k)| \le 1 $$ for all $$ k $$, which at the highest grid mode ($$ \sin^2 = 1 $$) enforces $$ 1 - 4r \ge -1 \iff r \le \frac{1}{2} $$.
3. **Backward Euler & Crank–Nicolson (Unconditional Stability):** Evaluating $$ u_{xx} $$ at the *new* time level $$ n+1 $$ (Backward Euler) gives $$ G = \frac{1}{1 + 4r\sin^2(k\Delta x/2)} \in (0, 1] $$ for *every* $$ r > 0 $$. Averaging levels $$ n $$ and $$ n+1 $$ (Crank–Nicolson) achieves **second-order accuracy** $$ O((\Delta t)^2 + (\Delta x)^2) $$ while staying unconditionally stable—at the modest cost of solving a fast $$ O(M) $$ tridiagonal Thomas system per step!
4. **Lax Equivalence Theorem:** For a consistent linear finite-difference scheme, *stability is both necessary and sufficient for convergence* to the true PDE solution as $$ \Delta x, \Delta t \to 0 $$.

### Step-by-Step Worked Example (Read Slowly): Hand-Stepping FTCS Across the $$ r = 0.5 $$ Stability Cliff

**Problem:** Simulate $$ u_t = u_{xx} $$ on $$ [0, 1] $$ with $$ u(0, t) = u(1, t) = 0 $$, grid spacing $$ \Delta x = 0.25 $$ (interior nodes $$ j = 1, 2, 3 $$ at $$ x = 0.25, 0.50, 0.75 $$), and initial vector $$ u^0 = [0, 0, 1, 0, 0] $$ (a unit spike at the midpoint). Compute two FTCS steps for (a) $$ r = 0.25 $$ (stable) and (b) $$ r = 0.75 $$ (unstable), and check the amplification factor $$ G $$ of the sawtooth mode.

1. **Case (a): Stable step $$ r = 0.25 $$ ($$ \Delta t = \frac{1}{64} $$):**
   Update rule: $$ u_j^{n+1} = 0.25 u_{j-1}^n + 0.50 u_j^n + 0.25 u_{j+1}^n $$.
   - **Step $$ n = 1 $$:**
     - $$ u_1^1 = 0.25(0) + 0.50(0) + 0.25(1) = 0.25 $$.
     - $$ u_2^1 = 0.25(0) + 0.50(1) + 0.25(0) = 0.50 $$.
     - $$ u_3^1 = 0.25(1) + 0.50(0) + 0.25(0) = 0.25 $$.
     So $$ u^1 = [0, 0.25, 0.50, 0.25, 0] $$ (smooth, nonnegative, max drops from $$ 1 $$ to $$ 0.50 $$!).
   - **Step $$ n = 2 $$:**
     - $$ u_1^2 = 0.25(0) + 0.50(0.25) + 0.25(0.50) = 0.25 $$.
     - $$ u_2^2 = 0.25(0.25) + 0.50(0.50) + 0.25(0.25) = 0.375 $$.
     - $$ u_3^2 = 0.25 $$.
     So $$ u^2 = [0, 0.25, 0.375, 0.25, 0] $$—clean physical diffusion!
2. **Case (b): Unstable step $$ r = 0.75 $$ ($$ \Delta t = \frac{3}{64} $$):**
   Update rule: $$ u_j^{n+1} = 0.75 u_{j-1}^n - 0.50 u_j^n + 0.75 u_{j+1}^n $$.
   - **Step $$ n = 1 $$:** $$ u_1^1 = 0.75 $$, $$ u_2^1 = -0.50 $$ (unphysical negative temperature!), $$ u_3^1 = 0.75 $$.
   - **Step $$ n = 2 $$:** $$ u_1^2 = -0.50(0.75) + 0.75(-0.50) = -0.75 $$, $$ u_2^2 = 0.75(0.75) - 0.50(-0.50) + 0.75(0.75) = +1.375 $$ (already *higher* than the initial peak of $$ 1 $$!), $$ u_3^2 = -0.75 $$.
3. **Von Neumann confirmation:** For the alternating sawtooth mode ($$ \sin^2(k\Delta x/2) = 1 $$), $$ G = 1 - 4(0.75) = -2.0 $$, so every step flips sign and *doubles* the error!

## Learning Objectives

This lesson introduces finite-difference schemes for the heat equation. Students should understand the basic explicit and implicit discretizations, stability concerns, and why numerical diffusion and time-step restrictions matter.

## Prerequisites

Students should know the heat equation, partial derivatives, and the basic idea of replacing derivatives by difference quotients.

## Introduction

![Finite differences for heat equation]({{ site.imgurl }}/chapter_img/chapter09/08_numerical_methods_heat_fd.svg)

Exact PDE solutions are invaluable, but they are not always available in realistic geometries or with complicated forcing. Numerical methods provide the practical bridge from mathematical model to computation. For the heat equation, finite differences are the classical first method to learn.

The key idea is simple: replace derivatives by grid-based approximations in space and time, then evolve the discrete system numerically.

## Concept in Three Ways

### Intuitive View

We replace the continuous rod by a grid of sample points and update the temperature at each point based on nearby values. Diffusion becomes a rule for local averaging across the mesh.

### Visual View

Each grid point exchanges information with its neighbors. Repeated time-stepping mimics the spreading and smoothing behavior of heat.

### Formal View

The second derivative is approximated by a centered difference, while the time derivative may be approximated explicitly or implicitly. This leads to update rules such as the forward-time centered-space scheme.

## Why Numerical Methods Matter

Finite differences show how PDEs become algorithms. They also reveal an important lesson: a mathematically correct PDE does not automatically yield a good numerical scheme. Stability, consistency, and convergence must all be considered.

This lesson also gives a practical interpretation of the heat equation as repeated local averaging, which deepens physical intuition.

## Common Misconceptions

### "If the continuous PDE is stable, any discrete scheme will also be stable"

No. Discretization can create instability if the time step and mesh size are poorly chosen.

### "Numerical diffusion is the same as physical diffusion"

Not always. A scheme may introduce extra artificial smoothing.

### "Implicit methods are always better"

Not necessarily. They have stability advantages, but they also require solving systems at each time step.

## Suggested Learning Path

### Step 1: Build the grid

Students should understand how space and time are discretized.

### Step 2: Approximate the derivatives

This converts the PDE into an algebraic update rule.

### Step 3: Compare explicit and implicit schemes

The tradeoff between simplicity and stability should be emphasized.

### Step 4: Discuss stability restrictions

The CFL-type condition is one of the key lessons of the topic.

### Checkpoints

- Can students explain the local averaging idea behind diffusion discretization?
- Do they understand why the time step cannot be chosen arbitrarily in explicit schemes?
- Can they compare explicit and implicit methods qualitatively?

## Worked Examples

### Example 1: Explicit Scheme

The forward-time centered-space method updates each grid value using neighboring temperatures from the previous step.

### Example 2: Stability Restriction

If the time step is too large compared with the square of the mesh width, oscillations or blow-up may appear numerically even though the PDE itself is diffusive.

### Example 3: Implicit Scheme

An implicit discretization is more stable but requires solving a linear system at each step.

## Conceptual Questions

1. Why does finite differencing turn diffusion into local averaging on a grid?
2. Why can a numerical method be unstable even when the PDE is stable?
3. Why are implicit methods often preferred for stiff diffusion problems?

## Application Problems

1. Why are numerical schemes essential for realistic PDE geometries?
2. How might artificial numerical diffusion distort a physical simulation?
3. Why is computational efficiency part of the mathematics of numerical PDEs?

## Interactive Teaching Strategies

- Have students compute one or two time steps by hand on a tiny grid.
- Compare stable and unstable simulations conceptually.
- Use the phrase "continuous model, discrete algorithm" repeatedly.
- Tie stability restrictions to the physical interpretation of diffusion.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the grid picture and local averaging before handling scheme formulas abstractly.

### Challenge for Advanced Students

Advanced students can study von Neumann analysis or compare finite differences with finite element methods.

## Summary

Finite differences turn diffusion PDEs into computable grid dynamics. They provide the first practical route from exact analysis to simulation and teach the crucial distinction between continuous PDE behavior and discrete numerical stability.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Numerical heat simulation
- Problem: We need approximate solutions when closed-form formulas are inconvenient or impossible.
- Model:
$$
u_j^{n+1}=u_j^n+r\left(u_{j+1}^n-2u_j^n+u_{j-1}^n\right).
$$
- Assumptions and limitations: Uniform grid, one-dimensional domain, CFL-type stability restriction.
- Interpretation: The scheme imitates the smoothing mechanism of the continuous heat equation.

#### Implicit time-stepping in engineering
- Problem: We want larger time steps without instability.
- Model: Backward Euler or Crank-Nicolson discretizations.
- Assumptions and limitations: Each time step requires solving a linear system.
- Interpretation: Better stability is purchased with extra algebraic work.

### 2. Additional Intuition and Connections

Finite-difference methods show how the PDE becomes a grid-based evolution rule. A common pitfall is to think that once we discretize, correctness is automatic. Stability and convergence must still be analyzed carefully.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

Nx = 80
dx = 1 / Nx
r = 0.45
x = np.linspace(0, 1, Nx + 1)
u = np.sin(np.pi * x)

snapshots = [u.copy()]
for _ in range(80):
    un = u.copy()
    u[1:-1] = un[1:-1] + r * (un[2:] - 2 * un[1:-1] + un[:-2])
    snapshots.append(u.copy())

for idx in [0, 10, 40, 80]:
    plt.plot(x, snapshots[idx], label=f"step {idx}")
plt.xlabel("x")
plt.ylabel("u")
plt.title("Finite-difference evolution for the heat equation")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: finite difference heat equation stability animation
- search: explicit implicit heat equation comparison
- search: CFL condition heat equation visualization

### 5. Worked Example

For the explicit scheme,
$$ r=\frac{\alpha^2 \Delta t}{(\Delta x)^2}, $$
the classical stability condition is
$$ r\le \frac{1}{2}. $$
If $$ r $$ is chosen too large, the numerical solution can blow up even though the true solution is smooth and decaying.

### 6. Difficulty Layering

**Undergraduate level.** Implement the explicit method and understand the stability restriction.

**Graduate level.** Use von Neumann analysis, compare explicit and implicit methods, and connect consistency-stability-convergence.

## Video tham khảo

- xem trước: [PDE | Finite differences: introduction](https://www.youtube.com/watch?v=g3Xw1r7QGOE) — commutant, English. commutant introduces finite differences for PDEs.
- [Finite Difference Method for PDES: Solution of Heat Equation](https://www.youtube.com/watch?v=ACduEf-K9qk) — Easy Mathematics, English. A finite-difference scheme written for the heat equation.
- [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, English. Forward and backward Euler, the time discretizations those heat schemes use.

## References

- Evans, Chapter 2.
