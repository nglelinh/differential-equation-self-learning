---
layout: post
title: "13-02 Runge-Kutta Methods"
chapter: '13'
order: 2
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: required
---

> **Storytelling Hook:** Forward Euler takes one blind glance at the slope at the start of a step and commits to it; to achieve $10^{-8}$ accuracy on a satellite orbit, Euler would need billions of tiny steps. Carl Runge and Wilhelm Kutta discovered a far smarter strategy: sample the slope at carefully weighted midpoint and endpoint probes *inside* each step so that low-order Taylor errors cancel out automatically—without ever computing a single analytical derivative of $f$.

## Learning Objectives

This lesson introduces Runge-Kutta methods as higher-accuracy one-step schemes. Students should understand why multiple slope evaluations improve accuracy, how RK4 is constructed, and why Runge-Kutta methods are the standard workhorses of numerical ODE solving.

## Prerequisites

Students should know Euler's method, local linearization, and the idea of truncation error.

## Background Knowledge Map: Inside Runge–Kutta Stage Design

Four pillars explain how Runge–Kutta (RK) methods achieve dramatic accuracy while remaining single-step:

1. **Quadrature Analogy (Midpoint, Heun, Simpson):** When $f(t,y) = f(t)$ depends only on $t$, RK2 reduces to the trapezoidal or midpoint rule and classical RK4 reduces directly to Simpson's rule $\frac{h}{6}(f_0 + 4f_{1/2} + f_1)$.
2. **Butcher Tableaux and Order Conditions:** An $s$-stage RK method is encoded by nodes $c_i$, stage weights $a_{ij}$, and quadrature weights $b_i$. Matching the Taylor expansion of $y(t_n+h)$ through $O(h^p)$ yields algebraic order conditions—for $p \le 4$, $s = p$ stages suffice, whereas $p = 5$ requires $s = 6$ stages (Butcher barrier).
3. **Embedded Pairs and Adaptive Step Control:** Modern solvers like Dormand–Prince RK45 (`solve_ivp`) compute a 4th- and 5th-order estimate from the *same* stages, using their difference to shrink $h$ near sharp features and stretch $h$ across smooth regions.
4. **Expanded Stability Regions:** For $y' = \lambda y$, classical RK4 has stability polynomial $R(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24}$, expanding the negative real stability interval to $[-2.785, 0]$ and even capturing a segment of the imaginary axis $[-2\sqrt{2}i, 2\sqrt{2}i]$.

## Introduction

![Runge-Kutta methods]({{ site.imgurl }}/chapter_img/chapter13/02_runge_kutta_methods.svg)

Euler's method is simple, but its accuracy is limited. A natural idea is to sample the slope not only at the beginning of the time step, but also at carefully chosen intermediate points. Runge-Kutta methods realize this idea and greatly improve accuracy without requiring higher derivatives.

Among them, RK4 is the most famous. It strikes a practical balance between computational cost and accuracy and is one of the most widely used numerical schemes in scientific computing.

## Concept in Three Ways

### Intuitive View

Instead of trusting a single slope value, we ask the ODE for several slope estimates along the step and combine them intelligently.

### Visual View

Euler's method uses one tangent direction. A Runge-Kutta method samples the vector field several times and averages the information to produce a more faithful step.

### Formal View

Runge-Kutta methods are one-step schemes of the form
$$ y_{n+1}=y_n+h\Phi(t_n,y_n,h), $$
where $$ \Phi $$ is built from several evaluations of $$ f(t,y) $$. In RK4, four slope samples are combined with carefully chosen weights.

## Why the Method Matters

Runge-Kutta methods show that accuracy can be improved systematically without abandoning the one-step framework. They are central both computationally and conceptually.

They also illustrate a major theme in numerical analysis: the design of a good method is a balance between cost, accuracy, and stability.

## Common Misconceptions

### "RK4 is always the best method"

No. It is excellent in many settings, but stiff problems and specialized systems may require different methods.

### "More slope evaluations automatically mean better performance"

