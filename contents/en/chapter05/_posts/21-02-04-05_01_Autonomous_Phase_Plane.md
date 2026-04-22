---
layout: post
title: "05-01 Autonomous Systems and the Phase Plane"
chapter: '05'
order: 1
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

## Learning Objectives

This lesson opens the chapter on nonlinear dynamics by shifting attention from explicit solution formulas to the geometry of motion. Students should understand planar autonomous systems, vector fields, nullclines, trajectories in the phase plane, and why phase-plane reasoning remains useful even when closed-form solutions do not exist.

## Prerequisites

Students should already know basic systems of differential equations, the interpretation of equilibrium points, and the linear phase portraits from the previous chapter. Familiarity with one-dimensional autonomous equations and phase lines is also very helpful.

## Introduction

![Phase plane of a two-dimensional autonomous system]({{ site.imgurl }}/chapter_img/chapter05/01_autonomous_phase_plane.svg)

In earlier chapters, many models could be understood by solving for functions of time explicitly. Nonlinear dynamics changes the emphasis. The key questions become: where do trajectories go, what structures organize them, and how does the system behave qualitatively over long times? These are geometric questions more than computational ones.

An autonomous system is the natural place to begin because the right-hand side does not depend explicitly on time. That means the geometry of the motion depends only on the current state. Instead of graphing each variable against time, we plot the state directly in the phase plane. This is the main conceptual transition of the chapter.

## Concept in Three Ways

### Intuitive View

Imagine that every point in the plane is a possible state of the system. At each point, the system "wants to move" in a specific direction. If we draw that preferred direction everywhere, we obtain a dynamical map. A trajectory is the curve traced out by following that map.

### Visual View

For a system
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
we attach the vector
$$ \left(f(x,y),g(x,y)\right) $$
to the point $$ \left(x,y\right) $$. The resulting direction field shows local motion. The nullcline $$ \dot{x}=0 $$ is where horizontal motion disappears, while the nullcline $$ \dot{y}=0 $$ is where vertical motion disappears. These curves divide the plane into regions with different directions of flow.

### Formal View

A planar autonomous system has the form
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
with no explicit dependence on $$ t $$. A trajectory is the image of a solution
$$ t\mapsto \left(x(t),y(t)\right) $$
in state space. An equilibrium point satisfies
$$ f(x_*,y_*)=0,\qquad g(x_*,y_*)=0. $$

## Common Misconceptions

- "If there is no closed-form formula, the system cannot be understood." Wrong. The phase plane often gives strong qualitative information.
- "A phase-plane trajectory is the same as a graph over time." Wrong. It compares state to state, not state to time.
- "Nullclines are trajectories of the system." Wrong. They are only curves where one component of velocity is zero.
- "Autonomous means simple." Not at all. Autonomous systems can display highly nonlinear and complicated behavior.

## Suggested Learning Path

### Step 1: Draw the Direction Field

Students should begin by asking what direction the system points in each region of the plane.

### Step 2: Find Nullclines and Equilibria

These are the structural skeleton of the phase plane.

### Step 3: Use Sign Information

Reading signs of $$ \dot{x} $$ and $$ \dot{y} $$ on different regions is often enough to sketch the flow.

### Step 4: Trace Sample Trajectories

Trajectories must remain tangent to the vector field and respect uniqueness of solutions.

### Checkpoints

- Can students distinguish a trajectory from a nullcline?
- Can students read the signs of $$ \dot{x} $$ and $$ \dot{y} $$ correctly in each region?
- Do students understand why autonomous systems are naturally studied in state space?

## Worked Examples

### Example 1: A Linear Saddle Read from Signs

Consider
$$ \dot{x}=x,\qquad \dot{y}=-y. $$
The nullclines are the coordinate axes. If $$ x>0 $$ then $$ \dot{x}>0 $$, and if $$ x<0 $$ then $$ \dot{x}<0 $$. Likewise, if $$ y>0 $$ then $$ \dot{y}<0 $$, and if $$ y<0 $$ then $$ \dot{y}>0 $$. So motion is outward in the horizontal direction but inward in the vertical direction. This is the geometry of a saddle.

### Example 2: A Nonlinear System with Simple Nullclines

Consider
$$ \dot{x}=x(1-y),\qquad \dot{y}=y(x-1). $$
The nullclines are
$$ x=0,\qquad y=1,\qquad y=0,\qquad x=1. $$
In the region $$ x>1,\ y<1 $$ we have both derivatives positive, so trajectories move up and to the right. In the region $$ x<1,\ y>1 $$ both derivatives are negative, so trajectories move down and to the left.

