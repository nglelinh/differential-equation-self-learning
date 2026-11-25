---
layout: post
title: "13-06 Stability and Convergence (CFL)"
chapter: '13'
order: 6
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: required
---

> **Storytelling Hook:** Why does doubling the spatial resolution of an explicit heat-equation simulation force you to take *four times* as many time steps—and why does a wave simulation shatter into jagged noise the instant $\Delta t$ exceeds $\Delta x / c$? Two of the most famous results in computational mathematics—**von Neumann stability analysis** and the **CFL condition**—reveal the exact speed limits governing numerical PDEs.

## Learning Objectives

This lesson develops the ideas of stability, convergence, and CFL-type restrictions in numerical PDE schemes. Students should understand why consistent discretization is not enough, how instability manifests computationally, and why the CFL condition captures a basic compatibility between mesh and propagation.

## Prerequisites

Students should know finite-difference PDE schemes and basic numerical stability ideas from ODE methods.

## Key ideas: Stability, Fourier Amplification, and the CFL Speed Limit

Four foundational principles connect discrete PDE stencils to guaranteed convergence:

1. **Lax Equivalence Theorem:** For a consistent finite-difference approximation to a well-posed linear initial-value PDE, **stability is both necessary and sufficient for convergence** as $\Delta x, \Delta t \to 0$.
2. **Von Neumann (Fourier Mode) Stability Analysis:** Substituting a single discrete Fourier mode $U_j^n = G(k)^n e^{ikj\Delta x}$ into a linear constant-coefficient scheme isolates the amplification factor $G(k)$; stability in $L^2$ requires $|G(k)| \le 1 + O(\Delta t)$ for all wavenumbers $k\Delta x \in [-\pi, \pi]$.
3. **The Courant–Friedrichs–Lewy (CFL) Necessary Condition:** For hyperbolic PDEs ($u_t + c u_x = 0$), the numerical domain of dependence must contain the physical characteristic cone—requiring the Courant number $\text{CFL} = |c|\Delta t / \Delta x \le 1$ for standard 3-point explicit schemes.
4. **Parabolic vs. Hyperbolic Scaling:** Explicit diffusion stencils require $\nu\Delta t / (\Delta x)^2 \le \frac{1}{2}$ (quadratic time-step penalty!), motivating unconditionally stable implicit schemes like **Crank–Nicolson**, where $|G(k)| \le 1$ for every $\Delta t > 0$.

## Introduction

![Stability and convergence CFL]({{ site.imgurl }}/chapter_img/chapter13/06_stability_convergence_cfl.svg)

Once a numerical PDE scheme has been written down, three questions immediately arise. Is it consistent with the PDE? Is it stable under repeated iteration? And if both are true, does it actually converge to the correct solution? These questions form the backbone of numerical PDE analysis.

For time-dependent hyperbolic and parabolic problems, the CFL condition is one of the most famous manifestations of these ideas.

## Concept in Three Ways

### Intuitive View

A numerical method must not let information move in an unphysical way relative to the mesh. If the grid and time step are badly mismatched, the computation can become unstable.

### Visual View

One may think of the numerical domain of dependence and compare it with the PDE's true domain of dependence. The CFL condition expresses compatibility between them.

### Formal View

Consistency measures whether the discrete equations approximate the continuous PDE. Stability measures whether errors remain controlled under iteration. Convergence means the numerical solution approaches the true solution as the mesh is refined.

## Why the Topic Matters

This lesson is one of the conceptual cores of numerical PDEs. It teaches that numerical correctness is a three-part story: consistency, stability, and convergence. A beautifully derived stencil can still be useless if it is unstable.

The CFL condition is especially memorable because it ties abstract analysis to an intuitive propagation-speed constraint.

## Common Misconceptions

### "If a scheme is consistent, it must converge"

No. Stability is also essential.

### "Instability just means the answer is a bit inaccurate"

No. Instability can make the computation completely meaningless.

### "CFL is only a technical restriction for experts"

No. It captures one of the most basic structural truths of mesh-based wave propagation.

## Suggested Learning Path

### Step 1: Separate the three ideas

Students should keep consistency, stability, and convergence conceptually distinct.

### Step 2: Study examples of instability

This makes the need for analysis concrete.

### Step 3: Introduce CFL intuition

The geometric picture of information travel should come first.

### Step 4: Connect to rigorous convergence principles

This completes the theoretical structure.

### Checkpoints

- Can students distinguish consistency, stability, and convergence?
- Do they understand why instability can destroy a scheme even if the stencil looks reasonable?
- Can they explain the intuitive meaning of a CFL condition?

## Worked Examples


### Worked example: Von Neumann Analysis of Explicit FTCS for the Heat Equation

Derive the exact stability threshold $r = \frac{\nu\Delta t}{(\Delta x)^2} \le \frac{1}{2}$ for the forward-time centered-space (FTCS) heat scheme $U_j^{n+1} = U_j^n + r(U_{j+1}^n - 2U_j^n + U_{j-1}^n)$, and test the worst-case sawtooth mode at $r = 0.4$ vs. $r = 0.6$.

1. **Insert the Fourier ansatz $U_j^n = G^n e^{i\theta j}$** (where $\theta = k\Delta x \in [-\pi, \pi]$):
   $$G = 1 + r\big(e^{i\theta} - 2 + e^{-i\theta}\big) = 1 + r\big(2\cos\theta - 2\big) = 1 - 4r\sin^2\!\left(\frac{\theta}{2}\right).$$
