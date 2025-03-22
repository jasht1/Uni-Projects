
# Question 1
## (a) In each case determine the state space matrices A, B, C, D for the LTI system model
### (i) The SISO system with transfer function shown (use any state variables but clearly show they are chosen)

$$G(s) = \frac{1}{s^{3}+3s^{2} + s}$$

Solving such that [[characteristic equation]] matched denominator $s^3 + 3s^2 + s + 1$.

$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & -3 & 0 \end{bmatrix}$$

$$B = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

$$C = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix}$$

$$D = 0$$

State variables are:
$$\text{x} = 
\begin{bmatrix} 
\begin{align*}
	x_{1} &:= y \\
	x_{2} &:= \dot{y} \\
	x_{3} &:= \ddot{y} \\
\end{align*}
\end{bmatrix}$$

With output being $x_{1}$

### (ii) A two-input system has differential equations

$$\dot{\text{x}} = \begin{bmatrix} 2 & 1 \\ 0 & 2\end{bmatrix}\text{x} + \begin{bmatrix}1 & 2 \\ 0 & 1\end{bmatrix} \begin{bmatrix}u \\ v\end{bmatrix}$$

$$y = x_{1}+ x_{2}$$

$u$ and $v$ are inputs such that:
$$u+v = 0$$

This can be simplified into a single input by solving for $v$ using $u$:

$$v = -u$$

Reducing $B$ to

$$\begin{bmatrix}1 & 2 \\ 0 & 1\end{bmatrix} \begin{bmatrix}u \\ (-u)\end{bmatrix} = \begin{bmatrix} u-2u \\ -u\end{bmatrix} = \begin{bmatrix} -1 \\ -1 \end{bmatrix}u$$

Thus the system:

$$A = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$
$$B = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$
$$C = \begin{bmatrix} 1 & 1 \end{bmatrix}$$
$$D = 0$$

With state equation:

$$\dot{\text{x}} = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}\text{x} + \begin{bmatrix} -1 \\ -1 \end{bmatrix}u$$

*okay these two where way too easy for 8 marks each*

## b) For the system presented in part (a)(i), decide whether it is 
### (i) controllable 
[2 marks]

`A = [0 , 1 , 0 ; 0 , 0 , 1 ; -1 , -3 , 0]`
`B = [0;0;1]`

```matlab
>> A = [0 , 1 , 0 ; 0 , 0 , 1 ; -1 , -3 , 0];
>> B = [0;0;1];
>> C_m = ctrb(A,B)

C_m =

     0     0     1
     0     1     0
     1     0    -3

>> length(A)-rank(C_m)

ans =

     0
```

The system is controllable

*doesn't say to do it by hand and it's only worth 2 marks*

### (ii) observable 
[2 marks]

```matlab
>> A = [0 , 1 , 0 ; 0 , 0 , 1 ; -1 , -3 , 0];
>> C = [1,0,0];
>> O_m = obsv(A,C)

O_m =

     1     0     0
     0     1     0
     0     0     1

>> length(A)-rank(O_m)

ans =

     0
```

The system is Observable

*doesn't say to do it by hand and it's only worth 2 marks*

## (c) Briefly explain the meaning of controllability. What are the implications for the control engineer if a system is not fully controllable. 
[5 marks]

For a system to be controllable any real output of the system must be reachable from any other by a finite set of real inputs in a finite time.

A system $(A, B)$ can be said to be completely controllable if the controllability matrix $C_{M}$ is of the same [[rank]] $n$ as there are states $\text{x}_{n}$ in the state space $\text{x}$.

$$\Large C_{M} := \begin{bmatrix} B & AB & A^{2}B & \cdots & A^{n-1}B \end{bmatrix}$$

If a system is not controllable then an engineer may not be able to effectively influence all the states of the system. It may be the case that the system cannot be relied upon as certain perturbations to the system sate or specific initial conditions could be catastrophic.  

# Question 2

## (a) Determine the state-space equations of the system

We have been asked to use $\theta$ and $\dot{\theta}$ as the state variables (*this will be important*).

$$\Large \text{x} = 
\begin{bmatrix} 
\begin{align*}
	x_{1} &:= \theta \\
	x_{2} &:= \dot{\theta} \\
