# Differential Equations and Advanced Applications
## Complete Course Structure

This document defines the full course architecture, chapter organization, and reference alignment for building lecture content.

---

## Course Philosophy

The course follows a natural mathematical progression:

```
ODE → Systems → PDE → Functional Analysis → Numerical Methods → ΨDO → Microlocal Analysis
```

Each phase builds on the previous, with theory and applications interwoven throughout.

---

## Chapter Overview

| Chapter | Title | Weeks | Primary References |
|---------|-------|-------|-------------------|
| 00 | Mathematical Foundations | 1-2 | Boyce & DiPrima (Appendices), Brezis (Ch. 1) |
| 01 | First-Order ODEs | 2-3 | Boyce & DiPrima, Zill |
| 02 | Higher-Order Linear ODEs | 3-4 | Boyce & DiPrima, Ross |
| 03 | Laplace Transforms | 4-5 | Boyce & DiPrima |
| 04 | Systems of ODEs | 5-6 | Boyce & DiPrima, Arnold |
| 05 | Nonlinear Dynamics & Stability | 6-7 | Strogatz, Arnold |
| 06 | Series Solutions & Special Functions | 7-8 | Boyce & DiPrima |
| 07 | Boundary Value Problems & Sturm-Liouville | 8-9 | Boyce & DiPrima, Haberman |
| 08 | Fourier Series & Orthogonal Expansions | 9-10 | Haberman, Evans |
| 09 | The Heat Equation | 10-11 | Evans, Haberman |
| 10 | The Wave Equation | 11-12 | Evans, Haberman |
| 11 | Laplace & Poisson Equations | 12-13 | Evans |
| 12 | Functional Analysis for PDEs | 13-14 | Brezis, Adams & Fournier |
| 13 | Numerical Methods | 14-15 | Ascher & Petzold |
| 14 | Introduction to Pseudo-Differential Operators | 15-16 | Trèves, Shubin |
| 15 | Advanced Topics & Microlocal Analysis | 16+ | Taylor, Hörmander, Zworski |

---

## Detailed Chapter Structure

### Chapter 00: Mathematical Foundations
**Directory**: `contents/{lang}/chapter00/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Real Analysis Review | required | Limits, continuity, uniform continuity |
| 2 | Derivatives & Multivariable Calculus | required | Partial derivatives, chain rule, implicit functions |
| 3 | Linear Algebra Essentials | required | Eigenvalues, eigenvectors, matrix exponentials |
| 4 | Complex Numbers & Exponentials | required | Euler's formula, complex roots |
| 5 | Introduction to Proofs in Analysis | optional | ε-δ arguments, existence proofs |
| 6 | Metric Spaces | required | Distance, Cauchy sequences, completeness |
| 7 | Normed Spaces | required | Norms, equivalence, Banach spaces |
| 8 | Inner Product Spaces | optional | Inner product, Cauchy-Schwarz, Hilbert |
| 9 | Integration Theory | required | Riemann, improper, Fubini |
| 10 | Vector Calculus | required | Gradient, divergence, curl, theorems |
| 11 | Special Functions | optional | Gamma, Bessel, Legendre |
| 12 | Illustration Gallery | optional | Visual synthesis of Chapter 00 mathematical foundations |
| 13 | Modern Applications: Scientific Machine Learning Foundations | optional | Autodiff, PINNs, neural operators, and function-space SciML (2022–2026) |

**References**: Boyce & DiPrima (Appendices), Brezis (Chapter 1)

---

### Chapter 01: First-Order Ordinary Differential Equations
**Directory**: `contents/{lang}/chapter01/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Introduction to Differential Equations | required | Classification, order, linearity |
| 2 | Separable Equations | required | Method, applications to growth/decay |
| 3 | Linear First-Order Equations | required | Integrating factors, general solution |
| 4 | Exact Equations | required | Exactness condition, potential functions |
| 5 | Substitution Methods | required | Bernoulli, homogeneous equations |
| 6 | Existence and Uniqueness | required | Picard-Lindelöf theorem, Lipschitz conditions |
| 7 | Applications: Population & Mixing | required | Logistic growth, tank problems |
| 8 | Applications: Mechanics & Circuits | required | Newton's law, RC/RL circuits |
| 9 | Autonomous Equations & Phase Lines | optional | Equilibria, stability via phase line |
| 11 | Modern Applications: Neural ODEs and Continuous-Depth Networks | optional | Continuous-depth nets, adjoints, torchdiffeq/Diffrax (2022–2026) |

