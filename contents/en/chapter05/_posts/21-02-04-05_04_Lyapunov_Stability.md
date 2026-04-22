---
layout: post
title: "05-04 Lyapunov Stability"
chapter: '05'
order: 4
owner: Course Team
lang: en
categories:
- chapter05
lesson_type: required
---

## Learning Objectives

This lesson helps students understand Lyapunov's method as a way to prove stability without solving the system explicitly, identify useful Lyapunov candidates, and connect stability analysis with energy-style reasoning.

## Prerequisites

Students should know equilibria, local stability, and basic multivariable differentiation. Physical intuition about energy in mechanics is especially helpful.

## Introduction

![Lyapunov function as a decaying energy surface]({{ site.imgurl }}/chapter_img/chapter05/04_lyapunov_stability.svg)

Many important nonlinear systems cannot be solved in closed form. If stability analysis required an explicit solution every time, much of nonlinear dynamics would be inaccessible. Lyapunov's method provides a different strategy: instead of solving for trajectories, we search for a scalar quantity that decreases along them.

This is one of the most beautiful ideas in the subject. A suitable Lyapunov function acts like an energy or a measure of distance from equilibrium. If the system cannot increase that quantity, it cannot wander arbitrarily away from equilibrium. If the quantity strictly decreases, the motion is often driven toward equilibrium.

## Concept in Three Ways

### Intuitive View

Think of a Lyapunov function as a landscape height. If trajectories always move downhill or remain level, they cannot spontaneously climb to higher terrain. If they always descend, they are being guided toward a low point.

### Visual View

Level curves of a Lyapunov function form nested barriers around an equilibrium. If the vector field points inward across those curves, the geometry of stability becomes visible even without an explicit formula for the trajectory.

### Formal View

For a system
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
a function $$ V(x,y) $$ is used as a Lyapunov candidate near the origin when
$$
V(0,0)=0,\qquad V(x,y)>0 \text{ for } (x,y)\neq (0,0)
$$
in a neighborhood of the origin. Along trajectories,
$$ \dot{V}=V_x f+V_y g. $$
If
$$ \dot{V}\le 0, $$
we obtain strong information about stability. If
$$ \dot{V}<0 $$
away from the equilibrium, asymptotic stability often follows.

## Common Misconceptions

- "To prove stability we must solve the system first." Wrong. This is exactly what Lyapunov's method avoids.
- "Any positive function is a good Lyapunov function." Wrong. Its derivative along trajectories matters critically.
- "If $$ \dot{V}=0 $$ then the method fails completely." Not always, but stronger conclusions may require additional tools.
- "Lyapunov theory belongs only to mechanics." Wrong. It is central in control, circuits, biology, and many other fields.

## Suggested Learning Path

### Step 1: Choose a Candidate

Students should first try energy-like expressions such as quadratic forms.

### Step 2: Check Positive Definiteness

The function must genuinely measure deviation from equilibrium.

### Step 3: Compute $$ \dot{V} $$

This is the decisive step in the method.

### Step 4: State the Correct Conclusion

It is essential to distinguish between stability and asymptotic stability.

### Checkpoints

- Can students tell the difference between $$ V>0 $$ and $$ \dot{V}<0 $$?
- Can students compute derivatives along trajectories correctly?
- Do students avoid making stronger conclusions than the hypotheses justify?

## Worked Examples

### Example 1: Asymptotic Stability

Consider
$$ x'=-x-y,\qquad
y'=x-y. $$
Choose
$$ V=x^2+y^2. $$
Then
$$ \dot{V}=2x(-x-y)+2y(x-y)=-2x^2-2y^2<0 $$
away from the origin. Therefore the origin is asymptotically stable.

### Example 2: Stability Without Asymptotic Decay

For
$$ x'=y,\qquad
y'=-x, $$
choose
$$ V=x^2+y^2. $$
Then
$$ \dot{V}=2xy+2y(-x)=0. $$
The energy is conserved. The origin is stable in the Lyapunov sense, but not asymptotically stable.

### Example 3: A Poor Candidate

If we choose
$$ V=x^2-y^2, $$
then even if its derivative looks simple, the function is not positive definite and cannot reliably measure distance from equilibrium. This reminds students that choosing $$ V $$ is partly an art.

## Conceptual Questions

