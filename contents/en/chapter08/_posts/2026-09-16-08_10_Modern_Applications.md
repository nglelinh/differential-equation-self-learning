---
layout: post
title: "08-10 Modern Applications: Fourier Neural Operators"
chapter: '08'
order: 10
owner: Course Team
lang: en
categories:
- chapter08
lesson_type: optional
---

## Objectives

This optional lesson takes Fourier series, Parseval’s identity, and the passage from series to transforms and places them under the Fourier neural operator and its 2022–2024 descendants. Students should be able to read an FNO layer as a learned Fourier multiplier, explain discretization invariance in the language of this chapter, and see aliasing as the same phenomenon that already appears in truncated trigonometric expansions. The convergence theory of Fourier series is not rewritten.

## Prerequisites

Students should know trigonometric and complex Fourier series, even/odd extensions, Parseval’s theorem, and the formal idea of a Fourier transform as a continuous analogue of the coefficients $$c_n$$.

## Introduction

A Fourier series represents a periodic function by a discrete set of harmonics. A Fourier multiplier acts on those harmonics by sending $$c_n\mapsto m_n c_n$$. Classical PDE theory uses this device constantly: differentiation becomes multiplication by $$in$$, and a constant-coefficient operator becomes a symbol. Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart, and Anandkumar (*Fourier Neural Operator for Parametric Partial Differential Equations*, ICLR 2021; [arXiv:2010.08895](https://arxiv.org/abs/2010.08895)) made the multiplier learnable. Each FNO layer computes a Fourier transform, multiplies by a trainable complex tensor on a band of low modes, inverts the transform, and adds a local nonlinear residual.

The 2023 JMLR paper of Kovachki et al. proved that such neural operators can approximate continuous maps between function spaces and that the same parameters can be used at many resolutions. Pathak et al. (*FourCastNet*, 2022; [arXiv:2202.11214](https://arxiv.org/abs/2202.11214)) used an FNO-like backbone for global weather prediction. Li, Huang, Huang, and Anandkumar (*Fourier Neural Operator with Learned Deformations*, *J. Comput. Phys.* 2023) adapted the idea to irregular geometries. Bonev, Kurth, Hundt, Kossaifi, Kashinath, and Anandkumar (*Spherical Fourier Neural Operators*, ICML 2023) replaced the flat FFT by spherical harmonics, which is the honest Fourier theory on the sphere.

This chapter is the reason those papers are readable. An FNO layer is not a mysterious attention block; it is a truncated Fourier expansion plus a learned symbol plus a nonlinear map.

## Key Concepts

### Learned symbols

A scalar periodic multiplier is a sequence $$m_n$$. An FNO layer uses a matrix-valued symbol $$R_n$$ acting on a vector of channels. The student who has written the complex series $$u=\sum c_n e^{inx}$$ already knows the forward and inverse maps. What is new is that $$R_n$$ is trained from pairs of functions, so the layer can approximate a solution operator rather than a single linear PDE.

### Parseval and energy of modes

Parseval’s theorem says that the $$L^2$$ energy is the $$\ell^2$$ energy of coefficients. That is the right way to regularize an FNO: penalize high-mode tails, monitor spectral decay, and refuse to celebrate a model whose energy sits in unresolved aliases. FourCastNet-style weather models live or die by whether they keep the correct energy cascade across scales, which is a Parseval question as much as a meteorological one.

### Aliasing, truncation, and Gibbs

A finite FFT is a truncated Fourier series on a grid. Modes above the Nyquist frequency fold back, exactly as a truncated trigonometric polynomial misrepresents a jump. Bartolucci, de Bézenac, Raonić, Molinaro, Mishra, and Alaifari (*Representation Equivalent Neural Operators*, NeurIPS 2023) analyzed when a discrete neural operator is a consistent discretization of a continuum operator rather than an alias-prone grid map. The Gibbs phenomenon, already visible in the square-wave examples of this chapter, reappears whenever an FNO is asked to learn a discontinuous or sharply layered field.

### From series to transforms

The chapter’s last optional lesson already passed from discrete coefficients to a Fourier transform. FNO on a large torus is the computational version of that passage: the FFT is the transform, the learned band of modes is a compactly supported symbol, and the inverse FFT returns a function. On the sphere one must use the spherical harmonic transform instead, which is why SFNO exists.

## Methods and Solution Techniques

An FNO training loop is a Fourier-analysis loop.

1. Sample input functions $$a$$ (coefficients, initial data, forcings) from a family.
2. Compute reference solutions $$u=\mathcal{G}(a)$$ with a classical solver.
3. Train the stacked multiplier layers so that $$\mathcal{G}_\theta(a)\approx u$$ in an $$L^2$$ or $$H^s$$ norm.
4. Test at a finer resolution than the training grid; success is evidence of discretization invariance.
5. Inspect the learned symbols $$R_n$$. For a linear constant-coefficient target they should resemble the true symbol of the inverse operator.

Geometry-aware variants insert a learned deformation (Geo-FNO) or change the harmonic family (SFNO). In all cases the design decision is the same one this chapter already teaches: which orthogonal system matches the domain?

## Examples

### Example 1: Differentiation as an FNO layer

Differentiation on the circle is the multiplier $$m_n=in$$. An FNO layer with one channel and no nonlinearity should recover this sequence if trained on enough smooth pairs $$(u,u')$$. Plotting $$\operatorname{Im}(R_n)$$ against $$n$$ is a direct Fourier-coefficient exercise.

### Example 2: The square wave as a stress test

The Fourier series of a square wave converges slowly and overshoots at jumps. An FNO trained only on smooth inputs will not learn that tail. Adding a few discontinuous samples, or switching to a basis better adapted to jumps, is the practical response. The example is old; the conclusion for operator learning is new.

### Example 3: FFT multiplier in NumPy

```python
import numpy as np

n = 256
x = np.linspace(0, 2 * np.pi, n, endpoint=False)
u = np.sin(3 * x) + 0.3 * np.cos(8 * x)
uhat = np.fft.rfft(u)
k = np.fft.rfftfreq(n, d=2 * np.pi / n) * 2 * np.pi
dudx = np.fft.irfft(1j * k * uhat, n=n)
print(np.max(np.abs(dudx - 3 * np.cos(3 * x) + 2.4 * np.sin(8 * x))))
```

An FNO layer is this code with $$1j k$$ replaced by a trained complex array and with extra channels and activations around it.

## Applications in Science, Engineering, and Modern Contexts

FNO and its descendants are used as surrogates for Navier–Stokes, Darcy flow, and weather and climate emulation. FourCastNet (2022) showed that a Fourier backbone can produce medium-range global forecasts orders of magnitude faster than a conventional GCM once trained. Spherical FNOs (2023) made the same idea geometrically correct for planetary data. In engineering, learned Fourier multipliers serve as real-time digital twins for periodic or statistically homogeneous devices.

The chapter’s even/odd extensions also have a modern echo. Boundary conditions on an interval are often encoded by choosing a sine or cosine transform rather than a full complex FFT, exactly as one chooses a half-range expansion. A student who understands that choice already understands a large fraction of practical FNO preprocessing.

## Challenges and Extensions

FNO assumes a geometry on which an FFT or a spherical harmonic transform is available. Deformed domains, fractures, and unstructured meshes need extra machinery. Nonlocal symbols with slow decay require many modes, and GPU memory then competes with accuracy. Nonlinear layers after the inverse transform reintroduce aliasing that a purely spectral linear solver would have filtered. Finally, a model trained on one statistical family of inputs need not generalize to another; Fourier structure is not a substitute for a correct training measure.

A reflective question: if the learned symbol $$R_n$$ does not decay, is the operator you are learning actually continuous on $$L^2$$? Parseval plus a bounded-multiplier theorem suggests the answer.

## Exercises

1. **Multiplier for the Helmholtz operator.** Write the symbol of $$(-\Delta+\kappa^2)^{-1}$$ on the circle. How many low modes would you keep in an FNO layer, and why?

2. **Parseval audit.** After training a toy FNO, compute the $$L^2$$ norm of the prediction and the $$\ell^2$$ norm of its Fourier coefficients. What should you see?

3. **Half-range choice.** You want Dirichlet conditions on $$[0,L]$$. Should the FFT be replaced by a sine expansion or a cosine expansion, and how does that choice appear in code?

4. **Computational experiment.** Implement a single linear Fourier-multiplier layer and train it to map $$u$$ to $$u_{xx}$$ on the circle. Plot the learned symbol against $$-n^2$$.

5. **Open exploration.** Read Li et al. (ICLR 2021) and either FourCastNet (2022) or Bonev et al. (ICML 2023). Write one page on which Fourier idea—periodicity, spherical harmonics, or learned deformations—is doing the real work.

## References

- Haberman, R. *Applied Partial Differential Equations*, Chapter 3; Evans, L. C. *Partial Differential Equations*, Appendix on Fourier series.
- Li, Z., et al. “Fourier neural operator for parametric partial differential equations.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
- Kovachki, N., et al. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, no. 89 (2023): 1–97.
- Pathak, J., et al. “FourCastNet: a global data-driven high-resolution weather model using adaptive Fourier neural operators.” 2022. [arXiv:2202.11214](https://arxiv.org/abs/2202.11214).
- Bonev, B., et al. “Spherical Fourier neural operators: learning stable dynamics on the sphere.” *ICML* 2023. [arXiv:2306.03838](https://arxiv.org/abs/2306.03838).
- Li, Z., Huang, D. Z., Huang, B., and Anandkumar, A. “Fourier neural operator with learned deformations for PDEs on general geometries.” *Journal of Computational Physics* 498 (2023): 112666.
