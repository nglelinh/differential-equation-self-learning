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

## References

- Boyce & DiPrima, Section 2.2
- Zill, Section 2.2
