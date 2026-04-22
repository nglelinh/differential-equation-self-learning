---
layout: post
title: "01-04 Exact Equations"
chapter: '01'
order: 4
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: required
---

This lesson covers exact differential equations and potential functions.

## Topics to Cover

- Exactness condition
- Finding potential functions
- Integrating factors for non-exact equations
- Geometric interpretation

## Key Concept

$$ M(x,y)dx + N(x,y)dy = 0 $$ is exact if:

$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

Then there exists $$ F(x,y) $$ such that $$ F_x = M $$, $$ F_y = N $$, and the solution is $$ F(x,y) = C $$.

![Exact equation solution contours]({{ site.imgurl }}/chapter_img/chapter01/01_04_exact_equations.svg)

![Exact vs non-exact vector fields]({{ site.imgurl }}/chapter_img/chapter01/01_04_exact_vs_nonexact.svg)

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Conservative mechanics
- Problem: Motion in a frictionless setting often preserves an energy-like quantity.
- Model:
$$ dF=F_t\,dt+F_y\,dy=0. $$
- Assumptions and limitations: The model assumes the system is conservative and ignores dissipation.
- Interpretation: Solutions lie on level curves of the conserved quantity.

#### Thermodynamic state functions
- Problem: Engineers need to know whether a differential expression corresponds to a genuine state function.
- Model:
$$ M(T,V)\,dT+N(T,V)\,dV. $$
- Assumptions and limitations: The state variables must describe an equilibrium setting. Nonequilibrium effects require richer models.
- Interpretation: Exactness means the quantity depends only on state, not on path.

#### Iso-cost curves in economics
- Problem: A firm studies combinations of two inputs yielding the same cost.
- Model:
$$ dC=C_x\,dx+C_y\,dy=0. $$
- Assumptions and limitations: Cost is assumed smooth and dependent on only two continuous inputs.
- Interpretation: Exact equations can therefore be understood as level-curve equations in economics too.

### 2. Conceptual Insight

Exact equations are the first place in the chapter where ODE meets multivariable calculus in a serious way. The test
$$ M_y=N_t $$
is not a random trick; it reflects equality of mixed partial derivatives and, geometrically, the possibility of reconstructing a potential function. A common pitfall is forgetting that the "constant of integration" can be a function of the other variable.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
T, Y = np.meshgrid(t, y)
F = T**2 * Y + T * Y**2

plt.figure(figsize=(6, 5))
contours = plt.contour(T, Y, F, levels=12, cmap="viridis")
plt.clabel(contours, inline=True, fontsize=8)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Level curves of F(t, y) = t^2 y + t y^2")
plt.grid(alpha=0.2)
plt.show()
```

For the corresponding exact equation $$ dF=0 $$, these contours are precisely the solution family.

### 4. External Search Prompts

- search: exact differential equations contour plot
- search: conservative vector field potential function
- search: thermodynamics exact differential state function

### 5. Worked Example

Consider
$$ \left(2ty+y^2\right)dt+\left(t^2+2ty\right)dy=0. $$
Since
$$ M_y=N_t=2t+2y, $$
the equation is exact, with potential
$$ F(t,y)=t^2y+ty^2. $$
Hence the solution is
$$ t^2y+ty^2=C. $$
The main interpretation is geometric: the dynamics are trapped on a level set of a hidden conserved quantity.

### 6. Difficulty Layering

**Undergraduate level.** Practice the exactness test and the construction of the potential function.

**Graduate level.** Connect exact equations to differential forms, simply connected domains, path independence, and integrating factors for non-exact equations.

## References

- Boyce & DiPrima, Section 2.6
- Zill, Section 2.4
