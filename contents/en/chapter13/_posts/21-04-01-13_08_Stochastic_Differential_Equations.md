---
layout: post
title: "13-08 Stochastic Differential Equations"
chapter: '13'
order: 8
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: optional
---

> **Storytelling Hook:** Watch a pollen grain jittering under a microscope or a stock price zigzagging across a trading screen: its path is continuous everywhere yet differentiable *nowhere*, because random kicks scale like $\sqrt{dt}$ rather than $dt$. That square-root scaling breaks ordinary calculus—giving birth to **Itô's Lemma** and **Stochastic Differential Equations (SDEs)**.

## Learning Objectives

This lesson introduces stochastic differential equations and the Euler-Maruyama method. Students should understand why randomness enters differential models, how stochastic increments differ from deterministic time steps, and why numerical simulation remains essential in this setting.

## Prerequisites

Students should know deterministic ODE methods and have some familiarity with random variables and Brownian motion at an intuitive level.

## Key ideas: Calculus and Numerics Driven by Brownian Motion

Four core ideas bridge deterministic ODEs to stochastic differential equations $dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t$:

1. **Brownian Motion and Quadratic Variation $(dW_t)^2 = dt$:** Increments $\Delta W_t = W_{t+\Delta t} - W_t \sim \mathcal{N}(0, \Delta t)$ are independent with standard deviation $\sqrt{\Delta t}$. Summing $(\Delta W_k)^2$ over a partition does *not* vanish—it converges to $T$, generating a mandatory second-order correction in the chain rule.
2. **Itô's Lemma:** For a smooth function $f(X_t)$, Taylor expanding to second order yields $df(X_t) = \big(f'\mu + \frac{1}{2}f''\sigma^2\big)\,dt + f'\sigma\,dW_t$. That extra $\frac{1}{2}f''\sigma^2\,dt$ drift separates Itô calculus from classical calculus.
3. **Euler–Maruyama and Milstein Discretization:** Replacing $dt \to \Delta t$ and $dW_t \to \sqrt{\Delta t}\,Z_n$ ($Z_n \sim \mathcal{N}(0,1)$) gives Euler–Maruyama, which achieves **strong order $1/2$** (pathwise) and **weak order $1$** (in expectation); adding the Milstein term $\frac{1}{2}\sigma\sigma'((\Delta W_n)^2 - \Delta t)$ lifts strong convergence to order $1$.
4. **Fokker–Planck (Kolmogorov Forward) Bridge to PDEs:** While individual trajectories $X_t$ are random, their probability density $p(x,t)$ evolves deterministically via the parabolic PDE $\partial_t p = -\partial_x(\mu p) + \frac{1}{2}\partial_{xx}(\sigma^2 p)$.

## Introduction

![Stochastic differential equations]({{ site.imgurl }}/chapter_img/chapter13/08_stochastic_differential_equations.svg)

Many systems evolve not only under deterministic laws but also under persistent random influence. Financial prices, molecular motion, noisy control systems, and ecological fluctuations all motivate differential models with randomness built into the dynamics.

Stochastic differential equations extend ordinary differential equations by adding noise terms, and their numerical treatment requires new ideas beyond standard deterministic stepping.

## Concept in Three Ways

### Intuitive View

An SDE describes a system that has both a drift trend and a random fluctuation. The future is shaped by law and noise simultaneously.

### Visual View

Instead of a single smooth trajectory, one observes many sample paths that fluctuate around a general trend.

### Formal View

A basic SDE may be written symbolically as
$$ dX_t = a(X_t,t)\,dt + b(X_t,t)\,dW_t, $$
where $$ W_t $$ is Brownian motion. The Euler-Maruyama method replaces the stochastic increment by simulated Gaussian steps.

## Why the Topic Matters

Stochastic differential equations show how numerical differential equations extend into random systems. They are a natural culmination of the chapter because they demonstrate that numerical thinking remains essential even when exact deterministic trajectories no longer exist.

They also connect differential equations to probability in a very concrete way.

## Common Misconceptions

### "An SDE is just an ODE with a random parameter"

