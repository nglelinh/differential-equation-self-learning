---
layout: post
title: "Wave Front Sets"
chapter: '15'
order: 1
owner: Lê Minh Hoàng
lang: en
categories:
- chapter15
lesson_type: required
---

![Wave front set as a description of the location and direction of singularities]({{ site.imgurl }}/chapter_img/chapter15/01_wave_front_sets.svg )

## Objectives

This lesson opens the microlocal chapter with its most important concept: the wave front set. After the lesson, students should understand why singular support is not enough, why wave front sets must record both location and frequency direction, and why this idea becomes the central tool for tracking singularities in modern PDE.

## Prerequisites

Students should know distributions, the Fourier transform, smooth cutoff functions, singular support, and the basic intuition that a function may be smooth in some directions but not in others. These ideas are reviewed in Lesson 15.00. In earlier chapters, regularity was mostly asked pointwise in space. Here we refine the question by asking about both position and cotangent direction.

## Introduction

If we only use singular support, we learn where a distribution fails to be smooth, but we do not learn in which directions the lack of smoothness occurs. That directional information may sound secondary at first, but in fact it is what determines how singularities move under a PDE. A corner, an edge, and a point source may occur at the same spatial location while carrying very different frequency structures.

The wave front set is designed to record exactly that missing information. It gives a map of singularities not just in physical space, but in local phase space, where each point is paired with suspicious cotangent directions.

## The Concept in Three Ways

### Intuitive View

Imagine light hitting an object with a sharp edge. If you only know where the edge is, that is not enough to predict the reflected light or the shadow. You also need to know how the edge is oriented. The wave front set plays the same role for singularities: it not only marks where something is rough, but also tells us in which frequency directions that roughness appears.

### Visual View

A very effective classroom diagram is to compare three examples:

- a smooth function, with no singular directions at all,
- the Dirac delta at the origin, singular in every nonzero direction,
- a step function in the variable $$ x_1 $$, singular mainly in directions normal to the jump.

This picture is powerful because it shows that "not smooth" is not one single phenomenon. A good board drawing marks a point $$ x_0 $$ in space and a cone of directions $$ \xi $$ in frequency space.

### Formal View

For $$ u\in \mathcal{D}'(\Omega) $$, we say that $$ (x_0,\xi_0)\notin WF(u) $$ if there exists a cutoff $$ \varphi\in C_c^\infty(\Omega) $$, equal to 1 near $$ x_0 $$, such that the Fourier transform of $$ \varphi u $$ decays rapidly in an open cone around $$ \xi_0 $$:

$$
\widehat{\varphi u}(\xi)=O(\lvert \xi\rvert^{-N})
\qquad \text{for every } N,
$$

as $$ \lvert \xi\rvert\to\infty $$ inside that cone.

If this rapid decay fails, then $$ u $$ has a microlocal singularity at

$$ (x_0,\xi_0). $$

## Quick Comparison with Singular Support

Students often need a very clear anchor at this stage:

- singular support answers: where is the object not smooth?
- the wave front set answers the stronger question: where is it not smooth, and in which frequency directions?
- projecting the wave front set down to physical space recovers the singular support.

In that sense, singular support is a map of where singularities live, while the wave front set is a map with directional arrows attached. In wave propagation and imaging, those arrows are often the most important part.

## Common Misconceptions

### "The wave front set is just singular support written differently"

False. Singular support remembers only location. The wave front set also remembers direction.

### "If a function is singular at a point, then it must be singular in every direction there"

Not true. Some singularities are directional and only show up along certain cotangent directions.

### "Rapid Fourier decay means the function is globally smooth"

No. We are taking the Fourier transform of $$ \varphi u $$ after localizing near $$ x_0 $$.

### "Wave front sets are too abstract to be useful outside pure theory"

False. They are central in wave propagation, inverse problems, and imaging.

## Learning Progression

### Step 1: Review singular support

Students should first recall the simpler question: where is the distribution not smooth?

### Step 2: Add local Fourier analysis

Localize near $$ x_0 $$ and look at the decay of the Fourier transform.

### Step 3: Introduce directional cones

We do not need every direction at once. We only test behavior near a chosen cone around $$ \xi_0 $$.

### Step 4: Connect to PDE

PDE rarely moves singular support as one large block. It moves singular directions one by one.

### Key Checkpoints

- Can students explain why singular support is not enough?
- Can they explain the role of the cutoff $$ \varphi $$?
- Can they explain why the decay test is performed inside an open cone rather than across all of frequency space?

## Worked Examples

### Example 1: A smooth function

If $$ u\in C^\infty(\Omega) $$, then after localizing with any smooth cutoff $$ \varphi $$, the Fourier transform of $$ \varphi u $$ decays rapidly in every direction. Therefore $$ WF(u)=\varnothing $$. This is the simplest consistency check.

### Example 2: The Dirac delta

