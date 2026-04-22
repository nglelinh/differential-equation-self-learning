---
layout: post
title: "04-04 Eigenvalue Method: Complex"
chapter: '04'
order: 4
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

## Learning Objectives

This lesson helps students handle linear systems when the matrix has complex conjugate eigenvalue pairs, convert complex solutions to real solutions, and read the phenomena of rotation, inward spirals, or outward spirals from the real and imaginary parts of eigenvalues.

## Prerequisites

Students need to grasp basic complex numbers, Euler's formula, and the real distinct eigenvalue case. This is where geometric intuition becomes especially strong, so connecting to harmonic oscillation from previous chapters is very helpful.

## Introduction

![Spiral trajectories when eigenvalues are complex conjugates]({{ site.imgurl }}/chapter_img/chapter04/04_eigenvalue_complex.svg)

In single-variable systems, complex solutions often signal oscillation. This continues to hold for linear systems, but now the geometric meaning is even clearer. When eigenvalues are complex, trajectories do not just grow or decay along a line, but rotate around the origin. If there is simultaneous contraction or expansion, trajectories become spirals.

This lesson is very rich in intuition. Just from the pair of numbers
$$ \alpha\pm i\beta, $$
we can immediately read three pieces of information: whether there is rotation, how fast the rotation, and whether amplitude contracts or expands. Not many places in mathematics do algebra and geometry speak so directly to each other.

## Concept in Three Ways

### Intuitive View

Think of the system as rotational motion in a plane. The imaginary part of the eigenvalue creates the rotational rhythm, while the real part is like each rotation simultaneously being contracted or expanded.

### Visual View

If
$$ \alpha<0, $$
trajectories spiral into the origin. If
$$ \alpha>0, $$
trajectories spiral outward. If
$$ \alpha=0, $$
trajectories only rotate around the origin without contracting or expanding, creating an ideal center in the linear model. The imaginary part $$ \beta $$ determines angular velocity.

### Formal View

Suppose $$ A $$ has eigenvalues
$$ \lambda=\alpha\pm i\beta,\qquad \beta\neq 0, $$
and complex eigenvector
$$ \mathbf{v}=\mathbf{a}+i\mathbf{b}. $$
One complex solution is
$$
\mathbf{x}(t)=e^{(\alpha+i\beta)t}(\mathbf{a}+i\mathbf{b}).
$$
Using Euler's formula, we can extract two independent real solutions:
$$
\mathbf{x}_1(t)=e^{\alpha t}\left(\mathbf{a}\cos \beta t-\mathbf{b}\sin \beta t\right),
$$
$$
\mathbf{x}_2(t)=e^{\alpha t}\left(\mathbf{a}\sin \beta t+\mathbf{b}\cos \beta t\right).
$$

## Common Misconceptions

- "Complex eigenvalues make solutions lose real meaning." Wrong. We can always extract two independent real solutions.
- "As long as there is an imaginary part, trajectories are always circles." Wrong. It also depends on whether the real part is zero.
- "If trajectories rotate then the system is definitely stable." Not true. It can rotate and simultaneously move away.
- "Real and imaginary parts of eigenvalues have the same role." Wrong. They encode two completely different behaviors.

## Suggested Learning Path

### Step 1: Find Complex Eigenvalues

Recognize the case of negative discriminant.

### Step 2: Find Complex Eigenvector

Work slowly and carefully with complex numbers.

### Step 3: Separate Real and Imaginary Parts

This is the step to return to the world of real solutions.

### Step 4: Interpret Geometrically

Ask immediately whether trajectories rotate, attract or repel.

### Checkpoints

- Can students correctly separate complex solutions into two real solutions?
- Can students explain the roles of $$ \alpha $$ and $$ \beta $$?
- Can students distinguish between centers, inward spirals, and outward spirals?

## Worked Examples

### Example 1: Pure Rotation

Consider
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix}.
$$
We have eigenvalues
$$ \lambda=\pm i. $$
Real solutions are combinations of sin-cos. Trajectories are circles around the origin. This is the first-order system model of undamped harmonic oscillation.

### Example 2: Inward Spiral

Consider
$$
A=
\begin{pmatrix}
-1 & -2\\
2 & -1
\end{pmatrix}.
$$
Eigenvalues are
$$ -1\pm 2i. $$
Since the real part is negative, trajectories rotate and simultaneously contract toward the origin. Thus the origin is a stable focus.

### Example 3: Outward Spiral

If we replace the previous matrix with
$$
A=
\begin{pmatrix}
1 & -2\\
2 & 1
\end{pmatrix},
$$
then eigenvalues are
$$ 1\pm 2i. $$
Trajectories still rotate with angular speed 2 but amplitude grows like $$ e^t $$. This is the typical model of an unstable spiral.

### Example 4: Reading Directly from Eigenvalue

