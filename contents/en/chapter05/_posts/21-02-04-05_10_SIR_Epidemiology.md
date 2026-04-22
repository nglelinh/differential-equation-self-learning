---
layout: post
title: "05-10 Applications: SIR Epidemiology"
chapter: '05'
order: 10
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: optional
---

## Learning Objectives

This lesson helps students analyze the SIR model as a nonlinear three-compartment system, interpret the outbreak threshold $$ \mathcal{R}_0 $$, understand the meaning of herd immunity, and see why differential equations are a natural language for basic epidemiology.

## Prerequisites

Students should know compartment models, nonlinear systems, and basic intuition about infection and recovery rates. This lesson also connects naturally with earlier discussions of thresholds and bifurcations.

## Introduction

![SIR epidemiology model and compartment flows]({{ site.imgurl }}/chapter_img/chapter05/10_sir_epidemiology.svg)

An epidemic is not just a list of case counts over time. It is a flow of people between states: susceptible, infected, and removed or recovered. The SIR model is simple enough to teach clearly and rich enough to reveal the most important qualitative ideas in epidemic dynamics.

The model is especially valuable because it makes threshold thinking concrete. An outbreak does not grow simply because infected people exist. It grows only when transmission is strong enough relative to recovery and the remaining susceptible population. This gives rise to the idea of the basic reproduction threshold and, from there, herd immunity.

## Concept in Three Ways

### Intuitive View

Imagine three connected compartments. People leave the susceptible group when they become infected, then leave the infected group when they recover or are removed from transmission. The epidemic curve is the visible result of those flows.

### Visual View

Typical solutions show $$ S(t) $$ decreasing, $$ I(t) $$ rising and then falling, and $$ R(t) $$ increasing. The most important qualitative event is not only the peak of infection, but the moment when the susceptible pool falls below what is needed to sustain growth of the infected class.

### Formal View

The basic SIR model is
$$ \frac{dS}{dt}=-\beta SI, $$
$$ \frac{dI}{dt}=\beta SI-\gamma I, $$
$$ \frac{dR}{dt}=\gamma I. $$
The total population is conserved:
$$ \frac{d}{dt}(S+I+R)=0. $$
Initial outbreak growth is determined by
$$ \dot{I}=I(\beta S-\gamma). $$

## Common Misconceptions

- "If there are infected people, an outbreak must grow." Wrong. Growth depends on the threshold condition.
- "Herd immunity means no infections occur." Wrong. It means sustained epidemic growth is no longer possible.
- "The SIR model is too simple to be useful." Wrong. It is extremely useful as a conceptual starting point.
- "Current case count alone determines the future." Wrong. The susceptible pool matters just as much.

## Suggested Learning Path

### Step 1: Interpret the Compartments

Every term should be understood in words first.

### Step 2: Check Population Conservation

This gives the basic structure of the system.

### Step 3: Analyze the Sign of $$ \dot{I} $$

This is where the outbreak threshold appears naturally.

### Step 4: Connect the Mathematics to Public Health Language

Students should explain what the threshold means operationally.

### Checkpoints

- Can students explain the terms $$ \beta SI $$ and $$ \gamma I $$ in words?
- Do students understand why total population is conserved in the basic model?
- Can students distinguish the outbreak threshold from the epidemic peak?

## Worked Examples

### Example 1: Conserved Population

Adding the three equations gives
$$ \frac{d}{dt}(S+I+R)=0. $$
Therefore
$$ S(t)+I(t)+R(t)=N $$
remains constant.

### Example 2: Initial Growth Condition

Since
$$ \dot{I}=I(\beta S-\gamma), $$
the infected class grows initially when
$$ \beta S(0)>\gamma. $$
If population is normalized to $$ 1 $$, this is often written as a threshold involving
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}. $$

### Example 3: Why the Peak Happens Before Susceptibles Vanish

The epidemic stops growing when
$$ \beta S=\gamma, $$
not when $$ S=0 $$. This is one of the most important conceptual lessons in the model.

