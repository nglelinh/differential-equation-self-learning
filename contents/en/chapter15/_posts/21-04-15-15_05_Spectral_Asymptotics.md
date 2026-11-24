---
layout: post
title: "Spectral Asymptotics"
chapter: '15'
order: 5
owner: Lê Minh Hoàng
lang: en
categories:
- chapter15
lesson_type: optional
---

> **Storytelling Hook:** In 1911, physicist Hendrik Lorentz posed a haunting question during a Göttingen lecture: does the high-frequency distribution of resonant tones inside an arbitrarily shaped room depend on the room's intricate geometry, or *only* on its total volume? Just months later, Hermann Weyl proved his celebrated **Weyl Law**, launching the modern field of spectral geometry and Mark Kac's famous question: *"Can one hear the shape of a drum?"*

![Spectral asymptotics and eigenvalue counting]({{ site.imgurl }}/chapter_img/chapter15/05_spectral_asymptotics.svg )

## Objectives

This optional lesson introduces spectral asymptotics, especially Weyl's law, as the bridge between high-energy spectra, geometry, and microlocal analysis. After the lesson, students should understand the meaning of the eigenvalue counting function, the intuition behind Weyl's law, and why large spectra reflect phase-space volume rather than just a list of numbers.

## Prerequisites

Students should know eigenvalue problems, the Laplacian, Hilbert spaces, and the semiclassical intuition that large eigenvalues correspond to high frequency. Chapter 12 on spectral theory provides useful background.

## Background Knowledge Map: Counting Eigenvalues via Phase-Space Volume

Four pillars connect the spectrum $0 < \lambda_1 \le \lambda_2 \le \dots$ of $-\Delta$ on a bounded domain $\Omega \subset \mathbb{R}^d$ to its geometry:

