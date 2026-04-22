---
layout: post
title: "11-02 Separation of Variables in Rectangles"
chapter: '11'
order: 2
owner: Course Team
lang: en
categories:
- chapter11
lesson_type: required
---

## Learning Objectives

This lesson solves Laplace's equation in rectangular domains using separation of variables. Students should understand how geometry and boundary conditions combine to determine harmonic expansions.

## Prerequisites

Students should know Laplace's equation, separation of variables from earlier PDE chapters, and the role of Fourier-type expansions on intervals.

## Introduction

![Separation of variables in rectangles]({{ site.imgurl }}/chapter_img/chapter11/02_separation_variables_rectangles.svg)

One of the most classical exact methods for Laplace's equation is separation of variables in a rectangle. The method is familiar in spirit from the heat and wave equations, but the elliptic setting gives it a different interpretation. Here, the goal is not to track evolution in time, but to find a harmonic equilibrium profile that fits prescribed boundary data.

The rectangular domain is especially important because it is one of the simplest settings where geometry, boundary conditions, and harmonic expansions interact in a clean and explicit way.

## Concept in Three Ways

### Intuitive View

If the boundary values of a rectangular plate are prescribed, the temperature or potential inside the rectangle adjusts to a unique harmonic balance. Separation of variables breaks that balance into simpler mode contributions.

### Visual View

The solution is assembled from spatial modes that fit the rectangular geometry. Different modes satisfy different boundary requirements and combine to reproduce the boundary profile.

### Formal View

For Laplace's equation in a rectangle,
$$ u_{xx}+u_{yy}=0, $$
one tries
$$ u(x,y)=X(x)Y(y). $$
This reduces the PDE to two ODEs linked by a separation constant. Boundary conditions then determine which mode families are admissible.

## Why the Method Matters

This lesson is one of the clearest demonstrations that elliptic PDEs can be solved exactly in special geometries. It also shows how harmonic structure is shaped jointly by the PDE and the domain.

The rectangular case becomes a model for thinking about more general domains and more advanced elliptic methods.

## Common Misconceptions

### "Separation of variables is identical to the wave or heat case"

The algebra may resemble earlier chapters, but the interpretation is different because this is an equilibrium problem, not an evolution problem.

### "The rectangle is only a toy domain"

No. It is a foundational example that teaches the main elliptic ideas in a solvable setting.

### "Boundary data affect only the final constants"

No. They determine the mode structure and the expansion itself.

## Suggested Learning Path

### Step 1: Write the product ansatz

Students should recall the familiar separation strategy.

### Step 2: Derive the two ODEs

This reveals the spectral structure hidden inside the elliptic equation.

### Step 3: Match the boundary conditions

This is where the rectangular geometry becomes decisive.

### Step 4: Interpret the harmonic expansion

Students should connect the separated modes to the final equilibrium profile.

### Checkpoints

- Can students explain why separation of variables is natural in a rectangle?
- Do they understand how the boundary data determine the admissible modes?
- Can they distinguish the elliptic setting from time-dependent PDE separation problems?

## Worked Examples

### Example 1: Three Zero Sides, One Nonzero Side

This is the standard model problem. The nonzero side is expanded in a sine series, and the interior solution is built from corresponding harmonic modes.

### Example 2: Symmetric Boundary Data

Symmetry can simplify the expansion and help identify which modes are present.

### Example 3: Mode Decay into the Interior

Higher modes often decay more rapidly away from the boundary, helping explain interior smoothing of boundary oscillations.

## Conceptual Questions

1. Why is a rectangular domain particularly well suited to separation of variables?
2. Why do the boundary conditions influence the harmonic expansion so strongly?
3. Why do higher oscillatory boundary modes often decay rapidly into the interior?

## Application Problems

1. How does this method model steady-state temperature in a rectangular plate?
2. Why is a Fourier series along one boundary natural in this setting?
3. How does the solution explain the smoothing of complex boundary data away from the edge?

## Interactive Teaching Strategies

- Sketch the rectangle and discuss which side carries the boundary data.
- Compare this separation method to the corresponding methods in the heat and wave chapters.
- Emphasize the idea of harmonic continuation from the boundary into the interior.
- Use mode pictures to show why oscillations decay inward.

## Differentiation

### Support for Struggling Students

Students needing support should focus on the standard one-nonzero-side rectangle problem before generalizing.

### Challenge for Advanced Students

Advanced students can compare multiple rectangular boundary configurations or investigate uniqueness through maximum principles.

## Summary

Rectangular separation of variables is one of the foundational exact techniques for elliptic PDEs. It turns geometry into harmonic mode structure and shows how boundary data determine interior equilibrium behavior.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Steady temperature on a rectangular plate
- Problem: A rectangular metal plate has prescribed boundary temperatures, and we want the interior equilibrium profile.
- Model:
$$ u_{xx}+u_{yy}=0 $$
on a rectangle with Dirichlet boundary conditions.
- Assumptions and limitations: Steady state, homogeneous material, ideal rectangular geometry.
- Interpretation: Separation of variables decomposes the boundary influence into spatial modes.

#### Electric potential in a rectangular capacitor geometry
- Problem: The electric potential between conducting boundaries in a rectangular region must be determined.
- Model: The same Laplace equation with voltage boundary data.
- Assumptions and limitations: Electrostatics, no internal charge.
- Interpretation: The rectangular geometry naturally produces sine and hyperbolic sine modes.

### 2. Additional Intuition and Connections

Separation of variables here resembles the wave and heat chapters, except time has disappeared. What remains is a balance among spatial directions. A common misconception is that modal thinking only belongs to time-dependent problems; in fact it is just as natural for elliptic PDEs.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

a, b = 1.0, 1.0
x = np.linspace(0, a, 160)
y = np.linspace(0, b, 160)
X, Y = np.meshgrid(x, y)
U = np.sin(np.pi * X / a) * np.sinh(np.pi * Y / a) / np.sinh(np.pi * b / a)

plt.contourf(X, Y, U, levels=20, cmap="inferno")
plt.colorbar(label="u")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Laplace solution on a rectangle")
plt.show()
```

### 4. Suggested Searches

- search: Laplace equation rectangle separation of variables
- search: steady state heat rectangle contour plot
- search: capacitor rectangle potential field

### 5. Worked Example

On the rectangle $$ 0<x<a $$, $$ 0<y<b $$, suppose
$$
u(0,y)=u(a,y)=u(x,0)=0, \qquad u(x,b)=\sin\!\left(\frac{\pi x}{a}\right).
$$
Then
$$
u(x,y)=\sin\!\left(\frac{\pi x}{a}\right)\frac{\sinh(\pi y/a)}{\sinh(\pi b/a)}.
$$
The solution shows how a single boundary mode penetrates into the domain.

### 6. Difficulty Layering

**Undergraduate level.** Set up and solve a rectangular problem by separation of variables.

**Graduate level.** Analyze series convergence, completeness of eigenfunctions, and stability with respect to boundary data.

## References

- Haberman, Chapters 6-7.
