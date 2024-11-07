# Week 2

## Dynamic systems
%%[[2024-10-04]] @ 09:13%%

A dynamic system is a system where the state variable is in flux.

### 

$x$ state variable
$y$ output variable

$u$ control variable

all of these can be $n$ dimensional vectors.

$y(t) = g(x,u,t)$

$\dot x = f(x,u,t)$

## Time variant vs time invariant
%%[[2024-10-04]] @ 09:21%%

### LTV
LTV = linear time variant

State Equation
$$\dot x = A(t) x(t) + B(x) u(t)$$
Output Equation
$$y=C(t)x(t) + D(t)u(t)$$

### LTI
LTI = linear time invariant

State Equation
$$\dot x = Ax(t) + Bu(t)$$
Output Equation
$$y=Cx(t) + Du(t)$$

## deriving a linear state equation

## Linearisation
%%[[2024-10-04]] @ 09:36%%

A system is nonlinear if the principle of superposition dose not apply.

### Segmentation
A nonlinear system can be liniearised by breaking it into linear sections each with their own linear equation.

when doing this it is important to provide the range within which the approximation is accurate.

An "equilibrium point" is chosen the centre of the locality where the approximation is accurate. 

### Taylor series
%%[[2024-10-04]] @ 09:52%%

We can use the lower order elements of a functions [[Taylor series]] to find a local linear approximation. 

#### Consider $f(x) = x^{2} \ @ x_{0}f(2)$

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [1,3,0,10]
disableZoom: false
grid: true
---
f(x) = x^2
```

## Practice question
%%[[2024-10-04]] @ 09:58%%

![[Lecture 3b - State space representation & Linearisation.pdf#page=24|3. State space representation & Linearisation, page 24]]

$e = r-y$
$u = e^{2}-16$  
$y = \frac{2}{2^{2}+15s}$

assumption:
1. Constant input
	$r(t)=1$

2. equilibrium
	$\dot x_{1} = \dot x_{2} = 0$

Entropy vs specific entropy
%%[[2024-10-04]] @ 16:36%%

S is entropy
s is specific entropy which is per kg

