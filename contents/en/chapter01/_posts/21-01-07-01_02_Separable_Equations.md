---
layout: post
title: "01-02 Separable Equations"
chapter: '01'
order: 2
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

Imagine a snowball melting in warm air so that its volume shrinks at a rate proportional to its surface area, or a chemical reaction whose speed depends on the product of reactant concentrations. Whenever the right-hand side of $$y' = f(x,y)$$ factors cleanly into an $$x$$-part times a $$y$$-part, you can decouple the two variables onto opposite sides of the equals sign and integrate directly—the oldest and most versatile exact technique in all of differential equations.

## Background Knowledge Map: What Makes Separation of Variables Rigorous

At the university level, separation of variables is more than "multiplying by $$dx$$"—four subtleties govern every problem:

1. **Chain-Rule Justification:** Writing $$g(y)\,y' = h(x)$$ and integrating with respect to $$x$$ yields $$\int g(y(x))\,y'(x)\,dx = \int h(x)\,dx$$; by substitution $$u = y(x)$$, this rigorously becomes $$\int g(y)\,dy = \int h(x)\,dx + C$$.
2. **Lost Equilibrium (Singular) Solutions:** Dividing both sides by $$q(y)$$ requires $$q(y) \ne 0$$; every root $$y = y^*$$ of $$q(y) = 0$$ is a constant equilibrium solution that must be checked separately so it is never dropped.
3. **Implicit vs. Explicit Solutions and Interval of Validity:** Integration often produces an implicit curve $$G(y) = H(x) + C$$; solving for $$y(x)$$ can introduce square-root branches (fixed by the initial condition) and vertical asymptotes that restrict the maximal interval of existence.
4. **Exponential Sign Absorption:** When $$\ln\lvert y \rvert = H(x) + C_1$$, exponentiating gives $$\lvert y \rvert = e^{C_1} e^{H(x)}$$, and allowing $$C = \pm e^{C_1}$$ (plus $$C = 0$$ from the equilibrium $$y \equiv 0$$) smoothly recovers all real constants $$C \in \mathbb{R}$$.

### Step-by-Step Worked Example (Read Slowly): Solving a Separable IVP with Blow-Up and Equilibrium Check

Solve the initial value problem
$$\frac{dy}{dx} = x\,(y^2 - 1), \qquad y(0) = 2,$$
and find its maximal interval of existence.

1. **Check for constant (equilibrium) solutions first:**
   Setting $$y^2 - 1 = 0$$ gives $$y \equiv 1$$ and $$y \equiv -1$$. Neither passes through $$y(0) = 2$$, so near $$x = 0$$ we safely have $$y^2 - 1 \ne 0$$.
2. **Separate variables and integrate using partial fractions:**
   $$\frac{dy}{y^2 - 1} = x\,dx \implies \frac{1}{2}\left(\frac{1}{y-1} - \frac{1}{y+1}\right)dy = x\,dx.$$
   Integrating both sides:
   $$\frac{1}{2}\ln\left\lvert \frac{y-1}{y+1} \right\rvert = \frac{x^2}{2} + C_1 \implies \left\lvert \frac{y-1}{y+1} \right\rvert = K e^{x^2}.$$
3. **Pin down the sign and constant using $$y(0) = 2$$:**
   At $$x = 0, y = 2$$, $$\frac{y-1}{y+1} = \frac{1}{3} > 0$$, so we drop the absolute value with $$K = \frac{1}{3}$$:
   $$\frac{y-1}{y+1} = \frac{1}{3}e^{x^2}.$$
4. **Solve explicitly for $$y(x)$$:**
   $$3(y - 1) = (y + 1)e^{x^2} \implies y(3 - e^{x^2}) = 3 + e^{x^2} \implies y(x) = \frac{3 + e^{x^2}}{3 - e^{x^2}}.$$
5. **Determine the maximal interval of existence:**
   The denominator vanishes when $$e^{x^2} = 3 \iff x = \pm\sqrt{\ln 3} \approx \pm 1.048$$. Because the initial point $$x = 0$$ lies between these vertical asymptotes, the maximal interval of existence is $$(-\sqrt{\ln 3},\; \sqrt{\ln 3})$$—even though the ODE itself is smooth everywhere on $$\mathbb{R}^2$$!

This lesson covers the method of separation of variables for first-order ODEs.

## Topics to Cover

