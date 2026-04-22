---
layout: post
title: "02-09 RLC Circuits"
chapter: '02'
order: 9
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: required
---
## Learning Objectives
This lesson helps students see how second-order equations arise in RLC electrical circuits, understand the structural analogy between circuits and mechanical oscillations, solve basic free and forced problems, and interpret the parameters resistance, inductance, and capacitance in dynamic language.

## Background Knowledge
Students should grasp second-order linear constant-coefficient ODEs, mechanical oscillations, and Kirchhoff's law. Deep electronics background is not needed; what's more important is knowing charge $$ q(t) $$, current $$ i(t)=q'(t) $$, and voltage across each element.

## Introduction
![Diagram for Lesson 02-09 RLC Circuits]({{ site.imgurl }}/chapter_img/chapter02/02_09_rlc_circuits.svg)

The RLC circuit is one of the most beautiful examples of the unity of applied mathematics. On one side is mass-spring-damper in mechanics. On the other is inductor-capacitor-resistor in circuits. Though the physical nature is different, both lead to the same second-order ODE structure. This helps students see that mathematics not only solves problems, but also reveals that phenomena from different fields share the same backbone.

In RLC circuits, inductance plays the role of inertia, resistance plays the role of damping, and capacitance creates the restoring mechanism. Therefore, the regimes of overdamped, critically damped, underdamped, and electrical resonance can all be read using the very language learned in mechanical oscillations.

## Three Ways to Understand the Concept
### Intuitive View
If mechanics is "an object doesn't want to change velocity instantly," then inductance is "current doesn't want to change instantly." If a spring stores elastic energy, a capacitor stores electric field energy. Resistance dissipates energy like friction.

### Visual View
Charge or current in an RLC circuit can oscillate, decay, or approach equilibrium without oscillation depending on parameters. Signal graphs over time look very similar to mechanical oscillation graphs: can be decaying sine-cosine, double exponential decay, or resonant response.

### Formal View
According to Kirchhoff's law for series RLC circuit:
$$
L\frac{d^2q}{dt^2}+R\frac{dq}{dt}+\frac{1}{C}q=E(t),
$$
where $$ q(t) $$ is charge on capacitor and $$ i(t)=q'(t) $$ is current. If
$$ E(t)=0, $$
we have free response. If $$ E(t)\neq 0 $$, we have forced response.

## Common Misconceptions
- "Electrical circuits only lead to first-order equations." Wrong. Series RLC circuits naturally lead to second-order ODEs.
- "The larger the resistance, the faster the system returns to equilibrium." Not necessarily. Too large can make the system return slower compared to critical damping.
- "If there is oscillation then the circuit definitely has no resistance." Wrong. Damped oscillation appears when resistance is present but not too large.
- "Resonance is only a mechanical concept." Wrong. It is very important in electronics and signal processing.

## Suggested Learning Progression
### Step 1: Write Kirchhoff's law
Sum of voltages across inductor, resistor, and capacitor equals external source.

### Step 2: Choose state variable
Usually charge $$ q(t) $$, then current follows from $$ q'(t) $$.

### Step 3: Analyze homogeneous part
Read regime from characteristic equation.

### Step 4: If source present, find forced solution
Distinguish transient and steady-state parts.

### Checkpoints
- Can the student correctly write the equation for $$ q(t) $$?
- Can the student see the analogy between RLC and mechanical oscillation?
- Can the student interpret the long-term signal in the circuit?

## Worked Examples
### Example 1: Circuit Without Source
Consider
$$ q''+4q'+5q=0. $$
The characteristic equation:
$$ r^2+4r+5=0, $$
gives
$$ r=-2\pm i. $$
Thus
$$ q(t)=e^{-2t}\left(c_1\cos t+c_2\sin t\right). $$
Charge oscillates and decays to 0. Current $$ i=q' $$ also decays.

### Example 2: Critical Damping in Circuit
Consider
$$ q''+6q'+9q=0. $$
We have repeated root $$ r=-3 $$, so
$$ q(t)=\left(c_1+c_2t\right)e^{-3t}. $$
This is non-oscillatory response but approaches 0 fastest in the non-oscillatory class.

### Example 3: Circuit with Constant Source
Consider
$$ q''+3q'+2q=10. $$
Homogeneous solution:
$$ q_h=c_1e^{-t}+c_2e^{-2t}. $$
Try constant particular solution $$ q_p=A $$:
$$ 2A=10 \Rightarrow A=5. $$
Thus
$$ q(t)=c_1e^{-t}+c_2e^{-2t}+5. $$
This shows the circuit gradually approaches a steady charge state of 5.

