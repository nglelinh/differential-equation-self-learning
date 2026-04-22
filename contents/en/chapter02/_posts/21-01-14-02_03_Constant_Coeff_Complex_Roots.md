---
layout: post
title: "02-03 Constant Coefficients: Complex Roots"
chapter: '02'
order: 3
owner: Course Team
lang: en
categories:
- chapter02
lesson_type: required
---
## Learning Objectives
This lesson helps students understand the origin of complex roots in the characteristic equation, convert them to real solutions using Euler's formula, and interpret the meaning of the real and imaginary parts in oscillatory dynamics. This is the central lesson for students to read harmonic oscillation, damped oscillation, and resonance in subsequent application lessons.

## Background Knowledge
Students should grasp the characteristic equation for constant coefficients, basic complex numbers, and Euler's formula
$$ e^{i\theta}=\cos \theta+i\sin \theta. $$
If students are weak in complex numbers, instructors should briefly review before proceeding to solution techniques.

## Introduction
![Diagram for Lesson 02-03 Constant Coefficients: Complex Roots]({{ site.imgurl }}/chapter_img/chapter02/02_03_constant_coeff_complex_roots.svg)

When the characteristic equation has no real roots, many students worry that the model loses physical meaning. In fact the opposite is true: complex roots are often the signature of oscillation. Ideal spring systems, LC circuits, and many wave phenomena all lead to complex roots. The imaginary part is not an "imaginary" object, but rather an algebraic encoding of oscillation frequency.

The beauty of this lesson is that complex numbers appear as intermediate tools, but the final result is still a real solution. Thanks to Euler's formula, a pair of conjugate roots generates a pair of sine and cosine functions, while the real part of the characteristic root controls whether amplitude grows or decays with time.

## Three Ways to Understand the Concept
### Intuitive View
A complex conjugate pair is like a rotating rhythm in the plane. When we view this rotational motion projected onto one axis, we see sine and cosine. If the rotation simultaneously contracts, we get damped oscillation. If it expands, we get growing oscillation.

### Visual View
With characteristic roots
$$ r=\alpha\pm i\beta, $$
the solution graph has the form
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
If $$ \alpha=0 $$, the amplitude remains constant. If $$ \alpha<0 $$, the amplitude decays. If $$ \alpha>0 $$, the amplitude grows. Meanwhile $$ \beta $$ determines the oscillation rate, i.e., the angular frequency.

### Formal View
For the equation
$$ ay''+by'+cy=0, $$
if the characteristic equation
$$ ar^2+br+c=0 $$
has roots
$$ r=\alpha\pm i\beta,\qquad \beta\neq 0, $$
then the general real solution is
$$
y(t)=e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
This comes from
$$
e^{(\alpha+i\beta)t}=e^{\alpha t}\left(\cos \beta t+i\sin \beta t\right).
$$

## Common Misconceptions
- "Complex roots mean the physical solution is not real." Wrong. The final result is still a real solution.
- "The imaginary part of the characteristic root makes the solution more complicated but has no meaning." Wrong. It is precisely the oscillation frequency.
- "If there are sine-cosine terms then the system is definitely stable." Wrong. It still depends on the real part $$ \alpha $$.
- "All oscillations have constant amplitude." Wrong. Damped and growing oscillations arise naturally when $$ \alpha\neq 0 $$.

## Suggested Learning Progression
### Step 1: Solve the characteristic equation
Check for negative discriminant to recognize complex roots.

### Step 2: Write the solution in complex exponential form
This is an intermediate step, not the final destination.

### Step 3: Use Euler's formula to convert to real solution
This is the important bridge between algebra and geometry.

### Step 4: Interpret the real and imaginary parts
The real part controls amplitude, the imaginary part controls frequency.

### Checkpoints
- Can the student correctly convert from $$ e^{(\alpha+i\beta)t} $$ to sine-cosine form?
- Can the student explain the roles of $$ \alpha $$ and $$ \beta $$?
- Can the student recognize the difference between harmonic oscillation and damped oscillation?

## Worked Examples
### Example 1: Pure Harmonic Oscillation
Solve
$$ y''+4y=0. $$
The characteristic equation:
$$ r^2+4=0, $$
so
$$ r=\pm 2i. $$
Therefore
$$ y(t)=c_1\cos 2t+c_2\sin 2t. $$
This is harmonic oscillation with angular frequency 2 and constant amplitude.

### Example 2: Damped Oscillation
Solve
$$ y''+2y'+5y=0. $$
The characteristic equation:
$$ r^2+2r+5=0. $$
We have
$$ r=-1\pm 2i. $$
Thus the general solution is
$$ y(t)=e^{-t}\left(c_1\cos 2t+c_2\sin 2t\right). $$
The exponential factor $$ e^{-t} $$ causes amplitude to decay over time, while $$ 2 $$ is the oscillation frequency.

### Example 3: Applying Initial Conditions
With the equation
$$ y''+2y'+5y=0, $$
suppose
$$ y(0)=1,\qquad y'(0)=0. $$
From $$ y(0)=1 $$ we deduce
$$ c_1=1. $$
We compute
$$
y'(t)=e^{-t}\left[-c_1\cos 2t-c_2\sin 2t-2c_1\sin 2t+2c_2\cos 2t\right].
$$
Substituting $$ t=0 $$:
$$ y'(0)=-c_1+2c_2=0. $$
Since $$ c_1=1 $$,
$$ 2c_2=1 \Rightarrow c_2=\frac{1}{2}. $$
Thus
$$
y(t)=e^{-t}\left(\cos 2t+\frac{1}{2}\sin 2t\right).
$$

