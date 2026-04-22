---
layout: post
title: "02-05 Nonhomogeneous Equations: Undetermined Coefficients"
chapter: '02'
order: 5
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: required
---
## Learning Objectives
This lesson helps students solve second-order linear nonhomogeneous equations using the method of undetermined coefficients, know how to choose the correct trial particular solution form, handle resonance phenomena by multiplying by powers of $$ t $$, and understand why this method is only suitable for families of functions closed under differentiation.

## Background Knowledge
Students need to grasp homogeneous solutions for constant-coefficient equations, the principle of superposition, and differentiation skills for polynomials, exponentials, and sine-cosine functions. This is a lesson where the ability to recognize forcing forms is as important as substitution technique.

## Introduction
![Diagram for Lesson 02-05 Nonhomogeneous Equations: Undetermined Coefficients]({{ site.imgurl }}/chapter_img/chapter02/02_05_undetermined_coefficients.svg)

When the right-hand side of the equation is not zero, we need to find a particular solution describing the system's response to external forcing. If the forcing has a nice form like polynomials, exponentials, sine-cosine, or products of these, we don't need to use heavy general tools. We can try a solution from the same family and adjust the unknown coefficients. This is precisely the method of undetermined coefficients.

The subtlety of the method lies in not simply copying the forcing exactly. If the trial form coincides with part of the homogeneous solution, we must multiply by $$ t $$, sometimes $$ t^2 $$, to create a linearly independent function. This is where the resonance phenomenon appears in algebraic language.

## Three Ways to Understand the Concept
### Intuitive View
The system is like a musical instrument struck by a special type of signal. If that signal belongs to a family "stable under differentiation," then we expect the forced response to also belong to that family. But if the excitation tone coincides with the system's natural mode, the response amplitude must change in a different manner, and that's why we need to multiply by $$ t $$.

### Visual View
If forcing is constant or polynomial, the particular solution typically curves like a polynomial. If forcing is $$ e^{at} $$, the particular solution typically carries the same exponential form. If forcing is $$ \sin bt $$ or $$ \cos bt $$, the particular solution typically is a sine-cosine combination. When resonance occurs, graphs typically show a term growing with $$ t $$ times the system's own mode.

### Formal View
For the equation
$$ ay''+by'+cy=g(t), $$
we write the general solution as
$$ y=y_h+y_p. $$
The method of undetermined coefficients finds $$ y_p $$ by guessing a form from the same family as $$ g(t) $$. If the guessed form coincides with components of $$ y_h $$, we multiply by $$ t^s $$, where $$ s $$ is the multiplicity needed to achieve linear independence.

## Common Misconceptions
- "Just copy the forcing as the trial particular solution." Wrong. We must also consider derivatives of the forcing and potential overlap with the homogeneous solution.
- "If the trial form is wrong then the method completely fails." Not quite. Most mistakes are due to missing terms or missing the $$ t $$ multiplier.
- "All forcing functions can use undetermined coefficients." Wrong. The method is only suitable for families closed under differentiation.
- "Resonance is just a physical concept." Wrong. It appears very concretely when the trial form hits the homogeneous solution.

## Suggested Learning Progression
### Step 1: Solve the homogeneous equation
Never skip this step, as it determines whether resonance occurs.

### Step 2: Look at forcing and choose appropriate function family
List all terms that could be generated after differentiation.

### Step 3: Check for overlap with homogeneous solution
If overlap occurs, multiply by $$ t $$ or higher power.

### Step 4: Substitute to find coefficients
This algebraic part needs to be neat and organized.

### Checkpoints
- Can the student choose a sufficient trial family?
- Can the student detect resonance?
- Can the student distinguish between particular and general solutions?

## Worked Examples
### Example 1: Polynomial Forcing
Solve
$$ y''-3y'+2y=t. $$
Homogeneous solution:
$$ y_h=c_1e^t+c_2e^{2t}. $$
Since forcing is a first-degree polynomial, we try
$$ y_p=At+B. $$
Then
$$ y_p'=A,\qquad y_p''=0. $$
Substituting:
$$ 0-3A+2(At+B)=t. $$
Comparing coefficients:
$$ 2A=1 \Rightarrow A=\frac{1}{2}, $$
$$
-3A+2B=0 \Rightarrow -\frac{3}{2}+2B=0 \Rightarrow B=\frac{3}{4}.
$$
Thus
$$ y(t)=c_1e^t+c_2e^{2t}+\frac{1}{2}t+\frac{3}{4}. $$

### Example 2: Exponential Forcing Without Resonance
Solve
$$ y''+y=e^t. $$
Homogeneous solution:
$$ y_h=c_1\cos t+c_2\sin t. $$
We try
$$ y_p=Ae^t. $$
Substituting:
$$
Ae^t+Ae^t=e^t \Rightarrow 2A=1 \Rightarrow A=\frac{1}{2}.
$$
Therefore
$$ y(t)=c_1\cos t+c_2\sin t+\frac{1}{2}e^t. $$

### Example 3: Exponential Forcing With Resonance
Solve
$$ y''-y=e^t. $$
The homogeneous solution is
$$ y_h=c_1e^t+c_2e^{-t}. $$
If we try $$ Ae^t $$ it will overlap with $$ y_h $$, so we must try
$$ y_p=Ate^t. $$
Computing derivatives:
$$ y_p'=Ae^t+Ate^t, $$
$$ y_p''=2Ae^t+Ate^t. $$
Substituting:
$$ \left(2Ae^t+Ate^t\right)-Ate^t=e^t. $$
Thus
$$ 2A=1 \Rightarrow A=\frac{1}{2}. $$
Therefore
$$ y(t)=c_1e^t+c_2e^{-t}+\frac{1}{2}te^t. $$
This is a classic algebraic resonance example.