### Example 4: Periodic Source and Resonance
Consider
$$ q''+q=\cos t. $$
This is an ideal model without damping, and forcing matches natural frequency. The particular solution has resonance form:
$$ q_p=\frac{1}{2}t\sin t. $$
Therefore
$$ q(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Amplitude grows with time, showing clear electrical resonance.

## Conceptual Questions
1. Why do RLC circuits and mechanical systems have the same equation structure?
2. How does resistance affect signals in a way analogous to mechanical damping?
3. In a circuit with periodic source, why must transient and steady-state parts be separated?

## Application Problems
1. A signal filter circuit needs to eliminate transient oscillations quickly. Explain the role of resistance in the design.
2. A radio resonance circuit needs to be sensitive to one particular frequency. Relate this to the circuit's natural frequency.
3. An electronic sensor has oscillating signal vibration before stabilizing. Explain this phenomenon using RLC language.

## Interactive Teaching Strategies
- Have students match mechanical and electrical quantities: mass with inductance, friction with resistance, spring with capacitance.
- Have the class directly compare two equations: one for spring, one for RLC circuit, then discuss what is similar and different.
- Ask students: "If we increase resistance, how do you predict the signal will oscillate less?"
- Can use simple circuit simulation or step response images to enhance intuition.

## Differentiation
### Support for Struggling Students
Use a parallel table between mechanics and electronics so students don't find the electrical part too foreign. When they see the ODE structure is the same, they are usually much more confident.

### Challenge for Advanced Students
Advanced students can be asked to compute the transfer function of a simple RLC circuit or investigate steady-state amplitude under periodic forcing as a function of source frequency.

## Memorable Summary
The RLC circuit is the electrical version of mechanical oscillation. The equation
$$ Lq''+Rq'+\frac{1}{C}q=E(t) $$
tells the whole story: inductance like inertia, resistance like damping, capacitance like restoring. Understanding this, many electrical phenomena become as familiar as spring problems.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Second-order electronic filters
- Problem: RLC circuits are used to select or suppress frequency bands in signal processing.
- Model:
$$ Lq''+Rq'+\frac{1}{C}q=E(t). $$
- Assumptions and limitations: Ideal linear components.
- Interpretation: The system may oscillate, decay, or resonate depending on parameters and input frequency.

#### Switching transients
- Problem: After a circuit is turned on, charge and current do not jump to steady state instantly.
- Model: Again the RLC equation.
- Assumptions and limitations: Nonlinear switching devices are ignored.
- Interpretation: The homogeneous solution captures transients, while the particular solution captures the driven operating state.

#### Electromechanical resonant sensing
- Problem: A device is designed to respond strongly near one preferred frequency.
- Model:
$$ Lq''+Rq'+\frac{1}{C}q=E_0\cos \omega t. $$
- Assumptions and limitations: One dominant mode and sinusoidal forcing.
- Interpretation: Electrical resonance is the circuit analogue of mechanical resonance.

### 2. Conceptual Insight

RLC circuits are a unification lesson. Inductance behaves like inertia, resistance like damping, and capacitance like restoring force. Once students really see that analogy, the mathematics becomes much easier to organize. A common misconception is that larger resistance always improves performance; too much resistance can actually slow the nonoscillatory return compared with critical damping.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
q = np.exp(-2*t) * (np.cos(t) + 0.5*np.sin(t))
i = np.gradient(q, t)

plt.plot(t, q, label="Charge q(t)")
plt.plot(t, i, label="Current i(t)=q'(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Damped RLC response")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Plotting charge and current together helps students understand why charge is often chosen as the primary state variable.

### 4. External Search Prompts

- search: RLC circuit resonance interactive
- search: transient response RLC animation
- search: circuit mechanical analogy visualization

### 5. Worked Example

Consider
$$ q''+4q'+5q=0,\qquad q(0)=1,\qquad q'(0)=0. $$
The solution has the form
$$ q(t)=e^{-2t}\left(c_1\cos t+c_2\sin t\right). $$
Applying the initial data gives
$$ q(t)=e^{-2t}\left(\cos t+2\sin t\right). $$
Then
$$ i(t)=q'(t) $$
also decays to zero. Physically, energy oscillates between the inductor and capacitor while resistance drains it away.

### 6. Difficulty Layering

**Undergraduate level.** Write the RLC equation correctly and compare it with the mechanical vibration model.

**Graduate level.** Connect with transfer functions, frequency response, and filter design intuition.

![RLC circuit responses]({{ site.imgurl }}/chapter_img/chapter02/02_09_rlc_circuits.svg)

![RLC response analysis]({{ site.imgurl }}/chapter_img/chapter02/02_09_rlc_response.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: the RLC circuit section is very suitable for seeing the analogy with mechanics.
- Zill — *Differential Equations with Boundary-Value Problems*: many exercises on transient and forced response.
- Ross — *Differential Equations*: concise and good for reviewing model structure.
