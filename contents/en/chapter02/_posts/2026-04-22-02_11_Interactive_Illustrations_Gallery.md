---
layout: post
title: "02-11 Interactive Illustrations Gallery"
chapter: '02'
order: 11
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: optional
---

Watching a single slider move the damping coefficient $$\gamma$$ across the critical threshold $$2\sqrt{mk}$$ does in five seconds what three pages of algebra struggle to convey: two real roots collide on the negative real axis, bounce off into the complex plane as a conjugate pair, and suddenly the sluggish curve springs into damped ripples. This gallery turns every algebraic concept of Chapter 02 into live motion.

## Key ideas: Four Visual Phenomena to Explore in This Gallery

Use the interactive widgets below to link root locations in the complex plane directly to time-domain trajectories:

1. **Root-Locus Migration ($$\gamma$$ Sweep):** As damping increases from $$0$$ past $$2\sqrt{mk}$$, characteristic roots move along a semicircle of radius $$\omega_0$$ in the left half-plane, collide at $$-\omega_0$$ (critical damping), and split along the negative real axis (overdamping).
2. **Beats vs. Pure Resonance Envelopes:** Dragging the driving frequency $$\omega$$ toward $$\omega_0$$ stretches the beat period $$T_{\text{beat}} = \frac{2\pi}{\lvert \omega - \omega_0\rvert} \to \infty$$ until the first beat arch unfolds into the straight linear ramp of pure resonance.
3. **Frequency-Response (Bode) Peak:** Varying $$\gamma$$ shows how lightly damped oscillators exhibit a razor-sharp gain spike near $$\omega_0$$ accompanied by an abrupt $$180^\circ$$ phase flip from in-phase ($$\omega \ll \omega_0$$) to anti-phase ($$\omega \gg \omega_0$$).
4. **Wronskian Parallelogram Evolution:** Plotting $$\bigl(y_1(t), y_1'(t)\bigr)$$ and $$\bigl(y_2(t), y_2'(t)\bigr)$$ in the phase plane visualizes Abel's identity as the parallelogram area shrinking at exact rate $$e^{-p t}$$.

### Worked example: Predicting the Exact Beat Period and Envelope Before Running the Simulation

Consider the undamped driven oscillator
$$u'' + 25u = 9\cos(4t), \qquad u(0) = 0, \quad u'(0) = 0.$$

1. **Identify natural and driving frequencies:**
   $$\omega_0 = 5, \qquad \omega = 4.$$
2. **Solve the IVP via undetermined coefficients:**
   Trial $$u_p = A\cos(4t) \implies (-16 + 25)A = 9 \implies A = 1$$.
   General solution: $$u(t) = c_1\cos(5t) + c_2\sin(5t) + \cos(4t)$$.
   Applying $$u(0) = 0 \implies c_1 = -1$$ and $$u'(0) = 0 \implies c_2 = 0$:
   $$u(t) = \cos(4t) - \cos(5t).$$
3. **Apply the sum-to-product trigonometric identity $$\cos\alpha - \cos\beta = 2\sin\!\left(\frac{\beta-\alpha}{2}\right)\sin\!\left(\frac{\beta+\alpha}{2}\right)$$:**
   $$u(t) = \underbrace{2\sin\!\left(\frac{t}{2}\right)}_{\text{slow envelope}}\,\underbrace{\sin\!\left(\frac{9t}{2}\right)}_{\text{fast carrier}}.$$
4. **Read off the exact visual features to verify in the gallery:**
   - Peak amplitude of each beat: $$2$$.
   - Fast carrier period: $$\frac{2\pi}{9/2} = \frac{4\pi}{9} \approx 1.40$$.
   - Envelope node spacing (one full beat pulse): $$\sin(t/2) = 0 \implies \Delta t = 2\pi \approx 6.283$$, containing $$\frac{2\pi}{4\pi/9} = 4.5$$ fast oscillations per beat!

## Overview

This supplementary lesson collects the interactive JavaScript illustrations for Chapter 02 in one place. It is intended as a visual companion to the chapter's solution methods and applications.

## What Is Included

- characteristic roots and mode decomposition
- repeated roots, complex roots, and oscillation envelopes
- reduction of order, undetermined coefficients, and variation of parameters
- higher-order mode mixing, vibrations, RLC circuits, and Wronskians

{% include interactive-frame.html
  title="Chapter 02 Interactive Gallery"
  description="Standalone interactive gallery for all Chapter 02 topics."
  path="interactives/chapter02/index.html"
  height="920px"
%}

## Video tham khảo

- xem trước: [Mechanical Vibrations: Underdamped vs Overdamped vs Critically Damped](https://www.youtube.com/watch?v=CTd1uVq5-l8) — Dr. Trefor Bazett, English. Damping cases to compare with the vibration applets in this gallery.
- [Second-Order Ordinary Differential Equations: Solving the Harmonic Oscillator Four Ways](https://www.youtube.com/watch?v=8ePqqZXSMQs) — Steve Brunton, English. Four solution methods for one oscillator, a map of the interactive models.
- [Undamped Mechanical Vibrations & Hooke's Law // Simple Harmonic Motion](https://www.youtube.com/watch?v=Z52emur7Rko) — Dr. Trefor Bazett, English. Simple harmonic motion as the undamped reference picture.
