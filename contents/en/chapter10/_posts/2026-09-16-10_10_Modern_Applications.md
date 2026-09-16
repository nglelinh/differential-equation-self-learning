---
layout: post
title: "10-10 Modern Applications: Neural Wave Propagation and Seismic Imaging"
chapter: '10'
order: 10
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: optional
---

## Objectives

This optional lesson relates d’Alembert’s formula, finite propagation speed, and energy conservation to physics-informed and operator-learning models of waves, with emphasis on seismic and acoustic applications from 2022–2024. Students should be able to say which wave identities a learned solver is obligated to respect and why inverse wave problems remain microlocal even after a network is introduced. The classical well-posedness theory is not rewritten.

## Prerequisites

Students should know the derivation of the wave equation, d’Alembert’s solution, separation of variables, and the energy method. The optional lessons on dispersion and acoustics are useful background.

## Introduction

Waves carry information at finite speed. That single fact distinguishes $$u_{tt}=c^2 u_{xx}$$ from the heat equation and is the reason seismic, acoustic, and electromagnetic imaging can even be attempted: singularities leave a record on the boundary after a computable delay. Learned solvers that ignore finite speed, energy, or characteristics may look accurate on a short movie and still be useless as imaging engines.

Rasht-Behesht, de Hoop, and collaborators demonstrated physics-informed neural networks for seismic inversion and wave-speed identification in the early 2020s, including *Journal of Geophysical Research* work in 2022 on full-waveform style PINNs. Moseley, Markham, and Nissen-Meyer (*Finite Basis Physics-Informed Neural Networks*, *Advances in Computational Mathematics* 2023; [arXiv:2109.09355](https://arxiv.org/abs/2109.09355)) introduced domain-decomposition PINNs that are much more successful on high-frequency waves than a single global network. On the operator-learning side, FNO and its successors have been trained as cheap wave propagators, while score-based and neural inverse operators (Molinaro, Yang, Li, Azizzadenesheli, Stuart, and Anandkumar, 2023; [arXiv:2201.12904](https://arxiv.org/abs/2201.12904)) attack the inverse problem of recovering coefficients from boundary traces.

The chapter’s energy identity and domain-of-dependence theorem are the admission tests for all of these models.

## Key Concepts

### Characteristics and domain of dependence

d’Alembert’s formula says that $$u(x,t)$$ depends only on initial data on $$[x-ct,x+ct]$$. A neural propagator that lets a localized pulse affect a point outside that interval is superluminal and therefore wrong, regardless of an $$L^2$$ score. Checking domain of dependence is as simple as initializing a compact bump and drawing the light cone.

### Energy conservation as a training constraint

The identity

$$
\frac{d}{dt}\int\Bigl(\tfrac12 u_t^2+\tfrac12 c^2 u_x^2\Bigr)\,dx=0
$$

for a finite string with conservative boundary conditions is a scalar unit test. Soft energy penalties help, but a structure-preserving architecture or a symplectic time integrator is more honest. High-frequency PINNs often dissipate energy because spectral bias kills the oscillatory part of $$u_t$$; that is a numerical viscosity the continuum equation does not contain.

### Inverse waves and visible singularities

Recovering $$c(x)$$ from boundary traces is not a standard BVP. Microlocal analysis, previewed in later chapters, says that only certain singularities are visible. A network that “reconstructs” a smooth $$c$$ from data that cannot see it is hallucinating. Neural inverse operators and diffusion posterior sampling (Chung et al., ICLR 2023) are most credible when they are restricted to the visible part of the wavefront, or when they report uncertainty on the invisible part.

### Domain decomposition for high frequency

A global multilayer perceptron does not like many wavelengths. Finite-basis PINNs and related 2022–2024 decompositions assign a local network to each subdomain and couple them by flux or overlapping penalties. That is the neural analogue of a finite-element or spectral-element mesh, and it is why wave PINNs became plausible for realistic frequencies.

## Methods and Solution Techniques

A wave-aware learning pipeline:

1. Decide whether the task is forward (propagate) or inverse (image).
2. For forward tasks, prefer operator models or decomposed PINNs; test light cones and energy.
3. For inverse tasks, write the forward wave map as a differentiable simulator (classical or learned) and invert with a regularizer that respects visibility.
4. Use d’Alembert on the line, or a modal solution on an interval, as a unit test before any field-scale experiment.
5. Report errors on characteristics, not only at final time: a phase error of a fraction of a wavelength is a large imaging error.

## Examples

### Example 1: Superluminal leakage

Initialize $$u(x,0)=\exp(-x^2/\varepsilon^2)$$, $$u_t=0$$, on a large interval and evaluate a learned solver at a point with $$|x|>cT+\sqrt{\varepsilon}$$. A nonzero value is a light-cone violation. The test costs one forward pass and uses nothing beyond this chapter.

### Example 2: Energy drift of a PINN

On $$[0,\pi]$$ with Dirichlet data, the modal energy of $$\sin(nx)\cos(nct)$$ is constant. A PINN trained on several modes should keep each modal energy. If high $$n$$ decay, the model is a low-pass filter, not a wave solver.

### Example 3: d’Alembert unit test

```python
import numpy as np

c = 1.0
f = lambda x: np.exp(-x**2)
g = lambda x: 0 * x

def dAlembert(x, t):
    return 0.5 * (f(x - c * t) + f(x + c * t))

print(dAlembert(0.0, 0.5), dAlembert(2.0, 0.5))
```

Any learned one-dimensional propagator should be compared with this formula before it is asked to do seismology.

## Applications in Science, Engineering, and Modern Contexts

Seismic full-waveform inversion, ultrasonic non-destructive testing, room acoustics, and electromagnetic time-domain simulation all need many forward wave solves. A trusted surrogate turns those loops into interactive design or into a prior for imaging. Medical photoacoustic imaging and ocean acoustics raise the same characteristic constraints. The 2022 JGR-style PINN inversions and the 2023 neural inverse-operator papers are early but concrete signs that the wave chapter now has a machine-learning practice, not only a metaphor.

Acoustics and Maxwell systems, already discussed in the optional applications lesson, inherit the same energy and finite-speed structure. A learned Maxwell solver that violates a discrete Poynting identity is the vector version of energy drift.

## Challenges and Extensions

Dispersion error is more damaging than amplitude error for imaging. Absorbing boundary conditions are difficult for PINNs. Three-dimensional elastic waves remain expensive to simulate for training. Inverse problems are severely ill-posed at missing apertures. Generative priors can restore plausible texture that is not in the data. Nonlinear waves (Burgers, KdV, Einstein) leave the linear characteristic picture and need different certificates.

A question to keep: if a network conserves energy but moves singularities at the wrong speed, which identity has it failed? The chapter’s answer is the characteristic relation, not the energy identity.

## Exercises

1. **Light cone.** From d’Alembert, prove that compactly supported initial data remain inside $$|x|\le R+ct$$. Design a numerical test for a learned solver.

2. **Energy of a mode.** Compute the energy of $$u=\sin(nx)\cos(nct)$$ on $$[0,\pi]$$. How would you turn the identity into a training constraint without destroying superposition?

3. **Visible jump.** Suppose $$c(x)$$ has a jump that no reflected ray from the available receivers can hit. Why should a reconstruction not be trusted near that jump, even if a network produces a sharp image?

4. **Computational experiment.** Train or hard-code a linear propagator and compare it with d’Alembert on a moving pulse. Report both $$L^2$$ error and the support leakage outside the light cone.

5. **Open exploration.** Read Moseley et al. (2023) or Rasht-Behesht et al. (2022) and write a page on why high-frequency waves force domain decomposition, using only ideas from this chapter.

## References

- Evans, L. C. *Partial Differential Equations*, Chapter 2; Haberman, Chapter 4.
- Moseley, B., Markham, A., and Nissen-Meyer, T. “Finite basis physics-informed neural networks (FBPINNs): a scalable domain decomposition approach for solving differential equations.” *Advances in Computational Mathematics* 49 (2023). [arXiv:2109.09355](https://arxiv.org/abs/2109.09355).
- Rasht-Behesht, M., Huber, C., Shukla, K., and Karniadakis, G. E. “Physics-informed neural networks (PINNs) for wave propagation and full waveform inversions.” *Journal of Geophysical Research: Solid Earth* 127 (2022): e2021JB023120.
- Molinaro, R., Yang, Y., Li, B., Azizzadenesheli, K., Anandkumar, A., and Stuart, A. “Neural inverse operators for solving PDE inverse problems.” 2023. [arXiv:2201.12904](https://arxiv.org/abs/2201.12904).
- Chung, H., et al. “Diffusion posterior sampling for general noisy inverse problems.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
