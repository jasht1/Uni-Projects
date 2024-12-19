Active Suspension Testing

## Active Suspension Performance

### Stability

### Bump Test
%%[[2024-12-18]] @ 23:59%%

The behaviour of the system is simulated to observe the response to a bump in the road. The bump in the simulation below is a 5 cm tall half sinusoid with a duration of half a second.

The simulations where created using the [[bump_response.m]] script that can be found [here](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/CourseWork/code/bump_response.m) in the working directory.

![[active_suspension-bump_response.svg]]

The Active suspension provides a substantial improvement in every respect. It eliminates the oscillations seen in the [[Passive Suspension Testing#Bump tests]] and reduces the magnitude of the body displacement, velocity and acceleration.

![[active_suspension-bump_response-x_b.svg]]

The effect of the bump is diminished significantly from the perspective of the passenger with the displacement felt being reduced to less than 20% of the actual disturbance.

%% ![[active_suspension-bump_response-all_props.svg]] %%
### Initial Condition Test
%%[[2024-12-19]] @ 01:37%%

The system is simulated with an initial velocity in the body and then in the wheel to compare how it recovers from a disturbance in each case.
The simulations where created using the [[initial_velocity_response.m]] script that can be found [here](https://github.com/jasht1/Uni-Projects/blob/master/State%20Space%20Control/CourseWork/code/initial_velocity_response.m) in the working directory.

![[active_suspension-V_i_response.svg]]

The initial wheel velocity of $0.5 \ m/s$ results in a very large acceleration of the car body. The acceleration is very short and results in negligible actual velocity or displacement of the car body but more than likely exceeds the maximum force the actuator can exert. 