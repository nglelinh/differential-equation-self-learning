---
layout: post
title: "14-10 Modern Applications: Neural Operators as Learned Symbols"
chapter: '14'
order: 10
owner: Course Team
lang: en
categories:
- chapter14
lesson_type: optional
---

## Objectives

This optional lesson reads Fourier neural operators, spectral neural operators, and related 2022–2024 architectures as computational cousins of pseudodifferential operators. Students should be able to match a learned Fourier multiplier to a symbol in $$S^m$$, explain alias-free operator learning in Hörmander’s language, and see elliptic parametrices as the analytic model for learned inverses. The symbol calculus of the chapter is not rewritten.

## Prerequisites

Students should know Fourier multipliers, symbol classes, composition of ΨDOs, and the idea of an elliptic parametrix. The preparatory review on multipliers is the intended warm-up.

## Introduction

A classical pseudodifferential operator is, to a first approximation, a Fourier multiplier whose symbol $$a(x,\xi)$$ varies slowly in $$x$$ and obeys derivative bounds in $$\xi$$. A Fourier neural operator layer is a Fourier multiplier whose symbol is a trained array $$R_\xi$$, followed by a pointwise nonlinearity. The analogy is imperfect—nonlinearities and finite bands take one outside the linear ΨDO calculus—but it is the right analogy. It explains why FNO works on translation-invariant elliptic and parabolic problems, why it struggles with rough coefficients, and why aliasing is a microlocal rather than merely numerical issue.

