---
layout: post
title: "14-04 Pseudo-Differential Operators: Definition"
chapter: '14'
order: 4
owner: Course Team
lang: en
categories:
- chapter14
lesson_type: required
---

> **Storytelling Hook:** How do you rigorously define the integral $(2\pi)^{-n}\iint e^{i(x-y)\cdot\xi} a(x,\xi) u(y)\,dy\,d\xi$ when $a(x,\xi)$ grows like $|\xi|^m$ so the integrand does not even decay in $\xi$? Through the magic of **oscillatory integrals**—integrating by parts using the phase $e^{i(x-y)\cdot\xi}$ to convert rapid oscillation into rapid decay.

## Learning Objectives

This lesson gives the basic definition of pseudo-differential operators. Students should understand how symbols generate operators through oscillatory integrals and how this extends the familiar action of differential operators and Fourier multipliers.

## Prerequisites

Students should know Fourier transforms, symbols, and the idea of oscillatory representation from the previous lessons.

## Key ideas: Defining $\Psi\text{DOs}$, Pseudolocality, and Sobolev Boundedness

Four core properties establish $\Psi^m(\mathbb{R}^n)$ as a rock-solid class of linear operators:

1. **Oscillatory Integrals and Schwartz Kernels:** Writing $Au(x) = (2\pi)^{-n}\int e^{ix\cdot\xi} a(x,\xi)\hat{u}(\xi)\,d\xi$ is well-defined on $\mathcal{S}(\mathbb{R}^n)$ and extends by duality to $\mathcal{S}'(\mathbb{R}^n)$; its Schwartz kernel $K_A(x,y) = (2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi$ is $C^\infty$ strictly off the diagonal $x = y$.
2. **Pseudolocality (Never Creating New Singularities):** Because $K_A(x,y)$ is smooth for $x \neq y$, $\operatorname{sing\,supp}(Au) \subseteq \operatorname{sing\,supp}(u)$! Even though a $\Psi\text{DO}$ is nonlocal, it can *never* move or invent singularities outside where $u$ was already singular.
3. **Calderón–Vaillancourt & $L^2$ Boundedness:** Every operator $A \in \Psi^0(\mathbb{R}^n)$ with uniformly bounded symbol derivatives is a bounded linear operator $L^2(\mathbb{R}^n) \to L^2(\mathbb{R}^n)$.
4. **Sobolev Mapping Theorem:** Conjugating by $\langle D\rangle^s$ upgrades $L^2$ boundedness to the universal mapping law: every $A \in \Psi^m$ maps $H^s(\mathbb{R}^n) \to H^{s-m}(\mathbb{R}^n)$ continuously for all $s \in \mathbb{R}$.

## Introduction

![Pseudo-differential operator definition]({{ site.imgurl }}/chapter_img/chapter14/04_pdo_definition.svg)

Once symbols have been introduced, the next question is how they actually act on functions. A pseudo-differential operator is the operator associated with a symbol through an oscillatory integral formula. This is the central definition of the chapter.

The importance of the definition is not merely formal. It makes visible how frequency-space information is transported back into physical-space operator action.

## Concept in Three Ways

### Intuitive View

The operator acts by decomposing a function into frequencies, modifying each frequency according to the symbol, and then recombining the result.

### Visual View

The symbol tells how strongly each local frequency component should be amplified, suppressed, or reshaped. The operator then assembles those modified components back into a function.

### Formal View

Given a symbol $$ a(x,\xi) $$, the associated pseudo-differential operator is formally written as an oscillatory integral involving $$ e^{ix\cdot \xi} $$, the symbol, and the Fourier transform of the input. This generalizes both Fourier multipliers and classical differential operators.

## Why the Definition Matters

This definition is the bridge between phase-space description and operator action. Everything that follows in the chapter depends on understanding this construction.

It also explains why pseudo-differential operators are often nonlocal in physical space, even though they remain highly structured in frequency space.

## Common Misconceptions

### "A pseudo-differential operator is just an ordinary differential operator in disguise"

No. It may be genuinely nonlocal and much more flexible.

### "The oscillatory integral formula is only formal notation"

No. It is the core mechanism by which the operator acts.

### "Only smooth functions matter in the definition"

Smooth test settings are the starting point, but the broader theory is built to extend beyond them.

## Suggested Learning Path

### Step 1: Start from Fourier multipliers

Students should first recognize the constant-coefficient special case.

### Step 2: Introduce $$ x $$-dependence

This shows why pseudo-differential operators go beyond pure multipliers.

### Step 3: Interpret the oscillatory formula

The formula should be explained conceptually, not only symbolically.

### Step 4: Compare with classical differential operators

This helps anchor the generalization.

### Checkpoints

- Can students explain how a symbol becomes an operator?
- Do they understand why the result may be nonlocal in physical space?
- Can they identify Fourier multipliers and differential operators as special cases?

## Worked Examples


### Worked example: Evaluating the Fractional Laplacian $(-\Delta)^{1/2}$ as a $\Psi\text{DO}$

Consider the first-order pseudo-differential operator $(-\Delta)^{1/2}$ on $\mathbb{R}$ with symbol $p(\xi) = |\xi|$ (smoothed near $\xi = 0$ if strict $S^1$ membership is required, though exact on nonzero frequencies). Apply $(-\Delta)^{1/2}$ to $u(x) = \cos(3x) + 2\sin(5x)$, and verify that applying it twice reproduces $-u''(x)$.

1. **Decompose $u$ into Fourier exponentials:**
   $$u(x) = \frac{1}{2}\big(e^{3ix} + e^{-3ix}\big) + \frac{2}{2i}\big(e^{5ix} - e^{-5ix}\big).$$
   Its Fourier transform is $\hat{u}(\xi) = \pi\big(\delta(\xi-3) + \delta(\xi+3)\big) - 2\pi i\big(\delta(\xi-5) - \delta(\xi+5)\big)$.
