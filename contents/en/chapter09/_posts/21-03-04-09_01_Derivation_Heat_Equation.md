---
layout: post
title: "09-01 Derivation of the Heat Equation"
chapter: '09'
order: 1
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: required
---

Drop a glowing ember onto one spot of a cold iron bar and watch what happens: heat does not jump magically across the bar, nor does it bounce back and forth like a sound wave. Instead, it spreads outward relentlessly from hot regions to cold regions, driven purely by local temperature differences. In 1807, Joseph Fourier captured this universal transport process in just two physical laws—conservation of thermal energy and Fourier's law of conduction—and fused them into the **Heat Equation**, $$ u_t = \alpha u_{xx} $$.

What makes this derivation extraordinary is its universality: replace temperature by dye concentration, financial option price, or probability density of a Brownian random walker, and the *exact same PDE* reappears.

## Background Knowledge Map: Conservation Laws and Diffusive Flux

1. **Integral Conservation Law (Balance on an Arbitrary Control Volume):** For any segment $$ [a, b] $$ of a 1D rod with cross-section $$ A $$, density $$ \rho $$, and specific heat $$ c $$, the rate of change of stored thermal energy $$ \frac{d}{dt}\int_a^b c\rho u(x,t)\,dx $$ equals net heat flowing in through the endpoints, $$ \phi(a,t) - \phi(b,t) $$, plus internal sources $$ \int_a^b Q(x,t)\,dx $$.
2. **Fourier's Constitutive Law of Heat Flux:** Empirically, heat flows *down* the temperature gradient: $$ \phi(x, t) = -K_0 u_x(x, t) $$, where $$ K_0 > 0 $$ is thermal conductivity. The minus sign is the Second Law of Thermodynamics in algebraic form!
3. **Curvature Drives Evolution (Geometric Meaning of $$ u_{xx} $$):** Combining conservation with Fourier's law yields $$ u_t = \alpha u_{xx} $$ with thermal diffusivity $$ \alpha = \frac{K_0}{c\rho} $$ (units $$ \text{m}^2/\text{s} $$). Where the temperature graph is concave down ($$ u_{xx} < 0 $$, a hot peak), $$ u_t < 0 $$ so the peak cools; where it is concave up ($$ u_{xx} > 0 $$, a cold valley), $$ u_t > 0 $$ so the valley warms!
4. **Dimensional Scaling $$ L^2 / \alpha $$:** Because time enters as a first derivative and space as a second derivative, the equation is invariant under the parabolic scaling $$ (x, t) \mapsto (\lambda x, \lambda^2 t) $$—doubling length quadruples diffusion time.

### Step-by-Step Worked Example (Read Slowly): Deriving $$ u_t = \alpha u_{xx} + q $$ and Computing Local Cooling Rate

**Problem:** (a) Starting from the integral balance $$ \frac{d}{dt}\int_a^b c\rho u\,dx = \phi(a,t) - \phi(b,t) + \int_a^b Q(x,t)\,dx $$ with $$ \phi = -K_0 u_x $$, derive the PDE for constant $$ c, \rho, K_0 $$. (b) An aluminum rod ($$ \alpha = 9.7 \times 10^{-5}\text{ m}^2/\text{s} $$) has instantaneous temperature profile $$ u(x, 0) = 20 + 80\sin(\pi x) $$ on $$ [0, 1]\text{ m} $$ with no internal source. Compute the exact initial cooling rate $$ u_t(0.5, 0) $$ in $$ ^\circ\text{C/s} $$ and the heat flux $$ \phi(0, 0) $$ at the left end (using $$ K_0 = 237\text{ W/(m}\cdot\text{K)} $$).

1. **Apply the Fundamental Theorem of Calculus to the boundary flux:**
   $$ \phi(a, t) - \phi(b, t) = -\int_a^b \frac{\partial \phi}{\partial x}\,dx = \int_a^b \frac{\partial}{\partial x}(K_0 u_x)\,dx. $$
2. **Collect all terms under one integral over arbitrary $$ [a, b] $$:**
   $$ \int_a^b \bigl[c\rho u_t - K_0 u_{xx} - Q(x,t)\bigr]\,dx = 0. $$
   Since $$ [a, b] $$ is arbitrary and the integrand is continuous, the integrand must vanish identically:
   $$ u_t = \alpha u_{xx} + \frac{Q}{c\rho}, \qquad \alpha = \frac{K_0}{c\rho}. $$
