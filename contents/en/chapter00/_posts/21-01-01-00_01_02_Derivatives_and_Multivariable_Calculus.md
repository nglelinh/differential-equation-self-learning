---
layout: post
title: 00-01-02 Derivatives and Multivariable Calculus
chapter: '00'
order: 3
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Picture a weather balloon drifting through a three-dimensional wind field while its altitude, latitude, and longitude all change at once: the rate at which its thermometer reading changes depends simultaneously on how temperature varies in space and how fast the balloon moves along each axis. Multivariable calculus is the exact language that connects partial derivatives, total differentials, and vector fields—the geometric machinery behind exact ODEs, Jacobians, and nonlinear linearization.

## Key ideas: Multivariable Tools You Will Use in Every Chapter

![Đạo hàm và Giải tích Nhiều biến]({{ site.imgurl }}/chapter_img/chapter00/01_02_derivatives_and_multivariable_calculus.svg)

Four concepts from multivariable calculus reappear constantly from Chapter 1 through Chapter 5:

1. **Total Differential and Fréchet Derivative:** Differentiability of $$\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m$$ means $$\mathbf{F}(\mathbf{x} + \mathbf{h}) = \mathbf{F}(\mathbf{x}) + D\mathbf{F}(\mathbf{x})\mathbf{h} + o(\|\mathbf{h}\|)$$, where the Jacobian matrix $$D\mathbf{F}(\mathbf{x})$$ is the best linear approximation to a nonlinear system near an equilibrium.
2. **Gradient and Level Curves:** For a scalar potential $$\Psi(x,y)$$, the gradient $$\nabla \Psi = (\Psi_x, \Psi_y)$$ points perpendicular to level curves $$\Psi(x,y) = C$$; along any solution curve of an exact ODE, $$d\Psi = \Psi_x\,dx + \Psi_y\,dy = 0$$.
3. **Multivariable Chain Rule:** Tracking a scalar energy or Lyapunov function $$V(x(t), y(t))$$ along an ODE trajectory $$\mathbf{x}'(t) = \mathbf{f}(\mathbf{x}(t))$$ relies directly on $$\frac{d}{dt}V(\mathbf{x}(t)) = \nabla V(\mathbf{x}) \cdot \mathbf{f}(\mathbf{x})$$.
4. **Clairaut's Mixed-Partials Theorem:** When second partials are continuous, $$\Psi_{xy} = \Psi_{yx}$$; this symmetry is the exact test $$M_y = N_x$$ that detects whether a first-order differential form $$M\,dx + N\,dy$$ is exact.

### Worked example: Computing a Jacobian and Orbital Derivative Along a Flow

Consider the nonlinear planar system
$$x' = f_1(x,y) = y, \qquad y' = f_2(x,y) = -\sin x - \frac{1}{2}y$$
(a damped pendulum) together with its mechanical energy $$E(x,y) = \frac{1}{2}y^2 + (1 - \cos x)$$.

1. **Compute the Jacobian matrix $$J(x,y) = D\mathbf{f}(x,y)$$:**
   $$J(x,y) = \begin{pmatrix} \frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\[4pt] \frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y} \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -\cos x & -\frac{1}{2} \end{pmatrix}.$$
2. **Evaluate the linear approximation at the downward equilibrium $$(0,0)$$ and upright equilibrium $$(\pi, 0)$$:**
   - At $$(0,0)$$: $$J(0,0) = \begin{pmatrix} 0 & 1 \\ -1 & -\frac{1}{2} \end{pmatrix}$$ (trace $$-\frac{1}{2} < 0$$, determinant $$+1 > 0$$ — stable spiral!).
   - At $$(\pi,0)$$: $$J(\pi,0) = \begin{pmatrix} 0 & 1 \\ 1 & -\frac{1}{2} \end{pmatrix}$$ (determinant $$-1 < 0$$ — unstable saddle!).
3. **Compute the rate of change of energy using the multivariable chain rule:**
   $$\nabla E(x,y) = \bigl(\sin x,\; y\bigr).$$
   Taking the dot product with the vector field $$\mathbf{f}(x,y) = (y,\; -\sin x - \tfrac{1}{2}y)$$:
   $$\frac{dE}{dt} = \nabla E \cdot \mathbf{f} = (\sin x)(y) + y\left(-\sin x - \frac{1}{2}y\right) = -\frac{1}{2}y^2 \le 0.$$
4. **Interpret the result:** Without solving the nonlinear ODE at all, multivariable calculus proves that energy strictly dissipates whenever the pendulum moves ($$y \ne 0$$), forcing trajectories to settle into equilibrium.

