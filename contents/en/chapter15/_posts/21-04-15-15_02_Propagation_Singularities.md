---
layout: post
title: "Propagation of Singularities"
chapter: '15'
order: 2
owner: Lê Minh Hoàng
lang: en
categories:
- chapter15
lesson_type: required
---

![Propagation of singularities along PDE characteristics]({{ site.imgurl }}/chapter_img/chapter15/02_propagation_singularities.svg )

## Objectives

This lesson introduces one of the most beautiful results in microlocal analysis: singularities do not move randomly but follow the geometry of the equation. After the lesson, students should understand the intuition behind propagation of singularities, the role of characteristics and bicharacteristics, and why hyperbolic equations behave very differently from elliptic ones.

## Prerequisites

Students should know wave front sets, principal symbols, and the basic idea of characteristics from transport or wave equations. It is also helpful to remember from earlier PDE chapters that wave equations tend to carry singular features along moving fronts rather than smoothing them immediately.

## Introduction

One of the major achievements of microlocal analysis is the discovery that singularities have trajectories. If a PDE solution has a singularity, that singularity does not simply vanish or spread out chaotically. Instead, it moves along curves determined by the principal symbol of the operator. This is a far more refined version of the classical slogan that waves travel along characteristics.

The result is not only conceptually elegant. It is also foundational for wave analysis, inverse problems, geometric optics, scattering, and imaging.

## The Concept in Three Ways

### Intuitive View

Imagine dropping a stone into a calm lake. The disturbance does not instantly appear everywhere. It propagates along moving wave fronts with a definite geometric structure. If the initial disturbance is a singularity, then the governing PDE and the geometry of the medium determine where that singularity goes next. Microlocal propagation is the phase-space version of this story.

### Visual View

A very good first picture is the one-dimensional wave equation: a singularity at time zero splits into two branches, one moving left and one moving right. Then lift that picture into phase space by attaching a cotangent direction. The correct trajectories are bicharacteristics, which live in phase space rather than only in physical space.

### Formal View

For a principal-type operator $$ P $$ with principal symbol $$ p(x,\xi) $$, singularities of solutions to $$ Pu=f $$ are governed by the characteristic set $$ \{(x,\xi):p(x,\xi)=0\} $$ and propagate along the Hamilton flow of $$ p $$, that is, along bicharacteristics. In short:

- singularities of $$ f $$ may create singularities of $$ u $$,
- away from those sources, singularities of $$ u $$ move along Hamiltonian trajectories in phase space.

## Comparing Three PDE Classes

Students often remember this topic best when three behaviors are placed side by side:

- elliptic equations tend to smooth singularities,
- parabolic equations usually damp high frequencies rapidly in time,
- hyperbolic equations transport singularities along geometric rays.

So when students hear "propagation of singularities," they should think first of hyperbolic or principal-type equations, not of PDE in general.

## Common Misconceptions

### "Singularities only move in physical space, so direction is optional"

False. The directional component in phase space is essential to the theorem.

### "Every PDE propagates singularities"

No. Elliptic equations usually smooth them rather than transport them.

### "Characteristics and bicharacteristics are exactly the same thing"

They are closely related, but bicharacteristics live in phase space and therefore contain richer information.

### "If the initial data is smooth, then no later singularity can ever matter"

In many hyperbolic settings, new singularities do not arise without a source or boundary mechanism, but the exact statement depends on the problem.

## Learning Progression

### Step 1: Review the wave equation

Students often already believe that singular features travel with wave fronts.

### Step 2: Move from characteristics to phase space

Introduce the principal symbol and the Hamilton flow.

### Step 3: State the theorem at the level of ideas

The geometric mechanism matters more than a full proof on the first pass.

### Step 4: Contrast with elliptic smoothing

This is where students see why microlocal analysis is necessary.

### Key Checkpoints

- Can students explain why bicharacteristics are needed?
- Can they distinguish hyperbolic transport from elliptic smoothing?
- Can they say why the principal symbol determines the route of singularities?

## Worked Examples

### Example 1: The transport equation

Consider $$ u_t+cu_x=0 $$. Solutions have the form $$ u(x,t)=u_0(x-ct) $$. So any jump or corner in the initial data simply moves along straight lines of slope $$ c $$. This is the simplest propagation model.

### Example 2: The one-dimensional wave equation

