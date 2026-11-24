---
layout: post
title: "14-07 ΨDOs on Manifolds"
chapter: '14'
order: 7
owner: Course Team
lang: en
categories:
- chapter14
lesson_type: optional
---

> **Storytelling Hook:** The Fourier transform lives on flat Euclidean space $\mathbb{R}^n$—there is no global plane wave $e^{ix\cdot\xi}$ on a curved sphere or torus. How, then, do mathematicians run pseudo-differential calculus on curved Riemannian manifolds (and prove landmark theorems like the Atiyah–Singer Index Theorem)? By patching local Euclidean $\Psi\text{DOs}$ with partitions of unity and discovering that the **principal symbol** lives intrinsically as a function on the cotangent bundle $T^*M$.

## Learning Objectives

This lesson extends pseudo-differential operators from Euclidean space to manifolds. Students should understand why coordinate invariance matters and how local symbolic constructions are patched together geometrically.

## Prerequisites

Students should know basic pseudo-differential operators in Euclidean space and have some familiarity with manifolds, charts, and coordinate changes.

## Background Knowledge Map: Lifting $\Psi\text{DOs}$ to Curved Manifolds

Four geometric pillars make pseudo-differential operators completely coordinate-free on any smooth manifold $M$:

1. **Diffeomorphism Invariance of $\Psi^m$:** Under a smooth change of coordinates $y = \kappa(x)$, the pullback of an operator $A \in \Psi^m$ remains in $\Psi^m$! Its full symbol transforms in a messy way involving higher derivatives of $\kappa$, *except* at leading order.
2. **Principal Symbol as a Function on $T^*M$:** Under $y = \kappa(x)$, covectors transform by $\xi = (d\kappa_x)^\top \eta$, and the leading symbol satisfies $\tilde{a}_m(\kappa(x), \eta) = a_m(x, (d\kappa_x)^\top \eta)$—defining a canonical, chart-independent function $\sigma_m(A) \in S^m(T^*M)/S^{m-1}(T^*M)$.
3. **Gluing via Partitions of Unity:** An operator $A: C_c^\infty(M) \to C^\infty(M)$ lies in $\Psi^m(M)$ iff (i) its localization $\psi A \varphi$ in every coordinate chart is a Euclidean $\Psi\text{DO}$ of order $m$, and (ii) whenever $\text{supp}(\psi) \cap \text{supp}(\varphi) = \emptyset$, $\psi A \varphi$ is infinitely smoothing (pseudolocal).
4. **Elliptic Operators on Compact Manifolds Are Fredholm:** On a *compact* manifold $M$, Rellich's theorem makes smoothing remainders $R \in \Psi^{-\infty}(M)$ compact on $H^s(M)$, so a parametrix $QP = I + R$ immediately proves that every elliptic $P \in \Psi^m(M)$ has finite-dimensional kernel and cokernel!

## Introduction

![Pseudo-differential operators on manifolds]({{ site.imgurl }}/chapter_img/chapter14/07_manifolds.svg)

Many PDE problems live naturally on curved spaces rather than flat Euclidean domains. If pseudo-differential operators are to support geometric analysis, they must be formulated in a way that respects coordinate changes and manifold structure.

This lesson shows how the symbolic calculus extends beyond local coordinates into a genuinely geometric setting.

## Concept in Three Ways

### Intuitive View

Locally, a manifold looks like Euclidean space, so pseudo-differential constructions can be made in charts. The challenge is making sure these local constructions agree consistently when the coordinates change.

### Visual View

One may imagine covering the manifold with overlapping coordinate patches, defining local operators there, and then patching them together with smooth partitions of unity.

### Formal View

Pseudo-differential operators on manifolds are defined locally in coordinate charts with compatibility under coordinate transformations. Their principal symbols become geometric objects on the cotangent bundle.

## Why the Topic Matters

Modern PDE, geometry, and microlocal analysis require operator theory on manifolds, not just flat spaces. This lesson shows how the pseudo-differential framework becomes genuinely geometric.

It also prepares students for deeper applications in spectral geometry and global analysis.

## Common Misconceptions

### "Everything important happens already in Euclidean space"

No. Many natural PDE problems are geometric from the beginning.

### "A coordinate change only modifies notation"

No. It tests whether the operator theory is genuinely invariant and geometric.

### "Pseudo-differential operators on manifolds are completely different objects"

No. They are local Euclidean constructions assembled coherently.

## Suggested Learning Path

### Step 1: Recall local chart intuition

Students should remember that manifolds are locally Euclidean.

### Step 2: Define operators locally

This brings the existing Euclidean theory into charts.

### Step 3: Discuss compatibility across overlaps

This is the core geometric issue.

### Step 4: Interpret the principal symbol geometrically

The cotangent bundle becomes the natural home of the symbol.

### Checkpoints

- Can students explain why pseudo-differential theory should extend to manifolds?
- Do they understand the role of coordinate compatibility?
- Can they say why the cotangent bundle is the natural symbol space?

## Worked Examples


### Step-by-Step Worked Example (Read Slowly): Checking Principal Symbol Invariance Under a Nonlinear Change of Coordinates

Take the 1D operator $P = -\frac{d^2}{dx^2} = D_x^2$ (symbol $p(x,\xi) = \xi^2$) and transform it under the smooth diffeomorphism $y = \kappa(x) = x^3 + x$ (note $\kappa'(x) = 3x^2 + 1 \ge 1 > 0$ everywhere). Verify explicitly that the principal symbol is invariant on $T^*\mathbb{R}$ while the lower-order symbol is not!

1. **Transform derivatives using the chain rule:** Since $\frac{dy}{dx} = \kappa'(x) = 3x^2 + 1$:
   $$\frac{d}{dx} = \kappa'(x)\frac{d}{dy}, \qquad \frac{d^2}{dx^2} = \big(\kappa'(x)\big)^2\frac{d^2}{dy^2} + \kappa''(x)\frac{d}{dy}.$$
