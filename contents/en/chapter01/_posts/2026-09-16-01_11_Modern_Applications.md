---
layout: post
title: "01-11 Modern Applications: Neural ODEs and Continuous-Depth Networks"
chapter: '01'
order: 11
owner: Course Team
lang: en
categories:
- chapter01
lesson_type: optional
---

## Objectives

This optional lesson shows how the first-order initial-value problem studied throughout the chapter reappeared, after 2018 and especially in the 2022–2026 literature, as a model for continuous-depth neural networks. Students should be able to write a neural ODE, explain why existence and uniqueness still govern the architecture, relate residual networks to Euler steps, and locate the main software implementations. The classical theory is left unchanged; the new material is an application layer.

## Prerequisites

Students should know separable and linear first-order equations, integrating factors, and the Picard–Lindelöf theorem. Familiarity with the idea of a parameterized vector field $$f(t,y;\theta)$$ is enough; no specialized machine-learning background is assumed.

## Introduction

A first-order equation $$y'=f(t,y)$$ is a rule that turns a present state into an instantaneous velocity. Deep residual networks do something remarkably similar: each layer updates a hidden state by adding a learned increment. Chen, Rubanova, Bettencourt, and Duvenaud made the analogy precise in *Neural Ordinary Differential Equations* (NeurIPS 2018) by replacing the discrete stack of layers with a genuine ODE

$$
\frac{dh}{dt}=f_\theta\bigl(t,h(t)\bigr),\qquad h(t_0)=x,
$$

and computing gradients by the adjoint method. The subsequent literature, surveyed in Kidger’s 2022 thesis ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)), treats residual nets, neural ODEs, neural controlled DEs, and neural SDEs as one family of continuous-depth models.

Why should a student of first-order equations care? Because every qualitative fact already proved in this chapter becomes a design constraint. If $$f_\theta$$ fails to be Lipschitz, uniqueness can fail and two identical inputs can produce different hidden states. If $$f_\theta$$ is stiff, an explicit solver wastes steps. If the data arrive at irregular times, a continuous trajectory is more natural than a fixed discrete grid. The same existence theory that makes population and mixing models trustworthy now decides whether a continuous-depth network is a well-posed map from input to output.

## Key Concepts

### Residual networks as Euler discretizations

A residual block $$h_{n+1}=h_n+\Delta t\,f_\theta(h_n)$$ is forward Euler for $$h'=f_\theta(h)$$. Taking the continuum limit is therefore not a metaphor: it is the same limiting process that turns difference quotients into derivatives. Augmented neural ODEs (Dupont, Doucet, and Teh, NeurIPS 2019) add extra dimensions so that trajectories can uncross, restoring expressivity that a purely first-order flow on the original space cannot have. The underlying reason is topological and already visible in the phase-line discussion of autonomous scalar equations: flows in one dimension cannot pass through each other.

### The adjoint method

Training requires $$\nabla_\theta\mathcal{L}$$ for a loss that depends on the terminal state $$h(T)$$. Differentiating through every solver step stores the whole trajectory. The adjoint method instead integrates

$$
\frac{da}{dt}=-a^\top D_h f_\theta(t,h),\qquad a(T)=\nabla_{h(T)}\mathcal{L}
$$

backwards and accumulates the parameter gradient along that reverse trajectory. The construction is the same sensitivity equation that appears when one differentiates an IVP with respect to a parameter, now used at the scale of a deep network. Kidger (2022) and the `torchdiffeq` documentation ([https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq)) emphasize that the adjoint is only as accurate as the forward and reverse solvers; inconsistent tolerances produce inconsistent gradients.

### Neural controlled differential equations

When the input is itself a path $$X(t)$$, as in irregular time series, Kidger, Morrill, Foster, and Lyons (*Neural Controlled Differential Equations*, ICLR 2021) replace the ODE by a controlled equation

$$
dh(t)=f_\theta\bigl(h(t)\bigr)\,dX(t).
$$

The first-order theory still applies after one rewrites the system as an ordinary equation driven by the increments of $$X$$. The advantage is that observations need not sit on a uniform grid, a fact that first-order modeling of mixing tanks and population counts already suggested: the continuous law is primary, the sampling grid is secondary.

### Software and the 2022–2026 stack

Two libraries dominate current practice. `torchdiffeq` implements adaptive ODE solvers and adjoints in PyTorch. Diffrax (Kidger, 2021–2022; [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/)) does the same in JAX, with a uniform interface for ODEs, CDEs, and SDEs. Both treat the solver as a differentiable primitive, so the first-order equation is no longer only a homework object: it is a layer.

## Methods and Solution Techniques

The practical workflow is a direct descendant of the IVP pipeline in this chapter.

1. Choose a vector field architecture $$f_\theta$$ (a small multilayer perceptron is typical).
2. Choose a solver whose stability region matches the problem: explicit Runge–Kutta for nonstiff dynamics, implicit or semi-implicit methods when the learned field is stiff.
3. Integrate from the input $$x$$ to a terminal time $$T$$, or to each observation time $$t_i$$.
4. Form a loss on the observed states and backpropagate, either by unrolling or by the adjoint.
5. Validate not only the loss but also qualitative first-order diagnostics: boundedness, comparison with a linearized field, and sensitivity to $$T$$.

