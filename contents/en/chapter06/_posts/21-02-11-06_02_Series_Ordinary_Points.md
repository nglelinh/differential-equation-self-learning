---
layout: post
title: "06-02 Series Solutions Near Ordinary Points"
chapter: '06'
order: 2
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: required
---

This lesson develops the method for finding power series solutions of ODEs about ordinary points—the foundation for all series solution techniques.

> **Teaching Notes**: Core technique for chapter. Walk through Example 1 completely. Emphasize how ODE becomes recurrence. Activity: "Recurrence Challenge" (20 min).

---

## Introduction

When an ODE can't be solved in closed form, we look for solutions as power series. If $$ x_0 $$ is an **ordinary point** (coefficients analytic there), the solution can be expressed as a power series about $$ x_0 $$. This is our first method— we'll handle singular points in the Frobenius method lesson.

> **Intuitive**: Think of a power series as an "infinite polynomial." Since polynomials satisfy ODEs (no derivatives of non-polynomial functions), making it "infinite" lets the series satisfy the ODE exactly.

---

## 1. Ordinary and Singular Points

### 1.1 Definition

For second-order linear ODE: $$ y'' + p(x)y' + q(x)y = 0 $$

- **Ordinary point** at $$ x_0 $$: $$ p(x) $$ and $$ q(x) $$ analytic at $$ x_0 $$ (finite, no division by zero)
- **Singular point** at $$ x_0 $$: either $$ p $$ or $$ q $$ not analytic there

**Example**: $$ y'' + x^{-1}y' + y = 0 $$ has singular point at $$ x = 0 $$ (because $$ x^{-1} $$ is not analytic there).

> **Visual**: Draw number line showing where coefficients are "nice" vs. "bad."

### 1.2 Why This Matters

At an ordinary point, we can always find two linearly independent power series solutions. At a singular point, we need more sophisticated methods (Frobenius).

> **Checkpoint**: Can students identify ordinary vs. singular points in $$ y'' + \sin(x)y = 0 $$?

---

## 2. Method: Series Solutions at Ordinary Points

### 2.1 The Method

1. Assume solution as power series: $$ y = \sum_{n=0}^{\infty} a_n(x - x_0)^n $$
2. Substitute into ODE
3. Collect powers of $$ (x - x_0)^n $$ to get recurrence for $$ a_n $$
4. Determine radius of convergence from coefficients
5. Write first few terms (or general form if possible)

### 2.2 Substitution Reminders

When substituting, remember:
- $$ y' = \sum_{n=1}^{\infty} n a_n (x - x_0)^{n-1} $$
- $$y'' = \sum_{n=2}^{\infty} n(n-1)a_n(x - x_0)^{n-2}$$

Shift indices to align powers before collecting coefficients.

> **Common Misconception**: Students forget to shift indices. Always match the lowest power on both sides!

---

## 3. Worked Examples

### Example 1: $$ y'' + y = 0 $$ about $$ x_0 = 0 $$

**Step 1**: Assume $$ y = \sum_{n=0}^{\infty} a_n x^n $$

**Step 2**: Substitute:
$$y'' = \sum_{n=2}^{\infty} n(n-1)a_n x^{n-2} + y = \sum_{n=0}^{\infty} a_n x^n = 0$$

**Step 3**: Shift first sum: let $$ m = n-2 $$, then $$ n = m+2 $$:
$$ y'' = \sum_{m=0}^{\infty} (m+2)(m+1)a_{m+2} x^m $$

Now equate coefficients for each $$ x^m $$:
$$(m+2)(m+1)a_{m+2} + a_m = 0 \Rightarrow a_{m+2} = -\frac{a_m}{(m+2)(m+1)}$$

**Step 4**: Generate terms:
- $$ a_0 $$ arbitrary $$ \Rightarrow a_2 = -a_0/2 $$, $$ a_4 = a_0/24 $$, ...
- $$ a_1 $$ arbitrary $$ \Rightarrow a_3 = -a_1/6 $$, $$ a_5 = a_1/120 $$, ...

**Step 5**: Write solution:
$$y = a_0\left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots\right) + a_1\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right)$$
$$ = a_0 \cos x + a_1 \sin x $$

> **Checkpoint**: Students can reproduce this recurrence?

### Example 2: Airy Equation $$ y'' - xy = 0 $$

This is $$ y'' - xy = 0 $$. Let $$ y = \sum a_n x^n $$:

$$y'' = \sum_{n=2}^{\infty} n(n-1)a_n x^{n-2} = \sum_{m=0}^{\infty} (m+2)(m+1)a_{m+2} x^m$$

And $$xy = \sum_{n=0}^{\infty} a_n x^{n+1} = \sum_{m=1}^{\infty} a_{m-1} x^m$$

Equating coefficients:
- $$ m = 0 $$: $$ 2a_2 = 0 \Rightarrow a_2 = 0 $$
- For $$ m \geq 1 $$: $$ (m+2)(m+1)a_{m+2} - a_{m-1} = 0 $$

Recurrence: $$ a_{m+2} = \frac{a_{m-1}}{(m+2)(m+1)} $$

This gives solutions in "clusters": $$ a_0 \Rightarrow $$ even powers; $$ a_1 \Rightarrow $$ odd powers. The series diverge (non-analytic at $$ x=0 $$), but this is correct!

