# Week 1
![[Basic control system block diagram 2023-09-25 09.55.03.excalidraw]]
# Week 2 - ODE
plotting things in matlab
t=0:0.01:50;y=1-cos(t);figure,plot(t,y)
t= initial time; function; figure plot(x,y)

## Transfer functions
S is a differentiation operator
solving transfer functions is just about remembering to solve for y(t)
### closed loop transfer func
$$T(s) = \frac{A}{1+AB}$$
$$T(s) = \frac{\text{forward path}} {(1+ \text{loop})}$$

# Week 3
Steady state error is just solving for when time derivatives are equal to 0
## dynamic systems
### Solving dynamic systems methods
#### Computer methods
create block diagram using integrators found from the differential equation
or
Transfer function blocks with control loop, found form plant diff equation 
#### Analytical methods 
particular integral + complementary function
or
[[Laplace transform]]
## [[Laplace transform]]
Converts form $f(t)$ to $f(s)$. where $s$ is in rad/sec and could be much better represented with an $\omega$ but anyway as you are still integrating the function up a plane all the same rules apply with the [[S plane]]
![[Laplace transform#Signal transforms truth table]]
## Tutorial questions
### Section 1
1. Calculate 𝐹(𝑠) for $𝑓(𝑡) = 𝑒^{−𝑎𝑡}$ where 𝑎 is a positive constant. Check with the table above. 
	$F(s)=\frac{1}{S+a}$ 
2. The unit impulse function 𝛿(𝑡) is a kind of concentrated pulse that looks a little like this. The integration should start just before 𝑡 = 0 and ‘during the pulse’ the term $𝑒^{−𝑠𝑡}$ hardly changes (since 𝑡 hardly changes). Find the Laplace transform of this function.
	$F(s)=1$
3. Calculate 𝐹(𝑠) for $𝑓(𝑡) = 𝑒^{𝑗𝜔𝑡}$ treating 𝑗𝜔 like a constant. The calculation is similar to question 1. 
	$F(s)=\frac{1}{S+j\omega}$
4. Noting that $𝑒^{𝑗𝜔𝑡} = cos 𝜔𝑡 + 𝑗 sin 𝜔𝑡$, try to derive 𝐹(𝑠) for cos 𝜔𝑡 (real part) and sin 𝜔𝑡 (imaginary part). 
	
6. Use integration by parts to find the Laplace transform of 𝑑𝑓 𝑑𝑡 , assuming 𝐹(𝑠) is the transform of 𝑓(𝑡).
### Section 2
6. For the above example, 𝑦̇ + 𝑦 = 𝑢, now assuming zero initial conditions, use the Laplace method to calculate (i) the impulse response (𝑢 = 𝛿(𝑡)), (ii) the step response (𝑢 = 1(𝑡)) and (iii) the ramp response (𝑢 = 𝑡). Plot the solutions in Matlab. 

7. Recompute the plots from question 6 using the s=tf('s') method. Note that as well as the command step, Matlab has a command impulse. There is no command “ramp” so you need to be a bit creative to get that result. 

8. For the second-order system 𝑑2𝑦 𝑑𝑡2 + 6 𝑑𝑦 𝑑𝑡 + 5𝑦 = 𝑢 (
	1. find the transfer function 
	2. determine the steady-state gain for this transfer function 
	3. use Laplace to find the unit step response, assuming zero initial conditions. Plot the result. 
	4. repeat (3) but with 𝑦(0) = 1, 𝑦̇ (0) = 2.
# Week 4 - Poles & zeroes
[[Slides_week4.pdf]]
2024-01-14 @ 18:09 
$e^{-at}: t_{s}= \frac{3}{a}$

# Week 5 - Bode Plots
[[Slides_week5.pdf]]
Oscillatory error is caused by imaginary poles being too close to axis

do you ever tune control systems to be oscillatory? It would be more effective to tune a higher order system at that point right?

$1/rt2$ theta gives 5% overshoot 
$1$
moving radially out and keeping theta the same makes the response quicker without changing overshoot. %%horizontal stretch%%

Positive means unstable
too high an angel of an angle ($<55 \degree$) means slow response, takes too long to settle. This indicates a disproportionately large imaginary component.
Lower than $-\sigma$ real part 
	*Why mechanistically is this a problem?*

*Careful with algebra in closed loop tf especially when simplifying* 

# Week 6 - $e_{ss}$ and type & order
[[Slides_Week6.pdf]]
## Type & order
order is the highest power of s in the denominator
	complexity
type is how many pure powers of s in the denominator
	poles on the real axis

Proper transfer functions are bottom heavy, with higher powers in the denominator than numerator

## steady state error $(e_{ss})$
### Considerations
*steady state error $(e_{ss})$ should be considered for the open loop system.*
*steady state error dose not apply to unstable systems*
### Final value theorem
#definition final value theorem: steady state error of a system that settles to a constant value  should be equal to the sum of constants
$$\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$$
### Error constant formula
For each system type there is only one input t,hat yields a non zero finite error. ![[Pasted image 20231030101423.png]]

| type | Step | Ramp | Parabolic |
| ---- | ---- | ---- | ---- |
| $S^0$ | $\frac{1}{1+K_p}$ | $\infty$ | $\infty$ |
| $S^1$ | 0 | $\frac{1}{k_v}$ | $\infty$ |
| $S^2$ | 0 | 0 | $\frac{1}{k_a}$ |
where $K_p = \text{error constant}$
#### Useful phrases
where $K_{p}$ is the error constant given by applying the final value theorem, $\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$, to the derivative of the OLTF.
##### Type 0 step
Given the OLTF is type 0 the steady state error ($e_{ss}$) of a step input is given by $\frac{1}{1+K_p}$, where $K_{p}$ is the error constant given by applying the final value theorem ($\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$) to the derivative of the OLTF.
##### Type 1 
###### Step
Given the OLTF is type 1 the steady state error ($e_{ss}$) of a step input will be $0$ the system will eventually settle to the exact intended value.
###### Ramp
Given the OLTF is type 1 the steady state error ($e_{ss}$) of a ramp input is given by $\frac{1}{k_v}$, where $K_{v}$ is the error constant given by applying the final value theorem ($\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$) to the derivative of the OLTF.
$$K_{V}=\lim_{s\to\infty}OLTF(s) = ...$$
Factoring this into the above mentioned equation,
$$e_{ss} = \frac{1}{k_{v}} = \frac{1}{\infty}= 0 \quad \therefore \quad e_{ss}= 0$$
####
in a closed loop system where G(s) is in the denominator we want a high gain to reduce steady state error
$$\frac{1}{1+K_p}$$

$$k_a=\lim_{s\to0} s^2g(s)$$

$$e_{ss}=\frac{1}{K_a}$$



- [x] format cntl sys w6 notes 📅 2023-12-30 ✅ 2024-01-16
- [-] do cntl sys w6 tutorial questions wed
# Week 7 - [[Root locus]]
quotient
argument = angle = $\tan(i/j)$ 

$$KG(s) = -1$$
With a given test point $s_0$ the required gain can be found with:$k = \frac{1}{G(s_0)}$
Angle argument:$$\angle G = \arg(G) =n\pi$$

In general there are $m$ zeros & $n$ poles
$$G(s)= k \frac{(s-z_1)(s-z_2)...(s-z_m)}{(s-p_1)(s-p_2)...(s-p_n)}$$

The point that asymptotes cross the real axes $(a)$ can be found by $$a = \frac{\sum p-\sum z}{n-m}$$

#MATLAB rltool(G)

# Week 8 - Ziegler-Nichols
2023-11-13 @ 13:49 
## Ziegler-Nichols gains
#definition For PID there are optimal gains called Ziegler-Nichols gains, which are: $$K_p = 0.6 K_u \qquad  T_i = \frac{P_u}{2} \qquad  T_d = \frac{P_u}{8}$$
## Placing poles

Knowing where S is we can solve for the angle using the angle sum formula
## Tutorial questions
1. For the breakaway point example with transfer function 𝐺(𝑠) = 0.1𝑠+1 𝑠2+𝑠+10, find the gains associated with 𝑠 = 0 and 𝑠 = −20. 
2. Check the positive gain value using rlocus in Matlab. 
3. Check both gain values using evalfr in Matlab. 
4. Sketch the general form of the root locus for 𝐺(𝑠) with three different stable poles, all with equal real parts, and no zeros. Pay particular attention to the angles of departure. 
5. Choose suitable values for the poles and check your sketch using rlocus. 
6. Repeat questions 4 and 5 in the case with 2 complex stable poles and one zero, all with equal real parts. 
7. Calculate the position of the breakaway point in case 𝐺(𝑠) = 𝑠+2 (𝑠+2)2+4 and check using rlocus.

# Week 9
[[Slides_Week9.pdf]]
## Frequency response function
*Typically applied to open loop tf*
Where the input is $u(t) = e^{j \omega T}$ the output is $y(t) = He^{j \omega T}$, for any given input frequency $|H|$ is the gain and $\angle H = e^{j \phi}$.

**$H(\omega)$ gives a frequency response function $H(\omega) = G(jw)$**

in general $\angle H = -\arctan \omega T$, therefore as $\omega \to \infty$ phase lag reaches $90 \degree$

The frequency response function $H(\omega)$ can be used to analyse stability. 
- If $\left|H\right| \ge 1$ then the frequency gain is positive and therefore unstable.
- If $\angle H = 180 \degree$ the phase lag will constructively interfere and cause instability.

now to actually control the stability we can use a lead compensator.
G(s)=kb(s+a)a(s+b)
Where $-a$ is the zero location & $-b$ is the pole location

%%what happens is you have multiple poles / zeros%%

At frequency 𝜔 and with time delay T seconds, the phase lag will be 𝜙 = 𝜔𝑇 radians. The gain equals 1 at all frequencies. Hence
𝐻(𝜔) = 𝑒−𝑗𝜔𝑇 
and transfer function 
𝐺(𝑠) = 𝑒−𝑠𝑇

#definition **Geometric mean**: $n$ numbers are multiplies together and the $n$th root is taken. 
	Can be used to find mid point on a logarithmic scale

#definition **Critical stability** is the margin between stability and instability.
#definition The **gain margin $Gm$** is the amount of extra gain before the function becomes unstable / reaches critical stability.
#definition The **Phase margin $Pm$** is the amount of extra phase lag before the the function becomes unstable / reaches critical stability.

Nyquist plot
	Way of visualising stability that plots both imaginary and real limits as a perimeter on the imaginary plane, stability can be inferred based on whether the poles are enclosed by the limits.


$e_{ss}=1K_{v}$

## Tutorial questions
1. A plant has a gain margin of 2.5 dB. What is the (linear) gain that can be applied before making the system unstable. 
	$Gm = 2.5 dB$
	$Gm = 20 \log _{10} k > 0$
	$k = \frac{10^{Gm}}{20}$/
1. The gain of a controller can by increased by a factor of 4 before it becomes unstable in closed loop. What is the gain margin in dB? 
2. A plant has a phase margin of 45°, which occurs when the frequency is 𝜔 = 1 rad/sec. What is the time delay in the feedback loop that will just make the system unstable. 
3. Use the function bode in Matlab to plot gain and phase for the following transfer functions. In each case find the gain and phase margins by zooming in on the relevant part of the plot. (a) 𝐺(𝑠) = 10 (𝑠+1)2(𝑠+2) (b) 𝐺(𝑠) = 5 𝑒−0.2𝑠 𝑠 
4. Repeat question 4 using the Matlab command margin. 
5. Given the open-loop transfer function 𝐺(𝑠) = 𝜔𝑛 2 𝑠2 + 2𝜁𝜔𝑛𝑠

# Week 10 - Stability testing
2024-01-08 @ 10:01 
In general, for a transfer function in the form $G(s)=\frac{N(s)}{D(s)}$, stability is determined by the roots of the denominator polynomial $D(s)$. 
If all the roots of $D(s)$ have negative real parts, the system is stable. If any root has a positive real part, the system is unstable.
## Routh-Hurwitz
for a CLTF
### Criteria for stability
1. The system will produce a bounded output for every bounded input;
2. If there is no input, the output should tend to be zero, irrespective of any initial conditions.
https://en.wikipedia.org/wiki/Routh%E2%80%93Hurwitz_stability_criterion

make Ralph table
### Routh-Hurwutz table
%% Improve this like [this](https://www.google.com/url?sa=i&url=https%3A%2F%2Fisaacscienceblog.com%2F2017%2F08%2F15%2Frouth-hurwitz-stability-criterion%2F&psig=AOvVaw0wY4O8HTqiaw86Ohpb95ma&ust=1705375414693000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCKjQxtK43oMDFQAAAAAdAAAAABAD) but with colour%%
For a given transfer function focus on the characteristic equation (the denominator).
$$tf = \frac{numerator}{as^{4}+bs^{3}+cs^{2}+ ds +e}$$
and construct a RH table by adding the coefficients of $s$ even in one row odd in the next, 
	(*other way around if the highest power of $s$ is odd*)

| $s^4$ | $a$ | $c$ | $e$ |
| ---- | ---- | ---- | ---- |
| $s^3$ | $b$ | $d$ | $0$ |
| $s^2$ | $= \frac{(bc-ad)}{b}$  | $= \frac{de-c0}{d}$ | $0$ |
| $s^1$ | $$ | $$ | $0$ |
| $s^0$ | $$ | $$ | $0$ |

#### Copy table
| $s^4$ | $$ | $$ |
| ---- | ---- | ---- |
| $s^3$ | $$ | $$ |
| $s^2$ | $$ | $$ |
| $s^1$ | $$ | $$ |
| $s^0$ | $$ | $$ |
## Nyquist

# Week 11
2023-12-04 @ 09:33 
[[Slides_Week11.pdf]]
### System sensitivity
In a system $y$ where $u$ is an input, $p$ is a parameter,
$$y=f(u,p)$$
we often need to know the sensitivity of system $y$ to an input $p$. This is the proportional change of $y$ to a proportional change in $p$.
$$ S^T_G = \frac{G}{T} \frac{\delta T}{\delta G} $$
### Simplifying [[Block diagrams]]

## Tutorial questions
2023-12-04 @ 10:12 
### 1 find bode plot of the CLTF
```
s = tf("s")

G = (s+8)/(s^3 + 7*s^2 + 15*s + 25)

K =140

C = K*(1+0.1*s)

bode(G*C)

rlocus(G*C)

K =400

bode(G*C)

rlocus(G*C)
```
### 2 plot sensitivity $S=1-t$


# Week 12 - Review & revision
[[Slides_Week12a.pdf]]
![[Week before exam]]