### Example 4: Growing Oscillation
Solve
$$ y''-2y'+5y=0. $$
The characteristic equation:
$$ r^2-2r+5=0, $$
so
$$ r=1\pm 2i. $$
Therefore
$$ y(t)=e^t\left(c_1\cos 2t+c_2\sin 2t\right). $$
Here the system still oscillates but amplitude grows according to $$ e^t $$. This helps students understand very clearly the meaning of a positive real part.

## Conceptual Questions
1. Why do complex roots of the characteristic equation lead to sine and cosine in the real solution?
2. What two pieces of physical information do the real and imaginary parts of the characteristic root encode?
3. Why do two systems both oscillate but one damps while the other grows in amplitude?

## Application Problems
1. A spring system with small damping oscillates around equilibrium. Explain why the expected solution should be damped oscillation rather than pure sine-cosine.
2. An electrical circuit has oscillating voltage but energy is gradually dissipated. Which part of the characteristic root reflects this?
3. A control system has an oscillating signal that grows larger. Explain why this suggests a positive real part in the characteristic root.

## Interactive Teaching Strategies
- Show students three graphs: constant amplitude, damped, growing amplitude, then ask them to guess the sign of $$ \alpha $$.
- Organize a "language translation" activity: from characteristic root $$ -1\pm 3i $$ to verbal description "damped oscillation with frequency 3."
- Have students prove the real solution formula from Euler in small groups.
- Encourage students to express solutions in amplitude-phase form if ready, to enhance intuition.

## Differentiation
### Support for Struggling Students
Give weaker students a fixed two-step table: solve characteristic equation, then apply template
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Separating the roles of $$ \alpha $$ and $$ \beta $$ with color or diagrams is often very effective.

### Challenge for Advanced Students
Advanced students can be asked to write the solution in the form
$$ Re^{\alpha t}\cos \left(\beta t-\phi\right) $$
and explain the meaning of initial amplitude, initial phase, and decay rate.

## Memorable Summary
Complex roots do not make the problem less realistic; they are mathematics' way of encoding oscillation. If
$$ r=\alpha\pm i\beta, $$
then the solution is
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Remember: $$ \alpha $$ controls amplitude, $$ \beta $$ controls frequency.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Ideal spring oscillation
- Problem: A spring-mounted mass oscillates forever in the absence of damping.
- Model:
$$ x''+\omega^2 x=0. $$
- Assumptions and limitations: No damping, linear spring, small motion.
- Interpretation: The roots $$ \pm i\omega $$ encode oscillation frequency, not unphysical behavior.

#### Damped sensor vibration
- Problem: A sensor vibrates after a disturbance and then settles.
- Model:
$$ x''+2\zeta\omega_n x'+\omega_n^2 x=0. $$
- Assumptions and limitations: Linear damping and one dominant mode.
- Interpretation: The negative real part sets the decay envelope while the imaginary part sets the oscillation rate.

#### LC or underdamped RLC circuit
- Problem: Energy oscillates between electric and magnetic storage while resistance slowly dissipates it.
- Model:
$$ Lq''+Rq'+\frac{1}{C}q=0. $$
- Assumptions and limitations: Ideal linear components.
- Interpretation: A sine-cosine term times a decaying exponential captures both oscillation and energy loss.

### 2. Conceptual Insight

Complex roots appear because rotational motion in a plane is the natural hidden geometry behind oscillation. Once projected back to the real axis, that rotation becomes sine and cosine. Students often memorize
$$ e^{\alpha t}(c_1\cos \beta t+c_2\sin \beta t) $$
without attaching meaning to the parameters. The main meaning is simple: $$ \alpha $$ controls the envelope, $$ \beta $$ controls the oscillation rate.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
signals = [
    (np.cos(3*t), "alpha=0, beta=3"),
    (np.exp(-0.4*t)*np.cos(3*t), "alpha=-0.4, beta=3"),
    (np.exp(0.2*t)*np.cos(3*t), "alpha=0.2, beta=3"),
]

for y, label in signals:
    plt.plot(t, y, label=label)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("How the real part alpha changes oscillation behavior")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

The three curves separate pure, damped, and growing oscillation in one view.

### 4. External Search Prompts

- search: damped oscillation envelope interactive
- search: complex roots oscillation visualization
- search: Euler formula sine cosine dynamics

### 5. Worked Example

For
$$ x''+2x'+10x=0,\qquad x(0)=1,\qquad x'(0)=0, $$
the characteristic roots are
$$ r=-1\pm 3i. $$
Hence
$$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right). $$
Applying the data gives
$$
x(t)=e^{-t}\left(\cos 3t+\frac{1}{3}\sin 3t\right).
$$
The model says: oscillation persists, but the amplitude decays like $$ e^{-t} $$.

### 6. Difficulty Layering

**Undergraduate level.** Convert complex roots to real solutions and read amplitude and frequency from $$ \alpha,\beta $$.

**Graduate level.** Use amplitude-phase form and connect to complex eigenvalues of linear systems.

![Complex roots - oscillations]({{ site.imgurl }}/chapter_img/chapter02/02_03_constant_coeff_complex_roots.svg)

![Complex plane visualization]({{ site.imgurl }}/chapter_img/chapter02/02_03_complex_plane.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: excellent presentation of the dynamic meaning of complex roots.
- Zill — *Differential Equations with Boundary-Value Problems*: many exercises converting between complex and real solutions.
- Ross — *Differential Equations*: concise and clear in reading $$ \alpha $$, $$ \beta $$ from characteristic roots.
