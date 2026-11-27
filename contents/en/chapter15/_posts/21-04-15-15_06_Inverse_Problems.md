---
layout: post
title: "Inverse Problems"
chapter: '15'
order: 6
owner: Lê Minh Hoàng
lang: en
categories:
- chapter15
lesson_type: optional
---

> **Storytelling Hook:** A forward PDE problem asks: given the rock layers beneath the Earth's crust, how do seismic waves travel to surface sensors? An **inverse problem** flips the arrow backward: listening *only* to surface echoes or boundary electrical currents, can you reconstruct the hidden interior? The catch is that forward operators smooth away fine details—so inverting them magnifies microscopic measurement noise exponentially unless you regularize.

![Inverse problems: reconstructing hidden parameters from measured data]({{ site.imgurl }}/chapter_img/chapter15/06_inverse_problems.svg)

## Objectives

This optional lesson introduces inverse problems as a natural application area of microlocal analysis and PDE. After the lesson, students should be able to distinguish forward and inverse problems, explain why inverse problems are often unstable, and see the roles of regularization, propagation of singularities, and incomplete data in reconstruction.

## Prerequisites

Students should know propagation of singularities, basic elliptic or wave equations, and the practical reality that measured data is noisy. It is also helpful to remember that in a forward problem the model is known, while in an inverse problem the hidden structure itself must be recovered.

## Key ideas: Uniqueness, Ill-Posedness, and Regularization in Inverse Problems

Four pillars define the mathematical theory of PDE inverse problems:

