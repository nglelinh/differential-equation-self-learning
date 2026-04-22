---
layout: post
title: "01-05 Substitution Methods"
chapter: '01'
order: 5
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

## Objectives

This lesson helps students see that many first-order ODE that initially look nonlinear and complicated actually hide a better variable. Once the right substitution is chosen, the equation often becomes separable, linear, or exact. Students should learn to recognize the most important patterns, especially Bernoulli equations and first-order homogeneous equations.

## Prerequisites

Students should be comfortable with separable equations, first-order linear equations, and the chain rule. Most of the difficulty in this topic is not computational. It is structural: the challenge is to notice which new variable reveals a familiar form.

## Introduction

Some differential equations resist the methods we already know, but only on the surface. A good substitution can expose the hidden structure and turn an unfamiliar problem into a familiar one. This is one of the first places in the course where students begin to experience an important mathematical habit: instead of attacking the equation as written, look for the right viewpoint from which the equation becomes simpler.

Substitution methods are especially valuable because they teach pattern recognition. Once students see how a Bernoulli equation becomes linear or how a homogeneous first-order equation becomes separable after introducing $$ v=y/t $$, they start to understand that solving differential equations is often about choosing coordinates wisely.

## The Concept in Three Ways

### Intuitive View

A substitution is like changing the camera angle. The object itself has not changed, but from a better angle its structure becomes visible. In ODE, the right substitution often collects repeated combinations into one new variable and removes the apparent complexity of the original equation.

### Visual View

A useful classroom picture is a flow chart:

- original equation,
- identify a recognizable pattern,
- choose a substitution,
- transform into a known type,
- solve and translate back.

Students should see substitution not as random guessing, but as a structured decision process.

### Formal View

Typical first-order substitution patterns include:

- Bernoulli equation:
$$ y'+p(t)y=q(t)y^n $$
with substitution
$$ u=y^{1-n}; $$

- homogeneous first-order equation:
$$ y'=F\left(\frac{y}{t}\right) $$
with substitution
$$ y=vt; $$

- equations with a repeated linear combination such as $$ at+by+c $$, where setting that combination equal to a new variable may simplify the equation.

## Common Misconceptions

### "Substitution is just clever guessing"

Not entirely. Good substitutions come from recognizable structural patterns.

### "If one substitution does not work, the equation has no method"

False. It may simply belong to a different recognizable class.

### "After substitution, the problem is finished"

Not yet. Students still need to solve the transformed equation and then translate back to the original variable.

### "Every nonlinear equation can be fixed by substitution"

No. Substitution is powerful, but not universal.

## Learning Progression

### Step 1: Look for structure

Students should search for repeated combinations, quotient patterns, or nonlinear powers that suggest a substitution.

### Step 2: Perform the substitution carefully

Use the chain rule correctly and rewrite the entire equation in the new variable.

### Step 3: Solve the transformed equation

At this point the equation should reduce to a form students already know.

### Step 4: Translate back

The final answer must be written in terms of the original variable.

### Key Checkpoints

- Can students explain why a particular substitution was chosen?
- Can they correctly compute the derivative after substitution?
- Can they return to the original variables without losing constants or domains?

## Worked Examples

### Example 1: A Bernoulli equation

Consider $$ y'+y=y^2 $$. This has the Bernoulli form with $$ n=2 $$. Let $$ u=y^{-1} $$. Then $$ u'=-y^{-2}y' $$. After substitution, the equation becomes linear in $$ u $$. This is the standard Bernoulli mechanism: nonlinear in $$ y $$, linear after changing variables.

### Example 2: A first-order homogeneous equation

Suppose

$$ y'=1+\frac{y}{t}. $$

Because the right-hand side depends on $$ y/t $$, use $$ y=vt $$. Then

$$ y'=v+t\frac{dv}{dt}. $$

Substituting gives an equation in $$ v $$ and $$ t $$ that is separable. The key point is that the quotient structure signals the correct substitution immediately.

### Example 3: A repeated expression

If an equation contains the combination $$ t+y $$ repeatedly, it can be useful to set $$ u=t+y $$. Then

$$ \frac{du}{dt}=1+\frac{dy}{dt}. $$

This often reduces the equation to one involving only $$ u $$ and $$ t $$, which may be separable or linear.

### Example 4: Why structure matters

An equation can look complicated in its original variables but simple in the right coordinates. This is the broader lesson of substitution methods: the right variable often reveals the correct method.

## Conceptual Questions

1. Why is substitution more about recognizing structure than about algebraic manipulation?
2. Why does the quotient $$ y/t $$ often suggest the substitution $$ y=vt $$?
3. Why is it important to interpret the transformed equation rather than only compute mechanically?

