---
layout: post
title: "01-09 Autonomous Equations and Phase Lines"
chapter: '01'
order: 9
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: optional
---

## Objectives

This lesson teaches students how to read the qualitative behavior of an autonomous ODE without solving it explicitly. Students learn how to identify equilibria, use the sign of $$ f(y) $$ to build a phase line, classify stability, and understand why qualitative analysis is essential when explicit formulas are difficult or unnecessary.

## Prerequisites

Students should know first-order equations of the form $$ y'=f(y) $$, the idea of equilibrium solutions, and how to test the sign of an expression. Background with logistic equations is especially helpful because it provides a concrete model in which phase-line reasoning already appears naturally.

## Introduction

We do not always need a closed formula to understand a dynamical system. If we know whether the system increases or decreases at each state value, then we can often predict long-term behavior, identify stable thresholds, and describe the role of equilibrium points. This is an important shift in mathematical thinking: from exact computation to structural analysis.

Autonomous equations are the ideal place to begin that shift because the right-hand side depends only on the current state. That allows us to study motion on a one-dimensional phase line. The tool is simple, but it opens the door to dynamical systems and stability theory later in the course.

## The Concept in Three Ways

### Intuitive View

Imagine a particle moving along a straight wire. At each location, we know whether it tends to move right or left. If at some location it remains still, that point is an equilibrium. If arrows on both sides point toward it, the equilibrium is stable. If arrows point away, it is unstable.

### Visual View

Draw a vertical line representing the state variable $$ y $$. For $$ y'=f(y) $$, the motion is determined by the sign of $$ f(y) $$:

- if $$ f(y)>0 $$, solutions move upward in time,
- if $$ f(y)<0 $$, solutions move downward,
- if $$ f(y)=0 $$, we have an equilibrium.

These arrows on the phase line often replace the need to draw full solution graphs in the $$ \left(t,y\right) $$ plane.

### Formal View

For the autonomous equation

$$ \frac{dy}{dt}=f(y), $$

an equilibrium $$ y_* $$ satisfies $$ f(y_*)=0 $$. In the one-dimensional setting of this chapter:

- if arrows on both sides point toward $$ y_* $$, the equilibrium is stable,
- if arrows on both sides point away, it is unstable,
- if one side points in and the other points out, it is semistable.

## Core Mathematical Idea

Phase-line analysis shows that long-term behavior is often controlled by equilibria and by the sign of $$ f(y) $$ on the intervals between them. We do not need an exact formula to know where solutions move. This is one reason the method is so valuable in biology, chemistry, and social modeling, where qualitative predictions may matter more than closed-form expressions.

The phase line also teaches students that a solution of an ODE is not only a graph over time. It is also a trajectory in state space. That idea becomes much more important in later chapters on systems and nonlinear dynamics.

## Common Misconceptions

### "You must solve the equation explicitly before discussing stability"

False. In one-dimensional autonomous problems, stability often follows directly from the sign of $$ f(y) $$.

### "Every equilibrium is stable"

False. Some equilibria repel nearby solutions.

### "If $$ f(y) $$ is positive, then all solutions grow forever"

Not necessarily. The sign may change on different intervals, and equilibria may block motion.

### "The phase line is only a sketching device"

False. It is a rigorous and powerful tool for qualitative analysis in one-dimensional autonomous systems.

## Learning Progression

### Step 1: Find the equilibria

Solve

$$ f(y)=0. $$

### Step 2: Split the phase line into intervals

The equilibria divide the state line into separate regions.

### Step 3: Test the sign of $$ f(y) $$ on each interval

Use a test point or factor analysis to determine arrow direction.

### Step 4: Interpret stability and long-term motion

Ask where nearby solutions move and what happens as time increases.

### Key Checkpoints

- Can students find all equilibria?
- Can they test the sign on each interval correctly?
- Can they explain stability in words, not just with arrows?

## Worked Examples

### Example 1: Logistic growth

Consider

$$ y'=ry\left(1-\frac{y}{K}\right). $$

The equilibria are $$ y=0,\qquad y=K $$. For positive populations, arrows point away from $$ 0 $$ and toward $$ K $$, so $$ 0 $$ is unstable and $$ K $$ is stable.

### Example 2: A cubic autonomous equation

Suppose $$ y'=y(y-1)(y-2) $$. The equilibria are $$ 0 $$, $$ 1 $$, and $$ 2 $$. By testing the sign on each interval, students can build the full phase line and determine which equilibria are stable or unstable.

### Example 3: Semistability

If an equation has $$ y'=(y-1)^2 $$, then the only equilibrium is $$ y=1 $$. Since the derivative is nonnegative on both sides, solutions move upward on both sides, so the equilibrium is semistable rather than fully stable or fully unstable.

### Example 4: Qualitative analysis without an explicit formula

Even if an autonomous equation is difficult to solve exactly, a phase line may still describe the long-term behavior completely. This is one of the strongest messages of the lesson.

