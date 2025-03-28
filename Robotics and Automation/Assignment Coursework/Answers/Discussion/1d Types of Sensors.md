
## 1d Types of Sensors

> [!question] 
> ![1d. What are the common sensors in a typical robotic system?](Questions.md#1d.%20What%20are%20the%20common%20sensors%20in%20a%20typical%20robotic%20system?)

Sensors are vital to control of robotic systems as they provide observability of the system parameters that enable open loop control. In this case "system perimeters" may refer both to the states of controllable system components and to external stimuli. 

The most common sensors deployed in robotics systems (based entirely on my own intuition) are likely:

1. **Switches**
   I believe the humble contact switch is almost certainly the most common sensor, not just in their user interface role but as limit switches, shock/bump sensors (yes I'm including reed switches), object detection and more. The simple solution is often the best solution.

2. **Rotary encoders**
   Bar switches I would expect hall effect based rotary encoders are the most common by far, given they provide highly accurate, precise, low latency measures at the point of actuation for electric motors which I would expect to me the most common form of actuator deployed in robotic systems. This is likely followed by other forms of rotary sensor i.e. potentiomiter, pulse, laser etc.

3. **Proximity / Distance**
   From autonomous vehicles to polishing grinding stone wheels, autonomous systems need to measure how close they are to things. Of this category I expect LIDAR/sonic to be most prominent.
