---
layout: post
title: "04-07 Phase Portraits for Linear Systems"
chapter: '04'
order: 7
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

## Learning Objectives

This lesson helps students sketch and interpret phase portraits for planar linear systems, classify equilibrium points using eigenvalues or the trace-determinant test, and understand why phase geometry gives strong qualitative information even when explicit formulas are not written out.

## Prerequisites

Students should know the solution forms for planar systems with real distinct, complex, and repeated eigenvalues. Some prior intuition about vector fields and trajectories from autonomous first-order equations is also helpful.

## Introduction

![Phase portrait of a two-dimensional linear system]({{ site.imgurl }}/chapter_img/chapter04/07_phase_portraits.svg)

An explicit solution formula can be exact without being visually informative. A phase portrait reverses that emphasis. It compresses algebra and enlarges geometry. We immediately see whether trajectories spiral, approach the origin, move away, or align with preferred directions.

This is where qualitative analysis becomes central. From a matrix
$$ A, $$
we can often predict whether the equilibrium at the origin is a saddle, stable node, unstable node, center, or spiral. That matters well beyond linear algebra, because in more complicated models phase geometry often gives the first reliable picture of system behavior.

## Concept in Three Ways

### Intuitive View

A phase portrait is like a wind map for the system. At each point in state space, the system has a preferred direction of motion. A trajectory is the path followed when a state is released into that directional field.

### Visual View

The portrait is drawn in the state plane, not on the $$ \left(t,x\right) $$ graph. Each point is a possible state. Arrows indicate local velocity, and curves show how those velocities stitch together into global motion. Invariant lines and spirals become visible immediately.

### Formal View

For
$$ \mathbf{x}'=A\mathbf{x}, $$
the equilibrium point $$ \mathbf{x}=\mathbf{0} $$ is classified by the eigenvalues of $$ A $$. In two dimensions, if
$$
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
$$
then the trace and determinant are
$$ \tau=a+d,
\qquad
\Delta=ad-bc. $$
The characteristic equation is
$$ \lambda^2-\tau\lambda+\Delta=0. $$
From the signs and discriminant $$ \tau^2-4\Delta $$, we classify the origin.

## Common Misconceptions

- "A phase portrait is just a sketch of solution graphs over time." Wrong. It lives in state space, not on the time axis.
- "If eigenvalues are complex, the system always rotates forever." Wrong. The real part decides whether spirals grow, decay, or remain neutral.
- "A stable equilibrium means every nearby trajectory reaches it in finite time." Wrong. Stability describes long-term tendency, often asymptotic.
- "The trace-determinant plane is a separate trick from eigenvalues." Wrong. It is simply a compact way to encode the same eigenvalue information for planar systems.

## Suggested Learning Path

### Step 1: Draw the Vector Field

Students should connect the matrix to directional arrows in the plane before worrying about exact formulas.

### Step 2: Identify Eigenvalue Type

Real distinct, repeated, or complex eigenvalues already suggest the broad geometry.

### Step 3: Use Trace and Determinant

For planar systems, this often gives the fastest route to classification.

### Step 4: Relate Algebra to Geometry

Students should explicitly say what each eigenvalue pattern means in the portrait.

### Checkpoints

- Can students tell the difference between a node, saddle, center, and spiral?
- Can students explain why the sign of the real part controls attraction or repulsion?
- Can students use trace and determinant consistently for a $$ 2\times 2 $$ system?

## Worked Examples

### Example 1: Stable Node

Consider
$$
A=
\begin{pmatrix}
-2 & 0\\
0 & -1
\end{pmatrix}.
$$
The eigenvalues are $$ -2 $$ and $$ -1 $$, both negative and real. Every trajectory moves toward the origin, though generally not at the same speed in each direction. The phase portrait is a stable node.

### Example 2: Saddle Point

Let
$$
A=
\begin{pmatrix}
1 & 0\\
0 & -2
\end{pmatrix}.
$$
One eigenvalue is positive and one is negative. Along one eigendirection the system is pushed away from the origin, while along the other it is pulled in. This mixed behavior creates a saddle, one of the most important structures in dynamical systems.

### Example 3: Spiral Sink

Take
$$
A=
\begin{pmatrix}
0 & -1\\
1 & -1
\end{pmatrix}.
$$
The trace is $$ -1 $$ and the determinant is $$ 1 $$. The characteristic equation is
$$ \lambda^2+\lambda+1=0, $$
so the eigenvalues are complex with negative real part. Trajectories spiral inward. This is a spiral sink.

