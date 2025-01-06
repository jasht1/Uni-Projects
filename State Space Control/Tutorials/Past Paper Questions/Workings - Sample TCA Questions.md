
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

Aside from the time varying input force $f(t)$, the following forces act on the system;

The spring would exert a force inversely proportional to the displacement of the block, as follows:

$$F_{s} = -k_{s} x_{b}$$

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

According to Newton's second law the acceleration of the bodies can be found by dividing the net force on the body by it's mass. 

$$a = \frac{F}{m}$$

Thus the acceleration of the block can be given by the following:

$$\ddot{\text{x}}_{b} = \frac{F_{s} + F_{f} + f(t)}{m_{b}} = \frac{-\mu}{m_{b}} \dot x _{b} + \frac{-k_{s}}{m_{b}} x_{b} + \frac{f(t)}{m_{b}}$$

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

And the [[State Space Representation#Input Equation|input equation]] will take the form: 

$$\Large \dot{\text{x}} = Ax +Bu$$

Where:

- $\dot x$ is the [[derivative]] of the [[State Space Representation#State Vector|State Vector]],
- $x$ is the [[State Space Representation#State Vector|State Vector]],
- $u$ is the [[State Space Representation#Input Vector|input Vector]],
- $A$ & $B$ are the [[State Space Representation#State Equations|input matrices]]:
	- $A$ is a matrix of first order coefficients that relate the [[State Space Representation#State Variable|State Variable]]s to their effect on the system dynamic.
	- $B$ is a matrix of first order coefficients that relate the system inputs to their effect on the system dynamic.

and thus $A$ & $B$ will be:

$$\Large
A = \begin{bmatrix}
	0 & 1 \\ 
	\frac{-k_{s}}{m_{b}} & \frac{-\mu}{m_{b}}
\end{bmatrix}
\qquad
B = \begin{bmatrix}
	0 \\ \frac{1}{m_{\text{b}}} \\
\end{bmatrix}$$


The [[State Space Representation#Output Equation|output equation]] gives the output of the system at time $t$.

$$\Large y = Cx + Du$$

Where:
- $y(t)$ is the [[State Space Representation#Output Vector|output vector]],
- $x(t)$ is the [[State Space Representation#State Vector|state vector]],
- $u(t)$ is the [[State Space Representation#Input Vector|input vector]],
- $C$ & $D$ are the [[State Space Representation#Output Equations|output matrices]]:
	- $C$ is a matrix of first order coefficients that relate the current system state to their impact on the system outputs.
	- $D$ is a matrix of firs order coefficients that relate the inputs to the system to their effect on the system outputs.

and assuming the state variable of interest is the block's position $x_{b}$ then the output matrices $C$ & $D$ will be:

$$\Large
C = \begin{bmatrix}
	1 & 0 \\ 
\end{bmatrix}
\qquad
D = \begin{bmatrix}
	0
\end{bmatrix}$$

## Assume that friction coefficient $\mu = 0.1 \ N \! \cdot \! m/s$ and spring stiffness $k_{s} = 200 \ N/m$. Calculate the poles of the system and plot them on the s-plane. Is the system stable?
%%[[2024-12-24]] @ 01:05%%

```matlab
>> k_s = 200;
>> mu = 0.1;

>> A = [0, 1;-k_s/m_b, -mu/m_b];
>> B = [0; 1/m_b];
>> C = [1, 0];
>> D = 0;

>> sys = ss(A,B,C,D)

sys =

  A =
         x1    x2
   x1     0     1
   x2  -200  -0.1

  B =
       u1
   x1   0
   x2   1

  C =
       x1  x2
   y1   1   0

  D =
       u1
   y1   0

Continuous-time state-space model.

>> pole(sys)

ans =

  -0.0500 +14.1420i
  -0.0500 -14.1420i

>> pzplot(sys)

*see "Pole Zero Plot" below*
```

> [!FIGURE] Pole Zero Plot ^q1d-pzplot
> ![[Q1d_pzplot.svg]]

The system **is stable** as the real component of the poles lay on the left of the y axis indicating a negative feedback that allows the system to settle to a steady state.

# Question 2

## (a) You are given the following model for a Magnetically Suspended Ball (shown in [[EGR3032M Sample TCA Questions.pdf#page=2&selection=12,0,13,42|Figure 2]]).
%%[[2024-12-24]] @ 14:45%%

Where the state vector $\text x$ is comprised of:

$$\Large \text{x} = 
\begin{bmatrix} 

	x_{1} := h \\
	x_{2} := i \\

\end{bmatrix} \quad
\begin{matrix} \begin{align}
& \leftarrow \text{displacment (m)}\\ 
& \leftarrow \text{current (A)}
\end{align}\end{matrix}$$

And the input vector $u$ is the input voltage ($V$):

$$\Large u = \begin{bmatrix} v(t) \end{bmatrix}$$

The $A$, $B$, $C$ & $D$ matrices are:

$$\Large
A = \begin{bmatrix}
	980 & -2.8 \\ 
	0 & -100
\end{bmatrix}
\qquad
B = \begin{bmatrix}
	0 \\ 100 \\
\end{bmatrix}
\qquad
C = \begin{bmatrix}
	1  & 0 \\ 
\end{bmatrix}
\qquad
D = \begin{bmatrix}
	0 \\
\end{bmatrix}$$

### (i) Check the open-loop stability of the system
%%[[2024-12-24]] @ 14:54%%

The system stability can be judged by the poles of the system, the poles are found as the [[eigenvalue]]s of the $A$ matrix given by the [[characteristic equation]]:

$$\Large \text {det} (A-\lambda I)=0$$

Where:
- $\text {det}$ : refers to the [[Determinant]], which gives the factor by which area is scaled when a [[linear transformation]] is applied.
  The determinant of a 2D transformation like this one can be found as:

$$\text{det} \left( \begin{bmatrix} 
	a & b \\
	c &d  \\
\end{bmatrix}\right)
= ad - bc$$

- $A$ : [[linear transformation|transformation matrix]]
- $\lambda$ : [[Eigenvalues & Eigenvectors#Eigenvalues|Eigenvalue]]
- $I$ : is the Identity matrix, a matrix of width and height = to number of dimensions and with 0s in all spots but the diagonal which contain 1s like so:

$$\begin{bmatrix} 
	1 &0 \\ 
	0 &1 \\ 
\end{bmatrix},
\begin{bmatrix} 
	1 &0 &0 \\ 
	0 &1 &0 \\ 
	0 &0 &1 \\ 
\end{bmatrix}, 
\text{ ect } \dots$$

So in this case, the steps are as follows:

1. Factor in the variables and simplify

$$\text{det} \left(
\begin{bmatrix}
	980 & -2.8 \\ 
	0 & -100 \\ 
\end{bmatrix}
-\begin{bmatrix} 
	\lambda & 0 \\
	0 & \lambda \\ 
\end{bmatrix} 
\right)=0$$

$$\text {det} \left(
\begin{bmatrix}
	980 - \lambda & -2.8 \\ 
	0 & -100 - \lambda  \\
\end{bmatrix}\right) = 0$$

2. Apply the determinant and simplify

$$(980 - \lambda)(-100 - \lambda) - (-2.8)(0) = 0$$

$$(980 - \lambda)(100 + \lambda)= 0$$

3. Identify the values of $\lambda$ that solve for $0$

$$\Large \lambda = \quad 980, \quad \text{or} \quad -100$$

4. Identify any positive real solutions

$$\text {In this case 980 is positive and real indicating an unstable system.}$$

### (ii) Show whether the system is controllable.
%%[[2024-12-31]] @ 02:35%%

For a system to be 'controllable' any real output of the system must be reachable from any other by a finite set of real inputs in a finite time. It must be proved that the available inputs can influence every state in the system uniquely, as if this is the case then there must exist some linear combination of inputs that can affect every change to the system. This can be judged by it's controllability matrix $C_{M}$:

$$\Large C_{M} := \begin{bmatrix} B & AB & A^{2}B & \cdots & A^{n-1}B \end{bmatrix}$$

The controllability matrix $C_{M}$ indicates how inputs propagate through the system accounting for higher order dynamics. Each term represents the impact of a further time step, and we need only consider as many time steps as there are states to be exhaustive.

The [[rank]] of a matrix indicates number of linearly independent rows & columns, thus: The system can be said to be completely controllable if the controllability matrix $C_{M}$ is of the same [[rank]] $n$ as there are states $\text{x}_{n}$ in the state space $\text{x}$.

In this case the the system $(A,B)$ is 2nd order, i.e. 2 states in the state space, so $C_{M}$ will take the form: $C_{M} := \begin{bmatrix} B & AB \end{bmatrix}$

Factoring in the values for $A$ & $B$:

$$C_{M} := \begin{bmatrix}
	\begin{bmatrix}
		0 \\ 100 \\
	\end{bmatrix} 
	& 
	\begin{bmatrix}
		980 & -2.8 \\ 
		0 & -100
	\end{bmatrix}
	\begin{bmatrix}
		0 \\ 100 \\
	\end{bmatrix}
\end{bmatrix}$$

And simplifying:

$$C_{M} := \begin{bmatrix}
	\begin{bmatrix}
		0 \\ 100 \\
	\end{bmatrix} 
	& 
	\begin{bmatrix}
		980 \times 0 & -2.8 \times 100 \\ 
		0 \times 0 & -100 \times 100
	\end{bmatrix}
\end{bmatrix}$$

Gives the controllability matrix $C_{M}$ as:

$$C_{M} := \begin{bmatrix}
		0 & -280 \\ 
		100 & -10000 \\ 
\end{bmatrix}$$

As the system only has a single input the resulting $C_{M}$ was square so the [[rank]] of $C_{M}$ can be determined by taking the [[Determinant]] of controllability matrix $det(C_{M})$:

$$det \left(\begin{bmatrix}
		0 & -280 \\ 
		100 & -10000 \\ 
\end{bmatrix}\right) = (0 \times -10000) - (-280 \times 100) = 28000$$

As $det(C_{M}) \neq 0$ $C_{M}$ must be full rank thus the system is controllable.


### (iii) Design a regulator with the following characteristic equation, designed to hold the ball at the reference height h=0: $$s^{2} + 150s + 9000 = 0$$
%%[[2025-01-05]] @ 14:00%%

[[Nise's Control Systems Engineering - Norman S_ Nise.pdf#page=671&selection=351,0,353,6|Nise's Control Systems Engineering - 12.2 Controller Design, page 671]]

The [[characteristic equation]] indicates the location of the system poles as found in [[#(i) Check the open-loop stability of the system]] along with features of the systems behaviour. Through the use of a regulator the [[characteristic equation]] can be moved to achieve different system behaviours. The regulator will consist of feedback $-K$ applied to the [[State Space Representation#State Vector|state vector]] $\text{x}$ and applied as the [[State Space Representation#Input Vector|input vector]] $u$.

$$\dot{\text{x}} = A \text{x} +Bu \quad \to \quad  \dot{\text{x}} = A \text{x} +B (-K \text{x})$$

Which can be rearranged and stated as:

$$\Large \dot{\text{x}} = (A - K B)\text{x}$$

This is of course based on the assumption that all the [[State Space Representation#State Variable|state variables]] are visible to the controller, in practice sensors for ball height and current would be necessary.

%%[[2025-01-05]] @ 17:31%%

To find the correct values for gain $K$ to move the [[characteristic equation]] to  $s^{2} + 150s + 9000 = 0$ the following equation must be satisfied:

$$\Large \text {det} (s I -(A - K B)) = s^{2} + 150s + 9000 = 0$$

As:
- $\text {det} (s I -(A - K B))$ : gives the [[characteristic equation]] of the system.
- $s^{2} + 150s + 9000$ : is the target [[characteristic equation]].

Both must be equal to 0 and therefore to each other.

1. Substituting in the values for $A$ & $B$ in matrix from the left hand side becomes:

$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-\left(
		\begin{bmatrix}
			980 & -2.8 \\ 
			0 & -100 \\ 
		\end{bmatrix}
		-
		\begin{bmatrix}
			k_{1} & k_{2} \\ 
		\end{bmatrix}
		\begin{bmatrix}
			0 \\
			-100 \\
		\end{bmatrix} 
	\right)
\right)
$$

2. This simplifies to:

%% Workings

$$\text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-\left(
		\begin{bmatrix}
			980 & -2.8 \\ 
			0 & -100 \\ 
		\end{bmatrix}
		-
		\begin{bmatrix}
			0 & 0 \\
			-100k_{1} & -100k_{2} \\
		\end{bmatrix} 
	\right)
\right)
$$

$$\text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-
	\begin{bmatrix}
		980 & -2.8 \\ 
		-100k_{1} & -100-100k_{2} \\ 
	\end{bmatrix}
\right)
$$

$$\text {det} \left(
	\begin{bmatrix} 
		s - 980 & 0+2.8 \\ 
		0+100k_{1} & s+100+100k_{2} \\ 
	\end{bmatrix}
\right)
$$

%%

$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s - 980 & 2.8 \\ 
		100k_{1} & s+100+100k_{2} \\ 
	\end{bmatrix}
\right)$$

3. Making the determinant:

$$\text{LHS} = (s-980)(s+100+100k_{2}) - (2.8)(100k_{1})$$

4. Expanding the brackets and substituting back into the equation:

%% Workings

$$(s-980)(s+100+100k_{2}) - (2.8)(100k_{1})$$

$$s^{2} +100s +100k_{2}s -980s -98000k_{2} -98000 -280k_{1}$$

$$s^{2} +100k_{2}s -880s -280k_{1} -98000k_{2} -98000$$

$$(-280)k_{1} +(100s -98000)k_{2} +s^{2} -880s -98000$$

$$s^{2} +(-880 +100k_{2})s + (-98000 -280k_{1} -98000k_{2})$$

%%

$$s^{2} +(-880 +100k_{2})s + (-98000 -280k_{1} -98000k_{2}) = s^{2} + 150s + 9000$$

5. The $s^{2}$ terms can be cancelled out:

$$\cancel{s^{2}} +(-880 +100k_{2})s + (-98000 -280k_{1} -98000k_{2}) = \cancel{s^{2}} + 150s + 9000$$

6. The $s$ term coefficient can only be affected by $k_{2}$, thus the value that satisfies $\frac{-880-150}{100} = k_{2}$ must be the identity. By this logic $k_{2}$ is substituted for $9.3$ and the $s$ term is cancelled:

$$\cancel{(-880 +100(9.3))s} + (-98000 -280k_{1} -98000(9.3)) = \cancel{150s} + 9000$$

7. Solving for $k1$ is then trivial:

%% Working 

$$-98000 -280k_{1} -98000(9.3) = 9000$$

$$-1009400 -280k_{1} = 9000$$

$$-280k_{1} = 9000+1009400$$

$$-280k_{1} = 1018400$$

$$k_{1} = \frac{1018400}{-280}$$

%%

$$\frac{9000+98000+98000(9.3)}{-280} = -3637.142857 = k_{1}$$

8. The system with the regulator $K$ is given by:

$$\Large \dot{\text{x}} = (A - K B)\text{x}$$

Where:

$$
A = \begin{bmatrix}
	980 & -2.8 \\ 
	0 & -100
\end{bmatrix}
\qquad
B = \begin{bmatrix}
	0 \\ 100 \\
\end{bmatrix}
\qquad
K = \Large\begin{bmatrix}
	9.3 & \frac{-25460}{7}
\end{bmatrix}$$

## (b) Sketch the model as a Block Diagram, including the state feedback controller.