Separation of variables and integrating factors remain useful as checks. If the learned field is close to linear, $$h'=Ah+b$$, the exact solution $$e^{At}$$ is an independent reference. If the field is autonomous and scalar, the phase line predicts the equilibria that the network is allowed to possess.

## Examples

### Example 1: Continuous depth for an irregular time series

Suppose observations $$y(t_i)$$ arrive at times $$0=t_0<t_1<\cdots<t_n$$ that are not equally spaced. A discrete network must invent a missing-value rule. A neural ODE simply evaluates the same trajectory at the given times. This is exactly how one treats a mixing-tank model whose measurements are taken whenever a technician happens to sample the tank.

### Example 2: Lipschitz failure as a training pathology

If $$f_\theta$$ uses an unbounded activation and large weights, the local Lipschitz constant can explode. Solvers then take tiny steps or fail, and uniqueness on the training interval becomes doubtful. Weight decay, spectral normalization, or a tanh final layer are therefore not merely regularization tricks; they are attempts to stay inside the Picard–Lindelöf hypothesis.

### Example 3: A minimal `torchdiffeq` sketch

```python
import torch
from torchdiffeq import odeint

class Field(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(2, 16), torch.nn.Tanh(), torch.nn.Linear(16, 2)
        )

    def forward(self, t, y):
        return self.net(y)

y0 = torch.tensor([1.0, 0.0])
t = torch.linspace(0.0, 2.0, 21)
with torch.no_grad():
    yt = odeint(Field(), y0, t)
print(yt.shape)  # (21, 2)
```

The output is a discrete sample of a continuous first-order trajectory. Replacing `Field` by $$f(t,y)=-y$$ recovers the exact exponential decay already solved by separation of variables.

## Applications in Science, Engineering, and Modern Contexts

Continuous-depth models are used for irregular medical time series, latent dynamics in neuroscience, residual architectures in computer vision, and hybrid physics–ML closures in which a known first-order law is kept and only a missing term is learned. In control and pharmacokinetics they provide a natural state-space form: the hidden state is the compartment vector, the vector field is partly mechanistic and partly learned. In all of these settings the chapter’s existence theory is the first sanity check. A model that cannot guarantee a unique solution from a given initial state is not yet a model; it is a family of possible futures.

Kidger (2022) and the SciML stack around Diffrax and `torchdiffeq` also changed the software culture of the field: solvers are no longer hidden inside a black-box integrator, but are first-class, differentiable layers. That cultural change is why a first-order course now has a direct path into contemporary machine learning.

## Challenges and Extensions

Neural ODEs can be slower to train than discrete residual nets, especially when the learned field is stiff. Reverse-mode adjoints may drift from the true gradient if tolerances are loose. Expressivity on the original space is limited by the fact that flows are invertible and cannot cross; augmentation, extra latent dimensions, or controlled equations are the usual remedies. There is also a philosophical caution: a successful fit does not identify a unique vector field. Many first-order right-hand sides can share the same sampled trajectory, just as many mixing models can share the same concentration measurements.

A good question to carry forward is: which properties of $$f$$ (Lipschitz constant, one-sided Lipschitz, monotonicity) should be constrained during learning if we want the same comparison theorems that make first-order scalar equations so transparent?

## Exercises

1. **From residual blocks to ODEs.** Write the residual update $$h_{n+1}=h_n+h\,f(h_n)$$ and take $$h\to 0$$. Recover $$h'=f(h)$$ and state the precise meaning of the limit on a finite interval.

2. **Picard iteration as training intuition.** For $$y'=\theta y$$, $$y(0)=1$$, write the first two Picard iterates. How does this iteration differ from a gradient step on $$\theta$$ for the loss $$\lvert y(1)-e\rvert^2$$?

3. **Adjoint for a linear scalar ODE.** Let $$y'=\theta y$$, $$y(0)=1$$, and $$\mathcal{L}=\tfrac12 y(T)^2$$. Compute $$\partial\mathcal{L}/\partial\theta$$ two ways: by differentiating the closed form, and by solving the adjoint equation. Confirm that they agree.

4. **Computational experiment.** Using `torchdiffeq` or Diffrax, fit a neural ODE to samples of the logistic equation $$y'=y(1-y)$$. Compare the learned field along the phase line with the exact autonomous right-hand side. Does the network recover the equilibria at $$0$$ and $$1$$?

5. **Open exploration.** Read Section 1 of Kidger (2022) and explain, in one page, why irregular time series make a continuous first-order model more natural than a fixed discrete architecture.

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*. Chapters 1–2; Zill, *Differential Equations with Boundary-Value Problems*, Chapters 1–2.
- Chen, R. T. Q., Rubanova, Y., Bettencourt, J., and Duvenaud, D. “Neural ordinary differential equations.” *NeurIPS* 2018. [arXiv:1806.07366](https://arxiv.org/abs/1806.07366).
- Kidger, P. *On Neural Differential Equations*. University of Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
- Kidger, P., Morrill, J., Foster, J., and Lyons, T. “Neural controlled differential equations for irregular time series.” *ICLR* 2021. [arXiv:2005.08926](https://arxiv.org/abs/2005.08926).
- Chen, R. T. Q., et al. `torchdiffeq` documentation. [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq). Kidger, P. Diffrax documentation. [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
