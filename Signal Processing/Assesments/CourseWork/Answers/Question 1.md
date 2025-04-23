
## Question 1

> [!question]- [Question 1 (60 marks)](Projects/Uni%20Projects/Signal%20Processing/Assesments/CourseWork/Brief.md#Question%201%20(60%20marks))
> ![Question 1 (60 marks)](Projects/Uni%20Projects/Signal%20Processing/Assesments/CourseWork/Brief.md#Question%201%20(60%20marks))

### S domain TF

The ideal behavior of a low pass filter is to admit frequencies ($\omega$) below the cut off ($\omega _{b}$) without distortion while rejecting frequencies above it. The power gain ($|H(j\omega)|^{2}$), being the absolute ratio of input to output e.m.f, should be like a sharp edged brick wall.

$$\Large |H(j\omega)|^{2} = \begin{cases}
\omega \le \omega_{b} : 1 \\
\omega \gt \omega_{b} : 0
\end{cases}$$

This desirable brick wall response was approximated for simple staged filter amplifiers by Butterworth in 1930, with [equation 2 (left)](#^Equation2-GeneralButterworthPowerResponse) where $n$ is the number of filter stages. Given the case of a 2 stage filter ($n = 2$) and a cut off frequency of $\omega_{b} = 5 \frac{\text{rad}}{\text{sec}}$ beyond which point signals should be reduced by at least $-3 \ \text{dB}$, the power gain function becomes [Equation 3 (right)](#^Equation3-PtypeButterworthPowerResponse).

| 

$$\Large |H(j\omega)|^{2} = \frac{1}{1 + \left( \frac{\omega}{\omega_{b}} \right)^{2n}}$$  ^Equation2-GeneralButterworthPowerResponse

| 

$$\Large |H(j\omega)|^{2} = \frac{1}{1 + \left( \frac{\omega}{5} \right)^{4}}$$ ^Equation3-PtypeButterworthPowerResponse

|

The $s$ domain transfer function equivalent for [Equation 3](#^Equation3-PtypeButterworthPowerResponse) can be designed by pole placement as the poles of of a Butterworth filter lie evenly spaced across the left hand plane of a circle of radius $r = \omega_{b}$ according to [[|Equation 4]]. 




%% $|H(j\omega)|^{2} @(\omega = \omega_{b}) = \frac{1}{\sqrt{2}} \approx -3.01$ ← represent this more clearly %%

%% explain how pole placement works %%


https://www.electronics-tutorials.ws/filter/filter_8.html

https://www.changpuak.ch/electronics/downloads/On_the_Theory_of_Filter_Amplifiers.pdf