1. **Hadamard Ill-Posedness:** Forward maps $F: \text{parameters} \to \text{data}$ are typically compact smoothing operators, so $F^{-1}$ is unbounded—arbitrarily tiny data noise $\delta$ can produce arbitrarily huge reconstruction errors unless extra prior information is imposed.
2. **Calderón's Problem and the Dirichlet-to-Neumann Map:** Can you determine interior conductivity $\gamma(x)$ in $\nabla\cdot(\gamma\nabla u) = 0$ purely from boundary voltage-to-current measurements $\Lambda_\gamma: u|_{\partial\Omega} \mapsto \gamma\partial_n u|_{\partial\Omega}$? Sylvester–Uhlmann (1987) proved uniqueness in $d \ge 3$ using Complex Geometric Optics (CGO) solutions.
3. **Stability Regimes (Logarithmic vs. Lipschitz):** Elliptic inverse problems (like Calderón's problem) exhibit notoriously weak *logarithmic* stability ($\|\gamma_1-\gamma_2\| \le C|\ln\delta|^{-\alpha}$), whereas hyperbolic wave/travel-time inverse problems often achieve much stronger Hölder or Lipschitz stability because waves carry sharp singularities to the boundary!
4. **Tikhonov Regularization and Microlocal Visibility:** Minimizing $\|F(x) - y^\delta\|^2 + \alpha\|x\|_{H^s}^2$ trades bias against variance; microlocal analysis tells us precisely *which* internal edges (wave front covectors) are stably visible from the available sensor geometry.

## Introduction

In a forward problem, we know the equation, the coefficients, and the source, and we compute the resulting solution or data. In an inverse problem, the order is reversed: we observe data outside and try to infer the hidden structure inside. This is the mathematical core of CT, ultrasound, seismic imaging, radar, and many modern sensing technologies.

What makes inverse problems difficult is instability. Tiny measurement errors can create large reconstruction errors. That is why inverse problems sit at the intersection of analysis, PDE, statistics, and computation.

## The Concept in Three Ways

### Intuitive View

Imagine hearing echoes in a room and trying to recover the room shape from those echoes. That is an inverse problem: infer an unseen interior from exterior data.

### Visual View

A clear classroom diagram uses two arrows:

- forward problem: parameters -> model -> data,
- inverse problem: data -> reconstruction of parameters.

Then add a noise cloud on the data side. Students immediately see the main difficulty: the input to the inverse problem is already imperfect.

### Formal View

If the forward map is modeled by $$ \mathcal{F}(m)=d $$, where $$ m $$ is the hidden parameter or structure and $$ d $$ is the measured data, then the inverse problem asks us to recover $$ m $$ from $$ d $$. In many settings, the inverse map $$ \mathcal{F}^{-1} $$:

- may not exist globally,
- may not be unique,
- or may be extremely unstable.

This is why regularization and prior information become central.

## Three Central Questions

Students often compress every difficulty into the vague statement "inverse problems are hard." It helps enormously to separate three different questions:

- visibility: which singularities or structures actually enter the measured data?
- uniqueness: does the data determine one and only one hidden object?
- stability: does small data noise cause only small reconstruction error?

Many research papers solve only one or two of these questions, not the full inverse problem at once. This distinction helps students read the literature more intelligently.

## Common Misconceptions

### "An inverse problem is just solving a formula backward"

False. The main issues are instability, nonuniqueness, and incomplete data.

### "If we have enough data, reconstruction is automatically good"

No. What matters is not only how much data we have, but which singularities the data can actually see.

### "Regularization is just a trick that changes the real problem"

No. Regularization is what makes an unstable inverse problem mathematically meaningful under noise.

### "Microlocal analysis is too abstract to help inverse problems"

False. It is exactly the right language for deciding which singularities are visible, recoverable, or lost.

## Learning Progression

### Step 1: Distinguish forward from inverse

Students should first see that inverse problems are not merely forward problems run in reverse.

### Step 2: Understand instability

Small noise can be amplified dramatically.

### Step 3: Introduce regularization

Extra structure, priors, or penalties are needed to stabilize reconstruction.

### Step 4: Connect to microlocal analysis

Propagation and wave front ideas explain what the data can really detect.

### Key Checkpoints

- Can students explain why inverse problems are typically harder than forward ones?
- Can they give one reason regularization is needed?
- Can they explain why visibility of singularities is central?

## Worked Examples


### Worked example: Hadamard's Classic Instability Example for Boundary Recovery

Consider recovering an interior harmonic field $u(x,y)$ on the strip $y > 0$ from noisy Cauchy data on the boundary $y = 0$: $\Delta u = 0$, $u(x,0) = 0$, $\partial_y u(x,0) = g_n(x) = \frac{1}{n}\sin(nx)$. Quantify how a tiny boundary perturbation explodes at height $y = 1$ for $n = 10$.

1. **Write the exact harmonic solution matching $u(x,0) = 0$ and $\partial_y u(x,0) = \frac{1}{n}\sin(nx)$:**
   $$u_n(x,y) = \frac{1}{n^2}\sin(nx)\sinh(ny).$$
   Check: $\Delta u_n = \frac{1}{n^2}(-n^2 + n^2)\sin(nx)\sinh(ny) = 0$, $u_n(x,0) = 0$, and $\partial_y u_n(x,0) = \frac{1}{n^2}\cdot n\sin(nx)\cosh(0) = \frac{1}{n}\sin(nx)$.
2. **Measure the size of the boundary data perturbation as $n \to \infty$:**
   $$\max_{x\in\mathbb{R}} |g_n(x)| = \frac{1}{n} \xrightarrow{n\to\infty} 0.$$
   For $n = 10$, the boundary noise is just $0.10$.
3. **Measure the resulting interior reconstruction at $y = 1$:**
   $$\max_{x\in\mathbb{R}} |u_n(x,1)| = \frac{\sinh(n)}{n^2} = \frac{e^n - e^{-n}}{2n^2} \xrightarrow{n\to\infty} +\infty.$$
   For $n = 10$: $\sinh(10) \approx 11013.2$, so $\max_x |u_{10}(x,1)| \approx \frac{11013.2}{100} \approx 110.13$!
4. **Takeaway:** A boundary error of $0.10$ amplified by more than **$1100\times$** just one unit inside the domain (and at $n = 20$, a boundary error of $0.05$ amplifies to $6.06 \times 10^5$!). That exponential blow-up is why every practical inverse solver requires spectral filtering or Tikhonov regularization.

### Example 1: Computed tomography

In a CT scan, the data consists of X-ray line integrals through the body. From these integrals, one tries to reconstruct the internal density. This is a standard inverse problem: data is measured outside, while the target object is hidden inside.

### Example 2: Reflection seismology

Waves are sent into the earth, and reflected signals are recorded at the surface. From travel times and reflected singularities, geophysicists infer the structure of underground layers. Singularities in the data often correspond to interfaces inside the earth.

### Example 3: Why instability matters

If two hidden media produce almost identical data, then even very small measurement noise may make them hard to distinguish. This is the practical reason reconstruction algorithms must include some stabilizing principle.

### Example 4: Visible versus invisible singularities

A singular edge in the object may be recovered if the measurement operator sees it in the right geometric directions. Other singularities may remain invisible. This is a truly microlocal statement and is one of the main points where wave front sets and FIO enter inverse theory.

## Conceptual Questions

1. Why is an inverse problem usually harder than the corresponding forward problem?
2. Why is visibility a different issue from uniqueness?
3. Why does regularization belong to the mathematics of inverse problems rather than to numerical convenience only?

## Application Problems

1. In CT imaging, why do line integrals contain enough information to reconstruct some singular structures but not necessarily all features equally well?
2. In seismic imaging, how does wave propagation geometry affect what can be reconstructed underground?
3. In medical imaging, why must reconstruction methods be designed with noise in mind from the beginning?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What exactly is known in a forward problem, and what is unknown in an inverse problem?
- Why can tiny noise cause large reconstruction errors?
- Why should singularity visibility matter more than smooth background information in many imaging tasks?

### Suggested Activities

- Ask students to build a forward-versus-inverse diagram for a real imaging system.
- Compare clean and noisy synthetic data and discuss reconstruction difficulty.
- Have groups classify questions into visibility, uniqueness, or stability.

### Participation Moves

- Start from familiar technologies such as CT or ultrasound.
- Ask students to explain the problem in ordinary language before abstract notation.
- Repeatedly connect the topic back to wave fronts and propagation.

## Differentiation

### Support for Struggling Students

- Use concrete imaging examples before formal operator notation.
- Emphasize the three-question framework: visibility, uniqueness, stability.
- Keep regularization intuitive at first.

### Challenge for Advanced Students

- Study linearized inverse problems through normal operators.
- Explore why FIO are natural measurement models in imaging.
- Connect microlocal visibility results to artifact formation in reconstruction.

## Quick Summary

Inverse problems try to reconstruct hidden structure from measured data. Their main difficulties are instability, incomplete visibility, and nonuniqueness, and microlocal analysis is one of the main tools for understanding what can actually be recovered.

---

## Real-World Applications

### 1. Computed tomography

The basic forward model is the Radon transform

$$
Rf(\theta,s)=\int_{x\cdot \theta=s} f(x)\,d\sigma(x).
$$

The inverse problem is to recover tissue density $$ f $$ from X-ray line integrals. The model assumes straight rays and negligible multiple scattering, which is only approximately true in practice. The interpretation is that reconstruction quality depends not only on numerical inversion but also on whether the geometry makes the important singularities visible.

### 2. Electrical impedance tomography

In EIT one applies voltages on the boundary of a body and measures the resulting currents. A simplified PDE model is $$ \nabla \cdot (\gamma(x) \nabla u)=0 $$, where $$ \gamma(x) $$ is the unknown conductivity. The model assumes a continuum medium and accurate boundary contact. The inverse problem is severely ill-posed, so small measurement noise can destroy high-resolution features. The interpretation is that stable recovery of coarse structure is often easier than stable recovery of sharp interfaces.

### 3. Seismic inversion

A wave field solves $$ u_{tt}-c(x)^2\Delta u=s $$, and one tries to infer the speed $$ c(x) $$ or reflecting interfaces from boundary recordings. The model assumes a known source and a linear or weakly nonlinear wave regime. Its limitation is that multipathing, attenuation, and unknown source signatures complicate recovery. The solution is interpreted microlocally: the first reliable information often comes from reflectors and travel times rather than a full smooth coefficient map.

## Conceptual Insight

The inverse problem is not merely to undo a formula. It is to undo a map that may erase, blur, or amplify information. A central misconception is that more data automatically means a stable answer. In reality, visibility, geometry, and noise amplification determine what can be trusted.

## Visualizations and Computation

### Python

This example shows how naive inversion amplifies high-frequency noise in a toy deconvolution problem.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 600)
f_true = (np.abs(x) < 1.5).astype(float)
kernel = np.exp(-x**2 / 0.7)
kernel /= kernel.sum()
data = np.convolve(f_true, kernel, mode='same')
noise = 0.03 * np.random.randn(len(x))
data_noisy = data + noise

