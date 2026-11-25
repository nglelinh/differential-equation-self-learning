---
layout: post
title: "07-05 Green's Functions for Boundary Value Problems"
chapter: '07'
order: 5
owner: Course Team
lang: en
categories:
- chapter07
lesson_type: required
---

Press a single fingertip onto a taut string at position $$ s $$, and the string bends into a sharp triangular tent with a kink right under your finger. Now imagine replacing a distributed load $$ f(x) $$ along the entire bridge or string with a continuum of tiny fingertip pokes of strength $$ f(s)\,ds $$. By linearity, the total deflection is simply the superposition of all those individual tent shapes: $$ y(x) = \int_a^b G(x, s) f(s)\,ds $$.

That tent shape $$ G(x, s) $$ is the **Green's function**—named after the self-taught Nottingham miller George Green, who introduced it in an 1828 essay printed at his own expense. Mathematically, $$ G(x, s) $$ is the exact integral kernel of the inverse differential operator $$ L^{-1} $$, turning differential equations into explicit integration formulas.

## Key ideas: Green's Functions as Continuous Inverse Matrices

1. **Distributional Definition $$ L_x[G(x,s)] = \delta(x - s) $$ (Impulse Response):** Just as column $$ j $$ of $$ A^{-1} $$ solves $$ A \mathbf{g}_j = \mathbf{e}_j $$, the function $$ x \mapsto G(x, s) $$ solves the homogeneous equation $$ L_x[G] = 0 $$ everywhere except at $$ x = s $$, while satisfying both homogeneous boundary conditions.
2. **Continuity and Jump Condition (The Kink at $$ x = s $$):** Integrating $$ -\frac{d}{dx}(p(x) G_x) + q(x) G = \delta(x - s) $$ across an infinitesimal window $$ [s - \varepsilon, s + \varepsilon] $$ forces two stitching rules: (i) $$ G(x, s) $$ is continuous at $$ x = s $$, and (ii) its derivative jumps by $$ G_x(s^+, s) - G_x(s^-, s) = -\frac{1}{p(s)} $$ (or $$ +\frac{1}{p(s)} $$ depending on sign convention for $$ L $$).
3. **Reciprocity Symmetry $$ G(x, s) = G(s, x) $$ (Self-Adjointness):** For any self-adjoint Sturm–Liouville operator, the deflection at $$ x $$ caused by a unit load at $$ s $$ equals the deflection at $$ s $$ caused by a unit load at $$ x $$—Maxwell's reciprocity theorem in mechanics and the symmetry of $$ A^{-1} $$ in linear algebra.
4. **Bilinear Spectral Expansion (Bridge to Eigenfunctions):** Expanding $$ G(x, s) $$ in orthonormal eigenfunctions yields $$ G(x, s) = \sum_{n=1}^{\infty} \frac{\phi_n(x)\phi_n(s)}{\lambda_n} $$, unifying Lesson 07-04 and Lesson 07-05 into two views of the exact same inverse operator!

### Worked example: Constructing $$ G(x, s) $$ for $$ -y'' = f(x) $$ on $$ [0, L] $$ and Verifying on $$ f(x) = 1 $$

**Problem:** Construct the Green's function for $$ -y'' = f(x) $$ on $$ [0, L] $$ with $$ y(0) = y(L) = 0 $$, then use $$ y(x) = \int_0^L G(x, s) f(s)\,ds $$ to solve $$ -y'' = 1 $$ and verify directly.

1. **Solve $$ -G_{xx} = 0 $$ on each side of $$ x = s $$:**
   - For $$ 0 \le x < s $$, $$ G(0, s) = 0 \implies G(x, s) = A(s)\,x $$.
   - For $$ s < x \le L $$, $$ G(L, s) = 0 \implies G(x, s) = B(s)\,(L - x) $$.
2. **Enforce continuity and the unit derivative jump at $$ x = s $$:**
   Since $$ p(x) = 1 $$ in $$ -(p G_x)' = \delta(x - s) $$, integrating across $$ s $$ gives $$ -G_x(s^+, s) + G_x(s^-, s) = 1 \implies G_x(s^+, s) - G_x(s^-, s) = -1 $$.
   - Continuity: $$ A s = B (L - s) $$.
   - Jump: $$ -B - A = -1 \implies A + B = 1 $$.
