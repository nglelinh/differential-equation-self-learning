---
layout: post
title: "06-01 Power Series Review"
chapter: '06'
order: 1
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: required
---

This lesson reviews power series—the technical foundation for all subsequent lessons on series solutions of differential equations.

> **Teaching Notes**: Key prerequisite for Chapter 06. Spend extra time here if students struggle with ratio test for $$ R $$. Activity: "Find the Region" (15 min) where students determine convergence for different series.

---

## Introduction

Power series are the workhorse of series solutions in differential equations. The entire chapter rests on manipulating Taylor-like expansions, differentiating/integrating term-by-term, and determining radii of convergence. Without fluency in these operations, constructing series solutions becomes impossible.

> **Intuitive**: A power series is like a polynomial that goes on forever. Just as a polynomial captures local behavior, a power series captures local behavior of analytic functions—but with infinite precision.

---

## 1. Power Series and Convergence

### 1.1 Definition

A power series about $$ x_0 $$ is:

$$ \sum_{n=0}^{\infty} a_n(x - x_0)^n $$

The **radius of convergence** $$ R $$ determines where the series converges absolutely:
- **Interval**: $$ \lvert x - x_0\rvert < R $$ (always converges)
- **Endpoint behavior**: Must test separately (may converge or diverge)

> **Visual**: Draw the convergence circle in complex plane. Inside = guaranteed convergence. Edge = requires separate test.

### 1.2 Operations Within Radius

Inside $$ \lvert x - x_0\rvert < R $$, we can:

- **Differentiate**: $$\displaystyle \frac{d}{dx}\sum_{n=0}^{\infty} a_n(x-x_0)^n = \sum_{n=1}^{\infty} na_n(x-x_0)^{n-1}$$
- **Integrate**: $$\displaystyle \int \sum_{n=0}^{\infty} a_n(x-x_0)^n\,dx = \sum_{n=0}^{\infty} \frac{a_n}{n+1}(x-x_0)^{n+1} + C$$
- **Add/Subtract**: Combine like powers
- **Multiply by $$ x^k $$**: Shift indices

> **Checkpoint**: Can students find $$ R $$ using ratio test? Differentiate $$ \sum_{n=0}^{\infty} x^n $$?

---

## 2. Finding Radius of Convergence

### 2.1 Ratio Test

For $$ \sum a_n(x - x_0)^n $$, compute:
$$R = \lim_{n \to \infty} \left\vert\frac{a_n}{a_{n+1}}\right\vert$$

**Example**: $$ \sum_{n=0}^{\infty} \frac{x^n}{n!} $$ has $$ a_n = 1/n! $$, so:
$$R = \lim_{n \to \infty} \frac{1/n!}{1/(n+1)!} = \lim_{n \to \infty} (n+1)! = \infty$$

This is $$ e^x $$—entire (converges everywhere).

### 2.2 Root Test

$$R = \frac{1}{\displaystyle \limsup_{n \to \infty} \sqrt[n]{\lvert a_n\rvert}}$$

> **Common Misconception**: Students think $$ R $$ is always determined by the formula. Actually, must compute for each series!

---

## 3. Taylor Series as Local Descriptions

### 3.1 Analytic Functions

If $$ f $$ is analytic at $$ x_0 $$, it equals its own Taylor series:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$$

This means: the coefficients contain ALL local information about $$ f $$. When solving ODEs by series, we exploit this structure.

### 3.2 Why This Matters for ODEs

When we substitute a series ansatz into an ODE, the ODE becomes an algebraic recurrence for coefficients. This is the key: differential equation $$ \rightarrow $$ algebraic recurrence.

> **Intuitive**: Derivatives turn powers into lower powers. The recurrence captures the ODE's structure in the coefficients.

---

## 4. Key Examples

### Example 1: Geometric Series

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n, \quad \lvert x\rvert < 1$$

Differentiating: $$ \frac{1}{(1-x)^2} = \sum_{n=1}^{\infty} n x^{n-1} $$

Integrating: $$ -\ln(1-x) = \sum_{n=1}^{\infty} \frac{x^n}{n} $$

### Example 2: Exponential Series

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}, \quad R = \infty$$

### Example 3: Trigonometric Series

$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \quad \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$

Both have $$ R = \infty $$.

> **Checkpoint**: Students can derive these from their definitions?

---

## 5. Operations Summary

| Operation | Result |
|-----------|--------|
| Differentiate $$ x^n $$ | $$ n x^{n-1} $$ |
| Integrate $$ x^n $$ | $$ \frac{x^{n+1}}{n+1} $$ |
| Shift index | $$\sum_{n=0}^{\infty} a_n x^{n+k} = \sum_{m=k}^{\infty} a_{m-k} x^m$$ |
| Ratio test | $$ R = \lvert a_n/a_{n+1}\rvert $$ as $$ n \to \infty $$ |

