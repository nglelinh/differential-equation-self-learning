---
layout: post
title: "05-03 Stability Classification"
chapter: '05'
order: 3
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

## Learning Objectives

This lesson helps students classify equilibria by stability type, connect eigenvalues of the Jacobian to geometric motion, and distinguish nodes, saddles, spirals, and centers in a nonlinear setting.

## Prerequisites

Students should know equilibria, Jacobians, and the classification of linear planar systems. Some familiarity with the trace-determinant plane is also useful.

## Introduction

![Stability classification from the spectrum of the Jacobian]({{ site.imgurl }}/chapter_img/chapter05/03_stability_classification.svg)

Finding an equilibrium is only the beginning. The real dynamical question is whether nearby states are attracted, repelled, or mixed in their behavior. Stability classification gives a language for this local geometry.

The central idea is that the local behavior of a smooth nonlinear system is often inherited from the linearized system. If the Jacobian has a saddle structure, the nonlinear system also behaves like a saddle nearby. If the Jacobian has eigenvalues with negative real part, nearby trajectories are pulled toward the equilibrium. This makes classification one of the most practical diagnostic tools in nonlinear dynamics.

## Concept in Three Ways

### Intuitive View

Stability asks what happens after a small disturbance. If the system returns, the equilibrium is attracting. If it drifts away, the equilibrium is unstable. If some directions return and others escape, the equilibrium is a saddle.

### Visual View

A stable node pulls trajectories straight inward, a saddle attracts in one direction and repels in another, a spiral rotates while attracting or repelling, and a center produces closed nearby motion in the ideal linear case.

### Formal View

For a planar nonlinear system, classify an equilibrium by the eigenvalues of the Jacobian
$$ J(x_*,y_*). $$
If both eigenvalues have negative real part, the equilibrium is locally asymptotically stable. If one eigenvalue is positive and one negative, it is a saddle and therefore unstable. Complex eigenvalues with nonzero real part produce spirals. Zero real part requires additional analysis.

## Common Misconceptions

- "Stable means the trajectory reaches equilibrium instantly." Wrong. Stability concerns nearby motion over time, usually asymptotically.
- "A center in the linearized system guarantees nonlinear neutral stability." Not always.
- "A saddle is unstable only because both directions move outward." Wrong. A saddle is unstable because at least one direction moves outward.
- "Classification is purely algebraic." Wrong. The value lies in the geometry it predicts.

## Suggested Learning Path

### Step 1: Compute the Jacobian at the Equilibrium

This is the local matrix that controls the first-order behavior.

### Step 2: Find Eigenvalues

Their real and imaginary parts determine attraction, repulsion, and rotation.

### Step 3: Translate Algebra into Geometry

Students should explicitly state what the eigenvalues mean in the phase plane.

### Step 4: Interpret Stability

The classification should always be explained in terms of nearby trajectories.

### Checkpoints

- Can students identify a saddle immediately from opposite-sign eigenvalues?
- Can students explain why negative real parts imply attraction?
- Do students know that nonhyperbolic cases are exceptional and need more tools?

## Worked Examples

### Example 1: Stable Node

Suppose the Jacobian at an equilibrium is
$$
J=
\begin{pmatrix}
-2 & 0\\
0 & -1
\end{pmatrix}.
$$
Both eigenvalues are negative, so the equilibrium is a stable node. Nearby states move inward without oscillation.

### Example 2: Saddle

If
$$
J=
\begin{pmatrix}
1 & 0\\
0 & -2
\end{pmatrix},
$$
one direction grows and the other decays. The equilibrium is a saddle and is unstable.

### Example 3: Spiral Sink

For
$$
J=
\begin{pmatrix}
0 & -1\\
1 & -1
\end{pmatrix},
$$
the eigenvalues are complex with negative real part. Nearby trajectories spiral inward, so the equilibrium is a spiral sink.

## Conceptual Questions

1. Why is a saddle always unstable?
2. What information is carried by the real part of an eigenvalue?
3. Why should we be careful when the linearization produces purely imaginary eigenvalues?

