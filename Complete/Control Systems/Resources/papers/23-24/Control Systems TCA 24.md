# 1
$$𝐺(𝑠) = \frac{𝑠 + 1} {𝑠^3 + 𝑠^2 + 𝑠}$$
## 1.1
2024-01-15 @ 13:33 

| Type | 1 |
| ---- | ---- |
| Order | 3 |

## 1.2
2024-01-15 @ 13:36 
$$𝐺(𝑠) = \frac{s + 1} {s(s^2 + s + 1)}$$
given it is a type 1 system here will be a pole at $0$.
the other poles are found by solving the polynomial $s^{2} + s + 1=0$ which gives roots at $$s = -(-1)^{\frac{1}{3}} \approx -0.50000 - 0.86603 i$$
## 1.3
###### Figure 1
![[Control Systems TCA 24 figure1.png]]
### 1.3.1
2024-01-15 @ 13:44 
The forward path transfer function $KG(s)$ is
$$KG(𝑠) = \frac{K(s + 1)} {s(s^2 + s + 1)}$$
The closed loop transfer function is 
$$\frac{KG(s)}{1+KG(s)}= \frac{K(s + 1)} {s(s^2 + s + 1)+K(s + 1)}$$
### 1.3.2
2024-01-15 @ 13:50 
$𝑟(𝑡) = 1(𝑡)$ is effectively just a standard step input and given the OLTF is type 1 the steady state error ($e_{ss}$) of a step input will be $0$ the system will eventually settle to the exact intended value. 
$$e_{ss}= 0$$
### 1.3.3
2024-01-15 @ 13:52 
$𝑟(𝑡) = 𝑡 1(𝑡)$ is effectively a ramp input and given the OLTF is type 1 the steady state error ($e_{ss}$) of a ramp input is given by $\frac{1}{k_v}$, where $K_{v}$ is the error constant given by applying the final value theorem ($\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$) to the derivative of the OLTF.
$$K_{V}=\lim_{s\to\infty}s\times OLTF(s) = \frac{K((0) + 1)} {(0)^{2} + (0) + 1}=K$$
Factoring this into the above mentioned equation,
$$e_{ss} = \frac{1}{k_{v}} = \frac{1}{K}$$
### 1.3.4
2024-01-15 @ 13:57 
Given that:
$K=20$
gives a CLTF of
$$CLTF = \frac{20s + 20} {s(s^2 + s + 1)+20(s + 1)}$$
#### Settling time
We can approximate the settling time $(T_s)$ with the formula:
$$T_{s}​ \approx \frac{-P_{(imaginary)} \times 4}{P_{(real)} \times\omega_{n}}​$$
For which we must first identify the poles;
Taking the characteristic equation
$$s(s^2 + s + 1)+20(s + 1)$$
and collecting like terms
$$s^{3} + s^{2} + 21s + 20$$
then finding the roots
$$\matrix{s^{3} + s^{2} + 21s + 20 = 0 
\\ \therefore
\\ s \approx -0.95436
\\ s \approx -0.0228 \pm 4.5778 i}$$
Now the natural frequency $\omega_{n}$ can be identified
$$\omega_{n}​=\sqrt{P_{(real)}^{2}+P_{(imaginary)}^{2}}​$$
With this we can calculate the settling time $(T_s)$ for all the roots and identify which has the dominant impact
$$T_{s}​ \approx \frac{-P_{(imaginary)} \times 4}{P_{(real)} \times \sqrt{P_{(real)}^{2}+P_{(imaginary)}^{2}}}​$$
##### Root 1 $s \approx -0.95436$
$$T_{s}​ \approx \frac{0 \times 4}{-0.95436 \times \sqrt{-0.95436^{2}+0}} \approx \infty​$$
First root lies on the x axis so it would make the system critically undamped giving an effectively infinite settling time however this is not the dominant pole so will be counteracted by the faster behaviour determined by root 2.
##### Root 2 $s \approx -0.0228 \pm 4.5778 i$
the 2% settling time is found by
$$T_{s}​ \approx \frac{-4.5778 \times 4}{-0.0228 \times \sqrt{-0.0228^{2}+4.5778^{2}}}​$$
$$T_{s}​ \approx  175.44$$
a 5% settling time can be found by changing the 4 to a 3 giving:
$$T_{s}​ \approx  131.58$$
#### Overshoot
Overshoot ratio can be found by the formula
$$e^{-\zeta\pi/\sqrt{1- \zeta^{2}}}$$
factoring in the damping ratio with the values for the dominant pole
$$e^{\frac{-0.0228\pi}{4.5778\sqrt{1- \frac{-0.0228}{4.5778}^{2}}}} = 0.9844747...$$

