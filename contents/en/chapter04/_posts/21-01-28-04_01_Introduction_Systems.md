---
layout: post
title: "04-01 Introduction to Systems of ODEs"
chapter: '04'
order: 1
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

## Learning Objectives

This lesson opens the chapter on systems of differential equations, helping students understand why many phenomena cannot be fully described by a single variable, how to write state in vector form, and see the connection between higher-order equations and first-order systems. After this lesson, students should shift from thinking "one function evolving in time" to thinking "the entire state of a system evolving in time."

## Prerequisites

Students should grasp first-order ODEs, second-order ODEs, the concept of initial conditions, and some basic linear algebra such as vectors and matrices. Physical intuition about position, velocity, flow, or multiple interacting populations is also very helpful, since systems of equations often arise when one quantity is not enough to tell the full dynamical story.

## Introduction

![Diagram converting higher-order equation to state-space system]({{ site.imgurl }}/chapter_img/chapter04/01_introduction_systems.svg)

In previous chapters, we typically solved a single equation for a single unknown function. But reality is rarely contained in one variable alone. An oscillating object needs both position and velocity. An electrical circuit needs charge and current. An ecological model may need to track multiple species simultaneously. When multiple quantities evolve together and influence each other, the natural viewpoint is no longer a single equation, but a system.

The central idea of this chapter is: a system of differential equations is not just a more verbose version of a single ODE, but the right language for multi-state models. Once we accept viewing state as a vector, many powerful tools emerge: matrices, eigenvalues, phase portraits, matrix exponentials, and ultimately a geometric reading of dynamics.

## Concept in Three Ways

### Intuitive View

A system of equations is like a team of people moving together, where each person depends not only on themselves but also on the positions and movements of others. You cannot understand the formation by tracking each person individually; you must track the entire configuration.

### Visual View

If a single ODE gives a trajectory on the $$ \left(t,y\right) $$ plane, then a two-variable system gives a trajectory in the state plane $$ \left(x_1,x_2\right) $$, a three-variable system gives a trajectory in three-dimensional space, and in general in state space $$ \mathbb{R}^n $$. The solution is then not just a graph over time, but a state curve showing which configurations the system passes through.

### Formal View

