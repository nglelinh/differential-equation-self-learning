---
layout: post
title: "02-12 Modern Applications: Hamiltonian and Second-Order Neural Models"
chapter: '02'
order: 12
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: optional
---

## Objectives

This optional lesson relates constant-coefficient second-order equations, mechanical vibrations, and energy methods to the 2019–2024 literature on Hamiltonian, Lagrangian, and second-order neural networks. Students should be able to see a learned oscillator as a structured residual of $$y''+p y'+q y=g(t)$$, explain why symplectic or energy-preserving architectures outperform generic networks on conservative systems, and connect Wronskian independence to identifiability of learned modes. The classical solution techniques of the chapter are not rewritten.

## Prerequisites

Students should know the characteristic equation, damped and forced oscillators, reduction of order, and the interpretation of the Wronskian. A passing acquaintance with kinetic and potential energy for a unit-mass oscillator is enough.

## Introduction

The equation $$y''+\omega^2 y=0$$ is the simplest conservative oscillator. Its solutions rotate in the $$(y,y')$$ plane and preserve the energy $$\tfrac12(y')^2+\tfrac12\omega^2 y^2$$. When the same structure is hidden inside data—planetary motion, molecular dynamics, robotic arms, or electrical LC circuits—a generic neural network can fit short trajectories and still drift secularly because nothing forces it to conserve energy or a symplectic form.

