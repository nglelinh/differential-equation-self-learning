---
layout: post
title: "01-07 Applications: Population and Mixing"
chapter: '01'
order: 7
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

## Objectives

This lesson shows how ODE leave the page and become working models of real systems. Through population growth and mixing problems, students learn how to translate everyday language into differential equations, solve the resulting models, interpret the meaning of solutions, and judge whether a model is too simple or reasonably persuasive for the question at hand.

## Prerequisites

Students should know separable equations, first-order linear equations, and the habit of checking units. Application problems become mechanical very quickly if students do not understand the meaning of each quantity, so unit analysis and "rate in minus rate out" reasoning are especially important here.

## Introduction

A good mathematical model does not begin with a clever formula. It begins with the right question. Population changes because of births and deaths. Salt concentration changes in a tank because material flows in and flows out. The key step is to choose a state variable and then write its rate of change as the sum of the mechanisms acting on it. Once that is done, ODE become the natural bridge between observation and prediction.

These two model families are especially valuable pedagogically. Population models reveal growth, saturation, and the role of equilibrium. Mixing problems train one of the most universal principles in applied science: rate of change equals rate in minus rate out.

## The Concept in Three Ways

### Intuitive View

In population models, a larger population often creates more births, but finite resources prevent indefinite growth. In a mixing tank, the amount of dissolved substance changes because some is added and some is removed. Both settings are fundamentally balance laws.

### Visual View

The graph of exponential growth and the graph of logistic growth look very different. Exponential growth keeps bending upward without limit, while logistic growth first rises quickly and then levels off near a carrying capacity. In a mixing problem, the amount of salt often moves toward a balance value, showing that the system gradually forgets its initial state and becomes controlled by the long-term input.

### Formal View

Three standard models are:

Exponential growth:
$$ \frac{dP}{dt}=rP. $$

Logistic growth:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$

Constant-volume mixing:
$$ \frac{dS}{dt}=\text{rate in}-\text{rate out}. $$

If the tank is well mixed, then the rate out is usually the outflow rate times the current concentration.

## Core Modeling Ideas

In every application problem, the most important step is the choice of state variable. For population, the state variable is the number of individuals $$ P(t) $$. For a tank problem, it is often the amount of dissolved substance $$ S(t) $$ rather than the concentration itself, unless concentration is chosen deliberately from the start. Then we write the rate balance.

One important teaching point is that modeling is not the same as solving. If students write the correct ODE but cannot solve it immediately, they have still achieved something mathematically substantial.

## Common Misconceptions

### "Population models are always exponential"

False. Exponential growth is only reasonable in an early stage or when resource limits are ignored.

### "In a mixing problem, the rate out is constant"

False. It usually depends on the current concentration in the tank.

### "If the formula is solvable, then the model must be correct"

False. A clean formula can still come from unrealistic assumptions.

### "Equilibrium is just a formal concept"

False. In applications, it often represents the long-term state that the system approaches.

## Learning Progression

### Step 1: Choose the state variable

Ask clearly which quantity is changing in time.

### Step 2: Write a rate balance

For population, use net growth. For mixing, use rate in minus rate out.

### Step 3: Check units

Both sides of the equation must carry consistent units such as kg/minute or individuals/day.

### Step 4: Solve and interpret

Do not stop at the formula. Ask what happens in the long run and what the parameters mean.

### Key Checkpoints

- Can students choose the correct state variable?
- Can they write the correct outflow term using the current concentration?
- Can they explain the difference between exponential and logistic growth in words?

## Worked Examples

### Example 1: Exponential population growth

Suppose

$$ \frac{dP}{dt}=0.04P,\qquad P(0)=1000. $$

This gives $$ P(t)=1000e^{0.04t} $$. The model predicts unbounded growth, which may be reasonable only in an early phase.

### Example 2: Logistic growth

Suppose

$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$

Then $$ P=0 $$ and $$ P=K $$ are equilibria. The carrying capacity $$ K $$ provides a built-in saturation mechanism, which exponential growth lacks.

### Example 3: Mixing in a constant-volume tank

Let $$ S(t) $$ be the amount of salt in the tank. If brine flows in with concentration $$ c_{\text{in}} $$ at rate $$ q $$ and the tank volume is constant $$ V $$, then

$$ \frac{dS}{dt}=qc_{\text{in}}-q\frac{S}{V}. $$

This is a first-order linear equation. The outflow term depends on the current tank concentration $$ S/V $$, not on the initial concentration.

### Example 4: Long-term behavior

In the mixing equation above, the steady state occurs when

$$ \frac{dS}{dt}=0. $$

