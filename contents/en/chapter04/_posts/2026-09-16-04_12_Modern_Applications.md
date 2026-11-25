---
layout: post
title: "04-12 Modern Applications: Latent ODEs and Learned Linear Systems"
chapter: '04'
order: 12
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: optional
---

From predicting ICU patient trajectories measured at irregular hospital hours to processing million-token text sequences faster than Transformers, modern AI has rediscovered Chapter 04's linear systems at massive scale. **Latent ODEs**, **Koopman/DMD linearizations**, and **Structured State-Space Models (S4 / Mamba)** all rely on a single profound idea: lift messy, nonlinear observations into a higher-dimensional latent space where the dynamics evolve as a clean, diagonalizable linear system $$\mathbf{z}' = A\mathbf{z} + B\mathbf{u}(t)$$.

## Key ideas: Linear Systems Theory Inside Modern Sequence & Scientific AI

Four Chapter 04 pillars sit directly inside state-of-the-art machine learning architectures:

1. **Latent ODEs for Irregular Time Series:** Real clinical or sensor data arrive at uneven timestamps $$t_1, t_2, \dots$$; an encoder maps history into an initial latent state $$\mathbf{z}(0) \in \mathbb{R}^d$$, evolves $$\mathbf{z}' = f_\theta(\mathbf{z})$$ continuously to *any* query time $$t$$, and decodes predictions seamlessly across missing intervals.
2. **Koopman Operator & Dynamic Mode Decomposition (DMD):** Even a strongly nonlinear ODE $$\mathbf{x}' = \mathbf{f}(\mathbf{x})$$ becomes *strictly linear* when lifted to observable functions $$\mathbf{g}(\mathbf{x})$$; autoencoders learn the lifting map $$\mathbf{z} = \phi_\theta(\mathbf{x})$$ so latent dynamics obey $$\mathbf{z}' = A\mathbf{z}$$ and multi-step forecasting is just $$e^{At}\mathbf{z}_0$$!
3. **Diagonal State-Space Models (S4D / Mamba):** Restricting $$A = \operatorname{diag}(\lambda_1, \dots, \lambda_d)$$ with $$\operatorname{Re}(\lambda_k) < 0$$ eliminates expensive matrix exponentials completely: discretizing with Zero-Order Hold (ZOH) step $$\Delta$$ turns $$e^{A\Delta}$$ into an $$O(d)$$ elementwise exponential!
4. **Exact ZOH Discretization Formula:** Passing from continuous time $$\mathbf{z}' = A\mathbf{z} + B u$$ to discrete step $$\Delta$$ yields $$\mathbf{z}_{k+1} = \bar{A}\mathbf{z}_k + \bar{B}u_k$$ where $$\bar{A} = e^{A\Delta}$$ and $$\bar{B} = A^{-1}(e^{A\Delta} - I)B$$—pure Chapter 04 variation of parameters!

### Worked example: Computing Exact ZOH Discretization for a Diagonal State-Space Layer

Consider a 2-channel diagonal continuous state-space layer (as in S4D/Mamba) with
$$A = \begin{pmatrix} -1 & 0 \\ 0 & -4 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \qquad \mathbf{z}(0) = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$
driven by a piecewise-constant token input $$u(t) = u_0 = 3$$ on $$[0, \Delta]$$ with step size $$\Delta = 0.5$$.

1. **Compute the exact discrete transition matrix $$\bar{A} = e^{A\Delta}$$:**
   Because $$A$$ is diagonal,
   $$\bar{A} = \begin{pmatrix} e^{-0.5} & 0 \\ 0 & e^{-2} \end{pmatrix} \approx \begin{pmatrix} 0.6065 & 0 \\ 0 & 0.1353 \end{pmatrix}.$$
2. **Compute the exact discrete input matrix $$\bar{B} = \int_0^\Delta e^{As}B\,ds = A^{-1}(e^{A\Delta} - I)B$$:**
   - Channel 1 ($$\lambda_1 = -1, b_1 = 1$$): $$\bar{b}_1 = \frac{e^{-0.5} - 1}{-1}(1) = 1 - e^{-0.5} \approx 0.3935$$.
   - Channel 2 ($$\lambda_2 = -4, b_2 = 2$$): $$\bar{b}_2 = \frac{e^{-2} - 1}{-4}(2) = \frac{1 - e^{-2}}{2} \approx 0.4323$$.
3. **Update the latent state after one token $$u_0 = 3$$:**
   $$\mathbf{z}_1 = \bar{A}\mathbf{z}_0 + \bar{B}u_0 = \mathbf{0} + 3\begin{pmatrix} 0.3935 \\ 0.4323 \end{pmatrix} = \begin{pmatrix} 1.1805 \\ 1.2970 \end{pmatrix}.$$
4. **Compare memory horizons of the two eigenvalues:**
   Channel 1 ($$\lambda_1 = -1$$, retention $$60.7\%$$ per step) acts as **long-term memory**, while Channel 2 ($$\lambda_2 = -4$$, retention $$13.5\%$$ per step) acts as a **fast local filter**—showing how eigenvalues directly govern receptive fields in modern AI!