Greydanus, Dzamba, and Yosinski introduced Hamiltonian neural networks at NeurIPS 2019 by learning a scalar Hamiltonian $$H_\theta(q,p)$$ and integrating Hamilton’s equations rather than an unstructured vector field. Cranmer, Greydanus, Hoyer, Battaglia, Spergel, and Ho (*Lagrangian Neural Networks*, 2020; [arXiv:2003.04630](https://arxiv.org/abs/2003.04630)) imposed the Euler–Lagrange equation instead, which is often easier when the data are positions and velocities rather than positions and momenta. Finzi, Wang, and Wilson (*Simplifying Hamiltonian and Lagrangian Neural Networks*, NeurIPS 2020) then showed how to encode constraints and coordinates more cleanly. The 2022 papers of Sosanya and Greydanus on dissipative Hamiltonian networks and of Gruver, Finzi, Goldblum, and Wilson (*Deconstructing the Inductive Biases of Hamiltonian Neural Networks*, ICLR 2022) clarified when those inductive biases actually help.

All of this work is a modern reading of the present chapter: second-order linear structure, energy, and linear independence of modes are not only solution devices, they are architectural priors.

## Key Concepts

### From characteristic roots to learned modes

A constant-coefficient equation $$y''+a y'+b y=0$$ has a two-dimensional solution space spanned by modes determined by the characteristic roots. A learned second-order model should recover a similar low-dimensional modal picture if the data are nearly linear. When the data are nonlinear but still conservative, the Hamiltonian picture replaces the characteristic polynomial: one learns $$H_\theta$$ and lets the geometry of its level sets organize the motion. Zhong, Dey, and Chakraborty (*Symplectic ODE-Net*, ICLR 2020) take the further step of integrating the learned field with a symplectic integrator, so that the numerical method respects the same structure as the continuous system.

### Energy as a Lyapunov-like diagnostic

For the undamped oscillator the energy is constant; for the damped oscillator it decreases. A neural model that is accurate in instantaneous $$L^2$$ error can still create energy, which is immediately visible as a secular growth of amplitude. Plotting a learned energy along a trajectory is therefore as informative as plotting a Wronskian: both are scalar diagnostics of structural fidelity. Dissipative Hamiltonian networks (Sosanya and Greydanus, 2022) split the vector field into a conservative piece and a Rayleigh-like dissipation, echoing the decomposition $$y''+\gamma y'+\omega^2 y=0$$ already studied here.

### Second-order neural ODEs

One may also learn a second-order field directly,

$$
q''=f_\theta(q,q',t),
$$

which is the natural form for mechanical systems and is equivalent to a first-order system in $$(q,q')$$. The reduction is the same one used to convert a second-order linear ODE into a first-order planar system. The advantage of staying in second-order form is that one can impose $$f_\theta=-\nabla V_\theta(q)-\gamma q'$$ and recover a forced, damped mechanical model with a learned potential.

### What the 2022–2024 analyses changed

Gruver et al. (ICLR 2022) showed that some reported gains of Hamiltonian networks come from easier integration or better coordinate choices rather than from a mystical energy prior. That caution is pedagogically valuable. Structure-preserving learning works when the data really are nearly Hamiltonian, just as undetermined coefficients work when the forcing really lies in the UC family. The chapter’s message is unchanged: exploit structure that is present, do not invent structure that is not.

## Methods and Solution Techniques

A practical pipeline looks like this.

1. Decide whether the data are conservative, dissipative, or forced. The same classification used for mechanical vibrations applies.
2. If conservative, learn $$H_\theta$$ or a Lagrangian $$L_\theta(q,\dot q)$$ and integrate with a symplectic or variational integrator.
3. If dissipative, learn an energy plus a dissipation potential, or learn a Rayleigh term.
4. If forced and nearly linear, compare the learned response with the particular solution produced by undetermined coefficients or variation of parameters.
5. Monitor modal diagnostics: instantaneous frequency, amplitude envelope, and a learned Wronskian-like independence measure when several modes are present.

Variation of parameters has a learning analogue. One may freeze a linear conservative core $$y''+\omega^2 y$$ and learn only a particular forcing network $$g_\theta(t)$$. The general solution is then the same superposition already proved in the chapter, with a data-driven particular solution.

## Examples

### Example 1: Fitting a noisy harmonic oscillator

Samples of $$y=\cos(\omega t)$$ with small noise can be fit by an unstructured neural ODE, but the learned period typically drifts. A Hamiltonian network with $$H_\theta=\tfrac12 p^2+V_\theta(q)$$ and a quadratic penalty on $$V_\theta$$ near $$0$$ recovers a constant period because the level sets of $$H_\theta$$ are closed. This is the geometric content of complex characteristic roots, now imposed as an architecture.

### Example 2: Resonance as a learning failure mode

If one trains on a forced oscillator near resonance with a short window, a generic network can memorize the growing amplitude without discovering the mechanism $$y''+\omega^2 y=\cos(\omega t)$$. A structured model that keeps the linear operator and learns only the forcing identifies the resonant match immediately. The chapter’s resonance discussion is therefore a diagnostic, not a relic.

### Example 3: Energy monitor in Python

```python
import numpy as np
from scipy.integrate import solve_ivp

def f(t, z, omega=3.0):
    q, p = z
    return [p, -omega**2 * q]

sol = solve_ivp(f, [0, 20], [1.0, 0.0], rtol=1e-8, atol=1e-8, dense_output=True)
t = np.linspace(0, 20, 400)
q, p = sol.sol(t)
energy = 0.5 * p**2 + 0.5 * 9.0 * q**2
print(energy.max() - energy.min())
```

A structure-preserving learned model should keep this oscillation of energy comparably small. A generic network usually does not.

## Applications in Science, Engineering, and Modern Contexts

Learned Hamiltonian and Lagrangian models appear in molecular simulation, celestial mechanics, robotics, and power-grid oscillation studies. In each case the engineering question is long-horizon stability: a controller or a surrogate that slowly injects energy is unsafe. RLC identification is the electrical twin of the same idea; a learned circuit model that does not respect passivity will predict nonphysical gain. The 2022–2024 literature also feeds into scientific ML more broadly: once a second-order inductive bias is available, it can be combined with PINNs or neural operators so that a continuum model inherits conservation from the architecture rather than from a soft penalty alone.

## Challenges and Extensions

Coordinate choice remains delicate. Hamiltonian structure is not invariant under arbitrary reparameterizations of $$q$$, and a poor choice of generalized coordinates can erase the benefit of the prior. Dissipation, contact, and hybrid switching (impacts, diodes) leave the smooth Hamiltonian category. Identifiability is another issue: many Hamiltonians generate similar short trajectories, just as many characteristic polynomials can fit a short oscillatory record. Finally, symplectic integration of a badly learned $$H_\theta$$ will faithfully preserve the wrong energy.

A reflective prompt: if a learned model conserves a quantity that is not the physical energy, have we succeeded or failed? The Wronskian suggests an answer: structural invariants are valuable only when they correspond to the linear independence or conservation laws of the true system.

## Exercises

1. **Energy identity.** For $$y''+\gamma y'+\omega^2 y=0$$, multiply by $$y'$$ and derive the energy-dissipation law. How would you turn that identity into a training constraint?

2. **Learned characteristic polynomial.** Suppose a linear second-order network produces two complex modes $$e^{\alpha t}\cos\beta t$$ and $$e^{\alpha t}\sin\beta t$$. Recover $$a$$ and $$b$$ in $$y''+a y'+b y=0$$ and discuss uniqueness.

3. **Wronskian diagnostic.** Generate two learned solutions from nearby initial data and compute a discrete Wronskian. What would a vanishing Wronskian tell you about the learned solution space?

4. **Computational experiment.** Fit both an unstructured neural ODE and a Hamiltonian network to samples of $$y''+9y=0$$ on $$[0,4]$$, then extrapolate to $$[0,40]$$. Compare amplitude drift.

5. **Open exploration.** Read Gruver et al. (ICLR 2022) and write a short critique: when should this chapter’s linear theory be hard-wired into a network, and when should it be used only as a diagnostic?

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*, Chapters 3–4; Ross, *Differential Equations*, on mechanical and electrical oscillators.
- Greydanus, S., Dzamba, M., and Yosinski, J. “Hamiltonian neural networks.” *NeurIPS* 2019. [arXiv:1906.01563](https://arxiv.org/abs/1906.01563).
- Cranmer, M., Greydanus, S., Hoyer, S., Battaglia, P., Spergel, D., and Ho, S. “Lagrangian neural networks.” 2020. [arXiv:2003.04630](https://arxiv.org/abs/2003.04630).
- Gruver, N., Finzi, M., Goldblum, M., and Wilson, A. G. “Deconstructing the inductive biases of Hamiltonian neural networks.” *ICLR* 2022. [arXiv:2202.04836](https://arxiv.org/abs/2202.04836).
- Zhong, Y. D., Dey, B., and Chakraborty, A. “Symplectic ODE-Net: learning Hamiltonian dynamics with control.” *ICLR* 2020. [arXiv:1909.12077](https://arxiv.org/abs/1909.12077).