---

## 4. Radius of Convergence

### 4.1 Theorem

The series solution converges at least to where the coefficients are analytic.

For $$ y'' + p(x)y' + q(x)y = 0 $$, solution converges for $$ \lvert x - x_0\rvert < R $$ where:
$$ R = \min\{R_p, R_q\} $$

where $$ R_p $$ is radius of analyticity of $$ p $$, $$ R_q $$ of $$ q $$.

### 4.2 Example

$$ y'' + \sin(x)y = 0 $$: coefficients are $$ p = 0 $$, $$ q = \sin x $$ (entire). Solution converges for all $$ x $$ ($$ R = \infty $$).

> **Checkpoint**: Students can determine $$ R $$ for $$ y'' + x^{-1}y = 0 $$? (Singular at $$ x=0 $$, so solution might only converge to...)

---

## 5. Conceptual Questions

1. **Why power series?** $$ \rightarrow $$ Analytic functions are exactly those representable by power series. ODE with analytic coefficients has analytic solutions.

2. **Why does the method work?** $$ \rightarrow $$ Derivatives of $$ x^n $$ produce lower powers, turning ODE into algebraic recurrence. The recurrence encodes the ODE's structure.

3. **What's the limitation?** $$ \rightarrow $$ Only works at ordinary points. At singular points, need Frobenius method.

---

## 6. Application

**Simple harmonic oscillator with polynomial forcing**: $$ y'' + y = x^2 $$

The homogeneous solution is $$ \cos x $$, $$ \sin x $$. For particular solution, assume $$ y_p = Ax^2 + B $$. Substituting gives particular solution, then add homogeneous.

---

## Interactive Activities

### Activity: "Recurrence Challenge" (20 min)

Groups solve different ODEs by series:

| ODE | Recurrence |
|-----|-----------|
| $$ y'' - y = 0 $$ | $$ a_{n+2} = a_n/(n+2)(n+1) $$ |
| $$ y'' + xy = 0 $$ (Airy) | $$ a_{m+2} = a_{m-1}/(m+2)(m+1) $$ |
| $$ y'' + 2y' + y = 0 $$ | $$ a_{n+2} = -2a_{n+1} - a_n $$ divided by appropriate factors |

Each group presents their recurrence and finds first few terms.

---

## Summary

| Step | Action |
|------|--------|
| 1 | Assume $$ y = \sum a_n(x-x_0)^n $$ |
| 2 | Substitute $$ y, y', y'' $$ into ODE |
| 3 | Shift indices to align powers |
| 4 | Collect coefficients of each $$ x^n $$ |
| 5 | Get recurrence for $$ a_n $$ |
| 6 | Determine $$ R $$ from coefficient analyticity |

> **One-Liner**: At ordinary points, substitute power series into ODE, collect like powers, get algebraic recurrence for coefficients—the ODE becomes a counting problem.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Graded-index optics
- Problem: A field amplitude in a smoothly varying medium satisfies an ODE with analytic variable coefficients.
- Model:
$$ y''+x y=0. $$
- Assumptions and limitations: The coefficient must be analytic near the point of expansion.
- Interpretation: If $$ x=0 $$ is an ordinary point, the local solution can be built entirely from a power series.

#### Variable-stiffness engineering model
- Problem: A beam or circuit with gently varying coefficients may not admit elementary solutions.
- Model:
$$ y''+(1+x)y=0. $$
- Assumptions and limitations: The method is local and depends on analyticity of the coefficients.
- Interpretation: Series methods produce a local solution even when no standard closed form exists.

### 2. Additional Intuition and Connections

An ordinary point is where the ODE remains analytically well behaved after being written in standard form. That is why Taylor-type series work naturally there. A common pitfall is to mishandle index shifts after substitution. Another is to forget that the initial conditions determine the first free coefficients.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def ode(t, z):
    y, yp = z
    return [yp, -t * y]

t = np.linspace(0, 2.0, 400)
sol = solve_ivp(ode, [0, 2.0], [1.0, 0.0], t_eval=t)

series = 1 - t**3 / 6 + t**6 / 180

plt.plot(t, sol.y[0], label="numerical")
plt.plot(t, series, "--", label="series truncation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Series versus numerical solution near an ordinary point")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: series solution ordinary point differential equation
- search: Airy equation power series visualization
- search: recurrence coefficients ODE series method

### 5. Worked Example

Consider
$$ y''+x y=0,\qquad
y=\sum_{n=0}^{\infty}a_n x^n. $$
Substitution gives
$$
\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n+\sum_{n=1}^{\infty}a_{n-1}x^n=0.
$$
Hence
$$
a_2=0,\qquad
(n+2)(n+1)a_{n+2}+a_{n-1}=0\quad (n\ge 1).
$$
This is the standard pattern: the differential equation becomes a recurrence for the coefficients.

### 6. Difficulty Layering

**Undergraduate level.** Learn substitution, power matching, and coefficient recurrence.

**Graduate level.** Connect the method to existence theorems for analytic solutions and to the distance to the nearest singular point.

![Ordinary points]({{ site.imgurl }}/chapter_img/chapter06/06_02_series_ordinary_points.svg)

## References

- Boyce & DiPrima, Section 5.2: series solutions at ordinary points
- Tenenbaum & Pollard, *Ordinary Differential Equations*: detailed examples
