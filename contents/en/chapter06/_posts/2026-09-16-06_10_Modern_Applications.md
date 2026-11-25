---
layout: post
title: "06-10 Modern Applications: Spectral Bases and Operator Learning"
chapter: '06'
order: 10
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: optional
---

Ask a standard deep neural network to solve a differential equation with sharp oscillations or boundary layers, and you will witness a striking pathology called *spectral bias*: gradient descent learns smooth low-frequency shapes almost instantly, while stalling for thousands of epochs on high-frequency modes. Yet classical mathematicians solved this exact problem two centuries ago—by expanding solutions in Chebyshev, Legendre, and Bessel bases that already diagonalize the underlying differential operators.

Today's most reliable Physics-Informed Neural Networks (PINNs) and Neural Operators (DeepONet, Spectral Neural Operators) do not replace Chapter 06; they *embed* Chapter 06 inside modern architectures, letting neural networks learn only the expansion coefficients in a well-conditioned classical basis.

## Key ideas: Classical Spectral Bases in Modern SciML

1. **Spectral Bias vs. Orthogonal Basis Conditioning:** In a standard MLP, high-frequency features have tiny Neural Tangent Kernel (NTK) eigenvalues, causing slow convergence. Expanding $$ u_N(x) = \sum_{n=0}^N c_n \phi_n(x) $$ in Chebyshev or Legendre polynomials preconditions the optimization landscape so high-order modes train cleanly.
2. **Exponential (Spectral) Convergence for Analytic Solutions:** When the true ODE/PDE solution is analytic on $$ [-1, 1] $$, Chebyshev/Legendre coefficients decay geometrically ($$ |c_n| \le C \rho^{-n} $$ for some $$ \rho > 1 $$), achieving machine precision with far fewer degrees of freedom than finite differences or raw MLPs.
3. **Branch–Trunk Factorization (DeepONet as Learned Generalized Series):** DeepONet approximates an operator $$ \mathcal{G}(a)(x) \approx \sum_{k=1}^p b_k(a)\,t_k(x) $$, directly mirroring a truncated series solution where branch outputs $$ b_k(a) $$ play the role of generalized coefficients and trunk outputs $$ t_k(x) $$ play the role of learned basis functions.
4. **Exact Boundary & Singularity Enforcement:** Multiplying a spectral/neural ansatz by distance functions or Frobenius factors $$ x^r $$ bakes boundary conditions and regular singular behavior into the architecture by construction, eliminating stiff penalty terms from the loss function.

### Worked example: Chebyshev Galerkin Spectral Residual vs. Monomial Basis Conditioning

**Problem:** Approximate the solution of the BVP $$ -u''(x) + u(x) = 1 $$ on $$ [-1, 1] $$ with $$ u(\pm 1) = 0 $$ using a 1-mode Chebyshev basis function $$ \phi_0(x) = T_0(x) - T_2(x) = 2(1 - x^2) $$ via Galerkin projection, and compare the midpoint value $$ u_1(0) $$ to the exact solution $$ u(x) = 1 - \frac{\cosh x}{\cosh 1} $$.

1. **Verify exact boundary satisfaction:**
   Since $$ T_0(\pm 1) = 1 $$ and $$ T_2(\pm 1) = 2(\pm 1)^2 - 1 = 1 $$, we have $$ \phi_0(\pm 1) = 0 $$ automatically—zero boundary penalty needed!
2. **Set up the 1-mode ansatz $$ u_1(x) = c_0 \phi_0(x) = 2c_0(1 - x^2) $$:**
   Compute $$ u_1''(x) = -4c_0 $$, so the PDE residual is
   $$ R(x) = -u_1''(x) + u_1(x) - 1 = 4c_0 + 2c_0(1 - x^2) - 1 = 6c_0 - 2c_0 x^2 - 1. $$
3. **Enforce the Galerkin orthogonality condition $$ \int_{-1}^{1} R(x)\,\phi_0(x)\,dx = 0 $$:**
   Using $$ \int_{-1}^{1} (1 - x^2)\,dx = \frac{4}{3} $$ and $$ \int_{-1}^{1} x^2(1 - x^2)\,dx = \frac{2}{3} - \frac{2}{5} = \frac{4}{15} $$:
   $$ 2\left[6c_0\left(\frac{4}{3}\right) - 2c_0\left(\frac{4}{15}\right) - \frac{4}{3}\right] = 0 \implies \left(8 - \frac{8}{15}\right) c_0 = \frac{4}{3} \implies \frac{112}{15} c_0 = \frac{4}{3}. $$
   Solving gives $$ c_0 = \frac{4}{3} \cdot \frac{15}{112} = \frac{5}{28} \approx 0.17857 $$.
4. **Compare $$ u_1(0) $$ against the exact analytical value:**
   - Spectral 1-mode approximation: $$ u_1(0) = 2 c_0 = \frac{5}{14} \approx 0.35714 $$.
   - Exact solution: $$ u(0) = 1 - \frac{1}{\cosh 1} = 1 - \frac{1}{1.54308} \approx 0.35195 $$.
   With literally **one single Chebyshev basis parameter** $$ c_0 $$, we land within $$ 0.0052 $$ (1.5%) of the exact solution across the domain—illustrating why spectral bases dramatically accelerate modern neural solvers!

