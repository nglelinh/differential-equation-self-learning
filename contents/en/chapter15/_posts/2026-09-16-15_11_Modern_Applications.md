---
layout: post
title: "15-11 Modern Applications: Learned Inverse Problems and Microlocal Priors"
chapter: '15'
order: 11
owner: Course Team
lang: en
categories:
- chapter15
lesson_type: optional
---

## Objectives

This optional lesson connects wavefront sets, propagation of singularities, and inverse problems to the 2022–2024 practice of neural inverse operators and score-based reconstruction. Students should be able to say which singularities a learned imager is allowed to recover, why a plausible image can still be microlocally dishonest, and where the current-research lesson of this chapter meets scientific ML. The microlocal theorems already developed are not rewritten.

## Prerequisites

Students should know wavefront sets, the propagation theorem for real principal-type operators, the idea of a Fourier integral operator, and the optional inverse-problems lesson. The existing “Current Research Directions” lesson is complementary: it maps the analytic landscape; this one adds the machine-learning layer.

## Introduction

Microlocal analysis was built to answer visibility questions. Which singularities of a hidden potential, a sound speed, or an attenuation travel to the detectors? Which ones are lost in a shadow? Those questions did not become obsolete when neural networks arrived. They became more urgent, because a network can paint a sharp edge that no ray, no canonical relation, and no FIO ever carried to the data.