## Application Problems

1. In a modeling context, how can a substitution represent a meaningful change of state variables rather than just a trick?
2. Why might a ratio variable such as concentration per volume or output per input naturally simplify a system?
3. In population or growth models, how can a transformed variable reveal the balance between nonlinear growth and damping?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What repeated pattern in the equation makes you think of a substitution?
- What known method are you hoping to reach after the substitution?
- How do you check that the substitution really simplified the problem?

### Suggested Activities

- Give students several first-order equations and ask them only to identify the best substitution, not solve them yet.
- Build a classroom table: pattern, substitution, resulting method.
- Have groups explain why two different-looking equations actually require the same substitution idea.

### Participation Moves

- Ask for structure first, computation second.
- Let students predict the target method before carrying out algebra.
- Encourage them to justify substitutions in words, not just formulas.

## Differentiation

### Support for Struggling Students

- Focus first on Bernoulli and homogeneous equations as the two main templates.
- Provide explicit pattern-recognition cues.
- Practice the chain rule step separately when needed.

### Challenge for Advanced Students

- Compare several substitutions for the same equation and discuss which one is best.
- Explore nonlinear substitutions that come from invariants or symmetries.
- Connect substitution methods to broader ideas of coordinate change in differential equations.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Self-limiting growth
- Problem: A microbial population grows roughly exponentially at low density but slows due to crowding.
- Model:
$$ \frac{dy}{dt}+ay=by^2. $$
- Assumptions and limitations: The coefficients are constant and the environment is uniform. Seasonality and spatial variation are ignored.
- Interpretation: The substitution $$ u=1/y $$ exposes a hidden linear structure.

#### Ratio-driven economic adjustment
- Problem: Output responds to the ratio between accumulated capital and elapsed time, not separately to each quantity.
- Model:
$$ \frac{dy}{dt}=F\left(\frac{y}{t}\right). $$
- Assumptions and limitations: The law is scale-homogeneous and has no external clock effect.
- Interpretation: The substitution $$ y=vt $$ reveals that the true variable may be the ratio itself.

#### Nonlinear aggregation in aerosol chemistry
- Problem: Particles are supplied to a chamber but also disappear through pairwise aggregation.
- Model:
$$ \frac{dc}{dt}+kc=qc^2. $$
- Assumptions and limitations: The chamber is well mixed and rate coefficients are constant.
- Interpretation: This Bernoulli structure shows that not every nonlinear equation is structurally mysterious.

### 2. Conceptual Insight

Substitution methods teach a major mathematical habit: the original variable is not always the best one. A strong substitution compresses repeated structure, exposes symmetry, or linearizes the model. The main pitfall is to choose a clever new variable but then differentiate it carelessly or forget to translate the final answer back.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

r, K, P0 = 0.9, 50, 5
t = np.linspace(0, 10, 400)
P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
U = 1 / P

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(t, P, color="darkgreen")
axes[0].set_title("Original variable P(t)")
axes[0].set_xlabel("t")
axes[0].set_ylabel("P")

axes[1].plot(t, U, color="darkred")
axes[1].set_title("Transformed variable u(t) = 1 / P(t)")
axes[1].set_xlabel("t")
axes[1].set_ylabel("u")

for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

This side-by-side picture helps students feel why a substitution can make nonlinear behavior easier to analyze.

### 4. External Search Prompts

- search: Bernoulli differential equation application
- search: homogeneous first order equation visualization
- search: Riccati equation substitution linearization

### 5. Worked Example

Consider
$$ \frac{dy}{dt}+0.5y=0.02y^2,\qquad y(0)=4. $$
Setting
$$ u=\frac{1}{y} $$
gives
$$ \frac{du}{dt}-0.5u=-0.02. $$
Solving yields
$$
u(t)=0.04+0.21e^{0.5t},
\qquad
y(t)=\frac{1}{0.04+0.21e^{0.5t}}.
$$
The solution shows bounded long-term behavior rather than explosive exponential growth.

### 6. Difficulty Layering

**Undergraduate level.** Recognize Bernoulli and homogeneous patterns and justify the substitution choice clearly.

**Graduate level.** Connect substitution methods to Riccati equations, symmetry reduction, and broader coordinate changes in dynamical systems.

![Bernoulli and homogeneous equations]({{ site.imgurl }}/chapter_img/chapter01/01_05_substitution_methods.svg)

![Substitution pattern visualization]({{ site.imgurl }}/chapter_img/chapter01/01_05_substitution_patterns.svg)

## Quick Summary

Substitution methods work by revealing hidden structure. The right new variable can turn a difficult-looking ODE into a separable, linear, or exact equation that students already know how to solve.
