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

%%
##### Weight
$$F_{w_{\text{b}}} = w_{\text{b}}g$$
$$F_{w_{\text{w}}} = w_{\text{w}}g$$
%%

####

#### References
https://www.mathworks.com/help/robust/gs/tuning-control-system-with-multiple-valued-plant-parameters-using-control-system-tuner.html

https://www.researchgate.net/publication/361381452_Design_of_Virtual_Reference_Feedforward_Controller_for_an_Active_Suspension_System

https://www.researchgate.net/publication/352565005_Artificial_Neural_Network_Prediction_of_the_Optimal_Setup_Parameters_of_a_Seven_Degrees_of_Freedom_Mathematical_Model_of_a_Race_Car_IndyCar_Case_Study