## Objectives

This optional lesson connects matrix systems, eigenvalues, and fundamental matrices to latent neural ODEs and modern system-identification models. Students should be able to read a latent ODE as a hidden linear or nonlinear system, explain why eigenvalue structure still governs long-time behavior, and locate the 2019–2022 papers that turned continuous-time state space models into a standard deep-learning tool. The eigenvalue methods of the chapter are not replaced.

## Prerequisites

Students should know how to write a first-order system $$\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$$, compute eigenvalues and eigenvectors, form $$e^{At}$$, and read a linear phase portrait. Compartment models from the last required lesson are the ideal running example.

## Introduction

A system of ODEs is the native language of interacting quantities: coupled oscillators, tanks in series, and epidemiological compartments. The same language is now used inside neural networks. Rubanova, Chen, and Duvenaud (*Latent ODEs for Irregularly-Sampled Time Series*, NeurIPS 2019) encode an irregular sequence into a hidden initial state, then generate the future by integrating a neural ODE in that latent space. The observed series is a readout of a continuous-time system that the network never writes down in closed form, but that still has a Jacobian, a spectrum, and a phase portrait.

Kidger’s 2022 survey ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) and the Neural CDE paper (Kidger, Morrill, Foster, and Lyons, ICLR 2021) extended the idea from autonomous latent fields to systems driven by an input path. In parallel, the SciML community around Diffrax and DiffEqFlux treated mechanistic systems and neural systems as interchangeable objects: one may freeze a known matrix $$A$$ and learn only a forcing, or learn the entire field. The chapter’s matrix exponential is the exact solution of the linear special case, and therefore the first diagnostic for any of these models.

## Key Concepts

### Latent state space

A latent ODE is a system

$$
\mathbf{z}'=f_\theta(\mathbf{z}),\qquad \mathbf{x}(t)=g_\phi\bigl(\mathbf{z}(t)\bigr),
$$

where $$\mathbf{x}$$ is observed and $$\mathbf{z}$$ is hidden. If $$f_\theta(\mathbf{z})\approx A\mathbf{z}$$ near an equilibrium, the classification already proved in this chapter applies verbatim: real negative eigenvalues give nodal decay, complex eigenvalues with negative real part give spirals, a zero eigenvalue signals a line of equilibria or a conservation law. Training that ignores this spectrum can fit the observations and still be internally unstable.

### Fundamental matrices and linearizations

The fundamental matrix $$\Phi(t)=e^{At}$$ maps an initial condition to the state at time $$t$$. In a latent linear model the same object is a learned state-transition operator. For a nonlinear latent field the local fundamental matrix is the state-transition matrix of the variational equation $$\mathbf{v}'=Df_\theta(\mathbf{z}(t))\mathbf{v}$$. That is precisely the linearization used to draw phase portraits, now computed automatically by differentiating the solver.

### Inputs, control, and Neural CDEs

Nonhomogeneous systems $$\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$$ are the classical way to add forcing. Neural CDEs replace $$\mathbf{g}(t)\,dt$$ by a controlled increment $$f_\theta(\mathbf{z})\,dX(t)$$, which is the right model when the input is a measured path rather than a prescribed function of time. Variation of parameters remains the conceptual solution formula: the homogeneous system transports the effect of each increment forward with $$\Phi(t)\Phi(s)^{-1}$$.

### Identifiability of compartments

Pharmacokinetic and epidemiological compartment models are only identifiable up to certain similarities. The same ambiguity appears in latent ODEs: if $$P$$ is invertible, $$\mathbf{w}=P\mathbf{z}$$ yields an equivalent system with matrix $$PAP^{-1}$$. Eigenvalues are invariant; eigenvectors and compartment meanings are not. A modern paper that reports a latent trajectory without discussing this gauge freedom is leaving out a fact this chapter already knows.

## Methods and Solution Techniques

A practical identification workflow uses the chapter as a checklist.

1. Fit a latent ODE or a linear state-space model to the series.
2. Linearize the learned field at the inferred equilibrium or operating point.
3. Compute eigenvalues and compare them with the time scales visible in the data.
4. If the application is a compartment model, test whether the spectrum, not the particular basis, is stable across random seeds.
5. For driven systems, compare the learned response with variation of parameters on the linearized system.

Software: `torchdiffeq` for PyTorch latent ODEs; Diffrax for JAX, including CDEs; the SciML stack in Julia for hybrid mechanistic–neural systems. In all three, the solver returns a trajectory of a system, not a stack of unrelated discrete layers.

## Examples

### Example 1: Two-tank latent recovery

A pair of mixing tanks is a linear system whose eigenvalues are real and negative. If one observes only the downstream concentration, a latent ODE with two hidden dimensions should recover those two time scales, even if the learned coordinates are a rotation of the physical compartments. Plotting the eigenvalues across training seeds is more informative than plotting the hidden trajectories.

