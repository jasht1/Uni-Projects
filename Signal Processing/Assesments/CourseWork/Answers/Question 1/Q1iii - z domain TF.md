
### Converting to a z-domain Transfer Function

%% Explainer about s vs z domains %%

An $s$-domain transfer function can be mapped to the $z$-domain via the [following substitution (left)](#^Equation1-sTozDomainMap) that maps the infinite analogue frequency axis $j\omega$ of the $s$-domain onto the unit circle $z = e^{j\Omega}$ of digital frequency in the $z$-domain. However, having to fit the entire -ve half of the $s$-domain into the unit circle warps the frequency scale especially effecting higher frequency information. This warping can be reduced by pre-warping the frequencies with the [following substitution (right)](#^Equation2-FrequencyPreWarp).

|

$$s = \frac{2}{T} \cdot 1 - \frac{z^{-1}}{1 +z^{-1}}$$
^Equation1-sTozDomainMap

|

$$\omega{'} = \frac{2}{T} \cdot \tan\left( \frac{\omega T}{2} \right)$$
^Equation2-FrequencyPreWarp

|

Performing these substitutions to on [Equation 7](Q1i%20-%20s%20domain%20TF.md#^Equation7-PTFilterTF) found in the the previous section and simplifying gives the following $z$-domain transfer function. For the full method with a detailed walk through see appendix ! %% add appendix
[Q1iii - full method](Q1iii%20-%20full%20method.md)%%

$$
\begin{align*}
\text{pre-warp}\\
H(s) &= \frac{\omega_b{^2}}{s^2 + \sqrt{2} \omega_b s + \omega_{b}{^2}} \to \frac{\omega_b'{^2}}{s^2 + \sqrt{2} \omega_b' s + \omega_b'{^2}}\\

\text{bilinear transform}\\
H(z) &= \frac{\omega_b'{^2}}{\left(\frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}} \right)^{2} + \sqrt{2} \omega_b' \cdot \left(\frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}} \right) + \omega_b'{^2}} \\

\text{cancel out complex}\\
\text{fractions} \qquad\ \\
H(z) &= \frac{\omega_b'{^2}}{\left(\frac{2}{T}\right)^2 \frac{(1 - z^{-1})^2}{(1 + z^{-1})^2} + \sqrt{2} \omega_b' \cdot \left(\frac{2}{T}\right) \cdot \frac{(1 - z^{-1})}{(1 + z^{-1})} + \omega_{b'{^2}}} \times \frac{(1 + z^{-1})^2}{(1 + z^{-1})^{2}} \\

\text{expand polynomials}\\
H(z) &= \frac{\omega_b'{^2} (1 + 2z^{-1} + z^{-2})}
{
\left(\frac{2}{T}\right)^2 + \sqrt{2} \omega_b' \cdot \frac{2}{T} + \omega_b'{^2} 
+ \left[-2\left(\frac{2}{T}\right)^2 + 2\omega_b'{^2}\right]z^{-1} 
+ \left[\left(\frac{2}{T}\right)^2 - \sqrt{2} \omega_b' \cdot \frac{2}{T} + \omega_b'{^2}\right]z^{-2}
}\\\\

\text{aprox numerical}\\
\text{values} \qquad\\
H(z) &\approx \frac{0.0675 + 0.1350 z^{-1} + 0.0675 z^{-2}}{1 - 1.2765 z^{-1} + 0.4129 z^{-2}}
\end{align*}
$$
