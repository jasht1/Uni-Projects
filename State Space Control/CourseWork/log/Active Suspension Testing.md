## Active Suspension Performance

Where the [[Passive Suspension Testing]] section focused more on introducing and explaining of terms measures and intuitions. The performance of the active suspension system will be discussed largely in contrast with the baseline performance of the passive suspension system. 
All of the same tests have been performed with the MATLAB implementation of the active suspension utilising the actuator and a PD controller. The controller takes in the car body displacement state variable referred to previously as $x_b$ / `x_b` as it's input, which may be collected in the real system with a ride height sensor. PD refers to proportional and derivative as the controller takes the form `{matlab}controller = kp + kd * s;` where `kp` is a proportional gain and `kd` is a derivative gain on the car body position. The output of this controller is fed into the actuator input of the state space system where it applies it's force against the wheel and body.

### Stability
%%[[2024-12-19]] @ 04:36%%

```matlab
>> pole(tuned_suspension)

ans =

   -120.48  +     0i
   -6.8655  +38.709i
   -6.8655  -38.709i
  -0.64921  +     0i
```

The active suspension eliminates one of the modes of resonance that was present in the [[Passive Suspension Testing#Stability|Passive Suspension Testing]] at $6 \text{ Hz}$. It slightly reduces the natural frequency of the other mode that was previously near $45 \text{ Hz}$ and reduced its damping coefficient. Two additional poles have been added, these act as negative gains which can help the system as long as they aren't in a similar range to typical system inputs, in which case they can lead to instability.

> [!FIGURE] Figure n: Active Suspension Pole Zero Map ^active-pzplot
> ![[active_suspension-pole_zero.svg]]

Comparing the [[#^active-suspension-nyquist|Nyquist plots]] below with those of the Passive Suspension shows how the controller has effected the natural modes of resonance in the system. The modes of the body position and acceleration are substantially smaller in both their real and imaginary components whereas those of the wheel are larger. The system still has to absorb and dissipate the same amount of energy but the active suspension shifts much of the systems energy into the wheel mass%% causing it to resonate more while the car body resonates less %%.

> [!figure] Figure n: Active Suspension Nyquist Diagrams ^active-suspension-nyquist
> ![[active_suspension-nyquist.svg]]


### Bump Test
%%[[2024-12-18]] @ 23:59%%

The behaviour of the system is simulated to observe the response to a bump in the road. The bump in the simulation below is a 5 cm tall half sinusoid with a duration of half a second.

The simulations where created using the [[bump_response.m]] script that can be found [here](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/CourseWork/code/bump_response.m) in the working directory.

> [!FIGURE] Figure n: Active Suspension Bump Response ^active-bump-response
> ![[active_suspension-bump_response.svg]]

The Active suspension provides a substantial improvement in every respect. It eliminates the oscillations seen in the [[Passive Suspension Testing#Bump tests]] and reduces the magnitude of the body displacement, velocity and acceleration.

> [!FIGURE] Figure n: Active Suspension Bump against Body Displacment ^active-bump-xb
> ![[active_suspension-bump_response-x_b.svg]]

The effect of the bump is diminished significantly from the perspective of the passenger with the displacement felt being reduced to less than 20% of the actual disturbance.

%% ![[active_suspension-bump_response-all_props.svg]] %%
### Initial Condition Test
%%[[2024-12-19]] @ 01:37%%

The system is simulated with an initial velocity in the body and then in the wheel to compare how it recovers from a disturbance in each case.
The simulations where created using the [[initial_velocity_response.m]] script that can be found [here](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/CourseWork/code/initial_velocity_response.m) in the working directory.

> [!FIGURE] Figure n: Active Suspension Initial Velocity Response ^active-iv
> ![[active_suspension-V_i_response.svg]]

In the initial car body velocity simulation the peak car body acceleration is actually 50% higher with this controller implementation than it was in the [[Passive Suspension Testing#Initial Condition tests]]. However, the benefit is made clear by comparing the root mean squared acceleration across the same 5 second simulation with $0.5 \ m/s$ of initial body velocity, the controller reduces `rms(a_b)` down from $0.6677 \ m/s$ to $0.1903 \ m/s$, less than 30% of that of the passive suspension.
The initial wheel velocity simulation sees significant improvement by all measures, most importantly peak acceleration similarly reduced by 2 orders of magnitude with a 96% reduction in root mean squared acceleration `rms(a_b)`. 