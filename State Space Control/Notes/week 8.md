
## Full state feedback
%%[[2024-11-15]] @ 09:42%%

Further to feeding back a single output variable, we can feedback the computed values of all of the system states. 

Given that we can already determine state equations that associate the states of the systems with it's dynamics, aswell as a control matrix that modifies the behaviour of the system using these states. We can use feedback of these states in our control system.

The closed loop dynamics of the system are given by the [[State Space Representation#Input Equation|input]] & [[State Space Representation#Output Equation|output]] equation equations: $$ \dot x = Ax+Bu$$

7