3. **Evaluate the initial cooling rate at the midpoint $$ x = 0.5\text{ m} $$:**
   - $$ u_x(x, 0) = 80\pi\cos(\pi x) $$.
   - $$ u_{xx}(x, 0) = -80\pi^2 \sin(\pi x) \implies u_{xx}(0.5, 0) = -80\pi^2 \approx -789.57\text{ }^\circ\text{C/m}^2 $$.
   - Cooling rate:
     $$ u_t(0.5, 0) = \alpha u_{xx}(0.5, 0) = (9.7 \times 10^{-5})(-789.57) \approx -0.0766\text{ }^\circ\text{C/s}. $$
   Negative sign confirms the hot peak is cooling!
4. **Compute the heat flux at $$ x = 0 $$:**
   $$ \phi(0, 0) = -K_0 u_x(0, 0) = -(237)(80\pi \cos 0) \approx -59{,}565\text{ W/m}^2. $$
   The negative flux means nearly $$ 60\text{ kW/m}^2 $$ of heat is rushing *leftward* out of the rod into the cold $$ 20^\circ\text{C} $$ bath at $$ x = 0 $$!

## Learning Objectives

This lesson derives the heat equation from conservation of energy and Fourier's law. Students should understand why diffusion produces a second spatial derivative, how constitutive assumptions enter the model, and why the resulting PDE describes smoothing rather than oscillation.

## Prerequisites

Students should know derivatives, flux ideas, and basic conservation laws. Some prior familiarity with Fourier series is useful, since later solution methods will rely on them, but the derivation itself is primarily a modeling argument.

## Introduction

![Derivation of the heat equation]({{ site.imgurl }}/chapter_img/chapter09/01_derivation_heat_equation.svg)

The heat equation is one of the foundational PDEs of mathematical physics. Its meaning is simple and profound: temperature evolves because heat flows from regions of high temperature to regions of low temperature. Unlike the wave equation, which preserves oscillatory motion, the heat equation describes a smoothing process. Peaks flatten, valleys fill in, and sharp distinctions gradually disappear.

What makes this equation so important pedagogically is that it emerges directly from first principles. We do not guess it. We derive it by combining a balance law with a constitutive law that relates heat flux to temperature gradient.

## Concept in Three Ways

### Intuitive View

Heat spreads because neighboring regions tend to equalize temperature differences. If one point is hotter than the surrounding material, energy flows outward. If one point is colder, energy flows inward. The system naturally moves toward thermal balance.

### Visual View

If we graph temperature along a rod, steep slopes indicate strong heat flow. A sharp temperature spike generates rapid spreading. Over time, the profile becomes smoother and more uniform.

### Formal View

Consider a thin rod with temperature $$ u(x,t) $$. Conservation of thermal energy says that the change in heat content of a small interval equals the net heat flux entering it. Fourier's law states that the heat flux is proportional to minus the temperature gradient:
$$ q=-k u_x. $$
Combining conservation with this law yields
$$ u_t=\alpha^2 u_{xx}, $$
where $$ \alpha^2 $$ is the thermal diffusivity.

## Why the Derivation Matters

The derivation teaches more than one PDE. It teaches a modeling template that appears throughout applied mathematics:

- identify a conserved quantity,
- write a balance law,
- specify a constitutive relation,
- combine them into a differential equation.

This framework reappears in mass transport, fluid flow, electromagnetism, and probability.

## Common Misconceptions

### "The heat equation is just a formula for temperature"

No. It is a balance law plus a constitutive law, and its structure reflects those assumptions.

### "The second derivative appears for purely algebraic reasons"

No. It appears because the flux depends on the first derivative, and conservation differentiates flux once more.

### "Heat propagation is like wave propagation"

Not at all. Heat diffusion smooths and dissipates contrast, whereas waves preserve oscillatory structure and transport disturbances differently.

### "Steady temperature means nothing is happening mathematically"

Wrong. Steady states are extremely important and lead directly to Laplace and Poisson equations later.

## Suggested Learning Path

### Step 1: Start from a small interval

Students should isolate a tiny rod segment and ask how its thermal energy changes.

### Step 2: Write the flux law

Heat flow is proportional to the negative temperature gradient.

### Step 3: Apply conservation

The time rate of change of heat content equals inflow minus outflow.

### Step 4: Take the limit

Passing from the interval balance to the differential equation yields the PDE.

### Checkpoints

- Can students explain why heat flows down the temperature gradient?
- Can they identify the meaning of each term in the derivation?
- Do they understand why the result is diffusion rather than transport or oscillation?

## Worked Examples

### Example 1: Constant Temperature

If $$ u(x,t)=C $$, then both $$ u_t $$ and $$ u_{xx} $$ vanish. Constant profiles are equilibrium solutions.

### Example 2: Linear Temperature Profile

If $$ u(x,t)=ax+b $$, then $$ u_{xx}=0 $$, so such profiles are also steady states in the absence of sources. This is an early hint that equilibrium heat profiles are closely tied to second derivatives.

