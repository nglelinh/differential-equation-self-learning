---
layout: post
title: "Weak Derivatives"
chapter: '12'
order: 2
owner: Lê Minh Hoàng
lang: en
categories:
- chapter12
lesson_type: required
---

> **Storytelling Hook:** Pluck a guitar string at its midpoint and release it: at the instant of release, the string forms a sharp triangular tent with a corner right in the middle. Classical calculus throws up its hands—no derivative exists at the tip! Yet the string has finite elastic tension and obeys the wave equation effortlessly. **Weak derivatives** resolve this paradox by shifting differentiation onto infinitely smooth test functions via integration by parts.

![Weak derivatives understood through integration by parts]({{ site.imgurl }}/chapter_img/chapter12/02_weak_derivatives.svg )

## Objectives

This lesson explains why weak derivatives are needed, how they are defined using test functions, and why they mark the decisive shift from classical calculus to modern PDE. After the lesson, students should be able to compute basic weak derivatives and explain how weak differentiation is connected to integration by parts and weak solutions.

## Prerequisites

Students should know classical derivatives, integration by parts, smooth compactly supported test functions, and the idea of working with integrals rather than pointwise values. Some familiarity with $$ L^1_{\mathrm{loc}} $$ is also helpful because weak derivatives do not require classical smoothness.

## Key ideas: Extending Differentiation Beyond Smooth Functions

Weak derivatives generalize calculus without sacrificing rigor by resting on four pillars:

1. **Smooth Compactly Supported Test Functions $C_c^\infty(\Omega)$:** Test functions vanish near $\partial\Omega$, killing all boundary terms in integration by parts and isolating the interior behavior of $u$.
2. **Integration by Parts as a Definition:** We call $v \in L^1_{\text{loc}}(\Omega)$ the $\alpha$-th weak derivative of $u \in L^1_{\text{loc}}(\Omega)$ if $\int_\Omega u\,D^\alpha \varphi\,dx = (-1)^{|\alpha|}\int_\Omega v\,\varphi\,dx$ for every $\varphi \in C_c^\infty(\Omega)$.
3. **Uniqueness Almost Everywhere:** By the Fundamental Lemma of the Calculus of Variations, if two locally integrable functions $v_1, v_2$ satisfy the weak-derivative identity for all $\varphi \in C_c^\infty(\Omega)$, then $v_1 = v_2$ a.e.
4. **Kinks Survive, Jumps Break:** In 1D, continuous piecewise-$C^1$ functions (kinks like $|x|$) possess weak derivatives in $L^1_{\text{loc}}$, whereas jump discontinuities (like the Heaviside step) produce boundary leftovers that no $L^1_{\text{loc}}$ function can represent—requiring distributions instead.

## Introduction

Many natural solutions in analysis are not smooth. They may have corners, kinks, or abrupt changes. If we insist on classical derivatives only, then we are forced to say that such functions "have no derivative" and therefore cannot solve a differential equation. That viewpoint is too rigid for PDE.

The idea of a weak derivative is to stop looking for the derivative directly on the function itself. Instead, we observe how the function interacts with smooth test functions. Integration by parts moves the derivative onto the test function. If that identity still holds, then we say that the derivative exists in a weaker sense.

## The Concept in Three Ways

### Intuitive View

Imagine a road with a sharp corner. If you stand exactly at the corner, the slope is undefined. But if you look at a small neighborhood around the corner, you can still detect the average directional change of the road. A weak derivative records that averaged change when the function is examined through smooth probes.

### Visual View

The function $$ u(x)=\lvert x\rvert $$ is the standard picture. At $$ x=0 $$, the classical derivative fails because the graph changes direction abruptly. Yet the slope is $$ -1 $$ on the left and $$ 1 $$ on the right, and that information survives very stably when multiplied by a smooth test function and integrated.

Another useful board picture is the slogan "move the derivative onto the test function." That is the visual core of weak differentiation and later of weak formulations of PDE.

### Formal View

Let $$ u\in L^1_{\mathrm{loc}}(\Omega) $$. We say that $$ v\in L^1_{\mathrm{loc}}(\Omega) $$ is the weak derivative of $$ u $$ with respect to $$ x_i $$ if

$$
\int_\Omega u\,\partial_i\varphi\,dx=-\int_\Omega v\,\varphi\,dx
\qquad \forall \varphi\in C_c^\infty(\Omega).
$$

We then write $$ v=\partial_i u $$ in the weak sense.

If $$ u\in C^1(\Omega) $$, ordinary integration by parts shows that the weak derivative agrees with the classical derivative, so the new definition is a consistent extension.

## Common Misconceptions

### "A weak derivative is only an approximation"

False. It is not a vague or approximate object. It is a mathematically exact definition that uses a different viewpoint.

### "If a function has no classical derivative, then it cannot have a weak derivative"

False. Functions such as $$ \lvert x\rvert $$ or $$ x_+ $$ are basic examples showing the power of the weak notion.

