
The digital systems represented by $z$-domain transfer functions operate in discrete time samples unlike a continuous $s$-domain representation. Given that the $z$ variable is $z = r \cdot e^{i\omega}$ then $z^{-n}$ can be expressed as:
$$z^{-n} = (r \cdot e^{i\omega})^{-n} = e^{-i\omega n} \times r^{-n}$$
with $e^{-i\omega\color{red}n}$ shifting the phase and $r^{\color{red}n}$ scaling the amplitude so that the coefficients of each $z^{-n}$ term represent the influence of a sample from $n$ sampling periods ago.
The difference equation uses this property to give a recursive relationship that predicts the system output $y[n]$ for a given set of input samples $x[n]$. This can be found by collecting the $z$-domain transfer function into $z^{-n}$ terms. 

$$\begin{align*}
H(z) = \frac{Y(z)}{X(z)} &= \frac
{a_{0} + a_{1} z^{-1} +a_{2} z^{-2}\dots}
{1 - b_{1} z^{-1} + b_{2} z^{-2}\dots}\\
&\downarrow &\times X(z)\\
Y(z) (1 - b_{1} z^{-1} + b_{2} z^{-2}) &= X(z) (a_{0} + a_{1} z^{-1} + a_{2} z^{-2})\\
\end{align*}$$
These coefficients can be used directly in difference equation based on the mapping:
$$ \begin{align*}
z^{-1} Y(z) \to&\ y[n-1] & z^{-1} X(z) \to&\ x[n-1] \\
z^{-2} Y(z) \to&\ y[n-2] & z^{-2} X(z) \to&\ x[n-2] \\

\dots && \dots
\end{align*} $$

$$y[n] = \left( a_{0} \ x[n] + a_{1} \ x[n-1] + a_{2} \ x[n-2] \dots \right)
- \left( b_{1} \ y[n-1] + b_{2} \ y[n-2]\dots \right)$$

For the case of the butterworth $z$-domain filter found previously this is:
$$ H(z) = \frac{0.0675 + 0.1350 z^{-1} + 0.0675 z^{-2}}{1 - 1.2765 z^{-1} + 0.4129 z^{-2}} $$
$$y[n] = 0.0675 x[n] + 0.1350 x[n-1] + 0.0675 x[n-2] + 1.2765 y[n-1] - 0.4129 y[n-2]$$
