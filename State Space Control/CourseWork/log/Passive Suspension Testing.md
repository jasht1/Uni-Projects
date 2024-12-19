
## Passive Suspension Performance
%%[[2024-12-16]] @ 16:07%%

### Stability
%%[[2024-12-16]] @ 16:08%%

The poles of the system can be used to judge it's stability. The poles can be found as the eigenvalues of the feed forward transfer function and Matlab has built in methods `eig` or `pole` which can be used identify them. 

```matlab
>> pole(passive_suspension) 

ans =

 -32.1112  +44.9092i
 -32.1112  -44.9092i
  -1.5525  + 6.0982i
  -1.5525  - 6.0982i
```

From these an intuition can be gained of the systems inherent stability and and of its modes of natural resonance. In this case they indicate 2 modes of damped oscillation.
The real component indicates the linear damping of the system; if it is positive the system is positively reinforcing and any disturbance will grow indefinitely, if it is negative it contributes negative feedback and the system will trend towards a steady state.
The imaginary component indicates oscillatory behaviour, it indicates the frequency(s) the system will tend to oscillate at when disturbed.

Faster oscillations with less damping combine to make a more energetic system, in the case of a suspension this is to be avoided as it makes the suspension feel too "bouncy". In contrast slower oscillation with less damping can make the car feel "floaty" removing the "road feel" that informs the drivers intuition. Damping ratio gives a measure of this behaviour where the first case is considered under damped indicated by a damping ratio closer to 0, and the second case would be over damped with a damping ratio closer to 1.

![[passive_suspension-pole_zero.svg]]

The radial gird lines in the figure above indicate lines of constant damping ratio and the blue crosses are the poles of the passive suspension system.%%  A controller and actuator provides a means for affecting the system behaviour and thus move these poles.  %%
The mechanical properties of the spring, damper & tire in the passive suspension determine these poles and cause natural modes of oscillation. These present slightly differently differently in each state variable as can be visualised in the Nyquist plots below. 

![[passive_suspension-nyquist.svg]]

The wheel position displays two fairly distinguishable elliptical modes this is to be expected as it is connected by two springs of quite different elasticity. In contrast the car body position displays a more homogenised oscillation that can be interpreted as the superposition of 1) the natural frequency of the car body mass & suspension spring as it is deformed by 2) the wheel mass and tire elasticity. 
The velocities are of course derivatives of the resonance of the position variables, displaying the same behaviour but as a rate of change. An intuition can be gleamed for visualising how the potential energy shifts from the car body mass to the tire and back by following around the "fish shape" in the resonance of the car body velocity. This effect is far more substantial than it's equivalent in the wheel's velocity as the car body has significantly more mass and thus deflects less.

### Bump tests

The behaviour of the system is simulated to observe the response to a bump in the road. The bump in the simulation below is a 5 cm tall half sinusoid with a duration of half a second.

The simulations where created using the [[bump_response.m]] script that can be found [here](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/CourseWork/code/bump_response.m) in the working directory.

![[passive_suspension-bump_response.svg]]

The passive suspension dose slightly reduce the impulse but results in a larger displacement than the original bump and oscillates several times.

![[passive_suspension-bump_response-x_b.svg]]

%% ![[passive_suspension-bump_response-all_props.svg]] %%

### Initial Condition tests
%%[[2024-12-18]] @ 15:08%%

The system is simulated with an initial velocity in the body and then in the wheel to compare how it recovers from a disturbance in each case.
The simulations where created using the [[initial_velocity_response.m]] script that can be found [here](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/CourseWork/code/initial_velocity_response.m) in the working directory.

> [!note] *Figure n* ^figure-n
> ![[passive_suspension-V_i_response.svg]]

The system recovers from disturbances to the wheel much faster than a similar disturbance to the body as can be seen in [[#^figure-n|figure n]]. However this is to be expected as at the same velocity the car body represents far more inertia and thus more energy for the system to dissipate.

