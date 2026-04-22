---
layout: post
title: "08-05 Half-Range Expansions"
chapter: '08'
order: 5
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: required
---

## Learning Objectives

This lesson introduces half-range sine and cosine expansions. Students should understand why extensions from $$ [0,L] $$ to $$ [-L,L] $$ are useful, how even and odd extensions produce cosine-only or sine-only series, and why these expansions are important for PDE boundary conditions.

## Prerequisites

Students should know Fourier coefficients and the role of even and odd symmetry.

## Introduction

![Half-range expansions]({{ site.imgurl }}/chapter_img/chapter08/05_half_range_expansions.svg)

In many problems, a function is given only on half of a symmetric interval, usually $$ [0,L] $$. At first this seems to break the Fourier-series framework, since the standard formulas are written on $$ [-L,L] $$. The remedy is simple and elegant: extend the function to a symmetric interval in a way that matches the desired boundary behavior.

This is one of the most important moments in the chapter because it shows that Fourier analysis is flexible. The choice of extension is not arbitrary; it is guided by the structure of the problem.

## Concept in Three Ways

### Intuitive View

If we know a function only on half an interval, we may reflect it across the origin. Reflecting evenly produces a cosine series, while reflecting oddly produces a sine series.

### Visual View

An even extension creates a mirror image. An odd extension creates a sign-reversed mirror image. The resulting full function on $$ [-L,L] $$ then fits naturally into the standard Fourier framework.

### Formal View

Given $$ f(x) $$ on $$ [0,L] $$:

- the even extension leads to a cosine series,
- the odd extension leads to a sine series.

These are called half-range cosine and sine expansions.

## Why Half-Range Expansions Matter

Half-range expansions are essential in PDEs because boundary conditions frequently select sine or cosine bases. For example, zero-value boundary conditions often lead to sine modes, while zero-flux conditions often lead to cosine modes.

This means the choice of extension is really a way of encoding boundary behavior in harmonic language.

## Common Misconceptions

### "The extension is arbitrary"

No. The extension should be chosen to match the physical or boundary-value structure of the problem.

### "Half-range expansions are less important than full Fourier series"

No. In PDE applications they are often the natural and necessary form.

### "Sine and cosine series are just cosmetic variants"

No. They correspond to distinct symmetry and boundary interpretations.

## Suggested Learning Path

### Step 1: Start with a function on $$ [0,L] $$

Students should recognize why the ordinary full-range formulas do not apply immediately.

### Step 2: Construct the even and odd extensions

This step should be visual and geometric before it becomes algebraic.

### Step 3: Write the resulting cosine or sine series

Students should see how the extension choice determines the basis.

### Step 4: Connect to PDEs

This is where the lesson becomes truly useful.

### Checkpoints

- Can students explain the difference between even and odd extension?
- Do they know why one leads to cosine and the other to sine?
- Can they connect the choice to a boundary condition?

## Worked Examples

### Example 1: Even Extension

A function defined on $$ [0,L] $$ can be reflected evenly to produce a cosine-only expansion.

### Example 2: Odd Extension

The same original function can be reflected oddly to produce a sine-only expansion.

### Example 3: PDE Interpretation

If a rod has zero temperature at one end, sine modes often appear naturally. If a boundary condition expresses zero derivative, cosine modes may be more appropriate.

## Conceptual Questions

1. Why is extending a function to $$ [-L,L] $$ useful even if the original problem lives on $$ [0,L] $$?
2. Why do odd extensions naturally produce sine series?
3. How do half-range expansions connect to boundary-value problems?

## Application Problems

1. In heat conduction on $$ [0,L] $$, how do boundary conditions suggest the correct half-range basis?
2. In string vibration, why are sine modes often more natural than cosine modes?
3. Why is a half-range expansion not merely an algebraic trick, but a modeling choice?

## Interactive Teaching Strategies

- Ask students to sketch the even and odd extensions of the same function.
- Compare the resulting series conceptually before computing coefficients.
- Tie each extension to a physical boundary condition.
- Reinforce that extension choice reflects structure, not convenience alone.

## Differentiation

### Support for Struggling Students

Students needing support should work visually with extensions and sketches before engaging coefficient formulas.

### Challenge for Advanced Students

Advanced students can compare how the same original function behaves under sine versus cosine expansion and discuss which is more natural in different applications.

## Summary

Half-range expansions are not artificial tricks. They are exactly the harmonic tools needed when a problem is posed on $$ [0,L] $$ and when boundary conditions naturally select sine or cosine modes. They are one of the central bridges from Fourier series to PDE solution methods.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Heat or vibration on a half-interval
- Problem: Data are given only on $$ [0,L] $$, but the natural separated basis uses sines or cosines on a symmetric interval.
- Model: Extend the function evenly to obtain a cosine series, or oddly to obtain a sine series.
- Assumptions and limitations: The extension must match the physical boundary condition.
- Interpretation: Half-range expansions convert a problem on $$ [0,L] $$ into a standard periodic Fourier problem on $$ [-L,L] $$.

#### Fixed and free endpoint models
- Problem: A fixed boundary suggests sine modes, while a free or zero-flux boundary suggests cosine modes.
- Model: Use sine or cosine half-range expansions according to the endpoint physics.
- Assumptions and limitations: The choice depends on the actual boundary condition being modeled.
- Interpretation: Half-range expansions are the natural language for many finite-interval PDE problems.

### 2. Additional Intuition and Connections

Half-range expansions show that Fourier analysis is not restricted to functions that are originally periodic. We can create a periodic setting by extending the function appropriately. A common pitfall is to choose the wrong extension and therefore obtain a basis incompatible with the physical boundary conditions.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x_ext = np.linspace(-np.pi, np.pi, 800)
odd_ext = x_ext
even_ext = np.abs(x_ext)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x_ext, odd_ext)
axes[0].set_title("Odd extension -> sine series")
axes[1].plot(x_ext, even_ext)
axes[1].set_title("Even extension -> cosine series")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: half range sine cosine series visualization
- search: odd even extension Fourier series
- search: boundary conditions sine cosine expansions

### 5. Worked Example

For $$ f(x)=x $$ on $$ [0,\pi] $$, the odd extension produces the sine series
$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$
The even extension leads instead to a cosine series with completely different coefficients. The same half-interval data therefore yield two different expansions, depending on the intended boundary condition.

### 6. Difficulty Layering

**Undergraduate level.** Learn to choose even or odd extension and compute the corresponding sine or cosine series.

**Graduate level.** Connect half-range expansions to the eigenfunction bases of Dirichlet and Neumann Laplacians on finite intervals.

## References

- Haberman, Chapter 3: classical treatment of half-range sine and cosine series.
