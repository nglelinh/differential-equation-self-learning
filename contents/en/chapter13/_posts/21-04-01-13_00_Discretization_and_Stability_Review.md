---
layout: post
title: "Preparatory Review: Discretization, Taylor Approximation, and Stability Intuition"
chapter: '13'
order: 0
owner: Course Team
lang: en
categories:
- chapter13
lesson_type: optional
---

## Learning Objectives

This preparatory lesson builds the conceptual foundation for numerical differential equations before any named scheme is introduced. After completing it, students should understand why discretization is necessary, how Taylor expansion justifies time-stepping formulas, why local error and global error are different, and why stability is a mathematical property of the numerical method rather than of the differential equation alone.

## Why This Lesson Matters

Students often enter numerical methods with correct analytical knowledge but the wrong expectations. They know how to solve or analyze a differential equation, so they expect a numerical method to be nothing more than an automatic calculator for the same object. But the moment one passes from a continuous model to a discrete algorithm, a new mathematical problem is created. The differential equation lives on a continuum; the numerical method lives on a mesh. The behavior of the discrete system has to be studied in its own right.

This is the conceptual heart of Chapter 13. Euler's method, Runge-Kutta methods, multistep methods, stiff solvers, finite differences, and finite elements all begin from the same shift of viewpoint:

> A differential equation is continuous in time or space, but a computer can only evolve finitely many numbers at finitely many grid points.

The aim of this lesson is to make that shift explicit before students meet the first scheme.

## Prerequisites

Students should know initial value problems for ODEs, Taylor expansions, the geometric meaning of derivatives, and the basic idea that exact solutions of many realistic models are unavailable in closed form. No prior stability theory is assumed.

## 1. From a Continuous Model to a Discrete Process

Consider an initial value problem $$ y'(t)=f(t,y(t)), \qquad y(t_0)=y_0 $$. From an analytical point of view, the unknown is a function defined for all times in an interval. From a computational point of view, this is immediately impossible: a computer cannot store a continuum of values. It can only store approximations at discrete times $$ t_n=t_0+nh $$. The first act of numerical analysis is therefore not approximation of derivatives, but replacement of the continuum by a grid. Once that decision is made, the problem changes form. We no longer ask for the exact function $$ y(t) $$ at every time. We ask for a sequence $$ y_0, y_1, y_2, \dots $$ that should track the exact solution at the mesh points.

This is why a numerical method is not simply the differential equation rewritten in another notation. It is a dynamical system on discrete data. That discrete system may preserve the geometry of the continuous problem, distort it, stabilize it, or destabilize it.

### Physical meaning

In applications, discretization is a measurement decision. A weather model, an electrical simulation, and a population forecast are not computed "for all time continuously." They are advanced in discrete steps. Choosing the step size already encodes a model of what time scales are considered visible or relevant.

## 2. Taylor Expansion as the First Numerical Principle

The most basic justification for time-stepping comes from Taylor's theorem. If the true solution is smooth enough, then near $$ t_n $$ we have

$$ y(t_n+h)=y(t_n)+hy'(t_n)+\frac{h^2}{2}y''(\xi_n) $$

for some intermediate point $$ \xi_n $$.

Since $$ y'(t_n)=f(t_n,y(t_n)) $$, the first-order approximation becomes $$ y(t_n+h)\approx y(t_n)+h f(t_n,y(t_n)) $$. This is the conceptual source of Euler's method. The point is not merely that Taylor gives a formula. The deeper point is that every one-step method can be read as a controlled approximation to the local Taylor behavior of the true solution.

### Why Taylor expansion matters beyond Euler

Higher-order Runge-Kutta methods, predictor-corrector methods, and finite difference formulas all compete in part by matching more terms of the Taylor expansion. In numerical analysis, order of accuracy is a precise way of saying how faithfully the discrete update imitates local smooth behavior of the exact solution.

## 3. Local Error Versus Global Error

One of the first conceptual traps in numerical analysis is to confuse the error made in one step with the cumulative error made after many steps.

### Local truncation error

The local truncation error measures what happens if we start a single step from the exact value and compare one discrete update with the exact solution one step later. It tests how accurate the method is as a local approximation rule.

### Global error

The global error measures the actual difference between the numerical sequence and the true solution after many steps. This error contains two effects:

- the local defect of each step,
- the propagation and amplification of previous errors.

This distinction is mathematically decisive. A method can have very small local error and still perform poorly over long time intervals if the scheme amplifies perturbations.

### Heuristic relationship

For a well-behaved first-order method such as forward Euler, the local truncation error is typically $$ O(h^2) $$, while the global error is typically $$ O(h) $$. One power of $$ h $$ is lost because the local defect accumulates over roughly $$ 1/h $$ steps on a fixed time interval.

This is the first place where students should see that numerical analysis is not just approximation theory. It is approximation plus dynamical propagation of error.

## 4. Stability: The Numerical Method Has Its Own Dynamics

The word "stability" means many things in mathematics, but in numerical ODEs it begins with a simple question:

> If we perturb the data slightly, will the discrete process magnify that perturbation uncontrollably?

This is not the same as asking whether the continuous differential equation is stable. The numerical method generates its own recurrence relation, and that recurrence has its own amplification behavior.

The standard test equation is $$ y'=\lambda y $$, especially when $$ \operatorname{Re}(\lambda)<0 $$. The true solution decays:

$$ y(t)=e^{\lambda t}y_0. $$

Any reasonable numerical method should imitate that decay, at least under suitable conditions.

