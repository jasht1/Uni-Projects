
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

9

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
[5 marks]
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
[3 marks]
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


### (iii) Design a regulator with the following characteristic equation, designed to hold the ball at the reference height $h=0$: $$s^{2} + 150s + 9000 = 0$$

[10 marks]
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

6. The $s$ term coefficient can only be affected by $k_{2}$, thus the value that satisfies $\frac{150+880}{100} = k_{2}$ must be the identity. By this logic $k_{2}$ is substituted for $10.3$ and the $s$ term is cancelled:

$$\cancel{(-880 +100(10.3))s} + (-98000 -280k_{1} -98000(10.3)) = \cancel{150s} + 9000$$

7. Solving for $k1$ is then trivial:

%% Working 

$$-98000 -280k_{1} -98000(10.3) = 9000$$

$$-1107400 -280k_{1} = 9000$$

$$-280k_{1} = 9000+1107400$$

$$-280k_{1} = 1116400$$

$$k_{1} = \frac{1116400}{-280}$$

%%

$$k_{1} = \frac{9000+98000+98000(9.3)}{-280} = -3987.1$$

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
	-3987.1 & 10.3
\end{bmatrix}$$

## (b) Sketch the model as a Block Diagram, including the state feedback controller.
[7 marks]
%%[[2025-01-11]] @ 15:59%%

![[State Space System Diagram (A,B,C,K).excalidraw.svg]]

# Question 3