This lesson covers derivatives and essential multivariable calculus concepts that form the foundation for optimization theory and algorithms.

---

## Derivatives and Rate of Change

The derivative of a single variable function represents its instantaneous rate of change, which is fundamental to understanding how functions behave locally.

### Basic Derivative Concepts

**Slope between two points:**

$$ \text{Slope} = \frac{y_2 - y_1}{x_2 - x_1} $$

**Derivative (instantaneous rate of change):**

$$f'(x_0) = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

The derivative tells us how quickly the function is changing at any given point, which is essential for finding optimal points where the rate of change is zero.

### Level Curves of Functions

Level curves are a fundamental concept in multivariable calculus used to visualize functions of two variables, typically denoted as $$ f(x, y) $$. They provide a way to represent a 3D surface in a 2D plane.

A **level curve** of a function $$ f(x, y) $$ is the set of all points $$ (x, y) $$ in the domain of $$ f $$ where the function takes a constant value:

$$ f(x, y) = c $$

**Examples:**
- For $$ f(x, y) = x^2 + y^2 $$, the level curves are circles: $$ x^2 + y^2 = c $$
- For $$ f(x, y) = x + y $$, the level curves are parallel lines: $$ x + y = c $$

Level curves help us understand:
1. The topography of the function
2. Directions of steepest ascent and descent
3. Locations of potential optima

---

## Multivariable Calculus Key Concepts

### Partial Derivatives

For a function $$ f(x_1, x_2, \ldots, x_n) $$, the **partial derivative** with respect to $$ x_i $$ is:

$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}$$

This measures how $$ f $$ changes when only $$ x_i $$ varies while all other variables remain fixed.

### Gradient Vector

The **gradient** is a vector composed of all partial derivatives:

$$\nabla f(\mathbf{x}) = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix}$$

The gradient points in the direction of steepest increase of the function and is perpendicular to level curves.

### Hessian Matrix

The **Hessian matrix** contains all second-order partial derivatives:

$$
\nabla^2 f(\mathbf{x}) = \mathbf{H} = \begin{pmatrix} 
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}
$$

The Hessian provides information about the curvature of the function and is crucial for:
- Determining the nature of critical points (minimum, maximum, or saddle point)
- Second-order optimization methods like Newton's method

---

## Chain Rule for Multivariable Functions

The chain rule is fundamental for computing derivatives of composite functions, which frequently appear in optimization problems.

### Basic Chain Rule

For a function $$ z = f(x, y) $$ where $$ x = g(t) $$ and $$ y = h(t) $$:

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}
$$

### General Chain Rule

For $$ z = f(x_1, x_2, \ldots, x_n) $$ where each $$ x_i = x_i(t_1, t_2, \ldots, t_m) $$:

$$
\frac{\partial z}{\partial t_j} = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} \frac{\partial x_i}{\partial t_j}
$$

### Applications in Optimization

The chain rule is essential for:

1. **Gradient Computation**: Computing gradients of composite objective functions
2. **Constraint Handling**: Dealing with constraints that are functions of other variables
3. **Algorithm Implementation**: Backpropagation in neural networks and automatic differentiation
4. **Sensitivity Analysis**: Understanding how changes in parameters affect optimal solutions

### Example: Optimization with Constraints

Consider minimizing $$ f(x, y) = x^2 + y^2 $$ subject to $$ g(x, y) = x + y - 1 = 0 $$.

Using the constraint to eliminate one variable: $$ y = 1 - x $$, so we minimize:
$$ h(x) = f(x, 1-x) = x^2 + (1-x)^2 $$

Using the chain rule:
$$h'(x) = \frac{\partial f}{\partial x} \cdot 1 + \frac{\partial f}{\partial y} \cdot \frac{d(1-x)}{dx} = 2x + 2(1-x)(-1) = 4x - 2$$

Setting $$ h'(x) = 0 $$ gives $$ x = 1/2 $$, so the optimal point is $$ (1/2, 1/2) $$.

This demonstrates how multivariable calculus concepts work together to solve optimization problems systematically.

## Video tham khảo

- xem trước: [Visualizing the chain rule and product rule | Chapter 4, Essence of calculus](https://www.youtube.com/watch?v=YG15m2VwSjA) — 3Blue1Brown, English. The chain rule picture is the tool used when an ODE right-hand side depends on several variables.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, English. Start here for the derivative as instantaneous rate of change, the meaning of y' in every later model.
- [Calculus Review: The Derivative (and the Power Law and Chain Rule)](https://www.youtube.com/watch?v=-NhgElcA3K8) — Steve Brunton, English. A short calculus review of the derivative rules used when checking that a formula solves an ODE.