## Objectives

This optional lesson links power series, Frobenius solutions, and classical special functions to the 2021–2024 practice of spectral PINNs and operator learning. Students should see Chebyshev, Legendre, and Fourier bases as more than textbook families: they are the function-space coordinates in which modern surrogate models are most stable. The Frobenius method and the classical identities for Bessel and Legendre functions are left unchanged.

## Prerequisites

Students should know ordinary and regular singular points, recurrence relations for power series, and the elementary properties of Bessel and Legendre functions. Orthogonality on an interval is the single most useful extra idea.

## Introduction

A series solution is an expansion of an unknown function in a basis that the differential equation itself suggests. Scientific machine learning rediscovered the same tactic. A generic multilayer perceptron prefers low frequencies and struggles with thin boundary layers or highly oscillatory special-function behavior; a spectral architecture expands the unknown, or the operator, in Chebyshev, Legendre, or Fourier modes and learns only the coefficients. Lu, Jin, Pang, Zhang, and Karniadakis introduced DeepONet in *Nature Machine Intelligence* (2021) as a trunk–branch factorization that is, in spirit, a learned generalized Fourier expansion. Kovachki et al. (*JMLR* 2023) then placed Fourier, low-rank, and graph neural operators on a common Banach-space footing.

On the PINN side, Wang, Sankaran, Wang, and Perdikaris collected practical spectral and architectural advice in “An expert’s guide to training physics-informed neural networks” ([arXiv:2308.08468](https://arxiv.org/abs/2308.08468), 2023). Hao et al. (*PINNacle*, NeurIPS 2024 Datasets and Benchmarks; [arXiv:2306.08827](https://arxiv.org/abs/2306.08827)) showed that spectral bias, multi-scale structure, and geometry remain first-order obstacles across more than twenty PDE tasks. Those obstacles are exactly why this chapter spends time on special functions: they are the bases that already diagonalize the operators we care about.

## Key Concepts

### Spectral bias and classical bases

Deep networks trained by gradient descent fit smooth, low-frequency content first. That is helpful for an analytic solution about an ordinary point and disastrous for a Bessel oscillation or a thin layer near a regular singular point. Expanding $$u$$ as

$$
u_N(x)=\sum_{n=0}^{N}c_n\,\phi_n(x)
$$

with $$\phi_n$$ Chebyshev, Legendre, or a Frobenius-inspired family moves the oscillation into the basis, so the network or the linear solver only sees slowly varying coefficients $$c_n$$. This is the same reason one uses a Frobenius ansatz $$x^r\sum a_k x^k$$ rather than a plain power series at a singular point.

### DeepONet as a learned special-function expansion

DeepONet writes an operator as

$$
\mathcal{G}(a)(x)\approx\sum_{k=1}^{p}b_k(a)\,t_k(x).
$$

The trunk nets $$t_k$$ play the role of learned special functions of the independent variable; the branch nets $$b_k$$ play the role of coefficients that depend on the input function $$a$$. When the true solution operator is compact or has rapidly decaying singular values, a short trunk basis suffices, just as a few Legendre polynomials suffice for a smooth solution of a regular Sturm–Liouville problem.

### Recurrence, stability, and evaluation

Classical special functions come with recurrences that are numerically stable if used in the right direction. Learned spectral models need an analogue: orthonormalization, spectral decay penalties, or a hard constraint that high-mode coefficients be small. Without that discipline one reintroduces the divergence that a careless power series already exhibits outside its radius of convergence.

### Physics applications as operator-learning tests

The vibrating membrane and radial Schrödinger problems of the chapter are not only historical applications. They are clean benchmarks: an angular Fourier factor times a Bessel or Legendre radial factor. A neural operator that cannot recover those separations is not yet respecting the geometry that special functions encode.

## Methods and Solution Techniques

Three current strategies sit on top of this chapter’s toolkit.

- **Spectral PINNs.** Replace the network output by a truncated orthogonal expansion and train the coefficients, sometimes with a residual computed by quadrature.
- **Hybrid trunk bases.** Freeze $$t_k$$ as Chebyshev or eigenfunctions and learn only the branch coefficients, which is DeepONet with a classical trunk.
- **Fourier / Laplace neural operators.** Learn multipliers in a spectral domain, then invert. This is series solution at the level of operators rather than functions.

In each case the radius of convergence, the weight of orthogonality, and the distinction between ordinary and singular points remain the right diagnostics. A spectral model on $$[-1,1]$$ with Chebyshev nodes is not automatically valid near a singularity at the origin in polar coordinates.

## Examples

### Example 1: Legendre coefficients as a learned trunk

The solution of $$(1-x^2)y''-2x y'+n(n+1)y=0$$ is $$P_n(x)$$. If a DeepONet trunk is given enough capacity on $$[-1,1]$$ and the training family includes these eigenproblems, one of the trunk functions should correlate strongly with $$P_n$$. Computing that correlation is a better check than a generic $$L^2$$ plot.

### Example 2: Frobenius exponent as a feature

Near a regular singular point the leading exponent $$r$$ is an algebraic unknown. A network that takes $$\log x$$ or $$x^r$$ as an input feature is doing Frobenius by hand. Without that feature it will spend its capacity trying to invent a branch point, usually unsuccessfully. This is one of the multi-scale failures documented in the 2023–2024 PINN guides and in PINNacle.

### Example 3: Chebyshev residual

```python
import numpy as np

# u = exp(x) on [-1, 1], Chebyshev interpolant of degree 8
n = 8
k = np.arange(n + 1)
x = np.cos(np.pi * k / n)
c = np.polynomial.chebyshev.chebfit(x, np.exp(x), n)
xx = np.linspace(-1, 1, 200)
uu = np.polynomial.chebyshev.chebval(xx, c)
print(np.max(np.abs(uu - np.exp(xx))))
```

A spectral PINN that cannot beat this error on an analytic target is wasting the basis that the chapter already provides.

## Applications in Science, Engineering, and Modern Contexts

Spectral operator learning is now used for parametric PDEs in fluids, radiative transfer, and electromagnetics, where the true solutions are expansions in cylindrical or spherical harmonics. Quantum-mechanical surrogates for radial Schrödinger operators are a direct continuation of the chapter’s physics applications. In engineering, Chebyshev PINNs appear as cheap inner solvers inside design loops: one learns a map from a coefficient function to a short vector of spectral coefficients, then reconstructs the field at arbitrary nodes.

The special-function viewpoint also helps communication between analysts and computational scientists. Saying “the trunk learned a Bessel-like radial basis” is more informative than saying “the network generalized.” That vocabulary is this chapter’s contribution to the 2022–2026 literature.

## Challenges and Extensions

Spectral methods hate discontinuities; Gibbs phenomena reappear in learned Fourier and Chebyshev models. Geometry is another obstacle: a basis built for an interval does not automatically transfer to an annulus or a sphere, which is why spherical FNOs (Bonev et al., ICML 2023) had to be invented. Theory for DeepONet approximation in infinite dimensions (Lanthaler, Mishra, and Karniadakis, 2022) gives rates in terms of trunk and branch widths, but those rates assume smoothness that a regular singular point may destroy. Finally, a learned basis is not orthogonal by default, so coefficient magnitudes cannot be read as energies unless one re-orthogonalizes.

A good question: is a neural trunk a new special function, or a numerical approximation of an old one? The answer depends on whether the trunk continues to satisfy a structured recurrence or Sturm–Liouville identity after training.

## Video tham khảo

- xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, English. A Fourier neural operator uses spectral basis functions as its trunk, the idea of this lesson.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, English. DeepONet, the branch-trunk operator network named alongside spectral bases.
- [Taylor series | Chapter 11, Essence of calculus](https://www.youtube.com/watch?v=3d6DsjIBzJ4) — 3Blue1Brown, English. Classical series as the hand-built spectral basis those networks generalize.

## Exercises

1. **Radius of convergence.** Fit a power series and a Chebyshev series to $$1/(1+25x^2)$$ on $$[-1,1]$$. Why does the first diverge at the endpoints in the high-degree limit while the second need not?

2. **Trunk–branch identification.** For the operator that maps $$f$$ to the solution of $$y''=f$$, $$y(\pm 1)=0$$, propose a classical trunk and say what the branch must compute.

3. **Bessel feature.** Explain how to encode the Frobenius exponent of Bessel’s equation of order $$\nu$$ as a network input. What goes wrong if $$\nu$$ is not integer and the second solution involves $$\log x$$?

4. **Computational experiment.** Train a small DeepONet-style model, or a linear spectral surrogate, that maps the source $$f$$ to the solution of $$-y''=f$$ on $$[0,\pi]$$ with Dirichlet data, using a sine trunk. Compare coefficients with the exact Fourier sine series.

5. **Open exploration.** Read the DeepONet paper (2021) and the PINNacle report (2024) and write a short note on when a classical special-function trunk should be frozen rather than learned.

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*, Chapter 5; Haberman, *Applied Partial Differential Equations*, on Bessel and Legendre applications.
- Lu, L., Jin, P., Pang, G., Zhang, Z., and Karniadakis, G. E. “Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators.” *Nature Machine Intelligence* 3 (2021): 218–229.
- Kovachki, N., et al. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, no. 89 (2023): 1–97.
- Wang, S., Sankaran, S., Wang, H., and Perdikaris, P. “An expert’s guide to training physics-informed neural networks.” 2023. [arXiv:2308.08468](https://arxiv.org/abs/2308.08468).
- Hao, Z., et al. “PINNacle: a comprehensive benchmark of physics-informed neural networks for solving PDEs.” *NeurIPS* 2024 Datasets and Benchmarks. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
