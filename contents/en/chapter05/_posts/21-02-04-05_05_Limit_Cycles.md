---
layout: post
title: "05-05 Limit Cycles"
chapter: '05'
order: 5
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

Your heartbeat does not die down like a damped pendulum, nor does it depend delicately on its initial amplitude like a frictionless spring: whether you rest or sprint, your cardiac pacemaker snaps reliably back onto the exact same self-sustained oscillation. Linear ODEs can *never* produce an isolated, self-correcting periodic orbit—only nonlinear systems exhibit **limit cycles**, the mathematical heartbeat of clocks, neurons, lasers, and circadian rhythms.

## Background Knowledge Map: Proving and Ruling Out Limit Cycles in the Plane

Four theorems form the complete toolkit for planar periodic orbits:

1. **Isolated Periodic Orbit (Stable vs. Unstable vs. Semistable):** Unlike a linear center (a continuous family of nested ellipses), a **limit cycle** $$\Gamma$$ is an *isolated* closed trajectory; nearby trajectories spiral onto $$\Gamma$$ (stable/attracting), away from $$\Gamma$$ (unstable/repelling), or one of each (semistable).
2. **Poincaré–Bendixson Theorem (Existence):** If a closed, bounded, positively invariant region $$R \subset \mathbb{R}^2$$ (such as an annulus with inward-pointing arrows on both inner and outer boundaries) contains **no equilibria**, then $$R$$ MUST contain at least one periodic orbit! (Strictly 2D—fails in $$\mathbb{R}^3$$ where strange attractors exist!)
3. **Bendixson–Dulac Criterion (Non-Existence):** If $$\operatorname{div}(B\mathbf{f}) = \frac{\partial(Bf)}{\partial x} + \frac{\partial(Bg)}{\partial y}$$ has a strict constant sign ($$> 0$$ or $$< 0$$) across a simply connected region $$D$$ for some smooth weighting function $$B(x,y)$$, then Green's Theorem forbids *any* closed orbit inside $$D$$!
4. **Index / Gradient Obstructions:** Every planar closed orbit must enclose at least one equilibrium point (index sum $$= +1$$), and a pure gradient system $$\mathbf{x}' = -\nabla V(\mathbf{x})$$ can *never* have a limit cycle because $$V$$ strictly decreases along every non-constant orbit!

### Step-by-Step Worked Example (Read Slowly): Trapping a Stable Limit Cycle in Polar Coordinates and Testing Bendixson

**Part A — Exact Stable Limit Cycle in Polar Form:**
Analyze the nonlinear planar system (Hopf normal form):
$$x' = -y + x\bigl(4 - x^2 - y^2\bigr), \qquad y' = x + y\bigl(4 - x^2 - y^2\bigr).$$

1. **Convert to polar coordinates $$(r, \theta)$$ using $$r r' = x x' + y y'$$ and $$r^2 \theta' = x y' - y x'$$:**
   $$r r' = (x^2 + y^2)(4 - r^2) = r^2(4 - r^2) \implies r' = r(4 - r^2), \qquad \theta' = 1.$$
2. **Read the radial phase line for $$r \ge 0$$:**
   - $$r = 0$$ is an unstable equilibrium ($$r' > 0$$ for $$0 < r < 2$$).
   - $$r = 2$$ is a **stable periodic orbit** (the circle $$x^2 + y^2 = 4$$ traversed counterclockwise at period $$T = 2\pi$$):
     - Inside ($$0 < r < 2$$): $$r' > 0$$ (trajectories spiral **outward** toward $$r = 2$$).
     - Outside ($$r > 2$$): $$r' < 0$$ (trajectories spiral **inward** toward $$r = 2$$).
   - Notice the annulus $$1 \le r \le 3$$ has $$r'\vert_{r=1} = +3 > 0$$ (inward) and $$r'\vert_{r=3} = -15 < 0$$ (inward) with zero equilibria inside—a textbook Poincaré–Bendixson trapping region!

**Part B — Ruling Out Closed Orbits with Bendixson's Criterion:**
Consider $$x' = y - x^3,\; y' = -x - y^3$$ on $$\mathbb{R}^2$$:
3. **Compute the divergence:**
   $$\frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} = -3x^2 - 3y^2 = -3(x^2 + y^2) < 0 \quad \text{for all } (x,y) \ne (0,0).$$
   Because the divergence is strictly negative everywhere except a single point, Bendixson's theorem guarantees this system has **zero limit cycles** anywhere in $$\mathbb{R}^2$$!

