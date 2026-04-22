---
layout: post
title: "03-06 Impulse Functions and the Delta Distribution"
chapter: '03'
order: 6
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: required
---
## Learning Objectives
This lesson helps students understand the Dirac delta as an idealized model of an instantaneous impulse, learn the Laplace of delta, and interpret the relationship between impulsive force, derivative jumps, and the response of linear systems. This is the lesson that strongly transitions from discontinuous signals to signals concentrated at a single moment.

## Prerequisites
Students need to master Heaviside, basic Laplace, and intuition about signals with finite area or impact. Some physics background on impulsive force in mechanics will make this lesson very natural.

## Introduction
![Illustration for Lesson 03-06 Impulse Functions and the Delta Distribution]({{ site.imgurl }}/chapter_img/chapter03/03_06_impulse_functions.svg)

A hammer strike on an object, an extremely short electrical pulse, an instantaneous jolt to an oscillating system: all have very small duration but still transmit a finite amount of impact. If we try to model such events with ordinary functions, we must work with pulses that become increasingly narrow and tall. The Dirac delta appears as the perfect idealization for this type of forcing.

This lesson is very important because it opens the language of impulse response. In systems theory, if we know how a system reacts to a delta, we nearly know the entire system. Therefore, delta is not just a strange object from analysis; it is the cornerstone of linear system analysis.

## Three Ways to Understand the Concept
### Intuitive View
The Dirac delta can be seen as a strike that is "infinitely short but with finite total impact." It is not an ordinary function with finite values at every point, but a distribution concentrating all mass at exactly one moment.

### Visual View
We imagine a sequence of pulses that become increasingly narrow and increasingly tall, but always have area equal to 1. When the width approaches 0, that sequence approaches delta. The important image is not the height, but the area: that is the total impact of the pulse.

### Formal View
The Dirac delta at $$ t=a $$ is denoted $$ \delta(t-a) $$ and satisfies the sifting property:
$$ \int_{-\infty}^{\infty} f(t)\delta(t-a)\,dt=f(a) $$
with appropriate assumptions. In Laplace, we have
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
This is an extremely beautiful formula because it shows delta is the "differential sibling" of Heaviside in an intuitive sense.

## Common Misconceptions
- "Delta is a function that takes infinite value at one point and 0 elsewhere." This is only intuitive, not the standard definition.
- "Delta is unrealistic because it doesn't exist physically." Wrong. It is a very useful idealized model for very short pulses.
- "The Laplace of delta is complicated because delta itself is strange." Actually the Laplace formula for delta is very simple.
- "Impulses just make the solution jump." Need to be careful: usually the position solution is continuous, but the derivative may jump.

## Suggested Learning Sequence
### Step 1: Understand delta as the limit of narrow pulses
This is the best intuitive starting point.

### Step 2: Master the sifting property
This is the central working formula.

### Step 3: Learn the Laplace of delta
Connect with Heaviside and time delay.

### Step 4: Interpret the jump of the system
Connect directly with mechanics and linear systems.

### Checkpoints
- Can students distinguish between "point value" and "integral impact" of delta?
- Do students remember
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as} $$
and understand the reason?
- Can students interpret which quantity the impulse changes in the system?

## Detailed Examples
### Example 1: Laplace of Delta
Compute
$$ \mathcal{L}\{\delta(t-a)\}. $$
By Laplace definition:
$$
\mathcal{L}\{\delta(t-a)\}=\int_0^\infty e^{-st}\delta(t-a)\,dt.
$$
Apply the sifting property:
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
This example shows delta converts to a very compact delay factor in the $$ s $$ domain.

### Example 2: Oscillation Problem with Impulse
Solve
$$ y''+y=\delta(t-\pi),\qquad y(0)=0,\qquad y'(0)=0. $$
Apply Laplace:
$$ \left(s^2Y\right)+Y=e^{-\pi s}. $$
Thus
$$ Y=\frac{e^{-\pi s}}{s^2+1}. $$
Since
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\}=\sin t,
$$
by the shifting theorem:
$$ y(t)=u(t-\pi)\sin (t-\pi). $$
The solution shows the system remains still until exactly the moment of receiving the impulse, then begins oscillating like a free response instantly activated.

### Example 3: Derivative Jump
With the equation
$$ y''=\delta(t-a), $$
we integrate both sides over a very small neighborhood around $$ a $$:
$$
\int_{a^-}^{a^+} y''(t)\,dt=\int_{a^-}^{a^+}\delta(t-a)\,dt=1.
$$
Therefore
$$ y'(a^+)-y'(a^-)=1. $$
This shows the impulse creates a jump in velocity, very consistent with mechanical intuition about impulsive force.

