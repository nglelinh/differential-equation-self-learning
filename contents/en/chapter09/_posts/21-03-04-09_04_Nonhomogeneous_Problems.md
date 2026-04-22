---
layout: post
title: "09-04 Nonhomogeneous Problems"
chapter: '09'
order: 4
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: required
---

## Learning Objectives

This lesson handles heat equations with nonhomogeneous terms or boundary data. Students should understand steady-state decomposition and the idea of reducing nonhomogeneous problems to homogeneous ones plus correction terms.

## Prerequisites

Students should know separation of variables for homogeneous heat problems and the role of boundary conditions in determining eigenfunctions.

## Introduction

![Nonhomogeneous heat equation problems]({{ site.imgurl }}/chapter_img/chapter09/04_nonhomogeneous_heat.svg)

Real heat problems are rarely perfectly homogeneous. A rod may have nonzero endpoint temperatures, external heat sources, or nonuniform environmental forcing. In such cases, the pure homogeneous framework is no longer enough, but the core ideas of separation of variables still survive through decomposition.

The standard strategy is to split the solution into a steady component and a transient component. This turns a more complicated problem into one that is structurally familiar.

## Concept in Three Ways

### Intuitive View

If the boundary keeps injecting or maintaining heat, the temperature profile tends to settle around a nonzero equilibrium shape. What remains after subtracting that equilibrium is a transient part that decays over time.

### Visual View

The full solution can be imagined as a fixed background profile plus a time-dependent correction that gradually fades. The background captures the nonhomogeneous forcing, while the correction behaves like a homogeneous diffusion problem.

### Formal View

If
$$ u_t = \alpha^2 u_{xx} + f(x,t) $$
or the boundary data are nonzero, one often writes
$$ u(x,t)=v(x,t)+w(x), $$
where $$ w(x) $$ is chosen to satisfy the nonhomogeneous boundary or steady-state part. Then $$ v(x,t) $$ satisfies a related homogeneous problem more suitable for Fourier methods.

## Why Decomposition Matters

Nonhomogeneous problems show that classical methods are not fragile. Instead of abandoning separation of variables, we adapt it by transforming the problem into one with homogeneous structure.

This lesson is also important conceptually because it separates persistent effects from transient effects. In applications, that distinction often matters more than the exact formula itself.

## Common Misconceptions

### "Nonhomogeneous means separation of variables no longer works"

No. Often it works after a suitable decomposition.

### "The steady-state part is unimportant"

No. It may dominate the long-term behavior of the system.

### "Boundary forcing and source forcing are the same thing"

Not necessarily. They affect the problem differently and may require different correction strategies.

## Suggested Learning Path

### Step 1: Identify the source of nonhomogeneity

Students should distinguish nonzero forcing from nonzero boundary data.

### Step 2: Solve for a steady or correcting profile

This isolates the persistent nonhomogeneous structure.

### Step 3: Reduce to a homogeneous transient problem

The remaining part can then be handled with standard separation methods.

### Step 4: Interpret the result physically

The total solution combines equilibrium and decay.

### Checkpoints

- Can students identify what must be subtracted to homogenize the problem?
- Do they understand the physical difference between steady and transient parts?
- Can they explain why the transient part often decays away?

## Worked Examples

### Example 1: Nonzero Boundary Temperatures

If a rod has endpoints held at different temperatures, one first finds the steady-state linear profile and then studies the deviation from it.

### Example 2: Internal Heat Source

With a source term, the steady-state equation becomes a Poisson-type ODE in space, while the transient part still satisfies a homogeneous diffusion problem.

### Example 3: Long-Time Limit

In many problems, the transient contribution decays and the solution approaches the steady profile. This explains the physical meaning of equilibrium temperature distributions.

## Conceptual Questions

1. Why is it helpful to split a nonhomogeneous problem into steady and transient parts?
2. Why does the transient part usually satisfy a homogeneous equation?
3. Why is the long-term behavior often controlled by the steady-state component?

## Application Problems

1. How would you model a rod with one end kept hot and the other kept cold?
2. Why does an internal heat source prevent the equilibrium profile from being harmonic?
3. In practice, why is long-time behavior often more important than the full transient formula?

## Interactive Teaching Strategies

- Ask students to identify which parts of a problem are transient and which are persistent.
- Use physical rod examples with nonzero endpoint temperatures.
- Compare the full problem and the homogenized problem side by side.
- Emphasize decomposition as a structural idea rather than a trick.

## Differentiation

### Support for Struggling Students

Students needing support should work with simple nonzero boundary examples before handling source terms.

### Challenge for Advanced Students

Advanced students can examine time-dependent forcing or higher-dimensional nonhomogeneous heat problems.

## Summary

Nonhomogeneous heat problems are often solved by splitting the solution into steady and transient parts. This decomposition is physically natural, mathematically effective, and one of the most useful strategies in classical PDE analysis.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Time-dependent boundary temperatures
- Problem: The rod endpoints are driven by nonhomogeneous thermal data.
- Model: Split the solution into a boundary-fitting part and a homogeneous remainder:
$$ u(x,t)=v(x,t)+w(x,t). $$
- Assumptions and limitations: The auxiliary part $$ w $$ is chosen to absorb the boundary difficulty.
- Interpretation: Nonhomogeneous boundaries can often be reduced to homogeneous ones by a smart change of unknown.

#### Interior heat sources
- Problem: The system includes forcing inside the domain.
- Model:
$$ u_t=\alpha^2 u_{xx}+f(x,t). $$
- Assumptions and limitations: The source is smooth enough for expansion or Duhamel methods.
- Interpretation: The solution splits into a free part and a forced part.

### 2. Additional Intuition and Connections

Nonhomogeneous heat problems usually do not require a fundamentally new method. The key is to separate off a part that handles the boundary or forcing. A common pitfall is to force nonhomogeneous boundary data directly into a sine basis without first changing variables.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 300)
t = 0.05
steady = x
transient = 0.3 * np.sin(np.pi * x) * np.exp(-np.pi**2 * t)
u = steady + transient

plt.plot(x, steady, label="boundary-fitting part")
plt.plot(x, u, label="full solution")
plt.xlabel("x")
plt.ylabel("u")
plt.title("Splitting a nonhomogeneous heat problem")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: nonhomogeneous heat equation steady state decomposition
- search: Duhamel principle heat equation
- search: heat equation with source term visualization

### 5. Worked Example

Consider
$$ u_t=u_{xx},\qquad u(0,t)=0,\qquad u(1,t)=1. $$
Set
$$ w(x)=x,\qquad v(x,t)=u(x,t)-x. $$
Then $$ v $$ satisfies homogeneous boundary conditions,
$$ v(0,t)=v(1,t)=0, $$
so the standard separation-of-variables machinery applies to $$ v $$.

### 6. Difficulty Layering

**Undergraduate level.** Learn the standard trick of converting nonhomogeneous boundary data into homogeneous boundary data.

**Graduate level.** Connect to Duhamel's principle, superposition, and semigroup formulations with forcing.

## References

- Haberman, Chapters 1-2.
