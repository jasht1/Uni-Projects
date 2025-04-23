### S domain Transfer Function

The ideal behaviour of a low pass filter is to reject frequencies ($\omega$) above the cut off ($\omega _{b}$) while admitting frequencies below it without distortion. The power gain ($|H(j\omega)|^{2}$), defined as the magnitude of the frequency response ($H(j\omega$) squared, should ideally resemble a sharp edged brick wall as given by [Equation 1](#^Equation1-BrickWall).

$$\Large |H(j\omega)|^{2} = \begin{cases}
\omega \le \omega_{b} : 1 \\
\omega \gt \omega_{b} : 0
\end{cases}$$
^Equation1-BrickWall

This desirable brick wall response was approximated for simple staged filter amplifiers by Butterworth in 1930, with [equation 2 (left)](#^Equation2-GeneralButterworthPowerResponse) where $n$ is the number of filter stages. Given the case of a 2 stage filter ($n = 2$) and a cut off frequency of $\omega_{b} = 5 \frac{\text{rad}}{\text{sec}}$ beyond which point signals should be reduced by at least $-3 \ \text{dB}$, the power gain function becomes [Equation 3 (right)](#^Equation3-PtypeButterworthPowerResponse).

| 

$$\Large |H(j\omega)|^{2} = \frac{1}{1 + \left( \frac{\omega}{\omega_{b}} \right)^{2n}}$$
^Equation2-GeneralButterworthPowerResponse

| 

$$\Large |H(j\omega)|^{2} = \frac{1}{1 + \left( \frac{\omega}{5} \right)^{4}}$$
^Equation3-PtypeButterworthPowerResponse

|

The $s$-domain transfer function equivalent for [Equation 3](#^Equation3-PtypeButterworthPowerResponse) can be designed by pole placement as the poles ($s_{k}$) of of a Butterworth filter lie evenly spaced across the left hand plane of a circle of radius $r = \omega_{b}$ according to [Equation 4 (left)](#^Equation4-GeneralButterworthPoles). In the case of a 2 stage filter the poles will be those shown in [Equation 5 (right)](#^Equation5-2StageButterworthPoleLocations).

|

$$\begin{align*}
& \text{for $k$ in $[0, n-1]$ :} \\ 
& \Large \quad s_{k} = \omega_{b} \cdot e ^{j \pi \left( \frac{2k + 1}{2n} \right)}
\end{align*}$$
^Equation4-GeneralButterworthPoles

|

$$\text{for $n = 2$ :} \quad
\large \begin{align*}
s_{0} &= \omega_{b} e^{j 3 \pi /4} \\
s_{1} &= \omega_{b} e^{j 5 \pi /4} \\
\end{align*}$$
^Equation5-2StageButterworthPoleLocations

|

The $s$-domain transfer function ($H(s)$) of any filter with Gain $A$ can be represented by [Equation 6 (left)](#^Equation7-PTFilterTF) by using the product of the poles as the denominator. Thus the prototype filter is given by [Equation 7 (right)](#^Equation7-PTFilterTF).

|

$$H(s) = \frac{A\omega_{b}{^n}}{\prod\limits^{n-1}_{k=0}(s-s_{k})}$$
^Equation6-GeneralFilterTF

|

$$H(s) = \frac{\omega_{b}{^2}}{s^{2} + \sqrt2 \omega_{b}s + \omega_{b}{^2}}$$
^Equation7-PTFilterTF

|

%% Refs

https://www.electronics-tutorials.ws/filter/filter_8.html

https://www.changpuak.ch/electronics/downloads/On_the_Theory_of_Filter_Amplifiers.pdf

%%