## Conceptual Questions

1. Why does the susceptible population play such a central role in outbreak dynamics?
2. Why is the epidemic threshold not the same as the peak time?
3. How does the SIR model embody the idea of herd immunity mathematically?

## Application Problems

1. In public health, why can vaccination reduce outbreak severity even if it does not eliminate every case?
2. In network security, how might an SIR-style compartment model be used as an analogy for malware spread?
3. Why is it misleading to interpret transmission rate alone without considering recovery and susceptible fraction?

## Interactive Teaching Strategies

- Ask students to tell the epidemic story in compartment language before showing formulas.
- Plot $$ S(t) $$, $$ I(t) $$, and $$ R(t) $$ together and discuss what each curve means.
- Emphasize the threshold condition by asking when infection starts to decrease.
- Connect the mathematical threshold to public-health language carefully and precisely.

## Differentiation

### Support for Struggling Students

Students who need support should first master the direction of flow between the three compartments and the conservation of total population.

### Challenge for Advanced Students

Advanced students can extend the model to vaccination, exposed classes, or age-structured contact patterns.

## Summary

The SIR model is a simple but powerful nonlinear compartment system. Its greatest lessons are conservation, threshold behavior, and the dependence of epidemic growth on both transmission and the susceptible pool.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Community influenza outbreak
- Problem: We want to know when the number of infections grows and when it starts to decline.
- Model:
$$
\dot{S}=-\beta SI,\qquad
\dot{I}=\beta SI-\gamma I,\qquad
\dot{R}=\gamma I.
$$
- Assumptions and limitations: The model assumes homogeneous mixing and ignores age structure, births, deaths, and seasonality.
- Interpretation: Initial conditions and transmission parameters determine whether infection rises initially or dies out.

#### Computer-virus spread as a compartment analogy
- Problem: Susceptible, infected, and patched computers can be viewed as three interacting compartments.
- Model: The same SIR structure with infection and recovery interpreted as transmission and patching.
- Assumptions and limitations: Real networks are not well mixed.
- Interpretation: A threshold analogous to $$ \mathcal{R}_0 $$ still gives intuition about outbreak potential.

### 2. Additional Intuition and Connections

SIR is the most important nonlinear compartment model in the chapter. The threshold $$ \mathcal{R}_0 $$ speaks about initial growth of the epidemic, not directly about final outbreak size. A common misunderstanding is to equate herd immunity with zero cases; in reality it means crossing a threshold below which sustained growth is impossible.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

beta, gamma = 0.6, 0.2

def sir(t, z):
    S, I, R = z
    return [-beta * S * I, beta * S * I - gamma * I, gamma * I]

t = np.linspace(0, 80, 1000)
sol = solve_ivp(sir, [0, 80], [0.99, 0.01, 0.0], t_eval=t)

plt.plot(t, sol.y[0], label="S")
plt.plot(t, sol.y[1], label="I")
plt.plot(t, sol.y[2], label="R")
plt.xlabel("t")
plt.ylabel("fraction")
plt.title("Dynamics of the SIR model")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: SIR model interactive simulation
- search: basic reproduction number visualization
- search: herd immunity threshold SIR

### 5. Worked Example

We have
$$ \dot{I}=I(\beta S-\gamma). $$
So if initially
$$ \beta S(0)>\gamma, $$
then infections increase. If total population is normalized to $$ 1 $$, the initial threshold is
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}. $$
This lets students see the outbreak threshold directly from the equations.

### 6. Difficulty Layering

**Undergraduate level.** Understand flows between compartments, total-population conservation, and the initial outbreak condition.

**Graduate level.** Extend to SEIR models, vaccination, next-generation matrices, and stability of the disease-free equilibrium.

![SIR epidemiology]({{ site.imgurl }}/chapter_img/chapter05/05_10_sir_epidemiology.svg)

## References

- Strogatz, Chapter 3 and later biological examples: threshold interpretation in simple nonlinear models.
- Murray, *Mathematical Biology*: broad perspective on compartmental epidemic models.
