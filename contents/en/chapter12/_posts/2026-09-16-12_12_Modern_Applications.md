---
layout: post
title: "12-12 Modern Applications: Operator Learning in Sobolev Spaces"
chapter: '12'
order: 12
owner: Course Team
lang: en
categories:
- chapter12
lesson_type: optional
---

## Objectives

This optional lesson uses $$L^p$$ spaces, weak derivatives, Sobolev norms, and Lax–Milgram well-posedness as the official language of neural-operator theory. Students should be able to say in which space a learned map is claimed to be continuous, why discretization invariance is a functional-analytic statement, and which 2022–2024 papers supply approximation rates. The weak-formulation theory of the chapter is not rewritten.

## Prerequisites

Students should know $$L^p$$ norms, weak derivatives, the spaces $$H^1$$ and $$H^1_0$$, the Lax–Milgram theorem, and the idea of a weak solution of a linear elliptic PDE.

## Introduction

A neural network on a mesh is a map between finite-dimensional spaces. A neural operator is advertised as a map between function spaces. That advertisement is empty unless one names the spaces. Kovachki et al. (*JMLR* 24(89), 2023) do exactly that: they define neural operators as compositions of affine integral operators and nonlinearities acting on Banach spaces, prove a universal approximation theorem, and insist that the same parameters be usable at many discretizations.

