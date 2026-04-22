---
layout: post
title: "01-08 Applications: Mechanics and Circuits"
chapter: '01'
order: 8
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

## Objectives

This lesson shows students that basic physical laws lead to ODE almost automatically. Through falling motion with drag, RC circuits, and RL circuits, students learn how Newton's law and Kirchhoff's law become differential equations, how to solve those equations, and how to interpret parameters such as time constants, terminal velocity, and response speed.

## Prerequisites

Students should be comfortable with first-order linear equations and a small amount of basic physical language: force, velocity, voltage, charge, and current. Deep physics background is not required. What matters most is seeing how balance laws create differential equations naturally.

## Introduction

If an object falls through air, it does not speed up forever. Drag grows and eventually balances gravity, creating a terminal velocity. If a capacitor is connected to a source, its charge does not jump instantly to the final value. It builds gradually. If an RL circuit is switched on, current does not immediately reach steady state either. These familiar phenomena are all lessons about change in time.

The beauty of mechanics and circuit examples is that every parameter has a clear physical meaning. This allows students to connect the mathematical solution directly to the real world: which term creates resistance, which parameter sets the response speed, and why a steady state appears.

## The Concept in Three Ways

### Intuitive View

In mechanics with linear drag, gravity pulls downward while the medium pushes back, so the velocity approaches a limiting value. In a circuit, the source drives the system toward equilibrium while resistance prevents instantaneous response.

### Visual View

A falling-velocity graph with linear drag usually rises quickly at first and then flattens as it approaches terminal velocity. The charging curve of an RC circuit has the same overall shape: fast change initially, then leveling near a final state. These graphs are signatures of stable first-order linear behavior.

### Formal View

Standard models include:

Falling body with linear drag:
$$ m\frac{dv}{dt}=mg-cv. $$

RC circuit:
$$ R\frac{dq}{dt}+\frac{1}{C}q=E(t). $$

RL circuit:
$$ L\frac{di}{dt}+Ri=E(t). $$

Each becomes a first-order linear equation after dividing by the coefficient of the derivative term.

## Core Modeling Ideas

In these examples, the ODE comes directly from a balance law. In mechanics, total force equals mass times acceleration. In circuits, Kirchhoff's law balances voltage drops. Once the equation is written, the problem returns to the framework students already know: identify the standard form, apply the integrating factor, and then interpret the meaning of the result.

An important teaching point is that the parameters are not just symbols. Ratios such as $$ m/c $$, $$ RC $$, and $$ L/R $$ give characteristic response times of the system.

## Common Misconceptions

### "A falling object always accelerates forever"

False. With linear drag, the velocity approaches a terminal limit.

### "When a source is switched on, current or charge reaches steady state immediately"

False. Real first-order models include a transient response.

### "Resistance only changes the final value"

False. It also affects how quickly the system approaches that value.

### "Physical parameters are just numbers to substitute"

False. Each one carries structural information about the dynamics.

## Learning Progression

### Step 1: Write the physical law

Identify the force balance or voltage balance first.

### Step 2: Choose the state variable

Velocity $$ v(t) $$, charge $$ q(t) $$, or current $$ i(t) $$ should be chosen deliberately.

### Step 3: Put the equation in standard linear form

Divide through so that the derivative has coefficient 1.

### Step 4: Solve and interpret steady state

Do not stop at the formula. Ask where the solution tends and how fast it gets there.

### Key Checkpoints

- Can students choose the correct sign for drag or resistance terms?
- Can they find the steady state by setting the derivative equal to zero?
- Can they explain the time constant in words?

## Worked Examples

### Example 1: Falling body with linear drag

Choose downward as positive. If a mass $$ m $$ experiences gravity $$ mg $$ and drag $$ cv $$ upward, then

$$ m\frac{dv}{dt}=mg-cv. $$

Rewriting,

$$ \frac{dv}{dt}+\frac{c}{m}v=g. $$

This is a first-order linear equation. Its steady state is the terminal velocity

$$ v_{\infty}=\frac{mg}{c}. $$

### Example 2: RC charging circuit

For a constant source $$ E_0 $$, the equation

$$ R\frac{dq}{dt}+\frac{1}{C}q=E_0 $$

describes charging. The long-term steady state is $$ q_{\infty}=CE_0 $$. The approach rate is governed by the time constant $$ RC $$.

### Example 3: RL circuit

With constant source $$ E_0 $$,

$$ L\frac{di}{dt}+Ri=E_0 $$

gives a current that approaches

$$ i_{\infty}=\frac{E_0}{R}. $$

The time scale is controlled by $$ L/R $$.

### Example 4: Reading the graph physically

