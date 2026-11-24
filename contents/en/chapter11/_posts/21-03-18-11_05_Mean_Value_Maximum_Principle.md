---
layout: post
title: "11-05 Mean Value Property and Maximum Principle"
chapter: '11'
order: 5
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

> **Storytelling Hook:** Suppose you measure the temperature on the walls of a source-free room and find every point on the boundary sits between $18^\circ\text{C}$ and $24^\circ\text{C}$. Without ever stepping inside, you can guarantee with mathematical certainty that no interior point is $24.1^\circ\text{C}$—and if even one interior point hits $24^\circ\text{C}$, the entire room must be a uniform $24^\circ\text{C}$. That astonishing rigidity flows from the **Mean Value Property** and **Maximum Principle**.

## Learning Objectives

This lesson studies qualitative properties of harmonic functions. Students should understand the mean value property, maximum principle, and the resulting uniqueness phenomena.

## Prerequisites

Students should know Laplace's equation and the idea that harmonic functions describe source-free equilibrium.

## Background Knowledge Map: Rigidity, Averaging, and Stability of Harmonic Functions

Four interlocking theorems turn the local statement $\Delta u = 0$ into global structural control:

1. **Spherical and Solid Mean Value Identities:** For any harmonic function $u$ and any closed ball $\overline{B_R(x_0)} \subset \Omega$, $u(x_0)$ equals both the surface average on $\partial B_R(x_0)$ and the volume average over $B_R(x_0)$. Conversely, any continuous function with the Mean Value Property is automatically $C^\infty$ and harmonic.
2. **Weak and Strong Maximum Principles:** On a bounded connected domain $\Omega$, a non-constant harmonic function attains its strict maximum and minimum exclusively on $\partial\Omega$. Reaching an extremum in the interior forces $u$ to be constant everywhere in $\Omega$.
3. **Uniqueness and $L^\infty$ Stability:** If two harmonic functions $u_1, u_2$ satisfy $|u_1 - u_2| \le \varepsilon$ on $\partial\Omega$, applying the Maximum Principle to $w = u_1 - u_2$ proves $|u_1 - u_2| \le \varepsilon$ throughout $\Omega$—giving immediate uniqueness ($\varepsilon = 0$) and continuous dependence on boundary data.
4. **Harnack's Inequality and Liouville's Theorem:** Positive harmonic functions cannot vary wildly on compact subsets (Harnack), and any bounded harmonic function on all of $\mathbb{R}^n$ must be constant (Liouville), echoing Liouville's theorem in complex analysis.

## Introduction

![Mean value property and maximum principle]({{ site.imgurl }}/chapter_img/chapter11/05_mean_value_maximum_principle.svg)

One of the most remarkable aspects of Laplace's equation is how rigid its solutions are. Harmonic functions do not behave like arbitrary smooth functions. They satisfy strong average and extremum properties that reveal how tightly the interior is controlled by the surrounding values.

The mean value property and the maximum principle are two of the most elegant expressions of this rigidity. Together, they explain why harmonic functions are so special and why elliptic equations are dominated by boundary behavior.

## Concept in Three Ways

### Intuitive View

A harmonic function is locally balanced. Its value at a point is not determined by a local spike or dip, but by a kind of equilibrium with nearby values.

### Visual View

If we average a harmonic function around a circle, the average equals the value at the center. This means the function cannot hide a sharp isolated peak in the interior.

### Formal View

For a harmonic function, the value at a point equals the average of the function on suitable surrounding spheres or circles. From this one derives the maximum principle: a nonconstant harmonic function cannot attain its maximum or minimum in the interior.

## Why These Principles Matter

These results are among the deepest structural theorems of elliptic PDE theory. They show that the interior values are constrained by the boundary, and they imply strong uniqueness results.

They also provide one of the clearest examples in analysis of how a differential equation can impose global geometric behavior.

## Common Misconceptions

### "The mean value property is just a nice curiosity"

