Test: [[EGR2006M TCA_2021-2022.pdf]]
Solutions: [[Slides_Week12a.pdf]]
# 1
![[EGR2006M TCA_2021-2022 fig1.png]]
## 1.1 - Derive the transfer function of the whole system shown in Figure 1.
![[Q1a-CS-TCA2023.excalidraw]]
## 1.2 - Whats the order of each subsystem & the whole system
| Transfer function | a | b | c | T |
| ---- | ---- | ---- | ---- | ---- |
| order | 2 | 2 | 0 | 3 |
## 1.3 - Calculate the steady-state error of the whole system for a unit step input.

For a step input steady state error can be found by the formula
$\frac{1}{1+K_p}$ where $K_p$ is the error constant given by the final value theorem.
**final value theorem**: steady state error of a system that settles to a constant value  should be equal to the sum of constants
$$\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$$
Using the function of $G_{(s)}$ found in [[#1.1 Derive the transfer function of the whole system shown in Figure 1.|1.1]];
$$G_{(s)} = \frac{50 s}{s^{2} + s + 100}$$
$$\lim_{s\to0}G_{(s)}= \frac{0}{100} = \infty$$
Factoring into $K_{p}$ into the previously mentioned formula gives:
$$ e_{ss}=\frac{1}{1+\infty}=0$$
___
# 2
![[Fig2-CS-TCA2022.png]]
## 2.1 - Find the system transfer function.
![[Q2.1-CS-TCA2023.excalidraw]]
## 2.2 - Design the value of $K$ so that for an input $100tu(t)$, there will be a 1% steady-state error
2024-01-14 @ 17:09 
The open loop transfer function found previously is a type one system, $$\frac{k}{s^{2}+11s}$$Therefore a ramp is the only non 0 error state.
for a ramp input steady state error is $e_{ss} = \frac{1}{K_{v}}$ 
Given that
$$e_{ss}= 0.01 = \frac{1}{K_{v}} \quad\therefore\quad K_{v}= 100$$
Using the final value theorem 
$$K_{v}= \lim_{s \rightarrow 0} \left(s\frac{k}{s^{2}+11s}\right) = \frac{k}{11} \quad\therefore\quad k= 1100$$
## 2.3 - Does the calculated value for $K$ meets the criteria for stability?
2024-01-14 @ 17:09 
Factoring the value of $k$ found in [[#2.2 - Design the value of $K$ so that for an input $100tu(t)$, there will be a 1% steady-state error|2.2]] $k=1100$ into the closed loop transfer function identified in [[#2.1 - Find the system transfer function.|2.1]]  $$\frac{1100}{s^{2}+11s +1100}$$The poles can be identified by solving for singularities in other words solving for $s$ where the denominator is $0$
$$s^{2}+11s +1100 =0$$
$$s = \frac{-1}{2} i \sqrt{4279} \pm 11 i) \approx -5.5 \pm 32.707i$$
As the real component of the roots is negative the system should be stable.
## 2.4 - Find the steady-state error in terms of K for the following inputs: $100𝑟(𝑡)$, $100𝑡^{2}𝑟(𝑡)$ where $r(t)$ is a step input and comment on the results.
2024-01-14 @ 18:31 
The open loop transfer function $\frac{k}{s^{2}+11s}$ is a type one system given this we can determine that:
1. $100𝑟(𝑡)$ being a step input will have $e_{ss}=0$ it will settle to the exact position
2. $100𝑡^{2}𝑟(𝑡)$ being equivalent to a parabolic input will have $e_{ss} = \infty$, the error will increase indefinitely

# 3
It is desired to develop a policy for drug delivery to maintain the virus count at prescribed levels. For the purpose of obtaining an appropriate $𝑢1$, the feedback shown in Figure 3 will be used. As a first approach, consider $𝐺(𝑠) = 𝐾$, a constant to be selected. **Use the Routh – Hurwitz criterion to find the range of the gain K to keep the closed loop system stable**. The HIV (AIDS) linearized model can be shown to have the following transfer function:
###### Transfer function
$$P(s) = \frac{-520s - 10.3844}{ s^3 + 2.6817s^2 + 0.11s + 0.0126}$$
###### Figure 3
![[Pasted image 20240114221858.png]]
### Resources
https://www.youtube.com/watch?v=S0_Hd5M7aJY
## Answer
The total transfer function of [[#Figure 3]] is:
$$\frac{G\times P(s)}{1+ G\times P(s)} = \frac{K \times\frac{-520s - 10.3844}{ s^3 + 2.6817s^2 + 0.11s + 0.0126}}{(1+K \times \frac{-520s - 10.3844}{ s^3 + 2.6817s^2 + 0.11s + 0.0126})}$$
Simplifying
$$=\frac{-520sK - 10.3844K}{ (s^3 + 2.6817s^{2} + 0.11s + 0.0126)-520sK - 10.3844K}$$
Collecting like terms: 
$$=\frac{(-520K)s - 10.3844K}{ s^3 + 2.6817s^{2} + (0.11-520K)s + (0.0126 - 10.3844K)}$$
Using the denominator in R H array to find the range of $K$ for which the system is stable:

| $s^3$ | $1$ | $(0.11-520K)$ |
| ---- | ---- | ---- |
| $s^2$ | $2.6817$ | $(0.0126 - 10.3844K)$ |
| $s^1$ | $\frac{(0.11-520K)\times(2.6817)-(0.0126 - 10.3844K)}{2.6817}$ |  |
| $s^0$ | $\frac{\frac{(0.11-520K)\times(2.6817)-(0.0126 - 10.3844K)}{2.6817} \times (0.0126 - 10.3844K)}{\frac{(0.11-520K)\times(2.6817)-(0.0126 - 10.3844K)}{2.6817}}$ |  |
Simplifying the last two equations
$$\frac{(0.11-520K)\times(2.6817)-(0.0126 - 10.3844K)}{2.6817} = 0.105301 - 516.128 K$$ 
$$\frac{\frac{(0.11-520K)\times(2.6817)-(0.0126 - 10.3844K)}{2.6817} \times (0.0126 - 10.3844K)}{\frac{(0.11-520K)\times(2.6817)-(0.0126 - 10.3844K)}{2.6817}} = 0.0126 - 10.3844K$$

| $s^3$ | $1$ | $(0.11-520K)$ |
| ---- | ---- | ---- |
| $s^2$ | $2.6817$ | $(0.0126 - 10.3844K)$ |
| $s^1$ | $0.105301 - 516.128K$ |  |
| $s^0$ | $0.0126 - 10.3844K$ |  |
For the system to be stable the first column of the R H array must all be the same side of the y axis, therefore;
$$\matrix{0.105301 - 516.128K \ge 0 \implies K\le0.000204021\\ 0.0126 - 10.3844K \ge 0 \implies K\le0.00121336 \\ \therefore \\K\le0.000204021}$$
# 
+-