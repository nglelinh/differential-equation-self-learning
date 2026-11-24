---
layout: post
title: "03-03 Inverse Laplace Transform"
chapter: '03'
order: 3
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: required
---

Solving an ODE in the $$s$$-domain is the easy half of the journey—you end up with a compact rational expression like $$\frac{3s^2 + 4s + 11}{(s - 1)(s^2 + 4s + 13)}$$. Translating that rational function back into a time-domain trajectory $$y(t)$$ is where algebra meets artistry: partial fractions isolate the real exponential modes, and completing the square isolates the damped oscillations.

## Background Knowledge Map: Four Tools for Inverting Rational Transforms

Every proper rational function $$P(s)/Q(s)$$ yields cleanly to four systematic tools:

1. **Lerch's Uniqueness Theorem:** If two continuous functions on $$[0,\infty)$$ have the same Laplace transform on some half-line $$s > s_0$$, they are identical everywhere—so table-matching produces the *unique* continuous inverse $$\mathcal{L}^{-1}\{F(s)\}$$.
2. **Partial Fraction Decomposition (Factoring $$Q(s)$$ Over $$\mathbb{R}$$):** Linear factors $$(s - r)^m$$ expand into $$\sum_{k=1}^m \frac{A_k}{(s - r)^k}$$ (giving $$t^{k-1}e^{rt}$$), while irreducible quadratic factors $$(s - \alpha)^2 + \beta^2$$ expand into $$\frac{Bs + C}{(s - \alpha)^2 + \beta^2}$$.
3. **Heaviside Cover-Up Shortcut:** For any simple real pole $$s = r$$, the residue $$A$$ in $$\frac{A}{s - r}$$ is computed instantly by covering up $$(s - r)$$ in $$F(s)$$ and evaluating at $$s = r$$: $$A = \lim_{s\to r}(s - r)F(s)$$.
4. **Completing the Square + Numerator Alignment:** For an irreducible quadratic denominator $$(s - \alpha)^2 + \beta^2$$, rewrite the numerator $$Bs + C$$ as $$B(s - \alpha) + \frac{C + B\alpha}{\beta}\cdot\beta$$ so the two pieces invert directly to $$e^{\alpha t}\cos(\beta t)$$ and $$e^{\alpha t}\sin(\beta t)$$.

### Step-by-Step Worked Example (Read Slowly): Inverting a Mixed Linear + Irreducible Quadratic Transform

Find the inverse Laplace transform of
$$F(s) = \frac{3s^2 + 4s + 11}{(s - 1)(s^2 + 4s + 13)}.$$

1. **Check denominator factoring and set up partial fractions:**
   The quadratic $$s^2 + 4s + 13 = (s + 2)^2 + 9$$ has discriminant $$16 - 52 = -36 < 0$$ (irreducible). Write
   $$\frac{3s^2 + 4s + 11}{(s - 1)(s^2 + 4s + 13)} = \frac{A}{s - 1} + \frac{Bs + C}{s^2 + 4s + 13}.$$
2. **Find $$A$$ immediately by Heaviside cover-up at $$s = 1$$:**
   $$A = \left.\frac{3s^2 + 4s + 11}{s^2 + 4s + 13}\right|_{s=1} = \frac{3 + 4 + 11}{1 + 4 + 13} = \frac{18}{18} = 1.$$
3. **Clear denominators to find $$B$$ and $$C$$:**
   $$3s^2 + 4s + 11 = 1(s^2 + 4s + 13) + (Bs + C)(s - 1).$$
   Subtract $$(s^2 + 4s + 13)$$ from both sides:
   $$2s^2 - 2 = (Bs + C)(s - 1) \implies 2(s - 1)(s + 1) = (Bs + C)(s - 1) \implies Bs + C = 2s + 2.$$
   So $$B = 2,\; C = 2$$! (Exact factorization is an instant arithmetic verification.)