2. **Enforce $|G(\theta)| \le 1$ for all $\theta \in [-\pi, \pi]$:** Since $0 \le \sin^2(\theta/2) \le 1$ and $r > 0$, we automatically have $G(\theta) \le 1$. The danger is the lower bound at the highest grid frequency $\theta = \pi$ (the alternating sawtooth $(-1)^j$, where $\sin^2(\pi/2) = 1$):
   $$G(\pi) = 1 - 4r \ge -1 \iff 4r \le 2 \iff r = \frac{\nu\Delta t}{(\Delta x)^2} \le \frac{1}{2}.$$
3. **Check numerically on the sawtooth mode $U_j^0 = (-1)^j$:**
   - At $r = 0.4$ (stable): $G(\pi) = 1 - 1.6 = -0.6$, so after $5$ steps the sawtooth shrinks to $(-0.6)^5 = -0.0778$.
   - At $r = 0.6$ (unstable): $G(\pi) = 1 - 2.4 = -1.4$, so after $10$ steps the sawtooth grows to $(-1.4)^{10} \approx +28.93$, and after $50$ steps to $2.0 \times 10^7$—exploding from pure round-off noise!

### Example 1: Stable Heat Scheme

A parabolic scheme with an appropriate step restriction behaves smoothly and converges.

### Example 2: Unstable Explicit Scheme

With a too-large time step, oscillations or blow-up appear, showing that consistency alone is not enough.

### Example 3: Wave Equation CFL Condition

The numerical domain of dependence must contain the physical one, giving a concrete mesh-speed relation.

## Conceptual Questions

1. Why is stability indispensable for convergence?
2. Why does the CFL condition have a geometric interpretation?
3. Why is numerical analysis about more than discretizing derivatives?

## Application Problems

1. Why might a computationally cheap explicit scheme fail completely in practice?
2. Why is the CFL condition especially natural for transport and wave problems?
3. How does stability analysis guide mesh and time-step selection in simulations?

## Interactive Teaching Strategies

- Compare stable and unstable simulations visually.
- Use domain-of-dependence diagrams to explain CFL.
- Ask students to classify statements as about consistency, stability, or convergence.
- Reinforce that numerical analysis is a structural theory, not just implementation.

## Differentiation

### Support for Struggling Students

Students needing support should work with concrete stable/unstable examples before formal theorem language.

### Challenge for Advanced Students

Advanced students can explore von Neumann analysis or the Lax equivalence framework.

## Summary

Stability and convergence are central to numerical PDE theory, and the CFL condition is one of the clearest examples of how mesh structure must respect PDE propagation. A consistent scheme becomes meaningful only when stability is also secured.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Weather and wave forecasting
- Problem: The time step must be compatible with grid spacing and propagation speed.
- Model: A typical CFL condition for transport or wave problems has the form
$$ \frac{c\Delta t}{\Delta x}\le C. $$
- Assumptions and limitations: The exact constant depends on the scheme; violating CFL often causes numerical blow-up.
- Interpretation: Physical information must not outrun the numerical grid.

#### Traffic flow or fluid dynamics
- Problem: Shock-like features require a stable relation between mesh size and step size.
- Model: Analyze a scheme through Fourier or von Neumann stability.
- Assumptions and limitations: Linearized analysis captures only part of nonlinear behavior.
- Interpretation: Stability and convergence must be studied together.

### 2. Additional Intuition and Connections

Consistency says the scheme approximates the PDE locally; stability says errors are not amplified without bound; convergence says the numerical solution approaches the exact one. The Lax-Richtmyer principle shows that, in suitable linear settings, consistency plus stability yields convergence. A common pitfall is to verify consistency and assume the rest follows automatically.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

nu = np.linspace(0, 1.5, 400)
G = np.abs(1 - 1j * nu)

plt.plot(nu, G)
plt.axhline(1, color="black", linewidth=0.8)
plt.xlabel("dimensionless CFL / frequency")
plt.ylabel("|G|")
plt.title("Amplification factor and stability")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: CFL condition animation numerical wave propagation
- search: von Neumann stability visualization
- search: Lax equivalence theorem intuition

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="The CFL condition in the upwind scheme" description="Adjust the CFL number directly and see when the numerical profile still tracks physical transport and when it begins to break down." path="interactives/chapter13/cfl-condition-en.html" height="640px" %}

### 5. Worked Example

For the transport equation
$$ u_t + c u_x = 0 $$
with explicit upwind scheme,
$$
u_j^{n+1}=u_j^n-\nu(u_j^n-u_{j-1}^n),\qquad \nu=\frac{c\Delta t}{\Delta x},
$$
stability holds when $$ 0\le \nu \le 1 $$. This is the familiar CFL restriction from wave and flow simulation.

### 6. Difficulty Layering

**Undergraduate level.** Understand the intuition of CFL and the relation among consistency, stability, and convergence.

**Graduate level.** Connect to von Neumann analysis, energy methods, and nonlinear stability concepts.

## Video tham khảo

- xem trước: [Harvard AM205 video 3.18 - CFL condition & upwinding](https://www.youtube.com/watch?v=GsilBPN8Ew4) — Chris Rycroft, English. Chris Rycroft on the CFL condition and upwinding.
- [Von Neumann analysis: derivation of the CFL criterion](https://www.youtube.com/watch?v=5_VtrWGaEGM) — LMU Seismology, English. Von Neumann analysis leading to a CFL restriction.
- [Stability of Forward Euler and Backward Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=RdXCGnTT6UY) — Steve Brunton, English. The ODE version of the same stability restriction, for Euler.

## References

- Ascher & Petzold: foundational treatment of numerical stability and convergence.