Let $$ u=\delta_0 $$ in $$ \mathbb{R}^n $$. Its singular support is the single point $$ 0 $$. But after localizing near the origin, its Fourier transform is essentially constant, so there is no rapid decay in any nonzero direction. Hence $$ WF(\delta_0)=\{(0,\xi):\xi\neq 0\} $$. The delta is singular at one point, but in all directions there.

### Example 3: A step function

Consider the Heaviside function in one variable. The singularity occurs at the jump point, and its wave front directions are normal to the jump. This is the first example showing that singularities can be directional rather than isotropic.

### Example 4: Why localization matters

A function may be smooth near one point and singular elsewhere. The cutoff $$ \varphi $$ allows us to isolate the neighborhood of interest, so the wave front set is truly local in position but directional in frequency.

## Conceptual Questions

1. Why does singular support lose information that the wave front set preserves?
2. Why is the Fourier transform the right tool for detecting directional smoothness?
3. Why does the Dirac delta have singularity in every nonzero direction?

## Application Problems

1. In imaging, why is it useful to know not only where an edge occurs but also in which direction the edge is visible?
2. In wave propagation, why should directional singularity information matter more than location alone?
3. In tomography, how might different edge directions be seen differently by measured data?

## Interactive Teaching Strategies

### Questions to Ask in Class

- If you know where a singularity is, what important information is still missing?
- Why does a localized Fourier transform encode directional behavior?
- Which seems more singular: a point source or a jump across a surface, and why?

### Suggested Activities

- Draw and compare a smooth bump, a delta, and a step function.
- Ask groups to describe singular support first, then refine their answer using wave front sets.
- Use hand sketches of cones in frequency space so students can visualize directional testing.

### Participation Moves

- Start with pictures before formulas.
- Ask students to explain the definition verbally before writing the notation.
- Revisit the same examples repeatedly so the abstraction stays grounded.

## Differentiation

### Support for Struggling Students

- Work mainly with one-dimensional examples first.
- Emphasize the slogan "wave front set = location plus direction of singularity."
- Use the delta and the step function as the two main anchor examples.

### Challenge for Advanced Students

- Compare wave front sets of measures supported on smooth hypersurfaces.
- Connect wave front sets with oscillatory integral examples.
- Explore how wave front sets behave under pullback or Fourier transform.

## Quick Summary

The wave front set refines singular support by recording not only where singularities occur, but also in which cotangent directions they occur. It is the basic language of microlocal regularity and singularity propagation.

---

## Real-World Applications

### 1. Edge detection in computer vision

In a grayscale image, a sharp boundary between two objects behaves like a jump discontinuity. A simple model is $$ u(x_1,x_2)=H(x_1-a)+b(x_1,x_2) $$, where $$ H $$ is the Heaviside step function and $$ b $$ is a smooth background illumination term. The singular support tells us that the image is non-smooth along the line $$ x_1=a $$, while the wave front set tells us that the dominant singular directions are normal to the edge. The model assumes an idealized sharp edge and ignores blur, noise, and pixelation. Its main interpretation is practical: edge detectors work best when they recover not only where the edge is, but also which direction is geometrically important.

### 2. Limited-angle CT and tomographic visibility

In computed tomography, the measured data is approximately the Radon transform

$$
Rf(	heta,s)=
\int_{x\cdot \theta=s} f(x)\,d\sigma(x).
$$

The inverse problem is to recover the internal density $$ f $$ from line-integral data. Wave front analysis explains that an interface is visible only when the acquisition geometry probes directions transverse to that interface. The model assumes a linear attenuation law and ideal rays; in practice, scattering, detector noise, and incomplete angle coverage degrade reconstruction. The solution is interpreted microlocally: some edges are recoverable, others are invisible no matter how much algebra one applies.

### 3. Seismic reflector interpretation

In exploration seismology, a pressure field approximately satisfies $$ p_{tt}-c(x)^2\Delta p=s(x,t) $$, where discontinuities in the material coefficients produce reflected singularities. A geological interface may be smooth as a surface but still generate a strong singular response in the normal direction. The model assumes linear acoustics and neglects strong multiple scattering. The main interpretation is that wave front information identifies not only the location of an underground interface but also its orientation, which is what migration algorithms try to reconstruct.

## Conceptual Insight

The key physical idea is that roughness is directional. A point source, a crack, and a flat edge can all sit at the same place in space while generating completely different high-frequency signatures. That is why the wave front set lives in cotangent space rather than ordinary physical space. A common pitfall is to think of $$ \xi $$ as a direction along the edge; for jump singularities, the important directions are typically normal to the edge, because those are the directions in which oscillations fail to decay rapidly.

## Visualizations and Computation

### Python

The following script compares a smooth image with a sharp vertical edge and shows how the localized Fourier spectrum becomes anisotropic for the edge.

