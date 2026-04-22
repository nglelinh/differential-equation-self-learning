---
layout: post
title: "Fourier Integral Operators"
chapter: '15'
order: 3
owner: Lê Minh Hoàng
lang: en
categories:
- chapter15
lesson_type: required
---

![Fourier integral operators and the transformation of wave fronts]({{ site.imgurl }}/chapter_img/chapter15/03_fourier_integral_operators.svg )

## Objectives

This lesson introduces Fourier integral operators as the natural class of operators describing wave propagation and wave-front transformation. After the lesson, students should understand how FIO differ from pseudodifferential operators, the roles of phase functions and amplitudes, and why FIO are the right language for propagation of singularities.

## Prerequisites

Students should know pseudodifferential operators, wave front sets, and the idea that propagation of singularities requires more than frequency-local filtering. Some intuition from oscillatory phases and Hamilton-Jacobi ideas is also useful.

## Introduction

Pseudodifferential operators are powerful, but they still behave mainly like local frequency filters. In many wave problems, that is not enough. Waves are not only filtered. They are transported, refocused, scattered, phased, and geometrically transformed. To describe these effects, we need a broader class of operators: Fourier integral operators.

If pseudodifferential operators are the language of "modify amplitude locally in frequency," then Fourier integral operators are the language of "move and bend wave fronts."

## The Concept in Three Ways

### Intuitive View

Think of a beam of light passing through a lens. The lens does not merely make the beam stronger or weaker. It changes the phase and the direction of propagation of the entire wave pattern. Fourier integral operators play an analogous role for oscillatory components of a solution.

### Visual View

A good classroom picture starts with one wave front before propagation and another after propagation. With pseudodifferential operators, students are used to thinking "each frequency gets multiplied by a factor." With FIO, the phase function actually pushes the wave front to a new position and a new direction in phase space.

### Formal View

A typical FIO has the form

$$
Tu(x)=\int e^{i\phi(x,\xi)}a(x,\xi)\widehat{u}(\xi)\,d\xi,
$$

where

- $$ \phi(x,\xi) $$ is a phase function,
- $$ a(x,\xi) $$ is an amplitude.

When the phase is simply $$ \phi(x,\xi)=x\cdot \xi $$, we recover the familiar pseudodifferential form. So FIO really do extend the pseudodifferential class.

## Common Misconceptions

### "An FIO is just a pseudodifferential operator written in a longer way"

No. The real difference is the nontrivial phase function, which carries geometry.

### "The amplitude is the main part"

Not always. For propagation questions, the phase often carries the decisive geometric information.

### "FIO only belong to wave physics"

False. They are central in inverse problems, geometry, spectral theory, and imaging.

### "If the phase function looks abstract, then there is no intuitive meaning"

False. Even before mastering the full formalism, students can understand FIO as operators that transport wave fronts.

## Learning Progression

### Step 1: Review pseudodifferential operators

Emphasize their strength, but also their limitation as mainly local frequency filters.

### Step 2: Introduce the phase function

This is the term that creates geometry rather than mere multiplication.

### Step 3: Connect to propagation

FIO are the natural operator class that implements the movement of singularities.

### Step 4: Place FIO in the larger picture

Many solution operators for hyperbolic PDE can be represented microlocally by FIO.

### Key Checkpoints

- Can students explain how FIO go beyond pseudodifferential operators?
- Can they say why the phase function controls geometry?
- Can they connect FIO with propagation of singularities?

## Worked Examples

### Example 1: Recovering a pseudodifferential operator

If $$ \phi(x,\xi)=x\cdot \xi $$, then

$$
Tu(x)=\int e^{ix\cdot\xi}a(x,\xi)\widehat{u}(\xi)\,d\xi,
$$

which is the standard form of a pseudodifferential operator. This example shows that FIO contain the pseudodifferential class as a special case.

### Example 2: A translation operator

