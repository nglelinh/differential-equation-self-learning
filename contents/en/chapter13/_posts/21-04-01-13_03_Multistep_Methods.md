---
layout: post
title: "13-03 Multistep Methods"
chapter: '13'
order: 3
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: required
---

> **Storytelling Hook:** Runge–Kutta methods have short-term amnesia: at every new time step, they throw away all the expensive slope evaluations they just computed and start from scratch. **Linear multistep methods** (Adams–Bashforth, Adams–Moulton, and BDF) remember the past—reusing stored history $(f_n, f_{n-1}, \dots)$ to achieve high order with just **one** new function evaluation per step, at the price of a subtle new danger called parasitic-root instability.

## Learning Objectives

This lesson introduces multistep methods such as Adams-Bashforth and Adams-Moulton schemes. Students should understand how past solution values are reused, why these methods can be efficient, and what new issues arise when several previous steps are involved.

## Prerequisites

Students should know one-step methods, especially Euler and Runge-Kutta methods, and have some familiarity with interpolation ideas.

## Key ideas: Memory, Characteristic Polynomials, and Dahlquist Barriers

Four core ideas govern the theory and practice of linear multistep methods $\sum_{j=0}^k \alpha_j y_{n+j} = h\sum_{j=0}^k \beta_j f_{n+j}$:

1. **Polynomial Interpolation of Past Slopes (Adams Family):** Integrating $y' = f$ over $[t_n, t_{n+1}]$ and replacing $f$ by an interpolating polynomial through past points yields explicit **Adams–Bashforth** (extrapolation) and implicit **Adams–Moulton** (interpolation, often paired as predictor–corrector).
2. **Backward Differentiation Formulas (BDF):** Instead of integrating $f$, differentiating a polynomial interpolating past *solution* values $y_{n+1}, y_n, \dots$ produces BDF1–BDF6, the gold-standard workhorses for stiff ODEs.
3. **Zero-Stability and the Root Condition:** A multistep scheme introduces $k-1$ spurious "parasitic" roots to $\rho(\zeta) = \sum_{j=0}^k \alpha_j \zeta^j = 0$. The method is **zero-stable** iff all roots satisfy $|\zeta| \le 1$ and any root with $|\zeta| = 1$ is simple.
4. **Dahlquist's Stability Barriers:** You cannot have everything at once: (i) the maximum order of a zero-stable $k$-step method is $k+1$ ($k$ odd) or $k+2$ ($k$ even); (ii) no *explicit* multistep method is A-stable, and no A-stable linear multistep method can exceed order $2$ (the trapezoidal rule)!

## Introduction

![Multistep methods]({{ site.imgurl }}/chapter_img/chapter13/03_multistep_methods.svg)

One-step methods use only the current state to compute the next value. Multistep methods go further: they reuse information from several previous steps. This can make them more efficient, because one does not need as many new function evaluations per step.

At the same time, the method becomes more delicate. Starting values are needed, and stability behavior becomes subtler.

## Concept in Three Ways

### Intuitive View

Instead of forgetting the past after each step, a multistep method remembers recent history and uses it to make a better prediction.

### Visual View

If several recent points on the numerical trajectory are known, one can fit an interpolating curve and use it to approximate the next step.

### Formal View

A multistep scheme relates $$ y_{n+1} $$ to several previous values $$ y_n, y_{n-1},\dots $$ and corresponding function evaluations. Explicit families include Adams-Bashforth; implicit families include Adams-Moulton.

## Why the Method Matters

Multistep methods show that memory can be a numerical advantage. They often achieve high accuracy with fewer new evaluations than comparable one-step methods.

They also introduce genuinely new concepts in numerical analysis: zero-stability, starting procedures, and the interaction of recurrence structure with global error.

## Common Misconceptions

### "Using more past points is always better"

No. Longer memory can improve accuracy but may worsen stability or startup complexity.

### "Multistep methods can begin on their own"

Not usually. They require starting values from another method.

### "Explicit and implicit multistep methods differ only in algebraic inconvenience"

No. Stability properties may differ dramatically.

## Suggested Learning Path

### Step 1: Recall one-step limitations

Students should see why reusing past information is attractive.

### Step 2: Introduce interpolation-based intuition

This gives a geometric meaning to the formulas.

### Step 3: Compare explicit and implicit families

Adams-Bashforth and Adams-Moulton are the central examples.

### Step 4: Discuss startup and stability

This distinguishes multistep methods sharply from one-step schemes.

### Checkpoints

- Can students explain why multistep methods need starting values?
- Do they understand why past information may improve efficiency?
- Can they describe one difference between Adams-Bashforth and Adams-Moulton methods?

## Worked Examples


### Worked example: Deriving and Testing 2-Step Adams–Bashforth (AB2)

Derive the 2-step Adams–Bashforth formula from scratch, verify its zero-stability via the root condition, and take one step on $y' = y$ with $h = 0.1$.

1. **Interpolate $f(t, y(t))$ linearly through $(t_n, f_n)$ and $(t_{n+1}, f_{n+1})$:**
   $$P_1(t) = f_{n+1} + \frac{f_{n+1} - f_n}{h}(t - t_{n+1}).$$
2. **Integrate $P_1(t)$ over $[t_{n+1}, t_{n+2}]$:** Substitute $s = (t - t_{n+1})/h \in [0, 1]$ ($dt = h\,ds$):
   $$y_{n+2} - y_{n+1} = \int_{t_{n+1}}^{t_{n+2}} P_1(t)\,dt = h\int_0^1 \big(f_{n+1} + s(f_{n+1} - f_n)\big)\,ds = h\left(f_{n+1} + \frac{1}{2}(f_{n+1} - f_n)\right) = h\left(\frac{3}{2}f_{n+1} - \frac{1}{2}f_n\right).$$
