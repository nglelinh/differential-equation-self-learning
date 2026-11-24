---
layout: post
title: "07-07 Applications: Heat Conduction"
chapter: '07'
order: 7
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: required
---

Hold one end of a metal poker in ice water and heat the middle with a torch; remove the torch and watch the temperature profile evolve. Unlike a vibrating string that remembers its sharp corners forever as traveling waves, heat conduction ruthlessly erases jagged details. High-frequency spatial wiggles carry huge curvature $$ u_{xx} $$, which drives exponential decay factors $$ e^{-\alpha \lambda_n t} $$ that crush the $$ n = 10 $$ mode a *hundred times faster* in the exponent than the $$ n = 1 $$ mode!

This lesson shows how the exact same Sturm–Liouville eigenfunctions from Chapter 07 turn the heat equation into a low-pass thermal filter—and how shifting by a steady-state profile handles nonhomogeneous boundary temperatures cleanly.

## Background Knowledge Map: Thermal Modes, Steady States, and Decay Rates

1. **Exponential Smoothing $$ e^{-\alpha \lambda_n t} $$ (Parabolic Dissipation):** Separating $$ u_t = \alpha u_{xx} $$ gives $$ T_n(t) = e^{-\alpha \lambda_n t} $$. Because $$ \lambda_n = (n\pi/L)^2 $$ grows quadratically with $$ n $$, high spatial frequencies die out almost instantaneously, leaving the fundamental mode $$ n = 1 $$ to dominate the long-time cooling tail.
2. **Steady-State + Transient Decomposition:** When the rod ends are held at nonzero temperatures $$ u(0, t) = T_1 $$ and $$ u(L, t) = T_2 $$, we split $$ u(x, t) = u_{\text{ss}}(x) + v(x, t) $$. The steady state solves $$ u_{\text{ss}}'' = 0 $$ (a straight line connecting $$ T_1 $$ to $$ T_2 $$), while the transient $$ v $$ satisfies *homogeneous* Dirichlet BCs and decays to zero as $$ t \to \infty $$.
3. **Insulated Ends and Energy Conservation (Neumann Spectrum):** If both ends are insulated ($$ u_x(0, t) = u_x(L, t) = 0 $$), $$ \lambda_0 = 0 $$ is an eigenvalue with constant eigenfunction $$ \phi_0(x) = 1 $$. Its coefficient $$ a_0 = \frac{1}{L}\int_0^L f(x)\,dx $$ never decays—the rod equilibrates to the exact spatial average of its initial temperature!
4. **Characteristic Thermal Time Scale $$ \tau = L^2 / (\pi^2 \alpha) $$:** Doubling a rod's length $$ L $$ makes it take *four times longer* to cool, a universal diffusive scaling law ($$ t \sim L^2 / \alpha $$).

### Step-by-Step Worked Example (Read Slowly): Nonhomogeneous Rod Cooling and Mode-Decay Ratio

**Problem:** A copper rod of length $$ L = 1\text{ m} $$ with thermal diffusivity $$ \alpha = 10^{-4}\text{ m}^2/\text{s} $$ has endpoints fixed at $$ u(0, t) = 20^\circ\text{C} $$ and $$ u(1, t) = 60^\circ\text{C} $$, and starts with initial temperature $$ u(x, 0) = 20 + 40x + 30\sin(\pi x) + 10\sin(3\pi x) $$. Find $$ u(x, t) $$ explicitly, and compute the temperature at $$ x = 0.5\text{ m} $$ after $$ t = 1000\text{ s} $$.

1. **Find the steady-state temperature $$ u_{\text{ss}}(x) $$:**
   Solving $$ u_{\text{ss}}'' = 0 $$ with $$ u_{\text{ss}}(0) = 20 $$ and $$ u_{\text{ss}}(1) = 60 $$ gives
   $$ u_{\text{ss}}(x) = 20 + 40x. $$
2. **Extract the homogeneous transient initial condition $$ v(x, 0) $$:**
   $$ v(x, 0) = u(x, 0) - u_{\text{ss}}(x) = 30\sin(\pi x) + 10\sin(3\pi x). $$
   Notice $$ v(0, t) = v(1, t) = 0 $$, and $$ v(x, 0) $$ is already written in the Dirichlet eigenbasis $$ \sin(n\pi x) $$ with $$ \lambda_1 = \pi^2 $$ and $$ \lambda_3 = 9\pi^2 $$!