If the phase is chosen so that $$ \phi(x,\xi)=(x-y_0)\cdot\xi $$, then the operator effectively translates the input. Even in this simple case, the phase does something geometric rather than merely multiplying frequencies.

### Example 3: Wave propagation

Solution operators for the wave equation are not purely local frequency multipliers. They transport singularities along geometric rays. That is why they are modeled microlocally by FIO rather than by ordinary pseudodifferential operators.

### Example 4: Imaging interpretation

In tomography or scattering, the data operator often maps singularities from one geometric configuration to another. FIO provide the correct framework for describing which singularities are moved, seen, or hidden by the measurement process.

## Conceptual Questions

1. Why is a nontrivial phase function the real source of geometry in an FIO?
2. Why are pseudodifferential operators not enough for propagation problems?
3. Why should solution operators for wave equations naturally belong to an FIO class?

## Application Problems

1. In optics, how does a lens motivate the need for an operator that changes direction and phase, not only amplitude?
2. In seismic imaging, why is it useful to model the data map by an FIO?
3. In wave propagation, how does the geometry of rays enter the operator acting on the initial data?

## Interactive Teaching Strategies

### Questions to Ask in Class

- What can an FIO do that a pseudodifferential operator cannot?
- Why is phase more geometric than amplitude?
- If singularities move, what kind of operator should implement that movement?

### Suggested Activities

- Compare a pseudodifferential formula and an FIO formula side by side.
- Ask students to describe what the phase function is doing in plain language.
- Use propagation diagrams to show how singularities are pushed through phase space.

### Participation Moves

- Begin from wave or optics intuition before symbol calculus.
- Ask students to explain the operator in terms of moving wave fronts.
- Revisit the question "filtering versus transporting" repeatedly.

## Differentiation

### Support for Struggling Students

- Start from the slogan "pseudodifferential operators filter; FIO transport."
- Use the wave equation as the main anchor example.
- Keep the phase-amplitude distinction explicit and visual.

### Challenge for Advanced Students

- Study canonical relations associated with FIO.
- Connect FIO with symplectic geometry and Hamiltonian flow.
- Explore how FIO act on wave front sets in a precise microlocal theorem.

## Quick Summary

Fourier integral operators extend pseudodifferential operators by adding nontrivial oscillatory phase. They are the natural tools for describing how wave fronts move through phase space.

---

## Real-World Applications

### 1. Seismic migration

A seismic migration operator takes recorded wave data at the surface and back-projects it into the subsurface. Microlocally, this operator is modeled by an FIO because it maps singularities in the data to singularities of geological interfaces. A schematic representation is

$$
Tu(x)=\int e^{i\phi(x,\xi)} a(x,\xi) \widehat{u}(\xi)\,d\xi.
$$

The model assumes high-frequency propagation and a reasonably known background velocity. Its limitation is that strong multipathing and complex attenuation can break the clean FIO picture. The interpretation is powerful: migration does not merely sharpen data, it geometrically relocates wave fronts.

### 2. Synthetic aperture radar

Radar measurements collected along a moving platform can be described by oscillatory integrals that convert reflected waves into an image of the ground. The forward map and reconstruction map are both often FIO-like. The assumption is that the wavelength is short relative to feature size and that the propagation model is approximately linear. The main interpretation is that image artifacts and resolution limits are encoded in the canonical relation of the operator.

### 3. Geometric optics and lensing

A lens changes phase, not just amplitude. In a high-frequency approximation, a wave field after passing through a lens is modeled by an oscillatory operator whose phase encodes refraction. The main limitation is that diffraction beyond geometric optics is only partly captured. The solution is interpreted as a transformed wave front rather than a pointwise multiplication in frequency.

## Conceptual Insight

The simplest way to think about an FIO is as an operator that moves geometry. Pseudodifferential operators act like local filters in phase space, while FIO act like transport maps between phase-space configurations. A common pitfall is to focus only on the amplitude. For propagation questions, the phase function is usually the part that tells the real story.

