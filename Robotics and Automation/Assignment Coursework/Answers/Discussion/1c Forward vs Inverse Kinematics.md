
## 1c. Forward vs Inverse Kinematics
%%[[2025-03-26]] @ 18:52%%

> [!question] 
> ![1c. What are the differences between forward kinematics and inverse kinematics?](Questions.md#1c.%20What%20are%20the%20differences%20between%20forward%20kinematics%20and%20inverse%20kinematics?)

Fundamentally forward kinematics works out final global position and orientation based on a set of system states, and inverse kinematics dose the opposite, figuring out what set of system states will produce a given global position and orientation.

Both are useful techniques for operating robotic systems, where inverse kinematics provides motion planning and forward kinematics can be used for validation and simulation.

Both are applications of kinematic models, and a suitable kinematic model can often pull double duty for use in both forward and inverse kinematics, however forward kinematics is typically much simpler. The forward case can be found as a deterministic result of a series of transformations, where the inverse requires solving/approximating nonlinear equations. 

The use of forward kinematics to provide unsupervised learning data for machine learning based control approaches is a developing field in robotics [4] and especially in soft/continuum robotics where the lack of constraints makes kinematic particularly challenging. [5]