3. **Attach the exact exponential decay factors:**
   $$ u(x, t) = 20 + 40x + 30 e^{-\alpha \pi^2 t} \sin(\pi x) + 10 e^{-9\alpha \pi^2 t} \sin(3\pi x). $$
4. **Evaluate at $$ x = 0.5\text{ m} $$, $$ t = 1000\text{ s} $$ (using $$ \alpha t = 0.1 $$):**
   - Fundamental decay factor: $$ e^{-0.1 \pi^2} \approx e^{-0.98696} \approx 0.3727 $$.
   - Third-harmonic decay factor: $$ e^{-0.9 \pi^2} \approx e^{-8.8826} \approx 0.000139 $$ (virtually wiped out!).
   - Since $$ \sin(\pi/2) = 1 $$ and $$ \sin(3\pi/2) = -1 $$:
     $$ u(0.5, 1000) \approx 40 + 30(0.3727)(1) + 10(0.000139)(-1) \approx 40 + 11.18 - 0.0014 \approx 51.18^\circ\text{C}. $$
   Look at the physics in numbers: in 1000 seconds, the $$ n=1 $$ bump dropped to 37% of its original height, while the $$ n=3 $$ wiggle was crushed to 0.014%!

## Learning Objectives

This lesson applies boundary-value methods to steady heat conduction. Students should learn to interpret steady-state temperature profiles as BVP solutions, connect boundary conditions to physical heat exchange, and see how Green's functions and eigenfunction thinking prepare the way for later PDE chapters.

## Prerequisites

Students should know BVPs, Green's functions, and the physical meaning of temperature and heat flux. Some exposure to the heat equation is helpful but not required.

## Introduction

![Steady-state heat conduction in a rod]({{ site.imgurl }}/chapter_img/chapter07/07_heat_conduction.svg)

Steady heat conduction is one of the cleanest and most important applications of boundary value problems. Once time dependence disappears, the problem becomes purely spatial: find a temperature profile that balances internal sources, conductivity, and boundary constraints.

This lesson matters because it shows students that BVPs are not only abstract operator problems. They describe concrete equilibrium profiles in physics and engineering. It also prepares the transition to the full heat equation later in the course.

## Concept in Three Ways

### Intuitive View

A steady temperature profile is what remains after the transient evolution has died out. The system no longer changes in time, but the temperature may still vary across space.

### Visual View

Different boundary conditions create different profile shapes: fixed temperatures pin the endpoints, insulated ends flatten the slope there, and Robin conditions model exchange with an ambient environment.

### Formal View

