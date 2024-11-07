[[EGR2006M TCA_2022-2023.pdf]]
# 1
![[Pasted image 20240115011626.png]]
## 1.1 - open loop tf
2024-01-15 @ 01:16 
![[Q1.1.excalidraw|500]]
## 1.2
2024-01-15 @ 01:32 
3rd order 
type 1
## 1.3
2024-01-15 @ 01:33 
![[Q1.3.excalidraw|700]]
%% Error
Given the OLTF is type 0 the steady state error ($e_{ss}$) of a step input is given by $\frac{1}{1+K_p}$, where $K_{p}$ is the error constant given by applying the final value theorem ($\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$) to the derivative of the OLTF.
$$K_{p}=\lim_{s\to\infty}OLTF(s) = \frac{k11 +\frac{k}{0}}{2} = \infty$$
Factoring this into the above mentioned equation
$$e_{ss}= \frac{1}{ (1+\infty)}= \infty$$%%
Given the OLTF is type 1 the steady state error ($e_{ss}$) of a step input will be $0$ the system will eventually settle to the exact intended value.
Given the OLTF is type 1 the steady state error ($e_{ss}$) of a ramp input is given by $\frac{1}{k_v}$, where $K_{v}$ is the error constant given by applying the final value theorem ($\lim_{t\to\infty}x(t) = \lim_{s\to0}sX(s)$) to the derivative of the OLTF.
$$K_{V}=\lim_{s\to\infty}OLTF(s) = \frac{k}{0} = \infty$$
Factoring this into the above mentioned equation,
$$e_{ss} = \frac{1}{k_{v}} = \frac{1}{\infty}= 0 \quad \therefore \quad e_{ss}= 0$$
## 1.4
