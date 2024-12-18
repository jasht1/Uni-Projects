
## Comparison of Simulink and Matlab implementation

### Matlab Implementation

## Passive Suspension Performance
%%[[2024-12-16]] @ 16:07%%

### Stability
%%[[2024-12-16]] @ 16:08%%

The poles of the system can be used to judge it's stability. The poles can be found as the eigenvalues of the feed forward transfer function and Matlab has built in methods `eig` or `pole` which can be used identify them. 

```matlab
>> pole(plant) 

ans =

 -32.1112 +44.9092i
 -32.1112 -44.9092i
  -1.5525 + 6.0982i
  -1.5525 - 6.0982i
```

From these an intuition can be gained of the systems inherent stability and and of its modes of natural resonance. In this case they indicate 2 modes of damped oscillation.
The real component indicates the linear damping of the system; if it is positive the system is positively reinforcing and any disturbance will grow indefinitely, if it is negative it contributes negative feedback and the system will trend towards a steady state.
The imaginary component indicates oscillatory behaviour, it indicates the frequency(s) the system will tend to oscillate at when disturbed.

Faster oscillations with less damping combine to make a more energetic system, in the case of a suspension this is to be avoided as it makes the suspension feel too "bouncy". In contrast slower oscillation with less damping can make the car feel "floaty" removing the "road feel" that informs the drivers intuition. Damping ratio gives a measure of this behaviour where the first case is considered under damped indicated by a damping ratio closer to 0, and the second case would be over damped with a damping ratio closer to 1.

![[passive_suspension-pole_zero.svg]]

The radial gird lines in the figure above indicate lines of constant damping ratio and the blue crosses are the poles of the passive suspension system.%%  A controller and actuator provides a means for affecting the system behaviour and thus move these poles.  %%
The mechanical properties of the spring, damper & tire in the passive suspension determine these poles and cause natural modes of oscillation that can be visualised in the Nyquist plot below. 

![[passive_suspension-nyquist.svg]]

### Bump tests

The behaviour of the system is simulated to observe the response to a bump in the road. The bump in the simulation below is 5 cm half sinusoid with a duration of half a second.

![[passive_suspension-bump_response.svg]]

The passive suspension dose slightly reduce the impulse but results in a larger displacement than the original bump and oscillates several times.

![[passive_suspension-bump_response-x_b.svg]]

![[passive_suspension-bump_response-all_props.svg]]