**References**: Boyce & DiPrima (Ch. 1-2), Zill (Ch. 1-2), Ross

---

### Chapter 02: Higher-Order Linear ODEs
**Directory**: `contents/{lang}/chapter02/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Second-Order Linear Equations: Overview | required | Homogeneous, superposition principle |
| 2 | Constant Coefficients: Real Roots | required | Characteristic equation, distinct/repeated roots |
| 3 | Constant Coefficients: Complex Roots | required | Oscillatory solutions, Euler's formula |
| 4 | Reduction of Order | required | Finding second solutions |
| 5 | Nonhomogeneous Equations: Undetermined Coefficients | required | Polynomial, exponential, trig forcing |
| 6 | Variation of Parameters | required | General method for particular solutions |
| 7 | Higher-Order Equations | required | Extension to n-th order |
| 8 | Mechanical Vibrations | required | Free, damped, forced oscillations |
| 9 | Electrical Circuits: RLC | required | Series circuits, resonance |
| 10 | Wronskian & Linear Independence | optional | Theoretical foundations |
| 12 | Modern Applications: Hamiltonian and Second-Order Neural Models | optional | HNN/LNN, symplectic priors, learned oscillators (2019–2024) |

**References**: Boyce & DiPrima (Ch. 3-4), Zill (Ch. 3-4)

---

### Chapter 03: The Laplace Transform
**Directory**: `contents/{lang}/chapter03/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Definition & Basic Properties | required | Transform definition, linearity |
| 2 | Transforms of Elementary Functions | required | Exponentials, polynomials, trig functions |
| 3 | Inverse Laplace Transform | required | Partial fractions, table lookup |
| 4 | Solving IVPs with Laplace Transforms | required | Algebraic approach to ODEs |
| 5 | Step Functions & Discontinuous Forcing | required | Heaviside function, piecewise inputs |
| 6 | Impulse Functions & Delta Distribution | required | Dirac delta, impulse response |
| 7 | Convolution Theorem | required | Convolution integral, applications |
| 8 | Transfer Functions & Systems | optional | Input-output, frequency response |
| 10 | Modern Applications: Laplace Neural Operators and Learned Transfer Functions | optional | LNO pole-residue layers, causal operator learning (2023–2024) |

**References**: Boyce & DiPrima (Ch. 6), Zill (Ch. 7)

---

