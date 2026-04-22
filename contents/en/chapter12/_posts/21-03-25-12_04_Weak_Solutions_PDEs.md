---
layout: post
title: "Weak Solutions of PDEs"
chapter: '12'
order: 4
owner: Lê Minh Hoàng
lang: en
categories:
- chapter12
lesson_type: required
---

![A weak PDE formulation through test functions and integration by parts]({{ site.imgurl }}/chapter_img/chapter12/04_weak_solutions_pdes.svg )

## Objectives

This lesson explains how a classical PDE is rewritten in weak form, why weak solutions are the right notion for many elliptic problems, and how weak formulations lead directly to existence theorems such as Lax-Milgram. After the lesson, students should be able to derive weak forms for standard model problems.

## Prerequisites

Students should know weak derivatives, the spaces $$ H^1 $$ and $$ H^1_0 $$, integration by parts, and the basic meaning of homogeneous Dirichlet boundary conditions. It is important to emphasize that weak form does not throw away the PDE. It rewrites the same balance law in a more stable framework.

## Introduction

A classical PDE usually requires the solution to be smooth enough for every derivative in the equation to make pointwise sense. But in practice, natural solutions may have only weak derivatives. If we insist on the classical standard, we exclude precisely the solutions we most want to study.

Weak solutions solve this problem by multiplying the PDE by a test function and integrating by parts so that derivatives fall on the test function instead of on the unknown. The resulting equation is weaker in smoothness requirements but still preserves the balance or conservation content of the model.

## The Concept in Three Ways

### Intuitive View

Think of a stretched membrane fixed along its boundary. Even if the shape is not perfectly smooth at every point, it can still be in equilibrium. A weak solution describes that equilibrium through a global balance principle rather than through pointwise second derivatives.

### Visual View

On the board, it is very effective to draw two columns:

- on the left, the classical PDE such as $$ -\Delta u=f $$,
- on the right, the integral identity involving a test function $$ \varphi $$.

The arrow between them is integration by parts. Students can literally watch the derivative move from the unknown solution onto the test function.

### Formal View

Consider the Poisson problem

$$
\begin{cases}
-\Delta u=f & \text{in } \Omega,\\
u=0 & \text{on } \partial\Omega.
\end{cases}
$$

We say that $$ u\in H^1_0(\Omega) $$ is a weak solution if

$$
\int_\Omega \nabla u\cdot \nabla \varphi\,dx=\int_\Omega f\varphi\,dx
\qquad \forall \varphi\in H^1_0(\Omega).
$$

If $$ u $$ is smooth enough, this identity is obtained from the classical PDE by multiplying by $$ \varphi $$ and integrating by parts.

## Common Misconceptions

### "A weak solution is only an approximate solution"

False. It is an exact solution concept in a larger function space.

### "Weak form loses the boundary condition"

No. The boundary condition is encoded in the choice of trial and test space, such as $$ H^1_0(\Omega) $$ for homogeneous Dirichlet data.

### "Replacing a PDE by an integral identity is automatic"

Not quite. One must choose the correct solution space and test space so that every term is meaningful.

### "If a weak solution exists, then a classical solution automatically exists"

False. Extra regularity assumptions are needed to upgrade a weak solution to a more classical one.

## Learning Progression

### Step 1: Start from a model boundary-value problem

Poisson's equation is the standard first example because the integration-by-parts step is clear.

### Step 2: Multiply by a test function

Students should see that the test function is not arbitrary decoration. It is the probe that captures the PDE in averaged form.

### Step 3: Integrate by parts

This step lowers the derivative order on the unknown solution and reveals the natural energy space.

### Step 4: Identify the correct function space

The weak form only works if the solution and test functions live in a space where all terms make sense.

### Key Checkpoints

- Can students derive the weak form of Poisson's equation?
- Can they explain why $$ H^1_0(\Omega) $$ is the correct space for homogeneous Dirichlet data?
- Can they distinguish weak solutions from approximate or numerical ones?

## Worked Examples

### Example 1: Deriving the weak form of Poisson's equation

Start from $$ -\Delta u=f $$ with $$ u=0 $$ on the boundary. Multiply by a test function $$ \varphi\in C_c^\infty(\Omega) $$ or later $$ H^1_0(\Omega) $$ and integrate:

$$
\int_\Omega (-\Delta u)\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

Integration by parts gives

$$
\int_\Omega \nabla u\cdot \nabla \varphi\,dx=\int_\Omega f\varphi\,dx.
$$

That is the weak form.

### Example 2: A one-dimensional boundary-value problem

Consider

$$
\begin{cases}
-u''=f & \text{on } (0,1),\\
u(0)=u(1)=0.
\end{cases}
$$

The weak form is

