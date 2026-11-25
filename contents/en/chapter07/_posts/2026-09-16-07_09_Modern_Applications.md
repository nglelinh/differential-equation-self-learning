---
layout: post
title: "07-09 Modern Applications: PINNs for Boundary Value Problems"
chapter: '07'
order: 9
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: optional
---

Classical solvers like finite differences and finite elements solve boundary value problems by chopping the domain into a mesh and inverting a huge sparse matrix. Physics-Informed Neural Networks (PINNs) take a strikingly different approach: represent $$ u_\theta(x) $$ as a smooth neural network and train its weights $$ \theta $$ by minimizing the squared ODE/PDE residual plus boundary mismatches. Yet practitioners quickly discovered a painful trap—if you enforce boundary conditions only as "soft" penalty terms in the loss function, gradient conflicts can let the network satisfy the interior ODE while drifting away from the boundaries!

Modern PINN theory solves this by importing two classical Chapter 07 weapons directly into neural architectures: *hard boundary-condition trial functions* (a trick dating back to Lagaris et al., 1998) and *spectral/Green's-function priors*.

## Key ideas: PINNs Through the Lens of BVP Theory

1. **Soft Penalty vs. Hard Boundary Enforcement:** A soft PINN loss $$ \mathcal{L} = \mathcal{L}_{\text{ODE}} + \lambda_{\text{bc}}\mathcal{L}_{\text{BC}} $$ can suffer from stiff, competing gradients. By writing $$ u_\theta(x) = g(x) + d(x)\,N_\theta(x) $$—where $$ g(x) $$ interpolates the boundary values and $$ d(x) $$ vanishes on $$ \partial\Omega $$—the boundary conditions are satisfied *exactly* for every weight vector $$ \theta $$.
2. **Automatic Differentiation as Exact Operator Evaluation:** Reverse-mode autodiff computes $$ u_\theta'(x) $$ and $$ u_\theta''(x) $$ to machine precision without discretization error, turning any Sturm–Liouville residual $$ R_\theta(x) = -(p u_\theta')' + q u_\theta - f $$ into a differentiable objective.
3. **Eigenvalue & Inverse BVP Discovery:** Unlike classical solvers that need all coefficients in advance, PINNs can treat unknown physical parameters (or eigenvalues $$ \lambda $$) as trainable scalars alongside $$ \theta $$, recovering diffusivity or stiffness fields directly from sparse noisy measurements.
4. **Failure Modes & Diagnostics (Collocation & Stiffness):** Uniform collocation points can miss sharp boundary layers; adaptive residual-based sampling (RAR) and Fourier feature embeddings directly counteract spectral bias on high-wavenumber BVPs.

### Worked example: Designing a Hard-BC Trial Function and Computing Its Exact Residual

**Problem:** For the BVP $$ -u''(x) + u(x) = x $$ on $$ [0, 1] $$ with $$ u(0) = 1 $$ and $$ u(1) = 2 $$, construct a hard-BC trial function $$ u_\theta(x) = g(x) + x(1-x) N_\theta(x) $$, take the simplest 1-parameter linear network $$ N_\theta(x) = \theta $$ (a constant), and find the optimal $$ \theta^* $$ minimizing the collocation loss at the single interior point $$ x = \frac{1}{2} $$.

1. **Construct the boundary interpolant $$ g(x) $$ and distance factor $$ d(x) $$:**
   - Linear interpolant through $$ (0, 1) $$ and $$ (1, 2) $$: $$ g(x) = 1 + x $$.
   - Distance factor vanishing at $$ x = 0, 1 $$: $$ d(x) = x(1 - x) $$.
   - Trial function: $$ u_\theta(x) = 1 + x + \theta\, x(1 - x) $$.
   Check BCs: $$ u_\theta(0) = 1 $$ and $$ u_\theta(1) = 2 $$ for *every* $$ \theta \in \mathbb{R} $$!
