---
layout: post
title: "09-03 Homogeneous Boundary Conditions"
chapter: '09'
order: 3
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: required
---

Dip both ends of a metal rod in ice water and every drop of heat eventually escapes until the rod sits flat at $$ 0^\circ\text{C} $$. Now wrap both ends in perfect thermal insulation instead: no heat can leave, so the rod's total thermal energy is conserved forever and the temperature settles to the exact spatial average of its initial state. Change one end to Newton convective cooling ($$ u_x + h u = 0 $$), and the eigenvalues stop being neat multiples of $$ \pi $$ and become roots of a transcendental equation!

This lesson shows how the three classical homogeneous boundary conditions—Dirichlet, Neumann, and Robin—sculpt both the eigenbasis and the long-time fate of a diffusing rod.

## Key ideas: How Homogeneous BCs Control Thermal Fate

1. **Dirichlet BCs ($$ u(0,t) = u(L,t) = 0 $$ — Ice Baths):** Eigenfunctions are $$ \sin(n\pi x/L) $$ with $$ \lambda_n = (n\pi/L)^2 > 0 $$. Since $$ \lambda_1 > 0 $$, *every* mode decays exponentially and $$ u(x, t) \to 0 $$ as $$ t \to \infty $$.
2. **Neumann BCs ($$ u_x(0,t) = u_x(L,t) = 0 $$ — Insulated Ends):** Eigenfunctions are $$ \cos(n\pi x/L) $$ for $$ n = 0, 1, 2, \dots $$ including the **zero eigenvalue** $$ \lambda_0 = 0 $$ ($$ X_0(x) = 1 $$). Thus $$ u(x, t) \to \frac{a_0}{2} = \frac{1}{L}\int_0^L f(x)\,dx $$ as $$ t \to \infty $$, reflecting exact energy conservation!
3. **Mixed & Robin BCs ($$ u_x(L,t) + h u(L,t) = 0 $$ — Convective Cooling):** Mixing value and flux yields transcendental eigenvalue equations like $$ \tan(\mu L) = -\frac{\mu}{h} $$. For $$ h > 0 $$, heat leaks out into the ambient medium, so all eigenvalues remain strictly positive and $$ u \to 0 $$.
4. **Spectral Gap & Equilibration Speed:** The smallest nonzero eigenvalue $$ \lambda_{\min} $$ sets the exact asymptotic relaxation rate $$ e^{-\alpha \lambda_{\min} t} $$.

### Worked example: Insulated Rod Equilibration and Energy Conservation Check

**Problem:** A thermally insulated rod of length $$ L = 2 $$ with $$ \alpha = 1 $$ satisfies $$ u_t = u_{xx} $$, $$ u_x(0, t) = u_x(2, t) = 0 $$, and initial temperature $$ u(x, 0) = 10 + 6\cos(\pi x) $$. Solve for $$ u(x, t) $$, verify total thermal energy $$ E(t) = \int_0^2 u(x, t)\,dx $$ is constant in time, and find $$ \lim_{t\to\infty} u(x, t) $$.

1. **Identify the Neumann eigenvalues on $$ [0, 2] $$:**
   For $$ X'' + \lambda X = 0 $$ with $$ X'(0) = X'(2) = 0 $$, the eigenfunctions are $$ X_n(x) = \cos\!\left(\frac{n\pi x}{2}\right) $$ with $$ \lambda_n = \left(\frac{n\pi}{2}\right)^2 $$ for $$ n = 0, 1, 2, \dots $$
2. **Match $$ u(x, 0) = 10 + 6\cos(\pi x) $$ to the eigenbasis:**
   - $$ 10 = 10 \cdot X_0(x) $$ corresponds to $$ n = 0 $$ ($$ \lambda_0 = 0 $$).
   - $$ 6\cos(\pi x) = 6\cos\!\left(\frac{2\pi x}{2}\right) $$ corresponds to $$ n = 2 $$ ($$ \lambda_2 = \pi^2 $$)!
3. **Write the exact time-dependent solution:**
   $$ u(x, t) = 10 + 6 e^{-\pi^2 t} \cos(\pi x). $$