2. **Multiply by the symbol $|\xi|$ and invert the Fourier transform:**
   - At $\xi = \pm 3$: $|\xi| = 3$, multiplying $\cos(3x)$ by $3$.
   - At $\xi = \pm 5$: $|\xi| = 5$, multiplying $2\sin(5x)$ by $5$.
   Therefore:
   $$(-\Delta)^{1/2} u(x) = 3\cos(3x) + 10\sin(5x).$$
3. **Apply $(-\Delta)^{1/2}$ a second time:** Multiplying mode $\pm 3$ by $3$ and mode $\pm 5$ by $5$ again yields:
   $$(-\Delta)^{1/2}\big((-\Delta)^{1/2} u\big)(x) = 9\cos(3x) + 50\sin(5x).$$
4. **Verify against $-u''(x)$:** Differentiating $u(x) = \cos(3x) + 2\sin(5x)$ twice gives $u''(x) = -9\cos(3x) - 50\sin(5x)$, so $-u''(x) = 9\cos(3x) + 50\sin(5x)$—confirming $(-\Delta)^{1/2} \circ (-\Delta)^{1/2} = -\Delta$!

### Example 1: Constant Multiplier Operator

A symbol depending only on $$ \xi $$ gives a Fourier multiplier.

### Example 2: Differential Operator Symbol

Polynomial symbols recover familiar differential operators.

### Example 3: Variable Symbol Prototype

An $$ x $$-dependent symbol illustrates the shift from pure multipliers to general pseudo-differential behavior.

## Conceptual Questions

1. Why does the definition naturally generalize Fourier multipliers?
2. Why can pseudo-differential operators be nonlocal even when their symbols are structured?
3. Why is the symbol-operator correspondence central to the theory?

## Application Problems

1. Why are pseudo-differential operators natural in modern elliptic inversion problems?
2. How does the definition prepare for parametrix construction?
3. Why is frequency-space modification often easier to describe than physical-space action?

## Interactive Teaching Strategies

- Move repeatedly between the symbol picture and the operator picture.
- Compare several concrete special cases.
- Emphasize that the oscillatory integral is the action mechanism, not decorative notation.
- Reinforce that frequency-space algebra becomes operator theory.

## Differentiation

### Support for Struggling Students

Students needing support should focus on Fourier multipliers and polynomial symbols as anchor examples.

### Challenge for Advanced Students

Advanced students can compare different quantization conventions and their symbolic consequences.

## Summary

Pseudo-differential operators are defined by turning symbols into operators through oscillatory integral formulas. This definition unifies Fourier multipliers, differential operators, and much of modern PDE operator theory.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Biomedical imaging and deconvolution
- Problem: A measurement device may distort data in a way that depends on both location and frequency.
- Model:
$$
(\operatorname{Op}(a)u)(x)=\frac{1}{2\pi}\int e^{ix\xi}a(x,\xi)\hat u(\xi)\,d\xi.
$$
- Assumptions and limitations: Linear response is assumed; nonlinear device effects are ignored.
- Interpretation: A ΨDO is a location-dependent frequency filter.

#### Semiclassical quantum mechanics
- Problem: Observables are built from phase-space functions rather than from simple differential expressions.
- Model: Quantize a phase-space function $$ a(x,\xi) $$ into an operator $$ \operatorname{Op}(a) $$.
- Assumptions and limitations: The result depends on the quantization convention.
- Interpretation: This creates a direct bridge from classical symbols to operators.

### 2. Additional Intuition and Connections

The definition says: Fourier transform the function, multiply by a symbol, then transform back, except now the multiplier may vary with position. In short, it is "frequency filtering that changes from place to place." A common pitfall is to treat $$ a(x,\xi) $$ as an auxiliary detail; it is the core object encoding the operator.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 512, endpoint=False)
u = np.sin(6 * x) + 0.5 * np.sin(16 * x)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi

window = 0.6 + 0.4 * np.cos(x - np.pi)
uhat = np.fft.fft(u)
Tu = np.zeros_like(u)
for j, xj in enumerate(x):
    a = 1 / (1 + window[j] * xi**2)
    Tu[j] = np.sum(np.exp(1j * xj * xi) * a * uhat) / len(x)

plt.plot(x, u, label="original")
plt.plot(x, Tu.real, label="Op(a)u")
plt.legend()
plt.title("A symbol depending on both position and frequency")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: pseudodifferential operator definition intuition
- search: local Fourier multiplier visualization
- search: quantization symbol to operator example

### 5. Worked Example

If $$ a(x,\xi)=i\xi $$, we recover the first derivative. If $$ a(x,\xi)=1/(1+\xi^2) $$, we obtain a smoothing operator. These two examples show that the ΨDO definition simultaneously contains differential operators and smoothing filters.

### 6. Difficulty Layering

**Undergraduate level.** Understand the definition through two examples: differentiation and smoothing.

**Graduate level.** Connect to Kohn-Nirenberg quantization, Weyl quantization, and oscillatory kernels.

## Video tham khảo

- xem trước: [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, Vietnamese. The oscillatory-integral definition of a pseudodifferential operator.
- [Index Theory Lecture 8: Algebra of pseudodifferential operators](https://www.youtube.com/watch?v=uUCQHWHqLCU) — Masoud Khalkhali, English. The resulting algebra and its mapping properties.
- [Ps d o’s lecture 2 (Xuwen Zhu)](https://www.youtube.com/watch?v=0OBoX9_-ndQ) — Mathematics video VAROQUI Hervé, Vietnamese. A second pass through the definition.

## References

- Trèves: core definition and interpretation.
- Taylor: accessible treatment of operator quantization.