### Forward Euler on the test equation

Applying forward Euler gives $$ y_{n+1}=(1+h\lambda)y_n $$. Thus the discrete behavior is governed by repeated multiplication by $$ 1+h\lambda $$. If $$ \lvert 1+h\lambda\rvert<1 $$, then perturbations decay. If not, the numerical method may oscillate or blow up even though the true solution decays smoothly.

This is the first dramatic lesson of numerical stability:

> A correct differential equation can produce qualitatively wrong numerical behavior when the step size and the scheme are mismatched.

## 5. Why Stiffness Appears

Stiffness is often introduced later in the chapter, but students benefit from an early intuition. A problem is called stiff when the continuous solution may vary on a moderate time scale, while some hidden modes decay on much faster scales. Those fast decaying modes force explicit methods to use tiny step sizes for stability, even when the solution itself no longer changes rapidly.

This is why backward Euler and other implicit methods matter. They are not merely more complicated variants of Euler. They are responses to a structural mismatch between physical time scales and explicit stability restrictions.

## 6. Worked Examples

### Example 1: Deriving a first step from Taylor expansion

Suppose $$ y'(t)=f(t,y), \qquad y(t_0)=y_0 $$. Taylor expansion gives $$ y(t_0+h)=y_0+h y'(t_0)+O(h^2) $$. Using the ODE, $$ y'(t_0)=f(t_0,y_0) $$, so $$ y(t_0+h)=y_0+h f(t_0,y_0)+O(h^2) $$. Discarding the higher-order term leads to the discrete rule $$ y_1=y_0+h f(t_0,y_0) $$. This is not yet "Euler's method" as a memorized formula. It is the first discrete consequence of Taylor approximation.

### Example 2: Why local and global errors differ

Assume a one-step method makes an error of size about $$ Ch^2 $$ in each step. Over a time interval of length $$ T $$, the number of steps is approximately $$ T/h $$. If the error does not explode, the accumulated effect is roughly

$$ \frac{T}{h}\cdot Ch^2 = CT h. $$

So the global error is of order $$ h $$. This simple counting argument is not a proof, but it explains why one loses one power of $$ h $$ between local and global accuracy.

### Example 3: Stability for a decaying equation

Consider $$ y'=-5y, \qquad y(0)=1 $$. The true solution is $$ y(t)=e^{-5t} $$. Forward Euler gives $$ y_{n+1}=(1-5h)y_n $$. If $$ h=0.1 $$, then the amplification factor is $$ 0.5 $$, so the numerical solution decays. If $$ h=0.5 $$, then the factor is $$ -1.5 $$, so the numerical solution alternates sign and grows in magnitude. The model is correct, the method is correct, but the choice of step size destroys the computation.

### Example 4: A first look at implicit stability

For the same test problem, backward Euler gives

$$ y_{n+1}=\frac{1}{1+5h}y_n. $$

Now the amplification factor is always positive and less than one for every $$ h>0 $$. This is the beginning of the idea of absolute stability and why implicit methods matter for stiff problems.

## 7. Visualization

The following Python code compares the exact solution of a decaying ODE with forward Euler at two different step sizes.

```python
import numpy as np
import matplotlib.pyplot as plt

lam = -5.0
T = 2.0

def forward_euler(h):
    n = int(T / h)
    t = np.linspace(0, n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = 1.0
    for k in range(n):
        y[k + 1] = y[k] + h * lam * y[k]
    return t, y

t_exact = np.linspace(0, T, 400)
y_exact = np.exp(lam * t_exact)

t1, y1 = forward_euler(0.1)
t2, y2 = forward_euler(0.5)

plt.figure(figsize=(8, 4))
plt.plot(t_exact, y_exact, label="exact solution", linewidth=2)
plt.plot(t1, y1, "o-", label="forward Euler, h=0.1")
plt.plot(t2, y2, "s--", label="forward Euler, h=0.5")
plt.axhline(0.0, color="black", linewidth=0.8)
plt.title("Stable and unstable step sizes for a decaying ODE")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

The graph makes the numerical lesson visible: one discretization respects the decay of the continuous model, while the other invents oscillatory instability that does not exist in the exact problem.

## 8. Common Pitfalls

### Thinking that numerical methods only approximate values

A numerical method also creates a discrete dynamical system with its own qualitative behavior.

### Thinking that smaller step size solves every difficulty

Reducing $$ h $$ helps accuracy and often helps stability, but stiffness can make explicit methods impractical no matter how conceptually simple they are.

### Confusing consistency with convergence

A method may approximate the differential equation correctly in one step and still fail globally if stability is poor.

### Treating stability as a purely technical appendix

Stability is one of the central ideas of numerical analysis because it controls whether local information produces trustworthy long-time computation.

## 9. Bridge to Chapter 13 Proper

The logic of the chapter now becomes clear.

1. Discretization replaces the continuous problem by a mesh-based recurrence.
2. Taylor expansion justifies the first update formulas.
3. Local and global errors must be distinguished.
4. Stability determines whether errors remain controlled.
5. More sophisticated methods are built by improving order, improving stability, or both.

Lesson 13.01 begins with Euler's method because it is the first complete realization of all these ideas in a single scheme. Later lessons then refine the same framework for higher-order methods, multistep methods, stiff equations, and numerical PDEs.

## References

- U. Ascher and L. Petzold, *Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations*
- E. Hairer, S. P. Norsett, and G. Wanner, *Solving Ordinary Differential Equations I*
- R. J. LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations*
