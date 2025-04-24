Beginning with [Equation 7](Q1i.md#^Equation7-PTFilterTF) for the 2 stage Butterworth low pass filter $s$-domain transfer function:

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

$$H(z) = \frac{\omega_b'{^2}}{\left(\frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}} \right)^{2} + \sqrt{2} \omega_b' \cdot \left(\frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}} \right) + \omega_b'{^2}}$$

$$H(z) = \frac{\omega_b'{^2}}{\left(\frac{2}{T}\right)^2 \frac{(1 - z^{-1})^2}{(1 + z^{-1})^2} + \sqrt{2} \omega_b' \cdot \left(\frac{2}{T}\right) \cdot \frac{(1 - z^{-1})}{(1 + z^{-1})} + \omega_{b'{^2}}} \times \frac{(1 + z^{-1})^2}{(1 + z^{-1})^{2}}$$