### Example 4: Center

For
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix},
$$
the eigenvalues are purely imaginary, $$ \pm i $$. Trajectories neither decay nor grow. In the ideal linear setting they move on closed curves around the origin, producing a center.

## Conceptual Questions

1. Why can a phase portrait be more informative than an explicit formula when first trying to understand a system?
2. Why does a positive determinant not by itself guarantee stability?
3. What geometric role do eigenvectors play when the eigenvalues are real?

## Application Problems

1. In a control system, why is distinguishing a stable node from a saddle important for safety?
2. In a mechanical model, what physical meaning might a spiral sink have?
3. Why does the trace-determinant picture become especially useful when comparing families of planar systems depending on parameters?

## Interactive Teaching Strategies

- Have students classify several matrices before they solve for any explicit trajectories.
- Overlay trajectories on a direction field so the local-to-global connection becomes visible.
- Use paired examples with the same determinant but different traces to show how classification changes.
- Ask the class to describe a portrait in words before naming its algebraic type.

## Differentiation

### Support for Struggling Students

Students who feel overwhelmed should begin by sorting systems into three broad groups: both eigenvalues negative, opposite signs, or complex pair. That coarse structure already explains much of the portrait.

### Challenge for Advanced Students

Advanced students can study the trace-determinant plane as a parameter map, including the curves separating repeated, complex, and saddle behavior, and connect those boundaries to bifurcation thinking.

## Summary

Phase portraits turn linear systems into geometry. By reading trajectories in state space, students learn to classify equilibria, anticipate long-term behavior, and connect matrix information directly to motion.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Linearization near equilibrium
- Problem: Near an equilibrium, we may only need to know whether trajectories saddle, spiral, or converge.
- Model:
$$ \mathbf{x}'=A\mathbf{x}. $$
- Assumptions and limitations: If the model comes from a nonlinear system, the interpretation is local.
- Interpretation: The phase portrait gives powerful qualitative information without explicit formulas.

#### Stability screening in control
- Problem: Engineers need to know quickly whether the origin is attracting or repelling.
- Model:
$$ \tau=\operatorname{tr}(A),\qquad \Delta=\det(A). $$
- Assumptions and limitations: Planar linear system.
- Interpretation: The signs of $$ \Delta $$ and $$ \tau^2-4\Delta $$ already classify the equilibrium type.

#### Rotational or nodal chemistry/biology models
- Problem: Two variables may move toward equilibrium by spiraling, sliding, or approaching directly.
- Model: The phase portrait of a two-dimensional linear system.
- Assumptions and limitations: Local linear behavior only.
- Interpretation: This is the geometric language of stability.

### 2. Conceptual Insight

Phase portraits are where geometry truly takes over. They compress eigenvalues, eigenvectors, and vector-field structure into one global picture. This lesson also prepares students for nonlinear systems later, where formulas may be unavailable but qualitative dynamics still matter.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2],
              [-3, -4]], dtype=float)
x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
X, Y = np.meshgrid(x, y)
U = A[0,0] * X + A[0,1] * Y
V = A[1,0] * X + A[1,1] * Y
N = np.sqrt(U**2 + V**2)

plt.quiver(X, Y, U / N, V / N, color="darkgreen")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Linear phase portrait generated by matrix A")
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: trace determinant plane interactive
- search: linear system phase portrait applet
- search: saddle node spiral source sink visualization

### 5. Worked Example

Let
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix}.
$$
Then
$$ \Delta=-2<0. $$
A negative determinant means the origin is a saddle. The first axis is repelling and the second is attracting. Even without solving explicitly, we know the equilibrium is strongly unstable.

### 6. Difficulty Layering

**Undergraduate level.** Classify equilibrium types correctly using eigenvalues or trace-determinant data.

**Graduate level.** Connect this with linearization of nonlinear systems and local dynamical interpretation.

![Phase portraits classification]({{ site.imgurl }}/chapter_img/chapter04/04_07_phase_portraits.svg)

## References

- Boyce & DiPrima, Chapter 7: good discussion of planar linear systems and phase portraits.
- Strogatz, *Nonlinear Dynamics and Chaos*: especially strong for visual and qualitative interpretation.
- Hirsch, Smale, and Devaney: for a more geometric perspective on planar flows.