A general first-order system has the form
$$ \mathbf{x}'=\mathbf{f}(t,\mathbf{x}), $$
where
$$
\mathbf{x}(t)=
\begin{pmatrix}
x_1(t)\\
x_2(t)\\
\vdots\\
x_n(t)
\end{pmatrix}.
$$
If an $$ n $$-th order equation
$$ y^{(n)}=F\left(t,y,y',\ldots,y^{(n-1)}\right) $$
is rewritten with
$$
x_1=y,\quad x_2=y',\quad \ldots,\quad x_n=y^{(n-1)},
$$
then it becomes a first-order system:
$$
\begin{cases}
x_1'=x_2,\\
x_2'=x_3,\\
\vdots\\
x_{n-1}'=x_n,\\
x_n'=F(t,x_1,\ldots,x_n).
\end{cases}
$$

## Common Misconceptions

- "A system of equations is just a different way to write a higher-order ODE." Wrong. They are equivalent in data, but systems reveal state structure and interactions far better.
- "Each equation in the system can be understood separately." Not true. The real meaning lies in the coupling between components.
- "State is just the value of the main variable." Wrong. State comprises all information needed to predict the future, often multiple variables simultaneously.
- "Only nonlinear systems are interesting." Wrong. Even linear systems give us very rich geometry and dynamics.

## Suggested Learning Path

### Step 1: Identify State Variables

Ask what quantities need to be known to predict the system's future.

### Step 2: Write State in Vector Form

Help students become comfortable with this concise yet meaningful notation.

### Step 3: From Higher-Order Equations to First-Order Systems

This is the most important technical bridge at the start of the chapter.

### Step 4: Shift from Time Graphs to State Trajectories

This is the most important conceptual shift.

### Checkpoints

- Can students explain why a system needs multiple state variables?
- Can students correctly convert a higher-order ODE to a first-order system?
- Do students understand how a trajectory in state space differs from a graph over time?

## Worked Examples

### Example 1: From Second-Order Oscillation to System

Consider the equation
$$ y''+2y'+5y=0. $$
Set
$$ x_1=y,\qquad x_2=y'. $$
Then
$$ x_1'=x_2, $$
and from the original equation,
$$ x_2'=-2x_2-5x_1. $$
We obtain the system
$$
\begin{cases}
x_1'=x_2,\\
x_2'=-5x_1-2x_2.
\end{cases}
$$
This example is crucial because it clearly shows students that a second-order ODE is really a two-variable state system.

### Example 2: Two-Population Model

Suppose $$ x(t) $$ and $$ y(t) $$ are two populations with simple linear interaction:
$$
\begin{cases}
x'=2x-y,\\
y'=x+3y.
\end{cases}
$$
Here, the rate of change of each population depends on both populations. There is no reasonable way to compress this picture into a single variable while preserving the original modeling intuition. This is an excellent example to emphasize why systems are the natural language.

### Example 3: State in an Electrical Circuit

A simple LC circuit can be written as a second-order equation for charge. But if we set
$$ x_1=q,\qquad x_2=q', $$
we immediately have a two-dimensional system, where $$ x_1 $$ is charge and $$ x_2 $$ is current. This has very strong physical meaning: we not only know "how much charge the circuit contains," but also "in which direction the charge is changing."

### Example 4: Meaning of Initial Conditions

With the system
$$ \mathbf{x}'=\mathbf{f}(t,\mathbf{x}), $$
initial conditions have the form
$$ \mathbf{x}(t_0)=\mathbf{x}_0. $$
This means we don't just know a number, but the entire initial configuration of the system. This is a very natural generalization of the initial value problem learned in previous chapters.

## Conceptual Questions

1. Why must many physical or biological models be written as systems rather than just a single ODE?
2. When writing a second-order ODE as a first-order system, what is "revealed" about the state?
3. Why do trajectories in state space often give better intuition than just looking at graphs over time?

## Application Problems

1. An autonomous vehicle must be described by both position and velocity. Explain why knowing only position at one instant is insufficient to predict subsequent motion.
2. An epidemiological model has three population groups: susceptible, infected, and recovered. Explain why a system of equations is the right language.
3. An electrical circuit has charge and current changing over time. Interpret them as two components of a state vector.

## Interactive Teaching Strategies

- Start with the question: "To fully predict the future of an oscillating object, is knowing its current position enough?"
- Have students work in pairs to convert 2 to 3 second-order ODEs to first-order systems.
- Plot both $$ y(t) $$ graphs and trajectories in the $$ \left(y,y'\right) $$ plane simultaneously so the class sees the difference between the two views.
- Encourage students to explain in words the meaning of each component in the state vector.

## Differentiation

### Support for Struggling Students

Students who struggle should use a fixed template: identify the state, write lower derivatives first, then use the original equation for the final derivative. Practicing this pattern correctly will help them fear vector notation less.

### Challenge for Advanced Students

Advanced students can be asked to think about when a two-dimensional first-order system can be compressed back into a second-order ODE, and when doing so loses modeling intuition.

## Summary

Systems of differential equations are the language of multi-component state. A higher-order ODE can be written as a first-order system, but the greater benefit is that we see the entire interaction structure of the system. To understand a system, ask: what comprises the state, how do components influence each other, and what does the state trajectory look like?

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Projectile or planar motion
- Problem: A moving body in the plane cannot be described by one scalar alone; position and velocity components evolve together.
- Model:
$$
\mathbf{x}(t)=
\begin{pmatrix}
x\\
y\\
v_x\\
v_y
\end{pmatrix},
\qquad
\mathbf{x}'=\mathbf{f}(t,\mathbf{x}).
$$
- Assumptions and limitations: Many details such as nonlinear drag or rotation are neglected.
- Interpretation: Systems are the natural language because the true state has several coupled components.

#### Multi-compartment epidemic modeling
- Problem: Susceptible, infected, and recovered populations evolve together.
- Model:
$$
\frac{dS}{dt}=f_1(S,I,R),\qquad
\frac{dI}{dt}=f_2(S,I,R),\qquad
\frac{dR}{dt}=f_3(S,I,R).
$$
- Assumptions and limitations: Homogeneous mixing and constant parameters.
- Interpretation: A system captures interaction that one scalar ODE cannot.

#### Converting higher-order ODEs to state form
- Problem: A second-order oscillation should be rewritten to use matrix and phase-space tools.
- Model:
$$
y''+2y'+5y=0
\quad\Longrightarrow\quad
\begin{cases}
x_1'=x_2,\\
x_2'=-2x_2-5x_1.
\end{cases}
$$
- Assumptions and limitations: Only the language changes, not the dynamics.
- Interpretation: First-order state form is the doorway into the entire chapter.

### 2. Conceptual Insight

Systems of ODEs mark the shift from “one changing quantity” to “a multi-dimensional evolving state.” That shift matters more than the algebraic rewrite itself. This lesson connects backward to higher-order ODEs and forward to eigenvalues, phase portraits, and matrix exponentials. A common mistake is to read each component equation in isolation; the real meaning lies in the coupling.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, X):
    x1, x2 = X
    return [x2, -2*x2 - 5*x1]

t = np.linspace(0, 12, 600)
for x10, x20 in [(1, 0), (0, 1), (1, -1)]:
    sol = solve_ivp(system, [0, 12], [x10, x20], t_eval=t)
    plt.plot(sol.y[0], sol.y[1], label=f"IC=({x10},{x20})")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("State trajectories of the equivalent first-order system")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: state space intuition differential equations
- search: converting second order ODE to first order system
- search: phase trajectory system of ODEs visualization

### 5. Worked Example

Consider
$$ y''+2y'+5y=0. $$
Set
$$ x_1=y,\qquad x_2=y'. $$
Then the system becomes
$$
\begin{cases}
x_1'=x_2,\\
x_2'=-5x_1-2x_2.
\end{cases}
$$
The initial data
$$ y(0)=1,\qquad y'(0)=0 $$
become
$$
\mathbf{x}(0)=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
The example shows that passing to system form does not lose information; it clarifies the underlying state structure.

### 6. Difficulty Layering

**Undergraduate level.** Focus on choosing state variables correctly and converting higher-order ODEs to first-order systems.

**Graduate level.** Emphasize state space, dynamical flow, and systems as evolution operators on $$ \mathbb{R}^n $$.

![Introduction to systems]({{ site.imgurl }}/chapter_img/chapter04/04_01_introduction_systems.svg)

## References

- Boyce & DiPrima, Chapter 7: excellent introduction to converting higher-order ODEs to state-space systems.
- Arnold, *Ordinary Differential Equations*: for deep geometric intuition about systems and state space.