\end{align*}
\end{bmatrix}$$

The motor equation is:
$$\tau \dot {\omega} + \omega = K_{0} v_{a} + K_{1}T_{l}$$

angular velocity is equivalent to change in rotation
$$\omega = \dot{\theta}$$

and displacement is equivalent to the product of ration & radius
$$x = r \theta$$

where the Torque load due to the spring is product of displacement, spring constant and radius 

$$T_{l}^{\text{spring}} = rkx + m\ddot{x} = r^{2}k\theta$$

The torque load from inertia is a product of angular acceleration radius and mass:

$$T_{l}^{\text{inertia}} = mr^{2}\ddot{\theta}$$

Thus the torque load is:

$$T_{l} = r^{2} k \theta + m r^{2} \ddot{\theta}$$

Substituting this back into the motor equation:

$$\tau \ddot{\theta} + \dot{\theta} = K_{0} v_{a} + K_{1}(r^{2} k \theta + m r^{2} \ddot{\theta})$$

Expanding the brackets
$$\tau \ddot{\theta} + \dot{\theta} = K_{0} v_{a} + K_{1}r^{2} k \theta + K_{1} m r^{2} \ddot{\theta}$$

rearanging for $\ddot{\theta}$:

$$(\tau + K_{1} m r^{2}) \ddot{\theta} + \dot{\theta} = K_{0} v_{a} + K_{1}r^{2} k \theta $$

$$\ddot{\theta} = -\frac{1}{\tau + K_1 m r^2} \dot{\theta} - \frac{K_1 r^2 k}{\tau + K_1 m r^2} \theta + \frac{K_0}{\tau + K_1 m r^2} v_a$$

%%
and the torque load is a variable in the equation for angular acceleration making this self referential. Thus we will assume it is negligible. 

Isolating variables for 
1. change in angle $\dot{\theta}$ (angular velocity $\omega$) 

$$\dot{\theta} = K_{0} v_{a} + K_{1}r^{2}k\theta - \tau \ddot{\theta}$$

2. and change in angular velocity $\ddot{\theta}$ (angular acceleration $\dot{\omega}$):

$$\ddot{\theta} = \frac{K_{0} v_{a} + K_{1}r^{2}k\theta - \dot{\theta}}{\tau}$$

Substituting this back into the change in angle $\dot{\theta}$:

$$\dot{\theta} = \cancel{K_{0} v_{a} + K_{1}r^{2}k\theta} - \cancel{\tau} \frac{\cancel{K_{0} v_{a} + K_{1}r^{2}k\theta} - \dot{\theta}}{\cancel{\tau}} = \dot{\theta}$$

we see the whole thing cancels out as angular acceleration is a product of angular velocity anyway.
%%


This makes the $A$ & $B$ matricies:

$$A = 
\begin{bmatrix}
0 & 1 \\
\frac{K_1 r^2 k}{\tau + K_1 m r^2} & \frac{1}{\tau + K_1 m r^2}
\end{bmatrix}$$

$$B  = 
\begin{bmatrix}
	0 \\ 
	\frac{K_0}{\tau + K_1 m r^2}
\end{bmatrix}$$

and thus the state equation:

$$\dot{\text{x}} = 
\begin{bmatrix} 
	K_{1}r^{2}k & -\tau \\
	\frac{K_{1}r^{2}k}{\tau} & \frac{1}{\tau} 
\end{bmatrix}
\text{x} 
+ 
B  = 
\begin{bmatrix}
	0 \\ 
	\frac{K_0}{\tau + K_1 m r^2}
\end{bmatrix}
u$$

With the $C$ & $D$ matricies:

$$C = \begin{bmatrix} r \\ 0\end{bmatrix}$$
$$D = 0$$

and thus the output equation:

$$y = \begin{bmatrix}r \\ 0\end{bmatrix} \text{x}$$

## (b) Use the Ackerman formula to determine the feedback gains required to place both closed-loop poles at $s = -2 \pm 4j$.


> [!NOTE] *Based on my work from [Past Paper Questions](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/Tutorials/Past%20Paper%20Questions/Workings%20-%20Sample%20TCA%20Questions.md)*