No. It is a fundamental characterization of harmonicity.

### "A harmonic function can have a sharp interior maximum if it is smooth enough"

No. The maximum principle forbids this unless the function is constant.

### "These are only abstract theorems with no practical role"

No. They are central for uniqueness, estimates, and qualitative understanding.

## Suggested Learning Path

### Step 1: Start from equilibrium intuition

Students should think of harmonic functions as perfectly balanced states.

### Step 2: Introduce the averaging principle

The mean value property should be presented visually and conceptually.

### Step 3: Derive the maximum principle idea

Students should see why interior spikes are impossible.

### Step 4: Apply to uniqueness

This is where the theory becomes operational.

### Checkpoints

- Can students explain the mean value property in words?
- Do they understand why an interior maximum is incompatible with harmonic balance?
- Can they connect these principles to uniqueness of solutions?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Direct Verification of the Mean Value Property and Boundary Bounds

Consider $u(x,y) = x^2 - y^2 + 3x - 2$. First verify directly that its average over *any* circle of radius $R > 0$ centered at $(1,2)$ equals $u(1,2)$, and then use the Maximum Principle to find the exact extrema of $u$ on the closed unit disk $\overline{B_1}$.

1. **Verify harmonicity and center value:** $\Delta u = 2 - 2 = 0$, so $u$ is harmonic everywhere. At $(1,2)$,
   $$u(1,2) = 1^2 - 2^2 + 3(1) - 2 = 1 - 4 + 3 - 2 = -2.$$
2. **Parameterize the circle of radius $R$ around $(1,2)$:** Write $x = 1 + R\cos\theta$, $y = 2 + R\sin\theta$ for $\theta \in [0, 2\pi]$. Expanding $u$ on this circle:
   $$u(1+R\cos\theta, 2+R\sin\theta) = (1 + 2R\cos\theta + R^2\cos^2\theta) - (4 + 4R\sin\theta + R^2\sin^2\theta) + (3 + 3R\cos\theta) - 2.$$
   Collect terms using $\cos^2\theta - \sin^2\theta = \cos(2\theta)$:
   $$u(1+R\cos\theta, 2+R\sin\theta) = -2 + 5R\cos\theta - 4R\sin\theta + R^2\cos(2\theta).$$
3. **Take the circular average:** Since $\int_0^{2\pi} \cos\theta\,d\theta = \int_0^{2\pi} \sin\theta\,d\theta = \int_0^{2\pi} \cos(2\theta)\,d\theta = 0$,
   $$\frac{1}{2\pi}\int_0^{2\pi} u(1+R\cos\theta, 2+R\sin\theta)\,d\theta = -2 = u(1,2),$$
   independently of $R$!
4. **Find the global maximum and minimum on $\overline{B_1}$:** By the Maximum Principle, extrema must lie on $x^2 + y^2 = 1$, where $y^2 = 1 - x^2$ for $x \in [-1,1]$. Substituting eliminates $y$:
   $$g(x) = x^2 - (1 - x^2) + 3x - 2 = 2x^2 + 3x - 3, \qquad x \in [-1,1].$$
   The critical point $g'(x) = 4x + 3 = 0$ gives $x = -3/4 \in [-1,1]$, where $g(-3/4) = 2(9/16) - 9/4 - 3 = -33/8 = -4.125$. Checking endpoints: $g(-1) = -4$, $g(1) = 2$. Thus on all of $\overline{B_1}$, $-4.125 \le u(x,y) \le 2$, attained on $\partial B_1$ at $(-3/4, \pm\sqrt{7}/4)$ and $(1,0)$, respectively.

### Example 1: Constant Function

A constant function is harmonic and trivially satisfies both the mean value property and the maximum principle.

### Example 2: Linear Harmonic Function

A linear harmonic function has no isolated interior maximum, illustrating the rigidity of harmonic behavior.

### Example 3: Uniqueness of a Boundary-Value Problem

