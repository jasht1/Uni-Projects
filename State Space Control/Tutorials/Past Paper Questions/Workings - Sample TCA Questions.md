
# Question 1

## (a) Answer TRUE or FALSE to the following statements:
[[EGR3032M Sample TCA Questions.pdf#page=1&selection=0,4,12,48|EGR3032M Sample TCA Questions, page 1]]
%%[[2024-12-23]] @ 18:06%%

### A state space model consists of transfer functions and frequency response graphs.
%%[[2024-12-23]] @ 18:06%%

FALSE, 

A [[State Space Representation|state space model]] must consist of an input equation and an output equation with suitable $A,B,C,D$ matrices. It doesn't necessarily include frequency response graphs.

### The general form of the LTI state equation is $y = \text{C}x + \text{D}u$
%%[[2024-12-23]] @ 18:10%%

False,

The equation given: 

$$y = \text{C}x + \text{D}u$$

is typically referred to as the "output equation", the state equation typically reefers to an equation that takes the form: 

$$\dot x = Ax+Bu$$

## How many state equations are needed to represent a ninth-order system?
%%[[2024-12-23]] @ 18:18%%

A system that can be defined by a single 9th order differential equation could be represented with 9 states in a 9 dimensional state vector, each with a state equation i.e. 9 rows in the $A$ & $B$  matrices.

## (c) Consider the system shown in [[EGR3032M Sample TCA Questions.pdf#page=1&selection=109,0,114,24|Figure 1]]. Derive a mathematical model in state space form, showing both state space and output equations. 
- Assume a linear spring, and a linear friction model $F_{f} = \mu \dot x$ , where $\mu$ is a friction coefficient.
- The displacement $x(t)$ is output.
%%[[2024-12-23]] @ 18:25%%

The system consist of a block sliding on a flat frictional surface connected horisontally to a rigid surface by a spring.

### Constituent Forces
%%[[2024-12-23]] @ 19:38%%

The spring would exert a force linearly proportional to the displacement of the block, as follows:

$$F_{s} = k_{s} x_{b}$$

Where:
$F_{s}$ : is the force exerted ($N$),
$k_{s}$ : is the spring constant of the spring $\frac{N}{m}$,
$x_{b}$ : is the displacement of the block.

Friction would exert a force in opposition to the motion of the block proportional to it's velocity, as follows:

$$F_{f} = -\mu \dot x_{b}$$

Where:
$F_{f}$ : is the frictional force ($N$),
$\mu$ : is a friction coefficient ($N \! \cdot \! m/s$),
$\dot x_{b}$ : is the velocity of the block.

### Equations of motion
%%[[2024-12-23]] @ 19:54%%

According to Newton's second law the acceleration of the bodies can be found by dividing the net force on the body by it's mass. $$a = \frac{F}{m}$$

Thus the acceleration of the block can be given by the following:
$$\ddot{\text{x}}_{b} = \frac{F_{s} + F_{f}}{m_{b}} = \frac{-\mu}{m_{b}} \dot x _{b} + \frac{k_{s}}{m_{b}} x_{b}$$

### State Equations
%%[[2024-12-23]] @ 19:44%%

The [[State Space Representation#State Vector|State Vector]] $\text{x}$ will take the form:

$$\Large \text{x} = 
\begin{bmatrix} 
\begin{align*}
	x_{1} &:= x_{\text{b}} \\
	x_{2} &:= \dot x_{\text{b}} \\
\end{align*}
\end{bmatrix}$$

And the input equation will take the form: 

$$\Large \dot{\text{x}} = Ax +Bu$$

Where:

- $\dot x$ is the [[derivative]] of the [[State Space Representation#State Vector|State Vector]]
- $x$ is the [[State Space Representation#State Vector|State Vector]]
- $u$ is the [[State Space Representation#Input Vector|input Vector]]
- $A$ is a matrix of first order coefficients that relate the [[State Space Representation#State Variable|State Variable]]s to their effect on the system dynamic.
- $B$ is a matrix of first order coefficients that relate the system inputs to their effect on the system dynamic.

and thus $A$ will be:
