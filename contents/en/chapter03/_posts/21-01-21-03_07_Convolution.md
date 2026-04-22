---
layout: post
title: "03-07 The Convolution Theorem"
chapter: '03'
order: 7
owner: Course Team
lang: en
categories:
- chapter03
lesson_type: required
---
## Learning Objectives
This lesson helps students understand convolution as a way to describe the output of a linear system based on accumulating responses to past inputs, learn to state and use the theorem
$$ \mathcal{L}\{f*g\}=FG, $$
and see that convolution is precisely the bridge between ODEs, impulse response, and the systems viewpoint.

## Prerequisites
Students need to master Laplace, delta, Heaviside, and basic impulse response ideas. The skill of changing the order of integration is helpful, but this lesson can be approached very well with systems intuition first then formulas.

## Introduction
![Illustration for Lesson 03-07 The Convolution Theorem]({{ site.imgurl }}/chapter_img/chapter03/03_07_convolution.svg)

If we know how a system responds to a very short pulse, can we construct its response to an arbitrary signal? In linear time-invariant systems, the answer is yes. We view the input signal as a continuous sum of infinitely many small pulses, then add the corresponding responses. The mathematics of this idea is precisely convolution.

This is a lesson with very large conceptual significance. Before this, Laplace was mainly a tool for solving equations. With convolution, Laplace becomes the language of systems: input, output, impulse response, and system memory all enter the same unified framework.

## Three Ways to Understand the Concept
### Intuitive View
Convolution says that the current output of the system depends not only on the current input, but on the cumulative effect of all past inputs, each weighted according to how the system responds after a certain delay.

### Visual View
If $$ g(t) $$ is the impulse response of the system and $$ f(t) $$ is the input, then to compute the output at time $$ t $$, we look at each past moment $$ \tau $$, take the input amount $$ f(\tau) $$, then multiply by the response the system still "remembers" after time $$ t-\tau $$, which is $$ g(t-\tau) $$. Then we sum everything from $$ 0 $$ to $$ t $$.

### Formal View
The convolution of two functions $$ f,g $$ on $$ t\ge 0 $$ is defined by
$$ (f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau. $$
The convolution theorem states:
$$ \mathcal{L}\{f*g\}=F(s)G(s). $$
Conversely,
$$ \mathcal{L}^{-1}\{F(s)G(s)\}=f*g. $$
This is an extremely powerful tool when taking the inverse Laplace directly is difficult.

## Common Misconceptions
- "Convolution is just a new integration technique." Wrong. It carries very deep systems meaning.
- "The formula is symmetric in $$ f $$ and $$ g $$ so their roles are completely the same." Algebraically yes, but in applications we usually assign one function as input and one as impulse response.
- "If we have convolution, we don't need Laplace." Not true. The two tools complement each other very powerfully.
- "Convolution always makes the problem easier." Not necessarily. Sometimes it's a better conceptual understanding than a shorter calculation.

## Suggested Learning Sequence
### Step 1: Understand in words the meaning of accumulation over the past
This is the soul of the lesson.

### Step 2: Write the convolution formula
Recognize the triangular domain $$ 0\le \tau\le t $$.

### Step 3: Connect with Laplace
Convolution in time becomes multiplication in the $$ s $$ domain.

### Step 4: Use to solve concrete problems
Especially when impulse response is known.

### Checkpoints
- Can students interpret $$ g(t-\tau) $$ in words?
- Do students remember the integration limits from 0 to $$ t $$?
- Do students understand why convolution naturally fits systems with memory?

## Detailed Examples
### Example 1: Computing Convolution Directly
Let
$$ f(t)=1,\qquad g(t)=t. $$
Then
$$ (f*g)(t)=\int_0^t 1\cdot (t-\tau)\,d\tau. $$
Computing gives
$$
(f*g)(t)=\left[t\tau-\frac{\tau^2}{2}\right]_0^t=\frac{t^2}{2}.
$$
We can check using Laplace:
$$
\mathcal{L}\{1\}=\frac{1}{s},\qquad \mathcal{L}\{t\}=\frac{1}{s^2},
$$
so
$$ F(s)G(s)=\frac{1}{s^3}. $$
Taking inverse:
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^3}\right\}=\frac{t^2}{2},
$$
matching perfectly.

### Example 2: From $$ s $$ Domain to Convolution
Compute
$$ \mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}. $$
We recognize
$$ \frac{1}{s(s+1)}=\frac{1}{s}\cdot \frac{1}{s+1}. $$
Thus
$$
\mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}=1*e^{-t}.
$$
Therefore
$$
(1*e^{-t})(t)=\int_0^t e^{-(t-\tau)}\,d\tau=1-e^{-t}.
$$
This is a very good example because it's both short and shows direct meaning.

