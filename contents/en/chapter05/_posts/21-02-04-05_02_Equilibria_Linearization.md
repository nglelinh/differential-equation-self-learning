---
layout: post
title: "05-02 Equilibria and Linearization"
chapter: '05'
order: 2
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

## Learning Objectives

This lesson helps students locate equilibrium points of nonlinear systems, compute the Jacobian matrix, use linearization to predict local behavior, and understand both the power and the limits of the linear approximation.

## Prerequisites

Students should know matrix methods for linear systems, eigenvalues, and phase portraits. They should also be comfortable differentiating multivariable functions and interpreting equilibrium points.

## Introduction

![Linearization near an equilibrium point]({{ site.imgurl }}/chapter_img/chapter05/02_equilibria_linearization.svg)

An equilibrium point is where a system can remain forever if placed exactly there. But the deeper question is what happens near that point. Does nearby motion drift away, spiral inward, or do something subtler? Linearization answers this by replacing the nonlinear system with its best local linear model.

This lesson is a major conceptual bridge. It brings all the linear theory from the previous chapter back into play, but now only as a local approximation. The Jacobian matrix becomes the main tool for converting nonlinear geometry into a tractable local model.

## Concept in Three Ways

### Intuitive View

Near an equilibrium, a smooth nonlinear system often looks like its tangent approximation. Just as a curve looks nearly straight under enough magnification, a nonlinear vector field looks nearly linear near a steady state.

### Visual View

If we zoom in near an equilibrium, the curved arrows of the nonlinear field begin to resemble the arrows of a linear system. The Jacobian captures the local stretching, compression, and rotation.

### Formal View

For a system
$$ \dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}), $$
an equilibrium $$ \mathbf{x}_* $$ satisfies
$$ \mathbf{f}(\mathbf{x}_*)=\mathbf{0}. $$
Let
$$ \mathbf{u}=\mathbf{x}-\mathbf{x}_*. $$
Then near $$ \mathbf{x}_* $$,
$$
\dot{\mathbf{u}}\approx J(\mathbf{x}_*)\mathbf{u},
$$
where $$ J(\mathbf{x}_*) $$ is the Jacobian matrix of first partial derivatives evaluated at the equilibrium.

## Common Misconceptions

- "Linearization gives the exact system near equilibrium." Wrong. It gives the best first-order local approximation.
- "If the linearization is stable, the nonlinear system is globally stable." Wrong. The conclusion is local.
- "Every equilibrium can be classified reliably by linearization." Not always. Nonhyperbolic equilibria require extra care.
- "The Jacobian is just a computational trick." Wrong. It encodes the local geometry of the vector field.

## Suggested Learning Path

### Step 1: Find Equilibria

Solve the nonlinear algebraic system obtained by setting all derivatives equal to zero.

### Step 2: Compute the Jacobian

Students should treat this as the local derivative of the vector field.

### Step 3: Evaluate the Jacobian at Each Equilibrium

This gives the linear model governing nearby perturbations.

### Step 4: Classify the Linearized System

Use eigenvalues and phase-portrait ideas from the linear chapter.

### Checkpoints

- Can students compute a Jacobian accurately?
- Can students explain why the linearization is only local?
- Do students know when a nonhyperbolic equilibrium is a warning sign?

## Worked Examples

### Example 1: Damped Pendulum Near the Bottom

Consider
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega.
$$
At $$ \left(0,0\right) $$, the Jacobian is
$$
J(0,0)=
\begin{pmatrix}
0 & 1\\
-1 & -c
\end{pmatrix}.
$$
For positive damping, the eigenvalues have negative real part, so the bottom equilibrium is locally asymptotically stable.

### Example 2: A Simple Nonlinear System

Take
$$ \dot{x}=y-x^3,\qquad
\dot{y}=-x-y. $$
The equilibrium is $$ \left(0,0\right) $$. The Jacobian is
$$
J(0,0)=
\begin{pmatrix}
0 & 1\\
-1 & -1
\end{pmatrix}.
$$
The eigenvalues have negative real part, so the origin behaves like a local spiral sink.

### Example 3: A Warning Example

If the Jacobian at an equilibrium has an eigenvalue with zero real part, then the linear approximation may fail to determine the true nonlinear behavior. This is exactly why bifurcation theory becomes necessary later in the chapter.

## Conceptual Questions

