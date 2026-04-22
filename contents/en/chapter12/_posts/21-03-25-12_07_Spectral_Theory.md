---
layout: post
title: "Spectral Theory"
chapter: '12'
order: 7
owner: Lê Minh Hoàng
lang: en
categories:
- chapter12
lesson_type: optional
---

![The spectrum of an elliptic operator and its basic eigenmodes]({{ site.imgurl }}/chapter_img/chapter12/07_spectral_theory.svg )

## Objectives

This lesson introduces spectral theory as a way of understanding differential operators through their eigenmodes. After the lesson, students should understand eigenvalues, eigenfunctions, orthogonality, and why self-adjoint operators on Hilbert spaces play a role similar to symmetric matrices in finite dimensions. This lesson is optional, but it forms a major bridge between functional analysis, Fourier methods, and PDE.

## Prerequisites

Students should know Hilbert spaces, inner products, orthogonality, Sturm-Liouville problems, and Fourier series. Earlier chapters on eigenvalues of differential equations are especially helpful.

## Introduction

When a vibrating or diffusing system is decomposed into basic modes, each mode becomes much easier to understand. Spectral theory is the language that organizes this process. Instead of treating an operator as a black box, we try to decompose it into preferred directions on which the operator acts by simple scalar multiplication.

## The Concept in Three Ways

### Intuitive View

A guitar string does not vibrate in an arbitrary shape. It vibrates in natural modes, and each mode has its own frequency. Differential operators in PDE behave similarly: they have preferred shapes, called eigenfunctions, and each such shape comes with an eigenvalue describing the response of the operator.

### Visual View

A classical board picture is the fixed string:

- the first mode has one bulge,
- the second has two,
- the third has three.

Then the teacher can point out that the functions $$ \sin(n\pi x) $$ are eigenfunctions of the one-dimensional Laplacian with Dirichlet boundary conditions.

### Formal View

For a linear operator $$ A $$ on a Hilbert space $$ H $$, a number $$ \lambda $$ is an eigenvalue if there exists $$ u\ne 0 $$ such that $$ Au=\lambda u $$. When $$ A $$ is self-adjoint with compact resolvent, one often obtains a discrete family of eigenvalues $$ \lambda_1\le \lambda_2\le \cdots \to \infty $$ and associated eigenfunctions that form an orthogonal complete system in $$ H $$.

## Common Misconceptions

### "The spectrum is just the list of eigenvalues"

Not always. In infinite-dimensional settings the spectrum can be more subtle, though in many classical elliptic examples the discrete eigenvalues are the main part students first study.

### "Eigenfunctions are only a computational trick"

False. They are the natural language for describing dynamics, decomposition, and structure.

### "Every operator has a nice orthogonal eigenbasis"

No. Important hypotheses such as self-adjointness and compact resolvent are often needed.

### "Orthogonality is just a convenience"

No. It is the key that allows independent mode decomposition and Fourier-type expansion.

## Learning Progression

### Step 1: Begin with symmetric matrices

Students already know that symmetric matrices have real eigenvalues and orthogonal eigenvectors.

### Step 2: Move to differential operators

Show that the same philosophy reappears for self-adjoint operators in Hilbert spaces.

### Step 3: Study a concrete model

The Dirichlet Laplacian on an interval is the perfect first example.

### Step 4: Connect to expansions

Once eigenfunctions are known, solutions can be expanded mode by mode.

### Key Checkpoints

- Can students explain the analogy between symmetric matrices and self-adjoint operators?
- Can they identify the eigenfunctions of the one-dimensional Dirichlet Laplacian?
- Can they explain why orthogonality matters?

## Worked Examples

### Example 1: The Dirichlet Laplacian on $$ (0,1) $$

Consider

$$
\begin{cases}
-u''=\lambda u & \text{on } (0,1),\\
u(0)=u(1)=0.
\end{cases}
$$

The eigenvalues are $$ \lambda_n=n^2\pi^2 $$, and the corresponding eigenfunctions are $$ u_n(x)=\sin(n\pi x) $$. This is the fundamental model example of spectral theory in PDE.

### Example 2: Orthogonality of eigenfunctions

If $$ m\ne n $$, then

$$ \int_0^1 \sin(m\pi x)\sin(n\pi x)\,dx=0. $$

So different eigenmodes are orthogonal in $$ L^2(0,1) $$. This makes expansions and coefficient extraction possible.