3. **Solve the $$ 2 \times 2 $$ system for $$ A(s) $$ and $$ B(s) $$:**
   From $$ B = 1 - A $$, substitute into $$ A s = (1 - A)(L - s) = L - s - A L + A s \implies A L = L - s $$, so
   $$ A(s) = \frac{L - s}{L}, \qquad B(s) = \frac{s}{L}. $$
   Therefore, the symmetric tent-shaped Green's function is
   $$ G(x, s) = \begin{cases} \dfrac{x(L - s)}{L}, & 0 \le x \le s, \\[6pt] \dfrac{s(L - x)}{L}, & s \le x \le L. \end{cases} $$
   Notice $$ G(x, s) = G(s, x) $$ visibly!
4. **Apply to $$ f(x) = 1 $$ and verify:**
   Split the integral at $$ s = x $$:
   $$ y(x) = \int_0^x \frac{s(L - x)}{L}\,ds + \int_x^L \frac{x(L - s)}{L}\,ds = \frac{L - x}{L} \cdot \frac{x^2}{2} + \frac{x}{L} \cdot \frac{(L - x)^2}{2} = \frac{x(L - x)}{2L}\bigl[x + (L - x)\bigr] = \frac{x(L - x)}{2}. $$
   Check: $$ y(0) = 0 $$, $$ y(L) = 0 $$, and $$ -y''(x) = -\frac{d^2}{dx^2}\left(\frac{Lx - x^2}{2}\right) = 1 $$. Exact!

## Learning Objectives

This lesson introduces Green's functions as a powerful method for solving linear nonhomogeneous BVPs. Students should learn to interpret a Green's function as the system's response to a point source, construct it in simple one-dimensional problems, and use the resulting integral formula for solutions.

## Prerequisites

Students should know linear BVPs, superposition, and the qualitative idea of a Dirac delta source. Familiarity with eigenfunction expansions is also helpful.

## Introduction