The [[characteristic equation]] indicates the location of the system poles along with features of the systems behaviour. Currently the poles are at $1$ & $3$ as found in [[#(a) Determine whether the system is stable.]] Poles located at $s = -2 \pm 4j$ imply a [[characteristic equation]] of:

$$(s - (-2 + j))(s - (-2 - 4j)) = s^2 + 4s + 20$$

Through the use of a regulator the [[characteristic equation]] can be moved to achieve different system behaviours. The regulator will consist of feedback $-K$ applied to the [[State Space Representation#State Vector|state vector]] $\text{x}$ and applied as the [[State Space Representation#Input Vector|input vector]] $u$.

$$\dot{\text{x}} = A \text{x} +Bu \quad \to \quad  \dot{\text{x}} = A \text{x} +B (-K \text{x})$$

Which can be rearranged and stated as:

$$\Large \dot{\text{x}} = (A - K B)\text{x}$$

This is of course based on the assumption that all the [[State Space Representation#State Variable|state variables]] are visible to the controller.

To find the correct values for gain $K$ to move the [[characteristic equation]] to $s^2 + 4s + 5 = 0$ the following equation must be satisfied:

$$\Large \text {det} (s I -(A - K B)) = s^2 + 4s + 20 = 0$$

As:
- $\text {det} (s I -(A - K B))$ : gives the [[characteristic equation]] of the system.
- $s^2 + 4s + 20$ : is the target [[characteristic equation]].

Substituting in the values for $A$ & $B$ in matrix from the left hand side ($\text{LHS}$) becomes:


$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-\left(
		\begin{bmatrix}
			0 & 1 \\
			\frac{K_1 r^2 k}{\tau + K_1 m r^2} & \frac{1}{\tau + K_1 m r^2}
		\end{bmatrix}
		-
		\begin{bmatrix} k_{1} & k_{2} \end{bmatrix}
		\begin{bmatrix}
			0 \\ 
			\frac{K_0}{\tau + K_1 m r^2}
		\end{bmatrix}
	\right)
\right)$$

*Absolutely not doing this bit by hand gfu*

```matlab
>> m = 0.4;
>> tau=0.15;
>> k_0=1.6;
>> k_1=2.3;
>> r=0.15;
>> k=200;
>> A = [0,1;(k_1*r^2*k)/(tau+k_1*m*r^2) , 1/(tau+k_1*m*r^2)]

A =

         0    1.0000
   60.6327    5.8582

>> B = [0 ; k_0/(tau+k_1*m*r^2)]

B =

         0
    9.3732

>> det([s,0;0,s]-(A-[K_1,K_2]*B))

ans =

(1523312000*K_2)/2913849 - (10000*s)/1707 + (32000*K_2*s)/1707 + s^2 - 34500/569
```

$$\text{LHS} = s^{2} + \frac{1523312000k_2}{2913849} - \frac{10000s}{1707} + \frac{32000k_{2}s}{1707} - \frac{34500}{569}$$

Substituting this back in:

$$\cancel{s^{2}} + \frac{1523312000}{2913849}k_2 - \frac{10000}{1707}s + \frac{32000}{1707}k_{2}s - \frac{34500}{569} = \cancel{s^2} + 4s + 20$$

and solving for $k_2$ by focusing on factors of $s$:

$$\frac{10000}{1707}s + \frac{32000}{1707}k_{2}s=4s$$

$$\frac{32000}{1707}k_{2} \cancel{s}=4\cancel{s}-\frac{10000}{1707}\cancel{s}$$

$$k_{2} \cancel{s}=(4-\frac{10000}{1707})\frac{1707}{32000} = \frac{-793}{8000}$$

Thus the gain matrix is:

$$K = \begin{bmatrix}\frac{-793}{8000}\end{bmatrix}$$

# Question 4

A nonlinear system has the following differential equations:

$$\dot{\text{x}}_{1} = - \text{x}_{1} + 2{\text{x}_{2}}^{2}$$

$$\dot{\text{x}}_{2} = 1 - \text{x}_{1} + u\text{x}_{2}$$

## (a) Show that the open-loop system ($u = 0$) has two possible equilibrium states. 
[5 marks]

at equilibrium $\dot{\text{x}}_{1}$ & $\dot{\text{x}}_{2}$ will be 0:

$$\dot{\text{x}}_{1} = - \text{x}_{1} + 2{\text{x}_{2}}^{2} = 0$$

$$\dot{\text{x}}_{2} = 1 - \text{x}_{1} + u\text{x}_{2} = 0$$

In addition as $u$ is 0

$$\dot{\text{x}}_{2} = 1 - \text{x}_{1} + (0)\text{x}_{2} = 1 - \text{x}_{1}$$

Thus by substitution

$$0 = 1 - \text{x}_{1} \to \text{x}_{1} = 1$$

Therefore:

$$0 = - (1) + 2{\text{x}_{2}}^{2}$$

$$\text{x}_{2}= \pm \sqrt{\frac{1}{2}} $$

This shows that there are two equilibrium conditions as:

$$(\text{x}_{1},\text{x}_{2})= \left( 1, + \sqrt{\frac{1}{2}}\right) \text{ or } \left( 1, - \sqrt{\frac{1}{2}}\right)$$

## (b) Linearize about each of these two equilibrium states and find the state space matrices, given that 𝑥1 is the measured output variable.



# Question 5

## (a) Determine whether the system is stable.
[4 marks]

$$\dot{\text{x}}(t) = \begin{bmatrix} 1 & 1 \\ -2 & -3 \end{bmatrix} \text{x} (t) + \begin{bmatrix}1 \\ 1 \end{bmatrix} u (t)$$

$$y(t) = x_{1}(t) - u(t)$$


> [!NOTE] From notes
> 
> The system stability can be judged by the poles of the system, the poles are found as the [[eigenvalue]]s of the $A$ matrix given by the [[characteristic equation]]:
> 
> $$\Large \text {det} (A-\lambda I)=0$$
> 
> Where:
> - $\text {det}$ : refers to the [[Determinant]], which gives the factor by which area is scaled when a [[linear transformation]] is applied.
>   The determinant of a 2D transformation like this one can be found as:
> 
> $$\text{det} \left( \begin{bmatrix} 
> 	a & b \\
> 	c &d  \\
> \end{bmatrix}\right)
> = ad - bc$$
> 
> - $A$ : [[linear transformation|transformation matrix]]
> - $\lambda$ : [[Eigenvalues & Eigenvectors#Eigenvalues|Eigenvalue]]
> - $I$ : is the Identity matrix, a matrix of width and height = to number of dimensions and with 0s in all spots but the diagonal which contain 1s like so:
> 
> $$\begin{bmatrix} 
> 	1 &0 \\ 
> 	0 &1 \\ 
> \end{bmatrix},
> \begin{bmatrix} 
> 	1 &0 &0 \\ 
> 	0 &1 &0 \\ 
> 	0 &0 &1 \\ 
> \end{bmatrix}, 
> \text{ ect } \dots$$

Implementing the above then:

$$\text{det} \left(
\begin{bmatrix}
	1 & 1 \\ 
	-2 & -3 \\ 
\end{bmatrix}
-\begin{bmatrix} 
	\lambda & 0 \\
	0 & \lambda \\ 
\end{bmatrix} 
\right)=0$$

$$\text {det} \left(
\begin{bmatrix}
	1 - \lambda & 1 \\ 
	-2 & -3 - \lambda  \\
\end{bmatrix}\right) = 0$$

$$(1 - \lambda) (-3 - \lambda) - (1)(-2) = 0$$

$$(1 - \lambda) (-3 - \lambda) = - 2$$

Therefore:

$$\lambda = 1 \text{ or } 3$$

The poles are positive therefore the system is unstable

## (b) Obtain by hand the transfer function of the system and compare the result to that of ss2tf in MATLAB.
[8 marks]

### By hand

https://www.informit.com/articles/article.aspx?p=32090&seqNum=12

Transforming the state space equation:

$$\dot{\text{x}}(t) = \begin{bmatrix} 1 & 1 \\ -2 & -3 \end{bmatrix} \text{x} (t) + \begin{bmatrix}1 \\ 1 \end{bmatrix} u (t)$$

$$y(t) = x_{1}(t) - u(t)$$

To the Laplace domain:

$$s \text{X} (s) = A \text{X} (s) + B U (s) $$

$$Y(s) = C \text{X} (s) + D U (s) $$

Where $\text{X} (s)$ is equivalent to:

$$\text{X} (s) = (A-\lambda I)^{-1} BUs$$

As:

$$(A-\lambda I)^{-1} = \frac{\text {adj} (A-\lambda I)}{\text {det} (A-\lambda I)}$$
I can reuse some of the previous workings substituting $-\lambda$ for $s$ and $A$ for $-A$:

$$\text{X} (s)  = \text {det} (s I -A) \quad \text {det} (A-\lambda I)=0$$

*Note this isn't true it just let's me reuse the values*
$$\text {det} (A-\lambda I) = \text {det} (-A + s I)$$

$$(1 - \lambda) (-3 - \lambda) +2 = (-1 + s) (3 + s) + 2 = 0$$

Giving $\text {det} (s I -A)$ as:

$$\text {det} (s I -A) = s^{2} + 2s + 5$$

And $\text {adj} (s I -A)$ is simply 

$$\text {adj} \left(\begin{bmatrix} 
	a & b \\
	c &d  \\
\end{bmatrix}\right) = \begin{bmatrix} 
	a & c \\
	b & d  \\
\end{bmatrix}$$

thus

$$\text {adj} (s I -A) = 
\begin{bmatrix}
	s-1 & -1 \\ 
	2 & s+3 \\
\end{bmatrix}$$

Making:

$$(s I -A)^{-1} = 
\begin{bmatrix}
	s-1 & -1 \\ 
	2 & s+3 \\
\end{bmatrix} 
\times 
\frac{1}{s^{2} + 2s + 5}$$

The transfer function is given by:

$$G(s) = \mathbf{C} (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} + \mathbf{D}$$

Substituting in the identity for $(s I -A)^{-1}$ along with $B$, $C$ and $D$:

$$G(s) = 
\begin{bmatrix} 1 & 0 \end{bmatrix}
\begin{bmatrix}
	s-1 & -1 \\ 
	2 & s+3 \\
\end{bmatrix}  
\frac{1}{s^{2} + 2s + 5}
\begin{bmatrix} 1 \\ 1 \end{bmatrix}
-1$$

Which reduces to:

$$G(s) = \frac{s+4}{s^2 + 2s + 5} - 1 = \frac{-s^2 - s - 1}{s^2 + 2s + 5}$$

Therefore:

$$G(s) = \frac{-s^2 - s - 1}{s^2 + 2s + 5}$$

*this feels like allot of work for presumably less than 8 marks*

### Solving via matlab

https://www.mathworks.com/help/matlab/ref/ss2tf.html

```matlab
>> A = [1, 1; -2, -3];
>> B = [1; 1];
>> C = [1, 0];
>> D = -1;
>>
>> [b,a] = ss2tf(A, B, C, D)

b =

   -1.0000   -1.0000    5.0000


a =

    1.0000    2.0000   -1.0000

>> tf(b,a)

ans =

  -s^2 - s + 5
  -------------
  s^2 + 2 s - 1

Continuous-time transfer function.

```

They give the same results

## (c) Explain why the results are the same but that for a problem involving tf2ss this may not be the case.
[3 marks]

The results are the same as matlab is essentially doing the exact same computation as was done above. 

It's worth noting that matlab results can differ when running the same simulation in `Discrete-time` vs `Continous-time`, solving by hand is equivalent to `Continous-time` but could differ slightly from a discrete time solution which returns the the Z-transform transfer function. see https://www.mathworks.com/help/matlab/ref/ss2tf.html#buh8iwp

## (d) Design a state-feedback controller with poles at $s = -2 \pm j$, showing your method clearly. 
[10 marks]

> [!NOTE] *Based on my work from [Past Paper Questions](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/Tutorials/Past%20Paper%20Questions/Workings%20-%20Sample%20TCA%20Questions.md)*

The [[characteristic equation]] indicates the location of the system poles along with features of the systems behaviour. Currently the poles are at $1$ & $3$ as found in [[#(a) Determine whether the system is stable.]] Poles located at $s = -2 \pm j$ imply a [[characteristic equation]] of:

$$(s - (-2 + j))(s - (-2 - j)) = s^2 + 4s + 5.$$

Through the use of a regulator the [[characteristic equation]] can be moved to achieve different system behaviours. The regulator will consist of feedback $-K$ applied to the [[State Space Representation#State Vector|state vector]] $\text{x}$ and applied as the [[State Space Representation#Input Vector|input vector]] $u$.

$$\dot{\text{x}} = A \text{x} +Bu \quad \to \quad  \dot{\text{x}} = A \text{x} +B (-K \text{x})$$

Which can be rearranged and stated as:

$$\Large \dot{\text{x}} = (A - K B)\text{x}$$

This is of course based on the assumption that all the [[State Space Representation#State Variable|state variables]] are visible to the controller.

To find the correct values for gain $K$ to move the [[characteristic equation]] to $s^2 + 4s + 5 = 0$ the following equation must be satisfied:

$$\Large \text {det} (s I -(A - K B)) = s^2 + 4s + 5 = 0$$

As:
- $\text {det} (s I -(A - K B))$ : gives the [[characteristic equation]] of the system.
- $s^2 + 4s + 5$ : is the target [[characteristic equation]].

Substituting in the values for $A$ & $B$ in matrix from the left hand side ($\text{LHS}$) becomes:

$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-\left(
		\begin{bmatrix} 1 & 1 \\ -2 & -3 \end{bmatrix}
		-
		\begin{bmatrix} k_{1} & k_{2} \end{bmatrix}
		\begin{bmatrix} 1 \\ 1 \end{bmatrix} 
	\right)
\right)$$

This simplifies to:

$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-\left(
		\begin{bmatrix} 1 & 1 \\ -2 & -3 \end{bmatrix}
		-
		\begin{bmatrix} k_{1} & k_{2} \\ k_{1} & k_{2} \end{bmatrix}
	\right)
\right)$$

$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s & 0 \\ 
		0 & s \\ 
	\end{bmatrix}
	-
	\begin{bmatrix} 1 -k_{1} & 1 -k_{2} \\ -2 -k_{1} & -3 -k_{2} \end{bmatrix}
\right)$$

$$\text{LHS} = \text {det} \left(
	\begin{bmatrix} 
		s - 1 +k_{1} & -1 +k_{2} \\ 
		2 +k_{1} & s +3 +k_{2} 
	\end{bmatrix}
\right)$$

$$\text{LHS} = (s - 1 +k_{1}) (s +3 +k_{2}) - (-1 +k_{2}) (2 +k_{1})$$

$$\text{LHS} = (s - 1 +k_{1}) (s +3 +k_{2}) - (-1 +k_{2}) (2 +k_{1})$$

*I always get these expansions wrong by hand*

```matlab
>> syms s k_1 k_2
>> expand((s - 1 +k_1)*(s +3 +k_2) - (-1 +k_2)*(2 +k_1))

ans =

4*k_1 - 3*k_2 + 2*s + k_1*s + k_2*s + s^2 - 1

```

$$\text{LHS} = s^{2} + 4k_{1} - 3k_{2} + 2s + k_{1}s + k_{2}s - 1$$

Factoring this back into the equation:

$$s^{2} + 4k_{1} - 3k_{2} + 2s + k_{1}s + k_{2}s - 1 = s^{2} + 4s + 5 = 0$$

We can cancel it down:

$$\cancel{s^{2}} + 4k_{1} - 3k_{2} + 2s + k_{1}s + k_{2}s - 1 = \cancel{s^{2}} + 4s + 5$$

$$4k_{1} - 3k_{2} - 2s + k_{1}s + k_{2}s - 6 = 0$$

 and factorise for $k_{1}$ & $k_{2}$:
 
$$(4+s)k_{1} - (3+s)k_{2} - 2s - 6 = 0$$

```matlab
>> a = 4*k_1 - 3*k_2 - 2*s + k_1*s + k_2*s - 6;

>> solve(a,s)

ans = (3*k_2 - 4*k_1 + 6)/(k_1 + k_2 - 2)

>> solve(a,k_1)

ans = (3*k_2 + 2*s - k_2*s + 6)/(s + 4)

>> solve(a,k_2)

ans = -(4*k_1 - 2*s + k_1*s - 6)/(s - 3)

```

*I think I have made a mistake somewhere I don't see a solution*