
## Slides
[[Lecture 1 - Introduction to control systems.pdf]]

## Linear time invariant

A linear system can be produced by spiting superposition i.e. section where answers are indefinite, into subsystems and analyse both possibilities within a linear framework. 

Quite often a linear system can be found by integrating a non linear system. 

## Spring and damper

$a = \frac{F}{m}$
$v = \int a \ dt$ 
$p = \int' a \ dt$

$F = \sum F_{n}$

$F_{1} = f(t)$
$F_{2} = kd$
$F_{3} = kv$

therefore:

$$p(t) = \int'\frac{\sum\limits F_{n}}{m} dt$$



## Example 1 Double trolley

![[Lecture 2 - Physical Modelling.pdf#page=29|2. Physical Modelling, page 29]]

![[SSC - Week 1 - Trolly Problem - Mass1.excalidraw]]

$F_{m_{1}} = F_{k_{1}} + F_{b} + F_{k_{2}}$
$F_{m_{2}} = f(t) + F_{b} + F_{k_{2}}$

where:
$F_{k_{1}} = k_{1}x$
$F_{b} = b (x-y)$
$F_{k_{2}} = k_{2}(x-y)$

therefore for $y_{1}$ being displacement of block 1 and for $y_{2}$ being the displacement of block 2:
$$\dot y_{1} = x_{2}$$
$$\dot x_{2} = \begin{bmatrix}
\frac{F_{k_{1}} + F_{b} + F_{k_{2}}}{m_{1}} \\
\frac{F_{b} + F_{k_{2}}}{m_{2}}
\end{bmatrix} $$


$x = d$



