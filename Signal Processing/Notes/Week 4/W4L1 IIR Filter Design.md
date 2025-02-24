---
tags:
  - "#Lecture_Notes"
---
## Truth Table
%%[[2025-02-20]] @ 09:18%%

analogue domain
| Laplace | Time | 

| $X(s)$ | x(t) | x


![](Pasted%20image%2020250220092736.png)

2 2
(s+a) +o;
| $X(s)$ | $x(t)$ | $x[nT]$ | $Normalised X(2)$ |
| - | - | - |

x[n]
1 Impulse Impulse Impulse 1
(1) 5[nT] 5[n]
Delayed Impulse Delayed Impulse z™"
3(n-m)T] 3[n-m]
1 Unit step Unit step Unit step oz
s u(t) u[nT] un] z-1
1 Ramp Ramp Ramp _z
5? t nT n (z-1)?
1 et il - z
sta Z-a
a 1-et 1-eoT 1-0" z(1-a)
s(s+a) (z-)(z-a)
, Sin(wct) Sin(wcnT) Sin(wdn) zsinw,
SS +] Zz" —2zcosw, +1
Ss Cos(act) Cos(wcnT) Cos(wdn) z(z—cos®,)
SS +] Zz" —2zcosw, +1
(s+a) e“'Cos(act) e""Cos(wcnT) a"Cos(wdn) 2(z—acosw,)
(s+a)’ +o! z* —2zacosw, +a’
, e*Sin(act) e"Sin(wnT) a"Sin(wdn) zasinw,

z* —2zacosw, +a’

 

 
Filter
$x(T) = 4.7e^{-4.5nT} - 4.7e^{-111nT}$
$T = 0.002$
$ha (t) = h_{d}[nT] = 4.7e^{-4.5nT} - 4.7e^{-111nT}$
$ha (t) = 4.7e^{-4.5n\times 0.002} - 4.7e^{-111n\times 0.002}$
$ha (t) = 4.7(e^{-4.5 \times 0.002})^{n} - 4.7(e^{-111\times 0.002})^{n}$

Impulse invariant = Z transform
$\frac{Y(z^{-1})}{x(z^{-1})}$

$Y(z^{-1}) = 4.7(\alpha_{1}-\alpha_{2})z^{-1}X(z^{-1})$

$y[n] = (\alpha_{1}-\alpha_{2})y[n-1] +$

https://blackboard.lincoln.ac.uk/ultra/stream


Bi-linear transform converts an analog filter $H_{a}(s)$ to a transfer function $H(z) = \frac{2}{T}\frac{z-1}{z+1}$
$$z = \frac {1+sT/2}{1-sT/2}$$


$$\omega _{c} = \frac{2}{T} \tan \left( \frac{\omega_{d}}{2}\right)$$
At small angles $\tan(x) = x$, thus at low frequencies

$$\omega_{c}= \frac{\omega_{d}}{T}$$

The inaccuracy of this approximation means that digital approximations are most accurate at low frequencies and less so as at higher frequencies. However this can be avoided by pre warping the critical frequencies. 

$$\omega_{c}^{\text{warped}}= \frac{2}{T} \tan \left( \frac{\omega_{c}}{2} \right)$$