4. **Verify boundary conditions, energy conservation, and equilibrium:**
   - BCs: $$ u_x(x, t) = -6\pi e^{-\pi^2 t}\sin(\pi x) $$, which vanishes at both $$ x = 0 $$ and $$ x = 2 $$ for all $$ t > 0 $$.
   - Total energy: $$ E(t) = \int_0^2 \bigl[10 + 6 e^{-\pi^2 t}\cos(\pi x)\bigr]\,dx = 20 + 6 e^{-\pi^2 t}\left[\frac{\sin(\pi x)}{\pi}\right]_0^2 = 20 $$ (strictly constant for all $$ t \ge 0 $$!).
   - Long-time limit: as $$ t \to \infty $$, $$ e^{-\pi^2 t} \to 0 $$, so $$ u(x, t) \to 10 = \frac{E(0)}{L} $$ uniformly across the rod!

## Learning Objectives

This lesson studies Dirichlet and Neumann boundary conditions for the heat equation. Students should understand how different boundary conditions select different eigenfunction families and encode different physical constraints.

## Prerequisites

Students should know separation of variables for the heat equation and basic eigenvalue problems from earlier chapters.

## Introduction

![Homogeneous boundary conditions for heat equation]({{ site.imgurl }}/chapter_img/chapter09/03_homogeneous_bcs_heat.svg)

The heat equation does not live in the interior of the domain alone. Its solution is shaped decisively by the conditions imposed at the boundary. Once separation of variables is introduced, one immediately sees that the boundary conditions determine which spatial eigenfunctions are admissible.

This makes homogeneous boundary conditions conceptually central. They do not merely simplify the algebra. They encode the physical interaction between the rod and its environment and determine the modal structure of the solution.

## Concept in Three Ways

### Intuitive View

If the endpoints of a rod are held at zero temperature, heat is absorbed at the ends, and the temperature profile must vanish there. If instead the boundary is insulated, then no heat crosses the boundary, so the temperature gradient must vanish there.

### Visual View

Dirichlet conditions force the graph of the temperature profile to meet fixed endpoint values. Neumann conditions instead constrain the slope at the endpoints. These two requirements lead to different families of spatial modes.

### Formal View

For a separated solution of the heat equation,
$$ u(x,t)=X(x)T(t), $$
the spatial factor solves an eigenvalue problem. Under homogeneous Dirichlet conditions,
$$ X(0)=X(L)=0, $$
the eigenfunctions are sine modes. Under homogeneous Neumann conditions,
$$ X'(0)=X'(L)=0, $$
the eigenfunctions are cosine-type modes.

## Why the Boundary Conditions Matter

Different boundary conditions correspond to different physics and different mathematics. Dirichlet conditions usually model a boundary held at prescribed temperature, while Neumann conditions model insulation or zero flux.

Because the eigenvalues and eigenfunctions depend on the boundary data, the entire separated solution changes when the physical interpretation of the endpoints changes.

## Common Misconceptions

### "Boundary conditions are secondary details"

No. They determine the admissible spatial modes and can completely change the solution family.

### "Dirichlet and Neumann problems are basically the same"

No. They correspond to different physical meanings and different eigenfunction bases.

### "Only the interior PDE matters"

Wrong. In boundary-value PDE theory, the boundary data are part of the problem itself, not an afterthought.

## Suggested Learning Path

### Step 1: Interpret the physical boundary

Students should first understand what it means physically to fix temperature or fix heat flux.

### Step 2: Solve the spatial eigenvalue problem

The role of the boundary conditions in selecting eigenfunctions should be explicit.

### Step 3: Compare Dirichlet and Neumann modes

This reveals how the same PDE can lead to different spectral structures.

### Step 4: Connect to later PDE applications

Boundary conditions are one of the main reasons Fourier sine and cosine expansions appear so naturally.

### Checkpoints

- Can students explain the physical meaning of Dirichlet and Neumann conditions?
- Do they know which boundary conditions lead to sine modes and which to cosine modes?
- Can they see why changing the boundary changes the full solution structure?

## Worked Examples

### Example 1: Fixed Endpoint Temperatures