### Example 3: A Concentrated Hot Spot

If the initial profile is sharply peaked, then the heat equation predicts rapid spreading and flattening. This is the characteristic signature of diffusion.

## Conceptual Questions

1. Why does Fourier's law use a negative sign?
2. Why does conservation lead from flux to a second derivative in space?
3. Why does the heat equation smooth rather than sharpen temperature profiles?

## Application Problems

1. In a biological tissue model, what quantity plays the role of diffusivity?
2. In financial mathematics, why does diffusion appear in models of uncertainty spread?
3. In material science, how does changing conductivity affect the rate of smoothing?

## Interactive Teaching Strategies

- Have students derive the PDE from a balance law in pairs.
- Ask them to compare the heat equation with the wave equation and list the conceptual differences.
- Use graphs of initial temperature distributions and ask what they expect qualitatively at later times.
- Reinforce that modeling assumptions, not symbolic manipulation alone, produce the PDE.

## Differentiation

### Support for Struggling Students

Students needing support should work repeatedly with the small-interval balance argument until the logic of flux difference becomes intuitive.

### Challenge for Advanced Students

Advanced students can examine variable conductivity, higher-dimensional derivations, or the probabilistic interpretation of diffusion.

## Summary

The heat equation is the canonical diffusion model. It emerges directly from conservation of energy and Fourier's law, and its structure explains why diffusion smooths profiles over time. This derivation is one of the central modeling patterns in the entire PDE course.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Heat conduction in a rod
- Problem: Heat flows from hotter to colder parts of a thin rod.
- Model:
$$ u_t=\alpha^2 u_{xx}. $$
- Assumptions and limitations: One-dimensional conduction, homogeneous material, no external source.
- Interpretation: The time derivative measures temperature change, while the spatial second derivative measures curvature of the temperature profile.

#### Diffusion of dissolved material
- Problem: Salt or dye spreads through a liquid.
- Model: The same heat equation with $$ u $$ interpreted as concentration.
- Assumptions and limitations: Constant diffusion coefficient and homogeneous medium.
- Interpretation: The heat equation is the universal model for smoothing gradients in diffusive processes.

### 2. Additional Intuition and Connections

The heat equation is the model example of diffusion: wherever the profile is strongly curved, time tends to flatten it. A common pitfall is to view the second derivative as only a computational detail. In fact it measures departure from local equilibrium. This lesson connects naturally to the steady-state BVPs of Chapter 7.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
u0 = np.where(x < 0.5, 1.0, 0.0)

plt.plot(x, u0, label="t = 0")
for t, sigma in [(0.002, 0.03), (0.01, 0.07), (0.03, 0.12)]:
    kernel = np.exp(-((x[:, None] - x[None, :])**2) / (4 * sigma**2))
    kernel /= kernel.sum(axis=1, keepdims=True)
    ut = kernel @ u0
    plt.plot(x, ut, label=f"t ~ {t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Smoothing of a heat profile over time")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: heat equation diffusion animation
- search: derivation Fourier law conservation energy heat equation
- search: smoothing effect heat equation

### 5. Worked Example

From Fourier's law
$$ q=-k u_x $$
and local conservation of energy on a short interval, we derive
$$ u_t=\alpha^2 u_{xx}. $$
The physical message is simple: heat flux follows the negative temperature gradient, and the local rate of temperature change is determined by the imbalance of incoming and outgoing flux.

### 6. Difficulty Layering

**Undergraduate level.** Understand the derivation from conservation and Fourier's law.

**Graduate level.** Emphasize the parabolic nature of the equation, instantaneous smoothing, and comparison with wave and elliptic equations.

## Video tham khảo

- xem trước: [Deriving the Heat Equation: A Parabolic Partial Differential Equation for Heat Energy Conservation](https://www.youtube.com/watch?v=9d8PwnKVA-U) — Steve Brunton, English. Brunton derives the one-dimensional heat equation from conservation.
- [But what is a partial differential equation?  | DE2](https://www.youtube.com/watch?v=ly4S0oi3Yz8) — 3Blue1Brown, English. 3Blue1Brown on what a partial differential equation is, with heat as the example.
- [(PHƯƠNG TRÌNH ĐẠO HÀM RIÊNG) PHƯƠNG TRÌNH TRUYỀN NHIỆT](https://www.youtube.com/watch?v=LJ6rd2EGVEI) — Đặng Pete, Vietnamese. A Vietnamese lecture deriving and introducing the heat equation.

## References

- Evans, Chapter 2: physical and mathematical derivation of diffusion equations.
- Haberman, Chapters 1-2: classical heat-conduction modeling.