1. Why is the Jacobian the correct object for local approximation?
2. What information does the linearized system preserve well?
3. Why must we be cautious when an equilibrium is nonhyperbolic?

## Application Problems

1. In engineering, why is local behavior near an operating point often more important than the full global system?
2. In chemistry, why might a steady operating concentration be analyzed through its Jacobian?
3. In mechanics, why does the pendulum behave differently near the bottom and near the top equilibrium?

## Interactive Teaching Strategies

- Ask students to compare a nonlinear vector field and its linearization visually near one equilibrium.
- Have small groups compute Jacobians for several examples and explain the geometry in words.
- Use a zoomed-in plot to show how a nonlinear field becomes nearly linear near equilibrium.
- Emphasize the phrase "local model" repeatedly to prevent overgeneralization.

## Differentiation

### Support for Struggling Students

Students who need more structure should use a routine: find equilibrium, compute Jacobian, substitute the equilibrium, then classify eigenvalues.

### Challenge for Advanced Students

Advanced students can investigate a nonhyperbolic example and see why linearization alone is inconclusive.

## Summary

Linearization is the local microscope of nonlinear dynamics. By replacing a nonlinear system with its Jacobian near equilibrium, we recover the power of linear theory while remembering that the result is only a local description.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Pendulum near equilibrium
- Problem: Near equilibrium we want a simpler model that predicts small oscillations accurately.
- Model:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega
$$
and near $$ \theta=0 $$:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}\approx -\theta-c\omega.
$$
- Assumptions and limitations: This approximation is reliable only for small angles.
- Interpretation: The Jacobian captures local behavior near equilibrium, not the entire nonlinear dynamics.

#### Chemical reaction near steady operation
- Problem: We want to know whether concentrations return to a nominal operating state after a small disturbance.
- Model:
$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}),\qquad
\dot{\mathbf{u}}=J(\mathbf{x}_*)\mathbf{u},
$$
where $$ \mathbf{u}=\mathbf{x}-\mathbf{x}_* $$.
- Assumptions and limitations: The linear model is only local in state space.
- Interpretation: The spectrum of the Jacobian is the nonlinear analogue of the eigenvalue analysis from Chapter 4.

### 2. Additional Intuition and Connections

Linearization is a local microscope. It tells us what the system looks like very close to equilibrium. A major pitfall is to use local conclusions globally. When the equilibrium is hyperbolic, linearization is often highly reliable; when it is nonhyperbolic, much more care is needed. This lesson is the main bridge from linear systems to nonlinear dynamics.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def nonlinear(t, z):
    x, y = z
    return [y, -np.sin(x) - 0.2 * y]

def linearized(t, z):
    x, y = z
    return [y, -x - 0.2 * y]

t = np.linspace(0, 20, 600)
z0 = [0.3, 0.0]
sol1 = solve_ivp(nonlinear, [0, 20], z0, t_eval=t)
sol2 = solve_ivp(linearized, [0, 20], z0, t_eval=t)

plt.plot(t, sol1.y[0], label="nonlinear")
plt.plot(t, sol2.y[0], "--", label="linearized")
plt.xlabel("t")
plt.ylabel("theta")
plt.title("Nonlinear system versus its linearization")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: linearization near equilibrium nonlinear system
- search: Jacobian local behavior phase plane
- search: pendulum linearization comparison

### 5. Worked Example

Consider
$$ \dot{x}=y-x^3,\qquad
\dot{y}=-x-y. $$
The equilibrium is $$ \left(0,0\right) $$. The Jacobian there is
$$
J(0,0)=
\begin{pmatrix}
0 & 1\\
-1 & -1
\end{pmatrix}.
$$
Its eigenvalues have negative real part, so the equilibrium is locally asymptotically stable. Near the origin, the nonlinear system behaves like a spiral sink.

### 6. Difficulty Layering

**Undergraduate level.** Compute Jacobians, locate equilibria, and classify local behavior through the linearized matrix.

**Graduate level.** Discuss the Hartman-Grobman theorem, hyperbolic equilibria, and failures of linearization at nonhyperbolic points.

![Equilibria and linearization]({{ site.imgurl }}/chapter_img/chapter05/05_02_equilibria_linearization.svg)

## References

- Strogatz, Chapter 6: clear treatment of linearization and local behavior.
- Arnold, Chapter 5: geometric insight into equilibria and local phase portraits.