### "Weak derivatives are only a technical trick"

No. They are the foundation of Sobolev spaces, weak solutions, variational methods, and modern PDE.

### "A weak derivative must be defined pointwise everywhere"

No. It is defined almost everywhere, which matches the nature of integral spaces.

## Learning Progression

### Step 1: Review integration by parts

In the smooth case,

$$ \int u\,\varphi'=-\int u'\varphi $$

if boundary terms vanish. This identity is the starting point.

### Step 2: Replace pointwise differentiation by testing

Rather than asking for a derivative at each point, ask whether there is a function $$ v $$ that makes the testing identity true for every smooth compactly supported $$ \varphi $$.

### Step 3: Compare with classical derivatives

Students should see that whenever a classical derivative exists, it is also the weak derivative.

### Step 4: Practice piecewise-smooth examples

Corners and kinks are the right place to build intuition because they show exactly why the weak framework is needed.

### Key Checkpoints

- Can students explain why integration by parts motivates the definition?
- Can they compute the weak derivative of a basic nonsmooth function?
- Can they say why weak differentiation is the right language for PDE?

## Worked Examples


### Worked example: Why $|x|$ Has a Weak Derivative While the Step Function Does Not

Test both $u(x) = |x|$ and the Heaviside step $H(x) = \mathbf{1}_{(0,1)}(x)$ on $\Omega = (-1,1)$ against an arbitrary test function $\varphi \in C_c^\infty(-1,1)$.

1. **Compute $\int_{-1}^1 |x|\varphi'(x)\,dx$ by splitting at the corner $x = 0$:**
   $$\int_{-1}^1 |x|\varphi'(x)\,dx = \int_{-1}^0 (-x)\varphi'(x)\,dx + \int_0^1 x\varphi'(x)\,dx.$$
   Integrate each piece by parts, remembering $\varphi(-1) = \varphi(1) = 0$:
   $$= \big[-x\varphi(x)\big]_{-1}^0 + \int_{-1}^0 \varphi(x)\,dx + \big[x\varphi(x)\big]_0^1 - \int_0^1 \varphi(x)\,dx = 0 + \int_{-1}^0 \varphi(x)\,dx + 0 - \int_0^1 \varphi(x)\,dx.$$
   Combining the two integrals gives:
   $$\int_{-1}^1 |x|\varphi'(x)\,dx = -\int_{-1}^1 \operatorname{sgn}(x)\varphi(x)\,dx.$$
   Since $v(x) = \operatorname{sgn}(x) \in L^1_{\text{loc}}(-1,1)$, $u' = \operatorname{sgn}(x)$ is the exact weak derivative of $|x|$! Notice that the boundary terms at $x=0$ vanished because $|x|$ is continuous there.
2. **Now test the step function $H(x) = \mathbf{1}_{(0,1)}(x)$:**
   $$\int_{-1}^1 H(x)\varphi'(x)\,dx = \int_0^1 \varphi'(x)\,dx = \varphi(1) - \varphi(0) = -\varphi(0).$$
   Suppose for contradiction that some $g \in L^1_{\text{loc}}(-1,1)$ satisfied $\int_{-1}^1 g(x)\varphi(x)\,dx = \varphi(0)$ for all $\varphi \in C_c^\infty(-1,1)$. Choosing a sequence of smooth bumps $\varphi_n$ supported in $(-1/n, 1/n)$ with $0 \le \varphi_n \le 1$ and $\varphi_n(0) = 1$, the right-hand side stays fixed at $1$, whereas the left-hand side satisfies $\left|\int_{-1/n}^{1/n} g\varphi_n\,dx\right| \le \int_{-1/n}^{1/n} |g(x)|\,dx \to 0$ by dominated convergence—a contradiction! Thus $H$ has no weak derivative in $L^1_{\text{loc}}$.

### Example 1: A smooth function

Let $$ u(x)=x^2 $$ on an interval. The classical derivative is $$ u'(x)=2x $$. For any test function $$ \varphi $$,

$$ \int u\,\varphi'=-\int 2x\,\varphi. $$

So the weak derivative is exactly the classical derivative.

### Example 2: The function $$ u(x)=\lvert x\rvert $$

For $$ x\neq 0 $$, the slope is $$ -1 $$ on the left and $$ 1 $$ on the right. The weak derivative is therefore

$$
u'(x)=
\begin{cases}
-1,&x<0,\\
1,&x>0,
\end{cases}
$$

which can be written as $$ \operatorname{sgn}(x) $$ almost everywhere. The point $$ x=0 $$ does not matter because one point has measure zero.

### Example 3: The positive-part function

Let $$ x_+=\max\{x,0\} $$. Then the weak derivative is

$$
\partial_x x_+=
\begin{cases}
0,&x<0,\\
1,&x>0,
\end{cases}
$$

or simply the indicator of the positive half-line almost everywhere.

