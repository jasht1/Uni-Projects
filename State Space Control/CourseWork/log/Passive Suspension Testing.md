
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

From these an intuition can be gained as to how the system responds and how prone it is to settle to steady state. 
The real component indicates the damping of the system; if it is positive the system is positively reinforcing and any disturbance will grow indefinitely, if it is negative it contributes negative feedback and the system will trend towards a steady state.
The imaginary component 


![[passive_suspension-pole_zero.svg]]

![[passive_suspension-nyquist.svg]]