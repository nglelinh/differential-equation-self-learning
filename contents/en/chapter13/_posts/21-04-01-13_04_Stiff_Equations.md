---
layout: post
title: "13-04 Stiff Equations"
chapter: '13'
order: 4
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: required
---

> **Storytelling Hook:** In a chemical combustion reaction, one radical species decays in a microsecond ($e^{-10^6 t}$) while the flame front evolves over whole seconds. Even after the fast radical has vanished to $10^{-100}$, an explicit solver like RK4 is held hostage—forced to crawl at microsecond steps just to keep the dead mode from exploding. That tyranny of separated timescales is **stiffness**, and breaking it requires implicit methods.

## Learning Objectives

This lesson introduces stiff differential equations and the numerical challenges they create. Students should understand why explicit methods may fail despite smooth true solutions, how stability regions become decisive, and why implicit methods are often preferred.

## Prerequisites

Students should know Euler methods, stability ideas for numerical schemes, and basic test equations such as exponential decay.

## Key ideas: Anatomy of Stiffness and Implicit Stability

Four core concepts separate stiff ODEs from ordinary non-stiff problems:

1. **Timescale Separation and Eigenvalue Spread:** A system $y' = Ay$ is stiff when its Jacobian has eigenvalues with large negative real parts ($\text{Re}(\lambda_i) \ll 0$) alongside slow modes—meaning the stiffness ratio $\max |\text{Re}(\lambda_i)| / \min |\text{Re}(\lambda_i)| \gg 1$ forces stability, not accuracy, to dictate the explicit step size.
2. **A-Stability (Left Half-Plane Inclusion):** A solver is **A-stable** if its stability region $\{z \in \mathbb{C} : |R(z)| \le 1\}$ contains the entire left half-plane $\text{Re}(z) \le 0$. Backward Euler ($R(z) = (1-z)^{-1}$) and the trapezoidal rule ($R(z) = \frac{1+z/2}{1-z/2}$) are A-stable; no explicit RK method can ever be A-stable.
3. **L-Stability and Fast Transient Damping:** Even among A-stable methods, the trapezoidal rule has $\lim_{\text{Re}(z)\to -\infty} R(z) = -1$, causing persistent ringing on ultra-stiff modes. **L-stable** methods (like Backward Euler and Radau IIA) satisfy $\lim_{z\to\infty} R(z) = 0$, killing dead modes cleanly.
4. **Newton Iteration Inside Implicit Steps:** Solving $y_{n+1} - h f(t_{n+1}, y_{n+1}) = y_n$ for nonlinear stiff systems requires Newton's method with the Jacobian $I - h J_f$, trading slightly higher per-step linear-algebra cost for $10^3\times$–$10^6\times$ larger time steps.

## Introduction

![Stiff equations]({{ site.imgurl }}/chapter_img/chapter13/04_stiff_equations.svg)

Some ODEs are numerically difficult not because the exact solution is complicated, but because the problem contains widely separated time scales. A solution may decay smoothly and quietly while explicit numerical methods require absurdly small time steps just to remain stable. This is the hallmark of stiffness.

Stiffness is one of the most important ideas in modern numerical ODE theory because it separates naive computation from genuinely robust computation.

## Concept in Three Ways

### Intuitive View

A stiff problem contains very fast transient behavior together with much slower dynamics. Even when the fast part dies out quickly, it can still control the time-step restrictions of explicit methods.

### Visual View

The exact solution may look smooth and simple, while the numerical method oscillates or blows up if the step size is too large. This mismatch is one of the clearest visual signs of stiffness.

### Formal View

The test equation
$$ y' = \lambda y, $$
with large negative $$ \lambda $$ is the standard model. Explicit Euler is stable only when $$ \lvert 1+h\lambda\rvert<1 $$, forcing very small $$ h $$ if $$ \lambda $$ is large in magnitude. Implicit schemes often remain stable for much larger time steps.

## Why Stiffness Matters

Stiffness changes what it means for a method to be practical. Accuracy alone is not enough; stability may dominate the cost of computation.

This lesson is also an important turning point because it motivates implicit methods and stability-region analysis in a concrete and compelling way.

## Common Misconceptions

### "Stiffness means the exact solution is wildly oscillatory"

Not necessarily. The exact solution may be completely smooth.

### "A smaller time step is always the right answer"

In principle yes, but in practice it may make the method computationally useless.

### "Stiffness is a rare specialized issue"

No. It appears frequently in chemical kinetics, control, reaction networks, and many coupled systems.

## Suggested Learning Path

### Step 1: Study the test equation

Students should see stiffness emerge first in the simplest setting.

### Step 2: Compare exact and numerical behavior

This reveals the central paradox of stiffness.

### Step 3: Introduce stability regions

This makes the explicit/implicit contrast mathematically precise.

### Step 4: Motivate implicit methods

The point is not only that stiffness exists, but that method choice must adapt to it.

### Checkpoints

- Can students explain why a stable exact solution may still be numerically difficult?
- Do they understand why explicit methods are often restricted by stiffness?
- Can they say why implicit methods help?

## Worked Examples


### Worked example: Explicit vs. Implicit Euler on a Stiff Decay-Forcing ODE

Consider the stiff IVP $y' = -1000(y - \cos t) - \sin t$ with $y(0) = 2$, whose exact solution is $y(t) = \cos t + e^{-1000 t}$. Take a single step of size $h = 0.01$ (well suited to track $\cos t$, yet $10\times$ larger than the fast timescale $10^{-3}$) with both forward Euler and backward Euler.

1. **Exact solution at $t_1 = 0.01$:**
   $$y(0.01) = \cos(0.01) + e^{-10} \approx 0.999950 + 0.000045 = 0.999995.$$
