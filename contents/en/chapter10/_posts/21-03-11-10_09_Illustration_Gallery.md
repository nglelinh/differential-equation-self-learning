---
layout: post
title: "Chapter 10 Illustration Gallery"
chapter: '10'
order: 9
owner: Course Team
lang: en
categories:
- chapter10
lesson_type: optional
---

Waves are inherently kinetic—they split into left- and right-moving twins, flip upside down at a clamped wall, scatter into reflected and transmitted pulses at an impedance jump, and separate into leading swells and trailing ripples under dispersion. This interactive gallery lets you watch every single phenomenon of Chapter 10 unfold in motion, turning static PDE formulas into physical intuition.

## Key ideas: Reading the Chapter 10 Visual Lab

1. **D'Alembert Splitting & Light Cones:** Launch a localized initial bump with zero velocity and watch it cleave cleanly into two half-height pulses racing apart at $$ \pm c $$; switch to initial velocity and watch an expanding flat plateau appear!
2. **Standing Waves vs. Traveling Waves:** Toggle between a single Fourier mode $$ \sin(n\pi x/L)\cos(\omega_n t) $$ and its two opposite traveling-wave components to see how interference creates fixed nodes.
3. **Interface Reflection & Phase Flip:** Adjust the density ratio $$ \rho_2/\rho_1 $$ across the junction and observe how entering a heavier medium flips the reflected wave upside down ($$ R < 0 $$) while entering a lighter medium reflects it upright ($$ R > 0 $$).
4. **Dispersion Packet Spreading:** In the dispersive frame, track an individual crest moving at $$ v_p $$ sliding *through* the slower-moving packet envelope traveling at $$ v_g $$!

### Worked example: Predicting a Double-Bounce Collision in the Gallery

**Problem:** A finite string of length $$ L = 4 $$ with wave speed $$ c = 1 $$ and fixed ends ($$ u(0,t)=u(4,t)=0 $$) starts from rest with a narrow triangular pulse of height $$ 1 $$ centered at $$ x = 2 $$. Using d'Alembert's odd-periodic reflection rule, predict the exact string state at $$ t = 2 $$, $$ t = 4 $$, and $$ t = 8 $$.

1. **At $$ t = 0^+ $$:** The height-$$ 1 $$ pulse splits into two height-$$ 0.5 $$ pulses moving left and right at speed $$ c = 1 $$.
2. **At $$ t = 2 $$ (hitting the walls $$ x = 0 $$ and $$ x = 4 $$):** Both half-pulses arrive simultaneously at the clamped walls and reflect **inverted** (height $$ -0.5 $$). Right at $$ t = 2 $$, incoming $$ +0.5 $$ and reflected $$ -0.5 $$ cancel momentarily, leaving the string completely flat ($$ u(x, 2) = 0 $$ everywhere, with all energy stored as kinetic velocity!).
3. **At $$ t = 4 $$ (mid-string collision):** Both inverted height-$$ (-0.5) $$ pulses meet at $$ x = 2 $$ and superpose to form an exact **upside-down copy** of the original triangle of height $$ -1 $$!
4. **At $$ t = 8 $$ (one full period $$ T = 2L/c = 8 $$):** After bouncing and flipping upright a second time, the string returns identically to its original $$ t = 0 $$ shape of height $$ +1 $$ at $$ x = 2 $$!

## Purpose of This Companion Lesson

This lesson gathers the Chapter 10 illustrations into one visual review space. The wave equation introduces students to a very different PDE worldview from the heat equation: information travels rather than immediately smooths, energy is transported rather than dissipated, and geometry enters through boundaries, interfaces, and domains of propagation. The gallery helps those themes remain visible as the chapter moves from derivation to applications.

The main lessons develop the formal derivations and solution methods. This companion lesson gives students a way to compare the full chapter at a glance: traveling versus standing waves, finite-speed propagation versus diffusion, conservation laws versus damping, and one-dimensional strings versus higher-dimensional media. That comparison is especially useful when the course begins to distinguish hyperbolic, parabolic, and elliptic behavior more sharply.

## How to Use This Lesson

Work through the gallery in lesson order. After each figure, return to the corresponding lecture and ask what mathematical feature the image is encoding: force balance, characteristic propagation, eigenmode structure, geometric spreading, energy conservation, interface matching, or physical interpretation. This makes the page a bridge between formulas and wave intuition.

The lesson is also a good review before Chapter 11, because it clarifies which features belong specifically to wave propagation and which will disappear in elliptic problems.

## Embedded Gallery

{% include interactive-frame.html
  title="Chapter 10 Illustration Gallery"
  description="A visual companion for derivation, propagation, standing modes, higher-dimensional geometry, energy identities, boundary interactions, and applications of the wave equation."
  path="interactives/chapter10/index-en.html"
  height="980px"
%}

## Suggested Study Prompts

1. Which figures emphasize finite-speed transport, and which emphasize boundary- or geometry-driven structure?
2. Where do you see the clearest contrast between wave behavior and heat diffusion?
3. How do the later application figures reinterpret the same PDE structure in different physical languages?

## Lesson Links

- [10.01 Derivation of the Wave Equation]({{ site.baseurl }}/contents/en/chapter10/10_01_Derivation_Wave_Equation/)
- [10.02 d'Alembert's Solution]({{ site.baseurl }}/contents/en/chapter10/10_02_DAlembert_Solution/)
- [10.03 Separation of Variables]({{ site.baseurl }}/contents/en/chapter10/10_03_Separation_of_Variables/)
- [10.04 Wave Equation in Higher Dimensions]({{ site.baseurl }}/contents/en/chapter10/10_04_Wave_Higher_Dimensions/)
- [10.05 Energy and Uniqueness]({{ site.baseurl }}/contents/en/chapter10/10_05_Energy_Uniqueness/)
- [10.06 Reflection and Transmission]({{ site.baseurl }}/contents/en/chapter10/10_06_Reflection_Transmission/)
- [10.07 Dispersion and Dissipation]({{ site.baseurl }}/contents/en/chapter10/10_07_Dispersion_Dissipation/)
- [10.08 Applications: Acoustics and Electromagnetics]({{ site.baseurl }}/contents/en/chapter10/10_08_Applications_Acoustics_Electromagnetics/)

## Video tham khảo

- xem trước: [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, English. The string animation this gallery is showing.
- [PDE 10 | Wave equation: d'Alembert's formula](https://www.youtube.com/watch?v=j2G91naZ8bo) — commutant, English. Traveling waves of d'Alembert's formula.
- [Phase Velocity versus Group Velocity:  Wave Dispersion](https://www.youtube.com/watch?v=EIqKG5TiSYs) — Physics Videos by Eugene Khutoryansky, English. A dispersive packet to compare with the ideal wave frames.
