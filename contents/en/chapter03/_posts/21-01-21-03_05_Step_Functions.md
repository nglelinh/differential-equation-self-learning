---
layout: post
title: "03-05 Step Functions and Discontinuous Forcing"
chapter: '03'
order: 5
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: required
---
## Learning Objectives
This lesson helps students use the Heaviside step function to model signals that suddenly turn on/off, understand the time-shifting theorem in Laplace, and solve problems with piecewise forcing without manually dividing the solution into intervals.

## Prerequisites
Students need to master basic Laplace, inverse Laplace, and the workflow for solving IVPs with Laplace. Intuition about signals turning on, closing switches, or external forces appearing only after a certain moment is also very helpful.

## Introduction
![Illustration for Lesson 03-05 Step Functions and Discontinuous Forcing]({{ site.imgurl }}/chapter_img/chapter03/03_05_step_functions.svg)

In the real world, many signals don't appear from the beginning and continue smoothly forever. A power source might turn on at the second second. A force might act then be cut off after a time interval. A system might bear loads in stages. Phenomena like these are unpleasant if we try to solve the ODE on each interval then manually connect continuity conditions.

The Heaviside step function and Laplace solve this problem beautifully. They allow us to write discontinuous signals with a single expression, then handle algebra in the $$ s $$ domain as usual. This is where students begin to feel that Laplace is not just convenient for calculations, but truly born to model systems.

## Three Ways to Understand the Concept
### Intuitive View
The step function is a switch. Before time $$ a $$, the switch is off so the value is 0. After that moment, the switch is on so the value is 1. If we multiply it by another function, we're saying "this function only starts operating from time $$ a $$."

### Visual View
The graph of
$$ u(t-a) $$
is a horizontal line at 0 until $$ t=a $$ then jumps to 1. If we look at
$$ u(t-a)f(t-a), $$
we see the graph of $$ f $$ doesn't start at 0 but is translated right to time $$ a $$. This image of shifting right is precisely why the factor $$ e^{-as} $$ appears in the Laplace domain.

### Formal View
The Heaviside step function is defined by
$$
u(t-a)=
\begin{cases}
0, & t<a,\\
1, & t\ge a.
\end{cases}
$$
The most important Laplace property is
$$ \mathcal{L}\{u(t-a)f(t-a)\}=e^{-as}F(s), $$
where
$$ F(s)=\mathcal{L}\{f(t)\}. $$
This is the time-shifting theorem, which is the center of the entire lesson.

## Common Misconceptions
- "The step function is just decorative notation to describe turning on sources." Wrong. It is a powerful algebraic tool in Laplace.
- "To write a piecewise function just set $$ u(t-a)f(t) $$." Not enough. Need to be careful about shifting the argument to $$ f(t-a) $$ to use the standard formula.
- "The factor $$ e^{-as} $$ is something to memorize mechanically." Wrong. It directly reflects the signal being time-delayed.
- "Discontinuous problems must be solved on each interval." No longer true when using Laplace.

## Suggested Learning Sequence
### Step 1: Learn to write piecewise functions using Heaviside
This is the most important modeling step.

### Step 2: Convert to the form
$$ u(t-a)f(t-a) $$
to use the shifting formula.

### Step 3: Apply Laplace and solve algebra as usual
No need to change the major workflow.

### Step 4: Return to time domain
Read the meaning of on/off signals in the final solution.

### Checkpoints
- Can students correctly write a piecewise function using Heaviside?
- Do students understand why the argument must be shifted to $$ t-a $$?
- Can students explain the meaning of the factor $$ e^{-as} $$?

## Detailed Examples
### Example 1: Writing Piecewise Functions with Heaviside
Consider the function
$$
f(t)=
\begin{cases}
0, & 0\le t<2,\\
3, & t\ge 2.
\end{cases}
$$
We write compactly:
$$ f(t)=3u(t-2). $$
Therefore
$$ \mathcal{L}\{f(t)\}=3\frac{e^{-2s}}{s}. $$
This example shows that converting signals to Heaviside is really quite brief.

### Example 2: Turning on a Sine Function Late
Consider the signal
$$
f(t)=
\begin{cases}
0, & 0\le t<1,\\
\sin (t-1), & t\ge 1.
\end{cases}
$$
We write
$$ f(t)=u(t-1)\sin (t-1). $$
Since
$$ \mathcal{L}\{\sin t\}=\frac{1}{s^2+1}, $$
we get
$$ \mathcal{L}\{f(t)\}=e^{-s}\frac{1}{s^2+1}. $$
The pedagogical point here is that the inside part must be $$ t-1 $$, not $$ t $$, if we want to apply the shifting theorem directly.

