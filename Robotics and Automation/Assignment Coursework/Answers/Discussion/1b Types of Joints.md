
## 1b. Types of Joints
%%[[2025-03-26]] @ 17:21%%

> [!question] 
> ![1b. What are the types of joints in a robot? What motions can they provide?](Questions.md#1b.%20What%20are%20the%20types%20of%20joints%20in%20a%20robot?%20What%20motions%20can%20they%20provide?)

### What are the types of joints in a robot? What motions can they provide?

To utilise actuation the parts of a traditional robot must be joined such that they can move by acting on each other but be constrained such that the motion is predictable and controllable. 

The following types are broadly applicable and useful for describing almost any conceivable joint.

| Joint Type  | Motion                                   | Degrees of Freedom |
| ----------- | ---------------------------------------- | ------------------ |
| Rotary      | Rotation                                 | 1                  |
| Linear      | Translation                              | 1                  |
| Cylindrical | Rotation & Translation                   | 2                  |
| Spherical   | Rotation                                 | 3                  |
| Planar      | Translation                              | 2                  |
| Universal   | Rotational                               | 2                  |
| Screw       | Links Rotational to Transnational motion | 1                  |
| Free        | Rotation & Translation                   | 6                  |

However the limits  of a Joint are also a vital consideration beyond degrees of freedom. For example a hinge and a wheel would both be "rotary" joints in this regime but their behaviour is not interchangeable given the hinge limits its rotation to $360\degree$ or less where a wheel would not. Similarly a cable would be classed as a "free" joint and still would be after it had snapped but the difference in system behaviour would likely be drastic.

MATLAB's Robotic System Toolbox has a class system for defining joints using the `rigidBodyJoint` object that considers both degrees of freedom with it's `type` and position limits aptly named `PositionLimits`. [3]
