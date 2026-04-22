---
layout: post
title: "Sobolev Spaces"
chapter: '12'
order: 3
owner: Lê Minh Hoàng
lang: en
categories:
- chapter12
lesson_type: required
---

![The intuition behind Sobolev spaces and weak gradients]({{ site.imgurl }}/chapter_img/chapter12/03_sobolev_spaces.svg )

## Objectives

This lesson builds Sobolev spaces as the setting in which we measure both a function and its weak derivatives. After the lesson, students should understand the definition of $$ W^{k,p} $$, the special role of $$ H^k=W^{k,2} $$, the meaning of $$ H^1_0 $$ in boundary-value problems, and the intuition that Sobolev spaces connect energy control to regularity.

## Prerequisites

Students should know $$ L^p $$ spaces, weak derivatives, norms, inner products, and the basic intuition of Dirichlet boundary conditions. It is also helpful to remember that in PDE, smoothness is often not assumed at the start but derived later.

## Introduction

When solving PDE, it is rarely enough to know that a function is integrable. We usually also need to control slope, curvature, or higher-order derivatives. But if we insist on classical derivatives only, we exclude too many important solutions. Sobolev spaces resolve exactly that tension: they are wide enough to contain weak solutions and structured enough to carry geometric and energetic information.

## The Concept in Three Ways

### Intuitive View

Imagine a stretched sheet. To decide whether it is smooth or wrinkled, it is not enough to know how high the sheet is. We also need to know how quickly its slope changes. A Sobolev norm measures both the size of the function and the size of its weak derivatives.

### Visual View

Two graphs may have the same $$ L^2 $$ size while one oscillates wildly and the other changes slowly. Sobolev spaces distinguish these cases because they look at the graph and at its gradient. A strong classroom picture is to draw two functions with the same rough height but very different slopes and show that $$ L^2 $$ alone does not capture the difference.

### Formal View

For $$ k\in\mathbb{N} $$ and $$ 1\le p\le\infty $$,

$$
W^{k,p}(\Omega)=\left\{u\in L^p(\Omega):D^\alpha u\in L^p(\Omega)\text{ for all }\lvert \alpha\rvert\le k\right\},
$$

where derivatives are taken in the weak sense.

When $$ p=2 $$, we write $$ H^k(\Omega)=W^{k,2}(\Omega) $$. In particular,

$$
\lVert u\rVert_{H^1}^2=\lVert u\rVert_{L^2}^2+\lVert \nabla u\rVert_{L^2}^2.
$$

The space $$ H^1_0(\Omega) $$ is the closure of $$ C_c^\infty(\Omega) $$ in the $$ H^1 $$ norm and is the natural home for homogeneous Dirichlet data.

## Common Misconceptions

### "A Sobolev space is just the $$ L^p $$ space of a derivative"

Not enough. The function itself and all weak derivatives up to the required order must belong to $$ L^p $$.

### "If a function is not smooth, it cannot belong to a Sobolev space"

False. Many nonsmooth functions, such as $$ \lvert x\rvert $$ on a bounded interval, lie in $$ H^1 $$.

### "$$ H^1_0 $$ means the function is classically zero at every boundary point"

Not necessarily. In Sobolev theory, boundary conditions are interpreted through traces or closure by smooth compactly supported functions.

### "Sobolev embedding always gives continuity"

False. The conclusion depends strongly on derivative order, dimension, and the exponent $$ p $$.

## Learning Progression

### Step 1: Start from weak derivatives

Sobolev spaces are simply the spaces of functions whose weak derivatives are integrable in the required sense.

### Step 2: Focus first on $$ H^1 $$

This is the most common Sobolev space in elliptic PDE and variational problems.

### Step 3: Introduce $$ H^1_0 $$

Students should see it as the natural space for homogeneous Dirichlet problems.

### Step 4: Preview embeddings

Controlling weak derivatives forces extra structure. This is the bridge from energy to regularity.

### Key Checkpoints

- Can students explain why $$ \lvert x\rvert $$ belongs to $$ H^1(-1,1) $$?
- Can they distinguish $$ H^1 $$ from $$ H^1_0 $$?
- Can they say why dimension matters for Sobolev embedding?

## Worked Examples

### Example 1: A linear function

Let $$ u(x)=x $$ on $$ (0,1) $$. Then $$ u\in L^2(0,1) $$ and the weak derivative is $$ u'(x)=1\in L^2(0,1) $$. Therefore $$ u\in H^1(0,1) $$. However, since it does not vanish at both endpoints, it does not belong to $$ H^1_0(0,1) $$.

### Example 2: The absolute-value function

Let $$ u(x)=\lvert x\rvert $$ on $$ (-1,1) $$. We know that $$ u\in L^2(-1,1) $$ and that its weak derivative is the sign function, which also lies in $$ L^2(-1,1) $$. Therefore $$ \lvert x\rvert\in H^1(-1,1) $$. This is a basic example of a Sobolev function that is not classically differentiable everywhere.

### Example 3: A singular function