## Visualizations and Computation

### Python

This toy model tracks a curve in phase space through a simple canonical transformation.

```python
import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(-2, 2, 300)
x0 = s
xi0 = np.sin(2 * s)

# Simple canonical-like map: free propagation for time t
t = 1.0
x1 = x0 + t * xi0
xi1 = xi0

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(x0, xi0)
axes[0].set_title('Initial wave front in phase space')
axes[1].plot(x1, xi1, color='crimson')
axes[1].set_title('After canonical transport')
for ax in axes:
    ax.set_xlabel('x')
    ax.set_ylabel('xi')
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### JavaScript

```html
<div id="fio-map"></div>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<script>
const s = Array.from({length: 200}, (_, i) => -2 + 4 * i / 199);
const x0 = s;
const xi0 = s.map(v => Math.sin(2 * v));
const x1 = x0.map((v, i) => v + xi0[i]);
Plotly.newPlot('fio-map', [
  {x: x0, y: xi0, mode: 'lines', name: 'initial'},
  {x: x1, y: xi0, mode: 'lines', name: 'transported'}
], {title: 'Toy canonical transformation', xaxis: {title: 'x'}, yaxis: {title: 'xi'}});
</script>
```

### External References

Search for `Fourier integral operator canonical relation`, `seismic migration FIO`, or `synthetic aperture radar microlocal analysis`.

## Difficulty Layering

### Undergraduate Level

At this level, treat FIO as operators that carry sharp features from one place and direction to another. The main comparison is with pseudodifferential operators: filter versus transport.

### Graduate Level

Students should study phase nondegeneracy, canonical relations, composition theorems, and the action of FIO on wave front sets. This is where symplectic geometry and microlocal propagation fully enter the subject.

> See the full gallery of chapter interactives here: [Chapter 15 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter15/15_10_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Tomography and backprojection
- Problem: Radon-type measurement operators and reconstruction operators carry singularities from the object to the data and back.
- Model: Such operators are often Fourier integral operators (FIOs), mapping wave front sets by canonical relations.
- Assumptions and limitations: The geometry of measurement and visibility is crucial.
- Interpretation: FIOs are the right language for transporting singularities rather than merely filtering them.

#### Wave propagators
- Problem: The solution operator for a hyperbolic PDE moves initial singularities through phase space.
- Model: Hyperbolic evolution operators are often FIOs.
- Assumptions and limitations: One needs a nondegenerate phase.
- Interpretation: FIOs encode how singularities move along canonical transformations.

### 2. Additional Intuition and Connections

Pseudodifferential operators mostly filter local frequency content; FIOs also transport singularities from one location-direction pair to another. They can be thought of as operators flowing along geometric optics. A common misconception is to view FIOs as merely more complicated ΨDOs; the canonical relation is the real new ingredient.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 600)
u = np.exp(-8 * (x + 1.5)**2) * np.cos(18 * x)
shift = 1.2
Tu = np.exp(-8 * (x - shift + 1.5)**2) * np.cos(18 * (x - shift))

plt.plot(x, u, label="initial wave packet")
plt.plot(x, Tu, label="after an FIO-like transport")
plt.legend()
plt.title("An operator transporting a wave packet")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Fourier integral operator intuition wave propagation
- search: Radon transform singularities canonical relation
- search: FIO wave packet propagation visualization

### 5. Worked Example

The translation operator
$$ (Tu)(x)=u(x-a) $$
can be written as an FIO with linear phase. It moves singularities from $$ x_0 $$ to $$ x_0+a $$ while preserving their frequency direction. This is the simplest model of how an FIO transports the wave front set.

### 6. Difficulty Layering

**Undergraduate level.** Understand FIOs as operators that transport singularities.

**Graduate level.** Connect to canonical relations, nondegenerate phase functions, and wave front set mapping theorems.
