---
layout: post
title: "13-01 Euler's Method"
chapter: '13'
order: 1
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: required
---

## Learning Objectives

This lesson introduces Euler's method as the first numerical scheme for ordinary differential equations. Students should understand how tangent-line approximation leads to a step-by-step update rule, how forward and backward Euler differ, and why discretization error must be analyzed carefully.

## Prerequisites

Students should know first-order ODEs, slope fields, and the geometric meaning of a derivative as local linear approximation. These ideas are reviewed in Lesson 13.00.

## Introduction

![Euler's method]({{ site.imgurl }}/chapter_img/chapter13/01_eulers_method.svg)

Exact ODE solutions are elegant, but in applications they are often unavailable or impractical. Numerical methods begin with a simple idea: if we know the derivative at the current point, then for a short time we can approximate the true solution by its tangent line.

Euler's method is the most basic realization of that idea. It is simple enough to derive in minutes and deep enough to launch the whole study of numerical differential equations.

## Concept in Three Ways

### Intuitive View

We move along the solution curve by taking short linear steps in the direction indicated by the ODE. Each step uses the current slope to predict the next value.

### Visual View

On a graph, Euler's method replaces the smooth solution curve by a polygonal path made from tangent-line segments. The smaller the time step, the better this polygon tracks the true solution.

### Formal View

For an initial value problem
$$ y' = f(t,y), \qquad y(t_0)=y_0, $$
with step size $$ h $$, forward Euler gives
$$ y_{n+1}=y_n+h f(t_n,y_n). $$
Backward Euler instead uses
$$ y_{n+1}=y_n+h f(t_{n+1},y_{n+1}), $$
which is implicit.

## Why the Method Matters

Euler's method is the first bridge from differential equations to algorithms. It teaches the central ideas of discretization, local truncation error, global error, and the tradeoff between simplicity and accuracy.

It also introduces a foundational insight: a good continuous model does not automatically produce a good numerical method. Stability and error behavior must be studied on their own terms.

## Common Misconceptions

### "Euler's method is too simple to matter"

No. It is the prototype from which many numerical ideas grow.

### "Smaller step size always solves every problem"

Not completely. It helps, but stiffness and stability can still create major issues.

### "Forward and backward Euler are basically the same"

No. One is explicit and simple, the other implicit and often more stable.

## Suggested Learning Path

### Step 1: Start from tangent-line approximation

Students should understand the geometric origin of the update rule.

### Step 2: Derive forward Euler

The derivation should feel natural from linearization.

### Step 3: Compare with backward Euler

This introduces the idea of implicit versus explicit schemes.

### Step 4: Discuss error and stability

Students should see immediately that computation is not only about producing numbers.

### Checkpoints

- Can students explain why the Euler update is a tangent-line step?
- Do they understand the difference between explicit and implicit forms?
- Can they say why repeated small local errors accumulate into global error?

## Worked Examples

### Example 1: Exponential Growth

For $$ y'=y $$, Euler's method approximates the exponential solution with repeated multiplicative updates.

### Example 2: Decay Equation

For $$ y'=-ky $$, Euler's method shows how numerical decay depends on the step size and can even misbehave if the step is poorly chosen.

### Example 3: Backward Euler Stability

For a rapidly decaying problem, backward Euler often remains stable when forward Euler struggles.

## Conceptual Questions

1. Why is Euler's method naturally connected to local linearization?
2. Why do local errors accumulate globally?
3. Why does implicitness matter for stability?

## Application Problems

1. Why is Euler's method often the first method implemented in simulation software?
2. In population modeling, why might a large time step produce misleading behavior?
3. Why are stiff problems a challenge for explicit methods?

## Interactive Teaching Strategies

- Plot one exact solution and one Euler polygon on the same graph.
- Have students compute several steps by hand for a simple ODE.
- Compare forward and backward Euler qualitatively before formal stability analysis.
- Reinforce the phrase "continuous model, discrete update rule."

## Differentiation

### Support for Struggling Students

Students needing support should work visually with tangent-line steps and simple test equations.

### Challenge for Advanced Students

Advanced students can explore consistency, convergence, and the stability region of Euler methods.

## Summary

Euler's method is the first numerical stepping scheme for ODEs and the conceptual foundation of numerical differential equations. It introduces approximation, stability, and error in their most accessible form.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Orbital mechanics and celestial motion
- Problem: When closed-form solutions are inconvenient, we update position and velocity step by step.
- Model: Write
$$ \mathbf{y}' = f(t,\mathbf{y}), $$
then apply forward Euler:
$$
\mathbf{y}_{n+1}=\mathbf{y}_n+h f(t_n,\mathbf{y}_n).
$$
- Assumptions and limitations: The time step must be small enough; forward Euler can drift in phase and energy.
- Interpretation: The method turns an ODE into a step-by-step computational rule.

#### Population or capital growth
- Problem: We want a quick discrete approximation for
$$ y'=ky. $$
- Model:
$$ y_{n+1}=y_n+hky_n=(1+hk)y_n. $$
- Assumptions and limitations: Constant growth rate; large steps produce significant global error.
- Interpretation: Euler makes the link between continuous growth and discrete compounding explicit.

### 2. Additional Intuition and Connections

Forward Euler follows the tangent line at the beginning of each step, so it is the most natural first-order discretization. The deeper lesson is not just the formula, but the perspective: every numerical method replaces a smooth evolution law with a discrete update rule. A common pitfall is to think smaller steps always solve every problem; for stiff systems, stability matters just as much as local accuracy.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y
t0, y0, h = 0.0, 1.0, 0.25
N = 12
t = np.linspace(t0, t0 + N * h, N + 1)
y = np.zeros(N + 1)
y[0] = y0

for n in range(N):
    y[n + 1] = y[n] + h * f(t[n], y[n])

tt = np.linspace(t0, t[-1], 400)
plt.plot(tt, np.exp(tt), label="exact solution")
plt.plot(t, y, "o-", label="forward Euler")
plt.legend()
plt.title("Forward Euler for y' = y")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Euler method slope field animation
- search: forward vs backward Euler stability visualization
- search: tangent line numerical ODE intuition

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="Forward Euler: exact versus numerical solution" description="Adjust lambda, step size, and the initial value to see directly how global error behaves in the forward Euler method." path="interactives/chapter13/euler-method-en.html" height="620px" %}

### 5. Worked Example

For
$$ y'=y, \qquad y(0)=1, $$
with step $$ h=0.5 $$, forward Euler gives
$$ y_1=1+0.5(1)=1.5, \qquad y_2=1.5+0.5(1.5)=2.25. $$
Meanwhile the exact value at $$ t=1 $$ is $$ e \approx 2.718 $$. This clearly shows how short linear steps approximate exponential growth only gradually.

### 6. Difficulty Layering

**Undergraduate level.** Derive Euler from tangent-line approximation and estimate error on simple ODEs.

**Graduate level.** Connect to consistency, absolute stability, and modified equations.

## References

- Ascher & Petzold: introductory discussion of one-step ODE methods.
