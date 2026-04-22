---
layout: post
title: "05-08 Competing Species"
chapter: '05'
order: 8
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

## Learning Objectives

This lesson helps students analyze two-species competition models, interpret coexistence and exclusion, use nullclines to predict long-term outcomes, and connect nonlinear systems with ecological and economic competition.

## Prerequisites

Students should know autonomous phase-plane methods, equilibria, and linearization. Familiarity with logistic growth is especially helpful.

## Introduction

![Two species competing for limited resources]({{ site.imgurl }}/chapter_img/chapter05/08_competing_species.svg)

Predator-prey systems describe interaction through consumption. Competition models describe a different mechanism: both populations suffer because they rely on the same limited resources. This makes the geometry of the phase plane especially instructive, since nullclines reveal directly whether coexistence is likely or whether one population will exclude the other.

Competition models are important because they generalize one-dimensional logistic growth. Each species now has its own self-limitation and an additional cross-competition term. This creates a mathematically clean setting for discussing survival, dominance, and coexistence.

## Concept in Three Ways

### Intuitive View

Each species grows when rare, but is limited by crowding. The other species adds extra pressure by consuming part of the same resource base. If cross-competition is strong enough, one species may drive the other out.

### Visual View

The nullclines divide the positive quadrant into regions where each species is increasing or decreasing. The relative position of the nullclines often predicts whether coexistence is stable or whether the system moves toward one of the axes.

### Formal View

A standard competition model is
$$
\dot{x}=x(1-x-\alpha y),\qquad
\dot{y}=y(1-y-\beta x).
$$
Boundary equilibria correspond to one species surviving alone, while an interior equilibrium represents coexistence when it lies in the positive quadrant.

## Common Misconceptions

- "If both species can survive alone, they must coexist together." Wrong. Cross-competition may be too strong.
- "Nullclines are actual population trajectories." Wrong. They only mark instantaneous zero change for one species.
- "Competition always leads to extinction of one species." Not necessarily. Stable coexistence is possible.
- "The model is only biological." Wrong. It also serves as a useful analogy for competing technologies or firms.

## Suggested Learning Path

### Step 1: Recall Logistic Growth

Students should see the model as logistic growth plus interaction.

### Step 2: Draw the Nullclines

The geometry of the lines is central.

### Step 3: Locate Equilibria

Boundary and interior equilibria should be interpreted carefully.

### Step 4: Read the Long-Term Outcome

Use the phase portrait to predict exclusion or coexistence.

### Checkpoints

- Can students distinguish self-limitation from cross-competition?
- Can students identify when the interior equilibrium lies in the positive quadrant?
- Do students see that geometry of nullclines often predicts the long-term outcome?

## Worked Examples

### Example 1: Nullclines

For
$$ \dot{x}=x(1-x-\alpha y), $$
the positive nullcline is
$$ x+\alpha y=1. $$
For
$$ \dot{y}=y(1-y-\beta x), $$
the positive nullcline is
$$ y+\beta x=1. $$

### Example 2: Coexistence

If the two nullclines intersect in the positive quadrant, there is a coexistence equilibrium. Whether it is stable depends on the parameter values and the local Jacobian.

### Example 3: Competitive Exclusion

If one nullcline lies in a way that consistently gives one species the advantage, trajectories may move toward an axis equilibrium. Then one species survives and the other is eliminated from the model.

## Conceptual Questions

1. Why is the logistic equation a natural starting point for competition models?
2. How do nullclines reveal coexistence versus exclusion?
3. Why can small parameter changes alter the ecological outcome dramatically?

## Application Problems

1. In ecology, how might habitat differences make the simple competition model inaccurate?
2. In economics, what aspects of firm competition are captured and missed by this model?
3. In conservation biology, why is coexistence analysis important for managing species under stress?

## Interactive Teaching Strategies

- Ask students to sketch nullclines before doing stability calculations.
- Compare one parameter set that leads to coexistence with another that leads to exclusion.
- Encourage verbal interpretation of each term before symbolic work.
- Let students describe the phase portrait in plain biological language.

## Differentiation

### Support for Struggling Students

Students who need support should start by mastering the sign pattern in the four regions created by the positive nullclines.

### Challenge for Advanced Students

Advanced students can explore how parameter variation changes the ecological outcome and connect this to bifurcation ideas.

## Summary

Competition models extend logistic growth into an interacting two-species setting. Their main lessons are how nullcline geometry predicts coexistence, exclusion, and the long-term effect of competition strength.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Two species competing for resources
- Problem: Two species rely on the same limited resource and inhibit each other.
- Model:
$$
\dot{x}=x(1-x-\alpha y),\qquad
\dot{y}=y(1-y-\beta x).
$$
- Assumptions and limitations: Parameters are fixed and the environment is homogeneous.
- Interpretation: Depending on $$ \alpha $$ and $$ \beta $$, the system predicts coexistence or competitive exclusion.

#### Competition for market share
- Problem: Two firms compete for a finite customer base.
- Model: A logistic-style coupled system analogous to biological competition.
- Assumptions and limitations: This is a stylized economic analogy that ignores pricing and strategic behavior.
- Interpretation: Small differences in cross-competition can determine long-run dominance.

### 2. Additional Intuition and Connections

Competition models are where nullcline geometry becomes especially meaningful. The intersections of the nullclines represent states where both species have zero instantaneous change. A common pitfall is to read nullclines as actual population paths. This lesson extends one-dimensional logistic thinking into two-dimensional interaction dynamics and clarifies coexistence versus exclusion.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

alpha, beta = 0.6, 0.8

def comp(t, z):
    x, y = z
    return [x * (1 - x - alpha * y), y * (1 - y - beta * x)]

for z0 in [(0.2, 0.7), (0.8, 0.2), (0.9, 0.9)]:
    sol = solve_ivp(comp, [0, 20], z0, max_step=0.05)
    plt.plot(sol.y[0], sol.y[1], lw=2)

x = np.linspace(0, 1.8, 200)
plt.plot(x, (1 - x) / alpha, "--", label="x-nullcline")
plt.plot((1 - x) / beta, x, "--", label="y-nullcline")
plt.xlim(0, 1.8)
plt.ylim(0, 1.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Competition model with nullclines")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: competing species nullclines coexistence
- search: competitive exclusion phase plane
- search: two species competition model visualization

### 5. Worked Example

Consider
$$ \dot{x}=x(1-x-0.6y),\qquad
\dot{y}=y(1-y-0.8x). $$
The positive nullclines are
$$ x+0.6y=1,\qquad y+0.8x=1. $$
Their intersection lies in the positive quadrant, so there is a candidate coexistence equilibrium. The Jacobian at that point determines whether coexistence is locally stable.

### 6. Difficulty Layering

**Undergraduate level.** Sketch nullclines, identify boundary and interior equilibria, and explain them biologically.

**Graduate level.** Analyze robust coexistence conditions, attracting regions, and links to competition theory in mathematical ecology.

![Competing species]({{ site.imgurl }}/chapter_img/chapter05/05_08_competing_species.svg)

## References

- Strogatz, Chapter 6: qualitative analysis of biological competition models.
- Murray, *Mathematical Biology*: ecological interpretation and extensions.
