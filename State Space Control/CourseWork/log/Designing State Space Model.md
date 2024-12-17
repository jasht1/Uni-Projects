### Givens
%%[[2024-12-16]] @ 12:46%%

The following are known values for the system that the model will be based off:

| Description                    | Notation     | Quantity | Units                                                     |
| ------------------------------ | ------------ | -------- | --------------------------------------------------------- |
| Quarter Car Mass               | $m_\text{b}$ | 150      | $\text{kg}$                                               |
| Wheel Mass                     | $m_\text{w}$ | 11       | $\text{kg}$                                               |
| Suspension Damping Constant    | $b_{s}$      | 690      | $\text{N} \! \cdot \! \text{m}^{-1} \! \cdot \! \text{s}$ |
| Suspension Spring Constant     | $k_{s}$      | 6936     | $\text{N} \! \cdot \! \text{m}^{-1}$                      |
| Tire Effective Spring Constant | $k_{t}$      | 28712    | $\text{N} \! \cdot \! \text{m}^{-1}$                      |

### Assumptions and Approximations
%%[[2024-12-16]] @ 01:01%%

As this is an independent suspension each wheel can be be assumed to behave similarly, and thus useful results can be found by only a quarter of the car and a single wheel.

Only linear vertical motion of the system will modelled under the assumption motion & rotation in other axis will be effectively constrained. The car body and wheel will be approximated as point masses within this single dimension with all forces acting in line with the centres of mass. 

Factors such as air resistance will be ignored, only the forces directly mentioned and their implicit consequences such as inertia from newton's second law will be in effect.

The model will assume the system starts in a steady state and is already under compression. It will assume the wheel never looses contact with the road and thus a restoring force equal to the effective elasticity of the tire is always in effect. 

### Constituent forces

%%[[2024-12-04]] @ 20:50%%

In order to determine the equations of motion the following constituent forces are considered.

##### Tire

$$\Large F_{k_{t}} = k_{t}(r - x_{w})$$

##### Spring

$$\Large F_{k_{s}} = k_{s}(x_{w} - x_{b})$$

##### Damper

$$\Large F_{b_{s}} = b_{s}(\dot x_{w} - \dot x_{b})$$

##### Actuator

$$\Large F_{f_{s}} = f_{s}(k_{1}x_{b}+k_{2}\dot{x}_{b}+k_{3}x_{w}+k_{4}\dot{x}_{w})$$

### Equations of Motion

%%[[2024-12-10]] @ 21:23%%

According to Newton's second law the acceleration of the bodies can be found by dividing the net force on the body by it's mass. $$a = \frac{F}{m}$$

##### Car Body Acceleration

$$\Large a_{\text{b}} = \frac{F_{f_{s}} + F_{k_{s}} + F_{b_{s}} }{m_{\text{b}}}$$

##### Wheel Acceleration

$$\Large a_{\text{w}} = \frac{F_{k_{t}} - F_{f_{s}} -F_{k_{s}} - F_{b_{s}}}{m_{\text{w}}}$$

### State Matrices 

%%[[2024-12-11]] @ 19:31%%

The standard form for the state equation is:

$$\Large \dot{\text{x}} = Ax +Bu$$

Where:

- $\dot x$ is the [[derivative]] of the [[#State Vector]]
- $x$ is the [[#State Vector]]
- $u$ is the [[#Input Vector]]
- $A$ is a matrix of first order coefficients that relate the [[#State Variable]]s to their effect on the system dynamic.
- $B$ is a matrix of first order coefficients that relate the system inputs to their effect on the system dynamic.

The state vector $\text{x}$ is comprised of the following state variables:

$$
\Large \text{x} = \begin{bmatrix} \begin{align*}
	x_{1} &:= x_{\text{b}} \\
	x_{2} &:= \dot x_{\text{b}} \\
	x_{3} &:= x_{\text{w}} \\
	x_{4} &:= \dot x_{\text{w}}
\end{align*}\end{bmatrix}
$$

Where $x$ and $\dot x$ refer to displacement and velocity respectively and $\text{b}$ and $\text{w}$ the body and wheel. Therefore the derivative of the state vector which gives the rate of change of the state vector is as follows:

$$
\Large \dot{\text{x}} = \begin{bmatrix} \begin{align*}
	\dot x_{1} &:= \dot x_{\text{b}} = x_{2}\\
	\dot x_{2} &:= \ddot x_{\text{b}} = a_{\text{b}}\\
	\dot x_{3} &:= \dot x_{\text{w}} = x_{4}\\
	\dot x_{4} &:= \ddot x_{\text{w}} = a_{\text{w}}
\end{align*}\end{bmatrix}
$$

Thus $A$ and $B$ are:

$$
\Large
A = \begin{bmatrix}
	0  & 1 & 0 & 0 \\
	-\frac{k_{s}}{m_{\text{b}}} & -\frac{b_{s}}{m_{\text{b}}} & \frac{k_{s}}{m_{\text{b}}} & \frac{b_{s}}{m_{\text{b}}} \\
	0 & 0 & 0 & 1 \\
	\frac{k_{s}}{m_{\text{w}}} & \frac{b_{s}}{m_{\text{w}}} & \frac{-k_{s}-k_{t}}{m_{\text{w}}} & -\frac{b_{s}}{m_{\text{w}}}
\end{bmatrix}
\qquad
B = \begin{bmatrix}
	0 & 0 \\
	0 & \frac{f_{s}}{m_{\text{b}}} \\
	0 & 0 \\
	\frac{k_{t}}{m_{\text{w}}} & -\frac{f_{s}}{m_{\text{w}}}
\end{bmatrix}
$$