### Chapter 04: Systems of Ordinary Differential Equations
**Directory**: `contents/{lang}/chapter04/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Introduction to Systems | required | Conversion from higher-order, applications |
| 2 | Matrices & Linear Systems | required | Matrix form $$\mathbf{x}' = A\mathbf{x}$$ |
| 3 | Eigenvalue Method: Real Distinct | required | General solution construction |
| 4 | Eigenvalue Method: Complex | required | Oscillatory behavior, spirals |
| 5 | Eigenvalue Method: Repeated | required | Generalized eigenvectors |
| 6 | Matrix Exponentials | required | $$e^{At}$$, fundamental matrix |
| 7 | Phase Portraits for Linear Systems | required | Classification of equilibria |
| 8 | Nonhomogeneous Systems | required | Variation of parameters for systems |
| 9 | Applications: Coupled Oscillators | required | Normal modes, beats |
| 10 | Applications: Compartment Models | optional | Pharmacokinetics, epidemiology |
| 12 | Modern Applications: Latent ODEs and Learned Linear Systems | optional | Latent ODEs, Neural CDEs, spectral identification (2019–2022) |

**References**: Boyce & DiPrima (Ch. 7), Arnold (Ch. 1-3)

---

### Chapter 05: Nonlinear Dynamics and Stability
**Directory**: `contents/{lang}/chapter05/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Autonomous Systems & Phase Plane | required | Vector fields, trajectories |
| 2 | Equilibria & Linearization | required | Jacobian, local behavior |
| 3 | Stability Classification | required | Nodes, saddles, spirals, centers |
| 4 | Lyapunov Stability | required | Energy methods, Lyapunov functions |
| 5 | Limit Cycles | required | Poincaré-Bendixson, van der Pol |
| 6 | Bifurcations | required | Saddle-node, transcritical, pitchfork, Hopf |
| 7 | Predator-Prey Models | required | Lotka-Volterra, analysis |
| 8 | Competing Species | required | Coexistence, competitive exclusion |
| 9 | Introduction to Chaos | optional | Lorenz system, sensitivity |
| 10 | Applications: Epidemiology (SIR) | optional | Basic reproduction number |
| 12 | Modern Applications: Neural Lyapunov Functions and Learned Certificates | optional | Neural Lyapunov/barrier certificates and verification (2019–2023) |

**References**: Strogatz (primary), Arnold (geometric perspective)

---

### Chapter 06: Series Solutions and Special Functions
**Directory**: `contents/{lang}/chapter06/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Power Series Review | required | Convergence, operations |
| 2 | Series Solutions Near Ordinary Points | required | Method, recurrence relations |
| 3 | Euler Equations | required | Solutions of form $$x^r$$ |
| 4 | Series Solutions Near Regular Singular Points | required | Frobenius method |
| 5 | Bessel's Equation | required | Bessel functions, properties |
| 6 | Legendre's Equation | required | Legendre polynomials, orthogonality |
| 7 | Other Special Functions | optional | Hermite, Laguerre, Chebyshev |
| 8 | Applications in Physics | optional | Vibrating membranes, quantum mechanics |
| 10 | Modern Applications: Spectral Bases and Operator Learning | optional | DeepONet trunks, spectral PINNs, special-function priors (2021–2024) |

**References**: Boyce & DiPrima (Ch. 5), Haberman

---

### Chapter 07: Boundary Value Problems and Sturm-Liouville Theory
**Directory**: `contents/{lang}/chapter07/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Two-Point Boundary Value Problems | required | Contrast with IVPs |
| 2 | Eigenvalue Problems | required | Eigenvalues, eigenfunctions |
| 3 | Sturm-Liouville Theory | required | Self-adjoint form, orthogonality |
| 4 | Eigenfunction Expansions | required | Generalized Fourier series |
| 5 | Green's Functions for BVPs | required | Construction, applications |
| 6 | Applications: Vibrating Strings | required | Normal modes |
| 7 | Applications: Heat Conduction | required | Steady-state problems |
| 9 | Modern Applications: PINNs for Boundary Value Problems | optional | PINN BVP losses, eigenproblems, Green inverses (2021–2024) |

**References**: Boyce & DiPrima (Ch. 10-11), Haberman (Ch. 5)

---

