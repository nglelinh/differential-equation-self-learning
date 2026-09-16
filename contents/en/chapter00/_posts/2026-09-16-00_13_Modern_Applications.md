---
layout: post
title: "00-13 Modern Applications: Scientific Machine Learning Foundations"
chapter: '00'
order: 13
owner: Course Team
lang: en
categories:
- chapter00
lesson_type: optional
---

## Objectives

This optional lesson connects the chapter’s calculus, linear algebra, and function-space language to scientific machine learning as it has developed from about 2022 to 2026. After reading it, students should be able to see automatic differentiation as a computational form of the chain rule, recognize neural networks as maps between Euclidean or function spaces, and explain why existence, uniqueness, and well-posedness still matter when a model is learned rather than written by hand. The goal is not to replace the foundations already studied, but to show why those foundations now sit underneath physics-informed networks, neural operators, and differentiable solvers.

## Prerequisites

Students should be comfortable with limits, derivatives, multivariable calculus, eigenvalues, and the idea of a normed or inner-product space. No prior deep-learning course is required. The only additional intuition needed is that a neural network is a parameterized family of functions, trained by reducing a loss, and that gradients of that loss are computed automatically.

## Introduction

The classical foundations of this chapter were built to make differential equations precise: one needs continuity to pass to limits, derivatives to write rates of change, linear algebra to diagonalize systems, and function spaces to measure how large a solution is. Those same ingredients now organize an entire research field often called scientific machine learning, or SciML. Instead of fitting a curve through a few data points, modern models try to learn a dynamical law, a solution operator, or a surrogate that respects a differential constraint.

Two questions make the connection concrete. First, if a residual network is a discrete dynamical system, what happens when the step size tends to zero and the architecture becomes a continuous vector field? Second, if a PDE defines a map from data $$a$$ to a solution $$u$$, can one learn that map as an operator between Banach spaces rather than as a finite vector of nodal values? Both questions are meaningless without the language of this chapter: Lipschitz conditions, Jacobians, completeness, and norms that do not secretly depend on a particular mesh.

## Key Concepts

### Automatic differentiation as computational calculus

Training a modern model requires derivatives of a scalar loss with respect to millions of parameters. Automatic differentiation implements the chain rule on a computational graph, so the gradient of