If two harmonic functions share the same boundary values, their difference is harmonic with zero boundary data. The maximum principle forces the difference to vanish.

## Conceptual Questions

1. Why does the mean value property express local equilibrium?
2. Why is the maximum principle a global consequence of local harmonicity?
3. Why are these principles so useful for uniqueness?

## Application Problems

1. Why does steady-state temperature inside a plate not develop an interior hot spot unless the boundary or source structure forces it?
2. Why is electrostatic potential in a charge-free region strongly constrained by surrounding values?
3. Why are qualitative principles valuable when explicit formulas are difficult or impossible?

## Interactive Teaching Strategies

- Use circle-averaging pictures to visualize the mean value property.
- Ask students to predict whether a nonconstant harmonic function can peak inside the domain.
- Compare harmonic functions with generic smooth functions that do not satisfy Laplace's equation.
- Use uniqueness proofs as the first serious application.

## Differentiation

### Support for Struggling Students

Students needing support should begin with graphical intuition and simple harmonic examples before formal theorem statements.

### Challenge for Advanced Students

Advanced students can investigate converse questions, such as whether the mean value property characterizes harmonic functions.

## Summary

Harmonic functions are rigid objects. The mean value and maximum principles express this rigidity in elegant and powerful ways, and they are among the most important structural tools in elliptic PDE theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Validating thermal sensor data
- Problem: If boundary temperatures stay within a fixed range, the interior cannot exceed that range when there is no source.
- Model: This follows from the maximum principle for $$ \Delta u=0 $$.
- Assumptions and limitations: Connected domain, sufficiently smooth harmonic function.
- Interpretation: Extremes of a harmonic function occur on the boundary, not in the interior.

#### Electrostatic potential without interior extrema
- Problem: In a charge-free region, electrostatic potential cannot have a strict interior maximum or minimum.
- Model: Mean value property and maximum principle for harmonic functions.
- Assumptions and limitations: No internal sources, sufficient smoothness.
- Interpretation: This qualitative fact is often more useful than an explicit formula.

### 2. Additional Intuition and Connections

The mean value property says that the value at a point equals the average over nearby circles. If a point were a genuine interior maximum, nearby averages would have to be smaller, which is impossible. That is the core intuition behind the maximum principle.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)
U = X**2 - Y**2

plt.contour(X, Y, U, levels=20)
plt.scatter([0], [0], color="red", label="u(0,0)=0 equals local average")
plt.axis("equal")
plt.legend()
plt.title("Contour lines of a harmonic function")
plt.show()
```

### 4. Suggested Searches

- search: maximum principle harmonic function visualization
- search: mean value property Laplace equation animation
- search: harmonic function no interior maxima

### 5. Worked Example

If $$ u $$ is harmonic on a bounded domain and $$ u=0 $$ on the entire boundary, then the maximum principle says both the maximum and minimum of $$ u $$ equal $$ 0 $$. Therefore
$$ u\equiv 0. $$
This gives a fast uniqueness proof without constructing the solution explicitly.

### 6. Difficulty Layering

**Undergraduate level.** Use the maximum principle for bounds and uniqueness.

**Graduate level.** Connect to Harnack inequalities, unique continuation, and weak maximum principles.

## Video tham khảo

- xem trước: [Harmonic functions: Mean value theorem](https://www.youtube.com/watch?v=p60dU_62KcQ) — Dr Chris Tisdell, English. Chris Tisdell proves the mean-value property of a harmonic function.
- [Properties of harmonic functions part 2: the mean value property](https://www.youtube.com/watch?v=_bC91Xqirgs) — William Nesse, English. The mean-value property stated and used.
- [Qualitative Properties of Laplace's Equation - Partial Differential Equations | Lecture 12](https://www.youtube.com/watch?v=Mi25YqpsxlM) — Jason Bramburger, English. Jason Bramburger on qualitative properties of Laplace's equation, including the maximum principle.

## References

- Evans, Chapter 2.