Three 2022–2024 developments make the contact concrete. Molinaro, Yang, Li, Azizzadenesheli, Anandkumar, and Stuart (*Neural Inverse Operators*, 2023; [arXiv:2201.12904](https://arxiv.org/abs/2201.12904)) learn regularized inverses of PDE forward maps, including Helmholtz-type imaging. Song, Shen, and collaborators brought score-based generative models to medical inverse problems around ICLR 2022, and Chung, Kim, Mccann, Klasky, and Ye (*Diffusion Posterior Sampling*, ICLR 2023; [arXiv:2209.14687](https://arxiv.org/abs/2209.14687)) gave a widely used recipe for combining a diffusion prior with a forward operator. Rasht-Behesht et al. (JGR 2022) and related PINN inversions attack seismic full-waveform problems with physics residuals.

In each case the forward map is an FIO, or a composition of FIOs, at high frequency. A learned inverse that does not respect the canonical relation is not a new theory of imaging; it is a prior that may or may not be honest about what the data contain.

## Key Concepts

### Visible versus invisible wavefronts

If $$\operatorname{WF}(f)$$ does not intersect the set of singularities that the FIO of the experiment can see, no method—analytic or learned—should claim to recover those singularities from the data alone. A generative prior can still invent them. Responsible papers therefore report uncertainty or a null-space component. Microlocal analysis is the language in which that null space is described.

### Neural inverse operators

A neural inverse operator approximates a regularized inverse $$F_\alpha^\dagger$$ of a forward map $$F$$. Regularization is not optional: the true inverse, when it exists, is usually unbounded on $$L^2$$. Sobolev and microlocal mappings tell one which spaces $$F_\alpha^\dagger$$ can map into. If $$F$$ loses one derivative and one set of directions, a network that outputs a very rough image in an invisible direction is fitting the prior, not the data.

### Score-based posteriors

Diffusion posterior sampling draws from an approximate posterior $$p(x\mid y)$$ by combining a learned score $$\nabla\log p(x)$$ with a data-consistency step involving $$F$$. The construction is powerful for medical imaging and inpainting. The microlocal caution is that the prior score can restore wavefronts that $$F^*F$$ annihilates. Looking at the residual $$y-F\hat x$$ in the wavefront set of the data, not only in an $$L^2$$ norm, is the right audit.

### PINN inversions and high frequency

Physics-informed inversions encode $$F$$ as a residual rather than as a trained surrogate. They are attractive when data are scarce and the PDE is trusted. They remain limited by spectral bias at high frequency, which is precisely the regime in which microlocal statements are sharpest. Domain-decomposition wave PINNs (Moseley et al., 2023) mitigate that bias but do not change the visibility calculus.

## Methods and Solution Techniques

A microlocally literate inverse-learning pipeline:

1. Identify the forward operator $$F$$ and, if possible, its canonical relation.
2. State which singularities are visible for the available acquisition geometry.
3. Choose a learned inverse (NIO, FNO inverse, PINN, or diffusion sampler) and a regularizer.
4. Validate on phantoms whose wavefronts are partly invisible; a method that “recovers” the invisible part is overfitting a prior.
5. Report both image-domain errors and data-domain wavefront residuals.

This pipeline does not compete with the current-research lesson; it adds a computational column to the same map (inverse problems, spectral geometry, imaging artifacts).

## Examples

### Example 1: Limited-angle tomography

Limited-angle X-ray data cannot see edges whose normals lie in a missing cone. A diffusion model trained on complete images will happily complete those edges. The reconstruction may look medical and still be microlocally false. The right figure is not the pretty image; it is the image with the missing cone painted as unknown.

### Example 2: Helmholtz imaging at increasing wavenumber

As $$k$$ grows, the Helmholtz inverse problem becomes more FIO-like and more sensitive to phase. A neural inverse trained at small $$k$$ will not automatically work at large $$k$$. That is the semiclassical lesson of this chapter in experimental form.

### Example 3: Data residual as a wavefront check

```python
import numpy as np

# toy 1D "projection": moving average hides high-frequency jumps
def F(x):
    return np.convolve(x, np.ones(5) / 5.0, mode="same")

x_true = np.zeros(64)
x_true[20:22] = 1.0
x_prior = np.zeros(64)
x_prior[40:42] = 1.0  # invented jump
print(np.linalg.norm(F(x_true) - F(x_true)), np.linalg.norm(F(x_true) - F(x_prior)))
```

The invented jump is almost invisible to $$F$$. A method that outputs it from $$y=F(x_{\mathrm{true}})$$ has used a prior, not the data. Wavefront language says the same thing without a toy convolution.

## Applications in Science, Engineering, and Modern Contexts

CT, MRI, photoacoustics, seismic imaging, and radar are the applied homes of this discussion. Hospitals already use learned reconstruction; the open scientific question is whether those reconstructions are stable in the microlocal sense or only in a perceptual sense. Geophysical imaging has the same split: a PINN or a neural inverse can produce a velocity model that fits the traces and still misplace a reflector along an invisible bicharacteristic.

Quantum and semiclassical topics of the chapter also have ML echoes—learned Wigner or Husimi representations, neural approximations of spectral measures—but the inverse-problem contact is the most mature 2022–2024 story, and it is the one that students can audit with the tools they already have.

## Challenges and Extensions

Generative priors can dominate the data. Acquisition geometries change, and a network trained on one canonical relation need not transfer to another. High-frequency analysis and low-frequency learned models live on different asymptotic planets; matching them is an active research problem. Uncertainty estimates are often poorly calibrated in invisible directions. Nonlinear inverse problems (anisotropic conductivity, nonlinear waves) leave the linear FIO calculus.

The existing research-directions lesson asked how much of a shape is audible or visible. The present lesson adds: how much of a shape is a network allowed to draw? The honest answer is still given by the wavefront set of the data, plus a clearly labeled prior.

## Exercises

1. **Missing cone.** Sketch the visible wavefronts for limited-angle tomography and explain why an $$\ell^2$$ residual can be small while an invisible edge is wrong.

2. **Canonical relation as a diagram.** Draw $$F$$ as a relation between $$T^*X$$ and $$T^*Y$$. Where in that diagram does a neural inverse have freedom, and where does it not?

3. **Prior versus data.** Using the toy convolution above, design a regularizer that forbids jumps in the invisible high-frequency component. What is the microlocal analogue?

4. **Computational experiment.** Implement a small linear inverse with a diffusion-like denoiser (even a Gaussian blur prior) and compare reconstructions of a visible edge and an invisible edge.

5. **Open exploration.** Read Chung et al. (ICLR 2023) or Molinaro et al. (2023) together with the inverse-problems lesson of this chapter. Write one page on a single sentence that should appear in every learned-reconstruction paper: which wavefronts are claimed to come from the data?

## References

- Hörmander, L. *The Analysis of Linear Partial Differential Operators*, Vols. III–IV; Zworski, M. *Semiclassical Analysis*; the inverse-problems and current-research lessons of this chapter.
- Molinaro, R., Yang, Y., Li, B., Azizzadenesheli, K., Anandkumar, A., and Stuart, A. “Neural inverse operators for solving PDE inverse problems.” 2023. [arXiv:2201.12904](https://arxiv.org/abs/2201.12904).
- Chung, H., Kim, J., Mccann, M. T., Klasky, M. L., and Ye, J. C. “Diffusion posterior sampling for general noisy inverse problems.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
- Song, Y., Shen, L., Xing, L., and Ermon, S. “Solving inverse problems in medical imaging with score-based generative models.” *ICLR* 2022. [arXiv:2111.08005](https://arxiv.org/abs/2111.08005).
- Rasht-Behesht, M., Huber, C., Shukla, K., and Karniadakis, G. E. “Physics-informed neural networks (PINNs) for wave propagation and full waveform inversions.” *JGR: Solid Earth* 127 (2022): e2021JB023120.
- Moseley, B., Markham, A., and Nissen-Meyer, T. “Finite basis physics-informed neural networks.” *Advances in Computational Mathematics* 49 (2023).
