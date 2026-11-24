---
layout: post
title: "03-10 Modern Applications: Laplace Neural Operators and Learned Transfer Functions"
chapter: '03'
order: 10
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: optional
---

Fourier Neural Operators (FNOs) revolutionized scientific machine learning by learning PDEs in the frequency domain, yet they carry an Achilles' heel: the Fourier transform assumes periodic signals and struggles with abrupt transients, step inputs, or decaying non-periodic responses. **Laplace Neural Operators (LNOs)** and modern **Structured State-Space Models (S4 / Mamba)** overcome this exact barrier by parameterizing learned layers directly as rational transfer functions—poles and residues in the complex $$s$$-plane!

## Background Knowledge Map: Classical Laplace Theory Inside Modern AI Architectures

Four concepts from Chapter 03 map directly onto cutting-edge neural operators and sequence models:

1. **Laplace Neural Operators (Pole–Residue Parameterization):** Instead of learning discrete Fourier modes on $$i\omega$$, an LNO learns a finite set of complex poles $$\mu_k \in \mathbb{C}$$ and residues $$\beta_k$$ representing $$H_\theta(s) = \sum_k \frac{\beta_k}{s - \mu_k}$$, naturally capturing both transient decay ($$\operatorname{Re}\mu_k < 0$$) and steady-state oscillation!
2. **Continuous-Time Convolution Kernels (S4 / HiPPO):** Long-sequence models like S4 represent a layer as a continuous LTI system $$\mathbf{x}' = A\mathbf{x} + B u,\; y = C\mathbf{x}$$, compute its exact transfer function $$H(s) = C(sI - A)^{-1}B$$, and execute training via fast FFT convolution while running inference in $$O(1)$$ recurrent time!
3. **Stability by Architectural Construction:** Enforcing $$\operatorname{Re}(\mu_k) < 0$$ (e.g., via $$\mu_k = -\operatorname{softplus}(\alpha_k) + i\omega_k$$) mathematically guarantees BIBO stability across arbitrarily long rollouts, preventing exploding activations.
4. **Handling Discontinuous Forcing:** Because Laplace transforms natively encode step switches and impulses via $$e^{-cs}$$, LNOs outperform pure Fourier surrogates on impact mechanics, switched circuits, and transient heat shocks.

### Step-by-Step Worked Example (Read Slowly): Evaluating a 2-Pole Learned Transfer Function on a Step Input

Suppose a trained 2-pole Laplace Neural Operator layer has learned a conjugate-symmetric pole–residue pair with poles $$p_{1,2} = -2 \pm 4i$$ and residues $$\beta_{1,2} = 1 \mp \frac{1}{2}i$$:
$$H_\theta(s) = \frac{1 - \frac{1}{2}i}{s - (-2 + 4i)} + \frac{1 + \frac{1}{2}i}{s - (-2 - 4i)}.$$

1. **Combine the conjugate pole–residue pair into a real rational transfer function:**
   Common denominator: $$(s + 2 - 4i)(s + 2 + 4i) = (s + 2)^2 + 16 = s^2 + 4s + 20$$.
   Numerator:
   $$\left(1 - \frac{1}{2}i\right)(s + 2 + 4i) + \left(1 + \frac{1}{2}i\right)(s + 2 - 4i) = 2(s + 2) + 2\left(\frac{1}{2}\cdot 4\right) = 2s + 8.$$
   So $$H_\theta(s) = \frac{2s + 8}{(s + 2)^2 + 16}$$.
2. **Verify BIBO stability and compute the learned impulse response $$h_\theta(t)$$:**
   Both poles have $$\operatorname{Re}(p) = -2 < 0 \implies$$ **strictly BIBO stable**.
   Rewrite numerator as $$2(s + 2) + 4 = 2(s + 2) + 1\cdot 4$$:
   $$h_\theta(t) = \mathcal{L}^{-1}\{H_\theta(s)\} = e^{-2t}\bigl(2\cos 4t + \sin 4t\bigr).$$
3. **Predict the steady-state output to a unit step input $$u(t) = u_0(t)$$ ($$U(s) = 1/s$$):**
   By the Final Value Theorem (valid since all poles of $$sY(s) = H_\theta(s)$$ have $$\operatorname{Re}(s) < 0$$):
   $$\lim_{t\to\infty} y(t) = \lim_{s\to 0} s\cdot\frac{H_\theta(s)}{s} = H_\theta(0) = \frac{8}{20} = \mathbf{0.4}.$$
   Every single learned parameter $$(\mu_k, \beta_k)$$ has an exact, inspectable physical meaning!

## Objectives

This optional lesson shows how the Laplace transform, convolution, and transfer-function viewpoint of the chapter reappear in 2023–2024 operator-learning models, especially the Laplace neural operator. Students should be able to interpret a learned pole–residue layer as a data-driven transfer function, compare Laplace and Fourier operator learning, and explain why discontinuous forcing remains a natural test for both classical and learned solvers. The transform tables and inversion techniques already developed are left intact.