1. Why does Lyapunov's method avoid the need for explicit solutions?
2. What is the difference between positive definiteness of $$ V $$ and negativity of $$ \dot{V} $$?
3. Why does $$ \dot{V}=0 $$ often give a weaker conclusion than $$ \dot{V}<0 $$?

## Application Problems

1. In robotics, why is an "error energy" a natural Lyapunov candidate?
2. In an electrical circuit with resistance, why does total stored energy often decrease?
3. In population dynamics, what might play the role of a Lyapunov-like measure of deviation from equilibrium?

## Interactive Teaching Strategies

- Let students test several candidate functions on the same system and compare outcomes.
- Pair an example with $$ \dot{V}<0 $$ and one with $$ \dot{V}=0 $$ to highlight the distinction.
- Ask students to interpret level curves of $$ V $$ geometrically before doing any algebra.
- Use the language of energy, storage, and dissipation whenever possible.

## Differentiation

### Support for Struggling Students

Students who need support should begin with the standard candidate
$$ V=x^2+y^2 $$
in several examples before attempting more subtle constructions.

### Challenge for Advanced Students

Advanced students can explore examples where $$ \dot{V}\le 0 $$ is not enough for asymptotic stability and see why extra theory is needed.

## Summary

Lyapunov's method turns stability into a problem of constructing a decreasing scalar quantity. It is powerful precisely because it works even when trajectories cannot be solved explicitly.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Mechanics with damping
- Problem: Even without an explicit solution, we want to prove that a damped pendulum loses energy and settles.
- Model:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega,
$$
with Lyapunov candidate
$$
V(\theta,\omega)=1-\cos\theta+\frac{1}{2}\omega^2.
$$
- Assumptions and limitations: The argument proves monotone energy loss, but does not automatically provide an exact convergence rate.
- Interpretation: If $$ \dot{V}\le 0 $$, the system cannot climb to higher energy levels on its own.

#### Robot control
- Problem: We want position and velocity tracking errors to decay to zero under a feedback law.
- Model:
$$ \dot{e}_1=e_2,\qquad
\dot{e}_2=-k_1 e_1-k_2 e_2, $$
with
$$ V=\frac{1}{2}(k_1 e_1^2+e_2^2). $$
- Assumptions and limitations: Saturation, delay, and measurement noise are neglected.
- Interpretation: A Lyapunov function acts as a certificate of stability, not just a heuristic.

### 2. Additional Intuition and Connections

Lyapunov's method replaces the question "Can we solve the trajectory?" with "Can we find a quantity that decreases?" The conditions $$ V>0 $$ and $$ \dot{V}\le 0 $$ play different roles: one measures distance from equilibrium, the other controls evolution along motion. A common pitfall is to claim asymptotic stability from $$ \dot{V}\le 0 $$ alone. This topic connects nonlinear stability with the energy viewpoint of mechanics and control.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, z):
    x, y = z
    return [-x - y, x - y]

t = np.linspace(0, 8, 400)
for z0 in [(2, 0), (0, 2), (-2, 1)]:
    sol = solve_ivp(system, [0, 8], z0, t_eval=t)
    V = sol.y[0]**2 + sol.y[1]**2
    plt.plot(t, V, label=f"IC={z0}")

plt.xlabel("t")
plt.ylabel("V(t)")
plt.title("A Lyapunov function decreasing in time")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Lyapunov function energy dissipation pendulum
- search: contour plot Lyapunov function trajectories
- search: asymptotic stability energy method

### 5. Worked Example

Consider
$$ x'=-x-y,\qquad
y'=x-y. $$
Choose
$$ V=x^2+y^2. $$
Then
$$ \dot{V}=2x(-x-y)+2y(x-y)=-2x^2-2y^2<0 $$
away from the origin. Therefore the origin is asymptotically stable. This is a model example of proving stability without solving the system explicitly.

### 6. Difficulty Layering

**Undergraduate level.** Practice testing simple Lyapunov candidates such as $$ x^2+y^2 $$.

**Graduate level.** Introduce Lyapunov's direct method in theorem form, LaSalle's invariance principle, and global stability questions.

![Lyapunov stability]({{ site.imgurl }}/chapter_img/chapter05/05_04_lyapunov_stability.svg)

## References

- Strogatz, Chapter 7: intuitive introduction to Lyapunov ideas.
- Arnold, Chapter 5: strong geometric and energetic viewpoint on nonlinear stability.
