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

## Learning Objectives

This lesson studies composition and adjoint rules in pseudo-differential calculus. Students should understand why operator algebra corresponds to symbolic asymptotics and how adjoints are reflected at the symbol level.

## Prerequisites

Students should know symbols, pseudo-differential operator definitions, and basic operator adjoint ideas.

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

## References

- Trèves: symbolic composition and adjoint theory.
- Taylor: clear discussion of leading-order symbolic rules.