### Example 3: Solving IVP with Delayed Source
Solve
$$ y'+y=u(t-2),\qquad y(0)=0. $$
Apply Laplace:
$$ \left(sY\right)+Y=\frac{e^{-2s}}{s}. $$
Thus
$$ Y=\frac{e^{-2s}}{s(s+1)}. $$
We know
$$ \frac{1}{s(s+1)}=\frac{1}{s}-\frac{1}{s+1}, $$
so
$$
\mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}=1-e^{-t}.
$$
By the shifting theorem:
$$ y(t)=u(t-2)\left(1-e^{-(t-2)}\right). $$
The solution shows the system remains still until time 2, then begins advancing to steady state.

### Example 4: Signal Turned On Then Off
Consider a signal equal to 5 on the interval from 1 to 3 and equal to 0 outside that interval. We write
$$ f(t)=5u(t-1)-5u(t-3). $$
This is a very good example to show students that Heaviside is exactly like operating an on/off switch.

## Conceptual Questions
1. Why does the factor $$ e^{-as} $$ directly reflect the signal being time-delayed?
2. Why do we need to write the function in the form $$ u(t-a)f(t-a) $$ instead of just $$ u(t-a)f(t) $$ in many cases?
3. What is the greatest advantage of Heaviside in modeling?

## Application Problems
1. An electrical switch only turns on power after 3 seconds. Describe the forcing using Heaviside and explain the physical meaning of the delay factor.
2. A mechanical system bears a constant force during a time interval then is cut off. Explain why Heaviside is more suitable than manually dividing the problem.
3. A control signal has transmission delay. Discuss how Laplace describes that delay.

## Interactive Teaching Strategies
- Start with a graph of an on/off signal and ask students to write it using Heaviside before introducing the formula.
- Have students practice converting between verbal description, piecewise description, and Heaviside description.
- Ask the class: "If the source only starts at the fifth second, what changes in the $$ s $$ domain?"
- Use matching activities between graphs and Heaviside expressions to increase intuition.

## Learning Differentiation
### Support for Struggling Students
Struggling students should do many exercises translating between "piecewise function" and "Heaviside" before going into ODEs. This lesson is often harder at the modeling stage than at the Laplace calculation stage.

### Challenge for Advanced Students
Advanced students can be asked to handle multi-level signals or multiple on/off cycles, or write the same signal with several equivalent Heaviside expressions then compare.

## Memorable Summary
The Heaviside step function is the switch of Laplace. It helps write on/off signals compactly and transforms time delay into the factor $$ e^{-as} $$ in the $$ s $$ domain. To use it correctly, practice writing signals in the form
$$ u(t-a)f(t-a). $$

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Switching on a circuit source
- Problem: A voltage source turns on only after time $$ a $$.
- Model:
$$ u(t-a)V_0. $$
- Assumptions and limitations: The switch is ideal and has no finite transition time.
- Interpretation: Heaviside models the delayed activation compactly, while the delay becomes $$ e^{-as} $$ in the Laplace domain.

#### Piecewise mechanical loading
- Problem: A beam or vibrating system receives a load only during part of the experiment.
- Model:
$$ F(t)=u(t-a)-u(t-b) $$
or scaled versions of this form.
- Assumptions and limitations: Loads start and stop instantaneously.
- Interpretation: One expression replaces interval-by-interval solving.

#### Delayed economic intervention
- Problem: A policy begins only after a known time.
- Model:
$$ u(t-a)f(t-a). $$
- Assumptions and limitations: The effect turns on sharply rather than gradually.
- Interpretation: A piecewise model becomes a single Laplace problem.

### 2. Conceptual Insight

Heaviside is the switch of the Laplace chapter. This lesson is where modeling becomes central again. The biggest common mistake is writing $$ u(t-a)f(t) $$ and then applying the standard shifting theorem directly. To use the standard formula cleanly, students should rewrite in the form $$ u(t-a)f(t-a) $$.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 600)
u2 = (t >= 2).astype(float)
signal = u2 * np.sin(t - 2)

plt.plot(t, u2, label="u(t-2)")
plt.plot(t, signal, label="u(t-2) sin(t-2)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("A delayed signal built with the Heaviside step")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: Heaviside step function Laplace visualization
- search: delayed input signal animation
- search: piecewise forcing differential equation Laplace

### 5. Worked Example

A source turns on at $$ t=2 $$ with amplitude 3:
$$
f(t)=
\begin{cases}
0, & 0\le t<2,\\
3, & t\ge 2.
\end{cases}
$$
Write it as
$$ f(t)=3u(t-2). $$
Then
$$ \mathcal{L}\{f(t)\}=3\frac{e^{-2s}}{s}. $$
If this forcing is inserted into a linear ODE, the usual Laplace workflow still applies without solving separately on each interval.

### 6. Difficulty Layering

**Undergraduate level.** Learn to translate piecewise signals into Heaviside form and use time shifting correctly.

**Graduate level.** Work with multiple switching times and compare equivalent Heaviside representations.

![Step functions]({{ site.imgurl }}/chapter_img/chapter03/03_05_step_functions.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: explains the time-shifting theorem very clearly.
- Zill — *Differential Equations with Boundary-Value Problems*: many good technical examples of discontinuous signals.
- Ross — *Differential Equations*: suitable for quickly reviewing Heaviside operations.
