
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

Performing these substitutions to on [Equation 7](Q1i.md#^Equation7-PTFilterTF) found in the the previous section and simplifying gives the following $z$-domain transfer function. For the full method see appendix ! %% add appendix %%


$$
\begin{align*}
H(s) &= \frac{\omega_b^2}{s^2 + \sqrt{2} \omega_b s + \omega_b^2} \\
s &= \frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
\end{align*}
$$