4. **Align the numerator $$2s + 2$$ with the shifted denominator $$(s + 2)^2 + 3^2$$:**
   $$2s + 2 = 2(s + 2) - 2 = 2(s + 2) - \frac{2}{3}(3).$$
   Therefore
   $$F(s) = \frac{1}{s - 1} + 2\frac{s + 2}{(s + 2)^2 + 3^2} - \frac{2}{3}\frac{3}{(s + 2)^2 + 3^2}.$$
5. **Invert term by term:**
   $$f(t) = e^t + 2e^{-2t}\cos(3t) - \frac{2}{3}e^{-2t}\sin(3t).$$
   Check at $$t = 0$$: $$f(0) = 1 + 2 - 0 = 3$$, matching the Initial Value Theorem $$\lim_{s\to\infty} sF(s) = 3$$!

## Learning Objectives
This lesson helps students understand the role of the inverse Laplace transform as the step back to the time domain, learn to use partial fraction decomposition for rational expressions, and recognize that solving in the $$ s $$ domain only makes sense when we can read the solution back in time. Students will also practice systematically recognizing patterns from inverse tables.

## Prerequisites
Students need to master the basic Laplace table, partial fraction decomposition skills, and how to read familiar patterns like
$$
\frac{1}{s-a},\qquad \frac{s}{s^2+b^2},\qquad \frac{b}{s^2+b^2}.
$$
This is a lesson at the intersection of rational algebra and dynamical meaning.

## Introduction
![Illustration for Lesson 03-03 Inverse Laplace Transform]({{ site.imgurl }}/chapter_img/chapter03/03_03_inverse_laplace.svg)

The Laplace domain is very convenient for calculations, but humans and physical systems live in the time domain. Therefore, after bringing a problem into the $$ s $$ domain, we must return. Without this, the solution remains merely an algebraic expression that hasn't told the physical story of the system. The inverse Laplace transform is precisely that bridge back.

In this course, we don't delve deeply into the Bromwich integral formula in full generality. Instead, we learn a pragmatic and very powerful version: pattern recognition from tables and partial fraction decomposition. This is how most initial engineering problems are handled.

## Three Ways to Understand the Concept
### Intuitive View
If the Laplace transform compresses a time signal into an algebraic expression, then the inverse transform decompresses it. The poles and coefficients in a rational expression in $$ s $$ correspond to exponential modes, oscillations, or growth in time.

### Visual View
A rational expression like
$$ \frac{1}{s-2} $$
immediately suggests an exponential mode $$ e^{2t} $$. A pattern like
$$ \frac{s}{s^2+9} $$
suggests the oscillation $$ \cos 3t $$. Therefore, taking the inverse Laplace is like reading the time structure hidden in the shape of the rational expression.

### Formal View
If
$$ F(s)=\mathcal{L}\{f(t)\}, $$
then
$$ f(t)=\mathcal{L}^{-1}\{F(s)\}. $$
In early chapter practice, when $$ F(s) $$ is a rational function, we typically:

1. Decompose into a sum of partial fractions.
2. Match each term with the corresponding table formula.
3. Add them together to get the time function.

## Common Misconceptions
- "The inverse transform is just looking up the inverse table." Not enough. Most problems require partial fraction decomposition first.
- "An expression in $$ s $$ has only one unique way to decompose." Wrong. There may be different ways to decompose, but we need to decompose into forms that match the table.
- "If the denominator is quadratic, it always gives sine." Wrong. Need to look at the numerator to distinguish sine, cosine, or a combination of both.
- "Once we get an expression in $$ s $$, the problem is solved." Wrong. Dynamical meaning only appears after returning to the time domain.

## Suggested Learning Sequence
### Step 1: Look at the structure of $$ F(s) $$
See if it's a first-order pattern, second-order, or a product of many factors.

### Step 2: Partial fraction decomposition
Decompose into a sum of terms matching the table.

### Step 3: Match each term with inverse formula
Do this slowly and accurately.

### Step 4: Check by forward Laplace if needed
This is a very good self-checking method.