### Chapter 08: Fourier Series and Orthogonal Expansions
**Directory**: `contents/{lang}/chapter08/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Periodic Functions & Fourier Series | required | Trigonometric series |
| 2 | Fourier Coefficients | required | Euler formulas, computation |
| 3 | Convergence of Fourier Series | required | Pointwise, uniform, L² |
| 4 | Even & Odd Functions | required | Cosine and sine series |
| 5 | Half-Range Expansions | required | Extensions to [0, L] |
| 6 | Parseval's Theorem | required | Energy and completeness |
| 7 | Complex Fourier Series | required | Exponential form |
| 8 | Fourier Transform: Introduction | optional | From series to transform |
| 9 | Illustration Gallery | optional | Visual synthesis of Chapter 08 concepts |
| 10 | Modern Applications: Fourier Neural Operators | optional | FNO, FourCastNet, spherical/deformed Fourier operators (2021–2024) |

**References**: Haberman (Ch. 3), Evans (Appendix)

---

### Chapter 09: The Heat Equation
**Directory**: `contents/{lang}/chapter09/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Derivation of the Heat Equation | required | Conservation of energy, Fourier's law |
| 2 | Separation of Variables | required | Product solutions, eigenvalue problems |
| 3 | Homogeneous Boundary Conditions | required | Dirichlet, Neumann |
| 4 | Nonhomogeneous Problems | required | Steady-state decomposition |
| 5 | Heat Equation on Infinite Domain | required | Fourier transform method |
| 6 | Fundamental Solution & Green's Functions | required | Heat kernel |
| 7 | Maximum Principles | required | Uniqueness, qualitative behavior |
| 8 | Numerical Methods: Finite Differences | optional | Explicit, implicit schemes |
| 9 | Applications: Diffusion Processes | optional | Biology, finance |
| 10 | Illustration Gallery | optional | Visual synthesis of Chapter 09 heat-equation ideas |
| 11 | Modern Applications: Neural Solvers for Diffusion and Score-Based Models | optional | Heat PINNs/operators and score-based diffusion SDEs (2021–2024) |

**References**: Evans (Ch. 2), Haberman (Ch. 1-2)

---

### Chapter 10: The Wave Equation
**Directory**: `contents/{lang}/chapter10/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Derivation of the Wave Equation | required | Vibrating string, membrane |
| 2 | d'Alembert's Solution | required | Traveling waves, characteristics |
| 3 | Separation of Variables | required | Standing waves, normal modes |
| 4 | Wave Equation in Higher Dimensions | required | Circular, spherical domains |
| 5 | Energy & Uniqueness | required | Conservation, well-posedness |
| 6 | Reflection & Transmission | required | Boundary effects |
| 7 | Dispersion & Dissipation | optional | Wave packets, damping |
| 8 | Applications: Acoustics & Electromagnetics | optional | Sound waves, Maxwell's equations |
| 9 | Illustration Gallery | optional | Visual synthesis of Chapter 10 wave-equation ideas |
| 10 | Modern Applications: Neural Wave Propagation and Seismic Imaging | optional | Wave PINNs, FBPINNs, neural inverse operators (2022–2024) |

**References**: Evans (Ch. 2), Haberman (Ch. 4)

---

### Chapter 11: Laplace and Poisson Equations
**Directory**: `contents/{lang}/chapter11/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Laplace's Equation: Introduction | required | Steady-state, harmonic functions |
| 2 | Separation of Variables in Rectangles | required | Cartesian coordinates |
| 3 | Laplace's Equation in Polar Coordinates | required | Circular domains |
| 4 | Poisson's Equation | required | Nonhomogeneous, sources |
| 5 | Mean Value Property & Maximum Principle | required | Uniqueness, qualitative behavior |
| 6 | Green's Functions for Laplace | required | Fundamental solution, method of images |
| 7 | Applications: Electrostatics | required | Potential theory |
| 8 | Applications: Fluid Flow | optional | Irrotational, incompressible flow |
| 9 | Illustration Gallery | optional | Visual synthesis of Chapter 11 elliptic ideas |
| 10 | Modern Applications: Neural Operators for Elliptic Problems | optional | Darcy/Poisson operator learning, PINO, maximum-principle tests (2021–2024) |

**References**: Evans (Ch. 2, 6), Haberman (Ch. 6-7)

---

