---
layout: post
title: "04-08 Nonhomogeneous Systems"
chapter: '04'
order: 8
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

## Learning Objectives

This lesson helps students solve nonhomogeneous linear systems, understand variation of parameters for systems, and interpret how forcing or external input reshapes the natural motion of a system. Students should also see Duhamel's integral formula as the system-level version of forced response from single-equation ODEs.

## Prerequisites

Students should know homogeneous linear systems, the matrix exponential, and basic integration of vector-valued functions. It helps if students already have the intuition that a forced scalar ODE consists of a natural part plus a driven part.

## Introduction

![Linear system with external forcing]({{ site.imgurl }}/chapter_img/chapter04/08_nonhomogeneous_systems.svg)

Real systems rarely evolve in total isolation. They are pushed by inputs, external forces, source terms, control signals, or noise. So instead of
$$ \mathbf{x}'=A\mathbf{x}, $$
we study
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
The solution is no longer just a combination of free modes. It also records the cumulative effect of forcing over time.

This lesson is useful because forcing does not destroy the linear theory already built. The homogeneous system still provides the skeleton. What changes is that constants in the homogeneous solution are replaced by time-dependent quantities, or equivalently, the forcing is accumulated through an integral involving the matrix exponential.

## Concept in Three Ways

### Intuitive View

The homogeneous system tells us how the system would move on its own. The forcing term tells us how the outside world keeps nudging it. The actual trajectory is the combination of self-dynamics and accumulated external influence.

### Visual View

Without forcing, trajectories follow the system's own flow. With forcing, the flow is continually bent by incoming input. In state space, the path is not only shaped by the matrix $$ A $$ but also by where and when the forcing term injects motion.

### Formal View

For
$$
\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t),
\qquad
\mathbf{x}(0)=\mathbf{x}_0,
$$
variation of parameters gives
$$
\mathbf{x}(t)=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
The first term is the free response, and the integral term is the forced response. This formula is often called Duhamel's principle in the context of linear systems.

## Common Misconceptions

- "The forcing term just adds directly to the final answer." Wrong. Its contribution is filtered through the system dynamics.
- "Only periodic forcing is interesting." Wrong. Constant, impulsive, transient, and control-driven inputs are all important.
- "The homogeneous solution becomes irrelevant once forcing is added." Wrong. It still determines transients and stability.
- "Variation of parameters is a completely new method unrelated to earlier work." Wrong. It is built directly on the homogeneous solution operator $$ e^{At} $$.

## Suggested Learning Path

### Step 1: Separate Free and Forced Parts

Students should clearly identify the role of $$ A\mathbf{x} $$ and the role of $$ \mathbf{g}(t) $$.

### Step 2: Derive Variation of Parameters

Seeing where the integral formula comes from prevents it from feeling like a black-box recipe.

### Step 3: Work Easy Forcing Examples

Constant or exponential inputs help students practice the formula without too much algebra.

### Step 4: Interpret Long-Time Behavior

Students should ask which part decays, which part persists, and how forcing can create steady states or ongoing oscillations.

### Checkpoints

- Can students state the variation-of-parameters formula correctly?
- Can students distinguish transient behavior from sustained forced behavior?
- Can students explain why forcing is convolved with the matrix exponential?

## Worked Examples

### Example 1: Constant Forcing in a Diagonal System

Consider
$$
\mathbf{x}'=
\begin{pmatrix}
-1 & 0\\
0 & -2
\end{pmatrix}\mathbf{x}
+
\begin{pmatrix}
1\\
3
\end{pmatrix}.
$$
The homogeneous system is stable, so transients decay. Each component behaves like a forced first-order equation:
$$ x_1'=-x_1+1,
\qquad
x_2'=-2x_2+3. $$
The long-term state is
$$
\begin{pmatrix}
1\\
\frac{3}{2}
\end{pmatrix}.
$$
This example helps students see that forcing can create a nonzero equilibrium.

### Example 2: Variation of Parameters Formula

For general input $$ \mathbf{g}(t) $$,
$$
\mathbf{x}(t)=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
If $$ A $$ is stable, then the first term typically decays, while the second term controls the long-time behavior. This is the cleanest way to interpret forced linear systems.

### Example 3: Periodic Forcing and Resonance Intuition

If a mechanical system is forced periodically, the forcing term may inject energy repeatedly at frequencies close to the system's natural modes. Even when the exact algebra is more involved, the formula shows that the response depends both on the input and on the system's own matrix structure.

### Example 4: Impulse Response View

