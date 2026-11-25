---
layout: post
title: "06-03 Euler Equations (Equidimensional in x)"
chapter: '06'
order: 3
owner: Course Team
lang: en
categories:
- chapter06
lesson_type: required
---

Step away from uniform straight beams and look at a circular drumhead, a spherical planet's gravitational field, or the electrostatic potential around a charged needle. The moment you switch from Cartesian coordinates to polar or spherical coordinates, the Laplacian automatically multiplies derivatives by powers of the radial distance $$ r $$: $$ r^2 y'' + \alpha r y' + \beta y = 0 $$. At $$ r = 0 $$, the leading coefficient vanishes—ordinary power series can blow up or develop fractional powers—yet the equation obeys a hidden geometric symmetry.

If you rescale $$ x \mapsto \lambda x $$, the operator $$ x \frac{d}{dx} $$ stays completely unchanged! That scale invariance is the soul of the Cauchy–Euler equation, and it makes $$ x^r $$ the exact eigenfunction of scale-invariant differential operators, just as $$ e^{rt} $$ is the eigenfunction of translation-invariant ones.

## Key ideas: Scale Invariance and Euler Equations

1. **Scale-Invariant Derivative Operator $$ \vartheta = x \frac{d}{dx} $$ (Lie Symmetry):** Under the change of variable $$ t = \ln x $$ (for $$ x > 0 $$), the chain rule gives $$ x \frac{d}{dx} = \frac{d}{dt} $$ and $$ x^2 \frac{d^2}{dx^2} = \frac{d^2}{dt^2} - \frac{d}{dt} $$. This transforms every Cauchy–Euler equation into a constant-coefficient linear ODE in $$ t $$, explaining *why* powers $$ x^r $$, logarithms $$ x^r \ln x $$, and log-oscillations $$ x^\alpha \cos(\beta \ln x) $$ appear.
2. **The Indicial Quadratic Equation (Algebraic Spectrum):** Substituting $$ y = x^r $$ produces $$ \bigl[a r(r-1) + b r + c\bigr] x^r = 0 $$. The three root regimes—distinct real, repeated real, and complex conjugate—mirror the three regimes of constant-coefficient ODEs, only viewed through the logarithmic lens $$ t = \ln x $$.
3. **Regular Singular Points Prototype (Bridge to Frobenius):** Writing $$ y'' + \frac{b}{ax} y' + \frac{c}{ax^2} y = 0 $$ shows that $$ x = 0 $$ is a *regular singular point*. Every more general equation with a regular singular point behaves asymptotically like a Cauchy–Euler equation as $$ x \to 0 $$, which is why Euler equations are the launchpad for the Frobenius method.
4. **Domain Extension to $$ x < 0 $$:** Using $$ |x|^r $$ and $$ \ln|x| $$ extends solutions cleanly to $$ (-\infty, 0) $$, while $$ x = 0 $$ remains a boundary where solutions may diverge, oscillate infinitely rapidly, or stay bounded depending on $$ \operatorname{Re}(r) $$.

### Worked example: Solving a Repeated-Root and Complex-Root Euler Pair

**Problem:** Solve the initial-value problem $$ x^2 y'' - 3x y' + 4y = 0 $$ with $$ y(1) = 2 $$, $$ y'(1) = 7 $$ for $$ x > 0 $$, and verify both the ODE and initial conditions directly.

1. **Form the indicial equation using $$ y = x^r $$:**
   Since $$ y' = r x^{r-1} $$ and $$ y'' = r(r-1)x^{r-2} $$, substituting gives
   $$ \bigl[r(r-1) - 3r + 4\bigr] x^r = 0 \implies r^2 - 4r + 4 = (r - 2)^2 = 0. $$
2. **Identify the repeated root and build the general solution:**
   The double root is $$ r_1 = r_2 = 2 $$. Under $$ t = \ln x $$, the transformed ODE is $$ \ddot{y} - 4\dot{y} + 4y = 0 $$, whose general solution is $$ (c_1 + c_2 t)e^{2t} $$. Returning to $$ x = e^t $$ yields
   $$ y(x) = c_1 x^2 + c_2 x^2 \ln x \qquad (x > 0). $$