For $$ u_{tt}-c^2u_{xx}=0 $$, the solution splits into left-moving and right-moving pieces. A singularity initially localized at one point is transported along two characteristic branches. This is the basic physical picture behind propagation theorems.

### Example 3: Why elliptic equations behave differently

For the Poisson equation $$ -\Delta u=f $$, singularities are not transported along rays in the same way. Instead, elliptic regularity shows that away from the singularities of $$ f $$, the solution becomes smoother. This sharp contrast is one of the main conceptual lessons of the topic.

### Example 4: Phase-space refinement

Two singularities may sit at the same spatial point but point in different cotangent directions. Propagation theory distinguishes them because different directions may follow different bicharacteristics. This is why wave front sets are the right language.

## Conceptual Questions

1. Why is the phrase "singularities have trajectories" more accurate than saying singularities simply spread?
2. Why does Hamiltonian geometry naturally appear in a PDE theorem?
3. Why must propagation of singularities be formulated in phase space rather than in physical space alone?

## Application Problems

1. In acoustics, why do sharp sound features follow travel-time geometry instead of disappearing immediately?
2. In seismic imaging, why is it so important to know which singularities can reach the detectors?
3. In geometric optics, how is the motion of singularities related to ray tracing?

## Interactive Teaching Strategies

### Questions to Ask in Class

- If a singularity starts at one point, what should determine where it moves next?
- Why should wave equations transport singularities while elliptic equations smooth them?
- What information is lost if we forget the cotangent direction?

### Suggested Activities

- Draw the motion of a jump under a transport equation.
- Compare propagation pictures for the wave equation and smoothing pictures for elliptic equations.
- Have students sketch the difference between a characteristic curve in space-time and a bicharacteristic in phase space.

### Participation Moves

- Begin from a physical wave picture before introducing symbols.
- Ask students to narrate the theorem as a geometric story.
- Encourage comparisons with earlier PDE classes the students already know.

## Differentiation

### Support for Struggling Students

- Stay close to the transport and one-dimensional wave equations.
- Use the slogan "hyperbolic PDE carry singularities along rays."
- Delay full Hamiltonian formalism until the geometric picture is secure.

### Challenge for Advanced Students

- Study the Hamilton vector field of a model symbol.
- Compare propagation in variable-coefficient wave equations.
- Explore boundary reflection and how singularities interact with geometry.

## Quick Summary

Propagation of singularities says that singularities of many hyperbolic or principal-type PDE travel along bicharacteristics determined by the principal symbol. Singularities are not random; they follow geometry.

---

## Real-World Applications

### 1. Seismic travel-time analysis

In seismic imaging, impulsive sources generate waves that travel through an inhomogeneous earth. A simplified model is $$ u_{tt}-c(x)^2\Delta u=0 $$. A sharp reflector or source pulse creates singularities that move along rays determined by the Hamiltonian associated with $$ \tau^2-c(x)^2\lvert \xi\rvert^2 $$. The model assumes linear acoustics and ignores strong attenuation and nonlinear effects. The solution is interpreted geometrically: travel times, reflections, and caustics are not arbitrary artifacts, but organized consequences of bicharacteristic flow.

### 2. Ultrasound and pulse echo imaging

Medical ultrasound relies on pulses that travel through tissue and reflect at interfaces where acoustic impedance changes. The forward model is again wave-like, and the returning echoes are strongest when the interface geometry sends singularities back toward the detector. The model assumes weak scattering and sufficiently short pulses. The main limitation is that multiple scattering and tissue heterogeneity complicate the ideal ray picture. Still, propagation theory explains why some anatomical edges are seen sharply and others remain faint or distorted.

### 3. Traffic and transport of discontinuities

A simpler first-order example is the transport equation $$ u_t + c u_x = 0 $$, or, in nonlinear traffic form, $$ \rho_t + (\rho v(\rho))_x = 0 $$. Here a density jump moves along characteristics and may steepen into a shock. The model assumes one-dimensional flow and ignores stochastic driver behavior. Its interpretation is still valuable: sharp features in the data move along curves dictated by the PDE, not by pointwise diffusion.

## Conceptual Insight

This topic is the phase-space refinement of the statement "waves follow rays." The extra microlocal content is that one does not merely follow a disturbance in space-time; one follows a disturbance together with its frequency direction. A common misconception is to imagine that a singularity spreads like dye in water. Hyperbolic propagation is much more rigid: singularities travel along specific geometric paths, while elliptic and parabolic equations behave very differently.

## Visualizations and Computation

### Python

