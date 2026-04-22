---
layout: post
title: "06-04 The Frobenius Method"
chapter: '06'
order: 4
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: required
---

This lesson presents the Frobenius method—the generalization of power series to handle regular singular points. This is the key technique for solving ODEs near singular points like Bessel's and Legendre's equations.

> **Teaching Notes**: Most challenging lesson in Chapter 06. Start with regular singular point definition (review from 06-02). Walk through Example 1 completely. If time is short, skip exceptional cases. Activity: "Classify the Singularity" (15 min).

---

## Introduction

At an ordinary point, we use power series $$ y = \sum a_n x^n $$. At a regular singular point, we need the **Frobenius method**: try solutions of the form

$$y = x^r \sum_{n=0}^{\infty} a_n x^n = \sum_{n=0}^{\infty} a_n x^{r+n}$$

where $$ r $$ is determined from an **indicial equation** (like Euler, but now a polynomial).

> **Intuitive**: The singular point forces a "correction" to the power. Instead of starting at $$ x^0 $$, we start at $$ x^r $$. The $$ r $$ tells us HOW we diverge from the regular point.

---

## 1. Regular Singular Points

### 1.1 Definition

For $$ y'' + p(x)y' + q(x)y = 0 $$:

$$ x_0 $$ is a **regular singular point** if:
- $$ (x-x_0)p(x) $$ is analytic at $$ x_0 $$
- $$ (x-x_0)^2 q(x) $$ is analytic at $$ x_0 $$

This "weakens" the singularity enough for Frobenius to work.

**Example**: $$ y'' + \frac{1}{x}y = 0 $$ has singular point at $$ x=0 $$.
- $$ xp(x) = 0 $$ (analytic ✓)
- $$ x^2 q(x) = x^2/x = x $$ (analytic ✓)
Therefore: regular singular point!

> **Visual**: Compare strong (irregular) vs. weak (regular) singularities. The regular ones are "tamed" enough to handle.

### 1.2 Why This Matters

At regular singular points, solutions behave like $$ x^r $$ times a series. The $$ r $$ roots determine the leading behavior. Bessel and Legendre equations have regular singular points at $$ x=0 $$.

---

## 2. The Method

### 2.1 Trial Solution

At regular singular point $$ x=0 $$:
$$y = x^r \sum_{n=0}^{\infty} a_n x^n = \sum_{n=0}^{\infty} a_n x^{r+n}$$

where $$ a_0 \neq 0 $$.

### 2.2 Process

1. Write $$ y = x^r \sum a_n x^n $$
2. Substitute into ODE
3. Collect powers of $$ x $$ (now shifted by $$ r $$)
4. Get indicial equation for $$ r $$
5. Solve for $$ r $$ (two roots)
6. For each $$ r $$, get recurrence for coefficients
7. Form two independent solutions

> **Common Misconception**: Students treat $$ r $$ as an integer. Actually, $$ r $$ can be any real or complex number!

---

## 3. Worked Examples

### Example 1: $$ 2x^2 y'' + xy' - x^2 y = 0 $$

This is $$ 2x^2 y'' + x y' - x^2 y = 0 $$.

Divide by 2: $$ x^2 y'' + \frac{1}{2}xy' - \frac{1}{2}x^2 y = 0 $$

At $$ x=0 $$: $$ p(x) = 1/(2x) $$, $$ q(x) = -1/(2) $$

Check regularity:
- $$ x p(x) = 1/2 $$ (analytic ✓)
- $$ x^2 q(x) = -x^2/2 $$ (analytic ✓)

So regular singular point. Try $$ y = x^r \sum a_n x^n = \sum a_n x^{r+n} $$.

Compute derivatives:
- $$ y' = \sum a_n (r+n) x^{r+n-1} $$
- $$ y'' = \sum a_n (r+n)(r+n-1) x^{r+n-2} $$

Substitute. Collecting lowest power $$ x^{r-2} $$:
$$ a_0[2(r)(r-1) + r] = a_0[2r^2 - r] = 0 $$

Indicial: $$ 2r^2 - r = 0 \Rightarrow r(2r - 1) = 0 $$

Roots: $$ r_1 = 0 $$, $$ r_2 = 1/2 $$

Since $$ r_1 - r_2 = -1/2 $$ (not an integer), solutions are independent.

For $$ r_1 = 0 $$: recurrence give one solution.
For $$ r_2 = 1/2 $$: recurrence gives second solution.

> **Checkpoint**: Can students identify $$ r $$ values and determine whether they differ by an integer?

### Example 2: $$ x^2 y'' + xy' + x^2 y = 0 $$ (Bessel of order 0)

This is Bessel's equation of order $$ \nu = 0 $$:

$$ x^2 y'' + x y' + x^2 y = 0 $$

At $$ x=0 $$: $$ xp(x) = 1 $$, $$ x^2 q(x) = x^2 $$ (both analytic). Regular singular point.

Indicial from lowest power:
$$ a_0[r(r-1) + r] = a_0[r^2] = 0 $$

So $$ r = 0 $$ is a repeated root! This is the Bessel case—only one power-series solution exists; the second involves $$ \ln x $$.

The $$ J_0(x) $$ solution has series: $$J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \cdots$$

The second solution $$ Y_0 $$ involves $$ \ln x $$.

---

## 4. The Three Cases

When roots differ by $$ r_1 - r_2 = \Delta $$:

**Case 1: $$ \Delta $$ not integer** (most common)
- Get two independent series solutions
- Each starts at its own $$ r $$

