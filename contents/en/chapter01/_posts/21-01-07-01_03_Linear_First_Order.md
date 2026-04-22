---
layout: post
title: "01-03 Linear First-Order Equations"
chapter: '01'
order: 3
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

This lesson covers linear first-order differential equations and the integrating factor method.

## Topics to Cover

- Standard form
- Integrating factor method
- General solution formula
- Initial value problems

## Key Method

For $$ y' + p(t)y = q(t) $$, the integrating factor is:

$$ \mu(t) = e^{\int p(t)dt} $$

General solution:

$$y(t) = \frac{1}{\mu(t)}\left[\int \mu(t)q(t)dt + C\right]$$

![Linear first-order solutions]({{ site.imgurl }}/chapter_img/chapter01/01_03_linear_first_order.svg)

![Integrating factor concept]({{ site.imgurl }}/chapter_img/chapter01/01_03_integrating_factor.svg)

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Newton cooling in measurement systems
- Problem: An object removed from a furnace cools toward room temperature, and engineers need a reliable time-to-safe-temperature estimate.
- Model:
$$ \frac{dT}{dt}+kT=kT_m. $$
- Assumptions and limitations: The ambient temperature is constant, the body is well mixed thermally, and the exchange law is linear.
- Interpretation: The solution always splits into steady state plus decaying transient.

#### RL circuit startup
- Problem: When a source is switched on, current in an inductor-resistor circuit rises gradually rather than instantly.
- Model:
$$ L\frac{di}{dt}+Ri=E_0. $$
- Assumptions and limitations: Ideal linear components are assumed and temperature effects on resistance are ignored.
- Interpretation: The ratio $$ L/R $$ acts as the characteristic response time.

#### Debt with continuous repayment
- Problem: A loan balance grows through interest but shrinks through constant repayment.
- Model:
$$ \frac{dB}{dt}=rB-p. $$
- Assumptions and limitations: Interest and repayment are treated as smooth and constant. Real contracts are discrete and often variable.
- Interpretation: The model shows immediately whether repayment is enough to overcome interest.

### 2. Conceptual Insight

The integrating factor matters because it restores a product-rule structure. That is the first small appearance of a much larger theme in applied mathematics: choose a multiplier or representation that turns the equation into an exact derivative or an integral identity. A common error is to memorize the formula for the integrating factor without first putting the equation into standard form.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
y_eq = 1.0
for y0 in [-1.0, 0.0, 0.5, 2.0]:
    y = y_eq + (y0 - y_eq) * np.exp(-t)
    plt.plot(t, y, label=f"y(0)={y0}")

plt.axhline(y_eq, color="black", linestyle="--", label="steady state")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Family of solutions for y' + y = 1")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Students can see at a glance that the steady state controls the long-time behavior, while the initial condition only affects the transient.

### 4. External Search Prompts

- search: integrating factor visualization
- search: Newton cooling curve differential equation
- search: RL circuit transient response plot

### 5. Worked Example

If a sensor moves from a 22 degree C room into an 80 degree C chamber and obeys
$$ \frac{dT}{dt}+0.4T=32,\qquad T(0)=22, $$
then
$$ T(t)=80-58e^{-0.4t}. $$
The constant term is the target equilibrium and the exponential term is memory of the initial state. That language helps students interpret many later engineering models.

### 6. Difficulty Layering

**Undergraduate level.** Master standard form, integrating factors, and the separation between transient and steady-state parts.

**Graduate level.** Connect to variation of constants, Green functions, and linear operator viewpoints that reappear in systems and PDE.

## References

- Boyce & DiPrima, Section 2.1
- Zill, Section 2.3