#### Conclusion
This gain may be appropriate for some applications but the settling time will be far to high for many situations and the overshoot is nearly 100% meaning the system over corrects by double its desired response.
# 2
$$𝐺(𝑠) = \frac{s + 2}{ s3 + 5s^{2} + 11s + 15}$$
###### Figure 2
![[Control Systems TCA 24 figure 2.png]]
## 2.1
2024-01-15 @ 14:53 
$$OLTF = K(s+1) G(s) = \frac{K(s+1) (s + 2)}{ s^{3} + 5s^{2} + 11s + 15}$$
simplify
$$= \frac{K(s^2+3s+2)}{s^{3} + 5s^{2} + 11s + 15}$$
Solve characteristic equation to find poles
$$\matrix{
s^{3} + 5s^{2} + 11s + 15 = 0
\\ \therefore
\\ s = -3
\\ s = -1 \pm 2 i }$$
solving for zeros
$$\matrix{s^{2}+3s+2 = 0
\\ \therefore
\\ s = -1
\\ s = -2}$$
## 2.2
2024-01-15 @ 15:04 
![[Q22 root locus plot.excalidraw]]
## 2.3
2024-01-15 @ 15:16 
As the imaginary axis is never crossed all values of $K$ will be stable
# 3 - skipped
# 4 
###### Figure 4
![[Control Systems TCA 24 figure 4.png]]
## 4.1
2024-01-15 @ 15:24 
![[Q41 diagram.excalidraw]]
solve $G_{1}$
$$G_{1}(t) = \frac{10}{0.1s^{2}+s}$$
solve $G_{2}$
$$G_{2}= \frac{G_{1}}{1+G_{1}}= \frac{10}{0.1s^{2}+s+10}$$
solve $G_{3}$
$$\begin{align}
G_{3}= G_{2}\times\frac{1+s}{s^{2}+1}&= \frac{10+10s}{0.1s^{4}+s^{3}+10s^{2}+0.1s^{2}+S+10}\\ \\&= \frac{10+10s}{0.1s^{4}+s^{3}+10.1s^{2}+S+10} \end{align}$$
solve $T(s)$
$$T(s) = \frac{G_{3}}{1+G_{3}}= \frac{10s+10}{0.1s^{4}+s^{3}+10.1s^{2}+11S+20}$$
## 4.2
2024-01-15 @ 15:44 
Find poles by solving characteristic equation (with calculator):
$$\matrix{0.1s^{4}+s^{3}+10.1s^{2}+11s+20=0
\\ s \approx -4.4989 \pm 8.3375 i
\\ s≈-0.5011 \pm 1.4061 i}$$
## 4.3
2024-01-15 @ 15:52 
The dominant poles are at $s≈-0.5011 \pm 1.4061 i$
### Settling time
We can approximate the 2% settling time $(T_s)$ with the formula:
$$T_{s}​ \approx \frac{-P_{(imaginary)} \times 4}{P_{(real)} \times \sqrt{P_{(real)}^{2}+P_{(imaginary)}^{2}}}​$$
Factoring the dominant pole values into the formula & solving
$$T_{s}​ \approx \frac{-1.4061 \times 4}{-0.5011 \times \sqrt{-0.5011^{2}+1.4061^{2}}}​ = 8.54337...$$
We can also solve for the 5% settling time by changing the 4 to a 3 giving
$$T_{s}\approx 6.40753...$$
### Overshoot ratio
Overshoot ratio can be found by the formula
$$e^{-\zeta\pi/\sqrt{1- \zeta^{2}}}$$
factoring in the damping ratio with the values for the dominant pole
$$\text{overshoot ratio} = e^{\frac{-0.5011\pi}{1.4061\sqrt{1- \frac{-0.5011}{1.4061}^{2}}}} = 0.301718...$$
### Conclusion
Depending on the application the settling time is likely the greatest deficiency of this system, time sensitive applications would need it be be significantly faster.
## 4.4
2024-01-15 @ 17:09 
converting the input signal to the time domain
$$\mathscr{L} \{cos(ωt)\}=\frac{s}{s^{2}+ω^{2}}​$$
Multiply the time domain input signal by the CLTF
$$\begin{align}
Y(s) &= \frac{s}{s^{2}+ω^{2}}\times 
\frac{10s+10}{0.1s^{4}+s^{3}+10.1s^{2}+11S+20} 
\\ \\&= 
\frac{10s^{2}+10s}{(s^{2} + \omega^{2}) (0.1s^{4}+s^{3}+10.1s^{2}+11S+20)} 
\\ \\&= 
\frac{10s^{2}+10s}{0.1s^{6}+s^{5}+10.1s^{4}+11s^{3}+20s^{2}
+0.1\omega ^{2}s^{4}+\omega ^{2}s^{3}+10.1\omega ^{2}s^{2}+11\omega ^{2}s+20\omega ^{2}}
\\ \\&= 
\frac{10s^2 + 10s}{0.1s^6 + s^5 + (10.1 + 0.1\omega^2)s^4 + (11 + \omega^2)s^3 + (20 + 10.1\omega^2)s^2 + 11\omega^2s + 20\omega^2}
\end{align}$$
This gives the following coefficients of $s$
$$\begin{align*} &0 &\text{ (coefficient of } s) \\ &20 + 10.1\omega^2 &\text{ (coefficient of } s^2) \\ &11 + \omega^2 &\text{ (coefficient of } s^3) \\ &10.1 + 0.1\omega^2 &\text{ (coefficient of } s^4) \\ &1 &\text{ (coefficient of } s^5) \\ &0.1 &\text{ (coefficient of } s^6) \end{align*}$$
Breaking into partial fractions
$$=\frac{10s^2 + 10s}{0.1s^6 + s^5 + (10.1 + 0.1\omega^2)s^4 + (11 + \omega^2)s^3 + (20 + 10.1\omega^2)s^2 + 11\omega^2s + 20\omega^2}
$$
$= \frac{A}{s} + \frac{B}{s^2} + \frac{Cs + D}{0.1s^2 + (10.1 + 0.1\omega^2)s + 11 + \omega^2} + \frac{Es + F}{0.1s^2 + (10.1 + 0.1\omega^2)s + 11 + \omega^2} + \frac{Gs + H}{0.1s^2 + (10.1 + 0.1\omega^2)s + 11 + \omega^2}$
determine the constants A, B, C, D, E, F, G, H by equating coefficients
`This is way too much work there must be another way`
let $D(s)$ be the denominator of the CLTF and $N(s)$ be the numerator
$$\begin{align}
(10s^2 + 10s) = & A \cdot (0.1s^6 + s^5 + (10.1 + 0.1\omega^2)s^4 \\
& + (11 + \omega^2)s^3 + (20 + 10.1\omega^2)s^2 \\
& + 11\omega^2s + 20\omega^2) + Bs + (Cs + D) \cdot (0.1s^2 \\
& + (10.1 + 0.1\omega^2)s + 11 + \omega^2) + (Es + F) \cdot (0.1s^2 \\
& + (10.1 + 0.1\omega^2)s + 11 + \omega^2) + (Gs + H) \cdot (0.1s^2 \\
& + (10.1 + 0.1\omega^2)s + 11 + \omega^2)
\end{align}
$$
`no I acctualy can't do this theres no way this is how your supposed to answer this`
`I could definitely make life easier by factoring out $\omega =2$`
Factoring out $\omega$
$$\begin{align*}
(10s^2 + 10s) = & A \cdot (0.1s^6 + s^5 + (10.1 + 0.1(2)^2)s^4 \\
& + (11 + (2)^2)s^3 + (20 + 10.1(2)^2)s^2 \\
& + 11(2)^2s + 20(2)^2) + Bs + (Cs + D) \cdot (0.1s^2 \\
& + (10.1 + 0.1(2)^2)s + 11 + (2)^2) + (Es + F) \cdot (0.1s^2 \\
& + (10.1 + 0.1(2)^2)s + 11 + (2)^2) + (Gs + H) \cdot (0.1s^2 \\
& + (10.1 + 0.1(2)^2)s + 11 + (2)^2)
\end{align*}
$$
$$\begin{align*}
(10s^2 + 10s) = & A \cdot (0.1s^6 + s^5 + 10.5s^4 + 15s^3 + 40s^2 + 44s + 80) \\
& + Bs + (Cs + D) \cdot (0.1s^2 + 10.5s + 15) \\
& + (Es + F) \cdot (0.1s^2 + 10.5s + 15) + (Gs + H) \cdot (0.1s^2 + 10.5s + 15)
\end{align*}
$$
`I should have done that at the start :facepalm`
`still not solvable think its time to give up 2024-01-15 @ 18:33 ` 