Kovachki et al. (*JMLR* 2023) already describe FNO as a parameterized family of integral operators with translation-invariant kernels. Fanaskov and Oseledets (*Spectral Neural Operators*, 2022–2023; [arXiv:2205.10573](https://arxiv.org/abs/2205.10573)) make the spectral calculus even more explicit. Bartolucci, de Bézenac, Raonić, Molinaro, Mishra, and Alaifari (*Representation Equivalent Neural Operators*, NeurIPS 2023; [arXiv:2305.19913](https://arxiv.org/abs/2305.19913)) give a framework for alias-free operator learning: a discrete model should be the exact restriction of a continuum operator, not an accidental grid map. Raonić, Molinaro, Rohner, Mishra, and de Bézenac (*Convolutional Neural Operators*, ICLR 2024; [arXiv:2302.01178](https://arxiv.org/abs/2302.01178)) pursue continuum-consistent convolutional kernels.

Those papers become easier once one has seen $$S^m_{\rho,\delta}$$ and the parametrix construction. A learned inverse of an elliptic operator is an attempt to build a parametrix from data.

## Key Concepts

### Symbols and learned multipliers

The operator $$Au=\mathcal{F}^{-1}\bigl(a(\xi)\hat u(\xi)\bigr)$$ is the constant-coefficient case of a ΨDO of order $$m$$ when $$a\in S^m$$. An FNO layer truncates $$a$$ to a low-frequency box and lets it depend on channels. Training $$a$$ on pairs $$(u,Au)$$ is symbol identification. If the target operator is $$(-\Delta+1)^{-1}$$, the learned symbol should look like $$(|\xi|^2+1)^{-1}$$ on the resolved band and should not grow like a positive power of $$|\xi|$$.

### Composition and stacking layers

The composition theorem says that the symbol of $$AB$$ is $$a\#b=ab$$ plus lower-order terms. Stacking linear FNO layers without nonlinearities is therefore a discrete symbol product. Nonlinear activations between layers take one outside the calculus, which is both the source of expressivity and the source of aliasing: a pointwise product of two band-limited functions is not band-limited.

### Elliptic parametrices as learned inverses

If $$A$$ is elliptic, there exists a ΨDO $$B$$ such that $$BA-I$$ and $$AB-I$$ are smoothing. A neural inverse that maps $$Au$$ back to $$u$$ up to a smooth error is numerically realizing that sentence. One should therefore test a learned inverse on highly oscillatory inputs: the high-frequency symbol must invert the principal symbol, while the low-frequency part may be learned more freely, just as a parametrix is unique only modulo smoothing operators.

### Aliasing as the wrong quantization

A grid map that folds high modes onto low modes is not a ΨDO of the intended order; it is a different operator. Representation-equivalent architectures insist that changing the mesh does not change the continuum operator being discretized. That is the computational form of the statement that a ΨDO is defined on functions, not on arrays.

## Methods and Solution Techniques

A symbol-aware reading of a neural operator:

1. Identify the candidate principal symbol (the high-frequency action).
2. Check the decay or growth of the learned multiplier against a class $$S^m$$.
3. Test composition: does the learned inverse of a learned forward operator look like the identity modulo a smoothing remainder?
4. Refine the mesh. If the operator changes identity, it was never a continuum ΨDO.
5. For variable coefficients, ask whether the architecture can represent an $$x$$-dependent symbol $$a(x,\xi)$$ or only a convolution.

Geo-FNO and convolutional neural operators are attempts to restore $$x$$-dependence and geometric invariance while keeping a continuum kernel.

## Examples

### Example 1: Symbol of the Bessel potential

The operator $$(I-\Delta)^{-s/2}$$ has symbol $$(1+|\xi|^2)^{-s/2}\in S^{-s}$$. A linear spectral layer trained on this map should reproduce that radial profile. Plotting $$|R_\xi|$$ against $$|\xi|$$ on a log-log scale is a homework problem in symbol classes.

### Example 2: Failure on a rough coefficient

The operator $$-\operatorname{div}(a(x)\nabla\cdot)$$ is a ΨDO of order $$2$$ only if $$a$$ is smooth enough. If $$a$$ is merely bounded and elliptic, the operator is still well-posed in $$H^1$$ but is no longer a classical ΨDO of the textbook type. An FNO trained on smooth $$a$$ will not automatically invert a checkerboard permeability. The chapter’s reminder that symbol calculus needs smoothness is the explanation.

### Example 3: Discrete multiplier

```python
import numpy as np

n = 128
k = np.fft.fftfreq(n) * n
symbol = 1.0 / (1.0 + k**2)
u = np.sin(2 * np.pi * np.arange(n) / n)
v = np.fft.ifft(symbol * np.fft.fft(u)).real
print(v.max(), v.min())
```

This is a discrete elliptic parametrix for $$I-\partial_{xx}$$ on the circle. A learned spectral layer should be compared with this object before it is compared with a deep nonlinear stack.

## Applications in Science, Engineering, and Modern Contexts

Thinking of neural operators as learned symbols clarifies several applications. Weather and climate emulators that use Fourier backbones are learning effective symbols for a huge variable-coefficient system; one should not expect a pure convolution to capture orography without a deformation or a position-dependent channel. Inverse elliptic and Helmholtz problems are attempts to learn parametrices from data. Image deblurring with a known point-spread function is literally inversion of a Fourier multiplier, and a network that ignores the symbol will reinvent a worse Wiener filter.

The same viewpoint connects to Chapter 08 (Fourier series) and Chapter 12 (function spaces): a symbol in $$S^{m}$$ maps $$H^{s}$$ to $$H^{s-m}$$. A learned operator that claims an elliptic inverse should therefore improve Sobolev regularity by about two derivatives, which is a measurable statement.

## Challenges and Extensions

Nonlinear layers leave the ΨDO calculus. Variable-coefficient and manifold settings need a full symbol $$a(x,\xi)$$, not only $$a(\xi)$$. Discrete aliasing can produce a compact error that looks small in $$L^2$$ and is large in $$H^{s}$$. Learning a parametrix from data does not automatically give the remainder estimates that Hörmander theory provides. On manifolds, FFTs are the wrong harmonic analysis; spherical and spectral-element analogues are required.

A reflective question: if two learned symbols agree at high frequency but differ by a Schwartz function, do they define the same operator modulo smoothing? The chapter’s answer is yes, and that is why high-frequency tests are the right tests.

## Exercises

1. **Order of a multiplier.** Show that $$a(\xi)=(1+|\xi|^2)^{m/2}$$ lies in $$S^{m}$$. What order should a learned inverse of $$I-\Delta$$ have?

2. **Composition remainder.** For two radial symbols $$a,b$$, the product $$ab$$ is the exact composition symbol. How would you test a two-layer linear FNO against this fact?

3. **Aliasing.** Give a one-dimensional example in which a grid multiplier of even size identifies $$k$$ with $$k-n$$. Why is the resulting operator not a consistent discretization of a continuum multiplier in $$S^{0}$$?

4. **Computational experiment.** Train a linear spectral layer to invert $$I-\partial_{xx}$$ on the circle and plot the learned symbol against $$(1+k^2)^{-1}$$. Then evaluate both operators on a high-frequency sine that was not in the training band.

5. **Open exploration.** Read Bartolucci et al. (NeurIPS 2023) or Fanaskov and Oseledets (2022) and write a page translating “representation equivalence” into the statement that a ΨDO is defined independently of the mesh.

## References

- Trèves, F. *Introduction to Pseudodifferential and Fourier Integral Operators*; Shubin, M. A. *Pseudodifferential Operators and Spectral Theory*; Taylor, M. E. *Pseudodifferential Operators*.
- Kovachki, N., et al. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, no. 89 (2023): 1–97.
- Fanaskov, V., and Oseledets, I. “Spectral neural operators.” 2022. [arXiv:2205.10573](https://arxiv.org/abs/2205.10573).
- Bartolucci, F., et al. “Representation equivalent neural operators: a framework for alias-free operator learning.” *NeurIPS* 2023. [arXiv:2305.19913](https://arxiv.org/abs/2305.19913).
- Raonić, B., et al. “Convolutional neural operators for robust and accurate learning of PDEs.” *ICLR* 2024. [arXiv:2302.01178](https://arxiv.org/abs/2302.01178).
- Li, Z., et al. “Fourier neural operator for parametric partial differential equations.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