3. **Apply the initial conditions at $$ x = 1 $$:**
   First compute the derivative by the product rule:
   $$ y'(x) = 2c_1 x + c_2 (2x \ln x + x). $$
   Evaluate at $$ x = 1 $$ (using $$ \ln 1 = 0 $$):
   - $$ y(1) = c_1(1) + c_2(0) = 2 \implies c_1 = 2 $$.
   - $$ y'(1) = 2c_1 + c_2 = 7 \implies 4 + c_2 = 7 \implies c_2 = 3 $$.
   Thus the unique solution is
   $$ y(x) = 2x^2 + 3x^2 \ln x. $$
4. **Hand-verify the ODE directly:**
   - $$ y'(x) = 4x + 6x\ln x + 3x = 7x + 6x\ln x $$.
   - $$ y''(x) = 7 + 6\ln x + 6 = 13 + 6\ln x $$.
   Plug into the left-hand side:
   $$ x^2(13 + 6\ln x) - 3x(7x + 6x\ln x) + 4(2x^2 + 3x^2\ln x) = (13 - 21 + 8)x^2 + (6 - 18 + 12)x^2\ln x = 0. $$
   Both coefficients cancel identically to zero, and $$ y(1) = 2, y'(1) = 7 $$!

This lesson presents Euler equidimensional equations—the simplest case where series solutions reduce to elementary guess and verify. These are the "polynomial" solutions that precede full power series.

> **Teaching Notes**: Quick lesson. Students already know how to solve these from Chapter 2 (characteristic equation). Emphasize why these are the "model problem" for singular points. Activity: "Identification Game" (10 min)—given ODE, identify as Euler or not.

---

## Introduction

Euler equations (also called **equidimensional equations**) have the form where each term's power matches its derivative order:

$$ x^2 y'' + ax y' + by = 0 $$

The power of $$ x $$ equals the order of derivative. This special form means trying $$ y = x^r $$ will work—we get a polynomial equation for $$ r $$.

> **Intuitive**: These are "self-similar" equations: if you zoom in at $$ x = 0 $$, the equation looks the same at every scale. This is why $$ x^r $$ works—it's the only function with that property.

---

## 1. The Method

### 1.1 Trial Solution

For Euler equation, try:
$$ y = x^r $$

Then:
$$ y' = r x^{r-1}, \quad y'' = r(r-1)x^{r-2} $$

Substitute into $$ x^2y'' + axy' + by = 0 $$:
$$x^2 \cdot r(r-1)x^{r-2} + ax \cdot r x^{r-1} + b x^r = x^r[r(r-1) + ar + b] = 0$$

The bracket must vanish:
$$r(r-1) + ar + b = 0 \Rightarrow r^2 + (a-1)r + b = 0$$

This is the **indicial equation** (polynomial in $$ r $$).

> **Visual**: Show that $$ x^r $$ differentiates to lower powers of $$ x $$, canceling the $$ x^2 $$ factor.

### 1.2 Three Cases

**Case 1: Distinct real roots** $$ r_1 \neq r_2 $$:
$$ y = C_1 x^{r_1} + C_2 x^{r_2} $$

**Case 2: Repeated real root** $$ r_1 = r_2 = r $$:
$$ y = C_1 x^r + C_2 x^r \ln x $$

**Case 3: Complex roots** $$ r = \alpha \pm i\beta $$:
$$y = x^\alpha[C_1 \cos(\beta \ln x) + C_2 \sin(\beta \ln x)]$$

> **Checkpoint**: Can students handle all three cases? When do we get $$ \ln x $$ terms?

---

## 2. Worked Examples

### Example 1: $$ x^2 y'' - xy' + y = 0 $$