Take the inverse Laplace transform of $Y(s)$ to find output in time domain

using the identity:
$$\mathscr{L}^{-1} \left\{\frac{s \cos \phi − ω \sin \phi }{s2 + ω2}\right\}  = cos(ωt + \phi)$$
# 5
###### Figure 5
![[Control Systems TCA 24 figure 5.png]]
## 5.1
2024-01-15 @ 16:25 
### Finding the OLTF
$$OLTF = \frac{K(s+1)^{2}}{s^{3}+10s^{2}+s}$$
### Finding poles
Find poles by solving the characteristic equation
$$\matrix{s^{3}+10s^{2}+s =0
\\ \therefore
\\ s =0
\\ s = -5 \pm 2\sqrt{6}}$$
### Finding zeros
$$\matrix{0= (s+1)^{2}
\\ \therefore
\\ s = -1}$$
## 5.2
2024-01-15 @ 16:32
$$CLTF = \frac{OLTF}{1+OLTF} = \frac{K(s^{2}+2s+1)}{s^{3}+10s^{2}+s+K(s^{2}+2s+1)}$$
## 5.3
2024-01-15 @ 16:38 

| Analysis technique | Open vs Closed loop tf |
| ---- | ---- |
| Root locus | OLTF |
| Gain margin | OLTF |
| Routh array | CLTF (potentially OLTF also) |
## 5.4
2024-01-15 @ 16:43 
Given that 
$$CLTF = \frac{K(s^{2}+2s+1)}{s^{3}+10s^{2}+s+K(s^{2}+2s+1)}$$
collecting like terms
$$CLTF = \frac{Ks^{2}+2Ks+K)}{s^{3}+(10 + K)s^{2}+(1+2K)s+K}$$
Add coefficients to RH array 

