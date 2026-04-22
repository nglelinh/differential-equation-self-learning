---
layout: post
title: "04-10 Applications: Compartment Models"
chapter: '04'
order: 10
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: optional
---

## Learning Objectives

This lesson helps students see systems of differential equations as the natural language of compartment models in pharmacokinetics, ecology, and epidemiology. Students learn to write inflow-minus-outflow balance laws for each compartment, detect conservation or loss of total mass, and interpret the system matrix as a map of transfers between compartments.

## Prerequisites

Students should know linear systems, source terms, and the basic modeling idea of "rate in minus rate out." Care with units and parameter meaning matters as much here as symbolic solution methods.

## Introduction

![Compartment model with transfers between storage regions]({{ site.imgurl }}/chapter_img/chapter04/10_compartment_models.svg)

Not every important system comes from mechanics. Another major class of applications is the compartment model, where each state variable tracks the amount of material, population, drug, or pollutant in a storage region, and coefficients describe transfer rates between those regions.

The beauty of compartment models is that they make systems feel concrete. The variables answer "how much is in each place," while the arrows answer "where is it going." The central modeling questions are therefore not only whether a quantity grows or decays, but where it is leaving, where it is entering, and whether total mass is conserved.

## Concept in Three Ways

### Intuitive View

Imagine several tanks connected by pipes. Each tank contains some quantity, and the amount in each tank changes because flow can enter or leave. Writing one differential equation per tank is exactly what a compartment model does.

### Visual View

A diagram of compartments and arrows is often more informative than the equations at first. Each arrow corresponds to a transfer term, and the sign of each term can usually be read directly from the picture.

### Formal View

In a two-compartment linear model, one common form is
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2+u_1(t),
$$
$$ \frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2+u_2(t). $$
Negative terms represent flow leaving a compartment, while positive terms represent flow entering from another compartment or an external source. The total quantity often has a simpler balance law than the individual variables.

## Common Misconceptions

- "Compartment models are only bookkeeping." Wrong. Their interaction structure can produce rich dynamics.
- "If each equation looks simple, the whole system must be simple." Not necessarily. Coupling between compartments can create subtle transient behavior.
- "The total amount is always conserved." Wrong. Conservation depends on whether there is leakage out of the system or external forcing.
- "All compartment models are linear." Wrong. Many important ones, including SIR epidemic models, are nonlinear even though the compartment viewpoint remains the same.

## Suggested Learning Path

### Step 1: Draw the Compartment Diagram

This is the most important modeling step.

### Step 2: Write Inflow Minus Outflow for Each Compartment

Every term should have a clear physical meaning.

### Step 3: Check Total Balance

Students should immediately ask whether total amount is conserved, lost, or externally supplied.

### Step 4: Analyze Dynamics

Interpret long-term states, transfer rates, and the role of parameters.

### Checkpoints

- Can students place signs correctly on inflow and outflow terms?
- Can students compute the balance law for the total amount?
- Can students distinguish internal transfer from external source or loss?

## Worked Examples

### Example 1: A Two-Compartment Drug Model

Suppose
$$ \frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2, $$
$$ \frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2. $$
Here $$ x_1 $$ may represent the amount of drug in the bloodstream and $$ x_2 $$ the amount in tissue. The parameter $$ k_{01} $$ models elimination from the body. The model is simple, but each coefficient has an immediate physical interpretation.

### Example 2: Total Balance

Adding the two equations gives
$$ \frac{d}{dt}(x_1+x_2)=-k_{01}x_1. $$
So total drug in the two compartments is not conserved. The only net loss comes from elimination out of compartment $$ 1 $$. This balance law is often more informative than either equation alone.

### Example 3: A Conserved Transfer Model

If there is no external loss and no external input, then internal transfers cancel when we add the equations. In such a case the total amount is constant. This is a useful modeling check: if the system is supposed to conserve mass, the equations must reflect that.

### Example 4: SIR as a Compartment Model

The SIR epidemic system
$$ \frac{dS}{dt}=-\beta SI, $$
$$ \frac{dI}{dt}=\beta SI-\gamma I, $$
$$ \frac{dR}{dt}=\gamma I $$
is nonlinear, but the compartment interpretation remains the same. Individuals move from susceptible to infected to recovered. This reminds students that the compartment viewpoint extends beyond linear algebra.

## Conceptual Questions

