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

Imagine hiking across a mountain range while keeping your altimeter glued to a fixed elevation: you trace a level contour line along which your total change in height is zero, $$d\Psi = \Psi_x\,dx + \Psi_y\,dy = 0$$. An exact differential equation is simply the reverse detective problem—you are handed the slope components $$M(x,y)\,dx + N(x,y)\,dy = 0$$ and asked to reconstruct the hidden elevation landscape $$\Psi(x,y) = C$$ whose contours are the solution curves.

## Background Knowledge Map: Conservative Vector Fields and Exact 1-Forms

Four ideas from multivariable calculus and differential geometry explain exact equations completely:

1. **Exactness as a Conservative Field:** The equation $$M\,dx + N\,dy = 0$$ is exact on a simply connected domain $$D$$ if and only if the vector field $$\mathbf{F} = (M, N)$$ is a gradient $$\nabla \Psi = (\Psi_x, \Psi_y)$$ for some smooth potential $$\Psi(x,y)$$.
2. **Clairaut's Integrability Test ($$M_y = N_x$$):** Because mixed partial derivatives commute ($$\Psi_{xy} = \Psi_{yx}$$), exactness requires $$M_y = N_x$$; on simply connected regions (no "holes"), this condition is also sufficient.
3. **Path-Independent Potential Reconstruction:** Integrating $$M$$ with respect to $$x$$ determines $$\Psi(x,y)$$ up to an unknown function $$g(y)$$ (not merely a constant!), which is then pinned down uniquely by matching $$\Psi_y = N$$.
4. **Special Integrating Factors:** When $$M_y \ne N_x$$, multiplying by a rescaling factor $$\mu(x,y)$$ can restore exactness—in particular, if $$\frac{M_y - N_x}{N}$$ depends only on $$x$$, then $$\mu(x) = \exp\!\left(\int \frac{M_y - N_x}{N}\,dx\right)$$ makes the equation exact.

### Step-by-Step Worked Example (Read Slowly): Repairing a Non-Exact Equation with an Integrating Factor and Finding Its Potential

Solve the differential equation
$$(3xy + y^2)\,dx + (x^2 + xy)\,dy = 0.$$

1. **Test for exactness:**
   Here $$M(x,y) = 3xy + y^2$$ and $$N(x,y) = x^2 + xy$$. Compute the cross-partials:
   $$M_y = 3x + 2y, \qquad N_x = 2x + y.$$
   Since $$M_y \ne N_x$$, the equation is **not** exact as written.
2. **Check for an $$x$$-only integrating factor:**
   $$\frac{M_y - N_x}{N} = \frac{(3x + 2y) - (2x + y)}{x^2 + xy} = \frac{x + y}{x(x + y)} = \frac{1}{x}.$$
   It depends solely on $$x$$! Thus
   $$\mu(x) = \exp\!\left(\int \frac{1}{x}\,dx\right) = x.$$
3. **Multiply through by $$\mu(x) = x$$ and re-verify exactness:**
   $$(3x^2 y + xy^2)\,dx + (x^3 + x^2 y)\,dy = 0.$$
   Check: $$\tilde{M}_y = 3x^2 + 2xy$$ and $$\tilde{N}_x = 3x^2 + 2xy$$. Exact!
4. **Reconstruct the potential function $$\Psi(x,y)$$:**
   Integrate $$\tilde{M}$$ with respect to $$x$$:
   $$\Psi(x,y) = \int (3x^2 y + xy^2)\,dx = x^3 y + \frac{1}{2}x^2 y^2 + g(y).$$
   Differentiate with respect to $$y$$ and set equal to $$\tilde{N}$$:
   $$\Psi_y = x^3 + x^2 y + g'(y) = x^3 + x^2 y \implies g'(y) = 0 \implies g(y) = \text{const}.$$
5. **Write the implicit general solution:**
   $$x^3 y + \frac{1}{2}x^2 y^2 = C \qquad (\text{or } 2x^3 y + x^2 y^2 = \tilde{C}).$$
   Differentiating $$2x^3 y + x^2 y^2 = \tilde{C}$$ immediately recovers $$(6x^2 y + 2xy^2)\,dx + (2x^3 + 2x^2 y)\,dy = 0$$!

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

## Video tham khảo

- xem trước: [Exact equations intuition 1 (proofy) | First order differential equations | Khan Academy](https://www.youtube.com/watch?v=iEpqcdaJNTQ) — Khan Academy, English. The exactness test ∂M/∂y=∂N/∂x and the potential function it comes from.
- [Exact equations example 1 | First order differential equations | Khan Academy](https://www.youtube.com/watch?v=Pb04ntcDJcQ) — Khan Academy, English. A first worked exact equation, useful beside the formal test.
- [Giải tích 6.2 PTVP Cấp 1: Phương trình Vi phân Toàn phần - Phần 1](https://www.youtube.com/watch?v=KrJzMAG3wUU) — Eureka! Uni, Vietnamese. Eureka Uni's Vietnamese lecture on exact first-order equations.

## References

- Boyce & DiPrima, Section 2.6
- Zill, Section 2.4