Imagine a very short burst of input near time $$ s $$. Its contribution at later time $$ t $$ is approximately
$$ e^{A(t-s)}\Delta\mathbf{u}. $$
So the system's response to general forcing can be understood as a superposition of responses to many tiny input pulses. This is a valuable bridge toward control theory and signal processing.

## Conceptual Questions

1. Why is the forced response written as an integral over past times rather than a simple algebraic term?
2. In a stable system, why can the forced term dominate long-term behavior even if the initial condition was large?
3. What does the kernel $$ e^{A(t-s)} $$ tell us physically?

## Application Problems

1. In an electrical circuit with an applied voltage source, how would you describe the difference between transient current and steady forced response?
2. In economics, if a stable linear model is driven by periodic policy intervention, why might oscillations persist?
3. In control engineering, why is it useful to think of forcing as a history of inputs filtered through system dynamics?

## Interactive Teaching Strategies

- Revisit a familiar scalar forced equation and then generalize each step to vector form.
- Ask students to label terms in the solution as free response and forced response.
- Compare two systems with the same input but different matrices $$ A $$ so students can see how dynamics shape the response.
- Encourage verbal interpretation before symbolic integration.

## Differentiation

### Support for Struggling Students

Students who need more structure should first solve diagonal forced systems, where each component behaves like a familiar scalar ODE. This lets them build confidence before working with full matrix formulas.

### Challenge for Advanced Students

Advanced students can derive the convolution formula carefully, study steady-state periodic response, or connect the formula to Green's functions and semigroup language.

## Summary

Nonhomogeneous linear systems combine self-dynamics with external input. The homogeneous flow still organizes the problem, and the forcing term enters through an accumulated history weighted by the matrix exponential.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Controlled linear systems
- Problem: A state-space model evolves under both internal dynamics and external control.
- Model:
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
- Assumptions and limitations: Constant coefficients and linear forcing.
- Interpretation: The solution contains both the autonomous response and the accumulated forced response.

#### Constant inflow in compartment models
- Problem: A multi-compartment system receives a steady outside source.
- Model:
$$
\mathbf{x}(t)=e^{A(t-t_0)}\mathbf{x}_0+\int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
- Assumptions and limitations: Linearized inflow-outflow structure.
- Interpretation: Duhamel's formula shows how forcing is filtered through the system memory.

#### Small but persistent forcing
- Problem: A small forcing term may dominate the long-term state if it acts long enough.
- Model: The same nonhomogeneous system formula.
- Assumptions and limitations: Linear setting with known forcing.
- Interpretation: Small amplitude does not mean small long-term effect.

### 2. Conceptual Insight

Nonhomogeneous systems make the free-plus-forced decomposition fully explicit in the systems setting. This is the direct analogue of variation of constants from scalar ODEs and a precursor to Duhamel, Green functions, and convolution ideas later.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

A = np.array([[-1, 0],
              [ 0, -2]], dtype=float)

def forcing(t):
    return np.array([1.0, 0.0])

def system(t, X):
    return A @ X + forcing(t)

t = np.linspace(0, 8, 500)
sol = solve_ivp(system, [0, 8], [0, 0], t_eval=t)

plt.plot(sol.t, sol.y[0], label="x1(t)")
plt.plot(sol.t, sol.y[1], label="x2(t)")
plt.xlabel("t")
plt.ylabel("State")
plt.title("Nonhomogeneous system with constant source")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: variation of constants for linear systems visualization
- search: Duhamel formula intuition ODE system
- search: forced linear system state response

### 5. Worked Example

Consider
$$
\mathbf{x}'=
\begin{pmatrix}
-1 & 0\\
0 & -2
\end{pmatrix}\mathbf{x}
+
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
The homogeneous part decays to zero. The new equilibrium satisfies
$$
A\mathbf{x}_*=-
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$
so
$$
\mathbf{x}_*=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Thus the forcing shifts the attracting state from the origin to a new location.

### 6. Difficulty Layering

**Undergraduate level.** Understand the solution formula and the distinction between free and forced parts.

**Graduate level.** Connect with Duhamel's principle, system response, and long-time forcing behavior.

![Nonhomogeneous systems]({{ site.imgurl }}/chapter_img/chapter04/04_08_nonhomogeneous_systems.svg)

## References

- Boyce & DiPrima, Chapter 7: clear examples of forced linear systems.
- Tenenbaum & Pollard: accessible derivations of variation of parameters.
- Kailath, *Linear Systems*: for readers wanting a stronger systems and control perspective.