For a rod with both ends held at zero temperature, the spatial eigenfunctions are sine modes. These vanish automatically at the endpoints.

### Example 2: Insulated Endpoints

If both ends are insulated, the relevant boundary conditions are Neumann, and cosine-type modes appear instead.

### Example 3: Mixed Interpretation

A rod can have one endpoint fixed in temperature and the other insulated. In that case, the eigenfunctions are different again, showing that the mode family is highly sensitive to the boundary model.

## Conceptual Questions

1. Why do homogeneous boundary conditions determine the admissible spatial basis?
2. Why are Dirichlet conditions naturally associated with sine modes?
3. Why do insulated boundaries lead to derivative constraints rather than value constraints?

## Application Problems

1. In a physical rod, when is a Dirichlet model more appropriate than a Neumann model?
2. How does boundary insulation affect long-term temperature behavior?
3. Why are cosine expansions more natural for zero-flux conditions?

## Interactive Teaching Strategies

- Compare endpoint behavior of sine and cosine functions visually.
- Ask students to classify physical scenarios as Dirichlet or Neumann before solving anything.
- Use side-by-side mode sketches to reinforce the different eigenfunction families.
- Emphasize that boundary conditions are spectral selection rules.

## Differentiation

### Support for Struggling Students

Students needing support should work with graph sketches of sine and cosine modes and connect them directly to endpoint constraints.

### Challenge for Advanced Students

Advanced students can explore Robin or mixed boundary conditions and examine how the eigenvalues shift.

## Summary

Boundary conditions determine the admissible spatial modes. They are not side constraints; they shape the entire solution structure. In the heat equation, homogeneous Dirichlet and Neumann conditions are two of the most important examples because they connect directly to sine and cosine expansions.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Rod with fixed-temperature ends
- Problem: Homogeneous Dirichlet conditions model endpoints held at a fixed reference temperature.
- Model:
$$ u(0,t)=u(L,t)=0. $$
- Assumptions and limitations: The boundary is perfectly controlled.
- Interpretation: The natural eigenbasis is the sine family.

#### Insulated endpoint
- Problem: Homogeneous Neumann conditions model zero heat flux across the boundary.
- Model:
$$ u_x(0,t)=0 \quad \text{or} \quad u_x(L,t)=0. $$
- Assumptions and limitations: Ideal insulation.
- Interpretation: The natural eigenbasis becomes the cosine family.

### 2. Additional Intuition and Connections

Boundary conditions determine the mode basis, not just a few constants. A common pitfall is to use the wrong sine-cosine basis because the physical meaning of the boundary has been ignored. This lesson is a direct bridge between Fourier series and PDE.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, np.sin(np.pi * x))
axes[0].set_title("Dirichlet -> sine mode")
axes[1].plot(x, np.cos(np.pi * x))
axes[1].set_title("Neumann -> cosine mode")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: Dirichlet Neumann heat equation modes
- search: homogeneous boundary conditions heat equation
- search: sine cosine basis PDE boundary conditions

### 5. Worked Example

With homogeneous Dirichlet conditions,
$$ u(0,t)=u(L,t)=0, $$
the spatial problem gives
$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right). $$
With homogeneous Neumann conditions,
$$ u_x(0,t)=u_x(L,t)=0, $$
we obtain
$$ \phi_n(x)=\cos\left(\frac{n\pi x}{L}\right). $$
This is the clearest example of the boundary determining the spectral family.

### 6. Difficulty Layering

**Undergraduate level.** Match the correct boundary condition to the correct eigenbasis.

**Graduate level.** Connect to self-adjoint realizations of the Laplacian under different domains.

## Video tham khảo

- xem trước: [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, English. Homogeneous endpoint conditions are what let the sine modes fit the bar in this solution.
- [Deriving the Heat Equation: A Parabolic Partial Differential Equation for Heat Energy Conservation](https://www.youtube.com/watch?v=9d8PwnKVA-U) — Steve Brunton, English. The derivation, including the boundary terms that become those homogeneous conditions.
- [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, English. Separation with boundary conditions imposed on the spatial eigenvalue problem.

## References

- Evans, Chapter 2.
