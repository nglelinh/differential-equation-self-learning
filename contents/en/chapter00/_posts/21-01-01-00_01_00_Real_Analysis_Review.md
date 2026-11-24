---
layout: post
title: "00-01-00 Real Analysis Review"
chapter: '00'
order: 0
owner: Course Team
lang: en
categories:
- chapter00
lesson_type: required
---

Imagine computing the trajectory of a satellite by refining a numerical step size from $$1\text{ s}$$ to $$0.1\text{ s}$$ to $$0.01\text{ s}$$: each refinement produces a new curve, and you want a guarantee that those approximations actually converge to a genuine mathematical solution rather than drifting toward a "hole" in the number line. Real analysis is the precision architecture that turns intuitive calculus into ironclad guarantees of existence, convergence, and stability for differential equations.

## Background Knowledge Map: Why Differential Equations Need Real Analysis

At the graduate level, four analytical pillars quietly power every existence theorem and approximation scheme in this course:

1. **Limits and $$\varepsilon$$–$$\delta$$ Precision:** Local behavior of derivatives and slope fields depends on controlling output error $$\lvert f(x) - L \rvert < \varepsilon$$ via input tolerances $$\lvert x - a \rvert < \delta$$—the exact mechanism behind continuous dependence on initial data.
2. **Cauchy Sequences and Completeness of $$\mathbb{R}$$:** In practice we rarely know the exact limit of an iterative solver (like Picard iteration) in advance; completeness guarantees that if consecutive iterates get arbitrarily close to one another, a limit genuinely exists inside the space.
3. **Compactness and Bolzano–Weierstrass:** Closed and bounded subsets of $$\mathbb{R}^n$$ force bounded sequences to have convergent subsequences and force continuous functions to attain global maxima—crucial for bounding nonlinear vector fields on local rectangles.
4. **Uniform Convergence of Function Sequences:** Passing a derivative or integral inside an infinite series $$\sum f_n(x)$$ fails under mere pointwise convergence; uniform convergence is the gatekeeper for power-series and Picard-iteration solutions.

### Step-by-Step Worked Example (Read Slowly): Proving a Recursive Sequence Is Cauchy and Finding Its Limit

Consider the iteration $$x_{n+1} = \frac{1}{2}\left(x_n + \frac{2}{x_n}\right)$$ starting from $$x_0 = 2$$ (Heron's method for $$\sqrt{2}$$), which mirrors how Picard iteration contracts toward an ODE solution:

1. **Compute the first three iterates by hand:**
   - $$x_0 = 2$$
   - $$x_1 = \frac{1}{2}\left(2 + \frac{2}{2}\right) = \frac{3}{2} = 1.5$$
   - $$x_2 = \frac{1}{2}\left(\frac{3}{2} + \frac{4}{3}\right) = \frac{17}{12} \approx 1.41667$$
   - $$x_3 = \frac{1}{2}\left(\frac{17}{12} + \frac{24}{17}\right) = \frac{577}{408} \approx 1.4142157$$
2. **Establish a lower bound via AM–GM:** For every $$n \ge 1$$,
   $$x_n = \frac{1}{2}\left(x_{n-1} + \frac{2}{x_{n-1}}\right) \ge \sqrt{x_{n-1} \cdot \frac{2}{x_{n-1}}} = \sqrt{2}.$$
3. **Measure the contraction between consecutive terms:**
   $$0 \le x_{n+1} - \sqrt{2} = \frac{x_n^2 - 2\sqrt{2}\,x_n + 2}{2x_n} = \frac{(x_n - \sqrt{2})^2}{2x_n} \le \frac{(x_n - \sqrt{2})^2}{2\sqrt{2}}.$$
4. **Conclude convergence by completeness:** Since $$x_1 - \sqrt{2} < 0.09$$, the error squares at every step ($$< 0.003$$ at $$n=2$$, $$< 3\times 10^{-6}$$ at $$n=3$$). Thus $$\{x_n\}$$ is monotone decreasing and bounded below by $$\sqrt{2}$$, hence Cauchy; by completeness of $$\mathbb{R}$$, $$L = \lim_{n\to\infty} x_n$$ exists and satisfies $$L = \frac{1}{2}(L + 2/L) \implies L = \sqrt{2}$$.

**Quick check:** Notice why completeness of $$\mathbb{R}$$ matters—every iterate $$x_n$$ is rational ($$2, \tfrac{3}{2}, \tfrac{17}{12}, \tfrac{577}{408}$$) and forms a Cauchy sequence in $$\mathbb{Q}$$, yet its limit $$\sqrt{2}$$ does not exist in $$\mathbb{Q}$$!

This lesson reviews essential concepts from real analysis that form the foundation for differential equations.

## Topics to Cover

- Limits and convergence
- Continuity and uniform continuity
- Completeness of $$ \mathbb{R} $$
- Sequences and series

## Key Definitions

**Limit**: A function $$ f(x) $$ approaches $$ L $$ as $$ x \to a $$ if for every $$ \varepsilon > 0 $$, there exists $$ \delta > 0 $$ such that $$ \lvert x - a \rvert < \delta $$ implies $$ \lvert f(x) - L \rvert < \varepsilon $$.

## Video tham khảo

- xem trước: [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, English. Watch the big picture of derivative and limit before using them as the language of change in later ODE chapters.
- [Limits, L'Hôpital's rule, and epsilon delta definitions | Chapter 7, Essence of calculus](https://www.youtube.com/watch?v=kfF40MiS7zA) — 3Blue1Brown, Vietnamese. The epsilon-delta segment is the precise meaning of the limit definition reviewed in this lesson.
- [Cauchy sequences and complete metric spaces, Real Analysis II](https://www.youtube.com/watch?v=m2iG0vR-7fM) — Dr. Bevin Maultsby, English. Cauchy sequences and completeness in a metric space, the setting later used for contraction mappings.

## References

- Boyce & DiPrima, Appendix A
- Brezis, Chapter 1

---

*This is a placeholder lesson. Full content to be developed.*
