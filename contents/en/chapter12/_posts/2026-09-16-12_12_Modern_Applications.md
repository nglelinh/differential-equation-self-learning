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

> **Storytelling Hook:** Train a standard neural network to predict stress fields on a $64\times 64$ grid, then ask it to predict on a $256\times 256$ grid, and the architecture breaks—its weights are hard-wired to finite pixel vectors. **Operator learning in Sobolev spaces** lifts deep learning into infinite-dimensional Hilbert spaces $H^s(\Omega)$ so models respect both physical derivatives and arbitrary mesh resolutions.

## Objectives

This optional lesson uses $$L^p$$ spaces, weak derivatives, Sobolev norms, and Lax–Milgram well-posedness as the official language of neural-operator theory. Students should be able to say in which space a learned map is claimed to be continuous, why discretization invariance is a functional-analytic statement, and which 2022–2024 papers supply approximation rates. The weak-formulation theory of the chapter is not rewritten.

## Prerequisites

Students should know $$L^p$$ norms, weak derivatives, the spaces $$H^1$$ and $$H^1_0$$, the Lax–Milgram theorem, and the idea of a weak solution of a linear elliptic PDE.

## Background Knowledge Map: Sobolev Analysis Inside Modern Operator Learning

Four functional-analytic concepts directly govern the design and generalization of neural PDE surrogates:

1. **Operators Between Sobolev Spaces:** A PDE solution map $\mathcal{G}: H^{s_1}(\Omega) \to H^{s_2}(\Omega)$ is an infinite-dimensional mapping; training architectures directly on function-space representations (spectral modes or integral kernels) guarantees discretization invariance.
2. **Sobolev Training Losses ($H^1$ vs. $L^2$):** Minimizing only $\|u_\theta - u\|_{L^2}$ allows spurious high-frequency oscillations with tiny amplitude but huge gradient error. Adding the derivative penalty $\|\nabla(u_\theta - u)\|_{L^2}$ trains in the true energy norm $H^1$.
3. **Spectral Truncation Rates in $H^s$:** Projecting a function $u \in H^s$ onto its first $K$ Fourier modes incurs an $L^2$ error of $O(K^{-s})$ and an $H^1$ error of $O(K^{-(s-1)})$—quantifying the exact mode budget $K$ required by an FNO.
4. **Compactness and Sample Complexity:** Because elliptic solution operators map bounded sets in $L^2$ into *compact* sets in $H^1$, the true solution manifold has rapidly decaying Kolmogorov $n$-widths, explaining why relatively few spectral modes capture complex PDE families.

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


### Step-by-Step Worked Example (Read Slowly): Quantifying $L^2$ vs. $H^1$ Spectral Truncation Error

Suppose a target PDE solution on $[0, 2\pi]$ has Fourier cosine expansion $u(x) = \sum_{k=1}^\infty k^{-3}\cos(kx)$, and a Fourier Neural Operator retains only modes $1 \le k \le K$ ($P_K u(x) = \sum_{k=1}^K k^{-3}\cos(kx)$). Compare the exact asymptotic $L^2$ and $H^1$ truncation errors for $K = 10$.

1. **Verify Sobolev regularity of $u$:** Since $|a_k|^2 = k^{-6}$, $\sum_{k=1}^\infty k^{2s} k^{-6} < \infty \iff 6 - 2s > 1 \iff s < 2.5$. Thus $u \in H^2(0,2\pi)$.
2. **Estimate the $L^2$ tail error using Parseval and an integral bound:**
   $$\|u - P_K u\|_{L^2}^2 = \pi \sum_{k=K+1}^\infty k^{-6} \approx \pi \int_K^\infty x^{-6}\,dx = \frac{\pi}{5 K^5}.$$
   For $K = 10$:
   $$\|u - P_{10} u\|_{L^2} \approx \sqrt{\frac{\pi}{5 \cdot 10^5}} \approx 2.51 \times 10^{-3}.$$
3. **Estimate the $H^1$ derivative tail error:** Differentiating multiplies mode $k$ by $k$, multiplying the squared tail by $k^2$:
   $$\|(u - P_K u)'\|_{L^2}^2 = \pi \sum_{k=K+1}^\infty k^2 \cdot k^{-6} = \pi \sum_{k=K+1}^\infty k^{-4} \approx \pi \int_K^\infty x^{-4}\,dx = \frac{\pi}{3 K^3}.$$
   For $K = 10$:
   $$\|(u - P_{10} u)'\|_{L^2} \approx \sqrt{\frac{\pi}{3 \cdot 10^3}} \approx 3.24 \times 10^{-2}.$$
4. **Takeaway for Sobolev training:** Even at $K = 10$, the gradient ($H^1$) truncation error is more than **12 times larger** than the $L^2$ error—illustrating mathematically why evaluating and training neural operators in $H^1$ is essential whenever fluxes, stresses, or velocities matter.

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

## Video tham khảo

- xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, English. Operator learning in function space, the modern use of the Sobolev setting.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, English. DeepONet as a map between function spaces.
- [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, English. The Sobolev space those operator-learning error estimates are stated in.

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
