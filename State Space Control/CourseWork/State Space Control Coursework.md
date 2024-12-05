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

### Free Body Diagrams
%%[[2024-11-01]] @ 00:08%%
#### Quarter Car System diagram
![[State Space Control Coursework - Suspension Diagram.excalidraw]]

#### Car Body
![[State Space Control Coursework - m_b free body diagram.excalidraw|30%]]

#### Wheel
![[State Space Control Coursework - m_w free body diagram.excalidraw|35%]]

### Equations of Motion

#### Constituent forces

##### Weight
$$F_{w_{\text{b}}} = w_{\text{b}}g$$
$$F_{w_{\text{w}}} = w_{\text{w}}g$$
##### Tire
$$F_{k_{t}} = k_{t}(x_{b} - x_{w})$$
##### Spring
$$F_{k_{s}} = k_{s}(x_{b} - x_{w})$$
##### Damper
$$F_{b_{s}} = b_{s}(\dot{x}_{b} - \dot{x}_{w})$$
## 

#### Implementation
- MLB & Simulink

### Simulations

- Passive suspension
- Simple tuning
- Advanced tuning

#### Performance

#### Stability