### Checkpoints
- Do students choose the correct partial fraction form?
- Do students recognize when a numerator of the form $$ As+B $$ is needed for a quadratic denominator?
- Can students interpret the solution back in time?

## Detailed Examples
### Example 1: Simple First-Order Denominator
Compute
$$ \mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\}. $$
From the table:
$$ \mathcal{L}\{e^{3t}\}=\frac{1}{s-3}. $$
Thus
$$
\mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\}=e^{3t}.
$$

### Example 2: Partial Fraction Decomposition
Compute
$$
\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s+2)}\right\}.
$$
We write
$$ \frac{1}{(s-1)(s+2)}=\frac{A}{s-1}+\frac{B}{s+2}. $$
Thus
$$ 1=A(s+2)+B(s-1). $$
Substituting $$ s=1 $$:
$$ 1=3A \Rightarrow A=\frac{1}{3}. $$
Substituting $$ s=-2 $$:
$$ 1=-3B \Rightarrow B=-\frac{1}{3}. $$
Thus
$$
\frac{1}{(s-1)(s+2)}=\frac{1}{3}\frac{1}{s-1}-\frac{1}{3}\frac{1}{s+2}.
$$
Therefore
$$
\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s+2)}\right\}=\frac{1}{3}e^t-\frac{1}{3}e^{-2t}.
$$

### Example 3: Quadratic Trigonometric Pattern
Compute
$$ \mathcal{L}^{-1}\left\{\frac{2}{s^2+4}\right\}. $$
From the formula
$$ \mathcal{L}\{\sin 2t\}=\frac{2}{s^2+4}, $$
we get
$$
\mathcal{L}^{-1}\left\{\frac{2}{s^2+4}\right\}=\sin 2t.
$$

### Example 4: General Numerator on Quadratic Denominator
Compute
$$ \mathcal{L}^{-1}\left\{\frac{s+1}{s^2+9}\right\}. $$
Decompose:
$$
\frac{s+1}{s^2+9}=\frac{s}{s^2+9}+\frac{1}{s^2+9}.
$$
From the table:
$$
\mathcal{L}^{-1}\left\{\frac{s}{s^2+9}\right\}=\cos 3t,
$$
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2+9}\right\}=\frac{1}{3}\sin 3t.
$$
Thus
$$
\mathcal{L}^{-1}\left\{\frac{s+1}{s^2+9}\right\}=\cos 3t+\frac{1}{3}\sin 3t.
$$

## Conceptual Questions
1. Why is partial fraction decomposition a natural intermediate step when taking the inverse Laplace?
2. Why can a quadratic denominator lead to sine, cosine, or a combination of both?
3. What does a simple pole at $$ s=a $$ say about the time behavior of the solution?

## Application Problems
1. In a mechanical system, a rational expression has multiple negative real poles. Explain why this suggests multiple decaying modes in time.
2. An output signal in the Laplace domain has a denominator of the form $$ s^2+b^2 $$. Explain what this says about the system's oscillation.
3. In control, what does looking at the poles of the transfer function tell us about stability before returning to the time domain?

## Interactive Teaching Strategies
- Have students play "reverse translation": look at a rational expression and quickly guess the time solution form.
- Highlight with different colors the partial fraction decomposition terms and their corresponding time functions.
- Give each group a different rational expression to decompose then match with the table.
- Encourage students to check by forward Laplace to increase confidence.

## Learning Differentiation
### Support for Struggling Students
Struggling students should use a comparison table of "pattern in $$ s $$" and "function in $$ t $$". Their problem is usually not the idea, but getting confused among many very similar patterns.

### Challenge for Advanced Students
Advanced students can be asked to handle cases of repeated poles or irreducible quadratics with general linear numerators, then interpret the meaning of each term.

