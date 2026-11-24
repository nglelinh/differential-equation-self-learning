---
layout: post
title: 00-01-01 Continuity and Uniform Continuity
chapter: '00'
order: 2
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Suppose two engineers discretize a temperature profile on a metal rod: near the center the curve is gentle, while near one end it spikes almost vertically. Pointwise continuity promises that at any *single* point you can zoom in far enough to make the function look flat—but uniform continuity promises that a *single* grid spacing $$\delta$$ works simultaneously across the entire domain. That distinction separates local intuition from global error bounds in differential equations.

## Background Knowledge Map: The Hierarchy of Regularity

When analyzing differential equations, continuity is not a single binary property—it is a ladder of progressively stronger controls:

1. **Pointwise Continuity:** For each fixed $$x_0$$ and $$\varepsilon > 0$$, the tolerance $$\delta = \delta(\varepsilon, x_0)$$ may shrink dangerously as $$x_0$$ approaches a boundary or infinity.
2. **Uniform Continuity:** A single $$\delta = \delta(\varepsilon)$$ works uniformly for all pairs $$x, y \in D$$ with $$\lvert x - y \rvert < \delta$$; this guarantees that Cauchy sequences map to Cauchy sequences and Riemann sums converge cleanly.
3. **Heine–Cantor Compactness Principle:** Every continuous function on a closed, bounded interval $$[a,b]$$ is automatically uniformly continuous—which is why local ODE theorems work on compact rectangles $$[t_0-a, t_0+a] \times [y_0-b, y_0+b]$$.
4. **Lipschitz Continuity:** Stronger still than uniform continuity, $$\lvert f(x) - f(y) \rvert \le L\lvert x - y \rvert$$ bounds the maximum secant slope everywhere and is the exact condition guaranteeing unique solutions in Picard–Lindelöf.

### Step-by-Step Worked Example (Read Slowly): Separating Pointwise, Uniform, and Lipschitz Continuity

Compare $$f(x) = x^2$$ on $$\mathbb{R}$$ versus $$f(x) = x^2$$ on $$[0, 3]$$, and contrast with $$g(x) = \sqrt{x}$$ on $$[0, 1]$$:

1. **Why $$f(x) = x^2$$ fails uniform continuity on $$\mathbb{R}$$:**
   Choose $$\varepsilon = 1$$. For any candidate $$\delta > 0$$, pick $$x_n = n$$ and $$y_n = n + \frac{\delta}{2}$$. Then $$\lvert x_n - y_n \rvert = \frac{\delta}{2} < \delta$$, yet
   $$\lvert f(y_n) - f(x_n) \rvert = \left(n + \frac{\delta}{2}\right)^2 - n^2 = n\delta + \frac{\delta^2}{4}.$$
   Choosing $$n > 1/\delta$$ forces $$\lvert f(y_n) - f(x_n) \rvert > 1 = \varepsilon$$. No single $$\delta$$ works globally.
2. **Why $$f(x) = x^2$$ IS Lipschitz (hence uniformly continuous) on $$[0, 3]$$:**
   For all $$x, y \in [0, 3]$$,
   $$\lvert x^2 - y^2 \rvert = \lvert x + y \rvert\,\lvert x - y \rvert \le (3 + 3)\lvert x - y \rvert = 6\lvert x - y \rvert.$$
   Thus $$L = 6$$ works globally on $$[0,3]$$, and $$\delta = \varepsilon / 6$$ certifies uniform continuity.
3. **Why $$g(x) = \sqrt{x}$$ on $$[0, 1]$$ is uniformly continuous yet NOT Lipschitz:**
   Since $$g$$ is continuous on the compact interval $$[0, 1]$$, Heine–Cantor guarantees uniform continuity (in fact $$\lvert \sqrt{x} - \sqrt{y} \rvert \le \sqrt{\lvert x - y \rvert}$$, so $$\delta = \varepsilon^2$$ works). However, taking $$y = 0$$ and $$x > 0$$ gives the secant slope
   $$\frac{\lvert \sqrt{x} - \sqrt{0} \rvert}{\lvert x - 0 \rvert} = \frac{1}{\sqrt{x}} \xrightarrow{x \to 0^+} +\infty,$$
   so no finite Lipschitz constant $$L$$ exists—precisely why the ODE $$y' = \sqrt{y},\; y(0) = 0$$ loses uniqueness!

This lesson introduces the fundamental concepts of continuity and uniform continuity, which are essential for understanding the behavior of functions in optimization.

---

## Continuity and Uniform Continuity

**Continuity** and **Uniform Continuity** are fundamental concepts that describe the behavior of functions, particularly concerning their "smoothness" or "predictability." While closely related, they capture distinct properties, with uniform continuity being a stronger condition than mere continuity.

### Definition of Continuity

A function $$ f: A \to \mathbb{R} $$ is said to be **continuous at a point** $$ c \in A $$ if, for every positive real number $$ \varepsilon > 0 $$, there exists a positive real number $$ \delta > 0 $$ such that for all $$ x \in A $$, if 

$$ \lvert x - c \rvert < \delta $$

then 

$$ \lvert f(x) - f(c) \rvert < \varepsilon $$ 

Intuitively, it means that for any desired level of precision $$ \varepsilon $$ in the output $$ f(x) $$, we can find a sufficiently small interval around $$ c $$ (of width $$ 2\delta $$) such that all $$ x $$ values within this interval map to $$ f(x) $$ values within an $$ \varepsilon $$-interval around $$ f(c) $$. The crucial aspect here is that the choice of $$ \delta $$ generally depends not only on $$ \varepsilon $$ but also on the specific point $$ c $$.

A function is **continuous on a set** $$ A $$ if it is continuous at every point $$ c \in A $$.

