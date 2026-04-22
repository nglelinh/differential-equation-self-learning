---
layout: post
title: "04-02 Matrices and Linear Systems"
chapter: '04'
order: 2
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

## Learning Objectives

This lesson helps students write linear systems in matrix form, understand why matrices are a dynamical summary of the system, and grasp the concept of fundamental matrix solution as the system version of general solution. This is the gateway to bringing linear algebra systematically into solving ODEs.

## Prerequisites

Students need to grasp vectors, matrices, matrix-vector multiplication, and the idea of linear independence. Understanding linear ODEs in one variable also helps students recognize how the superposition principle extends to systems.

## Introduction

![Matrix governing evolution of linear system]({{ site.imgurl }}/chapter_img/chapter04/02_matrices_linear_systems.svg)

When we write a system of many equations as a single matrix expression, what we gain is not just tidiness. We gain a structural map of interactions. Each row of the matrix tells how the rate of change of one state variable depends on the entire state, while each column tells how one state component influences the whole system.

This is a very important cognitive step. Previously, students may have viewed a system as a list of equations placed side by side. After this lesson, the system should be seen as a single linear entity with an evolution operator, the matrix $$ A $$.

## Concept in Three Ways

### Intuitive View

The matrix $$ A $$ is like the "law of interaction" for the system. It tells you that if you are at current state $$ \mathbf{x} $$, the system is pulled in certain directions, with certain strengths.

### Visual View

In a two-dimensional system
$$ \mathbf{x}'=A\mathbf{x}, $$
the matrix $$ A $$ assigns to each point $$ \mathbf{x} $$ a tangent vector $$ A\mathbf{x} $$. Thus, the matrix generates a vector field on the state plane. This is the first bridge from linear algebra to phase geometry.

### Formal View

A homogeneous linear system with constant coefficients is written
$$ \mathbf{x}'=A\mathbf{x}, $$
where $$ A $$ is a constant $$ n\times n $$ matrix. If there is external forcing, we write
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
If $$ \mathbf{x}_1,\ldots,\mathbf{x}_n $$ are linearly independent vector solutions of the homogeneous system, then the matrix
$$
\Phi(t)=
\begin{pmatrix}
\lvert  & & \rvert\\
\mathbf{x}_1(t) & \cdots & \mathbf{x}_n(t)\\
\lvert  & & \rvert
\end{pmatrix}
$$
is called the fundamental matrix solution, and every solution of the system has the form
$$ \mathbf{x}(t)=\Phi(t)\mathbf{c}. $$

## Common Misconceptions

- "Matrices are just shorthand notation." Wrong. They encode the interaction structure of the system.
- "Each column of the fundamental matrix is just a random solution." Wrong. The columns must be linearly independent to span the entire solution space.
- "If we can solve each component equation, we don't need matrices." Often not true, since equations are tightly coupled.
- "Matrix $$ A $$ only affects speed, not geometry." Wrong. It is $$ A $$ that determines the vector field and phase portrait.

## Suggested Learning Path

### Step 1: Write System in Vector-Matrix Form

Move from list of equations to a single expression.

### Step 2: Read Meaning of Each Row and Column

Make the matrix less abstract.

### Step 3: Understand Superposition Principle for Systems

Linear combinations of solutions are still solutions.

### Step 4: Build Fundamental Matrix Solution

This concept will return many times in the chapter.

### Checkpoints

- Can students correctly write the system as $$ \mathbf{x}'=A\mathbf{x} $$?
- Do students understand why we need $$ n $$ independent solutions for an $$ n $$-dimensional system?
- Can students interpret $$ A\mathbf{x} $$ as a state velocity vector?

## Worked Examples

### Example 1: Writing System in Matrix Form

Consider
$$
\begin{cases}
x_1'=2x_1-x_2,\\
x_2'=3x_1+4x_2.
\end{cases}
$$
Set
$$
\mathbf{x}=
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
2 & -1\\
3 & 4
\end{pmatrix}.
$$
Then the system is written concisely as
$$ \mathbf{x}'=A\mathbf{x}. $$
The pedagogical point here is students immediately see the matrix collects the entire system into a single multiplication.

### Example 2: Diagonal System

With
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix},
$$
the system becomes
$$
\begin{cases}
x_1'=2x_1,\\
x_2'=-x_2.
\end{cases}
$$
We solve to get
$$ x_1=c_1e^{2t},\qquad x_2=c_2e^{-t}. $$
Thus
$$
\mathbf{x}(t)=
c_1e^{2t}
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^{-t}
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
This example shows the coordinate axes play the role of two independent dynamical directions.

### Example 3: Fundamental Matrix Solution

