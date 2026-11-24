---
layout: post
title: "14-05 Composition and Adjoints"
chapter: '14'
order: 5
owner: Course Team
lang: en
categories:
- chapter14
lesson_type: required
---

> **Storytelling Hook:** If multiplying two pseudo-differential operators meant computing four nested oscillatory integrals every time, the theory would be unusable. Instead, the **Moyal–Kohn–Nirenberg asymptotic composition theorem** compresses operator composition into an explicit derivative series on symbols—turning operator algebra into pencil-and-paper differentiation.

## Learning Objectives

This lesson studies composition and adjoint rules in pseudo-differential calculus. Students should understand why operator algebra corresponds to symbolic asymptotics and how adjoints are reflected at the symbol level.

## Prerequisites

Students should know symbols, pseudo-differential operator definitions, and basic operator adjoint ideas.

## Background Knowledge Map: The Symbolic Algebra of Composition and Adjoints

Four structural theorems make $\Psi^*(\mathbb{R}^n) = \bigcup_m \Psi^m$ a closed $*$-algebra modulo smoothing operators:

1. **Asymptotic Composition Formula ($a \# b$):** If $A = a(x,D) \in \Psi^{m_1}$ and $B = b(x,D) \in \Psi^{m_2}$, then $A \circ B \in \Psi^{m_1 + m_2}$ with symbol
   $$(a \# b)(x,\xi) \sim \sum_{\alpha} \frac{1}{\alpha!}\,\partial_\xi^\alpha a(x,\xi)\,D_x^\alpha b(x,\xi).$$
2. **Principal Symbol Homomorphism:** At leading order ($\alpha = 0$), $(a\# b) \equiv a(x,\xi)b(x,\xi) \pmod{S^{m_1+m_2-1}}$. Thus $\Psi\text{DOs}$ commute *to leading order*, and their commutator $[A, B]$ drops by a full order to $\Psi^{m_1+m_2-1}$ with principal symbol $\frac{1}{i}\{a, b\}$!
3. **Formal $L^2$-Adjoint Formula ($a^*$):** The adjoint $A^*$ satisfying $\langle Au, v\rangle_{L^2} = \langle u, A^*v\rangle_{L^2}$ also lies in $\Psi^m$, with asymptotic symbol
   $$a^*(x,\xi) \sim \sum_{\alpha} \frac{1}{\alpha!}\,\partial_\xi^\alpha D_x^\alpha \overline{a(x,\xi)}.$$
4. **Finite Termination for Differential Operators:** Whenever $a(x,\xi)$ is a polynomial in $\xi$ of degree $m$, $\partial_\xi^\alpha a = 0$ for $|\alpha| > m$, so the asymptotic expansion terminates in finitely many terms and becomes an *exact* identity.

## Introduction

![Composition and adjoints]({{ site.imgurl }}/chapter_img/chapter14/05_composition_adjoints.svg)

One of the reasons pseudo-differential operators are so useful is that they support a symbolic algebra. When operators are composed, one can describe the new operator in terms of the symbols of the original ones. Likewise, adjoints have a corresponding symbol-level description.

These rules are what make the calculus operational rather than merely definitional.

## Concept in Three Ways

### Intuitive View

If an operator is encoded by a symbol, then composing operators should correspond to combining their symbolic effects. The result is not usually exact multiplication, but an asymptotic expansion reflecting the interaction of position and frequency dependence.

### Visual View

The symbolic picture of operator composition is like layering frequency-dependent filters whose local behavior interacts with position-dependent modulation.

### Formal View

Composition and adjoint operations correspond to asymptotic symbolic expansions. The leading-order term is often the product or conjugate-transpose analogue of the original symbols, with lower-order correction terms coming from derivatives.

## Why the Topic Matters

Without composition and adjoint rules, pseudo-differential operators would not form a useful working calculus. These rules are the heart of the symbolic machinery needed for parametrices, elliptic regularity, and microlocal analysis.

They also reveal why asymptotic expansions are so central in modern operator theory.

## Common Misconceptions

### "Composition is just symbol multiplication"

Only at leading order. Lower-order corrections usually appear.

### "Adjoints are a minor Hilbert-space detail"

No. They are essential in self-adjointness, energy identities, and spectral theory.

### "Asymptotic expansions are optional refinements"

No. They are fundamental to the full operator algebra.

## Suggested Learning Path

### Step 1: Recall symbol-operator correspondence

Students should begin from the symbol viewpoint.

### Step 2: Motivate why naive multiplication is insufficient

This reveals the role of derivative corrections.

### Step 3: State the asymptotic composition rule

The conceptual structure matters more than every coefficient detail.

### Step 4: Compare with adjoint behavior

This completes the basic operator algebra picture.

### Checkpoints

- Can students explain why composition is more subtle than plain multiplication?
- Do they understand why adjoints have symbolic meaning?
- Can they describe the importance of lower-order correction terms?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Verifying the Composition Formula $a \# b$ on $D_x^2 \circ x^2$

Let $A = D_x^2 = -\frac{d^2}{dx^2}$ (symbol $a(x,\xi) = \xi^2 \in S^2$) and $B = x^2$ (multiplication operator, symbol $b(x,\xi) = x^2 \in S^0$ on compact sets). Compute the symbol of $A \circ B$ using the composition formula $a \# b = \sum_{k=0}^\infty \frac{1}{k!}\partial_\xi^k a\,D_x^k b$, and cross-check by applying $-\frac{d^2}{dx^2}$ directly to $x^2 u(x)$.

1. **Compute the derivatives of $a(\xi) = \xi^2$ and $b(x) = x^2$ (with $D_x = -i\partial_x$):**
   - $k = 0$: $a = \xi^2$, $b = x^2$.
   - $k = 1$: $\partial_\xi a = 2\xi$, $D_x b = -i(2x) = -2ix$.
   - $k = 2$: $\partial_\xi^2 a = 2$, $D_x^2 b = (-i)^2(2) = -2$.
   - $k \ge 3$: $\partial_\xi^k a = 0$ (series terminates!).
2. **Sum the three terms of $a \# b$:**
   $$(a \# b)(x,\xi) = \frac{1}{0!}(\xi^2)(x^2) + \frac{1}{1!}(2\xi)(-2ix) + \frac{1}{2!}(2)(-2) = x^2\xi^2 - 4ix\xi - 2.$$
3. **Cross-check directly in physical space:** Apply $A \circ B = -\frac{d^2}{dx^2}(x^2 \cdot)$ to a smooth function $u(x)$:
   $$-\frac{d}{dx}\big(2x u + x^2 u'\big) = -\big(2u + 4x u' + x^2 u''\big) = x^2\left(-\frac{d^2 u}{dx^2}\right) - 4ix\left(-i\frac{du}{dx}\right) - 2u = (x^2 D_x^2 - 4ix D_x - 2)u.$$
   Every coefficient and sign matches $(a \# b)(x, D)$ identically!

### Example 1: Multiplier Composition

In the pure Fourier multiplier case, composition reduces to straightforward multiplication.

### Example 2: Variable Symbol Interaction

Position dependence creates derivative corrections, showing why the general rule is asymptotic rather than exact.

### Example 3: Leading Symbol of the Adjoint

The adjoint's principal symbol is closely related to the complex conjugate of the original principal symbol.

## Conceptual Questions

1. Why is symbol multiplication only the first approximation to composition?
2. Why are adjoints important in operator theory?
3. Why is asymptotic symbolic structure so useful in PDE analysis?

## Application Problems

1. Why are composition rules essential for constructing parametrices?
2. How do adjoints enter self-adjoint PDE problems?
3. Why is leading-order symbol information often enough for qualitative conclusions?

## Interactive Teaching Strategies

- Compare exact multiplier composition with the variable-symbol case.
- Emphasize principal symbol versus lower-order corrections.
- Use adjoint examples from familiar differential operators.
- Reinforce that operator algebra is symbolic calculus in action.

## Differentiation

### Support for Struggling Students

Students needing support should focus on principal symbols and leading-order intuition before lower-order formulas.

### Challenge for Advanced Students

Advanced students can explore asymptotic symbolic series more explicitly and relate them to commutators.

## Summary

Composition and adjoint rules turn pseudo-differential operators into a genuine symbolic calculus. They are the operational core of the theory and the foundation of later parametrix and microlocal results.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Signal-processing pipelines
- Problem: Real workflows often apply several filters, transforms, and reconstruction steps in sequence.
- Model: If $$ A=\operatorname{Op}(a) $$ and $$ B=\operatorname{Op}(b) $$, then
$$ AB=\operatorname{Op}(a\# b) $$
with a new asymptotic symbol.
- Assumptions and limitations: The full formula is generally an asymptotic expansion, not a finite identity.
- Interpretation: Composition tracks the cumulative effect in phase space.

#### Adjoint operators in inverse problems
- Problem: Imaging and optimization require adjoints to back-propagate residuals and compute gradients.
- Model: If $$ A=\operatorname{Op}(a) $$ then $$ A^*=\operatorname{Op}(a^*) $$ up to lower-order corrections.
- Assumptions and limitations: The underlying Hilbert-space pairing matters.
- Interpretation: The adjoint is the correct dual operator from the energy viewpoint.

### 2. Additional Intuition and Connections

Composition says that symbols also have an algebra, but not just ordinary multiplication because of the noncommuting roles of $$ x $$ and $$ \xi $$. The adjoint answers how the operator looks when moved across an inner product. A common pitfall is to replace $$ a\# b $$ by simple multiplication $$ ab $$ and ignore lower-order corrections.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 512, endpoint=False)
u = np.sin(5 * x) + 0.7 * np.sin(15 * x)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi
uhat = np.fft.fft(u)

a = 1 / (1 + xi**2)
b = xi**2 / (1 + xi**2)
Au = np.fft.ifft(a * uhat).real
BAu = np.fft.ifft(b * np.fft.fft(Au)).real
abu = np.fft.ifft((a * b) * uhat).real

plt.plot(x, BAu, label="B(Au)")
plt.plot(x, abu, "--", label="multiplier ab")
plt.legend()
plt.title("When symbols depend only on frequency, composition simplifies")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: pseudodifferential composition symbol product intuition
- search: adjoint operator imaging inverse problems
- search: noncommutativity phase space symbol calculus

### 5. Worked Example

If $$ a(\xi)=1/(1+\xi^2) $$ and $$ b(\xi)=\xi^2 $$ depend only on $$ \xi $$, then
$$
\operatorname{Op}(a)\operatorname{Op}(b)=\operatorname{Op}(ab).
$$
This is the easiest case. Once symbols depend on both $$ x $$ and $$ \xi $$, derivative correction terms enter the composition law.

### 6. Difficulty Layering

**Undergraduate level.** Understand composition in the pure Fourier-multiplier case.

**Graduate level.** Connect to the Moyal product, symbolic expansions, and adjoint formulas on manifolds.

## Video tham khảo

- xem trước: [Index Theory Lecture 8: Algebra of pseudodifferential operators](https://www.youtube.com/watch?v=uUCQHWHqLCU) — Masoud Khalkhali, English. Products and adjoints in the pseudodifferential algebra.
- [Ps d o’s lecture 2 (Xuwen Zhu)](https://www.youtube.com/watch?v=0OBoX9_-ndQ) — Mathematics video VAROQUI Hervé, Vietnamese. Zhu's second lecture, which reaches the composition calculus.
- [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, Vietnamese. The symbol product that composition is correcting by lower-order terms.

## References

- Trèves: symbolic composition and adjoint theory.
- Taylor: clear discussion of leading-order symbolic rules.