**Case 2: $$ \Delta = 0 $$ (repeated roots)**
- First solution: $$ y_1 = x^{r_1} \sum a_n x^n $$
- Second solution: $$ y_2 = y_1 \ln x + x^{r_1} \sum b_n x^n $$

**Case 3: $$ \Delta $$ is positive integer**
- First solution: $$ y_1 = x^{r_2} \sum a_n x^n $$ (starts at lower root)
- Second solution: May include $$ \ln x $$ term (the "exceptional case")

> **Checkpoint**: Can students identify which case they're in?

---

## 5. Radius of Convergence

The series solution converges for $$ \lvert x\rvert < R $$, where $$ R $$ is determined by distance to nearest singularity from the expansion point in the complex plane.

For equations with regular singular points at $$ x=0 $$, the solution converges until the next singularity.

---

## 6. Conceptual Questions

1. **Why multiply by $$ x^r $$?** $$ \rightarrow $$ The singular point "forces" a different power than $$ x^0 $$. The exponent $$ r $$ corrects for the type of singularity—exactly like how Euler uses $$ x^r $$.

2. **Why does Frobenius work at regular singular points?** $$ \rightarrow $$ Because the "weakness" condition ($$ (x-x_0)p $$ and $$ (x-x_0)^2q $$ analytic) ensures the equation behaves enough like Euler to let $$ x^r $$ work.

3. **What happens when roots differ by an integer?** $$ \rightarrow $$ The second solution gets "blocked" and must include $$ \ln x $$. This is the exceptional case.

---

## Interactive Activities

### Activity: "Classify the Singular Point" (15 min)

Given ODEs, students classify point $$ x=0 $$ and find $$ r $$ values:

| ODE | Classification | $$ r $$ values |
|-----|---------------|-----------|
| $$ y'' + \frac{1}{x}y' + y = 0 $$ | Regular | Solve $$ r(r-1) + r = 0 $$ |
| $$ y'' + \frac{1}{x^2}y = 0 $$ | Irregular | Can't use Frobenius |
| $$ y'' + y = 0 $$ | Ordinary | Use power series |
| $$ x^2 y'' + x y' + (x^2 - \nu^2)y = 0 $$ | Regular (Bessel) | $$ r = \pm \nu $$ |

---

## Summary

| Step | Action |
|------|--------|
| 1 | Identify regular singular point: $$ xp $$, $$ x^2q $$ analytic |
| 2 | Try $$ y = x^r \sum a_n x^n $$ |
| 3 | Get indicial equation for $$ r $$ |
| 4 | Solve for roots $$ r_1, r_2 $$ |
| 5 | Check $$ r_1 - r_2 $$ (integer?) |
| 6 | Find recurrence for each root |
| 7 | Form solution(s)—may need $$ \ln x $$ for repeated/conflict |

> **One-Liner**: Frobenius extends power series to regular singular points: try $$ x^r $$ times a series, get the indicial equation, and handle $$ \ln x $$ in the repeated-root or integer-difference cases.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Cylindrical and spherical models near the origin
- Problem: After separation of variables in cylindrical or spherical geometry, the radial equation has a singular point at the origin.
- Model:
$$ r^2 y''+r y'+(r^2-\nu^2)y=0. $$
- Assumptions and limitations: The singularity is regular rather than too severe.
- Interpretation: Frobenius detects the leading behaviors $$ r^\nu $$ and $$ r^{-\nu} $$ through the indicial equation.

#### Radial quantum equations
- Problem: Central-force models often lead to ODEs with $$ 1/r $$ or $$ 1/r^2 $$ singular structure.
- Model:
$$ r^2 y''+p(r) r y'+q(r)y=0 $$
with analytic $$ p,q $$ near $$ r=0 $$.
- Assumptions and limitations: The method is adapted to regular singular points, not arbitrary irregular ones.
- Interpretation: Physical admissibility often singles out the Frobenius branch that remains finite at the origin.

### 2. Additional Intuition and Connections

Frobenius is the natural extension of Taylor series when the equation has a mild singularity. Instead of forcing the leading term to be constant, we let the solution start with $$ x^r $$ and allow the equation to choose $$ r $$. A common pitfall is to miss the logarithmic second solution when the indicial roots differ by an integer or coincide.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

x = np.linspace(0.01, 10, 500)
plt.plot(x, jv(0, x), label="J0(x)")
plt.plot(x, np.ones_like(x), "--", label="leading r=0 term")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frobenius behavior for a Bessel-type equation")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Frobenius method regular singular point
- search: indicial equation visualization
- search: Bessel Frobenius series comparison

### 5. Worked Example

Consider
$$ x^2 y''+x y'+x^2 y=0. $$
Try
$$ y=\sum_{n=0}^{\infty}a_n x^{n+r}. $$
The lowest-order term yields the indicial equation
$$ r^2=0. $$
So $$ r=0 $$ is a repeated root, indicating that one Frobenius series solution exists and a second solution may involve a logarithm.

### 6. Difficulty Layering

**Undergraduate level.** Practice indicial equations, coefficient recurrences, and the main repeated-root or integer-difference cases.

**Graduate level.** Discuss regular versus irregular singularities, monodromy, and local analytic structure around singular points.

![Frobenius method]({{ site.imgurl }}/chapter_img/chapter06/06_04_frobenius_method.svg)

## References

- Boyce & DiPrima, Section 5.4: Frobenius method
- Abramowitz & Stegun: handbook of special functions
- Cambridge A Level notes on series solution techniques