Not necessarily. The extra work must justify the accuracy gained.

### "Runge-Kutta methods are just fancy Euler methods"

They are built from the Euler idea, but their structure is significantly more sophisticated.

## Suggested Learning Path

### Step 1: Identify Euler's limitation

Students should first see why one slope sample may be insufficient.

### Step 2: Motivate multiple stage evaluations

This should feel like a natural improvement.

### Step 3: Present a concrete method like RK4

The structure should be emphasized more than memorization.

### Step 4: Compare cost and accuracy

Students should understand the practical tradeoff.

### Checkpoints

- Can students explain why multiple stage slopes improve accuracy?
- Do they know the basic structure of RK4?
- Can they compare Runge-Kutta and Euler conceptually?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Executing One Complete Classical RK4 Step by Hand

Take a single large step $h = 0.5$ of classical 4th-order Runge–Kutta (RK4) on $y' = y$, $y(0) = 1$, and compare the result against the exact value $e^{0.5} \approx 1.6487213$.

1. **Compute the four stage slopes ($f(t,y) = y$, $y_0 = 1$, $h = 0.5$):**
   - Stage 1 (left endpoint): $k_1 = f(0, y_0) = 1$.
   - Stage 2 (first midpoint probe): $k_2 = f\!\left(0.25,\; 1 + \frac{0.5}{2}k_1\right) = 1 + 0.25(1) = 1.25$.
   - Stage 3 (refined midpoint probe): $k_3 = f\!\left(0.25,\; 1 + \frac{0.5}{2}k_2\right) = 1 + 0.25(1.25) = 1.3125$.
   - Stage 4 (right endpoint probe): $k_4 = f(0.5,\; 1 + 0.5 k_3) = 1 + 0.5(1.3125) = 1.65625$.
2. **Form the Simpson-weighted update:**
   $$y_1 = y_0 + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) = 1 + \frac{0.5}{6}(1 + 2.5 + 2.625 + 1.65625) = 1 + \frac{7.78125}{12} = 1.6484375.$$
3. **Verify against the 4th-degree Taylor polynomial of $e^{0.5}$:**
   $$1 + 0.5 + \frac{0.5^2}{2} + \frac{0.5^3}{6} + \frac{0.5^4}{24} = 1 + 0.5 + 0.125 + 0.0208333\dots + 0.0026041\dots = 1.6484375.$$
   It matches to *every* digit! Even with a huge step $h = 0.5$, the error $|e^{0.5} - y_1| \approx 2.84 \times 10^{-4}$ is nearly **1000 times smaller** than one step of forward Euler ($y_1^{\text{Euler}} = 1.5$, error $0.1487$).

### Example 1: RK2 as Improved Euler

A midpoint or improved Euler method shows the first step beyond the basic Euler scheme.

### Example 2: RK4 on an Exponential Problem

For a smooth test equation, RK4 typically performs dramatically better than forward Euler at the same step size.

### Example 3: Cost Comparison

One can compare one RK4 step with four Euler-like evaluations to discuss computational efficiency.

## Conceptual Questions

1. Why does sampling slopes inside the time step improve the approximation?
2. Why is RK4 considered a practical compromise rather than a universal answer?
3. How does one balance accuracy and computational work in method design?

## Application Problems

1. Why are Runge-Kutta methods widely used in scientific simulations?
2. In a smooth nonstiff system, why might RK4 outperform Euler dramatically?
3. Why is method order important when high accuracy is required?

## Interactive Teaching Strategies

- Compare one Euler step with one RK step graphically.
- Ask students to interpret intermediate stage points geometrically.
- Reinforce the idea that method design is guided by error analysis.
- Use RK2 before RK4 to build intuition incrementally.

## Differentiation

### Support for Struggling Students

Students needing support should focus on RK2 and the idea of midpoint slope correction before handling RK4 in full detail.

### Challenge for Advanced Students

Advanced students can explore Butcher tableaux, order conditions, or adaptive step-size ideas.

