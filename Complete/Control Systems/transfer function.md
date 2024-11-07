# Transfer functions
#definition A **Transfer function** is a [[Laplace transform]] of the [[#Impulse response]] of a [[time invarient system]] when the system initial conditions are set to 0. Denoted by: $H(s)$
![[Pasted image 20231016102150.png|400]]
Transfer functions utilise the [[S plane|complex domain]] as to reduce the complexity of common operations that would otherwise require [[convolution]].

## Poles & Zeros
#definition **Zeros** are the frequencies (values of s) for which the *numerator* of the [[transfer function]] becomes 0.
#definition **Poles** are the frequencies (values of s) for which the *denominator* of the [[transfer function]] becomes 0.
[Explainer video (Neso Academy)](https://www.youtube.com/watch?v=AZ7_MvANy_Q&t=2s)
### MATLAB command
``` MATLAB
%%pole-zero map
clear
close all
s-tf('s');
g-(0.5*s+1)/((s+1)*(s+5));
pzmap (G)
```
### ![[Root locus]]
## Solving transfer functions
### Standard responses
##### Impulse response
#definition **Impulse response** #WIP ...denoted by: $h(t)$ 
given by the [[Laplace transform#Inverse laplace transform|Inverse laplace transform]] of the [[transfer function]] $H(s)$.
Laplace transform of a impulse response is $1$$$ R(s) = 1$$
Equivalent to differentiating
##### step response
#definition **Step response** $R(s)$ is the response of the system when the input signal is the [[#step]] signal. 
$$\text{Step Response}=\int^t_0 (\text{Impulse respnse})dt$$
Laplace transform of a step response is $1/s$ $$ R(s) = 1/s$$
Equivalent to integrating
##### Ramp response
Laplace transform of a ramp response is $1/s^2$ $$ R(s) = 1/s^2$$

[Explainer video (Neso Academy)](https://www.youtube.com/watch?v=virn3Nnwb3A)

### [[Laplace transform]] method
[[Slides_week3.pdf]]
converts a time based function into an S domain function.
$$𝐹(𝑠) = ∫^\infty_0 𝑒^{−𝑠𝑡}𝑓(𝑡)𝑑𝑡$$
Multiplies the time domain function $f(t)$ by a degrading exponential $𝑒^{−𝑠𝑡}$ this ensures that the function tends to 0 so that any reasonable function forms a curve that crosses the x axis at two points.