3. **Check zero-stability (the root condition):** The first characteristic polynomial is $\rho(\zeta) = \zeta^2 - \zeta = \zeta(\zeta - 1)$, whose roots are $\zeta_1 = 1$ (simple) and $\zeta_2 = 0$ ($|\zeta_2| < 1$). Thus AB2 is **zero-stable**.
4. **Run one step on $y' = y$ with $h = 0.1$:** Given $y_0 = 1$ ($f_0 = 1$) and exact startup $y_1 = e^{0.1} \approx 1.10517$ ($f_1 = 1.10517$):
   $$y_2 = 1.10517 + 0.1\big(1.5(1.10517) - 0.5(1)\big) = 1.10517 + 0.1(1.15776) = 1.22095.$$
   Compare with $e^{0.2} \approx 1.22140$: the single-step error is just $4.5 \times 10^{-4}$ using only **one** new slope evaluation!

### Example 1: Two-Step Adams-Bashforth

This is the simplest explicit multistep example and shows how recent slopes are combined.

### Example 2: Adams-Moulton Correction

An implicit variant illustrates how multistep formulas can trade simplicity for better stability.

### Example 3: Startup Procedure

A Runge-Kutta method may be used to generate the first few values before the multistep recurrence begins.

## Conceptual Questions

1. Why is memory useful in numerical ODE solving?
2. Why do multistep methods require special startup procedures?
3. Why does recurrence structure make stability analysis more subtle?

## Application Problems

1. Why might a multistep method be more efficient than RK4 in long simulations?
2. Why is zero-stability essential for practical computation?
3. Why do implicit multistep methods often appear in stiff settings?

## Interactive Teaching Strategies

- Compare one-step and multistep methods side by side in terms of information used.
- Use interpolation pictures to motivate the formulas.
- Ask students to trace where each term in a two-step scheme comes from.
- Reinforce the idea that numerical memory changes both efficiency and stability.

## Differentiation

### Support for Struggling Students

Students needing support should work first with two-step examples and clear startup procedures.

### Challenge for Advanced Students

Advanced students can study root conditions for zero-stability or predictor-corrector combinations.

## Summary

Multistep methods use several previous steps to improve efficiency and accuracy. They broaden the numerical toolkit significantly, but also introduce new structural issues such as startup and zero-stability.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Numerical weather prediction
- Problem: Large atmospheric models want to reuse information from previous steps to reduce computational cost.
- Model: Adams-Bashforth or Adams-Moulton methods use
$$ f(t_n,y_n), f(t_{n-1},y_{n-1}), \dots $$
to advance the solution.
- Assumptions and limitations: A startup procedure is required, and stability can be delicate.
- Interpretation: Multistep methods economize on function evaluations after initialization.

#### Long-time circuit simulation
- Problem: Over long runs, many stages per step may become expensive.
- Model: Use BDF or Adams families to balance stability and efficiency.
- Assumptions and limitations: BDF is better for stiff problems; Adams methods are better for smooth nonstiff dynamics.
- Interpretation: Past information becomes a numerical resource for predicting the future.

### 2. Additional Intuition and Connections

Runge-Kutta uses many samples within one step; multistep methods use fewer samples per step but remember several previous states. These are two different numerical philosophies. A common pitfall is to see multistep schemes as merely longer formulas; in fact zero-stability is fundamental.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y
h = 0.25
N = 12
t = np.linspace(0, N * h, N + 1)
y = np.zeros(N + 1)
y[0] = 1.0
y[1] = np.exp(h)  # startup using the exact value to isolate AB2 behavior

for n in range(1, N):
    y[n + 1] = y[n] + h * (1.5 * f(t[n], y[n]) - 0.5 * f(t[n - 1], y[n - 1]))

tt = np.linspace(0, t[-1], 300)
plt.plot(tt, np.exp(tt), label="exact solution")
plt.plot(t, y, "o-", label="Adams-Bashforth 2")
plt.legend()
plt.title("A simple multistep example")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Adams Bashforth Adams Moulton visualization
- search: multistep method zero stability intuition
- search: BDF method stiff ODE animation

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="Adams-Bashforth 2" description="Watch how a multistep method uses both the current slope and the previous slope to advance the numerical solution." path="interactives/chapter13/multistep-methods-en.html" height="620px" %}

### 5. Worked Example

The second-order Adams-Bashforth method is
$$
y_{n+1}=y_n+h\left(\frac{3}{2}f_n-\frac{1}{2}f_{n-1}\right).
$$
It uses the current slope and the previous slope to approximate the integral of the vector field across one step. In practice, this means reusing already computed information instead of resampling the field several times inside each step.

### 6. Difficulty Layering

**Undergraduate level.** Learn Adams-Bashforth and Adams-Moulton through low-order examples.

**Graduate level.** Connect to root conditions, Dahlquist theory, and BDF families.

## Video tham khảo

- xem trước: [Numerical methods for ODEs - Multistep methods - Adams Bashforth](https://www.youtube.com/watch?v=fp6n7x55tkQ) — The Math Guy, English. The Math Guy derives Adams-Bashforth multistep methods.
- [Examples of Adams-Bashforth Methods](https://www.youtube.com/watch?v=JVKBe_vYdg0) — Melvin Leok, English. Melvin Leok works examples of Adams-Bashforth.
- [Runge-Kutta Integrator Overview:  All Purpose Numerical Integration of Differential Equations](https://www.youtube.com/watch?v=HOWJp8NV5xU) — Steve Brunton, English. One-step Runge-Kutta, the method multistep schemes are being compared with.

## References

- Ascher & Petzold: standard treatment of linear multistep methods.
