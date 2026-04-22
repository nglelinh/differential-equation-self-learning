---
layout: post
title: "03-02 Laplace Transform of Elementary Functions"
chapter: '03'
order: 2
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: required
---
## Learning Objectives
This lesson helps students build a Laplace table for basic functions: constants, powers, exponentials, sine, cosine, and simple combinations. The goal is not rote memorization, but understanding the relationship between the shape of functions in the time domain and the structure of rational expressions in the $$ s $$ domain, while learning to use linearity and shifting to quickly derive many new formulas.

## Prerequisites
Students need to master the Laplace definition, integration by parts skills, and basic Euler formulas. This is a lesson in practicing operations but also in building tables from definitions, so understanding the reasoning is more important than remembering results.

## Introduction
![Illustration for Lesson 03-02 Laplace Transform of Elementary Functions]({{ site.imgurl }}/chapter_img/chapter03/03_02_elementary_functions.svg)

To use the Laplace transform as a problem-solving tool, we need a basic vocabulary. That vocabulary is precisely the table of familiar transforms. But if we learn the table as a list of disconnected formulas, students forget very quickly. What is more lasting is recognizing patterns: exponential functions shift the variable $$ s $$, polynomials create powers of $$ 1/s $$, and sine-cosine create quadratic rational patterns.

Therefore, this lesson should be understood as a "table-building" session rather than a "table-copying" session. When students derive the first few formulas from the definition themselves, the remaining formulas become structured and much easier to remember.

## Three Ways to Understand the Concept
### Intuitive View
A slowly growing function like a constant or polynomial will have a Laplace transform with a pole at $$ s=0 $$. An exponential function $$ e^{at} $$ shifts the pole to $$ s=a $$. A sine-cosine oscillation that doesn't grow in amplitude will lead to a quadratic denominator because the second derivative returns to itself.

### Visual View
In the time domain, $$ 1 $$ is a constant level, $$ t $$ grows linearly, $$ e^{at} $$ grows exponentially, and $$ \sin bt $$ oscillates. In the Laplace domain, these very different shapes are transformed into fairly compact rational expressions. This compression is what makes Laplace useful: it gathers temporal behavior into a few poles and simple coefficients.

### Formal View
Some foundational formulas are
$$ \mathcal{L}\{1\}=\frac{1}{s}, $$
$$ \mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}, $$
$$ \mathcal{L}\{e^{at}\}=\frac{1}{s-a}, $$
$$ \mathcal{L}\{\cos bt\}=\frac{s}{s^2+b^2}, $$
$$ \mathcal{L}\{\sin bt\}=\frac{b}{s^2+b^2}. $$
These formulas are sufficient to build most early chapter examples.

## Common Misconceptions
- "Must memorize the entire table immediately." Wrong. Just master the basic patterns and how to derive them.
- "The formulas are random." Wrong. They closely reflect the derivative structure and growth of functions.
- "Sine and cosine are completely different so their formulas aren't related." Wrong. They both connect to the same pattern $$ s^2+b^2 $$.
- "Laplace of polynomials is just notation substitution." Wrong. It comes from repeated integration by parts.

## Suggested Learning Sequence
### Step 1: Rebuild the first few formulas from the definition
Especially $$ 1 $$, $$ e^{at} $$, $$ t $$.

### Step 2: See the pattern for powers
From $$ t $$ to $$ t^n $$ via integration by parts.

### Step 3: Build sine and cosine
Use integration by parts or Euler's formula.

### Step 4: Use linearity and shifting
To create more new formulas from basic ones.

### Checkpoints
- Can students distinguish the effect of parameter $$ a $$ in $$ e^{at} $$ from parameter $$ b $$ in $$ \sin bt $$?
- Do students recognize the pattern $$ n! / s^{n+1} $$?
- Can students derive a simple combination formula without immediately consulting a table?

## Detailed Examples
### Example 1: Laplace of $$ t $$
We compute
$$ \mathcal{L}\{t\}=\int_0^\infty te^{-st}dt. $$
Integration by parts with
$$ u=t,\qquad dv=e^{-st}dt. $$
Thus
$$ du=dt,\qquad v=-\frac{1}{s}e^{-st}. $$
Therefore
$$
\mathcal{L}\{t\}=\left[-\frac{t}{s}e^{-st}\right]_0^\infty+\frac{1}{s}\int_0^\infty e^{-st}dt=\frac{1}{s^2}.
$$

### Example 2: General Pattern for $$ t^n $$
From the above example and repeated integration by parts, we get
$$ \mathcal{L}\{t^2\}=\frac{2}{s^3}, $$
$$ \mathcal{L}\{t^3\}=\frac{6}{s^4}, $$
and generally
$$ \mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}. $$
This example teaches students to recognize patterns rather than recomputing from scratch.

### Example 3: Laplace of Sine and Cosine
With
$$
I=\mathcal{L}\{\sin bt\},\qquad J=\mathcal{L}\{\cos bt\},
$$
we can integrate by parts to obtain a system relating $$ I $$ and $$ J $$, then solve:
$$ I=\frac{b}{s^2+b^2},\qquad J=\frac{s}{s^2+b^2}. $$
The memorable point is that both share the denominator $$ s^2+b^2 $$, reflecting the second-order oscillatory nature of sine-cosine.