A System contains a ‘$v^{2}$’ damper, shown in [[EGR3032M Sample TCA Questions.pdf#page=3&selection=112,0,113,43|Figure 3]]. Inspecting the free body diagram and summing forces gives: 

$$M \ddot{x} = f(t) + f_{D}(t)$$

Where:
- $f_{D}(t) = - d \dot{x}^{2} (t)$ : damping force
- $d = 0.1$ Nm/s : damping coefficient
- $f(t) = 10 + \delta f(t)$ : applied force

> [!NOTE] Interpretation note
> The question posits the sum of the forces as:
> 
> $$M \ddot{x} + f_{D}(t) = f(t)$$
> 
> and the damper force as:
> 
> $$f_{D}(t) = d \dot{x}^{2} (t)$$
> 
> This is an interesting way of presenting the system, It is consistent but I would argue unclear. I would intuitively express the system as:
> 
> $$M \ddot{x} = f(t) + f_{D}(t)$$
> 
> To better indicate that $M \ddot{x}$ is the sum of forces, being a substitution of $F = ma$, and that the forces being summed are the applied force $f(t)$ and the damping force $f_{D}(t)$.
> with damper force as:
> 
> $$f_{D}(t) = - d \dot{x}^{2} (t)$$
> 
> To better indicate that damping force acts against the motion of the system. This is how I have expressed the question above.

## (a) Explain why this model is considered to be nonlinear.
[3 marks]
%%[[2025-01-11]] @ 16:08%%

For a system to be considered linear all the equations that govern it's behaviour may only sum system states. States can be multiplied by constants but products or indices of system states make a system non linear.
In this case the equation that governs the behaviour of the damper $fD(t) = d \dot{x}^{2} (t)$ is proportional to velocity squared. Raising a system state, velocity $v$, to a power makes this a non linear function. Thus the system as a whole is non-linear by transitive property. 

## (b) Linearise the model about the equilibrium point. 
[10 marks] 

The non linear damper force equation:

$$f_{D}(t) = - d \dot{x}^{2} (t)$$

can be expressed in terms of it's deviation $\delta$ from equilibrium $o$:

$$f_{D}(t) = - d (\dot{x}_{o} + \delta \dot{x})^{2}$$

and then linearised using a [[Taylor series]]:

$$\large \sum _{n=0}^{\infty }{\frac {f^{(n)}(0)}{n!}}x^{n}$$

In this case:

$$f_{D}(t) = - d \dot{x}^{2}_{o} - 2d \dot{x}_{o}\delta \dot{x} -d\delta \dot{x}^{2}$$

Given that $\delta \dot{x}^{2}$ is non linear this term will be dropped, leaving:

$$f_{D}(t) \approx - d \dot{x}^{2}_{o} - 2d \dot{x}_{o}\delta \dot{x} = -d\dot{x}_{o}(\dot{x}_{o} + \delta \dot{x})$$

At equilibrium $F = 0$ and by newtons second law $F=ma$ we may infer $M\ddot{x} = 0$. Thus at equilibrium the following condition must be satisfied:

$$d \dot{x}^{2}_{o} = f_{o}$$

When the system as a whole is represented based on it's deviation from equilibrium it is:

$$M \ddot{x} = \delta f + f_{o} - d \dot{x}^{2}_{o} - 2d \dot{x}_{o}\delta \dot{x}$$

where $f_{o}$ can be substituted for $d \dot{x}^{2}_{o}$ which cancels out:

$$M \ddot{x} = \delta f + \cancel{d \dot{x}^{2}_{o}} - \cancel{d \dot{x}^{2}_{o}} - 2d \dot{x}_{o}\delta \dot{x}$$

Giving a linear equation for approximating the motion about the equilibrium:

$$\large M \ddot{x} \approx \delta f - 2d \dot{x}_{o}\delta \dot{x}$$

## (c) Write the linearised model in LTI state space format 
[6 marks]

The [[State Space Representation#State Vector|State Vector]] $x$ will take the form:

$$\Large \text{x} = 
\begin{bmatrix} 
\begin{align*}
	x_{1} &:= \dot{x} \\
	x_{2} &:= \delta \dot x \\
\end{align*}
\end{bmatrix}$$

And the [[State Space Representation#Input Equation|input equation]] will take the form: 

$$\Large \dot{\text{x}} = A\text{x} +Bu$$

Where:

- $\text{x}$ is the [[State Space Representation#State Vector|State Vector]] defined above,
- $\dot{\text{x}}$ is the [[derivative]] of the [[State Space Representation#State Vector|State Vector]],
- $u$ is the [[State Space Representation#Input Vector|input]] in this case $\delta f$,
- $A$ & $B$ are the [[State Space Representation#State Equations|input matrices]]:
	- $A$ is a matrix of first order coefficients that relate the [[State Space Representation#State Variable|State Variable]]s to their effect on the system dynamic.
	- $B$ is a matrix of first order coefficients that relate the system inputs to their effect on the system dynamic.

$A$ & $B$ will be:

$$\Large
A = \begin{bmatrix}
	0 & 1 \\ 
	0 & \frac{- 2d \dot{x}_{o}}{M}
\end{bmatrix}
\qquad
B = \begin{bmatrix}
	0 \\ \frac{1}{M} \\
\end{bmatrix}$$

The [[State Space Representation#Output Equation|output equation]] gives the output of the system at time $t$.

$$\Large y = C\text{x} + Du$$

Where:
- $y$ is the [[State Space Representation#Output Vector|output vector]],
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


### (i) Can this linearised model be used to assess the system when relatively small forces are applied, causing small deflections of $\pm 5$ mm from the equilibrium point? Explain your answer. 
[3 marks] 

The inaccuracy of the approximation is due to the missing $\delta \dot{x}^{2}$ term and thus graphing this will give the error function:

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-0.1,0.1,-0.1,0.1]
disableZoom: false
grid: true
---
e(x) = pow(x,2)
```

at $\pm 5$ mm this represents a difference in estimated force from the damper of $\frac{1}{40000M} \ N$ thus an inacruracy in the acceleration predicted of $\frac{1}{40000M^{2}} \ m/s^{2}$. The position error will of course be cumulative so the further into the future it will be exponentially less accurate. Being that it is inversely proportional to mass, if the mass is particularly small then the inaccuracy will be larger.

It mostly depends on the level of accuracy needed, it is difficult to give definitive advice without further context. 

The travel distance of the damper is not as important, the model would perform similarly with one full oscillation to many shorter ones assuming a similar time frame and acceleration.
However it may be better suited to small deflections in the order of $\pm 5$ mm as these will likely be associated with lower accelerations closer to the equilibrium point.

### (ii) Can this linearised model be used to assess the system when a large impact is applied, causing the damper to fully compress and extend? Explain your answer. 
[3 marks]

The model is **not** suited to modelling larger impacts, the inaccuracy increases exponentially with velocity and a larger impact implies a high velocity. 

Again the travel distance of the damper is not as important, the model would perform similarly with one full oscillation to many shorter ones assuming a similar time frame and acceleration.

And again It mostly depends on the level of accuracy needed, it is difficult to give definitive advice without further context but it's unlikely this model would be sufficient.