1. Why is drawing the compartment diagram often the most important part of the modeling process?
2. What does the total balance law reveal that may not be obvious from each equation separately?
3. Why can a nonlinear epidemic model still be described as a compartment model?

## Application Problems

1. In pharmacokinetics, why is a two-compartment model often more realistic than a single well-mixed compartment?
2. In environmental modeling, why are compartment systems natural for pollutants moving among air, water, and soil?
3. In epidemiology, how does the compartment viewpoint help policymakers think about interventions?

## Interactive Teaching Strategies

- Begin with a compartment diagram and ask students to write the equations from arrows alone.
- Use a table with columns for compartment, inflow, and outflow before introducing the final system.
- Ask the class to predict whether total mass is conserved before any algebra is done.
- Compare a linear compartment model and the SIR model to show continuity of modeling ideas.

## Differentiation

### Support for Struggling Students

Students who need support should start with very small two-compartment examples and explicitly list every inflow and outflow term before writing equations. This reduces sign mistakes and improves physical interpretation.

### Challenge for Advanced Students

Advanced students can analyze stability of linear compartment models, study positivity of solutions, or compare linear transfer models with nonlinear compartment models from epidemiology or biochemistry.

## Summary

Compartment models translate flow and storage into systems of differential equations. Each variable tracks how much is present, each arrow tracks where it moves, and the total balance law often reveals the deepest structure of the model.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Two-compartment pharmacokinetics
- Problem: Drug moves between plasma and tissue while being eliminated from the body.
- Model:
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2.
$$
- Assumptions and limitations: First-order transfer rates and linear exchange.
- Interpretation: A system is natural because each compartment tells only one part of the transport story.

#### Pollutant exchange among reservoirs
- Problem: Pollutant mass moves between river, lake, soil, or atmosphere compartments.
- Model: Linear or near-linear compartment system.
- Assumptions and limitations: Well-mixed compartments and steady transfer rates.
- Interpretation: The system matrix reveals which reservoirs lose or gain material.

#### SIR as a nonlinear compartment model
- Problem: People move from susceptible to infected to recovered classes.
- Model:
$$
\frac{dS}{dt}=-\beta SI,\qquad
\frac{dI}{dt}=\beta SI-\gamma I,\qquad
\frac{dR}{dt}=\gamma I.
$$
- Assumptions and limitations: Homogeneous mixing and no demographic structure.
- Interpretation: Even when nonlinear, the compartment viewpoint remains the right organizing language.

### 2. Conceptual Insight

Compartment models show that systems of ODE are not only about oscillations and mechanics. They are also the language of transport, conservation, leakage, and accumulation. This lesson is a strong bridge into biological, medical, and environmental modeling, where signs and units often matter even more than formal solution technique.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, X):
    x1, x2 = X
    k12, k21, k01 = 0.4, 0.2, 0.1
    dx1 = -(k12 + k01) * x1 + k21 * x2
    dx2 = k12 * x1 - k21 * x2
    return [dx1, dx2]

t = np.linspace(0, 20, 500)
sol = solve_ivp(system, [0, 20], [10, 0], t_eval=t)

plt.plot(sol.t, sol.y[0], label="Compartment 1")
plt.plot(sol.t, sol.y[1], label="Compartment 2")
plt.plot(sol.t, sol.y[0] + sol.y[1], label="Total", linestyle="--")
plt.xlabel("t")
plt.ylabel("Amount")
plt.title("Two-compartment model")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: compartment model pharmacokinetics visualization
- search: two compartment model simulation
- search: SIR compartment diagram animation

### 5. Worked Example

For the two-compartment model
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2,
$$
the total amount satisfies
$$ \frac{d}{dt}(x_1+x_2)=-k_{01}x_1. $$
So total mass is not conserved because compartment 1 leaks to the outside. This is a very instructive modeling fact that emerges immediately by adding the equations.

### 6. Difficulty Layering

**Undergraduate level.** Draw the compartment diagram, assign the correct signs, and check total balance.

**Graduate level.** Compare linear and nonlinear compartment models and study stability and parameter interpretation.

![Compartment models]({{ site.imgurl }}/chapter_img/chapter04/04_10_compartment_models.svg)

## References

- Boyce & DiPrima, Chapter 7: several useful applications involving compartment models.
- Murray, *Mathematical Biology*: strong biological and epidemiological examples.
- Jacquez, *Compartmental Analysis in Biology and Medicine*: a classic reference for the modeling viewpoint.