### Example 3: System Response with Arbitrary Input
Suppose the impulse response of a system is
$$ h(t)=e^{-t}, $$
and the input is $$ f(t) $$. Then the output is
$$ y(t)=\int_0^t f(\tau)e^{-(t-\tau)}\,d\tau. $$
This is a weighted average of all past inputs, with weights decaying according to the age of the signal. The meaning of the system's "fading memory" emerges very clearly.

### Example 4: Convolution with Delta
We have
$$ f*\delta=f. $$
This correctly reflects delta's role as the identity element of convolution. In systems terms, input being delta returns exactly the impulse response.

## Conceptual Questions
1. Why does convolution naturally describe the output of a system with memory?
2. Why does multiplication in the $$ s $$ domain correspond to convolution in the time domain?
3. In applications, where is the difference between "input" and "impulse response" important even though convolution is symmetric?

## Application Problems
1. A sensor has a response that fades over time with each small stimulus. Explain why the total output is the convolution between the input and the sensor's memory function.
2. In image and signal processing, many filters are described by convolution. State the intuitive meaning of this.
3. A mechanical system receives many small continuous stimuli. Explain why accumulating impulse responses is a reasonable model.

## Interactive Teaching Strategies
- Have students describe the convolution formula in words before computing.
- Use drawings of the triangular integration domain to help them not get confused about limits.
- Compare computing convolution directly with computing via Laplace to see two views align.
- Organize Q&A activity: "If the system remembers the past very long, what will the impulse response function look like?"

## Learning Differentiation
### Support for Struggling Students
Struggling students should start with extremely simple examples like $$ 1*t $$, $$ 1*e^{-t} $$ before talking about systems. Once familiar with the formula, the meaning part becomes easier to absorb.

### Challenge for Advanced Students
Advanced students can be asked to prove the convolution theorem by changing order of integration, or compare continuous convolution with the discrete version in digital signal processing.

## Memorable Summary
Convolution is the operation that accumulates the influence of the entire past on the present. With Laplace,
$$ \mathcal{L}\{f*g\}=FG. $$
To understand linear systems, remember: knowing the impulse response nearly means knowing the entire system, and convolution is precisely the formula that builds output from that response.

## Enrichment: Applications, Insight, and Visualization

### 1. Real-World Applications

#### Output from impulse response
- Problem: If we know how a system responds to a unit impulse, we want the response to any input.
- Model:
$$ y(t)=(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau. $$
- Assumptions and limitations: The system is linear and time-invariant.
- Interpretation: The current output is an accumulated effect of the entire past.

#### Pharmacokinetics as memory
- Problem: Current drug concentration reflects all earlier doses, not just the current one.
- Model: Input is the dosing schedule, kernel is the decay response.
- Assumptions and limitations: Linear one-compartment behavior.
- Interpretation: Convolution literally means "sum of past influence."

#### Economic memory kernels
- Problem: A policy shock leaves a decaying influence rather than disappearing instantly.
- Model: Response = shock * memory kernel.
- Assumptions and limitations: Only a linearized memory model.
- Interpretation: Convolution is the mathematical language of memory in linear systems.

### 2. Conceptual Insight

The convolution theorem
$$ \mathcal{L}\{f*g\}=FG $$
is one of the most beautiful identities in the chapter because it turns past accumulation in time into ordinary multiplication in the $$ s $$ domain. This lesson links directly to transfer functions: once we know a system's impulse response, convolution gives the output for any input.

### 3. Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 600)
dt = t[1] - t[0]
f = np.ones_like(t)
g = np.exp(-t)
y = np.convolve(f, g)[:len(t)] * dt

plt.plot(t, f, label="f(t)=1")
plt.plot(t, g, label="g(t)=e^{-t}")
plt.plot(t, y, label="(f*g)(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Convolution as accumulated memory")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. External Search Prompts

- search: convolution animation signal processing
- search: impulse response and convolution visualization
- search: moving overlap convolution intuition

### 5. Worked Example

Let
$$ f(t)=1,\qquad g(t)=e^{-t}. $$
Then
$$ (f*g)(t)=\int_0^t e^{-(t-\tau)}\,d\tau. $$
Evaluating the integral,
$$ (f*g)(t)=1-e^{-t}. $$
From a systems perspective, this says a unit-step input filtered by an exponential memory kernel rises gradually rather than jumping instantly.

### 6. Difficulty Layering

**Undergraduate level.** Learn the formula and explain the meaning of $$ g(t-\tau) $$ in words.

**Graduate level.** Prove the theorem carefully and connect it with impulse-response theory for general LTI systems.

![Convolution]({{ site.imgurl }}/chapter_img/chapter03/03_07_convolution.svg)

## References
- Boyce & DiPrima — *Elementary Differential Equations*: the convolution section is very suitable for transitioning to systems language.
- Zill — *Differential Equations with Boundary-Value Problems*: many examples connecting convolution with practical forcing.
- Ross — *Differential Equations*: useful for reviewing formulas and a few short example patterns.