From the previous example, we can choose two independent solutions:
$$
\mathbf{x}_1(t)=e^{2t}
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\mathbf{x}_2(t)=e^{-t}
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
The fundamental matrix solution is
$$
\Phi(t)=
\begin{pmatrix}
e^{2t} & 0\\
0 & e^{-t}
\end{pmatrix}.
$$
Every solution is written as
$$ \mathbf{x}(t)=\Phi(t)\mathbf{c}. $$
This is the system version of the familiar "general solution" from single-variable ODEs.

### Example 4: Reading Rows and Columns of the Matrix

If in a system, the element $$ a_{21} $$ is large and positive, this says the first variable strongly acts in the positive direction on the rate of change of the second variable. This reading helps the matrix become a meaningful object, not just a table of numbers.

## Conceptual Questions

1. Why is writing a system in matrix form not just saving notation?
2. What meanings can each row and each column of matrix $$ A $$ be read as?
3. Why is the fundamental matrix solution a central concept for linear systems?

## Application Problems

1. In a two-sector economic model, one variable represents output and the other represents demand. Explain why matrices are the appropriate language to encode interaction.
2. In biology, two populations interact. Interpret the meaning of off-diagonal coefficients in the matrix.
3. In mechanics with multiple degrees of freedom, why does collecting the system into a matrix pave the way for eigenvalue analysis?

## Interactive Teaching Strategies

- Have students convert back and forth between component form and matrix form.
- Ask the class to describe in words the meaning of each coefficient in a small matrix.
- Have students build a fundamental matrix from two known solutions to see this concept is not foreign.
- Use different colors for the columns of $$ \Phi(t) $$ to emphasize they are basis solutions.

## Differentiation

### Support for Struggling Students

Struggling students should work with 2-dimensional systems first, where everything is still visible both geometrically and algebraically. Emphasize very clearly that a vector solution is a function of time, not a fixed vector.

### Challenge for Advanced Students

Advanced students can be asked to prove directly that if $$ \Phi(t) $$ is a fundamental matrix solution, then every solution has the form $$ \Phi(t)\mathbf{c} $$, or analyze the relationship between the determinant of $$ \Phi(t) $$ and linear independence.

## Summary

Linear systems are written as
$$ \mathbf{x}'=A\mathbf{x} $$
to reveal the dynamical operator of the system. Matrix $$ A $$ generates a vector field, while the fundamental matrix solution $$ \Phi(t) $$ generates the entire solution space. Understanding these two objects gives students the algebraic framework for the entire chapter.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Local species interaction
- Problem: Near equilibrium, two biological populations may influence one another through a linearized model.
- Model:
$$ \mathbf{x}'=A\mathbf{x}. $$
- Assumptions and limitations: The model is only locally valid near equilibrium.
- Interpretation: The matrix $$ A $$ is a compact interaction map.

#### Multi-node electrical networks
- Problem: Voltages or currents at several components evolve simultaneously and depend on each other.
- Model:
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
- Assumptions and limitations: Linear time-invariant approximation.
- Interpretation: Matrix form reveals the network structure immediately.

#### Capital-inventory feedback
- Problem: One economic variable changes the rate of change of another.
- Model:
$$
\begin{pmatrix}
x_1'\\
x_2'
\end{pmatrix}
=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix}.
$$
- Assumptions and limitations: Local linear approximation.
- Interpretation: Rows and columns reveal who influences whom.

### 2. Conceptual Insight

Writing a system in matrix form is not just notational compression. It changes how we think: $$ A $$ becomes both an interaction law and a generator of the vector field. This lesson is the real bridge from scalar ODE thinking into linear algebraic dynamics.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, -1],
              [3,  4]])
x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
X, Y = np.meshgrid(x, y)
U = 2*X - Y
V = 3*X + 4*Y
N = np.sqrt(U**2 + V**2)

plt.quiver(X, Y, U / N, V / N, color="teal")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Vector field of x' = Ax")
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: vector field matrix differential equation
- search: fundamental matrix intuition
- search: linear system state velocity visualization

### 5. Worked Example

Given
$$
\begin{cases}
x_1'=2x_1-x_2,\\
x_2'=3x_1+4x_2,
\end{cases}
$$
we write
$$
\mathbf{x}'=
\begin{pmatrix}
2 & -1\\
3 & 4
\end{pmatrix}\mathbf{x}.
$$
In this form we can read:
- the first row governs the rate of $$ x_1 $$,
- the second row governs the rate of $$ x_2 $$,
- the matrix as a whole generates the state-space vector field.

### 6. Difficulty Layering

**Undergraduate level.** Become fluent in the passage from a list of equations to $$ \mathbf{x}'=A\mathbf{x} $$.

**Graduate level.** Emphasize fundamental matrices, solution spaces, and linear flow maps.

![Matrices and linear systems]({{ site.imgurl }}/chapter_img/chapter04/04_02_matrices_linear_systems.svg)

## References

- Boyce & DiPrima, Chapter 7: clear presentation of matrix form and fundamental matrix solution.
- Arnold, *Ordinary Differential Equations*: good for geometric intuition of operator $$ A $$.
