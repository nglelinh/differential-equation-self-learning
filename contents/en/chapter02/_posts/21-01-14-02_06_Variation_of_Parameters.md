---
layout: post
title: "02-06 Variation of Parameters"
chapter: '02'
order: 6
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: required
---
## Learning Objectives
This lesson helps students understand variation of parameters as a general tool for finding particular solutions to nonhomogeneous equations, especially when the right-hand side does not fit undetermined coefficients. Students will learn how to replace constants with functions, set up the system of equations for those functions, and interpret the role of the Wronskian throughout the process.

## Background Knowledge
Students should grasp homogeneous solutions of second-order linear equations, the principle of superposition, the reduction of order technique, and skills for solving systems of two linear equations. Some familiarity with the Wronskian will be very helpful, but this lesson can also be used as motivation to see why the Wronskian is important.

## Introduction
![Diagram for Lesson 02-06 Variation of Parameters]({{ site.imgurl }}/chapter_img/chapter02/02_06_variation_of_parameters.svg)

The method of undetermined coefficients is beautiful but has limited scope. If forcing is $$ \ln t $$, $$ \tan t $$, or a function not belonging to a family closed under differentiation, we need a more general tool. Variation of parameters is the answer. Its idea is very elegant: the homogeneous solution already has the form
$$ c_1y_1+c_2y_2. $$
So when external forcing is present, rather than keeping $$ c_1,c_2 $$ constant, we allow them to vary with time.

This is one of those lessons where students easily feel the method is "natural" when understood correctly. We are not guessing the particular solution from outside; we use the very basis of the homogeneous system to construct the forced response. Therefore, variation of parameters is not just a technique. It is the logical continuation of the principle of superposition.

## Three Ways to Understand the Concept
### Intuitive View
Imagine the homogeneous solution provides two fundamental modes of system motion. When there is no external force, the weights of these two modes are constants. When external force is present, the system still moves in the same two-dimensional space, but the weights of the modes are "steered" over time. The new weights are the functions $$ u_1(t) $$ and $$ u_2(t) $$.

### Visual View
If the homogeneous solution creates a family of basis trajectories, the nonhomogeneous solution can be viewed as a trajectory that continuously changes how it mixes the two basic directions to adapt to forcing. This image helps students avoid feeling that the formula is something foreign.

### Formal View
Consider the normalized equation:
$$ y''+p(t)y'+q(t)y=g(t). $$
Suppose $$ y_1,y_2 $$ are two independent solutions of the homogeneous equation. We seek a particular solution of the form
$$ y_p=u_1(t)y_1(t)+u_2(t)y_2(t). $$
To simplify differentiation, we impose the auxiliary condition
$$ u_1'y_1+u_2'y_2=0. $$
Then we have the system
$$ u_1'y_1+u_2'y_2=0, $$
$$ u_1'y_1'+u_2'y_2'=g(t). $$
Solving this system for $$ u_1',u_2' $$ leads to formulas involving the Wronskian.

## Common Misconceptions
- "Variation of parameters is just undetermined coefficients written more complicatedly." Wrong. This is a much more general method.
- "The two functions $$ u_1,u_2 $$ are chosen arbitrarily." Wrong. They are constrained by the system of equations generated from substituting into the ODE.
- "The auxiliary condition
$$ u_1'y_1+u_2'y_2=0 $$
is a trick with no reason." Wrong. It is chosen to reduce order and make computation feasible.
- "If the integral is ugly then the method is wrong." Not true. The method is still correct even if the result is not elegant.

## Suggested Learning Progression
### Step 1: Solve the homogeneous problem
Find $$ y_1,y_2 $$ first. Without this step we cannot proceed.

### Step 2: Set particular solution in variation of parameters form
Write
$$ y_p=u_1y_1+u_2y_2. $$

### Step 3: Apply the auxiliary condition
This is the strategic step to avoid second derivatives of $$ u_1,u_2 $$.

### Step 4: Solve the system for $$ u_1',u_2' $$
Usually use the Wronskian.

### Step 5: Integrate and construct $$ y_p $$
Then combine with $$ y_h $$ for general solution.