Let $$ u(x)=x^{-1/2} $$ on $$ (0,1) $$. Since $$ u\notin L^2(0,1) $$, it certainly cannot belong to $$ H^1(0,1) $$. Sobolev membership always starts with integrability of the function itself.

### Example 4: A smooth compactly supported function

If $$ u\in C_c^\infty(\Omega) $$, then all derivatives of $$ u $$ are smooth and compactly supported, so they belong to every $$ L^p $$ on bounded domains. Hence $$ u\in W^{k,p}(\Omega) $$ for all finite orders $$ k $$ and exponents $$ p $$. These smooth functions serve as the building blocks of Sobolev spaces.

## Conceptual Questions

1. Why is $$ H^1 $$ often a more natural space for PDE than $$ C^1 $$?
2. Why must the $$ H^1 $$ norm include both the function and its gradient?
3. Why does the effect of Sobolev embedding depend on dimension?

## Application Problems

1. In a membrane problem, why is the deformation energy naturally expressed using $$ \lVert \nabla u\rVert_{L^2} $$?
2. In image smoothing, how does penalizing the gradient relate to Sobolev norms?
3. In elasticity, why are finite-energy displacement fields placed in Sobolev spaces instead of classical smooth spaces?

## Interactive Teaching Strategies

### Questions to Ask in Class

- Can a function with a corner still have finite energy?
- Why do we need $$ H^1_0 $$ in boundary-value problems?
- Is it enough to control only the size of the function and ignore its gradient?

### Suggested Activities

- Give students a list of model functions and ask them to classify each one into $$ L^2 $$, $$ H^1 $$, and $$ H^1_0 $$.
- Compare two functions with similar height but different oscillation and discuss which norm sees the difference.
- Ask small groups to invent an example that lies in $$ H^1 $$ but is not classically smooth.

### Participation Moves

- Ask for verbal explanations before formulas.
- Let students predict whether a function belongs to $$ H^1 $$ before calculating.
- Encourage students to tie the gradient term to a physical meaning such as energy or deformation.

## Differentiation

### Support for Struggling Students

- Work mostly in one dimension at first.
- Use familiar examples such as $$ x $$, $$ \lvert x\rvert $$, and $$ x^2 $$.
- Repeat the slogan "Sobolev means the function and its weak derivatives are integrable."

### Challenge for Advanced Students

- Prove that $$ H^1(\Omega) $$ is a Hilbert space.
- Explore the idea of traces.
- Investigate the first Sobolev embedding results in low dimensions.

## Quick Summary

Sobolev spaces control both a function and its weak derivatives. They are the natural framework for weak solutions, energy methods, and the first step from rough functions toward regularity theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Finite-energy elastic displacement
- Problem: In continuum mechanics, the key quantity is often finite strain energy rather than classical smoothness.
- Model: The space $$ H^1(\Omega) $$ collects functions whose values and weak gradients both lie in $$ L^2 $$.
- Assumptions and limitations: Linearized energy, quadratic strain model.
- Interpretation: Sobolev spaces are the natural language of elastic energy.

#### Heat flow and groundwater
- Problem: Temperature or pressure fields in rough media may fail to be classically smooth but still have square-integrable gradients.
- Model: Solutions are sought in $$ H^1 $$ rather than in a classical differentiable class.
- Assumptions and limitations: The domain and coefficients may lack high regularity.
- Interpretation: Sobolev spaces allow PDE models to live on realistic geometries and data.

### 2. Additional Intuition and Connections

Sobolev spaces measure both the size of a function and the size of its weak derivatives. They therefore sit between the rough world of $$ L^2 $$ and the overly restrictive world of $$ C^1 $$. A common pitfall is to identify $$ H^1 $$ with classically differentiable functions; many important $$ H^1 $$ functions only have weak derivatives.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
u = np.abs(x - 0.5)
v = x * (1 - x)

du = np.gradient(u, x)
dv = np.gradient(v, x)

print("Approx H1 seminorm of u:", np.sqrt(np.trapz(du**2, x)))
print("Approx H1 seminorm of v:", np.sqrt(np.trapz(dv**2, x)))

plt.plot(x, u, label="u=|x-1/2|")
plt.plot(x, v, label="v=x(1-x)")
plt.legend()
plt.title("Two nonclassical-looking functions that still belong to H1(0,1)")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Sobolev space intuition H1 finite energy
- search: weak gradient visualization Sobolev spaces
- search: finite element Sobolev space motivation

### 5. Worked Example

The function
$$ u(x)=\lvert x-\tfrac12\rvert $$
on $$ [0,1] $$ is not classically differentiable at $$ x=\tfrac12 $$, but its weak derivative equals $$ -1 $$ on the left and $$ 1 $$ on the right, so it belongs to $$ L^2(0,1) $$. Therefore
$$ u \in H^1(0,1). $$
This is a standard example of a finite-energy function with a sharp corner.

### 6. Difficulty Layering

**Undergraduate level.** Treat $$ H^1 $$ as the space of finite-energy functions.

**Graduate level.** Connect to trace theorems, compact embeddings, and Rellich-Kondrachov.
