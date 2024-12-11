Due [[2024-12-05|5th December]]
# State Space Control Coursework
%%[[2024-11-01]] @ 00:08%%

| Notation     | Quantity | Units                                                     |
| ------------ | -------- | --------------------------------------------------------- |
| $m_\text{b}$ | 150      | $\text{kg}$                                               |
| $m_\text{b}$ | 11       | $\text{kg}$                                               |
| $b_{s}$      | 690      | $\text{N} \! \cdot \! \text{m}^{-1} \! \cdot \! \text{s}$ |
| $k_{s}$      | 6936     | $\text{N} \! \cdot \! \text{m}^{-1}$                      |
| $k_{t}$      | 28712    | $\text{N} \! \cdot \! \text{m}^{-1}$                      |

## Background
![[State Space Representation]]

## Constructing a model

As this is an independent suspension each wheel can be be assumed to behave similarly, and thus useful results can be found by only a quarter of the car and a single wheel.

### Free Body Diagrams
%%[[2024-11-01]] @ 00:08%%
#### Quarter Car System diagram
![[State Space Control Coursework - Suspension Diagram.excalidraw]]

#### Car Body
![[State Space Control Coursework - m_b free body diagram.excalidraw|30%]]

#### Wheel
![[State Space Control Coursework - m_w free body diagram.excalidraw|35%]]

## System Dynamics

A state space representation will be used to model the behaviour of the system where the state variables will be the displacement and velocity of the car body and wheel.

### Constituent forces
%%[[2024-12-04]] @ 20:50%%

In order to determine the equations of motion the following constituent forces need to be understood.

%% 
##### Weight
$$\Large F_{w_{\text{b}}} = m_{\text{b}}g$$
$$\Large F_{w_{\text{w}}} = m_{\text{w}}g$$ 
%%
##### Tire
$$\Large F_{k_{t}} = k_{t}(x_{b} - x_{w})$$
##### Spring
$$\Large F_{k_{s}} = k_{s}(x_{b} - x_{w})$$
##### Damper
$$\Large F_{b_{s}} = b_{s}(\dot{x}_{b} - \dot{x}_{w})$$

#### Equations of Motion
%%[[2024-12-10]] @ 21:23%%

According to Newton's second law the acceleration of the bodies can be found by dividing the net force on the body by it's mass. $$a = \frac{F}{m}$$

##### Car Body Acceleration
$$\Large a_{\text{b}} = \frac{F_{w_{\text{b}}} - F_{k_{s}} - F_{b_{s}}}{m_{\text{b}}}$$

##### Wheel Acceleration
$$\Large a_{\text{w}} = \frac{F_{w_{\text{w}}} + F_{k_{s}} + F_{b_{s}} - F_{k_{t}}}{m_{\text{w}}}$$

#### State Equations

The standard form for the state equation is: $$\Large \dot{\text{x}} = Ax +Bu$$ 
Where:
- $\dot x$ is the [[derivative]] of the [[#State Vector]]
- $x$ is the [[#State Vector]]
- $u$ is the [[#Input Vector]]
- $A$ is a matrix of first order coefficients that relate the [[#State Variable]]s to their effect on the system dynamic.
- $B$ is a matrix of first order coefficients that relate the system inputs to their effect on the system dynamic.

The state vector $\text{x}$ is comprised of the following state variables: $$\Large \text{x} = \begin{bmatrix} \begin{align*}
	x_{1} &:= x_{\text{b}} \\
	x_{2} &:= \dot x_{\text{b}} \\
	x_{3} &:= x_{\text{w}} \\
	x_{4} &:= \dot x_{\text{w}}
\end{align*}\end{bmatrix}$$
Where $x$ and $\dot x$ refer to displacement and velocity respectively and $\text{b}$ and $\text{w}$ the body and wheel. Therefore the derivative of the state vector which gives the rate of change of the state vector is as follows: $$\Large \dot{\text{x}} = \begin{bmatrix} \begin{align*}
	\dot {x}_{1} &:= \dot {x}_{\text{b}} = x_{2}\\
	\dot {x}_{2} &:= \ddot {x}_{\text{b}} = a_{\text{b}}\\
	\dot {x}_{3} &:= \dot {x}_{\text{w}} = x_{4}\\
	\dot {x}_{4} &:= \ddot {x}_{\text{w}} = a_{\text{w}}
\end{align*}\end{bmatrix}$$
Thus $A$ and $B$ become: $$\Large 
A = \begin{bmatrix} 
	0  & 1 & 0 & 0 \\ 
	-\frac{k_{s}}{m_{\text{b}}} & -\frac{b_{s}}{m_{\text{b}}} & \frac{k_{s}}{m_{\text{b}}} & \frac{b_{s}}{m_{\text{b}}} \\ 
	0 & 0 & 0 & 1 \\ 
	-\frac{k_{s}}{m_{\text{b}}} & -\frac{b_{s}}{m_{\text{b}}} & \frac{k_{s}}{m_{\text{b}}} & \frac{b_{s}}{m_{\text{b}}}
\end{bmatrix} 
\qquad 
B = \begin{bmatrix} 
	0 \\ 0 \\ 0 \\ \frac{k_{t}}{m_{\text{w}}} 
\end{bmatrix}$$

#### Implementation
- MLB & Simulink

### Simulations

- Passive suspension
- Simple tuning
- Advanced tuning

#### Performance

#### Stability

