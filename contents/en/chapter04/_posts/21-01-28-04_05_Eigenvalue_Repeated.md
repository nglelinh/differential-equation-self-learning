---
layout: post
title: "04-05 Eigenvalue Method: Repeated"
chapter: '04'
order: 5
owner: Course Team
lang: en
categories:
- chapter04
lesson_type: required
---

## Learning Objectives

This lesson helps students handle the case of repeated eigenvalues, distinguish between "repeated eigenvalue but enough eigenvectors" and "repeated eigenvalue lacking eigenvectors," understand the role of generalized eigenvectors, and recognize why terms like $$ te^{\lambda t} $$ appear in solutions.

## Prerequisites

Students need to grasp eigenvalues, eigenvectors, solutions for systems with real distinct eigenvalues, and some intuition about linear independence. This is the lesson where Jordan structure begins to appear in concrete dynamical form.

## Introduction

![Repeated eigenvalue and generalized eigenvector]({{ site.imgurl }}/chapter_img/chapter04/05_eigenvalue_repeated.svg)

When eigenvalues are repeated, many students tend to think the system is just the old case but with fewer different numbers. In reality this is a much more subtle step. If the matrix still has enough eigenvectors, things remain fairly smooth. But if there are not enough eigenvectors, the system cannot be diagonalized, and dynamics exhibit a new component that is no longer pure exponential: terms with an additional factor of $$ t $$.

This is when students clearly see that linear algebra not only allows solving problems, but also tells when a system has a structure lacking "eigen-directions" and must be supplemented by generalized directions. The geometry of trajectories also changes: there is a principal direction and a sliding effect along that direction.

## Concept in Three Ways

### Intuitive View

If in the nice case the system has enough independent dynamical directions, then in the repeated case lacking eigenvectors, one principal direction must "carry" an additional auxiliary direction attached to it. Trajectories do not just contract or expand exponentially, but also slide along that direction at the rhythm of time.

### Visual View

When eigenvalues are repeated and the matrix is not diagonalizable, trajectories are still attracted or repelled along a dominant direction, but not as beautifully symmetric as the diagonalizable case. Terms $$ te^{\lambda t} $$ are precisely the trace of this eigenvector deficiency in the geometry.

### Formal View

If $$ \lambda $$ is a repeated eigenvalue with only one eigenvector $$ \mathbf{v} $$, we find a generalized eigenvector $$ \mathbf{w} $$ satisfying
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$
Then two independent solutions can be chosen as
$$ e^{\lambda t}\mathbf{v}, $$
and
$$ e^{\lambda t}(t\mathbf{v}+\mathbf{w}). $$
Thus the general solution is
$$
\mathbf{x}(t)=c_1e^{\lambda t}\mathbf{v}+c_2e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$

## Common Misconceptions

- "Repeated eigenvalues always cause the same difficulty." Wrong. Need to check whether there are enough eigenvectors.
- "If eigenvalues are repeated, just multiply by another constant." Wrong. When eigenvectors are lacking, must have terms with additional factor $$ t $$.
- "Generalized eigenvectors are just formal tricks." Wrong. They compensate for missing eigen-directions.
- "Two matrices with the same repeated eigenvalue will have the same geometry." Not true. The number of eigenvectors determines large differences.

## Suggested Learning Path

### Step 1: Find Repeated Eigenvalue

Recognize that the characteristic polynomial has repeated roots.

### Step 2: Check Number of Eigenvectors

This is the most important branching step.

### Step 3: If Eigenvectors Are Lacking, Find Generalized Eigenvector

Solve
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$

### Step 4: Write General Solution

Remember the appearance of $$ t\mathbf{v}+\mathbf{w} $$.

### Checkpoints

- Can students distinguish between repeated but diagonalizable and repeated non-diagonalizable?
- Can students correctly find generalized eigenvectors?
- Do students understand why the factor $$ t $$ appears?

## Worked Examples

### Example 1: Repeated Eigenvalue but Enough Eigenvectors

The matrix
$$
A=
\begin{pmatrix}
2 & 0\\
0 & 2
\end{pmatrix}
$$
has repeated eigenvalue $$ \lambda=2 $$, but every nonzero vector is an eigenvector. The general solution is simply
$$ \mathbf{x}(t)=e^{2t}\mathbf{c}. $$
This is an important reminder: repeated eigenvalue does not necessarily cause trouble.

### Example 2: Repeated Eigenvalue Lacking Eigenvectors

Consider
$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$
The only eigenvalue is $$ \lambda=1 $$. We have
$$
A-I=
\begin{pmatrix}
0 & 1\\
0 & 0
\end{pmatrix}.
$$
Solving
$$ (A-I)\mathbf{v}=0 $$
gives eigenvector
$$
\mathbf{v}=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Next find $$ \mathbf{w} $$ such that
$$ (A-I)\mathbf{w}=\mathbf{v}. $$
Writing
$$
\mathbf{w}=
\begin{pmatrix}
w_1\\
w_2
\end{pmatrix},
$$
we need
$$
\begin{pmatrix}
w_2\\
0
\end{pmatrix}
=
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$
so we can take
$$
\mathbf{w}=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
General solution:
$$
\mathbf{x}(t)=c_1e^t
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^t
\left(
t
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
\begin{pmatrix}
0\\
1
\end{pmatrix}
\right)
=
e^t
\begin{pmatrix}
c_1+c_2t\\
c_2
\end{pmatrix}.
$$