### Example 3: Time Translation in an Autonomous System

If $$ \left(x(t),y(t)\right) $$ is a solution, then shifting time by a constant produces another solution on the same geometric orbit. This is one reason the phase portrait of an autonomous system is independent of the choice of clock origin.

## Conceptual Questions

1. Why does the phase plane often provide better intuition than separate time graphs in two dimensions?
2. What role do nullclines play in sketching a trajectory?
3. Why does time translation symmetry matter for autonomous systems?

## Application Problems

1. In ecology, two populations evolve together. Why is the phase plane more informative than plotting the populations separately against time?
2. In chemistry, two concentrations interact through a reaction. How does the vector field act like a map of reaction tendencies?
3. In control, why is it valuable to know which regions of state space push the system upward, downward, inward, or outward?

## Interactive Teaching Strategies

- Show a direction field before revealing the equations and ask students to guess likely trajectories.
- Give students nullclines first and ask them to determine the sign pattern of motion in each region.
- Compare one solution viewed as a time graph and as a phase-plane orbit.
- Encourage verbal descriptions of motion before detailed sketching.

## Differentiation

### Support for Struggling Students

Students who feel overwhelmed should follow a fixed routine: find nullclines, test signs in each region, draw a few representative arrows, then sketch sample trajectories.

### Challenge for Advanced Students

Advanced students can explain why trajectories of an autonomous system cannot cross and how that follows from uniqueness of solutions.

## Summary

The phase plane is a geometric map of a planar autonomous system. By locating equilibria, drawing nullclines, and reading the direction field, students can understand qualitative motion even when an explicit formula is unavailable.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Damped pendulum
- Problem: We want to know whether an oscillating mechanical system settles to rest or keeps circulating.
- Model:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega.
$$
- Assumptions and limitations: Air resistance and friction are collapsed into a linear damping term, and there is no external forcing.
- Interpretation: The phase plane shows at a glance whether trajectories spiral into equilibrium or continue through repeated rotations.

#### Two interacting populations
- Problem: Two species change together, with growth of one affecting the other.
- Model:
$$ \dot{x}=x(1-y),\qquad
\dot{y}=y(x-1). $$
- Assumptions and limitations: This is an idealized interaction model with no carrying capacity, delay, or spatial structure.
- Interpretation: The vector field and nullclines reveal the geometry of motion before any explicit solution is attempted.

### 2. Additional Intuition and Connections

The phase plane marks a shift from solving formulas to reading geometry. Nullclines are not trajectories; they are curves where one component of velocity vanishes. A common pitfall is to confuse a state-space orbit with a time graph. This topic connects directly to Chapter 4: instead of classifying only linear systems, we now use geometry to study nonlinear ones as well.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, z):
    x, y = z
    return [x * (1 - y), y * (x - 1)]

x = np.linspace(0.1, 2.5, 20)
y = np.linspace(0.1, 2.5, 20)
X, Y = np.meshgrid(x, y)
U = X * (1 - Y)
V = Y * (X - 1)
N = np.sqrt(U**2 + V**2) + 1e-9

plt.quiver(X, Y, U / N, V / N, color="teal", alpha=0.7)
for z0 in [(0.5, 0.5), (1.8, 0.6), (0.8, 1.8)]:
    sol = solve_ivp(f, [0, 20], z0, max_step=0.05)
    plt.plot(sol.y[0], sol.y[1], lw=2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Phase plane of an autonomous system")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: autonomous system phase plane nullclines
- search: damped pendulum phase portrait
- search: nonlinear vector field trajectories

### 5. Worked Example

Consider
$$ \dot{x}=x(1-y),\qquad
\dot{y}=y(x-1). $$
The nullclines are
$$ x=0,\ y=1,\ y=0,\ x=1. $$
In the region $$ x>1,\ y<1 $$ we have $$ \dot{x}>0 $$ and $$ \dot{y}>0 $$, so trajectories point up and to the right. We already understand the local dynamics from sign information alone.

### 6. Difficulty Layering

**Undergraduate level.** Focus on vector fields, nullclines, equilibria, and reading arrow directions.

**Graduate level.** Emphasize flow maps, invariant sets, topological structure of trajectories, and uniqueness-based geometric consequences.

![Phase plane trajectories]({{ site.imgurl }}/chapter_img/chapter05/05_01_autonomous_phase_plane.svg)

## References

- Strogatz, Chapters 5-6: an excellent intuitive introduction to phase-plane reasoning.
- Arnold, Chapter 4: strong geometric perspective on vector fields and flows.