2. **Forward (Explicit) Euler step ($h = 0.01$):** At $t_0 = 0, y_0 = 2$, $f(0, 2) = -1000(2 - 1) - 0 = -1000$. Thus:
   $$y_1^{\text{FE}} = 2 + 0.01(-1000) = -8.0.$$
   At the next step, $y_2^{\text{FE}} \approx +82$, blowing up exponentially because $|1 - 1000h| = |-9| = 9 > 1$!
3. **Backward (Implicit) Euler step ($h = 0.01$):** Solve $y_1 = y_0 + h\big(-1000(y_1 - \cos(0.01)) - \sin(0.01)\big)$ algebraically for $y_1$:
   $$y_1 + 10 y_1 = 2 + 10\cos(0.01) - 0.01\sin(0.01) \implies 11 y_1 \approx 2 + 9.99950 - 0.00010 = 11.99940.$$
   Dividing by $11$ gives:
   $$y_1^{\text{BE}} \approx 1.09085.$$
   On step 2 ($t_2 = 0.02$), $y_2^{\text{BE}} \approx 1.0080$, snapping right onto the slow curve $\cos t$ with zero instability—demonstrating why L-stable implicit solvers conquer stiffness.

### Example 1: Large Negative Decay Constant

The exact solution decays rapidly, but explicit Euler demands a tiny step to avoid instability.

### Example 2: Backward Euler on the Same Problem

Backward Euler remains stable with much larger step sizes, illustrating the practical value of implicit methods.

### Example 3: Multi-Scale Dynamics

A system with fast and slow components shows how one time scale can dominate the numerical restriction even when the other is the main feature of interest.

## Conceptual Questions

1. Why can a simple decaying solution still be numerically stiff?
2. Why does stiffness turn stability into the dominant issue?
3. Why are implicit methods often the natural response to stiffness?

## Application Problems

1. Why do reaction networks and kinetics frequently generate stiff systems?
2. Why might explicit RK methods become inefficient on stiff problems even if they are highly accurate in nonstiff settings?
3. Why is the numerical cost of stiffness often about stability rather than accuracy?

## Interactive Teaching Strategies

- Compare exact solution graphs with unstable explicit Euler approximations.
- Use the test equation repeatedly as an anchor model.
- Emphasize the difference between continuous stability and discrete stability.
- Reinforce that stiffness is a computational phenomenon as much as a modeling one.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the scalar test equation before confronting large systems.

### Challenge for Advanced Students

Advanced students can study A-stability, L-stability, or stiff system examples from applications.

## Summary

Stiff equations are numerically challenging because stability restrictions, not solution complexity, dominate the step size. They motivate implicit methods and make stability analysis an essential part of numerical ODE theory.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Fast-slow chemical kinetics
- Problem: Some reactions decay extremely fast while the main observed behavior evolves slowly.
- Model: On the test equation
$$ y'=\lambda y,\qquad \Re(\lambda)\ll 0, $$
forward Euler requires very small steps for stability.
- Assumptions and limitations: There is a strong separation of time scales.
- Interpretation: Stiffness means stability, not accuracy alone, forces tiny time steps.

#### Electrical circuits with widely separated time scales
- Problem: State equations may contain very fast and very slow modes simultaneously.
- Model: Backward Euler or BDF methods are used for stiff linear systems.
- Assumptions and limitations: Each step requires solving an implicit system.
- Interpretation: Implicit methods cost more per step but may allow vastly larger stable steps.

### 2. Additional Intuition and Connections

Stiffness is a numerical phenomenon, not just a physical one. The exact solution may look smooth and slowly varying, yet explicit methods are trapped by a rapidly decaying hidden mode. A common pitfall is to diagnose stiffness only from the solution plot; stability restrictions are the real signature.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

lam = -15.0
h_values = [0.05, 0.15, 0.2]
N = 20

for h in h_values:
    y = np.zeros(N + 1)
    y[0] = 1.0
    for n in range(N):
        y[n + 1] = y[n] + h * lam * y[n]
    plt.plot(range(N + 1), y, "o-", label=f"h={h}")

plt.axhline(0, color="black", linewidth=0.8)
plt.legend()
plt.title("Forward Euler on the stiff test equation y' = lambda y")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: stiff equation forward backward Euler stability
- search: Dahlquist test equation visualization
- search: chemistry stiff ODE numerical example

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="Stiff equation: forward versus backward Euler" description="Change the negative eigenvalue and step size to compare explicit and implicit behavior on the stiff test equation." path="interactives/chapter13/stiff-equations-en.html" height="640px" %}

### 5. Worked Example

For
$$ y'=-15y,\qquad y(0)=1, $$
forward Euler has amplification factor
$$ 1+h\lambda = 1-15h. $$
Stability requires
$$ \lvert 1-15h\rvert<1, $$
so $$ 0<h<\frac{2}{15} $$. Even though the exact solution decays smoothly to zero, the numerical step size is severely constrained.

### 6. Difficulty Layering

**Undergraduate level.** Recognize stiffness through the test equation and compare explicit versus implicit methods.

**Graduate level.** Connect to A-stability, L-stability, and singular perturbations.

## Video tham khảo

- xem trước: [Stability of Forward Euler and Backward Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=RdXCGnTT6UY) — Steve Brunton, English. Why forward Euler collapses on a stiff decay while backward Euler does not.
- [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, English. The implicit step that stiffness forces you to take.
- [Numerical Integration of ODEs with Forward Euler and Backward Euler in Python and Matlab](https://www.youtube.com/watch?v=ITFolyl_66U) — Steve Brunton, English. A numerical comparison of the explicit and implicit Euler schemes.

## References

- Ascher & Petzold: classic reference for stiffness and implicit methods.
