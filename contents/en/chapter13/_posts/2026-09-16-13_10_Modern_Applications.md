---
layout: post
title: "13-10 Modern Applications: Differentiable Solvers and Neural SDEs"
chapter: '13'
order: 10
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: optional
---

## Objectives

This optional lesson treats Euler, Runge–Kutta, stiffness, CFL, and Euler–Maruyama as the numerical backbone of differentiable scientific computing. Students should be able to explain reverse-mode differentiation through a solver, locate `torchdiffeq` and Diffrax, and connect neural SDEs to the score-based diffusion models that dominated generative modeling in 2021–2024. The classical consistency and stability theory of the chapter is not replaced.

## Prerequisites

Students should know forward and backward Euler, RK4, linear stability regions, CFL, and the Euler–Maruyama scheme for SDEs. The preparatory review on discretization error is the right warm-up.

## Introduction

A numerical method is a map from a vector field and a step size to a discrete trajectory. If that map is differentiable, it can sit inside a learning loop: parameters of the field, of a controller, or of a closure can be trained by gradient descent. Chen et al. (NeurIPS 2018) popularized the adjoint method for neural ODEs. Kidger’s 2022 thesis ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) and the Diffrax library ([https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/)) turned the entire catalog of this chapter—explicit and implicit ODE solvers, CDEs, SDEs, adaptive stepping—into JAX primitives. `torchdiffeq` ([https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq)) did the same in PyTorch.

On the stochastic side, Kidger, Foster, Li, and Lyons (*Neural SDEs as Infinite-Dimensional GANs*, ICML 2021; *Efficient and Accurate Gradients for Neural SDEs*, NeurIPS 2021) showed how to backpropagate through SDE solvers. Song et al. (ICLR 2021) used diffusion SDEs as generative models. The numerical questions are the ones already studied here: strong versus weak error, stiffness, and the stability of Euler–Maruyama.

## Key Concepts

### Differentiating a one-step map

Forward Euler $$y_{n+1}=y_n+h f_\theta(y_n)$$ has Jacobian $$I+h Df_\theta(y_n)$$. Reverse-mode autodiff multiplies these Jacobians backwards, which is discrete adjoint propagation. Implicit Euler requires a linear solve at each step; the implicit-function theorem supplies the Jacobian. Stiff problems demand that implicit, not explicit, adjoints be used, for the same reason they demand implicit primal solves.

### Continuous adjoints and checkpointing

The continuous adjoint of Chen et al. integrates an extra ODE backwards and saves memory, at the cost of a new discretization error. Diffrax exposes both discretize-then-optimize and optimize-then-discretize options, which is the 2022-era way of saying: choose whether the gradient is the exact gradient of the numerical method or an approximation to the gradient of the continuum problem. Those are different objects, and the chapter’s local-error analysis applies to both.

### Neural SDEs and score SDEs

A neural SDE

$$
dX_t = b_\theta(t,X_t)\,dt + \sigma_\theta(t,X_t)\,dW_t
$$

is a learned Itô process. Training it requires a stochastic adjoint and a consistent Brownian path on the backward pass (Kidger et al., NeurIPS 2021). Score-based generative models use a prescribed forward SDE and learn only the score that defines the reverse drift. Euler–Maruyama is the default sampler; higher-order SDE schemes and predictor–corrector methods are the 2021–2024 refinements. The stability region of the scheme still decides whether a large reverse step explodes.

### CFL and learned PDE steppers

