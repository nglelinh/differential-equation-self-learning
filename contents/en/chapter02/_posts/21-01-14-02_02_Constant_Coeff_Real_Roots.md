---
layout: post
title: "02-02 Constant Coefficients: Distinct Real Roots"
chapter: '02'
order: 2
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: required
---
## Learning Objectives
This lesson helps students use the characteristic equation to solve second-order linear ODEs with constant coefficients, recognize the difference between distinct real roots and repeated roots, and interpret exponential modes as growth or decay components of the system. This is the foundational technical step for the entire chapter.

## Background Knowledge
Students need to grasp the principle of superposition, knowledge of exponential functions and the derivative of $$ e^{rt} $$. Familiarity with the "try a solution form and verify" approach from the previous chapter will make the characteristic equation appear as a very natural idea.

## Introduction
![Diagram for Lesson 02-02 Constant Coefficients: Distinct Real Roots]({{ site.imgurl }}/chapter_img/chapter02/02_02_constant_coeff_real_roots.svg)

When the coefficients of an equation are constant, we have a major advantage: differentiation does not change the nature of the exponential function. Therefore, if the model has the form
$$ ay''+by'+cy=0, $$
we have a basis to try
$$ y=e^{rt}. $$
This is one of the most beautiful moments in applied analysis: a continuous differential problem is transformed into a discrete algebraic problem via the characteristic polynomial.

More important than the formula is how to interpret the meaning of solutions. Two distinct real roots give two independent modes, typically two different growth or decay rates. A repeated root shows that the system has mode coincidence and requires an additional solution of the form $$ te^{rt} $$. This lesson is thus both about solution technique and about understanding solution structure.

## Three Ways to Understand the Concept
### Intuitive View
Imagine the system has two different "response rhythms." One mode may decay quickly, the other slowly. The general solution is a mixture of both. If the two rhythms coincide, the system loses an independent direction and we must find an additional special mode to compensate.

### Visual View
With negative real roots, graphs typically decay to zero. With positive real roots, graphs explode. If one root is positive and one negative, behavior is usually dominated long-term by the positive mode. When a repeated root appears, the graph still looks like an exponential but has an additional $$ t $$ factor that changes the transition rate.

### Formal View
Consider the homogeneous equation
$$ ay''+by'+cy=0,\qquad a\neq 0. $$
Trying the solution
$$ y=e^{rt} $$
we obtain
$$ ar^2+br+c=0. $$
This is the characteristic equation. If there are two distinct real roots $$ r_1\neq r_2 $$, the general solution is
$$ y(t)=c_1e^{r_1t}+c_2e^{r_2t}. $$
If there is a repeated root $$ r $$, the general solution is
$$ y(t)=\left(c_1+c_2t\right)e^{rt}. $$

## Common Misconceptions
- "The characteristic equation is just a memorization trick." Wrong. It comes directly from the fact that exponentials are a closed family under differentiation.
- "A repeated root only gives one solution $$ e^{rt} $$ so the problem cannot be solved." Wrong. We also have a second independent solution $$ te^{rt} $$.
- "Just solve the characteristic equation and you're done." Not sufficient. We must also apply initial conditions and interpret solution behavior.
- "The sign of the characteristic root does not matter." Wrong. It determines whether the system grows, decays, or approaches equilibrium.

## Suggested Learning Progression
### Step 1: Write the characteristic equation
Transform the ODE into a polynomial in $$ r $$.

### Step 2: Classify characteristic roots
Determine whether there are two distinct real roots or a repeated root.

### Step 3: Write the general solution in correct form
This is the step where students most often make mistakes with repeated roots.

### Step 4: Use initial conditions
Find the constants and identify the long-term dominant mode.

### Checkpoints
- Can the student write the characteristic polynomial correctly?
- Can the student distinguish between distinct and repeated roots?
- Can the student interpret long-term behavior from the signs of the roots?

## Worked Examples
### Example 1: Two Distinct Real Roots
Solve
$$ y''-3y'+2y=0. $$
The characteristic equation is
$$ r^2-3r+2=0, $$
which factors as
$$ \left(r-1\right)\left(r-2\right)=0. $$
Therefore
$$ r_1=1,\qquad r_2=2. $$
General solution:
$$ y(t)=c_1e^t+c_2e^{2t}. $$
Since both characteristic roots are positive, every nontrivial solution grows as $$ t $$ increases.

### Example 2: Applying Initial Conditions
With the same equation, suppose
$$ y(0)=4,\qquad y'(0)=5. $$
We have
$$ y(0)=c_1+c_2=4. $$
On the other hand
$$ y'(t)=c_1e^t+2c_2e^{2t}, $$
so
$$ y'(0)=c_1+2c_2=5. $$
Subtracting the two equations:
$$ c_2=1,\qquad c_1=3. $$
Thus
$$ y(t)=3e^t+e^{2t}. $$
As $$ t\to \infty $$, the mode $$ e^{2t} $$ dominates.

### Example 3: Repeated Root
Solve
$$ y''-4y'+4y=0. $$
The characteristic equation:
$$ r^2-4r+4=0=\left(r-2\right)^2. $$
We have a repeated root $$ r=2 $$. Therefore the general solution is
$$ y(t)=\left(c_1+c_2t\right)e^{2t}. $$
Many students make the mistake of writing only $$ c_1e^{2t}+c_2e^{2t} $$, but these two terms are not linearly independent.

