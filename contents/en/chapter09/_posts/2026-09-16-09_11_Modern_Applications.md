---
layout: post
title: "09-11 Modern Applications: Neural Solvers for Diffusion and Score-Based Models"
chapter: '09'
order: 11
owner: Course Team
lang: en
categories:
- chapter09
lesson_type: optional
---

## Objectives

This optional lesson connects the heat equation, the Gaussian kernel, and maximum principles to two 2021–2024 developments: physics-informed and operator-learning solvers for diffusion, and score-based generative models whose forward process is a diffusion SDE. Students should be able to recognize the heat kernel inside both stories and explain why a maximum principle is a unit test for a learned temperature field. The derivation and Fourier analysis of the heat equation remain the official theory.

## Prerequisites

Students should know the derivation of the heat equation, separation of variables, the fundamental solution on the line, and the maximum principle. The optional numerical-methods lesson in this chapter is helpful but not required.

## Introduction

The heat equation $$u_t=\alpha^2 u_{xx}$$ is the continuum model of smoothing. Its kernel is a Gaussian that becomes wider as time grows, and its maximum principle forbids interior hot spots that were not already present on the parabolic boundary. Those two facts are now infrastructure for machine learning.

On the scientific-ML side, PINNs, DeepONets, and Fourier neural operators are trained as diffusion solvers and as parametric surrogates for heat conduction, porous-media flow, and related parabolic problems. Hao et al. (*PINNacle*, NeurIPS 2024) include heat-conduction tasks among their twenty-plus PDE benchmarks. Li et al. (PINO, [arXiv:2111.03794](https://arxiv.org/abs/2111.03794); later journal versions) combine operator learning with a physics residual so that a coarse data set can be refined by the heat operator itself.

On the generative-model side, Song, Sohl-Dickstein, Kingma, Kumar, Ermon, and Poole (*Score-Based Generative Modeling through Stochastic Differential Equations*, ICLR 2021; [arXiv:2011.13456](https://arxiv.org/abs/2011.13456)) take a data distribution, evolve it by a diffusion SDE whose law satisfies a Fokker–Planck equation, and reverse the SDE to sample. The forward process is a heat flow on densities. Understanding the kernel and the maximum principle is therefore not an analogy; it is the reason the reverse process can be well-posed after one learns the score $$\nabla\log p_t$$.

## Key Concepts

### Learned solvers for the heat equation

A PINN for $$u_t-\alpha^2 u_{xx}=0$$ collates residual points in space-time. An operator model instead learns the map from initial data $$u(\cdot,0)$$, or from a conductivity field, to $$u(\cdot,T)$$. The second object is closer to the heat kernel: it is an approximate Green’s operator. Super-resolution tests, in which one evaluates the model on a finer grid than the one used for training, are meaningful only because the true heat operator is a map between function spaces, not a map between pixel grids.

### The kernel as a Gaussian convolution

On the line,

$$
u(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}\int_{\mathbb{R}}\exp\Bigl(-\frac{(x-y)^2}{4\alpha^2 t}\Bigr)u_0(y)\,dy.
$$

Score-based models use a closely related convolution to turn a complicated data law into an almost Gaussian law. The reverse SDE then denoises. Students who have already computed this kernel by Fourier transforms are looking at the same Gaussian, now used as a generator of samples rather than as a temperature formula.

### Maximum principles as diagnostics

A learned temperature that exceeds the initial and boundary maxima is not a slightly inaccurate solver; it is a solver that has left the theorem. PINNacle-style benchmarks should therefore report constraint violations as well as $$L^2$$ errors. The same diagnostic applies to a generative diffusion: a reverse process that concentrates mass more sharply than the estimated score allows is violating the Fokker–Planck structure.

### Causality in time

Wang, Sankaran, and Perdikaris (CMAME 2024) showed that PINNs which treat time as just another collocation coordinate can violate parabolic causality and fail on chaotic or turbulent evolutions. For the heat equation the same issue is milder but real: residual points at late time should not be allowed to “explain away” an inconsistent early-time field. Marching in time, or weighting residuals by a causal factor, restores the structure that the fundamental solution already encodes.

## Methods and Solution Techniques

Three complementary methods now sit beside separation of variables.

- **PINNs / causal PINNs.** Good for inverse conductivity identification and for irregular geometry; fragile on long horizons and on thin thermal layers.
- **Neural operators (FNO, DeepONet, PINO).** Good for families of initial data or coefficients; should be checked at new resolutions and against the kernel on the line.
- **Score-based / diffusion models.** Good for sampling from high-dimensional data laws; the link to this chapter is the Fokker–Planck / heat structure, not a claim that they replace PDE solvers.

Finite-difference schemes from the optional numerical lesson remain the reference solutions that train and test the first two methods.

## Examples

### Example 1: Kernel check on the line

If an operator model is trained on compactly supported initial data on a large interval, its response to an approximate delta should be close to a Gaussian of variance $$2\alpha^2 T$$. Measuring that variance is a heat-kernel exam question.

### Example 2: Maximum-principle failure

Train a small PINN on $$u_t=u_{xx}$$ with $$u(0,t)=u(1,t)=0$$ and $$u(x,0)=x(1-x)$$, then inspect $$\max u_\theta$$. If the maximum exceeds $$1/4$$, the model has violated the theorem and no $$L^2$$ table can excuse it.

### Example 3: Discrete heat step and a score step

```python
import numpy as np

u = np.array([0.0, 0.2, 0.8, 0.2, 0.0])
# one explicit heat step with r = 0.25
u_next = u.copy()
u_next[1:-1] = u[1:-1] + 0.25 * (u[2:] - 2 * u[1:-1] + u[:-2])
print(u_next)
```

A variance-exploding diffusion sampler uses a similar local averaging, then adds noise. The deterministic part is the heat equation; the noise is the stochastic chapter’s concern.

## Applications in Science, Engineering, and Modern Contexts

Learned heat solvers appear in thermal design, battery modeling, and medical heat-source identification. Operator-learning weather models treat atmospheric diffusion and mixing as part of a larger Fourier surrogate. Score-based models have become a default generator in vision and, increasingly, a prior for inverse problems in medical imaging (Song et al., ICLR 2022; Chung et al., *Diffusion Posterior Sampling*, ICLR 2023). In all of these settings the chapter’s kernel and maximum principle are the cheapest correctness tests one has.

Biology and finance, already mentioned in the optional diffusion-applications lesson, now have a second computational layer: instead of solving one Black–Scholes or Fisher equation, one may learn a family of such maps, or sample from a diffusion that was trained on historical trajectories. The mathematics of smoothing does not change.

## Challenges and Extensions

Long-time diffusion on fine grids is expensive to simulate for training data, so operator models can inherit a biased empirical measure. PINNs struggle with multi-scale conductivity. Generative diffusions require many function evaluations and careful score matching; their Fokker–Planck equation is high-dimensional and not a substitute for a well-posed PDE solve. Anisotropic and degenerate diffusions break the simple Gaussian picture. Finally, a model can match marginals at time $$T$$ and still have the wrong intermediate kernels.

What does it mean physically if a learned heat solver violates the maximum principle but wins a benchmark? It means the benchmark is measuring the wrong quantity.

## Exercises

1. **Variance of the kernel.** From the fundamental solution, show that a delta mass at the origin has variance $$2\alpha^2 t$$ at time $$t$$. How would you estimate $$\alpha$$ from a learned Green’s function?

2. **Maximum principle as a loss.** Propose a hinge penalty that charges a PINN whenever $$u_\theta$$ exceeds the boundary maximum. What theorem guarantees that the true solution pays nothing?

3. **Forward SDE and heat.** For the SDE $$dX=\sigma\,dW$$, write the Fokker–Planck equation for the density and identify it with the heat equation. What is $$\alpha$$ in terms of $$\sigma$$?

4. **Computational experiment.** Implement an explicit heat scheme and a tiny operator model (even a linear map on grid values) that learns one time step. Compare their kernels by applying both to a discrete delta.

5. **Open exploration.** Read Song et al. (ICLR 2021) and one PINNacle heat task (2024). Write a page explaining which of the two uses of diffusion—solving $$u_t=\alpha^2\Delta u$$, or sampling by noising and denoising—is closer to the fundamental solution of this chapter.

## References

- Evans, L. C. *Partial Differential Equations*, Chapter 2; Haberman, Chapters 1–2.
- Hao, Z., et al. “PINNacle: a comprehensive benchmark of physics-informed neural networks for solving PDEs.” *NeurIPS* 2024 Datasets and Benchmarks. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
- Li, Z., et al. “Physics-informed neural operator for learning partial differential equations.” [arXiv:2111.03794](https://arxiv.org/abs/2111.03794) (2021).
- Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., and Poole, B. “Score-based generative modeling through stochastic differential equations.” *ICLR* 2021. [arXiv:2011.13456](https://arxiv.org/abs/2011.13456).
- Wang, S., Sankaran, S., and Perdikaris, P. “Respecting causality for training physics-informed neural networks.” *CMAME* 421 (2024): 116813.
- Chung, H., Kim, J., Mccann, M. T., Klasky, M. L., and Ye, J. C. “Diffusion posterior sampling for general noisy inverse problems.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
