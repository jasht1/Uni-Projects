
#### State Space Representation
%%[[2024-10-21]] @ 21:18%%

A [[#State Space Representation]] is a standardised means of modelling complex MIMO dynamic systems using only linear equations in the time domain.
Below are explanations of all of the relevant terms and concepts referred to in this report.

##### State Space
%%[[2024-10-21]] @ 17:52%%

The [[#State Space]] is an $n$ dimensional manifold with a dimension $n$ for every [[#State Variable]] needed to describe the system. 

##### State Variable
%%[[2024-10-21]] @ 17:58%%

[[#State Variable]]s $x_{n}$ are any measures of the systems internal dynamics necessary to determine the system state by first order transfer functions. 
%% They are the means by which energy is stored by the system. It is good practice to use the minimum number of of state variables. https://www.youtube.com/watch?v=RdAZNUfWDpQ %%
##### State Vector
%%[[2024-10-21]] @ 17:49%%

The [[#State Vector]] $x$ is an $n$ dimensional vector that represents the overall state of the system as a point in the [[#State Space]] based on the values of all of the [[#State Variable]]s. 

##### Input Vector
%%[[2024-10-21]] @ 18:05%%

The [[#Input Vector]] $u$ is a vector that represents the external inputs affecting the system. 

##### State Equations
%%[[2024-10-21]] @ 21:45%%

The sets of linear equations in matrix form $A$ & $B$ that transform the [[#State Vector]] $x$ and [[#Input Vector]] $u$ respectively to their resulting effect on the system dynamic $\dot x$. 

##### Output Vector
%%[[2024-10-21]] @ 22:00%%

The [[#Output Vector]] $y$ is an $n$ dimensional vector that represents the outputs of interest of the system. 

##### Output Equations
%%[[2024-10-21]] @ 22:02%%

The sets of linear equations in matrix form $C$ & $D$ that transform the [[#State Vector]] $x$ and [[#Input Vector]] $u$ respectively to their resulting effect on the system outputs $y$. 

##### Input Equation
%%[[2024-10-21]] @ 17:48%%

The [[#Input Equation]] gives the change in the system $\dot x$ at a given time $t$.

$$\Large \dot x(t) = Ax(t) +Bu(t)$$
Where:
- $\dot x(t)$ is the [[derivative]] of the [[#State Vector]] at time $t$
- $x(t)$ is the [[#State Vector]] at time $t$
- $u(t)$ is the [[#Input Vector]] at time $t$
- $A$ & $B$ are the [[#State Equations]]:
	- $A$ is a matrix of first order coefficients that relate the [[#State Variable]]s to their effect on the system dynamic.
	- $B$ is a matrix of first order coefficients that relate the system inputs to their effect on the system dynamic.

##### Output Equation
%%[[2024-10-21]] @ 18:01%%

The [[#Output Equation]] gives the output of the system at time $t$.

$$\Large y(t) = Cx(t) + Du(t)$$
Where:
- $y(t)$ is the [[#Output Vector]] at time $t$
- $x(t)$ is the [[#State Vector]] at time $t$
- $u(t)$ is the [[#Input Vector]] at time $t$
- $C$ & $D$ are the [[#Output Equations]]:
	- $C$ is a matrix of first order coefficients that relate the current system state to their impact on the system outputs.
	- $D$ is a matrix of firs order coefficients that relate the inputs to the system to their effect on the system outputs.
