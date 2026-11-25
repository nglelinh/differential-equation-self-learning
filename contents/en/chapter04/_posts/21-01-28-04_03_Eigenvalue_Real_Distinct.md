---
layout: post
title: "04-03 Eigenvalue Method: Real Distinct"
chapter: '04'
order: 3
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

Plug the trial vector $$\mathbf{x}(t) = \mathbf{v}\,e^{\lambda t}$$ into the constant-coefficient system $$\mathbf{x}' = A\mathbf{x}$$: differentiation brings down $$\lambda$$, and canceling $$e^{\lambda t} > 0$$ turns a coupled calculus problem into the pure eigenvalue equation $$A\mathbf{v} = \lambda\mathbf{v}$$. Geometrically, each real eigenvector defines an invisible highway through the origin along which trajectories travel in a pure straight line without ever bending!

## Key ideas: Straight-Line Solutions and Spectral Decoupling

Four principles explain why distinct real eigenvalues yield the cleanest possible dynamics:

1. **Automatic Linear Independence:** Eigenvectors corresponding to distinct eigenvalues $$\lambda_1, \dots, \lambda_n$$ are guaranteed linearly independent, so $$\{\mathbf{v}_1 e^{\lambda_1 t}, \dots, \mathbf{v}_n e^{\lambda_n t}\}$$ immediately forms a complete fundamental set for $$\mathbf{x}' = A\mathbf{x}$$.
2. **Coordinate Decoupling via $$P^{-1}AP = D$$:** Setting $$\mathbf{x} = P\mathbf{y}$$ (where columns of $$P$$ are eigenvectors) converts $$\mathbf{x}' = A\mathbf{x}$$ into $$n$$ completely uncoupled scalar equations $$y_k' = \lambda_k y_k$$.
3. **Asymptotic Tangency (Fast vs. Slow Eigendirections):** For a stable node with $$\lambda_2 < \lambda_1 < 0$$, the fast mode $$e^{\lambda_2 t}$$ dies out far quicker than $$e^{\lambda_1 t}$$, so almost every trajectory bends to enter the origin **tangent to the slow eigenvector** $$\mathbf{v}_1$$!
4. **Saddle Geometry ($$\lambda_1 > 0 > \lambda_2$$):** Trajectories on the stable line $$\operatorname{span}(\mathbf{v}_2)$$ head directly into the origin, trajectories on the unstable line $$\operatorname{span}(\mathbf{v}_1)$$ flee away, and all other trajectories sweep in along $$\mathbf{v}_2$$ and curve out parallel to $$\mathbf{v}_1$$.

### Worked example: Solving a 2D Real-Distinct System and Predicting Asymptotic Direction

Solve the initial value problem
$$\mathbf{x}' = \begin{pmatrix} -4 & 2 \\ 1 & -3 \end{pmatrix}\mathbf{x}, \qquad \mathbf{x}(0) = \begin{pmatrix} 3 \\ 0 \end{pmatrix},$$
and determine the exact line along which $$\mathbf{x}(t)$$ approaches the origin as $$t \to +\infty$$.

1. **Find the eigenvalues of $$A$$:**
   $$\operatorname{tr}(A) = -7, \qquad \det(A) = (-4)(-3) - 2 = 10.$$
   Characteristic equation: $$\lambda^2 + 7\lambda + 10 = (\lambda + 2)(\lambda + 5) = 0 \implies \lambda_1 = -2,\; \lambda_2 = -5$$.
   Since both eigenvalues are real and negative, the origin is an **asymptotically stable node**.
2. **Compute an eigenvector for each eigenvalue:**
   - For $$\lambda_1 = -2$$ (slow mode): $$(A + 2I)\mathbf{v}_1 = \begin{pmatrix} -2 & 2 \\ 1 & -1 \end{pmatrix}\mathbf{v}_1 = \mathbf{0} \implies \mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$.
   - For $$\lambda_2 = -5$$ (fast mode): $$(A + 5I)\mathbf{v}_2 = \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix}\mathbf{v}_2 = \mathbf{0} \implies \mathbf{v}_2 = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$$.