### Example 2: Coupled oscillators and normal modes

Two coupled springs have a pair of imaginary eigenvalue pairs, corresponding to normal modes. A latent model trained on the sum of the two positions can recover the frequencies and still mix the mode shapes. The chapter’s normal-mode calculation is the reference: frequencies are spectral invariants, shapes are basis-dependent.

### Example 3: Linear latent ODE in code

```python
import torch
from torchdiffeq import odeint

A = torch.tensor([[-1.0, 1.0], [0.0, -2.0]])

def f(t, z):
    return z @ A.T

z0 = torch.tensor([1.0, 1.0])
t = torch.linspace(0.0, 4.0, 41)
zt = odeint(f, z0, t)
print(zt[-1])
```

Replacing $$A$$ by a small network turns this into a latent ODE. The first thing to print after training is still the spectrum of the Jacobian at equilibrium.

## Applications in Science, Engineering, and Modern Contexts

Latent ODEs are used in electronic health records, wearable sensors, climate time series, and neural population recordings—anywhere samples are irregular and the hidden state is a low-dimensional dynamical system. In engineering they sit next to classical Kalman filtering and subspace identification: the new ingredient is a nonlinear latent field trained end-to-end. Epidemiology is an especially honest test. An SIR-like latent system should not be celebrated for a low reconstruction error if its Jacobian at the disease-free equilibrium has the wrong spectral sign, because that sign is the basic reproduction number in linearized form.

The 2021–2022 CDE and rough-DE papers added a second application axis: systems driven by irregular controls, trades, or stimuli. That is the modern version of a nonhomogeneous linear system, and variation of parameters is still the reason the construction works.

## Challenges and Extensions

Latent dimension is a hyperparameter with no analogue of a computed Jordan form: too small and modes are lost, too large and the extra eigenvalues become unidentified and often unstable. Stiffness appears as soon as time scales separate, exactly as in a stiff linear system. Discrete observations leave a continuous system underdetermined. Finally, a learned nonlinear field can have spurious attractors far from the data, so extrapolation is a phase-portrait question, not a loss-function question.

A useful prompt: if two latent systems share eigenvalues but not eigenvectors, which scientific conclusions remain valid? The chapter’s answer is: those that depend on the similarity class of $$A$$, not on a preferred basis.

## Video tham khảo

- xem trước: [Latent Stochastic Differential Equations for Irregularly-Sampled Time Series - David Duvenaud](https://www.youtube.com/watch?v=93wr5vhI0F4) — Institute for Advanced Study, English. David Duvenaud on latent stochastic differential equations for irregular time series.
- [Neural ODEs (NODEs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=nJphsM4obOk) — Steve Brunton, English. Neural ODEs, the deterministic latent-dynamics model this lesson is extending.
- [Solving Systems of Differential Equations with Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=Zwb5eiYcL8w) — Steve Brunton, English. Classical linear systems, the structure a learned linear latent model is trying to recover.

## Exercises

1. **Similarity invariance.** Show that $$A$$ and $$PAP^{-1}$$ generate equivalent trajectories up to the change of coordinates $$\mathbf{w}=P\mathbf{z}$$. Which quantities in a latent-ODE paper should therefore be reported?

2. **Observed-output rank.** For $$\mathbf{x}'=A\mathbf{x}$$, $$y=c^\top\mathbf{x}$$, explain when a single scalar output can still recover the spectrum of $$A$$. Relate the answer to observability.

3. **Variation of parameters as a decoder.** Write the solution of $$\mathbf{z}'=A\mathbf{z}+B\mathbf{u}(t)$$ and interpret $$B\mathbf{u}(t)$$ as a Neural-CDE increment. What role does $$e^{A(t-s)}$$ play?

4. **Computational experiment.** Fit a two-dimensional linear latent ODE to samples of a two-tank system in which only the second tank is observed. Compare learned eigenvalues with the true ones across five random seeds.

5. **Open exploration.** Read Rubanova, Chen, and Duvenaud (NeurIPS 2019) and sketch the encoder–decoder diagram next to a classical compartment figure. Where is $$e^{At}$$ hiding?

## References

- Boyce, W. E., and DiPrima, R. C. *Elementary Differential Equations*, Chapter 7; Arnold, *Ordinary Differential Equations*, Chapters 1–3.
- Rubanova, Y., Chen, R. T. Q., and Duvenaud, D. “Latent ordinary differential equations for irregularly-sampled time series.” *NeurIPS* 2019. [arXiv:1907.03907](https://arxiv.org/abs/1907.03907).
- Kidger, P., Morrill, J., Foster, J., and Lyons, T. “Neural controlled differential equations for irregular time series.” *ICLR* 2021. [arXiv:2005.08926](https://arxiv.org/abs/2005.08926).
- Kidger, P. *On Neural Differential Equations*. University of Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
- Chen, R. T. Q., et al. `torchdiffeq`. [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq). Kidger, P. Diffrax. [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