1. **Eigenvalue Counting Function $N(\lambda) = \#\{k : \lambda_k \le \lambda\}$:** Weyl's leading law states $N(\lambda) \sim (2\pi)^{-d}\omega_d \operatorname{Vol}(\Omega)\,\lambda^{d/2}$ as $\lambda \to \infty$ (where $\omega_d$ is the unit ball volume in $\mathbb{R}^d$)—matching the semiclassical heuristic "one quantum state per $(2\pi)^d$ of phase-space volume $\{|\xi|^2 \le \lambda\}$."
2. **Dirichlet–Neumann Bracketing (Courant's Variational Proof):** Tiling $\Omega$ by tiny cubes and sandwiching $-\Delta$ between Dirichlet (lower bound) and Neumann (upper bound) subproblems proves Weyl's leading term elementarily without microlocal machinery.
3. **Second-Order Boundary Correction (Ivrii's Theorem):** For smooth domains whose periodic billiard trajectories have measure zero, $N(\lambda) = (2\pi)^{-d}\omega_d\operatorname{Vol}(\Omega)\lambda^{d/2} \mp \frac{1}{4}(2\pi)^{-(d-1)}\omega_{d-1}\operatorname{Area}(\partial\Omega)\lambda^{(d-1)/2} + o(\lambda^{(d-1)/2})$ ($-$ for Dirichlet, $+$ for Neumann)—letting you "hear" both area and perimeter!
4. **Wave Trace and Poisson Relation:** Studying the trace $\operatorname{Tr}(e^{-it\sqrt{-\Delta}}) = \sum_k e^{-it\sqrt{\lambda_k}}$ via FIOs reveals that its singularities in $t$ occur exclusively at the lengths of closed periodic geodesics/billiards!

## Introduction

If we stare at individual eigenvalues one by one, the spectrum can look mysterious. But at large scale, geometric structure appears: the number of eigenvalues below a large energy threshold often follows a power law determined by dimension and operator order. This is the world of spectral asymptotics.

What makes the topic so compelling is that the spectrum does not only measure oscillation. It also records geometry, metric structure, and phase-space volume. That is why spectral questions sit naturally at the intersection of PDE, geometry, and physics.

## The Concept in Three Ways

### Intuitive View

Think of a musical instrument. Individual notes sound different, but when we look at the whole collection of high notes, their density begins to reflect the size and shape of the instrument. Weyl's law is the mathematical version of that intuition.

### Visual View

A good classroom picture is the eigenvalue counting function $$ N(\lambda) $$, the number of eigenvalues below or equal to $$ \lambda $$. Compare its growth in one, two, and three dimensions. Students quickly see that the spatial dimension directly controls the growth rate.

### Formal View

If $$ N(\lambda) $$ counts eigenvalues of an elliptic operator of order $$ m $$, then in many settings $$ N(\lambda)\sim C\lambda^{n/m} $$ as $$ \lambda\to\infty $$, where $$ n $$ is the space dimension and $$ C $$ is a geometric constant related to phase-space volume. This is the heart of Weyl's law.

## Common Misconceptions

### "High-frequency spectrum is just a counting problem"

No. It encodes deep geometric information.

### "Weyl's law predicts each eigenvalue exactly"

False. It describes asymptotic growth of the counting function, not the exact position of every eigenvalue.

### "The constant $$ C $$ is just a technical coefficient"

No. It often reflects geometric quantities such as domain volume or phase-space volume.

### "If two domains have very similar spectra, they must have the same shape"

Not necessarily. This is exactly why inverse spectral questions are subtle and interesting.

## Learning Progression

### Step 1: Review the counting function

Students should understand what $$ N(\lambda) $$ measures before asymptotics are introduced.

### Step 2: Look at low-dimensional examples

One-dimensional examples are the most transparent.

### Step 3: Introduce Weyl's law

Highlight the roles of dimension and operator order.

### Step 4: Connect to semiclassical volume

High-energy spectral data is naturally interpreted through phase-space geometry.

### Key Checkpoints

- Can students explain what $$ N(\lambda) $$ means?
- Can they say why the exponent is $$ n/m $$?
- Can they explain why large spectra contain geometric information?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Testing One-Term and Two-Term Weyl Laws on the Square $[0,\pi]^2$

For the Dirichlet Laplacian $-\Delta$ on $\Omega = (0,\pi)^2$, the exact eigenvalues are $\lambda_{m,n} = m^2 + n^2$ for integers $m, n \ge 1$. Count $N(25)$ exactly by hand and compare with both the one-term and two-term Weyl formulas!

1. **Count all positive integer pairs $(m,n)$ with $m^2 + n^2 \le 25$:**
   - $m = 1$: $n^2 \le 24 \implies n \in \{1, 2, 3, 4\}$ ($4$ modes).
   - $m = 2$: $n^2 \le 21 \implies n \in \{1, 2, 3, 4\}$ ($4$ modes).
   - $m = 3$: $n^2 \le 16 \implies n \in \{1, 2, 3, 4\}$ ($4$ modes).
   - $m = 4$: $n^2 \le 9 \implies n \in \{1, 2, 3\}$ ($3$ modes).
   - $m = 5$: $n^2 \le 0 \implies$ none ($0$ modes).
   Exact count: $N(25) = 4 + 4 + 4 + 3 = 15$.
2. **Compute the 2D one-term Weyl prediction ($\operatorname{Area}(\Omega) = \pi^2$):**
   $$N_{\text{Weyl},1}(\lambda) = \frac{\operatorname{Area}(\Omega)}{4\pi}\lambda = \frac{\pi^2}{4\pi}(25) = \frac{25\pi}{4} \approx 19.63.$$
3. **Add the Dirichlet perimeter correction ($\operatorname{Perim}(\Omega) = 4\pi$):**
   $$N_{\text{Weyl},2}(\lambda) = \frac{\operatorname{Area}(\Omega)}{4\pi}\lambda - \frac{\operatorname{Perim}(\Omega)}{4\pi}\sqrt{\lambda} = 19.63 - \frac{4\pi}{4\pi}(5) = 19.63 - 5 = 14.63.$$
   Notice how the boundary correction immediately drops the discrepancy from $4.63$ down to just $0.37$—already accurate to $2.5\%$ at $\lambda = 25$!

### Example 1: The interval $$ [0,\pi] $$

For the Dirichlet Laplacian on $$ [0,\pi] $$, the eigenvalues are $$ \lambda_k=k^2 $$. The condition $$ \lambda_k\le \lambda $$ means $$ k\le \sqrt{\lambda} $$. So $$ N(\lambda)\sim \sqrt{\lambda} $$. This is exactly the case $$ n=1,m=2 $$.

### Example 2: Understanding the exponent $$ n/m $$

In higher dimensions, there are more independent oscillatory modes below the same energy threshold. This is the intuitive reason the exponent depends on the spatial dimension.

### Example 3: The planar Laplacian

In two dimensions, Weyl's law for the Laplacian has the form

$$
N(\lambda)\sim C\,\operatorname{Area}(\Omega)\,\lambda.
$$

So the area of the domain enters directly into the leading term. This makes the geometric nature of the law very concrete.

### Example 4: Reading Weyl's law through phase space

If we look at all pairs $$ \left(x,\xi\right) $$ satisfying $$ \lvert \xi\rvert^2\le \lambda $$, then Weyl's law says that the number of modes below energy $$ \lambda $$ is essentially the volume of this allowed region in phase space after suitable normalization. This is the modern semiclassical interpretation.

## Conceptual Questions

1. Why should large spectral data reflect geometry rather than just algebraic structure?
2. In what sense is Weyl's law really a phase-space statement?
3. Why does knowing the asymptotics of $$ N(\lambda) $$ not completely determine the domain?

## Application Problems

1. In structural vibration, how does the density of high-frequency modes reflect the size and geometry of a body?
2. In quantum mechanics, why is counting large energy levels closely related to classical phase-space volume?
3. In spectral geometry, why does Weyl's law give important information without solving the full inverse problem?

## Interactive Teaching Strategies

### Questions to Ask in Class

- If a domain becomes larger, should you expect more or fewer eigenvalues below a fixed threshold?
- Why should high frequency "see" geometry?
- What is gained by studying the counting function instead of individual eigenvalues?

### Suggested Activities

- Have students count eigenvalues explicitly in the one-dimensional interval case.
- Compare graphs of $$ N(\lambda) $$ in different dimensions.
- Ask groups to explain Weyl's law in ordinary language rather than in formulas.

### Participation Moves

- Start from musical or vibrational examples.
- Ask students to predict growth rates before deriving them.
- Encourage them to connect spectral growth with geometry and phase space.

## Differentiation

### Support for Struggling Students

- Stay with one-dimensional counting first.
- Emphasize the message rather than technical remainder terms.
- Use visual growth graphs repeatedly.

### Challenge for Advanced Students

- Explore the remainder term in Weyl asymptotics.
- Study the relation between Weyl's law and semiclassical analysis.
- Connect the topic to inverse spectral problems and quantum chaos.

## Quick Summary

Spectral asymptotics studies how the number of eigenvalues below a large threshold grows. Weyl's law shows that high-frequency spectral data is controlled by dimension, operator order, and phase-space geometry.

---

## Real-World Applications

### 1. Structural vibration and modal density

For a vibrating elastic structure, one often studies an eigenvalue problem of the form $$ L u = \lambda u $$, where $$ L $$ is an elliptic operator encoding stiffness and geometry. Engineers care about how many modes lie below a given frequency band because dense modal clustering can amplify resonance or noise. The model assumes linear elasticity and small displacements. The interpretation of Weyl-type asymptotics is that large-scale modal density is governed first by geometry and dimension, not by the exact shape of each individual eigenmode.

### 2. Quantum density of states

For a quantum Hamiltonian, large-energy eigenvalue counts approximate the classical phase-space volume of energetically allowed states. The assumption is that the Hamiltonian is confining enough for a discrete spectrum. The main limitation is that fine spectral fluctuations, tunneling, and symmetry effects lie beyond the leading asymptotic term. The interpretation is that spectral asymptotics provides the first bridge from quantum level counting to classical mechanics.

### 3. Room acoustics and instrument design

Acoustic resonances in a cavity are determined by Laplace eigenvalues with boundary conditions. The higher the frequency, the more the counting function reflects room volume and dimension rather than low-frequency geometric quirks. The model ignores damping and nonlinear sound production. The solution is interpreted as a practical rule: large rooms and larger effective phase-space volume support more resonant modes below the same threshold.

## Conceptual Insight

Weyl's law is not fundamentally a statement about a sequence of numbers. It is a statement about counting accessible oscillatory states in phase space. A common misconception is to expect asymptotics to determine every eigenvalue accurately. The leading term only captures bulk growth; the delicate information sits in lower-order corrections and oscillatory remainder terms.

## Visualizations and Computation

### Python

```python
import numpy as np
import matplotlib.pyplot as plt

k = np.arange(1, 300)
lam = k**2
grid = np.linspace(1, lam[-1], 600)
N = np.array([np.sum(lam <= val) for val in grid])

plt.figure(figsize=(8, 5))
plt.plot(grid, N, label='Exact counting function')
plt.plot(grid, np.sqrt(grid), '--', label='Weyl asymptotic in 1D')
plt.xlabel('lambda')
plt.ylabel('N(lambda)')
plt.title('Dirichlet Laplacian on [0, pi]')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### JavaScript

```html
<div id="weyl-count"></div>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<script>
const lam = Array.from({length: 250}, (_, i) => (i + 1) ** 2);
const grid = Array.from({length: 500}, (_, i) => 1 + (lam[lam.length - 1] - 1) * i / 499);
const N = grid.map(v => lam.filter(a => a <= v).length);
const asymp = grid.map(v => Math.sqrt(v));
Plotly.newPlot('weyl-count', [
  {x: grid, y: N, mode: 'lines', name: 'Exact'},
  {x: grid, y: asymp, mode: 'lines', name: 'sqrt(lambda)'}
], {title: 'Counting function and Weyl growth', xaxis: {title: 'lambda'}, yaxis: {title: 'N(lambda)'}});
</script>
```

### External References

Search for `Weyl law visualization`, `eigenvalue counting function Laplacian`, or `density of states geometry`.

## Difficulty Layering

### Undergraduate Level

Stay with concrete interval and rectangle examples, where students can count modes and compare them with growth laws.

### Graduate Level

Emphasize phase-space proofs, Tauberian ideas, remainder terms, trace formulas, and the transition from Weyl asymptotics to spectral geometry and quantum chaos.

> See the full gallery of chapter interactives here: [Chapter 15 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter15/15_10_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Drum frequencies and resonant cavities
- Problem: The number of vibration modes below a threshold $$ \lambda $$ follows a geometric growth law.
- Model: The eigenvalue counting function
$$ N(\lambda)=\#\{\lambda_j\le \lambda\} $$
satisfies Weyl-type asymptotics.
- Assumptions and limitations: The remainder depends on boundary geometry, symmetry, and dynamics.
- Interpretation: Spectral asymptotics links discrete spectra to phase-space volume.

#### Quantum energy levels
- Problem: We want to count low-energy states of Schrodinger or Laplace-Beltrami operators.
- Model: Use spectral asymptotic formulas or trace formulas.
- Assumptions and limitations: One usually assumes regular geometry or semiclassical scaling.
- Interpretation: The spectrum is not a random list; it reflects underlying geometry.

### 2. Additional Intuition and Connections

Spectral asymptotics asks how eigenvalues are distributed at high energy. The core intuition is that each phase-space cell corresponds roughly to one quantum state. A common pitfall is to extrapolate from the first few eigenvalues; asymptotics concerns the large-energy regime.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

lam = np.linspace(1, 400, 400)
N_exact = np.floor(np.sqrt(lam) / np.pi)
N_weyl = np.sqrt(lam) / np.pi

plt.plot(lam, N_exact, label="exact N(lambda) on [0,1]")
plt.plot(lam, N_weyl, "--", label="Weyl approximation")
plt.legend()
plt.title("Spectral asymptotics on an interval")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Weyl law visualization drum frequencies
- search: spectral asymptotics interval eigenvalue counting
- search: quantum chaos Weyl law intuition

### 5. Worked Example

On the interval $$ [0,1] $$ with Dirichlet boundary conditions,
$$ \lambda_n = n^2\pi^2. $$
Therefore
$$
N(\lambda)=\max\{n: n^2\pi^2\le \lambda\}=\left\lfloor \frac{\sqrt{\lambda}}{\pi}\right\rfloor.
$$
Weyl's law says that as $$ \lambda \to \infty $$,
$$ N(\lambda)\sim \frac{\sqrt{\lambda}}{\pi}. $$

### 6. Difficulty Layering

**Undergraduate level.** Count modes in simple domains and compare with growth laws.

**Graduate level.** Connect to Weyl's law, trace formulas, remainder estimates, and spectral geometry.

## Video tham khảo

- xem trước: [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), English. Microlocal methods aimed at spectral questions.
- [Lecture 22: The Spectral Theorem for a Compact Self-Adjoint Operator](https://www.youtube.com/watch?v=-sfaHVFWBU8) — MIT OpenCourseWare, English. The compact spectral theorem, the eigenvalue picture spectral asymptotics refine.
- [Lecture 20: Compact Operators and the Spectrum of a Bounded Linear Operator on a Hilbert Space](https://www.youtube.com/watch?v=SFDMFbzCsH0) — MIT OpenCourseWare, English. The spectrum of a bounded operator, the object those asymptotics count.