## Learning Objectives

This lesson helps students understand limit cycles as isolated periodic orbits, distinguish them from families of closed curves, interpret attracting and repelling periodic motion, and see why self-sustained oscillation is one of the hallmark behaviors of nonlinear systems.

## Prerequisites

Students should know planar phase portraits, equilibria, local stability, and the basic idea of periodic motion. Familiarity with the van der Pol oscillator is helpful but not required.

## Introduction

![Limit cycle with nearby trajectories]({{ site.imgurl }}/chapter_img/chapter05/05_limit_cycles.svg)

Oscillation is one of the most important recurring patterns in applied mathematics. But not all oscillations are alike. A linear center produces a whole family of closed orbits, while many nonlinear systems possess a single isolated periodic orbit that attracts nearby motion. That isolated periodic orbit is called a limit cycle.

Limit cycles matter because they explain self-sustained rhythms. A system may neither settle to equilibrium nor wander chaotically. Instead, it may lock onto a stable repeating pattern that persists despite perturbations. This is the mathematical language behind many biological, chemical, and engineering oscillators.

## Concept in Three Ways

### Intuitive View

A limit cycle is a repeating motion that the system prefers. Start nearby and the trajectory is pulled toward that repeating loop. Start slightly off and the system corrects itself back to the same rhythm.

### Visual View

In the phase plane, a stable limit cycle appears as a closed loop with nearby trajectories spiraling or drifting toward it. An unstable limit cycle pushes nearby trajectories away. Isolation is the key visual feature: the periodic orbit stands alone rather than belonging to a continuous family.

### Formal View

A limit cycle is an isolated periodic orbit of a planar autonomous system. If nearby trajectories approach it as $$ t\to\infty $$, the cycle is stable. If they move away, it is unstable. The Poincare-Bendixson theorem gives a major reason limit cycles are so important in planar systems.

## Common Misconceptions

- "Any closed orbit is a limit cycle." Wrong. The orbit must be isolated.
- "Every oscillatory system has a limit cycle." Wrong. Some systems have centers, quasiperiodicity, or decaying oscillations instead.
- "A limit cycle always comes from a linear system." Wrong. It is fundamentally nonlinear.
- "Periodic behavior always means conserved energy." Wrong. Many stable limit cycles involve gain and dissipation balancing each other.

## Suggested Learning Path

### Step 1: Distinguish Closed Orbits from Limit Cycles

Students should first understand why isolation matters.

### Step 2: Look at Nearby Trajectories

This determines whether the cycle is attracting or repelling.

### Step 3: Study a Standard Example

The van der Pol oscillator is the most common first model.

### Step 4: Connect to Applications

Students should learn to interpret limit cycles as self-sustained rhythms.

### Checkpoints

- Can students explain why a linear center does not give a limit cycle?
- Can students determine whether a periodic orbit is attracting?
- Do students understand why numerical simulation is often essential here?

## Worked Examples

### Example 1: Center Versus Limit Cycle

The linear system
$$ x'=y,\qquad y'=-x $$
has a family of closed orbits, but no isolated one. Therefore it has a center, not a limit cycle.

### Example 2: van der Pol Oscillator

Consider
$$ x'=y,\qquad y'=\mu(1-x^2)y-x $$
with $$ \mu>0 $$. Nearby trajectories are pushed away from the origin, but large-amplitude motion is damped. This combination typically creates a stable limit cycle.

### Example 3: Why Isolation Matters

If every nearby initial condition produces a different closed orbit, then the system is not selecting one preferred rhythm. A limit cycle, by contrast, acts as a distinguished periodic attractor.

## Conceptual Questions

1. Why is isolation essential in the definition of a limit cycle?
2. What is the difference between a center and a stable limit cycle?
3. Why are limit cycles especially important in applications involving repeated rhythms?

## Application Problems

