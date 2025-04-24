Beginning with [Equation 7](Q1i%20-%20s%20domain%20TF.md#^Equation7-PTFilterTF) for the 2 stage Butterworth low pass filter $s$-domain transfer function:

$$H(s) = \frac{\omega_b^2}{s^2 + \sqrt{2} \omega_b s + \omega_b^2}$$

The frequency pre-warping substitution may be applied for a minor benefit in accuracy. The sampling period $T$ in seconds is based on the Butterworth cut-off frequency $\omega_{b}$ such that $\omega_{s} = 10 \times \omega_{b}$. The cutoff frequency $\omega_{b} = 5 \ \frac{\text{rad}}{\text{s}}$ gives the sampling frequency $\omega_{s} = 50 \ \text{rad}/\text{s}$ or $F_{s} = \frac{\omega_{s}}{2\pi} = 25/\pi \ \text{Hz}$. The sampling period being the reciprocal $T = \frac{1}{F_{s}} = \pi/25 \ \text{s}$.​

$$
\omega_{b}' = \frac{2}{T} \cdot \tan\left( \frac{\omega_{b} T}{2} \right) \quad \text{Where} \quad \begin{align*}
\omega_{b} &= 5 \\
T &= \pi/25
\end{align*} \quad \text{such that} \quad \omega_{b}' = \frac{50}{\pi} \cdot \tan\left( \frac{\pi}{10} \right) = 5.17125757634 \dots
$$

If deemed necessary this instead makes the starting point:

$$H(s) = \frac{\omega_b'{^2}}{s^2 + \sqrt{2} \omega_b' s + \omega_b'{^2}}$$

In either case the $s$ variable must be mapped to it's corresponding $z$ variable using the bilinear transform:

$$s = \frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}$$

Doing so gives a messy intermediary with many complex fractions but by considering the the powers factor-wise these can be eliminated by multiplying the numerator and denominator by $(1 + z^{-1})^2$:

$$
\begin{align*}
H(z) &= \frac{\omega_b'{^2}}{\left(\frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}} \right)^{2} + \sqrt{2} \omega_b' \cdot \left(\frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}} \right) + \omega_b'{^2}} \\\\

&= \frac{\omega_b'{^2}}{\left(\frac{2}{T}\right)^2 \frac{(1 - z^{-1})^2}{(1 + z^{-1})^2} + \sqrt{2} \omega_b' \cdot \left(\frac{2}{T}\right) \cdot \frac{(1 - z^{-1})}{(1 + z^{-1})} + \omega_{b'{^2}}} \times \frac{(1 + z^{-1})^2}{(1 + z^{-1})^{2}} \\\\

&= \frac{\omega_b'{^2} (1 + z^{-1})^2} { \left(\frac{2}{T}\right)^2 (1 - z^{-1})^2 + \sqrt{2} \omega_b' \frac{2}{T} (1 - z^{-1})(1 + z^{-1}) + \omega_b'{^2} (1 + z^{-1})^2 }
\end{align*}
$$

Expanding the remaining polynomials:

$$
\begin{align*}

(1 + z^{-1})^2 
&= 
1 + 2z^{-1} + z^{-2} \\\\

\frac{2}{T}^2 (1 - z^{-1})^2 
&= 
\frac{2}{T}^2 (1 - 2z^{-1} + z^{-2}) \\\\

\sqrt{2} \omega_b' \frac{2}{T} (1 - z^{-1})(1 + z^{-1}) 
&= 
\sqrt{2} \omega_b' \frac{2}{T} (1 - z^{-2}) \\\\

\omega_b'{^2} (1 + z^{-1})^2 
&= 
\omega_b'{^2} (1 + 2z^{-1} + z^{-2}) \\

\end{align*}
$$

Substituting back in at this point gives the most complete and accurate form:

$$H(z) = \frac{\omega_b'{^2} (1 + 2z^{-1} + z^{-2})}
{
\left(\frac{2}{T}\right)^2 + \sqrt{2} \omega_b' \cdot \frac{2}{T} + \omega_b'{^2} 
+ \left[-2\left(\frac{2}{T}\right)^2 + 2\omega_b'{^2}\right]z^{-1} 
+ \left[\left(\frac{2}{T}\right)^2 - \sqrt{2} \omega_b' \cdot \frac{2}{T} + \omega_b'{^2}\right]z^{-2}
}
$$

Considering the numerical values of variables:

$$\begin{align*}{}
& T = \pi/25 &\approx 0.125663706\\
& \omega_{b}' = 2/T \cdot \tan(5 T/2) &\approx 5.171257576 \\
& 2/T = 50/\pi &\approx 15.91549431 \\
& 2/T \cdot\omega_{b}' &\approx 82.30312053 \\
& \omega_{b}'{^{2}} &\approx 26.74190492
\end{align*}$$

The numerator and denominator can be approximated by sections as:

$$\begin{align*}
&\text{numerator}\\
& \omega_b'{^{2} (1 + 2z^{-1} + z^{-2})} \qquad \approx 26.74789+53.49578 z^{−1} + 26.74789 z^{−2} &\\\\

&\text{denominator}\\
& \left(\frac{2}{T}\right)^{2} + \sqrt{2} \omega_b' \cdot \frac{2}{T} + \omega_{b}'{^{2}} \approx 253.30296+1.4142⋅82.34737+26.74789 &\approx 395.9572 &\\\\

& -2\left(\frac{2}{T}\right)^{2} + 2\omega_b'{^2} \approx −2⋅253.30296+2⋅26.74789 &\approx −505.5581 &\\\\


& \left(\frac{2}{T}\right)^2 - \sqrt{2} \omega_b' \cdot \frac{2}{T} + \omega_b'{^2} \approx 253.30296−116.5343+26.74789 &\approx 163.5165 &\\

\end{align*}
$$

Substituting these values back into the $z$-domain function, it can be slightly visually simplified by dividing by $\omega_{b}'{^{2}}$.

$$\begin{align*}
H(z) &= \frac{26.74789 + 53.49578 z^{-1} + 26.74789 z^{-2}}{395.9572 - 505.5581 z^{-1} + 163.5165 z^{-2}} \div \frac{26.74190492}{26.74190492}\\\\

H(z) &= \frac{1 + 2 z^{-1} + z^{-2}}{14.8065 - 18.9021 z^{-1} + 6.1138 z^{-2}}
\end{align*}$$

This is within rounding error of the answer given by MATLAB using the symbolic math Toolbox 

```matlab title=pretty(Hz)
                                                                2
                                  2118711989009112341915 (z + 1)
-------------------------------------------------------------------------------
                         2
31409137742043248063909 z  - 35900032040745566142689 z + 12965742254738767446441
```

%%
```matlab
                                                                         2
                                  2118711989009112341915358986240 (z + 1)
-----------------------------------------------------------------------------------------------------------
                                  2
31409137742043248063909313259961 z  - 35900032040745566142689028749128 z + 12965742254738767446441151434127
```
%%