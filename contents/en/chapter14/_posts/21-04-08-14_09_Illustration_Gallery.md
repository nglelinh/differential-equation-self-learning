---
layout: post
title: "Chapter 14 Illustration Gallery"
chapter: '14'
order: 9
owner: Course Team
lang: en
categories:
- chapter14
lesson_type: optional
---

> **Storytelling Hook:** A pseudo-differential symbol $a(x,\xi)$ lives in **phase space**—simultaneously displaying *where* an operator acts in space ($x$) and *which frequencies* it amplifies or silences ($\xi$). Viewing symbols, cutoffs, and off-diagonal smooth kernels side by side turns abstract Hörmander inequalities into unmistakable visual geometry.

## Purpose of This Companion Lesson

This lesson gathers the Chapter 14 illustrations into one visual review space. Pseudo-differential operators are often the point where students feel they have crossed from classical PDE techniques into a more modern language. The gallery helps that transition feel structured rather than abrupt by placing the chapter's main geometric and symbolic ideas side by side.

The core movement of the chapter is from Fourier-based intuition to operator calculus. Symbols encode frequency response, classes organize operator behavior, parametrices explain approximate inversion, and manifold constructions show that the theory is fundamentally geometric. This companion lesson lets students revisit that architecture as a coherent whole rather than as a sequence of isolated definitions.

## How to Use This Lesson

Work through the gallery in lesson order. After each figure, return to the corresponding lecture and ask what conceptual shift it is emphasizing: moving beyond local differential formulas, reading operators in frequency space, organizing symbols by asymptotic behavior, constructing operators from symbols, or proving regularity through parametrices. This helps the modern language stay connected to familiar PDE motivations.

The page is also a useful bridge into Chapter 15, where the symbolic viewpoint becomes more geometric and microlocal.

## Background Knowledge Map: Reading Phase-Space Plots of Symbols and Kernels

Keep four visual patterns in mind as you inspect the figures in this gallery:

1. **Order $m$ as Vertical Growth in $\xi$:** Positive-order symbols ($m > 0$, like $|\xi|^2$) flare upward away from $\xi = 0$ (amplifying high frequencies), zero-order symbols ($m = 0$) flatten to finite plateaus, and negative-order symbols ($m < 0$, parametrices) decay toward zero at infinity.
2. **Elliptic Characteristic Set vs. Non-Elliptic Valleys:** An elliptic symbol stays strictly away from zero for large $|\xi|$, whereas a hyperbolic wave symbol $\tau^2 - c^2|\xi|^2$ carves deep zero-valleys along the light cone—blocking global inversion.
3. **Off-Diagonal Smoothness of Schwartz Kernels:** Plotting $K_A(x,y)$ in the $(x,y)$-plane shows a sharp ridge strictly along the diagonal $x = y$ and silky smoothness everywhere off-diagonal, visualizing pseudolocality directly.
4. **Smoothing Remainders ($S^{-\infty}$):** Gaussian-like envelopes in $\xi$ collapse exponentially fast away from the origin, visually explaining why smoothing errors are negligible at high frequencies.

## Embedded Gallery

{% include interactive-frame.html
  title="Chapter 14 Illustration Gallery"
  description="A visual companion for symbol calculus, pseudo-differential operators, parametrices, manifold extensions, and elliptic regularity in modern PDE."
  path="interactives/chapter14/index-en.html"
  height="980px"
%}

### Step-by-Step Worked Example (Read Slowly): Contrasting Differential, Parametrix, and Smoothing Symbols at High Frequency

Compare three representative 1D symbols at $(x, \xi) = (0, 10)$: a second-order elliptic symbol $p(x,\xi) = (1+x^2)(1+\xi^2) \in S^2$, its leading parametrix $q_0(x,\xi) = (1+x^2)^{-1}(1+\xi^2)^{-1} \in S^{-2}$, and a smoothing symbol $r(x,\xi) = e^{-x^2 - \xi^2} \in S^{-\infty}$.

1. **Evaluate each symbol at $x = 0, \xi = 10$:**
   - Elliptic $S^2$: $p(0, 10) = 1 \cdot (1 + 100) = 101$ (amplifies mode $\xi=10$ by $\approx 10^2$).
   - Parametrix $S^{-2}$: $q_0(0, 10) = \frac{1}{101} \approx 9.90 \times 10^{-3}$ (damps mode $\xi=10$ by $\approx 10^{-2}$).
   - Smoothing $S^{-\infty}$: $r(0, 10) = e^{-100} \approx 3.72 \times 10^{-44}$ (effectively zero!).
2. **Check the product $q_0(0,10)\,p(0,10) = 1$:** While $p$ and $q_0$ balance each other across all frequencies, the smoothing remainder $r$ is already $44$ orders of magnitude smaller at $\xi = 10$—explaining why plots of $S^{-\infty}$ symbols look completely flat outside a tiny central disk around $\xi = 0$.

## Suggested Study Prompts

1. Which figures are primarily about changing viewpoint, and which are about changing technique?
2. Where does frequency-space intuition become full operator calculus?
3. How does the final regularity figure reinterpret earlier elliptic theory in the language of symbols?

## Lesson Links

- [14.00 Preparatory Review]({{ site.baseurl }}/contents/en/chapter14/14_00_Fourier_Multipliers_and_Symbols_Review/)
- [14.01 Motivation: Beyond Differential Operators]({{ site.baseurl }}/contents/en/chapter14/14_01_Motivation_Beyond_Differential_Operators/)
- [14.02 Fourier Transform and Symbol Calculus]({{ site.baseurl }}/contents/en/chapter14/14_02_Fourier_Transform_Symbol_Calculus/)
- [14.03 Symbol Classes]({{ site.baseurl }}/contents/en/chapter14/14_03_Symbol_Classes/)
- [14.04 Pseudo-Differential Operators: Definition]({{ site.baseurl }}/contents/en/chapter14/14_04_Pseudo_Differential_Operators_Definition/)
- [14.05 Composition and Adjoints]({{ site.baseurl }}/contents/en/chapter14/14_05_Composition_Adjoints/)
- [14.06 Elliptic Operators and Parametrices]({{ site.baseurl }}/contents/en/chapter14/14_06_Elliptic_Operators_Parametrices/)
- [14.07 PsiDOs on Manifolds]({{ site.baseurl }}/contents/en/chapter14/14_07_PDOs_on_Manifolds/)
- [14.08 Applications: Elliptic Regularity Revisited]({{ site.baseurl }}/contents/en/chapter14/14_08_Elliptic_Regularity_Revisited/)

## Video tham khảo

- xem trước: [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, Vietnamese. The symbol picture the gallery is trying to draw.
- [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, English. Fourier space, the screen those symbols act on.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, English. A research lecture to show what the pictures are preparing for.
