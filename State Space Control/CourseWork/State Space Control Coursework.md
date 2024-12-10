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

To model the behaviour of the system a state space representation will be used, where the state variables will be the displacement and velocity of the car body and wheel.

### Constituent forces
%%[[2024-12-04]] @ 20:50%%

In order to determine the equations of motion the following constituent forces need to be understood.

##### Weight
$$F_{w_{\text{b}}} = m_{\text{b}}g$$
$$F_{w_{\text{w}}} = m_{\text{w}}g$$
##### Tire
$$F_{k_{t}} = k_{t}(x_{b} - x_{w})$$
##### Spring
$$F_{k_{s}} = k_{s}(x_{b} - x_{w})$$
##### Damper
$$F_{b_{s}} = b_{s}(\dot{x}_{b} - \dot{x}_{w})$$

#### Equations of Motion
%%[[2024-12-10]] @ 21:23%%

According to Newton's second law the acceleration of the bodies can be found by dividing the net force on the body by it's mass. $$a = \frac{F}{m}$$

##### Car Body Acceleration
$$\Large a_{\text{b}} = \frac{F_{w_{\text{b}}} - F_{k_{s}} - F_{b_{s}}}{m_{\text{b}}}$$

##### Wheel Acceleration
$$\Large a_{\text{w}} = \frac{F_{w_{\text{w}}} + F_{k_{s}} + F_{b_{s}} - F_{k_{t}}}{m_{\text{w}}}$$

#### State Equations


#### Implementation
- MLB & Simulink

### Simulations

- Passive suspension
- Simple tuning
- Advanced tuning

#### Performance

#### Stability