2. **Compute the exact ODE residual via differentiation:**
   - $$ u_\theta'(x) = 1 + \theta(1 - 2x) $$.
   - $$ u_\theta''(x) = -2\theta $$.
   - Residual:
     $$ R_\theta(x) = -u_\theta''(x) + u_\theta(x) - x = 2\theta + \bigl[1 + x + \theta x(1 - x)\bigr] - x = 1 + \theta\bigl(2 + x - x^2\bigr). $$
3. **Minimize $$ \mathcal{L}(\theta) = \bigl[R_\theta(1/2)\bigr]^2 $$ at $$ x = \frac{1}{2} $$:**
   At $$ x = \frac{1}{2} $$, $$ 2 + \frac{1}{2} - \frac{1}{4} = \frac{9}{4} $$, so
   $$ R_\theta\!\left(\frac{1}{2}\right) = 1 + \frac{9}{4}\theta = 0 \implies \theta^* = -\frac{4}{9} \approx -0.4444. $$
4. **Compare $$ u_{\theta^*}(1/2) $$ to the exact BVP solution:**
   - Hard-BC 1-parameter PINN: $$ u_{\theta^*}(1/2) = 1.5 - \frac{4}{9}\left(\frac{1}{4}\right) = \frac{3}{2} - \frac{1}{9} = \frac{25}{18} \approx 1.3889 $$.
   - Exact solution $$ u(x) = x + \frac{\sinh(1 - x) + \sinh x}{\sinh 1} $$ at $$ x = \frac{1}{2} $$:
     $$ u\!\left(\frac{1}{2}\right) = 0.5 + \frac{2\sinh(0.5)}{\sinh 1} = 0.5 + \frac{1}{\cosh(0.5)} \approx 0.5 + \frac{1}{1.12763} \approx 1.3868. $$
   With just **one** trainable parameter and exact hard BCs, the midpoint error is only $$ 0.0021 $$ (0.15%)!

## Objectives

This optional lesson places two-point boundary value problems, Sturm–Liouville eigenvalues, and Green’s functions next to physics-informed networks and variational neural solvers. Students should be able to write a PINN loss for a BVP, explain why eigenvalue problems are harder than linear source problems, and use the 2021–2024 failure-mode literature as a diagnostic rather than as a reason to abandon the method. The Sturm–Liouville theory of the chapter is not rewritten.

## Prerequisites

Students should know two-point boundary conditions, self-adjoint Sturm–Liouville form, eigenfunction expansions, and the idea of a Green’s function as an inverse of a differential operator.

## Introduction

A boundary value problem asks for a function that satisfies a differential equation and conditions at more than one point. That global constraint is why BVPs feel different from IVPs, and it is why naive neural solvers often fail: the network can satisfy the ODE in the interior and still miss the second boundary, or it can satisfy both boundaries and still sit in the wrong eigenspace.

Raissi, Perdikaris, and Karniadakis (2019) set the modern PINN template. Krishnapriyan, Gholami, Zhe, Kirby, and Mahoney (*Characterizing possible failure modes in physics-informed neural networks*, NeurIPS 2021) then showed that simple convection, reaction, and high-frequency BVPs can make PINNs collapse. Wang, Yu, and Perdikaris analyzed gradient pathologies and stiffness in the PINN loss (*SIAM J. Sci. Comput.*, 2021, and later work). Cuomo et al. (*J. Sci. Comput.*, 2022) surveyed the resulting methodology. Hao et al. (*PINNacle*, NeurIPS 2024) turned those observations into a public benchmark that includes heat, fluids, and eigenvalue-like multi-scale tasks.

A parallel variational line, the Deep Ritz method of E and Yu (2018) and its descendants, minimizes an energy rather than a strong residual and is closer in spirit to the weak form that Sturm–Liouville theory already uses. Green’s functions sit at the other end: once an operator is inverted, learning the inverse as an operator (DeepONet, neural operators) becomes a BVP-level task rather than a pointwise one.

## Key Concepts

### PINN losses for two-point problems