### Example 4: Decaying Solution
Solve
$$ y''+5y'+6y=0. $$
The characteristic equation:
$$ r^2+5r+6=0, $$
gives
$$ r=-2,\qquad r=-3. $$
Thus
$$ y(t)=c_1e^{-2t}+c_2e^{-3t}. $$
Both modes decay to zero, so the system is stable in the sense that solutions approach equilibrium at zero. The mode $$ e^{-2t} $$ decays more slowly and dominates long-term.

## Conceptual Questions
1. Why is it particularly reasonable to try $$ e^{rt} $$ when coefficients are constant?
2. Why does a repeated root require a second solution of the form $$ te^{rt} $$?
3. From the sign of the characteristic roots, what can we read about stability or growth of the system?

## Application Problems
1. A mechanical system has two damping modes with different rates. Explain why the more slowly decaying mode determines long-term behavior.
2. In a population growth model linearized around equilibrium, what does a positive characteristic root suggest about stability?
3. An electrical signal has two exponential transient components. Explain why the component with smaller decay rate will be observed longer.

## Interactive Teaching Strategies
- Have students predict the graph shape from characteristic roots without solving in detail.
- Ask the class to compare two problems—one with distinct real roots, one with repeated roots—and describe in words what the real difference is.
- Have students do a quick matching exercise between characteristic equations and corresponding solution forms.
- Ask the class: "If one characteristic root is negative and one positive, what do you predict happens as $$ t $$ grows?"

## Differentiation
### Support for Struggling Students
Provide students with a fixed procedure table: write characteristic equation, solve quadratic, classify roots, choose general solution form. Practicing this structured repetition helps reduce formal errors.

### Challenge for Advanced Students
Advanced students can be asked to prove directly that $$ te^{rt} $$ is a solution when $$ r $$ is a repeated root, or to relate the multiplicity of characteristic roots to the number of independent solutions needed.

## Memorable Summary
For second-order constant-coefficient homogeneous ODEs, the key is to try $$ e^{rt} $$ to transform to a characteristic equation. Two distinct real roots give two independent exponential modes. A repeated root gives the form $$ \left(c_1+c_2t\right)e^{rt} $$. The sign of the characteristic roots indicates whether the system grows or decays.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Overdamped mechanical return
- Problem: A door closer or shock absorber returns to equilibrium without oscillation.
- Model:
$$ m x''+c x'+k x=0,\qquad c^2>4mk. $$
- Assumptions and limitations: Small motion, linear restoring force, and constant damping.
- Interpretation: Two distinct negative real roots create two decay rates, and the slower one dominates long-term behavior.

#### Electrical signal with two time scales
- Problem: A second-order filter may show two transient exponential components after a disturbance.
- Model:
$$ y''+a y'+b y=0. $$
- Assumptions and limitations: Constant coefficients and linear behavior around the operating point.
- Interpretation: The characteristic roots reveal two distinct memory scales.

#### Linearized biological or economic stability
- Problem: Near equilibrium, a nonlinear model may reduce to a constant-coefficient linear equation.
- Model:
$$ y''-3y'+2y=0 $$
as a canonical structural example.
- Assumptions and limitations: The approximation is trustworthy only near equilibrium.
- Interpretation: Positive roots indicate instability, negative roots indicate return.

### 2. Conceptual Insight

The characteristic equation works because exponential functions stay within the same family under differentiation. This lesson also previews system eigenvalue thinking later in the course. A common mistake is to believe that the constants $$ c_1,c_2 $$ determine the long-term behavior; the exponential modes do that.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 400)
curves = [
    (np.exp(-t) - np.exp(-3*t), "e^{-t} - e^{-3t}"),
    (2*np.exp(-t) + 0.5*np.exp(-3*t), "2e^{-t} + 0.5e^{-3t}"),
    (np.exp(t) - 0.2*np.exp(-2*t), "e^{t} - 0.2e^{-2t}"),
]

for y, label in curves:
    plt.plot(t, y, label=label)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Exponential modes from distinct real roots")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Students can see immediately that even a small positive mode eventually dominates the future.

### 4. External Search Prompts

- search: overdamped second order response plot
- search: two real roots transient response
- search: damping modes engineering visualization

### 5. Worked Example

Consider
$$ x''+4x'+3x=0,\qquad x(0)=1,\qquad x'(0)=0. $$
The characteristic equation is
$$ r^2+4r+3=0=(r+1)(r+3), $$
so
$$ x(t)=c_1e^{-t}+c_2e^{-3t}. $$
Applying the initial data gives
$$ x(t)=\frac{3}{2}e^{-t}-\frac{1}{2}e^{-3t}. $$
The slower mode $$ e^{-t} $$ governs the long-term decay.

### 6. Difficulty Layering

**Undergraduate level.** Master the characteristic equation, repeated-versus-distinct classification, and sign interpretation.

**Graduate level.** Connect with spectral viewpoints, dominant real parts, and matrix companion forms.

![Different cases of real roots]({{ site.imgurl }}/chapter_img/chapter02/02_02_real_roots_cases.svg)

![Characteristic equation visualization]({{ site.imgurl }}/chapter_img/chapter02/02_02_characteristic.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: very strong on characteristic equation techniques.
- Zill — *Differential Equations with Boundary-Value Problems*: many exercises on distinct and repeated roots.
- Ross — *Differential Equations*: useful for quickly reviewing how to identify the dominant mode.