3. **Form the general solution and match $$\mathbf{x}(0) = (3, 0)^\top$$:**
   $$\mathbf{x}(t) = c_1 e^{-2t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 e^{-5t}\begin{pmatrix} 2 \\ -1 \end{pmatrix}.$$
   At $$t = 0$$: $$c_1 + 2c_2 = 3$$ and $$c_1 - c_2 = 0 \implies c_1 = c_2 = 1$$.
   Thus
   $$\mathbf{x}(t) = e^{-2t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + e^{-5t}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} e^{-2t} + 2e^{-5t} \\ e^{-2t} - e^{-5t} \end{pmatrix}.$$
4. **Determine the exact asymptotic approach direction as $$t \to \infty$$:**
   Factor out the dominant slow exponential $$e^{-2t}$$:
   $$\mathbf{x}(t) = e^{-2t}\left[\begin{pmatrix} 1 \\ 1 \end{pmatrix} + e^{-3t}\begin{pmatrix} 2 \\ -1 \end{pmatrix}\right] \sim e^{-2t}\begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
   Because $$e^{-3t} \to 0$$, the trajectory curves smoothly to enter $$(0,0)$$ tangent to the slow line $$x_2 = x_1$$!

## Learning Objectives

This lesson helps students use eigenvalues and eigenvectors to solve linear systems when the matrix has real distinct eigenvalues, understand the meaning of each eigenvector mode as an invariant dynamical direction, and read the growing, decaying, or saddle behavior of the system from the signs of the eigenvalues.

## Prerequisites

Students need to grasp the characteristic equation of constant-coefficient ODEs, eigenvectors and matrices. This is the lesson where linear algebra steps into the center of solving ODEs, so intuition about vector spaces is very important.

## Introduction

![Solutions along two real distinct eigenvalues]({{ site.imgurl }}/chapter_img/chapter04/03_eigenvalue_real_distinct.svg)

If a linear system is written as
$$ \mathbf{x}'=A\mathbf{x}, $$
then the natural question is: are there directions such that if the system starts moving exactly along them, it will not be deflected to other directions? The answer is precisely the eigenvectors. Along these special directions, dynamics become as simple as possible: the system is only contracted or stretched by an exponential function.

This is the most beautiful case of the chapter. When the matrix has enough real distinct eigenvalues, the entire system separates into clearly independent modes. Each mode has its own rate, and the total solution is the superposition of those modes. From here, students can directly see why eigenvalues are not just algebraic tools, but the language for reading dynamics.

## Concept in Three Ways

### Intuitive View

An eigenvector is a direction that the system does not change direction, only changes magnitude over time. If you move along that direction, the trajectory does not bend but only extends outward or contracts inward.

### Visual View

In the phase plane, two eigenvectors create two invariant lines. Other trajectories typically curve to closely follow one of these two directions when time is large. If one eigenvalue is positive and one is negative, we see a saddle shape: one direction attracts, one direction repels.

### Formal View

We try the form
$$ \mathbf{x}(t)=\mathbf{v}e^{\lambda t}. $$
Substituting into the system:
$$
\lambda \mathbf{v}e^{\lambda t}=A\mathbf{v}e^{\lambda t}.
$$
This implies
$$ A\mathbf{v}=\lambda \mathbf{v}. $$
Thus $$ \lambda $$ is an eigenvalue and $$ \mathbf{v} $$ is an eigenvector. If $$ A $$ has two real distinct eigenvalues $$ \lambda_1,\lambda_2 $$ with independent eigenvectors $$ \mathbf{v}_1,\mathbf{v}_2 $$, then the general solution is
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{\lambda_1 t}+c_2\mathbf{v}_2e^{\lambda_2 t}.
$$

## Common Misconceptions

- "Eigenvalues only help solve systems, not understand them." Wrong. The signs of eigenvalues directly determine stability.
- "Eigenvectors are just technical tools." Wrong. They are the truly invariant directions of the vector field.
- "If both eigenvalues are negative then all trajectories look identical." Not true. They all attract to the origin, but at different rates and along different directions.
- "The mode with larger initial coefficient will always dominate long-term." Wrong. Usually the mode with larger eigenvalue dominates as $$ t\to\infty $$.

## Suggested Learning Path

### Step 1: Find Eigenvalues

Solve the equation
$$ \det(A-\lambda I)=0. $$

### Step 2: Find Eigenvectors

Solve
$$ (A-\lambda I)\mathbf{v}=0. $$

### Step 3: Write Exponential Modes

Each eigenvalue generates one mode.

### Step 4: Combine into General Solution and Read Dynamics

This is the most important step for meaning.

### Checkpoints

- Can students correctly solve for eigenvalues and eigenvectors?
- Can students correctly write solutions in the form $$ \mathbf{v}e^{\lambda t} $$?
- Can students read attracting and repelling directions from eigenvalue signs?

## Worked Examples

### Example 1: Diagonal System

Consider
$$
A=
\begin{pmatrix}
3 & 0\\
0 & -2
\end{pmatrix}.
$$
The eigenvalues are
$$ \lambda_1=3,\qquad \lambda_2=-2, $$
with corresponding eigenvectors
$$
\mathbf{v}_1=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\mathbf{v}_2=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
General solution:
$$
\mathbf{x}(t)=
c_1e^{3t}
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^{-2t}
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
The system has one repelling direction and one attracting direction, so the origin is a saddle.

### Example 2: Non-Diagonal Matrix with Real Distinct Eigenvalues

Consider
$$
A=
\begin{pmatrix}
4 & 1\\
2 & 3
\end{pmatrix}.
$$
We have
$$
\det(A-\lambda I)=
\begin{vmatrix}
4-\lambda & 1\\
2 & 3-\lambda
\end{vmatrix}
=(4-\lambda)(3-\lambda)-2.
$$
This gives
$$ \lambda^2-7\lambda+10=0, $$
so
$$ \lambda_1=5,\qquad \lambda_2=2. $$
Both eigenvalues are positive, so every nontrivial trajectory moves away from the origin, though at two different rates.

### Example 3: Reading the Dominant Mode

If the solution has the form
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{2t}+c_2\mathbf{v}_2e^{-t},
$$
then as $$ t\to\infty $$, the mode $$ e^{2t} $$ dominates if $$ c_1\neq 0 $$. This shows long-term behavior is not determined equally by all modes.

### Example 4: Initial Conditions Select Trajectory

When given
$$ \mathbf{x}(0)=\mathbf{x}_0, $$
we solve the system
$$ \mathbf{x}_0=c_1\mathbf{v}_1+c_2\mathbf{v}_2 $$
to find $$ c_1,c_2 $$. Thus initial conditions simply select how to mix the eigenmodes.

## Conceptual Questions

1. Why are eigenvectors special directions of the flow?
2. Why do eigenvalue signs determine local stability of the origin for linear systems?
3. Why can one mode dominate the entire long-term behavior of the system?

## Application Problems

1. An economic model has one growth direction and one recession direction. Interpret this using eigenvalues of opposite signs.
2. A biological system has two relaxation modes with different rates. Explain why the slower mode is usually observed longer.
3. A linearized mechanical system around equilibrium has two positive eigenvalues. What does this say about the system's ability to maintain stability?

## Interactive Teaching Strategies

- Have students predict trajectory geometry just from the signs of two eigenvalues.
- Use a diagonal matrix first, then a non-diagonal matrix so students see eigenvalues still read dynamics the same way.
- Ask the class: "If we start exactly on an eigenvector, what will the trajectory look like?"
- Have students sketch two invariant lines before writing the general solution.

## Differentiation

### Support for Struggling Students

Struggling students should work thoroughly with 2-dimensional systems using small matrices, where eigenvalues, eigenvectors and phase portraits are all visible simultaneously. Emphasize many times that $$ \mathbf{v}e^{\lambda t} $$ is a vector solution.

### Challenge for Advanced Students

Advanced students can be asked to explain why eigenvectors corresponding to distinct eigenvalues are always linearly independent, and relate this to the existence of a solution basis.

## Summary

When a matrix has real distinct eigenvalues, the linear system separates into independent exponential modes:
$$
\mathbf{x}(t)=\sum c_i\mathbf{v}_ie^{\lambda_i t}.
$$
Eigenvalues give rate and stability sign, eigenvectors give direction of motion. This is the simplest but also most fundamental case of the chapter.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Linearized biological or economic modes
- Problem: Near equilibrium, a system may evolve along two independent real modes.
- Model:
$$ \mathbf{x}'=A\mathbf{x} $$
with two distinct real eigenvalues.
- Assumptions and limitations: Local linearization only.
- Interpretation: Each eigenvector is an invariant direction and each eigenvalue is a rate.

#### Saddle behavior in mechanics
- Problem: One mode is stable and another is unstable.
- Model:
$$ \lambda_1>0,\qquad \lambda_2<0. $$
- Assumptions and limitations: Linear or linearized setting.
- Interpretation: The saddle is crucial because it attracts in one direction and repels in another.

#### Two-speed transient response
- Problem: An engineering system has two different time scales.
- Model:
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{\lambda_1 t}+c_2\mathbf{v}_2e^{\lambda_2 t}.
$$
- Assumptions and limitations: The matrix has two independent eigenvectors.
- Interpretation: The larger eigenvalue controls the long-time picture.

### 2. Conceptual Insight

The eigenvalue method for systems is the many-dimensional analogue of the characteristic equation for scalar constant-coefficient ODEs. Each eigenvalue gives a mode, and each eigenvector gives a direction. This is one of the clearest places where linear algebra and dynamics become the same story in two languages.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

A = np.array([[3, 0],
              [0, -2]])

def system(t, X):
    return A @ X

t = np.linspace(0, 2.5, 400)
for x0 in [(1, 1), (0.5, -1), (-1, 0.5)]:
    sol = solve_ivp(system, [0, 2.5], x0, t_eval=t)
    plt.plot(sol.y[0], sol.y[1], label=f"IC={x0}")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Phase portrait with distinct real eigenvalues")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: saddle point phase portrait eigenvalues
- search: eigenvectors invariant directions visualization
- search: linear system real eigenvalues dynamics

### 5. Worked Example

Take
$$
A=
\begin{pmatrix}
3 & 0\\
0 & -2
\end{pmatrix}.
$$
The eigenvalues are
$$ \lambda_1=3,\qquad \lambda_2=-2, $$
with eigenvectors along the coordinate axes. Hence
$$
\mathbf{x}(t)=
c_1
\begin{pmatrix}
1\\
0
\end{pmatrix}
e^{3t}
+
c_2
\begin{pmatrix}
0\\
1
\end{pmatrix}
e^{-2t}.
$$
The $$ x_1 $$-axis is repelling and the $$ x_2 $$-axis is attracting, so the origin is a saddle.

### 6. Difficulty Layering

**Undergraduate level.** Solve for eigenvalues and eigenvectors correctly and build the general solution.

**Graduate level.** Read dominant modes, stability, and saddle structure directly from the spectrum.

![Real distinct eigenvalues]({{ site.imgurl }}/chapter_img/chapter04/04_03_eigenvalue_real_distinct.svg)

## Video tham khảo

- xem trước: [Solving Systems of Differential Equations with Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=Zwb5eiYcL8w) — Steve Brunton, English. Build the general solution from real, distinct eigenpairs.
- [2x2 Systems of ODEs: Sources and Sinks](https://www.youtube.com/watch?v=NaNdkCPLftc) — Steve Brunton, English. Sources and sinks: what the signs of two real eigenvalues do to the phase portrait.
- [Phương trình vi phân - Phương pháp giá trị riêng giải hệ phương trình vi phân tuyến thuần nhất](https://www.youtube.com/watch?v=LVbsb6mAFZ4) — MATH KEY, Vietnamese. A Vietnamese lecture on the eigenvalue method for a homogeneous linear system.

## References

- Boyce & DiPrima, Chapter 7: standard presentation of real eigenvalue method.
- Arnold, *Ordinary Differential Equations*: excellent for intuition about invariant directions and saddles.