### Checkpoints
- Can the student remember that $$ u_1,u_2 $$ are functions not constants?
- Can the student correctly set up the two-equation system for $$ u_1',u_2' $$?
- Can the student understand why the Wronskian must be nonzero?

## Worked Examples
### Example 1: Forcing Inconvenient for Undetermined Coefficients
Solve
$$ y''+y=\tan t,\qquad \lvert t\rvert<\frac{\pi}{2}. $$
The homogeneous solution is
$$ y_h=c_1\cos t+c_2\sin t. $$
Take
$$ y_1=\cos t,\qquad y_2=\sin t. $$
The Wronskian is
$$ W=y_1y_2'-y_1'y_2=\cos^2 t+\sin^2 t=1. $$
By the variation of parameters formula:
$$
u_1'=-\frac{y_2g}{W}=-\sin t\tan t=-\frac{\sin^2 t}{\cos t},
$$
$$ u_2'=\frac{y_1g}{W}=\cos t\tan t=\sin t. $$
Therefore
$$ u_2=-\cos t. $$
And
$$ u_1'=-\frac{1-\cos^2 t}{\cos t}=-\sec t+\cos t, $$
so
$$ u_1=-\ln \lvert \sec t+\tan t\rvert+\sin t. $$
Thus
$$ y_p=u_1\cos t+u_2\sin t. $$
The important point here is to see that the method still works even when forcing is not "nice."

### Example 2: Polynomial Forcing Using General Method
Solve
$$ y''+y=t. $$
Homogeneous solution:
$$ y_h=c_1\cos t+c_2\sin t. $$
With $$ W=1 $$, we have
$$ u_1'=-t\sin t,\qquad u_2'=t\cos t. $$
Integrating by parts:
$$ u_1=t\cos t-\sin t, $$
$$ u_2=t\sin t+\cos t. $$
Thus
$$
y_p=\left(t\cos t-\sin t\right)\cos t+\left(t\sin t+\cos t\right)\sin t=t.
$$
Therefore
$$ y=c_1\cos t+c_2\sin t+t. $$
This example shows variation of parameters can give very neat results even when we use a "large knife" for a simple problem.

### Example 3: Role of the Wronskian
If $$ W=0 $$, the two solutions $$ y_1,y_2 $$ are not linearly independent, so the system for finding $$ u_1',u_2' $$ degenerates. This correctly reflects intuition: if the homogeneous solution basis does not have two independent directions, we cannot represent every forced response using it.

### Example 4: When to Use Variation of Parameters
If forcing is a simple polynomial or exponential, undetermined coefficients is usually faster. But if forcing is
$$ \ln t,\qquad \tan t,\qquad \sec t, $$
or a function not belonging to a family closed under differentiation, variation of parameters is typically the more natural choice. This is a method-selection skill students need to practice.

## Conceptual Questions
1. Why is variation of parameters a natural extension of the homogeneous solution?
2. What is the real role of the auxiliary condition
$$ u_1'y_1+u_2'y_2=0 $$
?
3. Why does the Wronskian appear naturally in this method?

## Application Problems
1. An oscillating system receives non-standard forcing like $$ \ln t $$. Explain why undetermined coefficients is not suitable but variation of parameters still works.
2. A linear control system has two known fundamental modes. Give a physical interpretation of allowing the "mode weights" to vary with time.
3. In forced wave models, why is an independent solution basis of the homogeneous system an essential condition for constructing complete response?

## Interactive Teaching Strategies
- Before giving formulas, ask the class: "If external force changes how the system mixes two fundamental modes, how would you modify the homogeneous solution form?"
- Have students perform each step separately: one group finds $$ y_h $$, one group sets up the system for $$ u_1',u_2' $$, one group computes the Wronskian.
- Compare solving the same problem with undetermined coefficients and variation of parameters to clearly see the tradeoff between generality and elegance.
- Encourage students to say in words when not to use this method, even though in principle it always works.

## Differentiation
### Support for Struggling Students
Provide weaker students with a fixed five-step framework as described above. They often get confused not because of integration, but because of losing structure amid too many symbols.