```python
import numpy as np
import matplotlib.pyplot as plt

N = 300
x = np.linspace(-2, 2, N)
X, Y = np.meshgrid(x, x)
phi = np.exp(-(X**2 + Y**2) / 0.4)

smooth = np.exp(-(X**2 + Y**2))
edge = (X > 0).astype(float)

def local_spectrum(u):
    return np.fft.fftshift(np.abs(np.fft.fft2(phi * u)))

spec_smooth = local_spectrum(smooth)
spec_edge = local_spectrum(edge)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].imshow(smooth, cmap="viridis", extent=[-2, 2, -2, 2])
axes[0, 0].set_title("Smooth image")
axes[0, 1].imshow(edge, cmap="gray", extent=[-2, 2, -2, 2])
axes[0, 1].set_title("Step edge")
axes[1, 0].imshow(np.log1p(spec_smooth), cmap="magma")
axes[1, 0].set_title("Localized spectrum: smooth")
axes[1, 1].imshow(np.log1p(spec_edge), cmap="magma")
axes[1, 1].set_title("Localized spectrum: directional edge")
for ax in axes.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()
```

### JavaScript

This Plotly sketch lets students change the edge angle by editing $$ \theta $$ and immediately see the corresponding image geometry.

```html
<div id="wf-edge"></div>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<script>
const n = 120;
const theta = Math.PI / 6;
const xs = Array.from({length: n}, (_, i) => -2 + 4 * i / (n - 1));
const z = xs.map(y => xs.map(x => (x * Math.cos(theta) + y * Math.sin(theta) > 0 ? 1 : 0)));
Plotly.newPlot('wf-edge', [{z, type: 'heatmap', colorscale: 'Gray'}], {
  title: 'Rotated edge: edit theta to change direction',
  xaxis: {title: 'x1'},
  yaxis: {title: 'x2'}
});
</script>
```

### External References

Search for `limited angle tomography wave front set`, `edge singularity Fourier direction`, or `seismic migration wave front set`.

## Difficulty Layering

### Undergraduate Level

Focus on the slogan: the wave front set is singular support plus direction. Students should be able to recognize three anchor examples: smooth data, the Dirac delta, and a jump across a line or surface.

### Graduate Level

Focus on the full conic definition, coordinate invariance, and the behavior of wave front sets under pullback, pushforward, Fourier transform, and pseudodifferential operators. At this level, the wave front set becomes the natural language for propagation theorems and inverse problems.

> See the full gallery of chapter interactives here: [Chapter 15 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter15/15_10_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### CT imaging and edge detection
- Problem: In medical imaging, what matters is often not just where an edge is, but which direction it faces.
- Model: The wave front set $$ WF(u) $$ records both location $$ x $$ and frequency direction $$ \xi $$ of singularities.
- Assumptions and limitations: This is a local microlocal model, not a direct replacement for discrete imaging algorithms.
- Interpretation: Two singularities at the same point but with different orientations are distinguished by $$ WF(u) $$.

#### Seismology and reflected waves
- Problem: From reflected wave data, we want to infer internal interfaces together with their normal directions.
- Model: Singularities of the medium and of the measured data are described by wave front sets.
- Assumptions and limitations: The analysis depends on linearized wave models and visibility assumptions.
- Interpretation: The wave front set is the right object for saying which information actually enters the data.

### 2. Additional Intuition and Connections

Singular support tells us where a distribution is not smooth, while the wave front set says in which directions it is not smooth. A straight edge, a corner, and a point source may occur at the same place but have very different frequency geometry. A common misconception is that singularity is only a pointwise property; microlocally, it also has direction.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

n = 128
x = np.linspace(-1, 1, n, endpoint=False)
X, Y = np.meshgrid(x, x)
u = (X > 0).astype(float)  # jump across x = 0

U = np.fft.fftshift(np.abs(np.fft.fft2(u)))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(u, extent=[-1, 1, -1, 1], origin="lower", cmap="gray")
axes[0].set_title("A distribution with a singular edge at x = 0")
axes[1].imshow(np.log1p(U), cmap="magma")
axes[1].set_title("Fourier magnitude: dominant normal frequency directions")
for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()
```

### 4. Suggested Searches

- search: wave front set edge orientation visualization
- search: singular support vs wave front set image processing
- search: seismic singularities wave front set intuition

### 5. Worked Example

Consider the step function
$$ u(x_1,x_2)=H(x_1). $$
Its singularity lies on the line $$ x_1=0 $$, but only in directions normal to that jump, namely directions parallel to the $$ x_1 $$ axis in frequency space. So $$ WF(u) $$ says much more than "the vertical axis is singular"; it records the normal direction of the discontinuity.

### 6. Difficulty Layering

**Undergraduate level.** Compare singular support and wave front set through delta, jump, and smooth examples.

**Graduate level.** Connect to the conic definition, pullback/pushforward, and coordinate invariance.