For $$-u''=f$$ on $$(0,1)$$ with $$u(0)=u(1)=0$$ a standard loss is

$$
\mathcal{L}(\theta)=\sum_i\bigl(u_\theta''(x_i)+f(x_i)\bigr)^2+\lambda\bigl(u_\theta(0)^2+u_\theta(1)^2\bigr).
$$

The weight $$\lambda$$ is not given by the equation. If it is too small the network ignores the boundary; if it is too large the residual is under-trained. That trade-off is the computational image of the fact that a BVP is an operator equation plus a subspace constraint, not an IVP plus a penalty.

### Eigenvalues as a joint unknown

A Sturm–Liouville eigenvalue problem asks for a pair $$(\lambda,u)$$. A PINN must therefore learn both, usually with a normalization $$\|u\|_{L^2}=1$$ and an orthogonality penalty against previously found eigenfunctions. Without those constraints the network drifts toward the trivial solution or toward a mixture of modes. The chapter’s eigenvectors-are-orthogonal theorem is the regularization.

### Green’s functions and operator learning

The solution $$u(x)=\int G(x,s)f(s)\,ds$$ is already an operator. Learning $$G$$, or learning the map $$f\mapsto u$$ directly, is often more reusable than learning one $$u$$. Physics-informed DeepONets (Wang, Wang, and Perdikaris, *Science Advances*, 2021) and the neural-operator theory of Kovachki et al. (2023) take that route. For a self-adjoint negative operator the learned kernel should come out approximately symmetric, which is a concrete check students can perform.

### Failure modes that the theory predicts

High Péclet numbers, thin layers, and sharp eigenfunction oscillations produce the same spectral bias already met in the series chapter. Causality is less of an issue for elliptic BVPs than for evolution, but the closest analogue is the maximum principle: a network that dips below the boundary values on a source-free interval is violating a theorem, not just a loss term. PINNacle (2024) documents how often popular fixes (adaptive weights, domain decomposition, residual-based resampling) help, and how often they do not.

## Methods and Solution Techniques

A BVP-oriented workflow is:

1. Write the strong form, the boundary operators, and, if available, the energy form.
2. Choose representation: a raw network, a network that hard-enforces boundaries by multiplying by $$x(1-x)$$, or a spectral trunk of eigenfunctions.
3. Train with residual and boundary (or energy) terms; adapt weights if the gradient of one term dominates.
4. For eigenvalues, add normalization and deflation.
5. Validate with the chapter’s tools: orthogonality integrals, Green’s identity, nodal counts of eigenfunctions.

Hard enforcement of Dirichlet data is the single most effective elementary improvement. It is the neural analogue of choosing a function space that already sits in $$H^1_0$$.

## Examples

### Example 1: Hard boundary encoding

The ansatz $$u_\theta(x)=x(1-x)n_\theta(x)$$ solves $$u(0)=u(1)=0$$ exactly. The loss then contains only the differential residual. This is a one-line change that often outperforms a large boundary penalty, and it mirrors the way one constructs a particular function in the variation-of-parameters or Green’s-function argument.

### Example 2: First eigenfunction of $$-u''=\lambda u$$

The exact pair is $$\lambda=\pi^2$$, $$u=\sqrt{2}\sin(\pi x)$$ on $$(0,1)$$. A PINN that reports $$\lambda\approx 9.87$$ but an eigenfunction with two interior zeros has jumped to a higher mode. Counting zeros is the Sturm oscillation theorem used as a unit test.

### Example 3: Residual assembly

```python
import torch

def u_hat(x, net):
    return x * (1 - x) * net(x)

x = torch.linspace(0, 1, 64, requires_grad=True).view(-1, 1)
net = torch.nn.Sequential(torch.nn.Linear(1, 32), torch.nn.Tanh(), torch.nn.Linear(32, 1))
u = u_hat(x, net)
du = torch.autograd.grad(u.sum(), x, create_graph=True)[0]
d2u = torch.autograd.grad(du.sum(), x, create_graph=True)[0]
f = torch.ones_like(x)
loss = ((-d2u - f)**2).mean()
print(float(loss))
```