Learned time-steppers for PDEs can violate CFL even if each snapshot looks smooth. Brandstetter, Worrall, and Welling (*Message Passing Neural PDE Solvers*, ICLR 2022; [arXiv:2202.03376](https://arxiv.org/abs/2202.03376)) and the PDEBench suite (Takamoto et al., NeurIPS 2022; [arXiv:2210.07182](https://arxiv.org/abs/2210.07182)) made this empirical. A roll-out that is stable for ten steps and blows up at one hundred is the classical stability story, now with a neural flux.

## Methods and Solution Techniques

A differentiable-solver workflow:

1. Choose a primal scheme whose stability region contains the expected spectrum (explicit RK for nonstiff ODEs, implicit or exponential methods for stiff ODEs, CFL-respecting schemes for hyperbolic PDEs, Euler–Maruyama or better for SDEs).
2. Decide between exact autodiff of the discrete scheme and a continuous adjoint.
3. Set tolerances so that the gradient is not dominated by solver noise.
4. For SDEs, store or reconstruct the same Brownian increments on the backward pass.
5. Validate with manufactured solutions, linear stability tests, and long roll-outs.

Software documentation is part of the method. Diffrax’s solver API and `torchdiffeq`’s `odeint_adjoint` are the references students should open before inventing a new backprop rule.

## Examples

### Example 1: Implicit Euler adjoint

For $$y'=-\lambda y$$, implicit Euler is $$y_{n+1}=y_n/(1+h\lambda)$$. Differentiating in $$\lambda$$ is elementary and should match autodiff. Explicit Euler’s gradient, by contrast, is taken through an unstable primal when $$h\lambda$$ is large, and is therefore meaningless.

### Example 2: Euler–Maruyama strong error

The scheme $$X_{n+1}=X_n+h b(X_n)+\sqrt{h}\,\sigma(X_n)\xi_n$$ has strong order $$1/2$$ in general. A neural SDE trained with a pathwise loss cannot beat that order unless the scheme is upgraded. Weak (distributional) losses can use weaker schemes, which is why generative-model samplers often care about weak error.

### Example 3: Diffrax-style ODE solve in spirit

```python
import numpy as np
from scipy.integrate import solve_ivp

def f(t, y, theta=0.8):
    return -theta * y

sol = solve_ivp(f, [0, 2], [1.0], rtol=1e-6, atol=1e-6)
print(sol.y[0, -1], np.exp(-0.8 * 2))
```

A differentiable solver replaces `solve_ivp` by an object that also returns $$\partial y(T)/\partial\theta$$. The primal numbers should still match this test.

## Applications in Science, Engineering, and Modern Contexts

Differentiable solvers are now standard in neural ODEs, universal differential equations (Rackauckas et al., 2021, and the SciML stack), system identification, and optimal control. Neural SDEs model irregular financial time series, molecular kinetics, and latent stochastic dynamics. Score-based SDEs generate images, molecules, and, increasingly, candidates for inverse problems in imaging. PDEBench (2022) and later suites such as The Well (Ohana et al., NeurIPS 2024) provide community roll-out tests so that a learned stepper can be compared with the classical methods of this chapter on public tasks.

In engineering, a differentiable CFD or circuit solver lets a designer optimize geometry or parameters with the same adjoint technology that optimal-control theory has used for decades. The new ingredient is that the residual itself may contain a network.

## Challenges and Extensions

Adjoints of long chaotic trajectories are unstable; shadowing and least-squares shadowing are research topics, not solved tools. Implicit solvers make the backward pass expensive. Stochastic adjoints need careful noise reconstruction. Learned PDE steppers overfit short horizons. Mixed discrete–continuous (hybrid) systems break naive autodiff. None of these issues repeals A-stability or CFL; they make those classical notions more valuable.

A question: if the continuous adjoint and the discrete adjoint disagree by $$10\%$$, which one should you trust for the optimization you are actually running? The chapter’s answer is the discrete adjoint, because that is the gradient of the method you deployed.

## Exercises

1. **Stability region and a learned step.** For $$y'=\lambda y$$, write the amplification factor of RK4. For which $$h\lambda$$ is a neural residual stepper allowed to use RK4 as its inner scheme?

2. **Discrete versus continuous adjoint.** For one implicit-Euler step of $$y'=-\theta y$$, compute both the exact gradient of the numerical map and the continuous adjoint evaluated at that step. When do they agree?

3. **Strong versus weak.** Explain why a score-based sampler can tolerate a scheme with poor strong order if the target metric is a distributional distance.

4. **Computational experiment.** Using `torchdiffeq` or a hand-rolled Euler map, fit $$\theta$$ in $$y'=-\theta y$$ to data generated with $$\theta=1$$. Compare training with a discrete adjoint and with a finite-difference gradient.

5. **Open exploration.** Read the Diffrax documentation or Kidger (2022), Chapter on numerics, and write a one-page guide: which solver class from this chapter should a user pick for (a) a nonstiff neural ODE, (b) a stiff chemical closure, (c) a neural SDE?

## References

- Ascher, U. M., and Petzold, L. R. *Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations*; Kloeden, P. E., and Platen, E. *Numerical Solution of Stochastic Differential Equations*.
- Kidger, P. *On Neural Differential Equations*. University of Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435). Diffrax docs: [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
- Kidger, P., Foster, J., Li, X., and Lyons, T. “Efficient and accurate gradients for neural SDEs.” *NeurIPS* 2021. [arXiv:2105.13493](https://arxiv.org/abs/2105.13493).
- Song, Y., et al. “Score-based generative modeling through stochastic differential equations.” *ICLR* 2021. [arXiv:2011.13456](https://arxiv.org/abs/2011.13456).
- Brandstetter, J., Worrall, D., and Welling, M. “Message passing neural PDE solvers.” *ICLR* 2022. [arXiv:2202.03376](https://arxiv.org/abs/2202.03376).
- Takamoto, M., et al. “PDEBench: an extensive benchmark for scientific machine learning.” *NeurIPS* 2022. [arXiv:2210.07182](https://arxiv.org/abs/2210.07182).
- Chen, R. T. Q., et al. `torchdiffeq`. [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq).