### Example 4: Why corners are allowed

Consider a piecewise linear function that changes slope at one interior point. The classical derivative fails at the breakpoint, but the derivative exists away from it and is locally integrable. That piecewise-defined slope is the weak derivative. This shows that weak derivatives naturally allow finitely many corners.

## Conceptual Questions

1. Why does moving the derivative onto a test function make sense when the original function is not smooth?
2. Why does a failure at a single point not prevent the existence of a weak derivative?
3. Why is the weak derivative the right stepping stone toward weak solutions of PDE?

## Application Problems

1. In mechanics, if a displacement profile has a corner but still has finite energy, why is weak differentiation more natural than classical differentiation?
2. In image processing, why might an edge be modeled more naturally with weak derivatives than with classical ones?
3. In PDE, why is it useful to define derivatives through test functions when the solution itself may be rough?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What exactly breaks down for the classical derivative of $$ \lvert x\rvert $$ at the origin?
- Why does one bad point not destroy an integral identity?
- If a function has a corner but no jump, what kind of derivative should you expect?

### Suggested Activities

- Ask students to compute the weak derivative of $$ \lvert x\rvert $$ and $$ x_+ $$.
- Put classical differentiation on one side of the board and weak differentiation on the other, then connect them through integration by parts.
- Let groups create their own piecewise linear example and identify its weak derivative.

### Participation Moves

- Start with a graph before any formulas.
- Ask students to explain the definition in everyday language before writing symbols.
- Invite students to compare what is lost and what is preserved when moving from classical to weak derivatives.

## Differentiation

### Support for Struggling Students

- Stay in one dimension at first.
- Use simple piecewise linear and absolute-value examples.
- Emphasize the slogan "differentiate the test function instead of the rough function."

### Challenge for Advanced Students

- Prove uniqueness of weak derivatives up to equality almost everywhere.
- Explore the relation between weak derivatives and distributions.
- Find a function with a distributional derivative that is not given by an $$ L^1_{\mathrm{loc}} $$ function.

## Quick Summary

A weak derivative records how a function changes when tested against smooth probes. It extends classical differentiation in exactly the way needed for Sobolev spaces, variational methods, and weak solutions of PDE.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Mechanics with kinks
- Problem: A bar or string may have a continuous displacement but a broken slope at one point.
- Model: Weak derivatives let us interpret the displacement $$ u $$ even when the classical derivative fails at some points.
- Assumptions and limitations: The function must still be integrable enough to pair with test functions.
- Interpretation: Weak differentiation preserves the correct global physics even when pointwise differentiability breaks down.

#### Variational image processing
- Problem: Image edges are sharp transitions, so classical derivatives easily fail there.
- Model: One works with weak or distributional derivatives of the image intensity.
- Assumptions and limitations: The image is modeled as a continuous or finely sampled function.
- Interpretation: Weak derivatives capture edges without demanding perfect smoothness.

### 2. Additional Intuition and Connections

A weak derivative does not compute pointwise slopes directly. Instead, it asks whether integration by parts remains valid against every smooth compactly supported test function. A common misconception is that weak derivatives are somehow less exact; in reality they are the right language for broader and more realistic function classes.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 600)
u = np.abs(x)
weak_du = np.sign(x)
weak_du[np.abs(x) < 1e-12] = 0.0

plt.plot(x, u, label="u(x)=|x|")
plt.plot(x, weak_du, label="approximate weak derivative")
plt.legend()
plt.title("A function with a corner can still have a weak derivative")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: weak derivative absolute value visualization
- search: image edges weak derivatives variational methods
- search: distributional derivative Heaviside function

### 5. Worked Example

For
$$ u(x)=\lvert x\rvert $$
on $$ (-1,1) $$, the classical derivative does not exist at $$ x=0 $$. However, the weak derivative is
$$ u'(x)=\operatorname{sgn}(x) $$
in the sense that
$$
\int_{-1}^1 \lvert x\rvert \varphi'(x)\,dx = -\int_{-1}^1 \operatorname{sgn}(x)\varphi(x)\,dx
$$
for every $$ \varphi \in C_c^\infty(-1,1) $$.

### 6. Difficulty Layering

**Undergraduate level.** Understand why cornered functions can still have weak derivatives.

**Graduate level.** Connect to distributions, BV functions, traces, and compactness arguments.

## Video tham khảo

- xem trước: [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, English. Weak derivatives, W^{1,p}, and H^1 explained in one lecture.
- [UPB Math 237 LEC5A Sobolev Spaces](https://www.youtube.com/watch?v=GhBM6L-avYU) — Gilbert Peralta, English. A university lecture developing Sobolev spaces from the weak derivative.
- [Lec 36 Sobolev lemma](https://www.youtube.com/watch?v=ln4N51019qk) — NPTEL - Indian Institute of Science, Bengaluru, English. NPTEL on the Sobolev lemma, the regularity gain weak derivatives can give.