### Example 3: Meaning of Factor $$ t $$

The term
$$ te^{\lambda t} $$
shows that beyond exponential contraction or expansion there is a linear sliding effect over time. This is precisely the dynamical signature of a Jordan block.

### Example 4: Comparing Two Systems with Same Eigenvalue

The two matrices
$$
\begin{pmatrix}
2 & 0\\
0 & 2
\end{pmatrix}
\qquad \text{and} \qquad
\begin{pmatrix}
2 & 1\\
0 & 2
\end{pmatrix}
$$
both have repeated eigenvalue $$ 2 $$, but the first is diagonalizable while the second is not. This comparison is excellent for teaching that eigenvalues alone don't tell the whole story.

## Conceptual Questions

1. Why don't repeated eigenvalues automatically lead to difficulty?
2. What is missing in the solution structure that generalized eigenvectors compensate for?
3. Why is the term $$ te^{\lambda t} $$ a characteristic signature of the non-diagonalizable case?

## Application Problems

1. A control system has two modes of the same rate but only one eigen-direction. How might this affect trajectory shape?
2. In linearized mechanics, why can two systems with the same eigenvalues still give different trajectories?
3. A multi-step numerical model generates a matrix close to Jordan form. Predict what geometric difficulties might appear.

## Interactive Teaching Strategies

- Compare directly two matrices with the same repeated eigenvalue but different numbers of eigenvectors.
- Have students find generalized eigenvectors in groups, as this step is prone to algebraic errors but very worthwhile to do themselves.
- Ask the class: "If we're missing an eigenvector, what kind of information do we need to add to have a full solution basis?"
- Sketch trajectories for both diagonalizable and non-diagonalizable cases to emphasize geometric differences.

## Differentiation

### Support for Struggling Students

Struggling students should use a clear checklist: find eigenvalues, find number of eigenvectors, if lacking then solve equation for generalized eigenvector, then write solution. Avoid having them jump straight to formulas with $$ t $$ without understanding the reason.

### Challenge for Advanced Students

Advanced students can be asked to directly relate this case to Jordan form and the matrix exponential of a Jordan block, to see the solution formula emerges very naturally from
$$ e^{Jt}. $$

## Summary

Repeated eigenvalues are only truly difficult when eigenvectors are lacking. Then we need generalized eigenvectors and new solutions will contain
$$ te^{\lambda t}. $$
To handle correctly, always ask two questions: are eigenvalues repeated, and are there enough eigenvectors?

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Systems lacking enough eigen-directions
- Problem: A matrix may have a repeated eigenvalue but not enough eigenvectors to span the space.
- Model:
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$
- Assumptions and limitations: The matrix is not diagonalizable.
- Interpretation: The generalized eigenvector compensates for the missing true eigen-direction.

#### Jordan-type control response
- Problem: A repeated mode in a linear system creates an extra factor of $$ t $$ in the time response.
- Model:
$$
\mathbf{x}(t)=c_1e^{\lambda t}\mathbf{v}+c_2e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$
- Assumptions and limitations: One Jordan block of size 2.
- Interpretation: The factor $$ t $$ is a dynamical fingerprint of non-diagonalizability.

#### Sliding motion along a dominant direction
- Problem: Even with one repeated eigenvalue, a system can still have two independent directions of motion once generalized vectors are included.
- Model: Repeated eigenvalue with geometric deficiency.
- Assumptions and limitations: Special but essential case.
- Interpretation: A second constant is not enough; a new time-dependent structure appears.

### 2. Conceptual Insight

This lesson is where Jordan structure stops being abstract and becomes visible in trajectories. Students often memorize the rule “add a factor of $$ t $$,” but the deeper reason is missing eigenvector structure. This also prepares the way for matrix exponentials and Jordan blocks later in the chapter.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 400)
x1 = np.exp(t)
x2 = t * np.exp(t)

plt.plot(t, x1, label=r"$e^t$")
plt.plot(t, x2, label=r"$t e^t$")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Generalized-eigenvector time factor")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: Jordan block phase portrait visualization
- search: repeated eigenvalue generalized eigenvector intuition
- search: te^lambda t linear system explanation

### 5. Worked Example

Consider
$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$
The only eigenvalue is
$$ \lambda=1. $$
One eigenvector is
$$
\mathbf{v}=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Find a generalized eigenvector from
$$ (A-I)\mathbf{w}=\mathbf{v}. $$
One valid choice is
$$
\mathbf{w}=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Then the general solution contains both
$$ e^t\mathbf{v} $$
and
$$ e^t(t\mathbf{v}+\mathbf{w}), $$
which explains the appearance of the extra time factor.

### 6. Difficulty Layering

**Undergraduate level.** Clearly distinguish repeated-but-diagonalizable from repeated-and-defective cases.

**Graduate level.** Connect with Jordan blocks, minimal polynomials, and non-diagonalizable flow structure.

![Repeated eigenvalues]({{ site.imgurl }}/chapter_img/chapter04/04_05_eigenvalue_repeated.svg)

## References

- Boyce & DiPrima, Chapter 7: section on repeated eigenvalues and generalized eigenvectors is very foundational for techniques.
- Arnold, *Ordinary Differential Equations*: good for understanding geometric meaning of Jordan structure.