![Green's function as the impulse response of a boundary value problem]({{ site.imgurl }}/chapter_img/chapter07/05_greens_functions_bvp.svg)

If we know how a system responds to a point impulse, then by superposition we can reconstruct its response to a general distributed source. That is the core idea of Green's functions. Instead of solving a new boundary value problem from scratch for every forcing term, we solve one structured problem and then integrate.

Conceptually, Green's functions sit at a beautiful intersection of analysis, physics, and operator theory. They are both impulse responses and integral kernels of inverse operators.

## Concept in Three Ways

### Intuitive View

Imagine pushing or heating the system at just one point. The Green's function records how that single-point action influences the rest of the domain. A general source is then built by adding up many such point effects.

### Visual View

For fixed $$ \xi $$, the function $$ G(x,\xi) $$ usually has one form to the left of the source point and another to the right. The function is often continuous at
$$ x=\xi, $$
but its derivative jumps. That jump is the signature of the point source.

### Formal View

For a linear operator $$ L $$ with homogeneous boundary conditions, the Green's function satisfies
$$ L G(x,\xi)=\delta(x-\xi) $$
together with the boundary conditions in the variable $$ x $$. The solution of
$$ Ly=f $$
is then
$$ y(x)=\int_a^b G(x,\xi)f(\xi)\,d\xi. $$

## Common Misconceptions

- "Green's functions are just a formula trick." Wrong. They represent the inverse operator as an integral kernel.
- "A point source is too artificial to matter." Wrong. It is the simplest building block for superposition.
- "The Green's function must be smooth everywhere." Wrong. The derivative jump is essential.
- "Green's functions only help computationally." Wrong. They also reveal how influence propagates through the system.

## Suggested Learning Path

### Step 1: Recall Superposition

The Green's approach depends completely on linearity.

### Step 2: Accept the Point-Source Model

Students should become comfortable with the idea of a concentrated source.

### Step 3: Construct the Two Branches

This is the main one-dimensional technique.

### Step 4: Read the Integral Formula

Students should understand the integral as a continuous superposition of point responses.

### Checkpoints

- Can students explain Green's functions in words without relying on formulas?
- Do they remember continuity and derivative jump conditions?
- Can they connect Green's functions to inverse operators?

## Worked Examples

### Example 1: The Simplest Green's Function

Consider
$$
-y''=f(x),\qquad 0<x<1,\qquad y(0)=0,\qquad y(1)=0.
$$
We seek
$$ -G_{xx}(x,\xi)=\delta(x-\xi) $$
with
$$ G(0,\xi)=0,\qquad G(1,\xi)=0. $$
The answer is
$$
G(x,\xi)=
\begin{cases}
x(1-\xi), & x\le \xi,\\
\xi(1-x), & x\ge \xi.
\end{cases}
$$

### Example 2: Solving with Green's Function

Using the formula
$$ y(x)=\int_0^1 G(x,\xi)f(\xi)\,d\xi, $$
if $$ f(\xi)=1 $$, then
$$ y(x)=\frac{x(1-x)}{2}. $$

### Example 3: The Derivative Jump

The Green's function above is continuous at $$ x=\xi $$, but the left and right derivatives differ by a fixed amount. That jump encodes the point source.

## Conceptual Questions

1. Why is linearity essential in the Green's function method?
2. Why is the derivative jump not a flaw but a feature?
3. What does the Green's function say physically about influence in the system?

## Application Problems

1. In mechanics, why is a point load a useful conceptual building block?
2. In electrostatics, how does a Green's function encode influence from source points to observation points?
3. In PDEs, why do Green's functions become even more powerful than in one-dimensional ODEs?

## Interactive Teaching Strategies

- Ask students to sketch the shape of $$ G(x,\xi) $$ for fixed $$ \xi $$ before deriving it.
- Emphasize the derivative jump visually and physically.
- Compare the Green's solution formula with the direct solution of one simple problem.
- Keep returning to the language of impulse response and superposition.

## Differentiation

### Support for Struggling Students

Students who need support should begin with the simplest Dirichlet problem on $$ [0,1] $$ and practice the two-branch construction carefully.

### Challenge for Advanced Students

Advanced students can investigate symmetry of Green's functions for self-adjoint problems and their relation to eigenfunction expansions.

## Summary

Green's functions transform a linear boundary value problem into an integral representation built from point-source responses. They are among the most powerful conceptual and computational tools in the subject.

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Deflection under distributed load
- Problem: We want the deformation produced by a nonuniform load without solving a new ODE from scratch for each source.
- Model:
$$ Ly=f,\qquad y(x)=\int_a^b G(x,\xi)f(\xi)\,d\xi. $$
- Assumptions and limitations: The system is linear, the boundary conditions are fixed, and the Green's function exists.
- Interpretation: The Green's function is the response to a point source, and the integral superposes point responses.

#### Potential generated by a distributed charge
- Problem: Compute the field due to a distributed source on an interval with grounded endpoints.
- Model:
$$ -u''=\rho(x),\qquad u(0)=u(L)=0. $$
- Assumptions and limitations: The one-dimensional setting is simplified but reveals the main mechanism clearly.
- Interpretation: Green's function records how a source at one point influences every observation point.

### 2. Additional Intuition and Connections

Green's functions turn the inverse of a differential operator into an integral kernel. This is a powerful bridge between ODEs, PDEs, and operator theory. A common pitfall is to view the construction as a purely computational trick. In fact, continuity and the jump in the derivative are the mathematical signature of the point source.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
xi = 0.35
G = np.where(x <= xi, x * (1 - xi), xi * (1 - x))

plt.plot(x, G, label=f"G(x,{xi})")
plt.axvline(xi, color="gray", ls="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("G")
plt.title("Green's function for -y'' with Dirichlet boundaries")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Green function boundary value problem visualization
- search: delta source response one dimensional Poisson
- search: impulse response differential operator

### 5. Worked Example

For
$$ -y''=f(x),\qquad y(0)=y(1)=0, $$
the Green's function is
$$
G(x,\xi)=
\begin{cases}
x(1-\xi), & x\le \xi,\\
\xi(1-x), & x\ge \xi.
\end{cases}
$$
Hence
$$ y(x)=\int_0^1 G(x,\xi)f(\xi)\,d\xi. $$
If $$ f(\xi)=1 $$, then
$$ y(x)=\frac{x(1-x)}{2}. $$

### 6. Difficulty Layering

**Undergraduate level.** Construct simple one-dimensional Green's functions and use them to write solutions.

**Graduate level.** Emphasize Green's functions as inverse kernels, symmetry, and connections to the resolvent of an operator.

![Green's functions for BVPs]({{ site.imgurl }}/chapter_img/chapter07/05_greens_functions_bvp.svg)

## Video tham khảo

- xem trước: [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, English. Mathemaniac's visual account of a Green's function as the response to a point source.
- [Introducing Green's Functions for Partial Differential Equations (PDEs)](https://www.youtube.com/watch?v=xNqLZnM-PPY) — Faculty of Khan, English. Faculty of Khan introduces Green's functions for PDEs and boundary-value problems.
- [Green's function for Sturm-Liouville problems](https://www.youtube.com/watch?v=8l4VsNSX_kw) — Nathan Kutz, English. Nathan Kutz constructs the Green's function of a Sturm-Liouville problem.

## References

- Boyce & DiPrima, Chapter 11: introductory Green's function construction.
- Haberman, Chapter 5: strong interpretation and applications.