### Example 4: Delta as Derivative of Heaviside
At an intuitive level, we can view
$$ \frac{d}{dt}u(t-a)=\delta(t-a). $$
This helps students connect the Heaviside lesson with the delta lesson: step and impulse are not separate, but two levels of describing sudden change.

## Conceptual Questions
1. Why is the area of the pulse more important than the maximum height in the intuition about delta?
2. Why does an impulse usually make the derivative jump rather than necessarily making the solution itself jump?
3. In systems theory, why is knowing the response to delta especially important?

## Application Problems
1. An object undergoes an instantaneous collision. Explain why velocity changes suddenly while position usually remains continuous.
2. An electrical circuit receives a very short electrical pulse. Discuss why the delta model is reasonable.
3. In signal processing, why is a linear system often characterized by its impulse response?

## Interactive Teaching Strategies
- Use images of a sequence of increasingly narrow pulses with the same area to build intuition before writing delta notation.
- Ask the class: "Does a hammer strike change position or velocity immediately?"
- Have students compare Heaviside and delta as two types of "turn on" and "strike" signals.
- Ask students to explain in words the meaning of the solution
$$ u(t-\pi)\sin(t-\pi). $$

## Learning Differentiation
### Support for Struggling Students
Keep the lesson at the level of sifting intuition and Laplace, avoiding overload with abstract distribution language. When students see clear mechanical applications, they usually accept delta more easily.

### Challenge for Advanced Students
Advanced students can be asked to relate delta to the weak derivative of Heaviside, or build the impulse response of a second-order system then compare with step response.

## Memorable Summary
The Dirac delta models a very short pulse with finite impact. In Laplace,
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
Impulses usually make the derivative of the solution jump. If Heaviside is a switch, then delta is an instantaneous strike.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Hammer strike on an oscillator
- Problem: A very short hit transfers finite momentum to a mechanical system.
- Model:
$$ y''+\omega^2 y=\delta(t-a). $$
- Assumptions and limitations: The pulse is idealized as instantaneous.
- Interpretation: The system is quiescent before the impulse and begins a free response immediately afterward.

#### Electrical pulse input
- Problem: A circuit receives an extremely short excitation pulse.
- Model:
$$ Lq''+Rq'+\frac{1}{C}q=\delta(t-a). $$
- Assumptions and limitations: The pulse is short enough that its detailed waveform can be ignored.
- Interpretation: Delta unifies pulse modeling across mechanics, circuits, and system theory.

#### Impulsive control
- Problem: A system is corrected by short strong control actions.
- Model:
$$ \delta(t-a) $$
or sums of shifted deltas.
- Assumptions and limitations: Idealized instantaneous actuation.
- Interpretation: The impulse response nearly characterizes the full linear system.

### 2. Conceptual Insight

Delta is the natural successor to Heaviside: if Heaviside flips a switch, delta delivers an instantaneous strike. In modern analysis it is a distribution, not an ordinary function, but at this course level the intuition of finite area concentrated at one instant is already very effective.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 800)
eps_values = [0.25, 0.12, 0.06]

for eps in eps_values:
    pulse = np.exp(-(t / eps)**2) / (eps * np.sqrt(np.pi))
    plt.plot(t, pulse, label=f"eps={eps}")

plt.xlabel("t")
plt.ylabel("Pulse height")
plt.title("Narrow pulses approaching delta")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: Dirac delta intuition narrow pulse
- search: impulse response oscillator animation
- search: delta function Laplace transform visualization

### 5. Worked Example

Consider
$$ y''+y=\delta(t-\pi),\qquad y(0)=0,\qquad y'(0)=0. $$
Taking Laplace,
$$
(s^2+1)Y=e^{-\pi s},
\qquad
Y=\frac{e^{-\pi s}}{s^2+1}.
$$
Since
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\}=\sin t,
$$
we obtain
$$ y(t)=u(t-\pi)\sin(t-\pi). $$
The physical interpretation is clean: the system is inactive until the strike, then oscillates.

### 6. Difficulty Layering

**Undergraduate level.** Learn the sifting property, Laplace transform of delta, and jump interpretation.

**Graduate level.** Connect delta with weak derivatives of Heaviside and with impulse-response theory.

![Impulse functions]({{ site.imgurl }}/chapter_img/chapter03/03_06_impulse_functions.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: explains delta in the spirit of applications very appropriately.
- Zill — *Differential Equations with Boundary-Value Problems*: many good examples of impulse response.
- Ross — *Differential Equations*: brief but very effective for mechanical intuition of impulses.