The printed residual is not yet a solution, but the construction already respects the two-point condition.

## Applications in Science, Engineering, and Modern Contexts

Neural BVP solvers are used for parametric elasticity, groundwater flow, and Helmholtz problems in which many right-hand sides or many coefficients must be inverted. Eigenvalue PINNs appear in vibrating-structure identification and in quantum ground-state searches. In both settings the reusable object is often the inverse operator, not a single snapshot, which is why Green’s functions and operator learning belong in the same conversation.

Engineering trust still runs through the classical tests. A learned mode shape that is not orthogonal to a lower mode, or a learned deflection that violates a maximum principle, should be rejected before it enters a design loop. PINNacle’s public tasks make that rejection empirical rather than anecdotal.

## Challenges and Extensions

PINNs remain sensitive to loss weights, sampling, and architecture. High-frequency Helmholtz BVPs and strong convection layers are still difficult in 2024 benchmarks. Variational methods need a correct function space and a quadrature that does not hide boundary layers. Operator-learning inverses need training families that cover the relevant sources; they do not create a Green’s function for free. Mixed boundary conditions and transmission problems require interface residuals that the basic two-point story does not contain.

A reflective prompt: if a PINN residual is small but the discrete Green’s identity fails, which error is more important? The chapter suggests the identity, because it encodes self-adjointness and conservation.

## Video tham khảo

- xem trước: [Physics Informed Neural Networks (PINNs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — Steve Brunton, English. Physics-informed networks enforce a boundary-value residual, the method of this lesson.
- [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, English. The classical Sturm-Liouville problem those networks are being asked to respect.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, English. Operator networks as another way to learn a boundary-value solution map.

## Exercises

1. **Function space first.** Explain why the ansatz $$u=x(1-x)n(x)$$ is a hard encoding of Dirichlet data but not of Neumann data. Propose an ansatz for $$u'(0)=u'(1)=0$$.

2. **Deflation.** Write a loss term that penalizes overlap of a new eigenfunction with $$\sin(\pi x)$$ and $$\sin(2\pi x)$$. Why is $$L^2$$ the natural inner product?

3. **Green’s check.** For $$-u''=f$$, $$u(0)=u(1)=0$$, the kernel is $$G(x,s)=\min(x,s)-xs$$. How would you test whether a learned operator $$\mathcal{G}(f)$$ is close to this integral operator?

4. **Computational experiment.** Train the hard-encoded PINN above with $$f\equiv 1$$ and compare $$u_\theta$$ with the exact $$u(x)=\tfrac12 x(1-x)$$. Then increase the frequency to $$f=\sin(8\pi x)$$ and record what happens to the error.

5. **Open exploration.** Read Krishnapriyan et al. (NeurIPS 2021) or the PINNacle paper (2024) and list three BVP features that systematically break a vanilla PINN. For each, name the theorem or construction from this chapter that predicted the difficulty.

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*, Chapters 10–11; Haberman, Chapter 5.
- Krishnapriyan, A. S., Gholami, A., Zhe, S., Kirby, R., and Mahoney, M. W. “Characterizing possible failure modes in physics-informed neural networks.” *NeurIPS* 2021. [arXiv:2109.01050](https://arxiv.org/abs/2109.01050).
- Cuomo, S., et al. “Scientific machine learning through physics-informed neural networks.” *Journal of Scientific Computing* 92 (2022): 88. [arXiv:2201.05624](https://arxiv.org/abs/2201.05624).
- Hao, Z., et al. “PINNacle: a comprehensive benchmark of physics-informed neural networks for solving PDEs.” *NeurIPS* 2024 Datasets and Benchmarks. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
- Wang, S., Wang, H., and Perdikaris, P. “Learning the solution operator of parametric partial differential equations with physics-informed DeepONets.” *Science Advances* 7, no. 40 (2021): eabi8605.