## Application Problems

1. In a feedback system, why is a saddle operating point dangerous?
2. In a biochemical network, what might a spiral sink mean physically?
3. In mechanics, how can classification near equilibrium guide design or control decisions?

## Interactive Teaching Strategies

- Present several Jacobians and ask students to classify them before drawing any portrait.
- Use quick sketches to reinforce the correspondence between eigenvalues and geometry.
- Compare two systems that both rotate, but one attracts and one repels.
- Ask students to explain a classification in words instead of only naming it.

## Differentiation

### Support for Struggling Students

Students who need support can begin with a simple decision tree: opposite signs means saddle, both negative means stable, both positive means unstable, complex with nonzero real part means spiral.

### Challenge for Advanced Students

Advanced students can analyze how the trace-determinant plane organizes these classifications and where repeated or nonhyperbolic cases lie.

## Summary

Stability classification turns local linear algebra into phase-plane geometry. By reading the Jacobian spectrum, students can predict whether nearby trajectories are attracted, repelled, or split between the two.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Stability of aircraft trim
- Problem: After a small disturbance, does an aircraft return to its trim configuration or diverge away?
- Model:
$$ \dot{\mathbf{u}}=J\mathbf{u}. $$
- Assumptions and limitations: The analysis is local and does not include actuator saturation or strong nonlinear maneuvers.
- Interpretation: Nodes, saddles, and spirals correspond to qualitatively different recovery or divergence behaviors.

#### Chemical reactor operation
- Problem: Is an operating point robust to small temperature and concentration perturbations?
- Model:
$$ \dot{x}=f(x,y),\qquad
\dot{y}=g(x,y), $$
classified through the Jacobian at equilibrium.
- Assumptions and limitations: The model is valid only near the operating state.
- Interpretation: A saddle is a strong warning sign because some disturbances decay while others amplify.

### 2. Additional Intuition and Connections

Stability classification is the geometric language of Jacobian spectra. Negative real part pulls trajectories in, positive real part pushes them out, and imaginary parts create rotation. A common pitfall is to assume that a center in the linearized system automatically implies nonlinear neutral stability. This lesson reuses Chapter 4 ideas, but now through the Jacobian of a nonlinear system.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

cases = {
    "stable node": np.array([[-2, 0], [0, -1]]),
    "saddle": np.array([[1, 0], [0, -2]]),
    "spiral sink": np.array([[0, -1], [1, -1]])
}

x = np.linspace(-2, 2, 16)
y = np.linspace(-2, 2, 16)
X, Y = np.meshgrid(x, y)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, (name, A) in zip(axes, cases.items()):
    U = A[0, 0] * X + A[0, 1] * Y
    V = A[1, 0] * X + A[1, 1] * Y
    N = np.sqrt(U**2 + V**2) + 1e-9
    ax.quiver(X, Y, U / N, V / N)
    ax.set_title(name)
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: stability classification phase portrait node saddle spiral
- search: trace determinant plane visualization
- search: nonlinear equilibrium classification Jacobian

### 5. Worked Example

For
$$
J=
\begin{pmatrix}
0 & 1\\
-2 & -3
\end{pmatrix},
$$
the characteristic equation is
$$ \lambda^2+3\lambda+2=0, $$
so the eigenvalues are $$ -1 $$ and $$ -2 $$. Since both are negative, the equilibrium is a stable node. In an engineering setting this means small disturbances decay without sustained oscillation.

### 6. Difficulty Layering

**Undergraduate level.** Classify equilibria using eigenvalues, trace, and determinant.

**Graduate level.** Connect classification to stable manifolds, unstable manifolds, and structural stability of hyperbolic points.

![Stability classification]({{ site.imgurl }}/chapter_img/chapter05/05_03_stability_classification.svg)

## References

- Strogatz, Chapters 5-6: concise and geometric explanation of local stability types.
- Arnold, Chapter 4: useful geometric interpretation of saddles, nodes, and spirals.