### Chapter 12: Functional Analysis for PDEs
**Directory**: `contents/{lang}/chapter12/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 1 | Function Spaces: $$L^p$$ Spaces | required | Norms, completeness |
| 2 | Weak Derivatives | required | Distributions, generalized derivatives |
| 3 | Sobolev Spaces | required | $$H^1$$, $$H^k$$, embeddings |
| 4 | Weak Solutions of PDEs | required | Variational formulation |
| 5 | Lax-Milgram Theorem | required | Existence, uniqueness |
| 6 | Elliptic Regularity | required | Smoothness of solutions |
| 7 | Spectral Theory | optional | Eigenvalues of differential operators |
| 8 | Introduction to Distributions | optional | Test functions, generalized functions |
| 9 | Minkowski Inequality & $$L^p$$ Geometry | optional | Triangle inequality in function spaces |
| 10 | Sobolev Theory | optional | Embeddings, compactness, traces |
| 11 | Illustration Gallery | optional | Visual synthesis of Chapter 12 functional-analytic ideas |
| 12 | Modern Applications: Operator Learning in Sobolev Spaces | optional | Neural operators as maps on Banach/Sobolev spaces (2022–2024) |

**References**: Brezis (primary), Adams & Fournier (Sobolev spaces)

---

### Chapter 13: Numerical Methods for Differential Equations
**Directory**: `contents/{lang}/chapter13/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 0 | Preparatory Review: Discretization, Taylor Approximation, and Stability Intuition | optional | Bridge lesson on time grids, local/global error, and the stability viewpoint |
| 1 | Euler's Method | required | Forward, backward Euler |
| 2 | Runge-Kutta Methods | required | RK4, error analysis |
| 3 | Multistep Methods | required | Adams-Bashforth, Adams-Moulton |
| 4 | Stiff Equations | required | Stability regions, implicit methods |
| 5 | Finite Differences for PDEs | required | Heat, wave, Laplace |
| 6 | Stability & Convergence (CFL) | required | von Neumann analysis |
| 7 | Finite Element Introduction | optional | Weak form, mesh discretization |
| 8 | Stochastic Differential Equations | optional | Euler-Maruyama, applications |
| 9 | Interactive Gallery | optional | Visual synthesis of Chapter 13 numerical methods |
| 10 | Modern Applications: Differentiable Solvers and Neural SDEs | optional | torchdiffeq, Diffrax, adjoints, neural/score SDEs (2021–2024) |

**References**: Ascher & Petzold (ODEs), Kloeden & Platen (SDEs)

---