1. In electronics, why is a stable limit cycle a good model for a sustained oscillator circuit?
2. In biology, how does a limit cycle help explain a self-maintained rhythm?
3. In mechanics, why can nonlinear damping create a preferred amplitude instead of total decay?

## Interactive Teaching Strategies

- Show students a center and a limit cycle side by side and ask them to describe the difference.
- Use simulations from several initial conditions to emphasize attraction toward one periodic orbit.
- Ask students to predict whether a periodic orbit is stable before checking numerically.
- Connect the phase-plane picture to physical language such as "self-sustained rhythm" or "preferred amplitude."

## Differentiation

### Support for Struggling Students

Students who need support should focus on the basic visual distinction: centers have many nearby closed curves, while stable limit cycles attract nearby trajectories.

### Challenge for Advanced Students

Advanced students can study the Poincare-Bendixson theorem and how it helps justify periodic behavior in planar systems.

## Summary

Limit cycles are isolated periodic orbits that organize nonlinear oscillation. They provide the mathematical language for self-sustained repeating behavior in systems that are neither simply stable nor simply divergent.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Self-sustained electronic oscillation
- Problem: An oscillator circuit should settle to a stable amplitude instead of decaying or blowing up.
- Model:
$$ \dot{x}=y,\qquad
\dot{y}=\mu(1-x^2)y-x. $$
- Assumptions and limitations: The model is a reduced description of gain and nonlinear saturation.
- Interpretation: A stable limit cycle explains why many initial states converge to the same periodic waveform.

#### Biological rhythms and heart cells
- Problem: A biological system needs a robust repeating rhythm despite perturbations.
- Model: A planar nonlinear system with an isolated stable periodic orbit.
- Assumptions and limitations: Real biological oscillators are often higher-dimensional.
- Interpretation: A limit cycle describes an intrinsic rhythm, not just conservative periodic motion.

### 2. Additional Intuition and Connections

A limit cycle is an isolated periodic orbit. That is different from the family of closed orbits around a linear center. A common pitfall is to see a closed curve and immediately call it a limit cycle; isolation and nearby attraction or repulsion matter. This topic links local stability to sustained oscillations and prepares the ground for Hopf bifurcation.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

mu = 1.5

def vdp(t, z):
    x, y = z
    return [y, mu * (1 - x**2) * y - x]

for z0 in [(0.2, 0.0), (2.0, 0.0), (0.5, 2.0)]:
    sol = solve_ivp(vdp, [0, 30], z0, max_step=0.05)
    plt.plot(sol.y[0], sol.y[1], lw=2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Convergence to the van der Pol limit cycle")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: van der Pol limit cycle phase portrait
- search: Poincare Bendixson visualization
- search: stable periodic orbit nonlinear oscillator

### 5. Worked Example

For the van der Pol system with $$ \mu>0 $$, trajectories near the origin are pushed outward, while trajectories far away are pulled inward by nonlinear damping. This inward-outward combination creates a stable periodic orbit. Because explicit closed-form solutions are rare, numerical simulation is the main practical tool.

### 6. Difficulty Layering

**Undergraduate level.** Understand the definition, identify limit cycles, and interpret nearby attraction or repulsion.

**Graduate level.** Use the Poincare-Bendixson theorem, Poincare maps, and Hopf bifurcation to explain the creation of periodic orbits.

![Limit cycles]({{ site.imgurl }}/chapter_img/chapter05/05_05_limit_cycles.svg)

## Video tham khảo

- xem trước: [MAE5790-8 Index theory and introduction to limit cycles](https://www.youtube.com/watch?v=O2fcpxLT5wk) — Cornell MAE, English. Index theory and the first appearance of a limit cycle in Strogatz's course.
- [MAE5790-9 Testing for closed orbits](https://www.youtube.com/watch?v=nWO74rlr58Y) — Cornell MAE, English. Tests for closed orbits.
- [MAE5790-10 van der Pol oscillator](https://www.youtube.com/watch?v=O1lQrHemPsw) — Cornell MAE, English. The van der Pol oscillator as the standard attracting cycle.

## References

- Strogatz, Chapter 7: excellent first introduction to periodic orbits and limit cycles.
- Arnold, Chapter 6: valuable geometric viewpoint on planar oscillatory dynamics.