---

## 6. Common Errors

| Error | Correction |
|-------|------------|
| Missing factorial in denominator | Check: $$ \sin x $$ series, denominator is $$ (2n+1)! $$ |
| Forgetting endpoint behavior | Test $$ x = \pm R $$ separately |
| Assuming uniform convergence | Only guaranteed inside $$ \lvert x-x_0\rvert < R $$ |
| Differentiating power series term-by-term at endpoint | Not valid at boundary |

> **Common Misconception**: "Power series work everywhere." Only inside radius! At endpoints, must test separately.

---

## Interactive Activities

### Activity: "Find the Region" (15 min)

Given series, students determine convergence region:

| Series | $$ R $$ | Behaviour at $$ x = \pm R $$ |
|--------|-----|-------------------------|
| $$ \sum x^n/n $$ | 1 |Diverges at $$ x = 1 $$, converges at $$ x = -1 $$ (alternating) |
| $$ \sum x^n/n^2 $$ | 1 |Converges at both endpoints |
| $$ \sum n! x^n $$ | 0 |Only at $$ x = 0 $$ |

Groups present their reasoning for each.

---

## Summary

| Concept | Formula | Remember |
|--------|---------|----------|
| Series form | $$ \sum a_n(x-x_0)^n $$ | "Infinite polynomial" |
| Radius | $$ R = \lvert a_n/a_{n+1}\rvert $$ as $$ n \to \infty $$ | Ratio test |
| Differentiate | $$ \sum na_n(x-x_0)^{n-1} $$ | Lower powers |
| Integrate | $$ \sum \frac{a_n}{n+1}(x-x_0)^{n+1} $$ | Higher powers |

> **One-Liner**: Power series are local descriptions of analytic functions; inside their radius, we can differentiate and integrate term-by-term, turning ODEs into algebraic recurrences.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Small-angle mechanics
- Problem: For the nonlinear pendulum
$$ \theta''+\frac{g}{L}\sin\theta=0, $$
we want a workable approximation near equilibrium.
- Model:
$$
\sin\theta=\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\cdots
$$
so the leading approximation becomes
$$ \theta''+\frac{g}{L}\theta\approx 0. $$
- Assumptions and limitations: This is reliable only for small angular displacement.
- Interpretation: Power series connect a nonlinear model to its familiar linear approximation.

#### Early-time engineering response
- Problem: A linear system with analytic forcing near $$ t=0 $$ can be approximated from a few series terms.
- Model:
$$
y''+y=e^t,\qquad
e^t=\sum_{n=0}^{\infty}\frac{t^n}{n!}.
$$
- Assumptions and limitations: The approximation is local in time.
- Interpretation: Series provide a compact local description even before a closed-form solution is written down.

### 2. Additional Intuition and Connections

A power series is an infinite polynomial carrying local information about a function. In this chapter, each derivative in the ODE becomes a relation among coefficients. A common pitfall is to forget that the radius of convergence is not automatically infinite. Another is to lose track of index shifts while differentiating or matching powers.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.2, 1.2, 500)
partial_1 = 1 + x
partial_3 = 1 + x + x**2 + x**3
partial_8 = sum(x**k for k in range(9))
exact = 1 / (1 - x)

plt.plot(x, exact, label="1/(1-x)", color="black")
plt.plot(x, partial_1, "--", label="order 1")
plt.plot(x, partial_3, "--", label="order 3")
plt.plot(x, partial_8, "--", label="order 8")
plt.ylim(-4, 8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Partial sums of the geometric series")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: power series radius of convergence visualization
- search: geometric series partial sums plot
- search: small angle approximation pendulum series

### 5. Worked Example

From
$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n,\qquad \lvert x\rvert<1,
$$
differentiation gives
$$ \frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}n x^{n-1}. $$
This is the simplest example of the chapter's core idea: calculus on the function side becomes algebra on the coefficient side, provided we remain inside the convergence interval.

### 6. Difficulty Layering

**Undergraduate level.** Practice radii of convergence, index shifts, and term-by-term differentiation and integration.

**Graduate level.** Emphasize analyticity, singularities in the complex plane, and how they determine the radius of convergence.

![Power series]({{ site.imgurl }}/chapter_img/chapter06/06_01_power_series_review.svg)

## References

- Boyce & DiPrima, Chapter 5: power series in ODE context
- Ross, Chapter 6: concise operations guide
- Apostol, *Calculus*: rigorous treatment of convergence
