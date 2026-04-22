---
layout: post
title: "11-07 Applications: Electrostatics"
chapter: '11'
order: 7
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

## Learning Objectives

This lesson connects Laplace and Poisson equations to electrostatics. Students should understand the interpretation of potential, field lines, and source distributions in terms of elliptic PDEs.

## Prerequisites

Students should know Laplace's equation, Poisson's equation, and the meaning of source terms and boundary conditions in elliptic problems.

## Introduction

![Applications in electrostatics]({{ site.imgurl }}/chapter_img/chapter11/07_applications_electrostatics.svg)

Electrostatics is one of the classical homes of elliptic PDE theory. In charge-free regions, the electric potential is harmonic. In regions containing charge density, the potential satisfies Poisson's equation. This makes electrostatics one of the clearest physical realizations of the mathematical theory developed in this chapter.

The lesson is valuable because it connects abstract elliptic ideas to concrete physical meaning: potential, source, field, and boundary influence all become visible and interpretable.

## Concept in Three Ways

### Intuitive View

Electric charges create influence throughout space. The potential records that influence, while the electric field is related to the spatial change of the potential.

### Visual View

Equipotential surfaces and field lines reflect the geometry of the charge distribution. Smooth harmonic behavior appears in empty regions, while sources alter the local structure.

### Formal View

In electrostatics, charge-free regions satisfy Laplace's equation for the potential, while regions with charge density satisfy Poisson's equation. Boundary values and source terms together determine the electrostatic configuration.

## Why Electrostatics Matters

Electrostatics is one of the most important physical interpretations of elliptic PDEs. It gives concrete meaning to abstract terms like harmonicity, potential, flux, and source density.

It also makes clear why Green's functions, the method of images, and maximum principles are so useful.

## Common Misconceptions

### "Potential theory is purely mathematical language"

No. It is deeply rooted in physical models such as electrostatics.

### "Only the charges matter"

No. Boundary conditions and geometric constraints are also crucial.

### "Laplace and Poisson equations arise in electrostatics by coincidence"

No. They arise naturally from the structure of the field and source relations.

## Suggested Learning Path

### Step 1: Recall the meaning of potential

Students should connect scalar potential to electric influence.

### Step 2: Distinguish charge-free and charged regions

This separates the Laplace and Poisson cases clearly.

### Step 3: Interpret boundaries physically

Conductors, grounded surfaces, and prescribed potentials should be discussed.

### Step 4: Connect to Green's-function methods

This shows how the theory becomes computationally useful.

### Checkpoints

- Can students explain why charge-free regions lead to Laplace's equation?
- Do they understand why sources lead to Poisson's equation?
- Can they connect boundary conditions to physical conductor behavior?

## Worked Examples

### Example 1: Charge-Free Region

The electric potential in a region without charges is harmonic and thus inherits the qualitative rigidity of harmonic functions.

### Example 2: Point Charge Heuristic

A point charge motivates the singular source idea that underlies Green's-function representations.

### Example 3: Grounded Boundary

A grounded conductor imposes zero-potential boundary data, showing the physical meaning of Dirichlet conditions.

## Conceptual Questions

1. Why does electrostatics naturally lead to elliptic PDEs?
2. Why do boundaries matter so strongly in potential problems?
3. Why is the scalar potential such a powerful organizing concept?

## Application Problems

1. Why is the potential harmonic in a charge-free cavity?
2. How does a grounded surface alter the electrostatic configuration?
3. Why are Green's functions especially natural in electrostatic calculations?

## Interactive Teaching Strategies

- Use sketches of field lines and equipotentials.
- Compare charge-free and charged examples side by side.
- Connect conductor boundary conditions directly to PDE boundary data.
- Reinforce the phrase "physical meaning of harmonicity."

## Differentiation

### Support for Struggling Students

Students needing support should focus on the charge-free versus charged distinction and on the meaning of potential before formal PDE language.

### Challenge for Advanced Students

Advanced students can explore method-of-images problems or derive field behavior from potential functions.

## Summary

Electrostatics is one of the classical homes of elliptic PDE theory. It gives physical meaning to potential, flux, and boundary conditions, and shows why Laplace and Poisson equations are central in mathematical physics.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Electric field around conductors
- Problem: We want the potential and electric field around electrodes in electrostatic equilibrium.
- Model:
$$ \Delta \phi=0 $$
in charge-free regions, or $$ -\Delta \phi=\rho/\varepsilon $$ when charges are present.
- Assumptions and limitations: Electrostatic regime, homogeneous medium.
- Interpretation: Equipotential lines and field lines reflect the geometry of elliptic solutions.

#### Coaxial cable
- Problem: The potential between two concentric cylinders determines electric field strength and effective capacitance.
- Model: In cylindrical symmetry, the solution depends only on radius.
- Assumptions and limitations: Perfect cylindrical symmetry, negligible end effects.
- Interpretation: This leads to the characteristic logarithmic potential profile.

### 2. Additional Intuition and Connections

Electrostatic potential is the model example of a harmonic function that is smooth and strongly constrained by boundary data. Every qualitative fact from the maximum principle and mean value property has a direct electromagnetic meaning.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 220)
y = np.linspace(-2, 2, 220)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2) + 1e-6
Phi = np.log(R)

plt.contour(X, Y, Phi, levels=20)
plt.axis("equal")
plt.title("Equipotential contours around a radially symmetric source")
plt.show()
```

### 4. Suggested Searches

- search: electrostatic potential contour plot Laplace equation
- search: coaxial cable Laplace equation solution
- search: equipotential lines electric field visualization

### 5. Worked Example

For radii $$ a<b $$, the potential in a coaxial cable with $$ \phi(a)=V_0 $$ and $$ \phi(b)=0 $$ is
$$ \phi(r)=V_0\frac{\ln(b/r)}{\ln(b/a)}. $$
The electric field is obtained from $$ E_r=-\phi_r $$. The logarithmic form is the hallmark of cylindrical symmetry.

### 6. Difficulty Layering

**Undergraduate level.** Explain why electrostatic potential is fully determined by boundary data.

**Graduate level.** Connect to capacitance, mixed boundary conditions, and inverse conductivity problems.

## References

- Haberman, Chapters 6-7.