$$
\mathcal{L}(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell\bigl(f_\theta(x_i),y_i\bigr)
$$

is obtained exactly (up to floating-point error) rather than by symbolic expansion or by a crude finite difference. This is the same multivariable calculus already reviewed in the chapter, now applied to compositions that are too large to write by hand. The practical consequence is that any solver, integral, or Fourier multiplier that is itself differentiable can be placed inside a learning loop.

### Neural networks as parameterized maps

A feed-forward network with parameters $$\theta$$ defines a map $$f_\theta:\mathbb{R}^{d_{\mathrm{in}}}\to\mathbb{R}^{d_{\mathrm{out}}}$$. When the unknown is a function $$u(x)$$, one may either evaluate $$f_\theta$$ at collocation points or lift the construction to an operator $$\mathcal{G}_\theta$$ acting on functions. In the first case the ambient space is Euclidean; in the second it is typically a Banach or Hilbert space such as $$L^2$$ or $$H^1$$. The distinction is not cosmetic. A model that is only defined on one mesh cannot be evaluated on a refined mesh without retraining, whereas an operator that is discretization-invariant can, in principle, be transferred across resolutions.

Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, and Anandkumar formulated this operator viewpoint systematically and proved a universal approximation theorem for neural operators acting between Banach spaces ([Kovachki et al., *JMLR* 24(89), 2023](https://jmlr.org/papers/v24/21-1524.html); [arXiv:2108.08481](https://arxiv.org/abs/2108.08481)). Their work makes precise something this chapter already hints at: approximation theory lives in function spaces, not merely in $$\mathbb{R}^n$$.

### Physics-informed residuals and well-posedness

A physics-informed neural network (PINN) represents an unknown solution by a network $$u_\theta$$ and penalizes the differential residual together with data or boundary terms. For a model problem $$u'=f(t,u)$$ one minimizes a loss of the form

$$
\mathcal{L}(\theta)=\sum_{k}\bigl\lvert u_\theta'(t_k)-f\bigl(t_k,u_\theta(t_k)\bigr)\bigr\rvert^2+\sum_{j}\bigl\lvert u_\theta(t_j)-u_j\bigr\rvert^2.
$$

Raissi, Perdikaris, and Karniadakis introduced the modern PINN template in 2019; the subsequent review by Karniadakis, Kevrekidis, Lu, Perdikaris, Wang, and Yang in *Nature Reviews Physics* (2021) framed PINNs, operator learning, and hybrid solvers as a single scientific-ML program. The 2022 survey of Cuomo, Di Cola, Giampaolo, Rozza, Raissi, and Piccialli then organized the rapidly expanding methodology and its failure modes ([Cuomo et al., *J. Sci. Comput.* 2022](https://doi.org/10.1007/s10915-022-01939-z); [arXiv:2201.05624](https://arxiv.org/abs/2201.05624)).

Existence and uniqueness theorems remain the right conceptual filter. If the underlying initial-value problem fails a Lipschitz condition, a small change in $$\theta$$ can produce a large change in $$u_\theta$$, and the optimization landscape becomes untrustworthy. Conversely, when the differential problem is well-posed, a small residual is meaningful information rather than an artifact of an ill-posed formulation.

### Continuous-depth models and completeness

Kidger’s 2022 thesis *On Neural Differential Equations* ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) presents residual networks, neural ODEs, neural controlled DEs, and neural SDEs as one family. The completeness of the ambient space matters here just as it does in elementary analysis: one needs a setting in which Picard iteration, adjoint equations, and stochastic integrals are guaranteed to converge. The same metric and norm language used to discuss Cauchy sequences now underwrites reverse-mode differentiation through an ODE solver.

## Methods and Solution Techniques

The methodological shift is best described as a change of unknown. Classical analysis seeks a function $$u$$ satisfying an equation. Scientific ML seeks parameters $$\theta$$ such that $$u_\theta$$, or an operator $$\mathcal{G}_\theta$$, approximately satisfies a family of equations. The computational engine is almost always a first-order method on $$\theta$$ (stochastic gradient descent or Adam), but the objects being differentiated are the same derivatives, Jacobians, and inner products studied in this chapter.

A useful taxonomy is therefore:

- **Function approximation.** Learn $$u_\theta(x)$$ for one instance, as in a PINN.
- **Operator approximation.** Learn $$\mathcal{G}_\theta:a\mapsto u$$ for a family of instances, as in a neural operator.
- **Hybrid modeling.** Keep a mechanistic core and learn only the missing vector field, closure, or forcing term.

In all three cases one should ask the same foundational questions already practiced here: in which space does the unknown live, what topology makes convergence meaningful, and which linear-algebraic structure (spectrum, inner product, orthogonality) is being exploited?

## Examples

### Example 1: A residual block as an Euler step

A residual layer $$x_{n+1}=x_n+h\,f_\theta(x_n)$$ is forward Euler for the ODE $$x'=f_\theta(x)$$. If $$f_\theta$$ is Lipschitz, the discrete trajectory converges, as $$h\to 0$$, to a unique continuous trajectory. This is Picard–Lindelöf in computational clothing. The same Lipschitz constant that guarantees uniqueness also controls the stiffness of training: a large Lipschitz constant produces a stiff neural ODE and an expensive solver.

### Example 2: Why the choice of norm matters

Suppose two candidate solutions $$u$$ and $$v$$ agree at mesh nodes but differ by a highly oscillatory mode between nodes. In the Euclidean norm of nodal values they look close; in $$H^1$$ they may be far apart because the derivatives differ. Operator-learning papers therefore report errors in function-space norms, not only in pointwise snapshots. That habit is a direct application of the normed-space discussion in this chapter.

### Example 3: A minimal autodiff check

The following snippet confirms that a computational graph recovers the exact derivative of a simple scalar map, the same fact the chain rule already guarantees.

```python
import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.sin(x) * torch.exp(-x)
y.backward()
print(float(x.grad), float((torch.cos(x) - torch.sin(x)) * torch.exp(-x)))
```

The two printed numbers agree. Scaling the same idea to a PINN residual or an ODE adjoint does not change the calculus; it only changes the size of the graph.

## Applications in Science, Engineering, and Modern Contexts

Scientific ML now appears wherever a differential model is trusted but expensive, incomplete, or only partly observed. Climate emulators learn surrogate operators for atmospheric PDEs; medical imaging networks invert elliptic or hyperbolic forward maps; control engineers learn certificates that prove stability rather than merely fitting trajectories. In each setting the chapter’s foundations decide what “a good approximation” means. A network that is accurate in $$L^2$$ may still be unusable if pointwise maxima or fluxes are the quantities of engineering interest. A learned vector field that is not Lipschitz can leave the existence theory, and therefore the simulator, behind.

The reviews of Karniadakis et al. (2021) and Cuomo et al. (2022) collect these application domains, while Kovachki et al. (2023) and Kidger (2022) supply the two theoretical poles: operator learning in infinite dimensions, and continuous-depth models as differential equations. Later chapters of this course return to the same papers in more specialized form. The point of the present lesson is simply that none of that literature is alien to the calculus and linear algebra already in hand.

## Challenges and Extensions

Several limitations should be stated clearly. Automatic differentiation through a long time horizon can be unstable; the adjoint method trades memory for a new ODE that may itself be stiff. PINN losses mix residuals, boundary data, and observations with weights that are not given by the equation, so a small reported loss need not imply a small solution error. Universal approximation theorems guarantee existence of a good network, not that gradient descent will find it. Finally, a learned model can violate conservation, positivity, or invariance unless those structures are built into the architecture.

A reflective question is therefore: if two networks achieve the same residual, which function-space norm should decide which one is closer to the true solution? Another: what does completeness buy us once the unknown is a probability measure over trajectories rather than a single curve?

## Exercises

1. **Chain rule and autodiff.** Let $$y=\sin(e^{x^2})$$. Compute $$y'$$ by hand and check the result with automatic differentiation. What quantity is being stored on the computational graph at each elementary operation?

2. **Lipschitz constants and uniqueness.** Consider $$x'=|x|^{1/2}$$ with $$x(0)=0$$. Explain why Picard–Lindelöf fails, and discuss what would go wrong if a neural ODE used a vector field with the same local regularity.

3. **Norms on a mesh.** Take $$u_h(x)=\sin(2\pi n x)$$ sampled on $$N$$ uniform nodes of $$[0,1]$$. Compare the Euclidean nodal norm with a trapezoidal approximation of $$\|u_h\|_{L^2}$$ and of $$\|u_h'\|_{L^2}$$ as $$n$$ grows. Which norm detects the oscillation?

4. **Computational experiment.** Using PyTorch or JAX, train a two-layer network to fit $$u(t)=e^{-t}$$ on $$[0,2]$$ by minimizing only the ODE residual $$u'+u$$ together with $$u(0)=1$$. Then repeat the experiment with a noisy initial condition. How does the learned solution change, and which theorem from this chapter explains the sensitivity?

5. **Open exploration.** Read the introduction of Kovachki et al. (2023) or Kidger (2022) and write a half-page argument answering: is a neural operator closer to a numerical solver, to a Green’s function, or to a new kind of special function?

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*. Appendices on calculus and linear algebra; the classical foundation this lesson refuses to replace.
- Karniadakis, G. E., Kevrekidis, I. G., Lu, L., Perdikaris, P., Wang, S., and Yang, L. “Physics-informed machine learning.” *Nature Reviews Physics* 3 (2021): 422–440.
- Cuomo, S., Di Cola, V. S., Giampaolo, F., Rozza, G., Raissi, M., and Piccialli, F. “Scientific machine learning through physics-informed neural networks: where we are and what’s next.” *Journal of Scientific Computing* 92 (2022): 88. [arXiv:2201.05624](https://arxiv.org/abs/2201.05624).
- Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., and Anandkumar, A. “Neural operator: learning maps between function spaces with applications to PDEs.” *Journal of Machine Learning Research* 24, no. 89 (2023): 1–97. [https://jmlr.org/papers/v24/21-1524.html](https://jmlr.org/papers/v24/21-1524.html).
- Kidger, P. *On Neural Differential Equations*. DPhil thesis, University of Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
