---
layout: post
title: "05-07 Predator-Prey Models"
chapter: '05'
order: 7
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

During World War I, commercial fishing in the Adriatic Sea collapsed due to naval blockades—yet when marine biologist Umberto D'Ancona checked port records afterward, he found a paradox: the fraction of *predatory* sharks and rays had surged dramatically while edible prey fish barely rose! Vito Volterra solved the mystery in 1926 using a two-equation nonlinear system that revealed both endless ecological oscillations and the startling **Volterra Principle**: indiscriminate harvesting always hurts predators more than prey.

## Key ideas: Four Surprises Inside the Lotka–Volterra Model

Four analytical properties make the classic Lotka–Volterra system $$x' = x(\alpha - \beta y),\; y' = y(-\gamma + \delta x)$$ a cornerstone of nonlinear ODEs:

1. **Two Equilibria (Extinction Saddle vs. Coexistence Center):** The origin $$(0, 0)$$ is a saddle (prey grow exponentially along $$y = 0$$, predators starve along $$x = 0$$), while the interior coexistence point $$(x^*, y^*) = (\gamma/\delta,\; \alpha/\beta)$$ has purely imaginary Jacobian eigenvalues $$\lambda = \pm i\sqrt{\alpha\gamma}$$.
2. **Exact First Integral (Conserved Quantity $$H(x,y)$$):** Because $$(x^*, y^*)$$ is a non-hyperbolic linear center, linearization alone cannot prove closed orbits! Dividing $$\frac{dy}{dx} = \frac{y(-\gamma + \delta x)}{x(\alpha - \beta y)}$$ separates variables and yields the exact conserved quantity
   $$H(x, y) = \delta x - \gamma\ln x + \beta y - \alpha\ln y = C,$$
   whose convex level curves rigorously prove *every* positive orbit is a closed periodic loop!