### Challenge for Advanced Students
Advanced students can be asked to derive the Cramer's rule formula for $$ u_1',u_2' $$ directly from the two-equation system, or to compare variation of parameters with Green's function method in linear problems.

## Memorable Summary
Variation of parameters is the way to let constants in the homogeneous solution become time functions to absorb forcing. This method is general, powerful, and based directly on the solution basis of the homogeneous system. Remember: find $$ y_1,y_2 $$ first, set up the system for $$ u_1',u_2' $$ afterward.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Nonstandard forcing in mechanics
- Problem: A vibrating system is driven by a source such as $$ \tan t $$, $$ \ln t $$, or measured data.
- Model:
$$ y''+p(t)y'+q(t)y=g(t). $$
- Assumptions and limitations: A homogeneous basis must already be known, and the Wronskian must stay nonzero.
- Interpretation: Variation of parameters is more general than undetermined coefficients because it does not require a closed forcing family.

#### Linear control with two natural modes
- Problem: External input changes how strongly the system mixes its two fundamental modes.
- Model:
$$ y_p=u_1(t)y_1(t)+u_2(t)y_2(t). $$
- Assumptions and limitations: The integrals may be unpleasant, even though the method remains valid.
- Interpretation: The constants in the homogeneous solution become time-varying weights.

#### Heat or vibration models with complicated source terms
- Problem: A source is too irregular for the standard forcing table.
- Model: Still a linear nonhomogeneous second-order ODE.
- Assumptions and limitations: In practice the resulting integrals may need numerical evaluation.
- Interpretation: Generality usually comes with more computational cost.

### 2. Conceptual Insight

Variation of parameters is an elegant continuation of superposition. Without forcing, mode weights are constant. With forcing, the weights evolve in time. This lesson points directly toward Duhamel's principle and Green functions later in the course. A common misconception is that the auxiliary condition
$$ u_1'y_1+u_2'y_2=0 $$
is arbitrary; it is a strategic simplification that removes second derivatives of $$ u_1,u_2 $$.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

t = np.linspace(0.05, 1.2, 400)
g = np.tan(t)
y1 = np.cos(t)
y2 = np.sin(t)
u1p = -y2 * g
u2p = y1 * g
u1 = np.concatenate(([0], cumulative_trapezoid(u1p, t)))
u2 = np.concatenate(([0], cumulative_trapezoid(u2p, t)))
yp = u1 * y1 + u2 * y2

plt.plot(t, yp, label="y_p from variation of parameters")
plt.xlabel("t")
plt.ylabel("y_p(t)")
plt.title("Particular solution for y'' + y = tan(t)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

This makes the method look much less mysterious: the particular solution is literally a time-dependent mixture of two basic modes.

### 4. External Search Prompts

- search: variation of parameters visualization
- search: Wronskian Cramer rule animation
- search: Green function second order ODE intuition

### 5. Worked Example

Solve
$$ y''+y=\tan t,\qquad \lvert t\rvert<\frac{\pi}{2}. $$
The homogeneous solution is
$$ y_h=c_1\cos t+c_2\sin t. $$
Take
$$ y_1=\cos t,\qquad y_2=\sin t,\qquad W=1. $$
Then
$$
u_1'=-y_2g=-\sin t\tan t,\qquad u_2'=y_1g=\cos t\tan t=\sin t.
$$
So
$$ u_2=-\cos t, $$
while $$ u_1 $$ follows from integration. Even though the integrals are less elegant than in standard forcing problems, the structure of the method remains clear.

### 6. Difficulty Layering

**Undergraduate level.** Learn the five-step workflow and know when to prefer this method over undetermined coefficients.

**Graduate level.** Connect with Cramer's rule, Green functions, and integral operator representations.

![Variation of parameters concept]({{ site.imgurl }}/chapter_img/chapter02/02_06_variation_of_parameters.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: presents the formula and motivation of the method very clearly.
- Zill — *Differential Equations with Boundary-Value Problems*: many non-standard forcing problems to practice variation of parameters.
- Ross — *Differential Equations*: useful for reviewing the general idea when comparing with undetermined coefficients.