Indicial: $$ r(r-1) - r + 1 = r^2 - 2r + 1 = (r-1)^2 = 0 $$
Repeated root: $$ r = 1 $$ (double)

Solution: $$ y = C_1 x^1 + C_2 x^1 \ln x = C_1 x + C_2 x \ln x $$

### Example 2: $$ x^2 y'' + 3xy' + y = 0 $$

Indicial: $$ r(r-1) + 3r + 1 = r^2 + 2r + 1 = (r+1)^2 = 0 $$
Repeated root: $$ r = -1 $$

Solution: $$ y = C_1 x^{-1} + C_2 x^{-1} \ln x $$

### Example 3: $$ x^2 y'' + xy' + y = 0 $$

Indicial: $$ r(r-1) + r + 1 = r^2 + 1 = 0 $$
Complex roots: $$ r = \pm i $$

Solution: $$ y = C_1 \cos(\ln x) + C_2 \sin(\ln x) $$

This is periodic in $$ \ln x $$—not periodic in $$ x $$, but oscillates as $$ \ln x $$ increases.

---

## 3. Why Euler Equations Matter

### 3.1 They're the Model Problems

Euler equations represent the behavior near singular points. When we study Frobenius method later, we'll see that solutions near singular points look like $$ x^r $$ plus logarithms.

### 3.2 Connection to Regular Singular Points

The Euler equation $$ x^2y'' + axy' + by = 0 $$ is exactly the "test equation" for the Frobenius method:
- If an ODE can be transformed to this form near $$ x=0 $$, it has regular singular points
- The roots $$ r $$ tell us the behavior near the singular point

> **Intuitive**: $$ x^r $$ is the "eigenfunction" of the singular point. Its behavior determines whether the point is regular or irregular.

---

## 4. Common Errors

| Error | Correction |
|-------|------------|
| Forgetting to get $$ x^r $$ in front | The solution must include $$ x^r $$: $$ y = x^r \ln x $$, not just $$ \ln x $$ |
| Missing $$ \ln x $$ for repeated roots | Always check discriminant of indicial! |
| Complex roots giving real-imaginary mix | Use real forms $$ \cos(\beta\ln x) $$, $$ \sin(\beta\ln x) $$ |

> **Common Misconception**: "Complex roots give oscillatory solutions." They give oscillatory in $$ \ln x $$, which means power-law growth/decay plus oscillation in $$ x $$.

---

## 5. Higher-Order Euler Equations

For $$ n $$-th order equation with constant-coefficient-like structure in powers of $$ x $$:
$$x^n y^{(n)} + a_{n-1} x^{n-1} y^{(n-1)} + \cdots + a_0 y = 0$$

Try $$ y = x^r $$. The indicial polynomial will be degree $$ n $$ in $$ r $$. Solve for roots, handle cases as before.

---

## 6. Conceptual Questions

1. **Why does $$ x^r $$ work?** $$ \rightarrow $$ Because derivatives of $$ x^r $$ are $$ x^{r-k} $$, which all have the same power scaling—the $$ x^2 $$ factor exactly cancels.

2. **Why do repeated roots give $$ \ln x $$?** $$ \rightarrow $$ When the repeated root blocks the second independent solution, $$ \ln x $$ is the only new function that works. It's the "integral factor" for singular problems.

3. **What happens if roots differ by an integer?** $$ \rightarrow $$ This signals trouble for second solutions—we may need to include $$ \ln x $$ terms. This is the "indicial conflict" that leads to the Frobenius method.

---

## Interactive Activities

### Activity: "Identification Game" (10 min)

Given ODEs, students identify which are Euler-type:

| ODE | Euler? | Reason |
|-----|-------|--------|
| $$ x^2 y'' + xy' + y = 0 $$ | ✓ | Powers match derivative order |
| $$ x y'' + y' + y = 0 $$ | ✗ | $$ x y'' $$ has only $$ x^1 $$, but $$ y'' $$ is degree 2 |
| $$ (1+x)^2 y'' + (1+x)y' + y = 0 $$ | ✗ | Not pure power structure |
| $$ x^2 y'' + 2xy' + y = 0 $$ | ✓ | Standard Euler form |