3. **Time-Averaged Populations Equal the Equilibrium:** Remarkably, integrating $$\frac{x'}{x} = \alpha - \beta y$$ over one full period $$T$$ gives $$\bar{y} = \frac{1}{T}\int_0^T y(t)\,dt = \frac{\alpha}{\beta} = y^*$$ and $$\bar{x} = \frac{\gamma}{\delta} = x^*$$—completely independent of the oscillation amplitude!
4. **Volterra's Fishing/Pesticide Principle:** Adding uniform harvesting/spraying rate $$\varepsilon$$ to both species changes $$\alpha \mapsto \alpha - \varepsilon$$ and $$\gamma \mapsto \gamma + \varepsilon$$, which **raises** the average prey population $$\bar{x} = \frac{\gamma + \varepsilon}{\delta}$$ and **lowers** the average predator population $$\bar{y} = \frac{\alpha - \varepsilon}{\beta}$$—explaining both D'Ancona's Adriatic sharks and why broad-spectrum insecticides can trigger pest outbreaks!

### Worked example: Linearizing, Verifying the First Integral, and Testing Harvesting on Lotka–Volterra

Analyze the predator–prey system ($$x$$ = rabbits, $$y$$ = foxes):
$$x' = x(2 - y), \qquad y' = y(-3 + x), \qquad x > 0,\; y > 0.$$

1. **Find the coexistence equilibrium and small-oscillation period:**
   Setting $$2 - y = 0$$ and $$-3 + x = 0$$ gives $$(x^*, y^*) = (3, 2)$$.
   Compute the Jacobian at $$(3, 2)$$:
   $$J(x, y) = \begin{pmatrix} 2 - y & -x \\ y & -3 + x \end{pmatrix} \implies J(3, 2) = \begin{pmatrix} 0 & -3 \\ 2 & 0 \end{pmatrix}.$$
   Eigenvalues: $$\lambda^2 + 6 = 0 \implies \lambda = \pm i\sqrt{6}$$.
   So small oscillations around $$(3, 2)$$ have period $$T \approx \frac{2\pi}{\sqrt{6}} \approx 2.565$$ time units (and check direction at $$(3+1, 2) = (4, 2)$$: $$y' = 2(1) > 0 \implies$$ **counterclockwise**!).
2. **Derive the exact first integral $$H(x, y)$$ to prove true closed orbits:**
   $$\frac{dy}{dx} = \frac{y(x - 3)}{x(2 - y)} \implies \left(\frac{2}{y} - 1\right)dy = \left(1 - \frac{3}{x}\right)dx.$$
   Integrating both sides gives
   $$H(x, y) = (x - 3\ln x) + (y - 2\ln y) = C.$$
   Check: $$\dot{H} = \left(1 - \frac{3}{x}\right)x(2-y) + \left(1 - \frac{2}{y}\right)y(x-3) = (x-3)(2-y) + (y-2)(x-3) = 0$$ identically!
3. **Quantify the effect of uniform harvesting $$\varepsilon = 0.5$$:**
   With $$x' = x(1.5 - y)$$ and $$y' = y(-3.5 + x)$$, the average rabbit population jumps from $$3$$ to **$$3.5$$** ($$+16.7\%$$) while the average fox population drops from $$2$$ to **$$1.5$$** ($$-25\%$$)!

## Learning Objectives

This lesson helps students analyze predator-prey systems as nonlinear interacting populations, interpret biological parameters, find equilibria and nullclines, and understand how cyclical population behavior emerges from feedback.

## Prerequisites

Students should know phase-plane analysis, equilibria, and linearization. Some biological intuition about growth, predation, and mortality is helpful.

## Introduction

![Lotka-Volterra predator-prey model]({{ site.imgurl }}/chapter_img/chapter05/07_predator_prey.svg)

Predator-prey systems are among the most famous examples in mathematical biology. They are simple enough to analyze qualitatively, but rich enough to display cyclical behavior, feedback, and nonlinear interaction.

What makes the model memorable is that neither population can be understood in isolation. Prey growth feeds predator growth, while predator abundance suppresses prey. The result is a coupled dynamical story rather than two independent population curves.

## Concept in Three Ways

### Intuitive View

When prey are abundant, predators have plenty of food and their numbers rise. As predators rise, prey are consumed more quickly and decline. Once prey become scarce, predators also begin to decline. Then prey recover, and the cycle may begin again.

### Visual View

The phase plane for predator-prey systems often contains a positive equilibrium and closed or nearly closed orbits around it. Nullclines show where one population stops changing instantaneously, and the surrounding sign pattern explains the cycle.

### Formal View

The classical Lotka-Volterra system is
$$ \dot{x}=ax-bxy,\qquad
\dot{y}=-cy+dxy, $$
where $$ x $$ is prey and $$ y $$ is predator. The positive equilibrium is
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$

## Common Misconceptions

- "Predator-prey cycles always converge to a stable oscillation." Not in the classical model.
- "The prey should always decrease when predators exist." Wrong. Prey can still increase when reproduction dominates predation.
- "The model predicts exact field data." Wrong. It is an idealized first model.
- "Each equation can be interpreted alone." Wrong. The essential meaning lies in the interaction terms.

## Suggested Learning Path

### Step 1: Interpret the Parameters

Students should say in words what each coefficient means biologically.

### Step 2: Find Nullclines and Equilibria

This gives the main structure of the phase portrait.

### Step 3: Use Linearization at the Positive Equilibrium

This explains local oscillatory behavior.

### Step 4: Compare Model and Reality

Students should identify what the model captures well and what it ignores.

### Checkpoints

- Can students explain why the interaction terms are nonlinear?
- Can students compute the positive equilibrium correctly?
- Do students know that the classical model is not automatically an attracting cycle?

## Worked Examples

### Example 1: Nullclines

For
$$ \dot{x}=ax-bxy, $$
the prey nullcline is
$$ x=0 \qquad \text{or} \qquad y=\frac{a}{b}. $$
For
$$ \dot{y}=-cy+dxy, $$
the predator nullcline is
$$ y=0 \qquad \text{or} \qquad x=\frac{c}{d}. $$
Their positive intersection gives the coexistence equilibrium.

### Example 2: Biological Meaning of the Equilibrium

At
$$ \left(\frac{c}{d},\frac{a}{b}\right), $$
predator death is exactly balanced by food intake and prey growth is exactly balanced by predation. This is the coexistence state of the model.

### Example 3: Cyclical Interpretation

Near the coexistence equilibrium, one population often lags behind the other. Prey increase first, then predator increase follows, then prey decrease, then predator decrease. This lag is one of the most important qualitative features of the model.

## Conceptual Questions

1. Why can predator-prey behavior be cyclical even without external periodic forcing?
2. Why is the coexistence equilibrium biologically meaningful?
3. Why must we be careful when interpreting the classical model as a realistic prediction?

## Application Problems

1. In ecology, how could seasonal effects change the predictions of the basic predator-prey model?
2. In agriculture, how might the model inform biological pest control?
3. In epidemiology of interacting species, why might simple predator-prey logic need to be modified?

## Interactive Teaching Strategies

- Ask students to tell the predator-prey story verbally before writing any equations.
- Plot time series and phase-plane orbits side by side.
- Have students mark which population should peak first and which should lag.
- Compare the basic model with one containing logistic prey growth.

## Differentiation

### Support for Struggling Students

Students who need support should focus first on interpreting the parameters and drawing the nullclines correctly.

### Challenge for Advanced Students

Advanced students can compare the classical model with more realistic predator-prey systems that possess attracting limit cycles.

## Summary

Predator-prey models show how nonlinear interaction creates rich population dynamics. The key ideas are coupling, feedback, coexistence equilibrium, and phase-plane interpretation.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Lynx-hare ecology
- Problem: Predator and prey populations rise and fall in a coupled way over time.
- Model:
$$ \dot{x}=ax-bxy,\qquad
\dot{y}=-cy+dxy. $$
- Assumptions and limitations: The model ignores carrying capacity, seasonality, and biological delay.
- Interpretation: More prey supports predator growth; more predators suppress prey; the feedback can create cycles.

#### Biological pest control
- Problem: A predator species is introduced to regulate an agricultural pest.
- Model: The same predator-prey structure, with parameters reinterpreted as attack and conversion rates.
- Assumptions and limitations: Real fields are spatially heterogeneous and involve intervention.
- Interpretation: The model helps explain when control leads to oscillations instead of a quiet steady state.

### 2. Additional Intuition and Connections

Predator-prey systems show that dynamics need not be monotone. A common pitfall is to assume that the classical Lotka-Volterra cycles are automatically stable. In fact, the basic model has neutrally closed orbits rather than an attracting limit cycle. This topic ties together nullclines, equilibria, linearization, and conserved-quantity intuition.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a, b, c, d = 1.5, 1.0, 1.0, 0.75

def lv(t, z):
    x, y = z
    return [a * x - b * x * y, -c * y + d * x * y]

t = np.linspace(0, 25, 1000)
sol = solve_ivp(lv, [0, 25], [1.8, 0.8], t_eval=t, max_step=0.05)

plt.subplot(1, 2, 1)
plt.plot(t, sol.y[0], label="prey")
plt.plot(t, sol.y[1], label="predator")
plt.xlabel("t")
plt.title("Time evolution")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sol.y[0], sol.y[1])
plt.xlabel("prey")
plt.ylabel("predator")
plt.title("Phase-plane orbit")
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: Lotka Volterra phase portrait
- search: predator prey nullclines interpretation
- search: biological control predator prey dynamics

### 5. Worked Example

For the Lotka-Volterra system, the positive equilibrium is
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
There, prey birth is balanced by predation and predator death is balanced by feeding. Linearization around this point predicts nearby oscillatory behavior.

### 6. Difficulty Layering

**Undergraduate level.** Find nullclines, compute equilibria, and interpret the parameters biologically.

**Graduate level.** Study conserved quantities, the Rosenzweig-MacArthur model, and mechanisms that produce attracting limit cycles.

![Predator-prey model]({{ site.imgurl }}/chapter_img/chapter05/05_07_predator_prey.svg)

## Video tham khảo

- xem trước: [Predator-Prey Population Models || Lotka-Volterra Equations](https://www.youtube.com/watch?v=DDEvlLa9z_U) — Exploring Maths, English. The Lotka-Volterra equations and the closed orbits of a predator-prey pair.
- [Predator-Prey Model (Lotka-Volterra)](https://www.youtube.com/watch?v=Tc05IbqTsFM) — Mike Saint-Antoine, English. A second walkthrough of the same model, including the phase-plane picture.
- [Lotka-Volterra Equation and Their Periodic Solutions](https://www.youtube.com/watch?v=WPck8AhuOsc) — Mike, the Mathematician, English. Why the periodic solutions of Lotka-Volterra are structurally fragile.

## References

- Strogatz, Chapter 6: accessible analysis of predator-prey dynamics.
- Murray, *Mathematical Biology*: broader biological context and model extensions.
