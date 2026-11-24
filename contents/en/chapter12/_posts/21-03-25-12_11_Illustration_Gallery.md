---
layout: post
title: "Chapter 12 Illustration Gallery"
chapter: '12'
order: 11
owner: Course Team
lang: en
categories:
- chapter12
lesson_type: optional
---

> **Storytelling Hook:** Infinite-dimensional Banach and Hilbert spaces can feel intimidatingly abstract—until you see their geometric footprints in two dimensions. From the diamond-to-square morphing of $L^p$ unit balls to high-frequency waves that vanish weakly while keeping constant energy, these illustrations make functional analysis tangible.

## Purpose of This Companion Lesson

This lesson gathers the Chapter 12 illustrations into one visual review space. Functional analysis can feel abstract when students first meet it, especially after several chapters driven by explicit differential-equation models. The gallery helps preserve the thread that runs through the chapter: all of these objects, spaces, and theorems were built to make PDE solvable, stable, and interpretable beyond the classical setting.

The main lessons move from norms and weak derivatives to Sobolev spaces, weak formulations, variational existence theory, and regularity. This companion page makes that progression easier to see as one connected architecture rather than a list of abstract definitions. It also places the optional topics, such as spectral theory and distributions, back into the same conceptual map.

## How to Use This Lesson

Work through the gallery in lesson order. After each figure, return to the corresponding lecture and ask what problem the concept is solving: how to measure a function, how to differentiate nonsmooth data, how to formulate a PDE weakly, how to prove existence, or how to recover regularity. This helps functional analysis stay tied to motivation rather than floating as separate theory.

The page is also a useful review before the later chapters on numerical analysis, pseudodifferential operators, and microlocal analysis, all of which reuse the language of operators, weak formulations, and generalized objects.

## Background Knowledge Map: Visual Anchors for Functional Analysis in PDEs

Use four visual lenses as you explore the diagrams in this gallery:

1. **Unit Ball Geometry ($L^1$ Diamond, $L^2$ Circle, $L^\infty$ Square):** The smoothness and strict convexity of the $L^2$ ball reflect unique orthogonal projections, while the sharp corners of $L^1$ and $L^\infty$ explain why projections onto subspaces can lose uniqueness.
2. **Weak vs. Strong Convergence via Rapid Oscillation:** Sequences like $\sin(nx)$ average to zero against any smooth test function (weak convergence) even though their $L^2$ amplitude never shrinks (failure of strong convergence).
3. **Sobolev Norms as High-Frequency Penalties:** Because differentiation multiplies Fourier mode $k$ by $ik$, plotting $|\hat{u}(k)|$ versus $k|\hat{u}(k)|$ visually reveals why $H^1$ suppresses jagged oscillations that $L^2$ ignores.
4. **Dirac Delta Approximations (Mollifiers):** Narrowing unit-area Gaussian bells illustrate how distributions arise as limits of smooth functions whose pointwise peak diverges while their integral action converges cleanly.

## Embedded Gallery

{% include interactive-frame.html
  title="Chapter 12 Illustration Gallery"
  description="A visual companion for Lp spaces, weak derivatives, Sobolev spaces, weak PDE formulations, Lax-Milgram, elliptic regularity, spectral theory, distributions, and Sobolev geometry."
  path="interactives/chapter12/index-en.html"
  height="980px"
%}

### Step-by-Step Worked Example (Read Slowly): Watching Strong $L^2$ Convergence Fail in $H^1$

Consider the sequence of smooth functions $v_n(x) = \frac{1}{n}\sin(nx)$ on $(0, \pi)$. Compute both $\|v_n\|_{L^2(0,\pi)}$ and $\|v_n'\|_{L^2(0,\pi)}$ to see firsthand why $v_n \to 0$ strongly in $L^2$ yet only *weakly* in $H^1$.

1. **Compute the $L^2$ norm:** Using $\int_0^\pi \sin^2(nx)\,dx = \frac{\pi}{2}$,
   $$\|v_n\|_{L^2(0,\pi)} = \frac{1}{n}\sqrt{\frac{\pi}{2}} \xrightarrow{n \to \infty} 0.$$
   Thus $v_n \to 0$ strongly in $L^2(0,\pi)$ (and even uniformly, since $|v_n(x)| \le 1/n$).
2. **Compute the derivative's $L^2$ norm:** Differentiating gives $v_n'(x) = \cos(nx)$, whose amplitude never shrinks:
   $$\|v_n'\|_{L^2(0,\pi)} = \left(\int_0^\pi \cos^2(nx)\,dx\right)^{1/2} = \sqrt{\frac{\pi}{2}} \not\to 0.$$
   Hence $v_n$ does **not** converge strongly to $0$ in $H^1(0,\pi)$!
3. **Verify weak convergence $v_n \rightharpoonup 0$ in $H^1(0,\pi)$:** For any smooth test function $\varphi \in C^1([0,\pi])$, integration by parts gives:
   $$\int_0^\pi v_n'(x)\varphi'(x)\,dx = \int_0^\pi \cos(nx)\varphi'(x)\,dx = \left[\frac{\sin(nx)}{n}\varphi'(x)\right]_0^\pi - \frac{1}{n}\int_0^\pi \sin(nx)\varphi''(x)\,dx \to 0$$
   (by Riemann–Lebesgue). Visually, the ripples shrink in height like $1/n$ while crowding $n$ times faster—keeping their total slope energy constant while cancelling out against every smooth observer.

## Suggested Study Prompts

1. Which figures are primarily about measuring functions, and which are about solving PDEs?
2. Where does the chapter move from definitions to theorem-driven existence and regularity?
3. How do the optional topics complete the overall functional-analytic picture rather than standing apart from it?

## Lesson Links

- [12.01 Lp Spaces]({{ site.baseurl }}/contents/en/chapter12/12_01_Lp_Spaces/)
- [12.02 Weak Derivatives]({{ site.baseurl }}/contents/en/chapter12/12_02_Weak_Derivatives/)
- [12.03 Sobolev Spaces]({{ site.baseurl }}/contents/en/chapter12/12_03_Sobolev_Spaces/)
- [12.04 Weak Solutions of PDEs]({{ site.baseurl }}/contents/en/chapter12/12_04_Weak_Solutions_PDEs/)
- [12.05 The Lax-Milgram Theorem]({{ site.baseurl }}/contents/en/chapter12/12_05_Lax_Milgram_Theorem/)
- [12.06 Elliptic Regularity]({{ site.baseurl }}/contents/en/chapter12/12_06_Elliptic_Regularity/)
- [12.07 Spectral Theory]({{ site.baseurl }}/contents/en/chapter12/12_07_Spectral_Theory/)
- [12.08 Distributions]({{ site.baseurl }}/contents/en/chapter12/12_08_Distributions/)
- [12.09 Minkowski Inequality]({{ site.baseurl }}/contents/en/chapter12/12_09_Minkowski_Inequality/)
- [12.10 Sobolev Theory]({{ site.baseurl }}/contents/en/chapter12/12_10_Sobolev_Theory/)

## Video tham khảo

- xem trước: [Dirac Delta: Not a Function but a Distribution](https://www.youtube.com/watch?v=XZKf1G5ATkM) — Scintropy, English. The delta distribution, the picture this functional-analysis gallery starts from.
- [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, English. Sobolev regularity as a gain of weak derivatives.
- [Peter Lax - Lax-Milgram Theorem](https://www.youtube.com/watch?v=d6lx6kKV9-E) — Simons Foundation, English. Lax-Milgram from its author, the theorem the frames are about.