In all of these first-order models, the initial behavior is influenced strongly by the starting condition, but the long-term behavior is dominated by the steady state and the response time. This is one of the main ideas students should carry into later applications.

## Conceptual Questions

1. Why do drag and resistance naturally produce first-order linear equations?
2. Why does setting the derivative equal to zero reveal the steady state?
3. Why is the time constant often more informative than the full exact formula?

## Application Problems

1. In a parachute model, how does increasing drag change the terminal velocity and response speed?
2. In an RC circuit, how does doubling resistance affect charging time?
3. In an RL circuit, how would you explain the role of inductance to a student who only knows mechanical inertia?

## Interactive Teaching Strategies

### Questions to Ask in Class

- Which term drives the system, and which term resists change?
- Why does the graph flatten instead of growing forever?
- What physical meaning should we attach to the steady-state value?

### Suggested Activities

- Have students derive the falling-body and circuit equations directly from laws before solving them.
- Compare the shapes of the solution graphs for different parameter values.
- Ask groups to interpret the same solution formula from both mathematical and physical viewpoints.

### Participation Moves

- Start from the physical story before introducing the equation.
- Ask students to explain each term in ordinary language.
- Repeatedly connect the final formula to a visible physical behavior.

## Differentiation

### Support for Struggling Students

- Keep the focus on one model at a time.
- Use sign diagrams to avoid mistakes in force or voltage balance.
- Emphasize steady-state reasoning before full solution methods.

### Challenge for Advanced Students

- Compare transient and steady-state behavior quantitatively.
- Explore time-dependent forcing $$ E(t) $$ in circuit models.
- Connect the first-order response to broader ideas of damping and relaxation.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Skydiver with linear drag
- Problem: We want a first estimate of how fast a falling body approaches a safe or unsafe speed range.
- Model:
$$ m\frac{dv}{dt}=mg-cv. $$
- Assumptions and limitations: Posture and drag coefficient are constant, and the drag law is linear. At higher speed, quadratic drag is often more realistic.
- Interpretation: The solution reveals terminal velocity directly.

#### RC smoothing circuit
- Problem: A sensor output should be smoothed before it is sent to the next stage of a device.
- Model:
$$ RC\frac{dV}{dt}+V=V_{\mathrm{in}}(t). $$
- Assumptions and limitations: The circuit is ideal and linear.
- Interpretation: The time constant $$ RC $$ quantifies the tradeoff between responsiveness and smoothing.

#### Simple cruise control
- Problem: A vehicle aims to reach a target speed under nearly constant engine force and speed-proportional drag.
- Model:
$$ m\frac{dv}{dt}=F_0-bv. $$
- Assumptions and limitations: Flat road, no gear changes, and no actuator delay are assumed.
- Interpretation: The mathematics is the same as in the falling-body model, which is a powerful lesson in structural similarity.

### 2. Conceptual Insight

Mechanics and circuits show students that parameters are part of the meaning of the equation, not just numbers to substitute. Mass, resistance, drag, and inductance determine both equilibrium values and response times. A common misconception is to focus only on the final value and forget that engineering performance often depends even more on the transient.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
g = 9.81
m = 80.0

for c in [10, 20, 40]:
    v = (m * g / c) * (1 - np.exp(-c * t / m))
    plt.plot(t, v, label=f"c={c}")

plt.xlabel("t")
plt.ylabel("v(t)")
plt.title("Falling velocity for different drag coefficients")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Students immediately see that larger drag changes both the limiting speed and the approach rate.

### 4. External Search Prompts

- search: falling body with drag simulation
- search: RC circuit step response interactive
- search: RL circuit transient plot

### 5. Worked Example

An 80 kilogram skydiver falls with linear drag coefficient $$ c=20 $$ kg/s from rest. Then
$$ 80\frac{dv}{dt}=80\cdot 9.81-20v,
\qquad
v(0)=0. $$
The solution is
$$ v(t)=39.24\left(1-e^{-t/4}\right). $$
The time constant is four seconds, so after about three time constants the velocity is already very close to terminal value.

### 6. Difficulty Layering

**Undergraduate level.** Build the ODE from Newton's law or Kirchhoff's law and interpret the resulting time constant.

**Graduate level.** Connect to transfer functions, impulse response, energy dissipation, and more realistic nonlinear drag or nonideal circuits.

![Falling body with drag]({{ site.imgurl }}/chapter_img/chapter01/01_08_applications_mechanics_circuits.svg)

![RC and RL circuits]({{ site.imgurl }}/chapter_img/chapter01/01_08_circuits_detail.svg)

## Quick Summary

Mechanics and circuit models show how physical balance laws naturally produce first-order ODE. The mathematics is important, but the deeper lesson is that parameters, steady states, and response times all carry concrete physical meaning.