### Example 4: Trigonometric Forcing
Solve
$$ y''+4y=\cos t. $$
Homogeneous solution:
$$ y_h=c_1\cos 2t+c_2\sin 2t. $$
Since forcing is $$ \cos t $$, we try
$$ y_p=A\cos t+B\sin t. $$
Then
$$ y_p''=-A\cos t-B\sin t. $$
Substituting:
$$ 3A\cos t+3B\sin t=\cos t. $$
Thus
$$ A=\frac{1}{3},\qquad B=0. $$
Therefore
$$ y(t)=c_1\cos 2t+c_2\sin 2t+\frac{1}{3}\cos t. $$

## Conceptual Questions
1. Why is the method of undetermined coefficients only suitable for certain types of forcing?
2. Why do we need to multiply by $$ t $$ when forcing overlaps with the homogeneous solution?
3. In physical interpretation, what does algebraic resonance remind us of?

## Application Problems
1. A mechanical system is excited by periodic force. Explain why trigonometric forcing leads to a trigonometric particular solution.
2. An electrical circuit receives an exponential signal from a source that turns on exponentially. Explain why the forced response typically belongs to the same function family.
3. A vibrating system is excited by a signal at exactly its natural mode. Discuss why the response may show a term multiplied by $$ t $$.

## Interactive Teaching Strategies
- Have students participate in a "guess the particular solution form" game before detailed calculations.
- Write several different forcings on the board and ask the class to point out which problems have resonance risk.
- Stop before the step of multiplying by $$ t $$ and ask: "If we try the old form, what will happen?"
- Encourage students to explain in words why we must include both sine and cosine when forcing has only one.

## Differentiation
### Support for Struggling Students
Give weaker students a reference table between forcing type and corresponding trial form. Practicing the distinction between "polynomial," "exponential," "trigonometric," "products of families" will help them fear the ansatz selection less.

### Challenge for Advanced Students
Advanced students can be asked to explain in vector space language why suitable forcing families must be closed under differentiation, or to handle forcing of the form $$ te^t $$ or $$ e^t\cos t $$.

## Memorable Summary
Undetermined coefficients works when forcing belongs to a nice family under differentiation. To use the method correctly, do four things: solve the homogeneous part, choose the right trial family, check for resonance, then find coefficients. If the trial form overlaps with the homogeneous solution, multiply by $$ t $$.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Forced mechanical vibration
- Problem: A spring-mass system is driven by constant or periodic forcing.
- Model:
$$ m x''+c x'+k x=F_0\cos \omega t $$
or
$$ m x''+c x'+k x=P_0. $$
- Assumptions and limitations: Constant coefficients and forcing from a differentiation-closed family.
- Interpretation: The particular solution should live in the same family as the forcing, unless resonance occurs.

#### Circuit input signals
- Problem: An RLC circuit receives polynomial, exponential, or trigonometric forcing.
- Model:
$$ Lq''+Rq'+\frac{1}{C}q=E(t). $$
- Assumptions and limitations: Undetermined coefficients only works when differentiation keeps us in the same finite-dimensional family.
- Interpretation: This explains why functions like $$ \ln t $$ or $$ \tan t $$ fall outside the method's scope.

#### Resonant excitation
- Problem: The forcing frequency matches a natural mode of the system.
- Model:
$$ y''+\omega_0^2 y=\cos \omega_0 t. $$
- Assumptions and limitations: Little or no damping.
- Interpretation: Multiplying the ansatz by $$ t $$ is the algebraic signature of resonance.

### 2. Conceptual Insight

Undetermined coefficients works because certain forcing families form finite-dimensional spaces closed under differentiation. That turns the search for a particular solution into a coefficient-finding problem. Students often copy the forcing mechanically and forget to include every derivative-generated term from the same family.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 1000)
y_res = 0.5 * t * np.sin(t)
y_nonres = 0.75 * np.cos(2*t)

plt.plot(t, y_res, label="Resonant: y_p ~ t sin(t)")
plt.plot(t, y_nonres, label="Nonresonant: y_p ~ cos(2t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Particular solutions with and without resonance")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

The resonant curve makes the algebraic effect of the extra factor $$ t $$ visually obvious.

### 4. External Search Prompts

- search: undetermined coefficients resonance animation
- search: forced oscillator particular solution visualization
- search: resonance t sin t explanation

### 5. Worked Example

For
$$ y''+y=\cos t, $$
the homogeneous solution is
$$ y_h=c_1\cos t+c_2\sin t. $$
Trying $$ A\cos t+B\sin t $$ fails because it overlaps with $$ y_h $$, so we multiply by $$ t $$ and use
$$ y_p=t\left(A\cos t+B\sin t\right). $$
One particular solution is
$$ y_p=\frac{1}{2}t\sin t, $$
so
$$ y(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
The factor $$ t $$ records cumulative energy injection at resonance.

### 6. Difficulty Layering

**Undergraduate level.** Learn the ansatz table, check resonance carefully, and compute coefficients cleanly.

**Graduate level.** Explain the method using invariant subspaces under differentiation and connect with annihilator methods.

![Undetermined coefficients - resonance]({{ site.imgurl }}/chapter_img/chapter02/02_05_undetermined_coefficients.svg)

![Trial forms visualization]({{ site.imgurl }}/chapter_img/chapter02/02_05_trial_forms.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: very strong on undetermined coefficients method and resonance.
- Zill — *Differential Equations with Boundary-Value Problems*: many exercises on choosing ansatz forms.
- Ross — *Differential Equations*: concise presentation, good for reviewing the forcing table.