From eigenvalue
$$ \lambda=-3\pm 4i, $$
we can immediately read: the system rotates, rotation speed is related to 4, and amplitude decreases like $$ e^{-3t} $$. Students should practice reflexively reading this meaning directly without solving completely.

## Conceptual Questions

1. Why are complex eigenvalues associated with rotational motion in the plane?
2. What dynamical roles do the real and imaginary parts of eigenvalues play?
3. Why can systems with the same imaginary part have circular rotation, inward spiral, or outward spiral?

## Application Problems

1. A control system has an oscillatory response that gradually damps out. Relate this to complex eigenvalues with negative real part.
2. A two-variable population model gives trajectories spiraling away from equilibrium. What does this suggest about stability?
3. An ideal electrical circuit oscillates harmonically without energy loss. Explain why the real part of eigenvalues must be zero.

## Interactive Teaching Strategies

- Have students guess trajectory shape just from eigenvalues before drawing.
- Organize matching exercises between eigenvalues and corresponding phase portraits.
- Ask the class to interpret in words the phrase
$$ \alpha\pm i\beta $$
as "rotating, attracting/repelling, fast/slow."
- Compare directly with harmonic oscillation from previous chapters to create a bridge.

## Differentiation

### Support for Struggling Students

Struggling students should rely on a short table: $$ \alpha<0 $$ is attracting, $$ \alpha>0 $$ is repelling, $$ \beta\neq 0 $$ is rotating. This simple schema helps them not drown in complex numbers.

### Challenge for Advanced Students

Advanced students can be asked to write solutions in the form of rotation combined with scaling, to see the structure
$$ e^{\alpha t}R_{\beta t} $$
hidden behind complex eigenvalue pairs.

## Summary

Complex eigenvalues do not make the system "lose reality," but make it start rotating. The imaginary part creates rotational oscillation, the real part creates contraction or expansion. To quickly read a 2D system, look at
$$ \alpha\pm i\beta $$
as encoding rotation plus contraction/expansion.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Rotation and spiraling in mechanics
- Problem: A system can rotate while simultaneously shrinking or expanding.
- Model:
$$ \lambda=\alpha\pm i\beta. $$
- Assumptions and limitations: Two-dimensional linear system.
- Interpretation: The imaginary part creates rotation and the real part creates contraction or expansion.

#### Damped oscillation in electronics
- Problem: Circuits or filters may spiral toward equilibrium rather than move straight toward it.
- Model:
$$
\mathbf{x}(t)=e^{\alpha t}\left(\mathbf{a}\cos \beta t+\mathbf{b}\sin \beta t\right).
$$
- Assumptions and limitations: Linear approximation near an operating point.
- Interpretation: Complex eigenvalues are the natural language of oscillatory state-space motion.

#### Rotational flow near equilibrium
- Problem: Two variables may circle around equilibrium instead of moving directly inward or outward.
- Model:
$$
\alpha<0 \Rightarrow \text{spiral sink},\qquad
\alpha>0 \Rightarrow \text{spiral source}.
$$
- Assumptions and limitations: Local linear model.
- Interpretation: The eigenvalues already tell the geometric story.

### 2. Conceptual Insight

If real eigenvalues represent stretching or shrinking along invariant lines, complex eigenvalues represent stretching or shrinking combined with rotation. This lesson is tightly connected to earlier work on damped oscillation: complex values are not artificial complications but an efficient encoding of real geometry.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 12, 800)
for alpha, label in [(-0.15, "Spiral sink"), (0.0, "Center"), (0.12, "Spiral source")]:
    x = np.exp(alpha * t) * np.cos(2 * t)
    y = np.exp(alpha * t) * np.sin(2 * t)
    plt.plot(x, y, label=label)

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("How the real part changes rotating trajectories")
plt.legend()
plt.axis("equal")
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: spiral sink spiral source phase portrait
- search: complex eigenvalues linear system visualization
- search: center vs spiral phase portrait animation

### 5. Worked Example

Let
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix}.
$$
The eigenvalues are
$$ \lambda=\pm i. $$
The real solutions represent pure rotation:
$$
\mathbf{x}(t)=
c_1
\begin{pmatrix}
\cos t\\
\sin t
\end{pmatrix}
+
c_2
\begin{pmatrix}
-\sin t\\
\cos t
\end{pmatrix}.
$$
Trajectories are circles around the origin, so the origin is a center in the linear model.

### 6. Difficulty Layering

**Undergraduate level.** Learn to extract real solutions from complex eigenpairs and interpret $$ \alpha,\beta $$.

**Graduate level.** Connect with normal forms for planar linear systems and the geometry of centers and spirals.

![Complex eigenvalues]({{ site.imgurl }}/chapter_img/chapter04/04_04_eigenvalue_complex.svg)

## References

- Boyce & DiPrima, Chapter 7: very clear on converting complex solutions to real solutions.
- Arnold, *Ordinary Differential Equations*: especially strong on geometric intuition of rotating trajectories.