No. The noise enters continuously through stochastic increments.

### "Ordinary Euler works unchanged for SDEs"

No. Stochastic increments require modified numerical interpretation.

### "Randomness destroys all structure"

No. Drift, diffusion, and statistical properties still organize the problem strongly.

## Suggested Learning Path

### Step 1: Motivate noisy dynamics

Students should begin from applications where deterministic models are too idealized.

### Step 2: Introduce the drift-plus-noise structure

This is the conceptual heart of an SDE.

### Step 3: Present Euler-Maruyama

This gives a computational starting point analogous to Euler's method.

### Step 4: Compare sample paths and deterministic trajectories

This highlights the new nature of the problem.

### Checkpoints

- Can students explain the difference between deterministic drift and stochastic fluctuation?
- Do they understand why stochastic increments are not ordinary derivatives?
- Can they describe the idea behind Euler-Maruyama simulation?

## Worked Examples


### Worked example: Itô's Lemma and One Euler–Maruyama Step for Geometric Brownian Motion

Solve the geometric Brownian motion SDE $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ analytically using Itô's Lemma, then compare the exact value after one step against Euler–Maruyama for $S_0 = 100$, $\mu = 0.05$, $\sigma = 0.2$, $\Delta t = 0.25$, and random draw $Z_0 = +1$ (so $\Delta W_0 = \sqrt{0.25}(1) = 0.5$).

1. **Apply Itô's Lemma to $f(S) = \ln S$:** Compute $f'(S) = \frac{1}{S}$ and $f''(S) = -\frac{1}{S^2}$. Then:
   $$d(\ln S_t) = \frac{1}{S_t}(\mu S_t\,dt + \sigma S_t\,dW_t) + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)(\sigma^2 S_t^2\,dt) = \left(\mu - \frac{1}{2}\sigma^2\right)dt + \sigma\,dW_t.$$
   Integrating from $0$ to $t$ yields the exact solution:
   $$S_t = S_0 \exp\!\left[\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right].$$
   Notice the Itô drag $-\frac{1}{2}\sigma^2$: volatility lowers the median growth rate!
2. **Evaluate the exact solution at $t_1 = 0.25$ with $W_{0.25} = 0.5$:**
   $$\mu - \frac{1}{2}\sigma^2 = 0.05 - \frac{1}{2}(0.04) = 0.03, \qquad S_{0.25}^{\text{exact}} = 100\exp\big(0.03(0.25) + 0.2(0.5)\big) = 100 e^{0.1075} \approx 111.349.$$
3. **Compute one Euler–Maruyama step:**
   $$S_1^{\text{EM}} = S_0 + \mu S_0 \Delta t + \sigma S_0 \Delta W_0 = 100\big(1 + 0.05(0.25) + 0.2(0.5)\big) = 100(1.1125) = 111.250.$$
   Notice that adding the Milstein correction $\frac{1}{2}\sigma^2 S_0((\Delta W_0)^2 - \Delta t) = \frac{1}{2}(0.04)(100)(0.25 - 0.25) = 0$ happens to vanish when $Z_0 = \pm 1$, leaving $S_1^{\text{EM}}$ within $0.09\%$ of the exact sample path!

### Example 1: Noisy Exponential Growth

A deterministic growth law perturbed by noise gives fluctuating sample paths rather than one predictable curve.

### Example 2: Brownian-Driven Motion

The random increment produces irregular sample paths even when the drift is simple.

### Example 3: Monte Carlo Viewpoint

Many sample paths may be simulated and compared statistically rather than expecting one exact deterministic answer.

## Conceptual Questions

1. Why is noise modeled through stochastic increments rather than ordinary forcing alone?
2. Why does stochastic simulation focus on sample paths and statistics?
3. How does Euler-Maruyama generalize Euler's method conceptually?

## Application Problems

1. Why are SDEs natural in finance and molecular modeling?
2. Why is a single simulation path not the whole story in stochastic computation?
3. How does randomness change the meaning of prediction in differential equations?

## Interactive Teaching Strategies