F = np.fft.fft(f_true)
K = np.fft.fft(kernel)
D = np.fft.fft(data_noisy)
recon = np.real(np.fft.ifft(D / (K + 1e-2)))

plt.figure(figsize=(9, 5))
plt.plot(x, f_true, label='true object')
plt.plot(x, data_noisy, label='measured data')
plt.plot(x, recon, label='regularized inversion')
plt.legend()
plt.title('Toy inverse problem: blur, noise, reconstruction')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### JavaScript

```html
<div id="inverse-toy"></div>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<script>
const x = Array.from({length: 300}, (_, i) => -6 + 12 * i / 299);
const truth = x.map(v => Math.abs(v) < 1.5 ? 1 : 0);
const blur = x.map(v => Math.exp(-v * v / 2));
Plotly.newPlot('inverse-toy', [
  {x, y: truth, mode: 'lines', name: 'hidden object'},
  {x, y: blur.map(v => v / Math.max(...blur)), mode: 'lines', name: 'blur kernel'}
], {title: 'Edit this sketch into a blur-and-recovery demo'});
</script>
```

### External References

Search for `limited angle tomography artifacts`, `electrical impedance tomography inverse problem`, or `seismic inversion wave front set`.

## Difficulty Layering

### Undergraduate Level

Focus on the distinction between forward and inverse problems, and on simple examples where noise makes naive inversion unreliable.