$$
\int_0^1 u'(x)\varphi'(x)\,dx=\int_0^1 f(x)\varphi(x)\,dx
\qquad \forall \varphi\in H^1_0(0,1).
$$

This is the one-dimensional model that students should master first.

### Example 3: Every classical solution is a weak solution

If $$ u\in C^2(\Omega)\cap C^0(\overline{\Omega}) $$ solves the Poisson problem classically and vanishes on the boundary, then the integration-by-parts argument shows that $$ u $$ satisfies the weak formulation. So the weak notion truly extends the classical one.

### Example 4: Why the test space matters

Suppose we try to use arbitrary test functions in $$ L^2(\Omega) $$. Then the term

$$ \int_\Omega \nabla u\cdot \nabla \varphi\,dx $$

is not even defined unless $$ \varphi $$ has a weak gradient. This is why the choice of $$ H^1_0(\Omega) $$ is not cosmetic but essential.

## Conceptual Questions

1. Why is weak formulation a reformulation of the PDE rather than a simplification of it?
2. Why does integration by parts lower the smoothness requirement on the solution?
3. Why does the function space itself encode part of the boundary condition?

## Application Problems

1. In elasticity or membrane theory, why is an energy balance more natural than pointwise second derivatives?
2. In finite element methods, why is the weak form the natural starting point for discretization?
3. Why do rough coefficients or rough data often force us to work with weak solutions instead of classical ones?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What changes when we move derivatives onto the test function?
- Why is the test function not just a trick but part of the structure?
- What information about the boundary condition is hidden in the space $$ H^1_0(\Omega) $$?

### Suggested Activities

- Have students derive the weak form of a simple one-dimensional boundary problem in pairs.
- Put the classical equation and the weak form side by side and ask students to identify corresponding pieces.
- Ask small groups to decide which function space is appropriate for different boundary conditions.

### Participation Moves

- Start from the question "What goes wrong if the solution is not twice differentiable?"
- Ask students to narrate the integration-by-parts step in words.
- Encourage them to explain weak form first physically, then mathematically.

## Differentiation

### Support for Struggling Students

- Work first in one dimension.
- Use Poisson's equation as the main model before moving to general operators.
- Emphasize the logic: multiply, integrate, move derivatives, choose the right space.

### Challenge for Advanced Students

- Derive weak formulations for Neumann or mixed boundary conditions.
- Connect weak solutions to minimizers of an energy functional.
- Explore when a weak solution becomes a classical one through regularity theory.

## Quick Summary

A weak solution is an exact solution concept built from integration against test functions. It lowers the smoothness requirements on the unknown while preserving the essential content of the PDE and opening the door to existence theorems and numerical methods.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Poisson problems with rough forcing
- Problem: Real heat sources, loads, or charge densities often lie only in $$ L^2 $$ and are not smooth.
- Model: Instead of solving $$ -\Delta u=f $$ classically, we seek $$ u $$ such that
$$
\int_\Omega \nabla u \cdot \nabla v\,dx = \int_\Omega f v\,dx
$$
for every test function $$ v $$.
- Assumptions and limitations: The data and domain must make the integrals meaningful.
- Interpretation: Weak solutions exist in settings where classical pointwise derivatives are too much to ask.

#### Membrane deflection and elasticity
- Problem: The displacement of a loaded membrane is often best described through energy rather than classical differentiability.
- Model: The weak formulation arises from minimizing the total elastic energy.
- Assumptions and limitations: Linear model and suitable boundary conditions.
- Interpretation: "Weak" does not mean inferior; it means adapted to the physical energy class.

### 2. Additional Intuition and Connections

Weak solutions arise when derivatives are transferred from the unknown to the test function by integration by parts. The reward is a much broader class of admissible solutions. A common misconception is that weak solutions are merely numerical approximations; in modern PDE theory they are often the primary notion of solution.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
u = 0.5 * x * (1 - x)
f = np.ones_like(x)

plt.plot(x, u, label="weak / classical solution")
plt.plot(x, f, label="source f=1")
plt.legend()
plt.title("The problem -u''=1 on (0,1) with Dirichlet boundary data")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: weak solution Poisson equation finite element intuition
- search: variational formulation membrane deflection
- search: integration by parts weak form PDE

### 5. Worked Example

Solve
$$
-u''=1 \quad \text{on } (0,1), \qquad u(0)=u(1)=0.
$$
The weak form is: find $$ u \in H_0^1(0,1) $$ such that
$$ \int_0^1 u'v'\,dx = \int_0^1 v\,dx $$
for every $$ v \in H_0^1(0,1) $$. The function
$$ u(x)=\frac{x(1-x)}{2} $$
satisfies this identity, so it is the weak solution.

### 6. Difficulty Layering

**Undergraduate level.** Learn how integration by parts generates the weak form.

**Graduate level.** Connect to Galerkin methods, compactness, and existence for nonlinear PDEs.
