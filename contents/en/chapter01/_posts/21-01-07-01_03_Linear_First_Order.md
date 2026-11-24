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

Consider a lake being fed by a slightly polluted stream while fresh water flows out at the same rate: the pollutant decays naturally at a rate proportional to its current amount, yet an external inflow keeps adding more. Linear first-order ODEs $$y' + p(t)y = q(t)$$ capture this exact tug-of-war between internal decay/growth and external forcing—and unlike nonlinear equations, a single unifying device, the integrating factor, solves every single one of them in closed integral form.

## Background Knowledge Map: Why the Integrating Factor Always Works

Four structural insights elevate the integrating-factor method from a recipe into a deep principle:

1. **Reverse Product Rule:** Multiplying $$y' + p(t)y = q(t)$$ by $$\mu(t) = \exp\!\left(\int p(t)\,dt\right)$$ forces $$\mu'(t) = \mu(t)p(t)$$, collapsing the entire left-hand side into a single exact derivative $$\frac{d}{dt}[\mu(t)y(t)] = \mu(t)q(t)$$.
2. **Homogeneous + Particular Decomposition:** Every solution splits cleanly as $$y(t) = \frac{C}{\mu(t)} + \frac{1}{\mu(t)}\int \mu(s)q(s)\,ds = y_h(t) + y_p(t)$$, foreshadowing the superposition principle for higher-order linear ODEs.
3. **Transient vs. Steady-State Behavior:** When $$p(t) = a > 0$$, the homogeneous piece $$C e^{-at}$$ decays exponentially to zero regardless of initial conditions (the *transient*), leaving only the long-term response driven by $$q(t)$$ (the *steady state*).
4. **Global Existence on Coefficient Continuity:** Unlike separable nonlinear equations that can blow up spontaneously, a linear first-order IVP is guaranteed to exist on the *entire* largest open interval where $$p(t)$$ and $$q(t)$$ are continuous.

### Step-by-Step Worked Example (Read Slowly): Solving a Forced Linear IVP and Identifying Transient vs. Steady State

Solve the initial value problem
$$t\,y' + 3y = 5t^2, \qquad t > 0, \qquad y(1) = 4.$$

1. **Put the equation into standard form $$y' + p(t)y = q(t)$$:**
   Divide by $$t > 0$$ (never skip this step before computing $$\mu(t)$$!):
   $$y' + \frac{3}{t}y = 5t.$$
   Here $$p(t) = \frac{3}{t}$$ and $$q(t) = 5t$$, both continuous on $$(0, \infty)$$.
2. **Compute the integrating factor $$\mu(t)$$:**
   $$\mu(t) = \exp\!\left(\int \frac{3}{t}\,dt\right) = e^{3\ln t} = t^3 \qquad (t > 0).$$
3. **Multiply the standard-form equation by $$\mu(t) = t^3$$ and verify the product rule:**
   $$t^3 y' + 3t^2 y = 5t^4 \iff \frac{d}{dt}\bigl(t^3 y\bigr) = 5t^4.$$
   (Quick check: expanding $$\frac{d}{dt}(t^3 y)$$ gives $$t^3 y' + 3t^2 y$$—exact match!)
4. **Integrate both sides and divide by $$t^3$$:**
   $$t^3 y = \int 5t^4\,dt = t^5 + C \implies y(t) = t^2 + \frac{C}{t^3}.$$
5. **Apply $$y(1) = 4$$ and interpret behavior:**
   $$4 = 1^2 + \frac{C}{1^3} \implies C = 3 \implies y(t) = t^2 + \frac{3}{t^3}.$$
   As $$t \to \infty$$, the initial-condition memory $$\frac{3}{t^3}$$ vanishes while the forced response $$t^2$$ dominates; as $$t \to 0^+$$, the singularity of $$p(t) = 3/t$$ causes $$y(t) \to +\infty$$.

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

## Video tham khảo

- xem trước: [Linear Differential Equations & the Method of Integrating Factors](https://www.youtube.com/watch?v=2H6BZHlD_3g) — Dr. Trefor Bazett, English. Why the integrating factor e^{∫p} turns a linear equation into an exact derivative.
- [The Method of Integrating Factors for Linear 1st Order ODEs **full example**](https://www.youtube.com/watch?v=20x2dNVztlU) — Dr. Trefor Bazett, English. A complete example of the integrating-factor formula from start to the initial condition.
- [Phương trình vi phân Tuyến tính cấp 1 (Bài 13.2) | Vi tích phân 2/Toán C](https://www.youtube.com/watch?v=m8BFHJQrLSM) — Nguyễn Văn Thùy, Vietnamese. A Vietnamese lecture on the first-order linear equation and its integrating factor.

## References

- Boyce & DiPrima, Section 2.1
- Zill, Section 2.3