- Compare one deterministic trajectory with many noisy sample paths.
- Ask students to identify drift and diffusion terms in sample models.
- Reinforce that numerical simulation is central because explicit formulas are often unavailable.
- Use simple Brownian-motion intuition before technical stochastic calculus language.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the conceptual meaning of noise and the drift-plus-randomness picture before technical formulas.

### Challenge for Advanced Students

Advanced students can explore weak versus strong convergence, Ito interpretation, or geometric Brownian motion.

## Summary

Stochastic differential equations extend differential modeling into random environments. The Euler-Maruyama method provides the first practical numerical tool, and the topic opens the door from deterministic computation to probabilistic dynamics.

> See the full gallery of chapter interactives here: [Chapter 13 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter13/13_09_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Financial markets
- Problem: Asset prices are driven by random fluctuations, not only deterministic trends.
- Model:
$$ dX_t=\mu X_t\,dt+\sigma X_t\,dW_t. $$
- Assumptions and limitations: Brownian motion is an idealization; real data may have jumps and changing volatility.
- Interpretation: SDEs inject randomness directly into the dynamics.

#### Brownian motion and diffusion
- Problem: A small particle in a fluid experiences continuous random kicks.
- Model: Use an SDE such as a Langevin model or geometric Brownian motion.
- Assumptions and limitations: White Gaussian noise is still an approximation.
- Interpretation: SDEs connect ODEs to probability and to PDEs such as Fokker-Planck equations.

### 2. Additional Intuition and Connections

SDEs replace ordinary differentials by a deterministic part and a stochastic part. Because Brownian paths are nowhere classically differentiable, Itô calculus replaces ordinary calculus. A common pitfall is to treat $$ dW_t $$ like an ordinary differential and miss Itô-specific effects.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
T, N = 1.0, 800
dt = T / N
t = np.linspace(0, T, N + 1)
mu, sigma, X0 = 0.3, 0.6, 1.0
dW = np.sqrt(dt) * np.random.randn(N)
X = np.zeros(N + 1)
X[0] = X0

for n in range(N):
    X[n + 1] = X[n] + mu * X[n] * dt + sigma * X[n] * dW[n]

plt.plot(t, X)
plt.title("One Euler-Maruyama sample path")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Euler Maruyama simulation visualization
- search: geometric Brownian motion sample paths
- search: Ito calculus intuition Brownian motion

### 4a. Interactive Web Illustration

{% include interactive-frame.html title="Euler-Maruyama for geometric Brownian motion" description="Generate many sample paths to distinguish a single stochastic trajectory from the average behavior of the system." path="interactives/chapter13/sde-euler-maruyama-en.html" height="660px" %}

### 5. Worked Example

For geometric Brownian motion
$$ dX_t=\mu X_t\,dt+\sigma X_t\,dW_t, $$
the Euler-Maruyama scheme is
$$
X_{n+1}=X_n+\mu X_n \Delta t+\sigma X_n \Delta W_n,
$$
where
$$ \Delta W_n \sim \mathcal{N}(0,\Delta t). $$
This is the stochastic analogue of forward Euler.

### 6. Difficulty Layering

**Undergraduate level.** Understand sample paths, Brownian noise, and Euler-Maruyama.

**Graduate level.** Connect to Itô's formula, strong/weak convergence, and Fokker-Planck equations.

## Video tham khảo

- xem trước: [21. Stochastic Differential Equations](https://www.youtube.com/watch?v=qdbkvD4N-us) — MIT OpenCourseWare, English. MIT 18.S096 introduces stochastic differential equations.
- [Lecture 24: Stochastic Calculus](https://www.youtube.com/watch?v=5cruqmIF6l0) — MIT OpenCourseWare, English. The stochastic calculus those equations are written in.
- [Latent Stochastic Differential Equations for Irregularly-Sampled Time Series - David Duvenaud](https://www.youtube.com/watch?v=93wr5vhI0F4) — Institute for Advanced Study, English. A research lecture on latent SDEs, the data-driven use of the same object.

## References

- Kloeden & Platen: standard reference for stochastic numerical methods.