Lanthaler, Mishra, and Karniadakis (*Error estimates for DeepONets*, *Transactions of Mathematics and Its Applications*, 2022) give quantitative rates in terms of trunk and branch sizes, again in infinite-dimensional norms. De Hoop, Kovachki, Nelsen, and Stuart (*Convergence rates for learning linear operators from noisy data*, *SIAM/ASA Journal on Uncertainty Quantification*, 2023; [arXiv:2108.12515](https://arxiv.org/abs/2108.12515)) treat the linear case as a statistical inverse problem on Hilbert spaces. Boullé and Townsend’s 2023 mathematical guide to operator learning organizes these results for analysts.

This chapter is the prerequisite those papers assume. Weak derivatives tell you that a model may converge in $$L^2$$ and still have a meaningless gradient. Lax–Milgram tells you that the true solution operator is bounded from $$H^{-1}$$ to $$H^1_0$$, so a learned operator that is only bounded on nodal $$\ell^2$$ is answering a different question.

## Key Concepts

### Named spaces, named errors

An error of $$10^{-3}$$ is meaningless until one writes $$\|u_\theta-u\|_{L^2}$$, $$\|u_\theta-u\|_{H^1}$$, or a weaker dual norm. Elliptic problems typically need $$H^1$$ because the energy is the $$H^1$$ seminorm. Evolution problems may be content with $$L^2$$ in space, uniformly in time. Operator-learning papers that report only relative $$L^2$$ on a single grid are hiding the functional-analytic claim.

### Discretization invariance

A family of discrete maps $$G_h$$ is a consistent discretization of an operator $$G$$ if, as the mesh size $$h\to 0$$, $$G_h$$ applied to a discretization of $$a$$ converges to a discretization of $$G(a)$$. Neural operators aim to have $$G_h$$ share parameters across $$h$$. That is possible only if the architecture is defined by integral kernels, Fourier multipliers, or other continuum objects, not by a weight matrix whose size equals the number of nodes.

### Weak residuals as physics losses

The weak form $$a(u,v)=\langle f,v\rangle$$ is already a residual. A physics-informed operator loss can penalize

$$
\sup_{\|v\|_{H^1_0}\le 1}\bigl\lvert a(u_\theta,v)-\langle f,v\rangle\bigr\rvert,
$$

which is the $$H^{-1}$$ residual. Collocating a strong Laplacian is a stricter, sometimes less stable, choice. The chapter’s movement from strong to weak solutions is therefore a training decision, not only a theoretical convenience.

### Compactness and rates

Universal approximation on compact sets of a Banach space requires compactness. Training measures supported on a bounded set of $$H^s$$ with $$s$$ large enough to compactly embed into the working space are the usual hidden assumption. If the data are merely in $$L^2$$, no compact embedding saves you, and no finite trunk can be uniformly accurate. That is Sobolev embedding used as a warning label.

## Methods and Solution Techniques

A functional-analytic checklist for reading or building a learned operator:

1. Name the input space (e.g. $$L^\infty$$ of coefficients, $$H^{-1}$$ of sources) and the output space (e.g. $$H^1_0$$).
2. Confirm that the architecture makes sense on those spaces at every resolution.
3. Train with a loss that is equivalent to the norm in which well-posedness holds, or explain the mismatch.
4. Test on a finer mesh and on a more oscillatory family, watching for a compactness failure.
5. For linear problems, compare the learned operator with the Lax–Milgram solution operator on a basis of sources.

## Examples

### Example 1: $$L^2$$ success, $$H^1$$ failure

A network can match a sawtooth in $$L^2$$ while its weak derivative stays far from a square wave. Plotting both norms is the Sobolev lesson in one figure. Any Darcy surrogate should report both.

### Example 2: Lax–Milgram as a generalization bound

If $$a(\cdot,\cdot)$$ is coercive with constant $$\alpha$$, then $$\|u\|_{H^1}\le\alpha^{-1}\|f\|_{H^{-1}}$$. A learned operator whose operator norm on these spaces exceeds $$C/\alpha$$ for a large $$C$$ is not yet a solver; it is an unstable interpolant. Computing an empirical operator norm on the test set is a cheap proxy.

### Example 3: Discrete $$H^1$$ seminorm

```python
import numpy as np

def h1_seminorm(u, dx):
    return np.sqrt(np.sum(np.diff(u)**2 / dx))

x = np.linspace(0, 1, 51)
dx = x[1] - x[0]
print(h1_seminorm(np.sin(2 * np.pi * x), dx), h1_seminorm(np.sin(20 * np.pi * x), dx))
```

The high-frequency sine is much larger in $$H^1$$. A model trained only in $$L^2$$ need not see that difference.

## Applications in Science, Engineering, and Modern Contexts

Once spaces are named, scientific claims become comparable. A weather emulator that is accurate in $$L^2$$ of temperature but wild in $$H^1$$ will have unusable fluxes. A medical-imaging operator that maps boundary data in $$L^2(\partial\Omega)$$ to interiors in $$L^2(\Omega)$$ may be smoothing away the very singularities a clinician needs. Uncertainty quantification for linear operators, as in de Hoop et al. (2023), is the right language for noisy experiments: one learns a posterior on a Hilbert space, not a single mesh vector.

The same viewpoint disciplines PINNs. A small strong residual at collocation points does not imply a small $$H^{-1}$$ residual, and therefore does not imply a small $$H^1$$ error via Lax–Milgram. Students who have proved that theorem already know how to read a PINN table skeptically.

## Challenges and Extensions

Nonlinear operators, time-dependent maps, and measure-valued outputs leave the Hilbert-space comfort zone. Sobolev embeddings fail in high dimension or at critical exponents, which is relevant to very high-dimensional parametric PDEs. Discrete aliasing can destroy a continuum Lipschitz bound. Statistical rates degrade with noise in ways that approximation theory alone does not capture. Finally, a universal-approximation theorem never promises that gradient descent will find the approximating parameters.

A question worth asking of every paper: in which Banach space is the claim stated, and is that space the one in which the PDE is well-posed?

## Exercises

1. **Norm dictionary.** For the Dirichlet Poisson map $$f\mapsto u$$, state continuity $$H^{-1}\to H^1_0$$ and $$L^2\to H^2\cap H^1_0$$ (on a smooth domain). Which one should a neural operator advertise if it only saw noisy $$f$$?

2. **Compactness.** Why does a training set bounded in $$H^2$$ yield a compact set in $$H^1$$ in one dimension? What fails if the bound is only in $$H^1$$?

3. **Weak loss.** Write a Monte Carlo approximation of the $$H^{-1}$$ residual for $$-u''=f$$. Why is a random choice of test functions $$v$$ only a lower bound?

4. **Computational experiment.** Take two grids and a linear interpolant of a fixed $$H^1$$ function. Compute discrete $$L^2$$ and $$H^1$$ errors under refinement. Then replace the interpolant by a pixel-wise neural map that was trained on the coarse grid and observe what happens.

5. **Open exploration.** Read Sections 1–2 of Kovachki et al. (2023) or Lanthaler, Mishra, and Karniadakis (2022) and translate one theorem statement into the notation of this chapter.

## References

- Brezis, H. *Functional Analysis, Sobolev Spaces and Partial Differential Equations*; Adams, R. A., and Fournier, J. J. F. *Sobolev Spaces*.
- Kovachki, N., et al. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, no. 89 (2023): 1–97. [https://jmlr.org/papers/v24/21-1524.html](https://jmlr.org/papers/v24/21-1524.html).
- Lanthaler, S., Mishra, S., and Karniadakis, G. E. “Error estimates for DeepONets: a deep learning framework in infinite dimensions.” *Transactions of Mathematics and Its Applications* 6 (2022). [arXiv:2102.09618](https://arxiv.org/abs/2102.09618).
- de Hoop, M. V., Kovachki, N. B., Nelsen, N. H., and Stuart, A. M. “Convergence rates for learning linear operators from noisy data.” *SIAM/ASA Journal on Uncertainty Quantification* 11 (2023). [arXiv:2108.12515](https://arxiv.org/abs/2108.12515).
- Boullé, N., and Townsend, A. “A mathematical guide to operator learning.” 2023. [arXiv:2312.05663](https://arxiv.org/abs/2312.05663).