2. **Rewrite $P$ in $y$-coordinates using $D_y = -i\frac{d}{dy}$ (so $\frac{d^2}{dy^2} = -D_y^2$ and $\frac{d}{dy} = i D_y$):**
   $$\tilde{P} = \big(\kappa'(x)\big)^2 D_y^2 - i\kappa''(x) D_y = (3x^2 + 1)^2 D_y^2 - 6ix D_y.$$
3. **Read off the full symbol $\tilde{p}(y,\eta)$ in the $y$-chart:**
   $$\tilde{p}(y,\eta) = \underbrace{(3x^2 + 1)^2 \eta^2}_{\text{principal part } \tilde{p}_2} \; \underbrace{-\; 6ix\,\eta}_{\text{subprincipal part } \tilde{p}_1}.$$
4. **Check cotangent-bundle invariance ($\xi = \kappa'(x)\eta = (3x^2+1)\eta$):**
   $$\tilde{p}_2(y,\eta) = \big(\kappa'(x)\eta\big)^2 = \xi^2 = p_2(x,\xi) \quad \text{(EXACT MATCH!)}.$$
   Meanwhile, the lower-order term $-6ix\eta$ appeared purely from the curvature $\kappa''(x) = 6x$ of the coordinate chart—proving why *only* the principal symbol $\sigma_m(P)$ is coordinate-invariant on $T^*M$.

### Example 1: Local Chart Construction

A Euclidean pseudo-differential formula is written in a chart as the first step of manifold construction.

### Example 2: Partition of Unity Patching

Several local pieces are combined into a global operator.

### Example 3: Symbol Geometry

The principal symbol becomes a coordinate-invariant object on cotangent space.

## Conceptual Questions

1. Why is the cotangent bundle the natural setting for symbols on manifolds?
2. Why is coordinate invariance essential in global operator theory?
3. Why does local Euclidean analysis remain relevant even on curved spaces?

## Application Problems

1. Why are manifold-based operators central in spectral geometry?
2. How does local chart analysis support global PDE results?
3. Why is microlocal analysis fundamentally geometric in advanced settings?

## Interactive Teaching Strategies

- Use atlas and chart pictures liberally.
- Compare Euclidean local formulas with their geometric interpretation.
- Reinforce the phrase "local construction, global invariance."
- Connect symbols on manifolds to cotangent geometry visually.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the basic chart-patching idea rather than full geometric abstraction.

### Challenge for Advanced Students

Advanced students can study geometric principal symbols or Laplace-type operators on curved manifolds.

## Summary

Pseudo-differential operators extend naturally to manifolds through local chart constructions patched together geometrically. This is one of the key steps from local PDE analysis to global geometric analysis.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Waves on the Earth's surface
- Problem: Climate, geophysical, and surface-wave data naturally live on manifolds rather than flat Euclidean space.
- Model: Construct ΨDOs in local charts and patch them with a partition of unity.
- Assumptions and limitations: A differentiable atlas is required.
- Interpretation: ΨDOs on manifolds transport symbolic calculus to curved geometry.

#### Spectral analysis on curved surfaces
- Problem: Many quantum, optical, and graphics problems live on curved domains.
- Model: Use Laplace-Beltrami and related ΨDOs on manifolds.
- Assumptions and limitations: Local geometry directly influences the symbol.
- Interpretation: Frequency is now understood in the cotangent geometry of the manifold.

### 2. Additional Intuition and Connections

Microlocal analysis really lives on the cotangent bundle, so it is not tied to flat coordinates. Manifolds simply require more careful chart transitions. A common pitfall is to think ΨDOs lose meaning away from Euclidean space; in fact their geometric power is most visible there.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 120)
phi = np.linspace(0, 2 * np.pi, 240)
Theta, Phi = np.meshgrid(theta, phi)
X = np.sin(Theta) * np.cos(Phi)
Y = np.sin(Theta) * np.sin(Phi)
Z = np.cos(Theta)
U = np.cos(2 * Phi) * np.sin(Theta)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, facecolors=plt.cm.coolwarm((U - U.min()) / (U.max() - U.min())))
ax.set_title("A mode on the sphere")
plt.show()
```

### 4. Suggested Searches

- search: pseudodifferential operators on manifolds intuition
- search: Laplace Beltrami eigenfunctions sphere visualization
- search: wave propagation curved surface simulation

### 5. Worked Example

On the sphere, the Laplace-Beltrami operator plays the role of the usual Laplacian. Its eigenfunctions, the spherical harmonics, are the curved-space analogue of Fourier modes. This is the simplest concrete example of frequency analysis on a manifold.

### 6. Difficulty Layering

**Undergraduate level.** Understand the move from flat space to curved space through local charts.

**Graduate level.** Connect to cotangent bundles, invariant symbols, and geometric microlocal analysis.

## Video tham khảo

- xem trước: [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, English. Vasy sets pseudodifferential operators on manifolds, including manifolds with boundary.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 2)](https://www.youtube.com/watch?v=3DN6bKJnlXc) — Institut Fourier, English. Part 2 of the same lectures, still on manifolds and propagation.
- [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, Vietnamese. The Euclidean definition being transplanted to charts.

## References

- Taylor: geometric operator viewpoint.
- Trèves: symbolic and geometric foundations.