---

## Summary

| Case | Roots | Solution |
|------|-------|----------|
| Distinct real | $$ r_1 \neq r_2 $$ | $$ C_1 x^{r_1} + C_2 x^{r_2} $$ |
| Repeated real | $$ r = r $$ | $$ C_1 x^r + C_2 x^r \ln x $$ |
| Complex | $$ \alpha \pm i\beta $$ | $$x^\alpha[C_1 \cos(\beta\ln x) + C_2 \sin(\beta\ln x)]$$ |

> **One-Liner**: Euler equations are the "model singular point" problems—try $$ x^r $$, get polynomial indicial, handle repeated roots with $$ \ln x $$.

---

## Extended: Applications, Intuition, and Visualization

### 1. Real-World Applications

#### Radial scaling in physics
- Problem: Scale-invariant radial models in heat or potential theory often lead to Cauchy-Euler equations.
- Model:
$$ x^2 y''+a x y'+b y=0. $$
- Assumptions and limitations: The problem is posed on $$ x>0 $$ and has scaling symmetry.
- Interpretation: Power-law solutions mirror the underlying self-similar structure of the model.

#### Elasticity or economic growth with constant elasticities
- Problem: A quantity evolves under coefficients proportional to inverse powers of the independent variable.
- Model:
$$ t^2 K''+\alpha t K'+\beta K=0. $$
- Assumptions and limitations: This is an idealized scale-invariant model.
- Interpretation: The solution modes are powers of $$ t $$, or oscillations in $$ \ln t $$ when the characteristic roots are complex.

### 2. Additional Intuition and Connections

Euler equations are special because the natural ansatz is $$ x^r $$ rather than $$ e^{\lambda x} $$. The substitution $$ x=e^t $$ converts them to constant-coefficient equations. A common pitfall is to forget the extra $$ \ln x $$ factor in the repeated-root case or the logarithmic oscillation in the complex-root case.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.2, 5, 400)
y1 = x**2
y2 = x**2 * np.log(x)

plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^2 log x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Typical solution shapes for Euler equations")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Suggested Searches

- search: Cauchy Euler equation log transform
- search: equidimensional equation power law solutions
- search: scaling invariant ODE visualization

### 5. Worked Example

Consider
$$ x^2 y''-3x y'+4y=0. $$
With the ansatz $$ y=x^r $$, the indicial or characteristic equation is
$$ r(r-1)-3r+4=0, $$
so
$$ r^2-4r+4=(r-2)^2=0. $$
The repeated root $$ r=2 $$ gives
$$ y=C_1 x^2+C_2 x^2\ln x. $$

### 6. Difficulty Layering

**Undergraduate level.** Master the three cases of the power ansatz: distinct, repeated, and complex roots.

**Graduate level.** Emphasize scaling symmetry, the substitution $$ x=e^t $$, and self-similar solution structure.

![Euler equations]({{ site.imgurl }}/chapter_img/chapter06/06_03_euler_equations.svg)

## Video tham khảo

- xem trước: [Cauchy Euler Differential Equation (equidimensional equation)](https://www.youtube.com/watch?v=zXZ4qmDpblE) — blackpenredpen, English. The Cauchy-Euler equation and the trial solution x^r.
- [Cauchy-Euler Differential Equations (2nd Order)](https://www.youtube.com/watch?v=ep7xoctAlEY) — Houston Math Prep, English. A second-order Cauchy-Euler equation worked in full.
- [Introduction to Cauchy Euler Differential Equations](https://www.youtube.com/watch?v=oqpc89Lfx-E) — The Math Sorcerer, English. Why the equidimensional equation is the model singular equation.

## References

- Boyce & DiPrima, Section 5.3: Euler equation as Frobenius special case
- Coddington & Levinson: theoretical backup for regular singular points