The script below compares a transported jump and a two-branch wave pulse.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 800)
t = 1.5
c = 1.2

u0 = (x < 0).astype(float)
transport = (x - c * t < 0).astype(float)
wave = np.exp(-((x - c * t) + 2)**2 / 0.3) + np.exp(-((x + c * t) + 2)**2 / 0.3)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(x, u0, label='initial jump')
axes[0].plot(x, transport, label='transported jump at t=1.5')
axes[0].set_title('Transport equation: singularity moves along one branch')
axes[0].legend()
axes[1].plot(x, wave, color='crimson')
axes[1].set_title('Wave equation: one pulse splits into left/right branches')
axes[1].set_xlabel('x')
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### JavaScript

```html
<div id="propagation-demo"></div>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<script>
const x = Array.from({length: 300}, (_, i) => -6 + 12 * i / 299);
const t = 1.5, c = 1.2;
const transport = x.map(v => (v - c * t < 0 ? 1 : 0));
const left = x.map(v => Math.exp(-((v + c * t) + 2) ** 2 / 0.3));
const right = x.map(v => Math.exp(-((v - c * t) + 2) ** 2 / 0.3));
Plotly.newPlot('propagation-demo', [
  {x, y: transport, mode: 'lines', name: 'transported jump'},
  {x, y: left, mode: 'lines', name: 'left-moving pulse'},
  {x, y: right, mode: 'lines', name: 'right-moving pulse'}
], {title: 'Propagation of singular features', xaxis: {title: 'x'}});
</script>
```

### External References

Search for `wave equation bicharacteristics`, `seismic ray tracing singularities`, or `hyperbolic PDE propagation visualization`.

## Difficulty Layering

### Undergraduate Level

Keep the focus on transport equations, d'Alembert's formula, and the idea that corners and jumps move along characteristics. The main learning goal is geometric intuition, not the full theorem.

### Graduate Level

Develop the Hamilton vector field, the characteristic set, and Hörmander's propagation theorem for principal-type operators. At this level students should understand why phase space, not only space-time, is essential.

> See the full gallery of chapter interactives here: [Chapter 15 Interactive Gallery]({{ site.baseurl }}/contents/en/chapter15/15_10_Interactive_Gallery/)

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Seismic waves
- Problem: Discontinuities in the medium generate singularities that move along wave rays.
- Model: For hyperbolic operators of principal type, $$ WF(u) $$ propagates along bicharacteristics of the principal symbol.
- Assumptions and limitations: Linearized wave models and sufficiently smooth coefficients are assumed.
- Interpretation: Singularities do not move arbitrarily; they follow Hamiltonian geometry.

#### Ultrasound and radar
- Problem: Short pulses reflect from objects and carry back singular features of the target.
- Model: Singularities of wave solutions propagate along characteristics in phase space.
- Assumptions and limitations: Visibility and measurement geometry matter.
- Interpretation: If we know the propagation law, we know where to look for recoverable information in the data.

### 2. Additional Intuition and Connections

In wave equations, corners and jumps do not instantly disappear the way they do in the heat equation. They move along characteristics or bicharacteristics. A common pitfall is to think singularities propagate only in physical space; the correct theorem lives in phase space because direction is essential.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
t = np.linspace(0, 1.5, 240)
X, T = np.meshgrid(x, t)
c = 1.0
u = (X - c * T > 0).astype(float)

plt.figure(figsize=(7, 4))
plt.contourf(X, T, u, levels=[-0.1, 0.5, 1.1], cmap="coolwarm")
plt.plot(c * t, t, "k--", label="characteristic x = ct")
plt.xlabel("x")
plt.ylabel("t")
plt.title("A jump set propagating along characteristics")
plt.legend()
plt.show()
```

### 4. Suggested Searches

- search: propagation of singularities wave equation animation
- search: bicharacteristics intuition microlocal analysis
- search: seismic ray tracing singularity propagation

### 5. Worked Example

For the transport equation
$$ u_t + c u_x = 0, \qquad u(x,0)=H(x), $$
the solution is
$$ u(x,t)=H(x-ct). $$
The initial jump at $$ x=0 $$ moves to the jump $$ x=ct $$. This is the simplest model of propagation of singularities.

### 6. Difficulty Layering

**Undergraduate level.** Track singularities along characteristics in 1D examples.

**Graduate level.** Connect to Hamilton vector fields, principal type operators, and Hormander's propagation theorem.
