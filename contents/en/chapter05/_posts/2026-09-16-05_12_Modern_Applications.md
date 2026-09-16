---
layout: post
title: "05-12 Modern Applications: Neural Lyapunov Functions and Learned Certificates"
chapter: '05'
order: 12
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: optional
---

## Objectives

This optional lesson carries Lyapunov stability, linearization, and phase-plane reasoning into the 2019–2023 literature on neural certificates. Students should be able to state what a learned Lyapunov function is expected to prove, distinguish empirical decrease from a verified decrease, and locate the main survey and NeurIPS results on neural Lyapunov and barrier methods. The classical stability theorems of the chapter remain the standard of truth.

## Prerequisites

Students should know autonomous systems, Jacobian linearization, the Lyapunov function test, and the elementary bifurcations. Limit cycles and SIR models are helpful running examples but are not required for the main argument.

## Introduction

A Lyapunov function is a scalar energy-like certificate: if $$V$$ is positive definite and $$\dot V\le 0$$ along the flow, the equilibrium is stable. Finding such a $$V$$ by hand is an art. The modern idea is to parameterize $$V_\theta$$ by a neural network and train it, often jointly with a controller $$u_\theta$$, so that the Lyapunov inequalities become a loss. Chang, Roohi, and Gao (*Neural Lyapunov Control*, NeurIPS 2019) gave an early and influential template. Dawson, Gao, and Fan then surveyed the broader landscape of neural Lyapunov, barrier, and contraction certificates in *IEEE Transactions on Robotics* 39 (2023): 1749–1767 ([https://doi.org/10.1109/TRO.2022.3232542](https://doi.org/10.1109/TRO.2022.3232542); [arXiv:2202.11762](https://arxiv.org/abs/2202.11762)).

Wu, Clark, Kantaros, and Vorobeychik (*Neural Lyapunov Control for Discrete-Time Systems*, NeurIPS 2023; [arXiv:2305.06547](https://arxiv.org/abs/2305.06547)) extended the idea to discrete time with mixed-integer verification, producing provably stable controllers on standard nonlinear benchmarks. The conceptual message for this chapter is sharp: a neural network does not relax Lyapunov’s theorem. It searches for a function that the theorem can accept.

## Key Concepts

### Certificates versus predictors

A trajectory predictor answers “where does the state go?”. A certificate answers “why may we believe it stays in a safe set?”. The second question is the Lyapunov question. A learned $$V_\theta$$ is useful only if one can check

$$
V_\theta(0)=0,\qquad V_\theta(x)>0\ \text{for }x\neq 0,\qquad \nabla V_\theta(x)\cdot f\bigl(x,u_\theta(x)\bigr)<0
$$

on a region of interest, not merely on the training samples. Dawson et al. (2023) emphasize that the field’s progress is precisely the move from sampled decrease to verified decrease.

### Neural Lyapunov, barrier, and contraction

A barrier certificate keeps trajectories out of a bad set; a contraction metric makes nearby trajectories approach one another. Both are close relatives of Lyapunov functions and of the phase-plane intuition already developed here. Linearization remains the local test: if the Jacobian at equilibrium has an eigenvalue with positive real part, no smooth Lyapunov function can prove stability, no matter how expressive the network is. Training will then either fail or produce a $$V_\theta$$ whose decrease is fictitious.

### Verification as a closed loop

Modern methods alternate learning and verification. The network proposes $$V_\theta$$; a satisfiability or mixed-integer solver searches for a counterexample $$x$$ where $$\dot V_\theta(x)\ge 0$$; that point is added to the training set. Wu et al. (NeurIPS 2023) make this loop efficient in discrete time. The loop is the computational analogue of the usual homework check: after you invent $$V$$, you must still compute $$\dot V$$ and sign it.

### Bifurcations and fragile certificates

If a parameter crosses a Hopf value, a stable equilibrium becomes an unstable focus surrounded by a limit cycle. A certificate trained on one side of the bifurcation cannot be reused blindly on the other. This is a modern reason to keep the chapter’s bifurcation diagrams: they tell you when a learned $$V_\theta$$ is allowed to exist.

## Methods and Solution Techniques

A responsible pipeline has four steps.

1. Identify the closed-loop field $$f(x,u_\theta(x))$$, including any saturation or safety filter.
2. Train $$V_\theta$$ (and possibly $$u_\theta$$) with a loss that rewards positivity and decrease on a sampled region.
3. Verify the decrease condition with an exact or conservative checker, not only with more samples.
4. Report the verified sublevel set $$\bigl\{x:V_\theta(x)\le c\bigr\}$$ as the region of attraction or safe set.

Phase portraits remain the first visualization. A learned $$V_\theta$$ whose sublevel sets cut across a saddle’s stable manifold is claiming a region the linearized theory forbids. Plotting $$\dot V_\theta$$ as a heat map is the neural analogue of checking the sign of $$V'$$ along a phase line.

## Examples

### Example 1: The damped pendulum

For $$\theta''+\sin\theta+\gamma\theta'=0$$ the energy $$V=\tfrac12(\theta')^2+(1-\cos\theta)$$ is a classical Lyapunov function, but it does not prove exponential decay by itself. A neural $$V_\theta$$ can add a cross term and enlarge the verified region of attraction, which is exactly the experiment reported in several neural-Lyapunov papers. The student should first plot the conservative energy, then ask what extra terms a network is allowed to add without destroying positive-definiteness.

### Example 2: A false certificate from samples

Suppose one samples only a neighborhood of a spiral sink and trains $$V_\theta=\|x\|^2$$. The sampled $$\dot V$$ may be negative while a distant unstable node, or a limit cycle, remains unseen. Verification on a box large enough to include those structures will fail. The example is the chapter’s warning about local versus global stability, now in software form.

### Example 3: Decrease residual in code

```python
import torch

def V(x):
    return (x**2).sum(dim=-1)

def f(x, gamma=0.3):
    # damped linear oscillator in first-order form
    q, p = x[..., 0], x[..., 1]
    return torch.stack([p, -q - gamma * p], dim=-1)

x = torch.randn(1000, 2)
x.requires_grad_(True)
Vx = V(x)
gradV = torch.autograd.grad(Vx.sum(), x)[0]
Vdot = (gradV * f(x)).sum(dim=-1)
print(float((Vdot < 0).float().mean()))
```

A value near $$1$$ on random samples is encouraging and still not a proof. That is the whole pedagogical point.

## Applications in Science, Engineering, and Modern Contexts

Learned certificates are now part of the robotics and control toolkit: quadrotor stabilization, vehicle path tracking, and safe reinforcement learning all need a reason to believe that a neural policy will not leave a safe set. Epidemiology provides a different audience. A learned Lyapunov function for an SIR-type model can certify that a disease-free equilibrium is asymptotically stable when $$R_0<1$$, or fail in a way that reveals a mistake in the learned incidence term. In scientific ML more broadly, a PINN that claims a stable steady state can be asked to produce a certificate, not only a small residual.

Dawson et al. (2023) collect these application domains and also the main failure modes: incomplete verification, overly small regions of attraction, and certificates that ignore actuation limits. Those are not new mathematical pathologies. They are the classical distinction between local linearization, regional Lyapunov arguments, and global phase portraits.

## Challenges and Extensions

Verification scales poorly with dimension; mixed-integer encodings of neural networks become expensive beyond modest state dimension. Discrete-time and continuous-time certificates are not interchangeable without a careful sampling argument. Stochastic and hybrid systems need supermartingale or multiple-Lyapunov extensions. Finally, a controller that is certified on a model is not thereby certified on the plant: model error can destroy $$\dot V<0$$.

A reflective question: if a neural certificate is verified on a compact set, what does it say about trajectories that start outside that set? The phase plane already answers: nothing, except that they may enter the set or escape to another attractor.

## Exercises

1. **Linear obstruction.** Let $$x'=Ax$$ with $$A$$ having an eigenvalue of positive real part. Prove that no $$C^1$$ Lyapunov function can satisfy $$\dot V<0$$ on a neighborhood of the origin. What, then, should a training algorithm do?

2. **From energy to a strict Lyapunov function.** For the damped pendulum, start from the mechanical energy and add a small cross term $$\varepsilon\theta\theta'$$. For which $$\varepsilon$$ is $$V$$ still positive definite near $$0$$, and for which is $$\dot V$$ strictly negative?

3. **Barrier versus Lyapunov.** Write a barrier condition that keeps $$x_1\ge 0$$ for a simple planar system. How does the condition differ from $$\dot V<0$$?

4. **Computational experiment.** Train a small network $$V_\theta$$ for $$x'=-x$$, $$y'=-2y$$ on the unit disk and then evaluate $$\dot V_\theta$$ on a grid. Identify any grid cells where the decrease fails, and discuss how a verifier would use those cells.

5. **Open exploration.** Read Dawson, Gao, and Fan (IEEE TRO 2023) and summarize, in one page, the difference between a sampled certificate and a verified certificate. Then glance at Wu et al. (NeurIPS 2023) and note what becomes easier in discrete time.

## References

- Strogatz, S. H. *Nonlinear Dynamics and Chaos*; Arnold, *Ordinary Differential Equations*, for the geometric stability picture.
- Chang, Y.-C., Roohi, N., and Gao, S. “Neural Lyapunov control.” *NeurIPS* 2019. [arXiv:2005.00611](https://arxiv.org/abs/2005.00611).
- Dawson, C., Gao, S., and Fan, C. “Safe control with learned certificates: a survey of neural Lyapunov, barrier, and contraction methods for robotics and control.” *IEEE Transactions on Robotics* 39, no. 3 (2023): 1749–1767. [https://doi.org/10.1109/TRO.2022.3232542](https://doi.org/10.1109/TRO.2022.3232542).
- Wu, J., Clark, A., Kantaros, Y., and Vorobeychik, Y. “Neural Lyapunov control for discrete-time systems.” *NeurIPS* 2023. [arXiv:2305.06547](https://arxiv.org/abs/2305.06547).