So the long-term amount satisfies $$ S_{\infty}=Vc_{\text{in}} $$. This gives a useful interpretation: eventually the tank approaches the input concentration.

## Conceptual Questions

1. Why is choosing the right state variable the most important modeling step?
2. Why does logistic growth often describe reality better than exponential growth?
3. Why does the outflow term in a mixing problem depend on the current state of the tank?

## Application Problems

1. Build a population model that includes both growth and harvesting. Which term represents each mechanism?
2. In a medicine-mixing model, why does the concentration in the bloodstream change by an input-minus-removal law?
3. In an ecological model, how would you explain carrying capacity to a non-mathematical audience?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What exactly is changing with time in this real-world problem?
- Which term represents inflow, and which term represents depletion?
- Does the model suggest unlimited growth or eventual stabilization?

### Suggested Activities

- Ask groups to derive the mixing equation from units alone.
- Compare exponential and logistic graphs and have students describe the biological difference.
- Give short application stories and ask students to choose the correct state variable before writing any equation.

### Participation Moves

- Start with ordinary language before formulas.
- Ask students to justify each term physically.
- Encourage discussion about model limitations, not only solution steps.

## Differentiation

### Support for Struggling Students

- Use short word problems with clear units.
- Emphasize "rate in minus rate out" repeatedly.
- Keep the first population examples close to exponential growth.

### Challenge for Advanced Students

- Compare short-term and long-term predictions of different population models.
- Analyze how parameter changes affect equilibria and stability.
- Build more realistic mixing models with changing volume.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Wildlife population with carrying capacity
- Problem: A deer population grows rapidly when small but slows as the habitat fills.
- Model:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$
- Assumptions and limitations: The carrying capacity is fixed and the population is homogeneous.
- Interpretation: The logistic solution predicts approach toward ecological balance.

#### Water-treatment mixing tank
- Problem: Engineers track contaminant mass in a stirred tank with steady inflow and outflow.
- Model:
$$
\frac{dS}{dt}=q_{\mathrm{in}}c_{\mathrm{in}}-q_{\mathrm{out}}\frac{S}{V}.
$$
- Assumptions and limitations: Perfect mixing and constant volume are assumed. Sedimentation and spatial nonuniformity are ignored.
- Interpretation: The equation is a direct rate-in minus rate-out balance law.

#### One-compartment drug infusion
- Problem: Medication is delivered continuously while the body clears it.
- Model:
$$ \frac{dC}{dt}=\frac{u_0}{V}-kC. $$
- Assumptions and limitations: Immediate mixing and first-order elimination are assumed.
- Interpretation: The solution predicts a steady therapeutic level and the time needed to approach it.

### 2. Conceptual Insight

This lesson is where modeling becomes the main skill rather than a decoration around solution methods. Students must choose the right state variable, write the correct balance law, and check units. Logistic growth then connects directly to autonomous equations and phase-line reasoning, while mixing problems connect to conservation principles used throughout engineering and biology.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 0.5, 1000
t = np.linspace(0, 25, 400)
for P0 in [50, 150, 400, 1200]:
    P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
    plt.plot(t, P, label=f"P0={P0}")

plt.axhline(K, color="black", linestyle="--", label="carrying capacity")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Logistic population trajectories")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

The figure makes stable equilibrium visible before the formal phase-line lesson arrives.

### 4. External Search Prompts

- search: mixing tank differential equation simulation
- search: logistic growth carrying capacity interactive
- search: pharmacokinetics one compartment ODE plot

### 5. Worked Example

A tank contains 200 liters of water and 8 kilograms of salt initially. Inflow has concentration 0.05 kg/L and flow rate 4 L/min; outflow is also 4 L/min. Then
$$ \frac{dS}{dt}=0.2-\frac{4}{200}S,
\qquad
S(0)=8. $$
The solution is
$$ S(t)=10-2e^{-0.02t}. $$
Long-term behavior is just as important as the formula: the tank approaches the inflow concentration and gradually forgets its initial state.

### 6. Difficulty Layering

**Undergraduate level.** Practice state-variable choice, unit checking, and physical interpretation of parameters.

**Graduate level.** Discuss positivity, parameter estimation, nondimensionalization, and model identifiability from data.

![Population growth models]({{ site.imgurl }}/chapter_img/chapter01/01_07_applications_population_mixing.svg)

![Mixing tank problem]({{ site.imgurl }}/chapter_img/chapter01/01_07_mixing_detail.svg)

## Quick Summary

Population and mixing models show how first-order ODE emerge naturally from balance laws. The real skill is not only solving the resulting equation, but also choosing the right state variable, building the rate law, and interpreting the meaning of the solution.
