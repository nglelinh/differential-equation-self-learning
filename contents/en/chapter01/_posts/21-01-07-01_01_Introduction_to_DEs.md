---
layout: post
title: "01-01 Introduction to Differential Equations"
chapter: '01'
order: 1
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

This lesson introduces the fundamental concepts and classification of differential equations.

## Topics to Cover

- What is a differential equation?
- Order and degree
- Linear vs nonlinear equations
- Ordinary vs partial differential equations
- Solutions: general, particular, singular

## Key Definition

A **differential equation** is an equation involving derivatives of an unknown function. For a function $$ y(t) $$:

$$F\left(t, y, \frac{dy}{dt}, \frac{d^2y}{dt^2}, \ldots\right) = 0$$

![Solution curves for dy/dt = y and dy/dt = -y]({{ site.imgurl }}/chapter_img/chapter01/01_01_introduction_to_des.svg)

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Thermal sensor relaxation
- Problem: A probe moved from a cold room into a furnace does not report the furnace temperature instantly.
- Model:
$$ \frac{dT}{dt}=-k\left(T-T_{\mathrm{env}}\right). $$
- Assumptions and limitations: The environment is treated as spatially uniform, the heat-transfer coefficient is constant, and the sensor is modeled as lumped. Strong radiation or nonlinear heat transfer is ignored.
- Interpretation: The exponential solution shows why measurement devices have response time and why "current reading" can lag behind the actual environment.

#### One-compartment pharmacokinetics
- Problem: Drug concentration changes because medication is infused while the body clears it.
- Model:
$$ \frac{dC}{dt}=\frac{u(t)}{V}-kC. $$
- Assumptions and limitations: The model assumes immediate mixing and first-order elimination. Multi-organ distribution or saturating metabolism would require richer models.
- Interpretation: The solution separates dosing from clearance and explains loading doses, maintenance doses, and steady concentration.

#### Savings with continuous interest and regular deposits
- Problem: An account grows by continuous compounding while additional money is deposited at a constant rate.
- Model:
$$ \frac{dA}{dt}=rA+s. $$
- Assumptions and limitations: Interest is fixed and deposits are smooth in time. Taxes, fees, and market uncertainty are omitted.
- Interpretation: The solution makes visible the competition between current capital growth and external contributions.

#### RC circuit as a low-pass filter
- Problem: A circuit should smooth out fast electrical noise while still following slower trends.
- Model:
$$
RC\frac{dV_{\mathrm{out}}}{dt}+V_{\mathrm{out}}=V_{\mathrm{in}}(t).
$$
- Assumptions and limitations: Components are ideal and linear. Parasitic inductance and nonlinear effects are neglected.
- Interpretation: The differential equation explains why the circuit follows slow inputs well but resists sudden jumps.

### 2. Conceptual Insight

A differential equation should first be read as a local law of change, not as a formula to memorize. That perspective connects immediately to the rest of the chapter: separable equations isolate time and state effects, linear equations split internal dynamics from forcing, and autonomous equations remove the explicit clock and keep only the state. A common misconception is to confuse a slope field with a solution curve. The slope field gives local directions; the solution curve is the global path assembled from those directions.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 21)
y = np.linspace(-2, 2, 21)
T, Y = np.meshgrid(t, y)

fields = [(Y, "y' = y"), (T - Y, "y' = t - y")]
fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharex=True, sharey=True)

for ax, F, title in zip(axes, [f[0] for f in fields], [f[1] for f in fields]):
    U = np.ones_like(F)
    V = F
    N = np.sqrt(U**2 + V**2)
    ax.quiver(T, Y, U / N, V / N, color="teal", pivot="mid")
    ax.set_title(title)
    ax.set_xlabel("t")
    ax.grid(alpha=0.2)

axes[0].set_ylabel("y")
plt.tight_layout()
plt.show()
```

The first field emphasizes pure growth and decay. The second emphasizes relaxation toward a moving target line, which is a strong physical intuition for negative feedback.

### 4. External Search Prompts

- search: slope field first order differential equation
- search: Newton cooling interactive simulation
- search: RC circuit step response visualization

### 5. Worked Example

Suppose an account starts with 5000 dollars, earns 4 percent continuous interest, and receives 1200 dollars per year continuously. Then
$$ \frac{dA}{dt}=0.04A+1200,\qquad A(0)=5000. $$
The analytical solution is
$$ A(t)=-30000+35000e^{0.04t}. $$
The formula shows that short-term growth is driven largely by deposits, while long-term behavior is dominated by exponential compounding. An Euler approximation with a half-year step already captures the early trend, which makes this a good first comparison between exact and numerical thinking.

### 6. Difficulty Layering

**Undergraduate level.** Focus on classification, initial conditions, and the interpretation of derivative as rate.

**Graduate level.** Emphasize state-space language, well-posedness, and the difference between deterministic ODE models and more realistic delayed or stochastic models.

## References

- Boyce & DiPrima, Chapter 1
- Zill, Chapter 1