- Recognizing separable equations
- Solution method
- Applications: exponential growth/decay
- Implicit solutions

## Key Method

A separable equation has the form:

$$ \frac{dy}{dx} = g(x)h(y) $$

Solution: Separate and integrate:

$$ \int \frac{1}{h(y)} dy = \int g(x) dx $$

![Solutions for separable equations]({{ site.imgurl }}/chapter_img/chapter01/01_02_separable_equations.svg)

![Exponential growth and decay]({{ site.imgurl }}/chapter_img/chapter01/01_02_growth_decay.svg)

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Radioactive decay
- Problem: A medical isotope loses activity over time and clinicians must estimate the remaining dose.
- Model:
$$ \frac{dN}{dt}=-\lambda N. $$
- Assumptions and limitations: Each atom decays independently with constant probability rate. Multi-step decay chains are ignored.
- Interpretation: The exponential solution explains half-life immediately and clarifies why percentage loss is constant while absolute loss shrinks.

#### Logistic population growth
- Problem: A fish population initially grows rapidly but slows as resources become scarce.
- Model:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$
- Assumptions and limitations: The environment is treated as homogeneous and the carrying capacity $$ K $$ is fixed. Seasonal forcing and age structure are absent.
- Interpretation: The solution corrects exponential growth by showing saturation near $$ K $$.

#### Vertical motion with quadratic drag
- Problem: A falling skydiver speeds up at first and then approaches terminal velocity.
- Model:
$$ \frac{dv}{dt}=g-kv^2. $$
- Assumptions and limitations: Motion is vertical, mass is constant, and drag is proportional to velocity squared. Opening the parachute or changing posture is not included.
- Interpretation: Separation of variables reveals directly that velocity is bounded by $$ \sqrt{g/k} $$.

### 2. Conceptual Insight

The separation method is not a mysterious algebra trick. It works because the dynamics already factor into a pure time part and a pure state part. That structural viewpoint also explains two important pitfalls: equilibrium solutions can be lost if we divide by the state factor too early, and implicit solutions are still perfectly valid solutions even when we cannot isolate the dependent variable explicitly.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 0.8, 100
t = np.linspace(0, 12, 400)
P0_values = [5, 20, 60, 140]

for P0 in P0_values:
    C = (K - P0) / P0
    P = K / (1 + C * np.exp(-r * t))
    plt.plot(t, P, label=f"P0={P0}")

plt.axhline(K, color="black", linestyle="--", label="K")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Logistic solutions for multiple initial conditions")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

This picture makes the role of the carrying capacity visible before any formal stability language appears.

### 4. External Search Prompts

- search: logistic equation phase line
- search: radioactive decay simulation differential equation
- search: skydiver quadratic drag solution

### 5. Worked Example

A fish lake has carrying capacity 5000, intrinsic growth rate 0.6 per year, and initial population 800. Then
$$
\frac{dP}{dt}=0.6P\left(1-\frac{P}{5000}\right),\qquad P(0)=800.
$$
Separation gives
$$ P(t)=\frac{5000}{1+5.25e^{-0.6t}}. $$
The formula predicts rapid early recovery followed by slow saturation, which is exactly the kind of biological interpretation students should practice reading from the equation.

### 6. Difficulty Layering

**Undergraduate level.** Recognize the product structure, keep equilibrium solutions, and solve cleanly with initial data.

**Graduate level.** Discuss finite-time blow-up, invariant regions, monotonicity, and the link between separated ODE and separation ideas later used in PDE.

## Video tham khảo

- xem trước: [Separation of Variables //  Differential Equations](https://www.youtube.com/watch?v=7Y-frhf-1Zk) — Dr. Trefor Bazett, English. The separation step dy/g(y)=f(x)dx and when the method is legitimate.
- [Newton's Law of Cooling  // Separable ODE Example](https://www.youtube.com/watch?v=_bAjWNsNrQA) — Dr. Trefor Bazett, English. Newton's law of cooling as a fully worked separable model.
- [17. Phương trình vi phân tách biến | Phương trình vi phân | Khan Academy](https://www.youtube.com/watch?v=_A1F5ygjdKk) — Khan Academy Vietnam, Vietnamese. Khan Academy Vietnam walks through separable first-order equations in Vietnamese.

## References

- Boyce & DiPrima, Section 2.2
- Zill, Section 2.2