## Memorable Summary
Taking the inverse Laplace is reading time back from the $$ s $$ domain. To do it well, look at the structure of the rational expression, decompose it into familiar pieces, then match with the inverse table. The Laplace domain is only a transit station; the final destination is always the time function.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Recovering time response from the $$ s $$ domain
- Problem: After solving an ODE algebraically in $$ s $$, we must still recover the physical time signal.
- Model:
$$ F(s)\mapsto f(t)=\mathcal{L}^{-1}\{F(s)\}. $$
- Assumptions and limitations: Introductory practice mainly uses rational functions.
- Interpretation: Simple poles become exponentials, quadratic factors become oscillations, and repeated poles produce polynomial factors.

#### Mechanical modal response
- Problem: An expression such as
$$ \frac{1}{(s+1)(s+3)} $$
represents two decaying modes in time.
- Model: Partial fraction decomposition before inverse transform.
- Assumptions and limitations: Constant-coefficient linear models.
- Interpretation: Inverse Laplace is the step where hidden modal structure becomes visible.

#### Circuit signals near resonance
- Problem: Quadratic factors in $$ s $$ must be translated back into sinusoidal time signals.
- Model:
$$
\frac{s}{s^2+\omega^2},\qquad \frac{\omega}{s^2+\omega^2}.
$$
- Assumptions and limitations: Standard oscillatory patterns only.
- Interpretation: The numerator tells us whether we are reading cosine, sine, or a combination.

### 2. Conceptual Insight

Inverse Laplace is where the algebraic work finally becomes physical interpretation. That is why partial fractions matter so much: they decompose the signal into readable time-domain building blocks. This lesson strongly echoes earlier chapters on exponential modes and oscillatory modes.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)
f1 = np.exp(2 * t)
f2 = np.cos(3 * t)
f3 = np.sin(3 * t)

plt.plot(t, f1, label="L^-1{1/(s-2)} = e^{2t}")
plt.plot(t, f2, label="L^-1{s/(s^2+9)} = cos 3t")
plt.plot(t, f3, label="L^-1{3/(s^2+9)} = sin 3t")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("Basic inverse Laplace patterns")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: inverse Laplace transform partial fractions visualization
- search: poles to time response animation
- search: repeated poles exponential response

### 5. Worked Example

Compute
$$
\mathcal{L}^{-1}\left\{\frac{2s+5}{s^2+4s+13}\right\}.
$$
Complete the square:
$$ s^2+4s+13=(s+2)^2+9. $$
Rewrite the numerator:
$$ 2s+5=2(s+2)+1. $$
Then
$$
\frac{2s+5}{(s+2)^2+9}
=2\frac{s+2}{(s+2)^2+9}+\frac{1}{(s+2)^2+9}.
$$
So the inverse transform is
$$ f(t)=2e^{-2t}\cos 3t+\frac{1}{3}e^{-2t}\sin 3t. $$
This is a classic damped oscillatory response.

### 6. Difficulty Layering

**Undergraduate level.** Build confidence with partial fractions and pattern recognition.

**Graduate level.** Read poles, repeated poles, and oscillatory structure directly from rational expressions.

![Inverse Laplace transform]({{ site.imgurl }}/chapter_img/chapter03/03_03_inverse_laplace.svg)

## Video tham khảo

- xem trước: [Partial Fractions and Laplace Inverse | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=D6Rd1K93nSA) — MIT OpenCourseWare, English. Partial fractions and the inverse Laplace transform, the computational heart of this lesson.
- [Laplace: Solving ODE's | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=5av3kiejazQ) — MIT OpenCourseWare, English. See the inverse used immediately to recover y(t) from an algebraic equation.
- [Laplace Transform: Basics | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=BniJM-ireXQ) — MIT OpenCourseWare, English. The forward table this inversion is reading backwards.

## References
- Boyce & DiPrima — *Elementary Differential Equations*: very good for learning inverse Laplace through partial fractions.
- Zill — *Differential Equations with Boundary-Value Problems*: many exercises right at the core of this lesson.
- Ross — *Differential Equations*: concise, clear, suitable for quickly reviewing inverse patterns.