### Graduate Level

Develop linearization, normal operators, stability estimates, Tikhonov regularization, and microlocal visibility theorems for Radon-type or wave-based measurement operators.

> See the full gallery of chapter interactives here: [Chapter 15 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter15/15_10_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Medical tomography
- Problem: From indirect measurements, we want to recover internal structure.
- Model: A forward operator maps the object to data, and the inverse problem asks for an inverse or approximate inverse.
- Assumptions and limitations: Limited-angle data, noise, and model mismatch all reduce stability.
- Interpretation: Microlocal analysis tells us which singularities are visible in the data.

#### Seismic inverse problems
- Problem: Surface wave measurements are used to infer reflectors inside the Earth.
- Model: Linearization, normal operators, and FIOs describe visibility and stability.
- Assumptions and limitations: Not every singular direction is observable.
- Interpretation: Inverse problems are governed more by visibility in phase space than by pointwise geometry alone.

### 2. Additional Intuition and Connections

Inverse problems are often unstable because the inverse of a high-frequency damping filter amplifies noise. That is why regularization is essential, not optional. A common misconception is that uniqueness of the forward model implies stable inversion; in practice that is often false.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 512, endpoint=False)
u_true = np.sin(3 * x) + 0.4 * np.sin(12 * x)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi
a = 1 / (1 + 0.3 * xi**2)
data = np.fft.ifft(a * np.fft.fft(u_true)).real
noise = 0.03 * np.random.default_rng(0).standard_normal(len(x))
data_noisy = data + noise

eps = 0.02
u_rec = np.fft.ifft(np.conj(a) * np.fft.fft(data_noisy) / (np.abs(a)**2 + eps)).real

plt.plot(x, u_true, label="true")
plt.plot(x, data_noisy, label="blurred noisy data")
plt.plot(x, u_rec, label="regularized reconstruction")
plt.legend()
plt.title("Inverse problems require regularization")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: inverse problem deconvolution regularization visualization
- search: CT visible singularities microlocal analysis
- search: seismic inverse problems wave front set intuition

### 5. Worked Example

If the forward operator is convolution with symbol $$ a(\xi) $$ that becomes small at high frequencies, then formal inversion multiplies by $$ 1/a(\xi) $$ and strongly amplifies noise where $$ a(\xi) $$ is near zero. Tikhonov regularization replaces that inverse by
$$
\frac{\overline{a(\xi)}}{\lvert a(\xi)\rvert^2+\varepsilon}.
$$
This is the standard model of instability in inverse problems.

### 6. Difficulty Layering

**Undergraduate level.** Distinguish forward and inverse problems through a simple deblurring example.

**Graduate level.** Connect to normal operators, visibility, regularization, and microlocal reconstruction theorems.

## Video tham khảo

- xem trước: [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), English. Zworski's microlocal lecture, the toolkit of boundary and inverse spectral problems.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, English. Vasy on scattering and inverse-type global problems for wave operators.
- [Introduction to Fourier Integral operators 1 (Allan Greenleaf)](https://www.youtube.com/watch?v=4O_oC9kFFWQ) — Mathematics video VAROQUI Hervé, Vietnamese. Fourier integral operators, which describe the measurements in many inverse problems.