## Conceptual Questions

1. Why is the phase line often enough to understand long-term behavior?
2. Why is an equilibrium classification fundamentally a directional statement?
3. Why does autonomous structure make qualitative analysis especially effective?

## Application Problems

1. In a biological model, how would you explain a stable equilibrium to someone thinking in terms of carrying capacity?
2. In a chemical model, how does a phase line help identify a stable concentration level?
3. In a social or economic model, why might an unstable equilibrium represent a fragile state?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What does the sign of $$ f(y) $$ tell us before we solve anything?
- Why can a stable equilibrium attract nearby states?
- Can one equilibrium be stable from one side and unstable from the other?

### Suggested Activities

- Give students several autonomous equations and ask them only to draw phase lines.
- Compare phase-line conclusions with exact formulas when available.
- Use logistic growth as a bridge from explicit solution to qualitative dynamics.

### Participation Moves

- Ask for arrow directions before any classification labels.
- Let students explain stability physically, then mathematically.
- Encourage them to describe the fate of solutions from different initial conditions.

## Differentiation

### Support for Struggling Students

- Use only equations with easily factorable right-hand sides at first.
- Keep the sign-testing process explicit and repetitive.
- Connect phase lines to previously solved logistic models.

### Challenge for Advanced Students

- Compare phase-line analysis with linearization intuition.
- Explore bifurcation-like behavior when parameters change.
- Connect one-dimensional phase lines with later phase-plane ideas in nonlinear systems.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Harvested population with collapse threshold
- Problem: A fishery under constant harvesting may recover or collapse depending on its current stock.
- Model:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right)-h. $$
- Assumptions and limitations: Harvesting is constant and the population is homogeneous. Seasonal effects and age structure are ignored.
- Interpretation: A phase line can reveal a critical threshold below which collapse becomes unavoidable.

#### Market-price adjustment
- Problem: Price adjusts in response to current excess demand.
- Model:
$$ \frac{dp}{dt}=f(p). $$
- Assumptions and limitations: The whole market is collapsed into one state variable and reacts without delay.
- Interpretation: The sign of $$ f(p) $$ tells us whether price is pushed toward equilibrium or away from it.

#### Chemical reactor with multiple operating states
- Problem: A reactor may settle into a low-temperature or high-temperature regime depending on initial conditions.
- Model:
$$ \frac{dy}{dt}=f(y), $$
with several zeros of $$ f(y) $$.
- Assumptions and limitations: This is a one-dimensional reduction of a richer system.
- Interpretation: Phase-line analysis captures multistability without requiring a closed-form solution.

### 2. Conceptual Insight

Autonomous equations teach a major shift in mathematical thinking: we can understand dynamics without explicitly solving for the trajectory formula. The sign of $$ f(y) $$ over intervals, not at isolated points, controls the motion. This lesson opens the door to later work on linearization, bifurcation, and nonlinear stability.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

f = lambda t, y: y * (1 - y) * (y - 0.3)
t_eval = np.linspace(0, 20, 400)

for y0 in [0.1, 0.25, 0.5, 1.2]:
    sol = solve_ivp(f, [0, 20], [y0], t_eval=t_eval, max_step=0.1)
    plt.plot(sol.t, sol.y[0], label=f"y0={y0}")

plt.axhline(0, color="black", linestyle=":")
plt.axhline(0.3, color="black", linestyle="--")
plt.axhline(1, color="black", linestyle=":")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Trajectories for an autonomous threshold model")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

The simulation makes the threshold state $$ 0.3 $$ visually obvious: initial conditions below it move toward 0, while those above it move toward 1.

### 4. External Search Prompts

- search: autonomous equation phase line interactive
- search: harvesting logistic bifurcation
- search: Allee effect phase line simulation

### 5. Worked Example

Consider the normalized harvesting model
$$ \frac{dx}{dt}=x(1-x)-0.16. $$
Equilibria satisfy
$$ x^2-x+0.16=0, $$
so
$$ x=0.2,\qquad x=0.8. $$
Sign analysis shows that $$ x=0.2 $$ is unstable and $$ x=0.8 $$ is stable. In application language, the lower equilibrium is a danger threshold and the upper one is a sustainable operating point.

### 6. Difficulty Layering

**Undergraduate level.** Find equilibria, build the phase line, and infer long-time behavior from sign information.

**Graduate level.** Connect with the derivative test $$ f'(y_*) $$, one-parameter bifurcation theory, structural stability, and one-dimensional Lyapunov thinking.

![Phase line and solutions for autonomous equations]({{ site.imgurl }}/chapter_img/chapter01/01_09_autonomous_equations.svg)

![Different stability types]({{ site.imgurl }}/chapter_img/chapter01/01_09_stability_types.svg)

## Quick Summary

For autonomous first-order equations, the sign of $$ f(y) $$ often reveals the full qualitative dynamics. Phase lines show where solutions move, which equilibria are stable, and what long-term behavior to expect even without an explicit formula.