A typical steady heat-conduction model in one dimension is
$$ -(k(x)T')'=f(x), $$
with boundary conditions such as
$$ T(0)=T_0,\qquad T(L)=T_L, $$
or flux-based alternatives. This is a boundary value problem for the equilibrium temperature.

## Common Misconceptions

- "Heat conduction always means a time-dependent PDE." Not at steady state.
- "A steady profile must be constant." Only if there is no source term and no nontrivial boundary forcing.
- "Boundary conditions only specify temperatures." Wrong. Flux and mixed conditions are also physically natural.
- "This topic is separate from Sturm-Liouville theory." Wrong. It uses the same operator ideas in equilibrium form.

## Suggested Learning Path

### Step 1: Interpret the Physical Setup

Students should identify the source term, conductivity, and endpoint conditions.

### Step 2: Write the BVP

The mathematical model should clearly separate interior balance from boundary data.

### Step 3: Solve Simple Cases Directly

Constant-source examples are especially instructive.

### Step 4: Connect to Later PDE Theory

This is the equilibrium shadow of the heat equation.

### Checkpoints

- Can students distinguish temperature conditions from flux conditions?
- Do they understand why steady-state removes time from the model?
- Can they solve a basic profile problem and interpret its shape physically?

## Worked Examples

### Example 1: Uniform Internal Heating

Solve
$$ -T''=1,\qquad 0<x<1,\qquad T(0)=0,\qquad T(1)=0. $$
Integrating twice gives
$$ T(x)=\frac{x(1-x)}{2}. $$
The profile is hottest in the interior and coolest at the ends.

### Example 2: Insulated Boundary

If one endpoint is insulated, then the heat flux there is zero, so the boundary condition becomes
$$ T'(0)=0. $$
This changes the profile shape because the slope must flatten at that end.

### Example 3: Robin Boundary Condition

A condition such as
$$ T'(L)+hT(L)=0 $$
models heat exchange with an ambient environment. This is one of the most physically important mixed boundary conditions.

## Conceptual Questions

1. Why is a steady heat problem naturally a BVP rather than an IVP?
2. What is the physical meaning of a Neumann or Robin thermal boundary condition?
3. Why does internal heating usually create curved temperature profiles rather than straight lines?

## Application Problems

1. In a wall or rod, how does a localized heat source change the equilibrium profile?
2. Why does insulation correspond to a derivative condition rather than a value condition?
3. How can boundary-value thinking help in thermal design for engineering systems?

## Interactive Teaching Strategies

- Use physical descriptions and ask students to translate them into boundary conditions.
- Compare profiles under Dirichlet, Neumann, and Robin conditions.
- Plot simple steady profiles and ask where the hottest point should be before solving.
- Connect each example to the language of flux balance and equilibrium.

## Differentiation

### Support for Struggling Students

Students who need support should focus on direct integration examples and practice translating thermal language into mathematical boundary conditions.

### Challenge for Advanced Students

Advanced students can study variable conductivity or interface conditions in layered materials.

## Summary

Steady heat conduction is a natural and concrete application of boundary value theory. It turns operator ideas, boundary conditions, and solution methods into physically interpretable temperature profiles.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Steady heat profile in a nonuniform rod
- Problem: Find the equilibrium temperature distribution when the rod has a heat source and fixed or insulated endpoints.
- Model:
$$ -(k(x)T')'=f(x), $$
with Dirichlet, Neumann, or Robin conditions.
- Assumptions and limitations: One-dimensional steady state with no time dependence.
- Interpretation: This is a canonical BVP leading naturally to Green's functions or eigenfunction expansions.

#### Multilayer wall conduction
- Problem: A composite wall has different thermal conductivities in different layers, but the interface temperatures and fluxes must still match.
- Model:
$$ -(k(x)T')'=0 $$
on each layer together with interface flux continuity.
- Assumptions and limitations: One-dimensional and steady.
- Interpretation: Boundary and interface conditions determine the full spatial temperature profile.

### 2. Additional Intuition and Connections

Steady heat conduction makes the BVP viewpoint especially clear: time is gone, and all that remains is a spatial equilibrium shape. A common pitfall is to confuse this with the time-dependent heat equation. This lesson also prepares students directly for Chapter 9.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

def ode(x, y):
    return np.vstack((y[1], -10 * np.ones_like(x)))

def bc(ya, yb):
    return np.array([ya[0], yb[0] - 100])

x = np.linspace(0, 1, 200)
y_guess = np.zeros((2, x.size))
sol = solve_bvp(ode, bc, x, y_guess)

plt.plot(sol.x, sol.y[0], label="T(x)")
plt.xlabel("x")
plt.ylabel("Temperature")
plt.title("Steady-state temperature profile")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
```

### 4. Suggested Searches

- search: steady state heat conduction boundary value problem
- search: rod temperature profile with heat source
- search: Dirichlet Neumann Robin heat boundary conditions

### 5. Worked Example

Solve
$$ -T''=1,\qquad 0<x<1,\qquad T(0)=0,\qquad T(1)=0. $$
Integrating twice gives
$$
T''=-1,\qquad
T'=-x+C_1,\qquad
T=-\frac{x^2}{2}+C_1x+C_2.
$$
The boundary conditions imply
$$ C_2=0,\qquad C_1=\frac{1}{2}, $$
so
$$ T(x)=\frac{x(1-x)}{2}. $$

### 6. Difficulty Layering

**Undergraduate level.** Solve simple steady heat profiles and interpret each boundary condition physically.

**Graduate level.** Connect the model to one-dimensional elliptic operators, maximum principles, and later PDE theory.

![Heat conduction]({{ site.imgurl }}/chapter_img/chapter07/07_heat_conduction.svg)

## Video tham khảo

- xem trước: [Deriving the Heat Equation: A Parabolic Partial Differential Equation for Heat Energy Conservation](https://www.youtube.com/watch?v=9d8PwnKVA-U) — Steve Brunton, English. Brunton derives the heat equation from energy conservation.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, English. 3Blue1Brown solves the heat equation by Fourier modes.
- [The Heat Equation and the Steady State Heat Distribution via Laplace's Equation](https://www.youtube.com/watch?v=OoRwXVIXpL0) — Steve Brunton, English. The steady state of the heat equation is Laplace's equation, the equilibrium of this application.

## References

- Boyce & DiPrima, Chapter 10: boundary-value treatment of equilibrium conduction models.
- Haberman, Chapter 5: strong applied interpretation.