## Summary

Runge-Kutta methods are the standard higher-accuracy one-step schemes for numerical ODEs. They improve on Euler by using multiple slope evaluations and form one of the central families in practical scientific computation.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Rocket or robot trajectory simulation
- Problem: We need higher accuracy than Euler provides, but want to avoid difficult implicit solves.
- Model: RK4 uses
$$ y_{n+1}=y_n+\frac{h}{6}(k_1+2k_2+2k_3+k_4) $$
with intermediate stages.
- Assumptions and limitations: Each step requires more function evaluations; this alone does not cure stiffness.
- Interpretation: Runge-Kutta improves accuracy by sampling slope information inside the step.

#### Epidemic dynamics
- Problem: Nonlinear systems such as SIR often need accurate medium-term simulation.
- Model: Apply RK2 or RK4 to
$$
S'=-\beta SI,\quad I'=\beta SI-\gamma I,\quad R'=\gamma I.
$$
- Assumptions and limitations: Accuracy still depends on step size; positivity may require care.
- Interpretation: RK methods are the default numerical workhorse before exploiting special model structure.

### 2. Additional Intuition and Connections

If Euler looks at one slope, Runge-Kutta looks at several slopes inside the same step and combines them carefully. This is a way of matching Taylor accuracy without explicitly computing higher derivatives. A common pitfall is to memorize RK4 as a formula without understanding its stage structure and weighted averaging.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y
h = 0.5
N = 8
t = np.linspace(0, N * h, N + 1)
y = np.zeros(N + 1)
y[0] = 1.0

for n in range(N):
    k1 = f(t[n], y[n])
    k2 = f(t[n] + h / 2, y[n] + h * k1 / 2)
    k3 = f(t[n] + h / 2, y[n] + h * k2 / 2)
    k4 = f(t[n] + h, y[n] + h * k3)
    y[n + 1] = y[n] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

tt = np.linspace(0, t[-1], 300)
plt.plot(tt, np.exp(tt), label="exact solution")
plt.plot(t, y, "o-", label="RK4")
plt.legend()
plt.title("Fourth-order Runge-Kutta for y' = y")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Runge Kutta method stage visualization
- search: RK4 vs Euler comparison ODE
- search: Butcher tableau intuition animation

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="RK4 versus Euler" description="Compare Euler and RK4 on the same ODE to see how multiple stages inside one step improve accuracy." path="interactives/chapter13/runge-kutta-en.html" height="620px" %}

### 5. Worked Example

For
$$ y'=y,\qquad y(0)=1,\qquad h=0.5, $$
one RK4 step from $$ t=0 $$ gives
$$
k_1=1,\quad k_2=1.25,\quad k_3=1.3125,\quad k_4=1.65625,
$$
so
$$
y_1 = 1 + \frac{0.5}{6}(1+2(1.25)+2(1.3125)+1.65625)\approx 1.6484,
$$
which is very close to $$ e^{0.5}\approx 1.6487 $$.

### 6. Difficulty Layering

**Undergraduate level.** Compare Euler, midpoint, and RK4 on the same ODE.

**Graduate level.** Connect to order conditions, Butcher tableaux, and SSP methods.

## Video tham khảo

- xem trước: [Runge-Kutta Integrator Overview:  All Purpose Numerical Integration of Differential Equations](https://www.youtube.com/watch?v=HOWJp8NV5xU) — Steve Brunton, English. Brunton's overview of Runge-Kutta as an all-purpose one-step integrator.
- [Coding a Fourth-Order Runge-Kutta Integrator in Python and Matlab](https://www.youtube.com/watch?v=vNoFdtcPFdk) — Steve Brunton, English. A fourth-order Runge-Kutta step written in code.
- [Understanding Runge-Kutta](https://www.youtube.com/watch?v=t48a2M27kjM) — ThatMathThing, English. ThatMathThing explains where the Runge-Kutta stages come from.

## References

- Ascher & Petzold: strong treatment of one-step and Runge-Kutta methods.