## Prerequisites

Students should know the definition of the Laplace transform, transforms of elementary functions, partial-fraction inversion, the convolution theorem, and the idea of a transfer function $$G(s)=Y(s)/U(s)$$ for a linear IVP.

## Introduction

The Laplace transform converts a linear initial-value problem into algebra. A derivative becomes multiplication by $$s$$, a convolution becomes a product, and a transfer function encodes the entire input–output map. That algebraic picture is so efficient that it was natural to ask whether a neural operator should work in the same domain.

Cao, Goswami, and Karniadakis introduced the Laplace neural operator (LNO) in 2023 ([arXiv:2303.10528](https://arxiv.org/abs/2303.10528)) and published the journal version in *Nature Machine Intelligence* in 2024 ([https://doi.org/10.1038/s42256-024-00844-4](https://doi.org/10.1038/s42256-024-00844-4)). LNO learns poles and residues in the Laplace domain, so a single layer can represent transient as well as steady response and can handle non-periodic inputs that a Fourier neural operator treats awkwardly. The construction is a learned analogue of the partial-fraction expansion already practiced in this chapter.

At the same time, Fourier neural operators (Li et al., ICLR 2021) and the broader neural-operator theory of Kovachki et al. (*JMLR* 2023) showed that spectral multipliers are a powerful way to learn maps between function spaces. The Laplace viewpoint is the natural counterpart for causal, one-sided-in-time dynamics: exactly the setting in which this chapter prefers Laplace to Fourier.

## Key Concepts

### Poles, residues, and learned transfer functions

For a linear system the transfer function is a rational function

$$
G(s)=\sum_{n}\frac{\beta_n}{s-\mu_n},
$$

up to polynomial terms. An LNO layer treats $$\mu_n$$ and $$\beta_n$$ as trainable parameters, then maps an input history to an output history through that pole–residue calculus. The student who has inverted $$Y(s)=G(s)U(s)$$ by partial fractions already understands the layer: learning replaces table lookup. The payoff is interpretability. A pole near the imaginary axis is a slowly decaying mode; a pair of complex poles is an oscillation; a pole in the right half-plane is an unstable mode that a control engineer would immediately reject.

### Convolution as the time-domain counterpart

The convolution theorem says that multiplication by $$G(s)$$ is convolution with the impulse response $$g(t)=\mathcal{L}^{-1}\{G(s)\}$$. A learned Laplace layer is therefore a structured convolutional operator whose kernel is a sum of exponentials and damped sinusoids—the same family that appears when one inverts elementary transforms. This is a much stronger inductive bias than a generic temporal convolution, and it is why LNO can outperform Fourier layers on transients and on signals that are not periodic.

### Discontinuous and impulsive inputs

Step and delta forcing were the classical reasons to prefer Laplace methods. They remain a revealing benchmark for learned solvers. A Fourier model on a periodic window smears a jump into Gibbs oscillations; a Laplace model that owns one-sided causality can keep the jump and then decay through the correct modes. Wang, Sankaran, and Perdikaris (*Computer Methods in Applied Mechanics and Engineering*, 2024; [https://doi.org/10.1016/j.cma.2024.116813](https://doi.org/10.1016/j.cma.2024.116813)) showed, in the PINN setting, that ignoring temporal causality is a training pathology. The same warning applies to operator learning: a spectral model that treats time as just another periodic coordinate can violate the causal structure that Laplace encodes by construction.

### From IVPs to parametric families

Classical Laplace methods solve one IVP. Operator learning solves a family: many forcings, many initial states, many coefficients. The Laplace domain is still the right place to share structure across the family, because the poles of a linear device do not depend on the particular input. That is why a single learned transfer function can be reused, just as one reuses $$G(s)$$ in a block diagram.

## Methods and Solution Techniques

A comparison of three modern pipelines is enough to locate LNO.

- **PINN in the time domain.** Represent $$y_\theta(t)$$ and penalize $$y'-f(t,y)$$. Best for a single instance, awkward for a large family of inputs.
- **Fourier neural operator.** Multiply by learned complex weights in the Fourier domain. Excellent for periodic or statistically stationary fields, weaker on transients and one-sided initial conditions.
- **Laplace neural operator.** Multiply by a learned pole–residue symbol. Natural for causal linear and weakly nonlinear oscillators, beams, and diffusion.

The classical inversion workflow remains the debugging tool. If an LNO layer reports poles $$\mu_n$$, one should invert the corresponding rational function by hand and compare the impulse response with the network’s response to an approximate delta. If they disagree, the layer is not doing the Laplace calculus it claims to do.

## Examples

### Example 1: Recovering an RC transfer function

For $$y'+y=u(t)$$ one has $$G(s)=1/(s+1)$$. Training LNO on several smooth inputs should recover a pole near $$-1$$. The test is then the step response $$1-e^{-t}$$, which this chapter already computes by hand. Agreement on the step, not on the training inputs, is the evidence that the learned object is a transfer function.

### Example 2: Why Fourier layers struggle with a causal step

A step $$u(t)=H(t)$$ is not periodic. Periodizing it on $$[0,T]$$ introduces a jump at the identified endpoints and a Gibbs-contaminated spectrum. A Laplace representation never periodizes in time; it encodes the same jump as a factor $$1/s$$. The example is elementary and already in the chapter, but it is the right mental picture for the 2024 LNO experiments on transients.

### Example 3: Impulse response as a unit test

```python
import numpy as np
from scipy.signal import dlti, dimpulse

# Discrete stand-in for G(s) = 1/(s+1) after a simple mapping
sys = dlti([0.1], [1, -np.exp(-0.1)])
t, y = dimpulse(sys, n=40)
print(np.array(y[0][:5]).ravel())
```

A learned Laplace layer should be subjected to the same test: feed an approximate impulse, read the output, and compare with $$\mathcal{L}^{-1}\{G(s)\}$$.

## Applications in Science, Engineering, and Modern Contexts

Learned transfer functions are immediately useful in structural dynamics, control, and reduced-order modeling. Cao, Goswami, and Karniadakis demonstrated LNO on Duffing and pendulum oscillators, on an Euler–Bernoulli beam, and on diffusion and reaction–diffusion equations—precisely the catalog of linear and weakly nonlinear devices that a Laplace-transform course already treats as canonical. In engineering practice the attraction is real-time evaluation: once the poles and residues are learned, evaluating a new forcing is a cheap residue calculus rather than a new time-stepping run. The same idea appears in floating-structure response and in large-scale Rossby-wave surrogates discussed in the LNO papers.

Control students can read LNO as a data-driven Bode or pole-zero model. The classical caution still applies: a pole estimated from short, noisy records can wander into the right half-plane. Laplace theory tells one what would then happen; learning does not repeal that conclusion.

## Challenges and Extensions

Nonlinear systems do not have a single transfer function. LNO, like classical harmonic linearization, can still be useful, but poles then depend on amplitude and operating point. Identification from limited data is ill-posed: many rational functions share similar responses on a short interval. Fourier and Laplace biases can also be combined, and the 2023–2025 operator-learning literature is actively exploring hybrid spectral layers. Finally, discontinuous forcing remains theoretically delicate for neural models because networks are typically smooth; a good Laplace prior does not automatically restore jump regularity.

What does it mean, then, to “learn $$G(s)$$” if the true system is only approximately linear? The chapter’s convolution theorem suggests a test: if the learned model fails to turn products in $$s$$ into convolutions in $$t$$, it is not a transfer function, however small the training error.

## Video tham khảo

- xem trước: [Control Systems Lectures - Transfer Functions](https://www.youtube.com/watch?v=RJleGwXorUk) — Brian Douglas, English. Classical transfer functions, the object a learned Laplace-domain layer is imitating.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, English. A Fourier neural operator is the closest public lecture on learning an input-output operator.
- [The Laplace Transform and the Important Role it Plays](https://www.youtube.com/watch?v=VJ9phDRys_I) — Brian Douglas, English. The Laplace transform itself, so the learned model stays tied to a causal linear system.

## Exercises

1. **Pole-residue inversion.** Let $$G(s)=(s+3)/((s+1)(s+2))$$. Invert by partial fractions and sketch the impulse response. Which features should a learned Laplace layer recover?

2. **Step versus harmonic probing.** Explain why fitting $$G(s)$$ only on sinusoidal inputs can hide an incorrect residue at a real pole. Design a training set that would expose the error.

3. **Causality.** Show that a non-causal kernel $$g(-t)$$ cannot arise as $$\mathcal{L}^{-1}\{G(s)\}$$ for a proper rational $$G$$ with left-half-plane poles. How would you detect a causality violation in a trained operator?

4. **Computational experiment.** Using SciPy’s signal tools or a small PyTorch pole-residue layer, fit $$G(s)=1/(s^2+2s+2)$$ from several input–output pairs and then predict the response to a square wave. Compare with the classical Laplace solution.

5. **Open exploration.** Read the LNO paper (2023/2024) and write a one-page comparison with the Fourier neural operator: for which problems in this chapter is Laplace the more honest inductive bias?

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*, Chapter 6; Zill, Chapter 7.
- Cao, Q., Goswami, S., and Karniadakis, G. E. “LNO: Laplace neural operator for solving differential equations.” [arXiv:2303.10528](https://arxiv.org/abs/2303.10528) (2023); *Nature Machine Intelligence* (2024). [https://doi.org/10.1038/s42256-024-00844-4](https://doi.org/10.1038/s42256-024-00844-4).
- Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., and Anandkumar, A. “Fourier neural operator for parametric partial differential equations.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
- Kovachki, N., et al. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, no. 89 (2023): 1–97.
- Wang, S., Sankaran, S., and Perdikaris, P. “Respecting causality for training physics-informed neural networks.” *Computer Methods in Applied Mechanics and Engineering* 421 (2024): 116813.