| $s^3$ | $1$ | $(1+2K)$ |
| ---- | ---- | ---- |
| $s^2$ | $(10+K)$ | $K$ |
| $s^1$ | $a_1$ | $a_2$ |
| $s^0$ | $b_1$ | $b_2$ |
Solve rest of array 
$$a_{1}= \frac{(10+K)(1+2K)-K}{(10+K)} = 2K-\frac{K}{10+K}+1$$
$$a_{2}= \frac{k(2K-\frac{K}{10+K}+1)-0}{2K-\frac{K}{10+K}+1} = K$$

| $s^3$ | $1$ | $(1+2K)$ |
| ---- | ---- | ---- |
| $s^2$ | $(10+K)$ | $K$ |
| $s^1$ | $\frac{(10+K)(1+2K)-K}{(10+K)}$ | $0$ |
| $s^0$ | $K$ | $0$ |
To satisfy RH stability criteria every cell in the first column must be on the same side of the y axis.
Given that the fist cell is positive the value of the 3 equations containing $K$ must also be positive.
Using this information we can solve for a range of $K$.
$$
\begin{align}
0 \le 10+K &\implies K \le10
\\
\\ 0 \le \frac{(10+K)(1+2K)-K}{(10+K)} &\implies 
	\cases{
	-10 \lt K \le - 5 -2 \sqrt{5}
	\\  2 \sqrt{5} - 5 \le K
	}
	\\
\\0 \le K &\implies 0 \le K
\end{align}
$$
Eliminating superfluous cases gives us a range of $K$
$$0 \le K\le10$$