### Chapter 14: Introduction to Pseudo-Differential Operators
**Directory**: `contents/{lang}/chapter14/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 0 | Preparatory Review: Fourier Multipliers, Symbols, and Elliptic Intuition | optional | Bridge lesson on multipliers, kernels, symbols, and elliptic inversion |
| 1 | Motivation: Beyond Differential Operators | required | Limitations of classical theory |
| 2 | Fourier Transform & Symbol Calculus | required | Symbols, oscillatory integrals |
| 3 | Symbol Classes | required | $$S^m_{\rho,\delta}$$, asymptotic expansions |
| 4 | Pseudo-Differential Operators: Definition | required | Action on functions, Schwartz space |
| 5 | Composition & Adjoints | required | Symbol calculus rules |
| 6 | Elliptic Operators & Parametrices | required | Invertibility, regularity |
| 7 | ΨDOs on Manifolds | optional | Coordinate invariance |
| 8 | Applications: Elliptic Regularity Revisited | optional | Modern proofs |
| 9 | Illustration Gallery | optional | Visual synthesis of Chapter 14 pseudo-differential ideas |
| 10 | Modern Applications: Neural Operators as Learned Symbols | optional | FNO/spectral operators as learned ΨDO symbols (2022–2024) |

**References**: Trèves (primary), Shubin, Taylor

---

### Chapter 15: Advanced Topics and Microlocal Analysis
**Directory**: `contents/{lang}/chapter15/_posts/`

| Order | Lesson | Type | Description |
|-------|--------|------|-------------|
| 0 | Preparatory Review: Distributions, Fourier Localization, and Singular Support | optional | Bridge lesson on distributions, cutoff functions, singular support, and directional regularity |
| 1 | Wave Front Sets | required | Microlocal regularity |
| 2 | Propagation of Singularities | required | Characteristics revisited |
| 3 | Fourier Integral Operators | required | Beyond ΨDOs |
| 4 | Semiclassical Analysis: Introduction | optional | $$\hbar \to 0$$ limit |
| 5 | Spectral Asymptotics | optional | Weyl law |
| 6 | Applications: Inverse Problems | optional | Imaging, tomography |
| 7 | Connections to Quantum Mechanics | optional | Schrödinger equation |
| 8 | Current Research Directions | optional | Open problems |
| 9 | Microlocal Elliptic Theory | optional | Elliptic set, parametrix, regularity |
| 10 | Interactive Gallery | optional | Visual synthesis of Chapter 15 microlocal themes |
| 11 | Modern Applications: Learned Inverse Problems and Microlocal Priors | optional | Neural inverse operators, score-based imaging, visibility (2022–2024) |

**References**: Hörmander (Vol III-IV), Grigis & Sjöstrand, Zworski

---

## Reference Book Summary

### Essential (Minimal Set)
1. **Boyce & DiPrima** — Foundations, ODEs through BVPs
2. **Evans** — PDE theory gold standard
3. **Brezis** — Functional analysis bridge
4. **Strogatz** — Nonlinear dynamics intuition
5. **Trèves** — ΨDO introduction
6. **Hörmander** — Definitive advanced reference

### Supporting References
- **Zill** — Extra ODE practice
- **Ross** — Concise ODE methods
- **Arnold** — Geometric ODE perspective
- **Haberman** — Applied PDE intuition
- **Adams & Fournier** — Sobolev space details
- **Ascher & Petzold** — Numerical ODE/DAE
- **Kloeden & Platen** — Stochastic methods
- **Shubin** — ΨDO applications
- **Taylor** — Clean ΨDO pedagogy
- **Grigis & Sjöstrand** — Microlocal precision
- **Zworski** — Semiclassical connections

---

## Content Creation Guidelines

When creating lectures for this course:

1. **Reference alignment**: Each lecture should cite 1-2 primary references from the chapter's designated texts
2. **Order field**: Use sequential integers within each chapter (critical for language switching)
3. **Lesson types**: Mark foundational content as `required`, advanced/specialized as `optional`
4. **Prerequisites**: Each lecture should explicitly state which prior lectures are assumed
5. **Progression**: Later chapters may reference earlier ones; maintain forward dependency only

---

## File Naming Convention

```
YYYY-MM-DD-CC_LL_NN_Title_With_Underscores.md
```

- `YYYY-MM-DD`: Date (use consistent dates within chapters)
- `CC`: Two-digit chapter number
- `LL`: Two-digit lesson number within chapter
- `NN`: Optional sub-lesson number
- `Title`: Descriptive title with underscores

Example: `21-01-01-05_03_00_Limit_Cycles.md` (Chapter 5, Lesson 3)

---

## Current Implementation Status

| Chapter | Status | EN Posts | VI Posts |
|---------|--------|----------|----------|
| 00 | Complete | 5 | 11 |
| 01 | Complete | 9 | 9 |
| 02 | Partial | 0 | 10 |
| 03 | Partial | 0 | 8 |
| 04 | Partial | 0 | 10 |
| 05 | Partial | 0 | 10 |
| 06 | Partial | 8 | 8 |
| 07 | Partial | 0 | 5 |
| 08 | Complete | 0 | 8 |
| 09 | Complete | 0 | 9 |
| 10 | Complete | 0 | 8 |
| 11 | Complete | 0 | 8 |
| 12 | Complete | 10 | 10 |
| 13 | Complete | 0 | 8 |
| 14 | Complete | 0 | 8 |
| 15 | Complete | 9 | 9 |

---

*Last updated: April 2026*
