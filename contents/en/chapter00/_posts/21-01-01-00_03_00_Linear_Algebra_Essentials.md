---
layout: post
title: "00-03-00 Linear Algebra Essentials"
chapter: '00'
order: 4
owner: Course Team
lang: en
categories:
- chapter00
lesson_type: required
---

Suppose three coupled masses oscillate on springs between two walls: at first glance their positions $$x_1(t), x_2(t), x_3(t)$$ seem hopelessly tangled, because every mass pulls on its neighbors. Linear algebra reveals that if you rotate your coordinate system into the matrix's eigenvectors, the tangled system splits cleanly into three independent one-dimensional motions. Almost every theorem about linear ODEs—from Wronskians to matrix exponentials—is linear algebra wearing calculus clothes.

## Key ideas: Linear Algebra as the Skeleton of Linear ODEs

![Đại số Tuyến tính Cốt lõi]({{ site.imgurl }}/chapter_img/chapter00/03_00_linear_algebra_essentials.svg)

Four linear-algebraic pillars organize Chapters 2 and 4 of this course:

1. **Vector Spaces and Superposition:** The solution set of an $$n$$th-order homogeneous linear ODE $$L[y] = 0$$ (or a system $$\mathbf{x}' = A\mathbf{x}$$) is an $$n$$-dimensional vector space; finding $$n$$ linearly independent solutions completely characterizes *every* possible motion.
2. **Linear Independence and Determinants:** Checking whether candidate solutions span the solution space reduces to testing whether a matrix determinant (the Wronskian or fundamental matrix determinant) is nonzero.
3. **Eigenvalues and Eigenvectors ($$A\mathbf{v} = \lambda\mathbf{v}$$):** An eigenvector is a direction preserved by the dynamics; along that line, the matrix system $$\mathbf{x}' = A\mathbf{x}$$ collapses to the scalar exponential $$c\,e^{\lambda t}\mathbf{v}$$.
4. **Diagonalization and Generalized Eigenvectors:** When $$A = PDP^{-1}$$, powers and exponentials simplify to $$e^{At} = Pe^{Dt}P^{-1}$$; when $$A$$ is defective (missing eigenvectors), Jordan chains explain why secular terms like $$t\,e^{\lambda t}$$ appear.

### Worked example: Diagonalizing a $$2\times 2$$ Matrix to Predict System Evolution

Let $$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$. We will find its eigenpairs, verify $$A = PDP^{-1}$$, and compute $$A^3$$ effortlessly.

1. **Form and solve the characteristic polynomial $$\det(A - \lambda I) = 0$$:**
   $$\det\begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix} = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2) = 0.$$
   So the eigenvalues are $$\lambda_1 = 5$$ and $$\lambda_2 = 2$$. (Check: $$\text{tr}(A) = 4+3 = 7 = 5+2$$ and $$\det(A) = 12-2 = 10 = 5\cdot 2$$.)
2. **Find an eigenvector for each eigenvalue:**
   - For $$\lambda_1 = 5$$: $$(A - 5I)\mathbf{v}_1 = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}\mathbf{v}_1 = \mathbf{0} \implies \mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$.
   - For $$\lambda_2 = 2$$: $$(A - 2I)\mathbf{v}_2 = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}\mathbf{v}_2 = \mathbf{0} \implies \mathbf{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$$.
3. **Assemble $$P$$, $$D$$, and $$P^{-1}$$:**
   $$P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}, \qquad D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}, \qquad \det(P) = -3, \qquad P^{-1} = -\frac{1}{3}\begin{pmatrix} -2 & -1 \\ -1 & 1 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}.$$
4. **Verify $$PDP^{-1} = A$$ and compute $$A^3$$:**
   $$A^3 = P D^3 P^{-1} = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} 125 & 0 \\ 0 & 8 \end{pmatrix}\frac{1}{3}\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 258 & 117 \\ 234 & 141 \end{pmatrix} = \begin{pmatrix} 86 & 39 \\ 78 & 47 \end{pmatrix}.$$
   Exactly the same similarity transform turns $$\mathbf{x}' = A\mathbf{x}$$ into $$e^{At} = P\operatorname{diag}(e^{5t}, e^{2t})P^{-1}$$ in Chapter 4!

This lesson covers the linear algebra concepts essential for systems of differential equations.

## Topics to Cover

- Eigenvalues and eigenvectors
- Matrix exponentials
- Diagonalization
- Jordan normal form

## Key Concepts

For a matrix $$ A $$, eigenvalues $$ \lambda $$ satisfy:

$$ \det(A - \lambda I) = 0 $$

The matrix exponential is defined as:

$$ e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!} $$

## Video tham khảo

- xem trước: [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) — 3Blue1Brown, English. Eigenvectors are the directions a linear system stretches, which is exactly how x'=Ax is solved.
- [Vectors | Chapter 1, Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs) — 3Blue1Brown, English. Vectors and linear combinations are the language of the state vector in a first-order system.
- [How (and why) to raise e to the power of a matrix | DE6](https://www.youtube.com/watch?v=O85OWBJ2ayo) — 3Blue1Brown, English. Why the matrix exponential is the closed form of a linear system with constant coefficients.

## References

- Boyce & DiPrima, Chapter 7 (Appendix)
- Arnold, Chapters 1-2

---

*This is a placeholder lesson. Full content to be developed.*