**Examples of continuous functions** include all polynomials (e.g., $$ f(x) = x^2 + 3x - 1 $$), trigonometric functions like $$ \sin(x) $$ and $$ \cos(x) $$, and exponential functions $$ e^x $$ on their respective domains. 

### Definition of Uniform Continuity

**Uniform Continuity**, on the other hand, imposes a more stringent condition. A function $$ f: A \to \mathbb{R} $$ is said to be **uniformly continuous on a set** $$ A $$ if, for every positive real number $$ \varepsilon > 0 $$, there exists a positive real number $$ \delta > 0 $$ such that for all $$ x, y \in A $$, if 

$$ \lvert x - y \rvert < \delta $$

then 

$$ \lvert f(x) - f(y) \rvert < \varepsilon $$

The **key distinction** from point-wise continuity lies in the order of quantifiers: for **uniform** continuity, the $$ \delta $$ depends *only* on $$ \varepsilon $$ and is independent of the specific points $$ x $$ and $$ y $$ in the domain.

### Definition of Lipschitz Continuity

**Lipschitz Continuity** provides an even more specific and quantitative notion of continuity. A function $$ f: A \to \mathbb{R} $$ is said to be **Lipschitz continuous** (or **L-Lipschitz**) on a set $$ A $$ if there exists a constant $$ L \geq 0 $$ such that for all $$ x, y \in A $$:

$$\lvert f(x) - f(y) \rvert \leq L \lvert x - y \rvert$$

The smallest such constant $$ L $$ is called the **Lipschitz constant** or **Lipschitz modulus** of $$ f $$.

**Key Properties of Lipschitz Continuity:**

1. **Bounded Rate of Change**: The Lipschitz condition ensures that the function cannot change faster than a linear rate determined by $$ L $$.

2. **Uniform Continuity**: Every Lipschitz continuous function is uniformly continuous (choose $$ \delta = \varepsilon/L $$ for $$ L > 0 $$).

3. **Almost Everywhere Differentiability**: Lipschitz continuous functions are differentiable almost everywhere, and where the derivative exists, $$ \lvert f'(x) \rvert \leq L $$.

**Examples:**
- $$ f(x) = \lvert x \rvert $$ is 1-Lipschitz on $$ \mathbb{R} $$
- $$ f(x) = \sin(x) $$ is 1-Lipschitz on $$ \mathbb{R} $$ (since $$ \lvert \cos(x) \rvert \leq 1 $$)
- $$ f(x) = x^2 $$ is not Lipschitz on $$ \mathbb{R} $$ but is Lipschitz on any bounded interval

### Key Differences and Hierarchy

The three types of continuity form a hierarchy of increasingly strong conditions:

**Continuity ⊆ Uniform Continuity ⊆ Lipschitz Continuity**

1. **Point-wise vs Global**: 
   - **Continuity**: Local property (checked at each point)
   - **Uniform Continuity**: Global property of the entire function
   - **Lipschitz Continuity**: Global property with quantitative bounds

2. **Choice of $$ \delta $$**: 
   - **Continuity**: $$ \delta $$ can depend on both $$ \varepsilon $$ and the specific point $$ c $$
   - **Uniform Continuity**: $$ \delta $$ depends only on $$ \varepsilon $$, working for all points simultaneously
   - **Lipschitz Continuity**: $$ \delta = \varepsilon/L $$ provides explicit relationship

3. **Rate of Change Control**:
   - **Continuity**: No control over rate of change
   - **Uniform Continuity**: Ensures bounded variation over small intervals
   - **Lipschitz Continuity**: Provides explicit linear bound on rate of change

4. **Strength Relationships**: 
   - Every Lipschitz continuous function is uniformly continuous
   - Every uniformly continuous function is continuous
   - The converses are not generally true

### Detailed Examples and Comparisons

**Example 1: $$ f(x) = x^2 $$**
- **On $$ \mathbb{R} $$**: Continuous but not uniformly continuous (rate of change $$ \lvert f'(x) \rvert = 2\lvert x \rvert $$ is unbounded)
- **On $$ [0,1] $$**: Continuous, uniformly continuous, and Lipschitz with $$ L = 2 $$

**Example 2: $$ f(x) = \sin(x) $$**
- **On $$ \mathbb{R} $$**: Continuous, uniformly continuous, and 1-Lipschitz (since $$ \lvert \cos(x) \rvert \leq 1 $$)

**Example 3: $$ f(x) = \lvert x \rvert $$**
- **On $$ \mathbb{R} $$**: Continuous, uniformly continuous, and 1-Lipschitz
- **Note**: Not differentiable at $$ x = 0 $$, but still Lipschitz

**Example 4: $$ f(x) = \sqrt{x} $$**
- **On $$ [0,1] $$**: Continuous and uniformly continuous, but not Lipschitz (derivative unbounded near $$ x = 0 $$)
- **On $$ [a,1] $$ for $$ a > 0 $$**: Lipschitz with $$ L = 1/(2\sqrt{a}) $$

## Video tham khảo

- xem trước: [This is the Epsilon Delta Definition of Continuity | Real Analysis](https://www.youtube.com/watch?v=O98eOlHyWmQ) — Wrath of Math, English. A worked epsilon-delta proof of continuity, which is the definition this lesson asks students to use.
- [Limits, L'Hôpital's rule, and epsilon delta definitions | Chapter 7, Essence of calculus](https://www.youtube.com/watch?v=kfF40MiS7zA) — 3Blue1Brown, Vietnamese. See how a limit, and therefore continuity, is a statement about controlling error with delta.
- [Metric Spaces 8: Cauchy Sequences](https://www.youtube.com/watch?v=UhEaX-uctnM) — Math at Andrews University, English. Cauchy sequences in a metric space, the uniform control of distance behind uniform continuity.