### Example 4: Using Exponential Shifting
From
$$ \mathcal{L}\{\cos 2t\}=\frac{s}{s^2+4}, $$
we deduce
$$
\mathcal{L}\{e^{3t}\cos 2t\}=\frac{s-3}{(s-3)^2+4}.
$$
This is a typical example of not needing to recompute the integral from scratch.

## Conceptual Questions
1. Why does the polynomial $$ t^n $$ lead to a high-order pole at $$ s=0 $$?
2. Why does $$ e^{at} $$ simply shift the variable $$ s $$?
3. What does the denominator $$ s^2+b^2 $$ say about the oscillatory nature of sine and cosine?

## Application Problems
1. A harmonic signal in electronics is often written as sine or cosine. Explain why their Laplace formulas are foundational for circuit analysis.
2. A signal that grows exponentially then oscillates, like $$ e^{at}\cos bt $$, might appear in what models and why is shifting by $$ s $$ reasonable?
3. A polynomial in time might describe a gradually increasing input. Explain why its image in the Laplace domain concentrates near $$ s=0 $$.

## Interactive Teaching Strategies
- Have students build the "core" table of 5 formulas before receiving the full table.
- Divide the class into groups: one group handles polynomials, one handles exponentials, one handles trigonometry, then combine results.
- Ask students to explain in words why the formulas for $$ \sin bt $$ and $$ \cos bt $$ are similar in the denominator.
- Organize a quick guessing game: look at a function in time, predict the shape of the rational expression in $$ s $$.

## Learning Differentiation
### Support for Struggling Students
Struggling students should use a summary table with "base function," "formula," "memory pattern." For example: polynomials give powers of $$ 1/s $$, exponentials give shifts, trigonometry gives quadratic denominators.

### Challenge for Advanced Students
Advanced students can be asked to prove the formula for $$ t^n $$ by induction or use parameter differentiation to derive many new formulas from $$ \mathcal{L}\{1\} $$.

## Memorable Summary
To use Laplace effectively, don't just learn the table—learn the patterns. Constants and polynomials give powers of $$ 1/s $$. Exponential functions shift $$ s $$. Sine-cosine create the pattern $$ s^2+b^2 $$. Understanding these three patterns makes most of the Laplace table easy to remember.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Harmonic oscillation
- Problem: A sine or cosine signal from mechanics or circuits must be transformed into the $$ s $$ domain.
- Model:
$$ \sin bt,\qquad \cos bt. $$
- Assumptions and limitations: Single-frequency oscillation with constant amplitude.
- Interpretation: The common denominator $$ s^2+b^2 $$ reflects the second-order nature of oscillation.

#### Exponential growth and decay
- Problem: Population, finance, and radioactive decay all lead to exponential signals.
- Model:
$$ f(t)=e^{at}. $$
- Assumptions and limitations: The growth or decay rate is constant.
- Interpretation: The pole shifts from $$ 0 $$ to $$ a $$, which is a powerful pattern to remember.

#### Ramp testing in control
- Problem: Engineers use step, ramp, and polynomial signals to test systems.
- Model:
$$ 1,\quad t,\quad t^2,\ldots $$
- Assumptions and limitations: Signals are smooth and defined for $$ t\ge 0 $$.
- Interpretation: The pattern $$ n!/s^{n+1} $$ shows that higher polynomial degree means higher pole multiplicity at zero.

### 2. Conceptual Insight

The elementary Laplace table should be learned as a pattern map rather than a list. Time-domain signal classes become pole structures in the $$ s $$ domain. This lesson also quietly prepares students for transfer functions later, where the shape of a rational expression already tells us a great deal about dynamics.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0.5, 6, 500)
L1 = 1 / s
Lt = 1 / s**2
Lsin = 2 / (s**2 + 4)
Lcos = s / (s**2 + 4)

plt.plot(s, L1, label="L{1} = 1/s")
plt.plot(s, Lt, label="L{t} = 1/s^2")
plt.plot(s, Lsin, label="L{sin 2t}")
plt.plot(s, Lcos, label="L{cos 2t}")
plt.xlabel("s")
plt.ylabel("F(s)")
plt.title("Some basic Laplace transforms")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: Laplace table intuition plot
- search: sine cosine Laplace transform visualization
- search: ramp input Laplace transform control

### 5. Worked Example

A standard ramp test input is
$$ f(t)=3t. $$
Using
$$ \mathcal{L}\{t\}=\frac{1}{s^2}, $$
we get
$$ \mathcal{L}\{3t\}=\frac{3}{s^2}. $$
If the same ramp is exponentially damped, for example $$ e^{-2t}t $$, shifting gives
$$ \mathcal{L}\{e^{-2t}t\}=\frac{1}{(s+2)^2}. $$
This is a good reminder that a small set of base formulas can generate many useful transforms.

### 6. Difficulty Layering

**Undergraduate level.** Memorize the core patterns through derivation, not repetition alone.

**Graduate level.** Use parameter differentiation and symbolic structure to derive families of transforms from a few seeds.

![Elementary functions Laplace transform]({{ site.imgurl }}/chapter_img/chapter03/03_02_elementary_functions.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: good for building the Laplace table with reasoning.
- Zill — *Differential Equations with Boundary-Value Problems*: many exercises directly from the definition.
- Ross — *Differential Equations*: concise, suitable for quickly reviewing formula patterns.