### Example 3: Expanding a function in eigenmodes

A function $$ f\in L^2(0,1) $$ can be written formally as

$$ f(x)\sim \sum_{n=1}^\infty c_n\sin(n\pi x). $$

This is a spectral expansion: the eigenfunctions form the basis in which the operator becomes simple.

### Example 4: Why the heat equation becomes easier

If $$ u_t-\Delta u=0 $$ is expanded in eigenfunctions of $$ -\Delta $$, each coefficient satisfies an ordinary differential equation of the form $$ c_n'(t)+\lambda_n c_n(t)=0 $$. The PDE has been separated into independent scalar modes. This is the practical power of spectral theory.

## Conceptual Questions

1. Why is self-adjointness the right analogue of matrix symmetry?
2. Why does orthogonality make mode decomposition possible?
3. Why do eigenfunctions connect so naturally to Fourier methods?

## Application Problems

1. In a vibrating string, how do eigenfunctions describe natural vibration shapes?
2. In the heat equation, how do eigenvalues control the rate of decay of different modes?
3. In quantum mechanics, why are eigenvalues interpreted as energy levels?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What do we gain by decomposing an operator into eigenmodes?
- Why are symmetric matrices the right starting point for this topic?
- Which feature of the Dirichlet Laplacian makes the sine basis so natural?

### Suggested Activities

- Draw the first few string modes and ask students to match them to formulas.
- Have students verify orthogonality integrals directly.
- Let groups explain how a PDE simplifies when expanded in eigenfunctions.

### Participation Moves

- Start from a physical vibration example.
- Ask students to describe an eigenfunction before writing the eigenvalue equation.
- Encourage them to connect this lesson with Fourier series from earlier chapters.

## Differentiation

### Support for Struggling Students

- Stay close to the interval $$ [0,1] $$ and the sine basis.
- Emphasize pictures of modes before abstract operator language.
- Reuse the analogy with symmetric matrices often.

### Challenge for Advanced Students

- Explore compact resolvent and why it leads to discrete spectra.
- Study the spectral theorem for bounded self-adjoint operators.
- Connect spectral theory to the later chapter on spectral asymptotics.

## Quick Summary

Spectral theory studies operators through their eigenvalues and eigenfunctions. In the best cases, self-adjoint operators behave like infinite-dimensional symmetric matrices, and their eigenmodes provide a natural basis for solving PDE.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Natural vibration modes
- Problem: Strings, membranes, and mechanical structures oscillate in characteristic modes.
- Model: Solve $$ Au=\lambda u $$ for a self-adjoint operator such as the Laplacian.
- Assumptions and limitations: The domain and boundary conditions determine the spectrum.
- Interpretation: The spectrum reveals natural frequencies and modal decompositions.

#### Quantum mechanics
- Problem: Energy levels of a quantum system are encoded in the spectrum of its Hamiltonian.
- Model: The standard example is a Schrödinger operator.
- Assumptions and limitations: Depending on the potential, the spectrum may be discrete, continuous, or mixed.
- Interpretation: Spectral theory turns dynamics into decomposition by energy modes.

### 2. Additional Intuition and Connections

Spectral theory is the infinite-dimensional analogue of matrix diagonalization. For sufficiently nice self-adjoint operators, one hopes to decompose the problem into orthogonal modes. A common pitfall is to think the spectrum consists only of eigenvalues; infinite-dimensional operators can also have continuous spectrum.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for n in [1, 2, 3, 4]:
    plt.plot(x, np.sin(n * np.pi * x), label=f"n={n}")

plt.legend()
plt.title("The first eigenfunctions of -d^2/dx^2 on [0,1]")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: spectral theory vibrating string eigenfunctions
- search: quantum well eigenstates visualization
- search: Laplacian spectrum rectangular domain

### 5. Worked Example

On $$ 0<x<1 $$ with Dirichlet boundary conditions, the problem
$$ -u''=\lambda u, \qquad u(0)=u(1)=0 $$
has nontrivial solutions precisely for
$$ \lambda_n=n^2\pi^2, \qquad u_n(x)=\sin(n\pi x). $$
This is the model example of decomposition into orthogonal modes.

### 6. Difficulty Layering

**Undergraduate level.** Learn spectral theory through familiar eigenvalue problems.

**Graduate level.** Connect to compact operators, resolvents, continuous spectrum, and functional calculus.
