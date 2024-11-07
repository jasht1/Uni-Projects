# Laplace Transform
An integral transform that determines the sinusoidal and exponential components of a function.
Converts frequency domain functions to time domain functions 

where $\mathscr{L} \{f(t)\}=F(s)$
$$ F(S) = \int_{-\infty}^\infty {f(t)e^{-st}}dt$$
Integral kernel $S$ is the combination of the exponential & sinusoidal components making it it a complex variable with a real & imaginary component respectively.
$$ S = \sigma + j\omega $$
where $\sigma$ is the damping factor determining the change in oscillation over time & $\omega$ is the angular frequency determining the speed of the oscillation.
## Truth table
![[laplace-truth-table.pdf]]
### Signal transforms truth table
| Signal type | signal          | Laplace Transform             |
| ----------- | --------------- | ----------------------------- |
| impulse     | $\delta(t)$     | 1                             |
| step        | $1$             | $\frac{1}{S}$                 |
| ramp        | $t$             | $\frac{1}{S^2}$               |
| integral    | $t^n$           | $\frac{n!}{S^{n+1}}$           |
| exponential | $e^{at}$       | $\frac{1}{S-a}$               |
| Sinusoidal            | $cos(\omega t)$ | $\frac{S}{S^2+\omega^2}$      |
| Sinusoidal            | $sin(\omega t)$ | $\frac{\omega}{S^2+\omega^2}$ |
## Videos
[Intuition 3b1b](https://www.youtube.com/watch?v=EW08rD-GFh0)
[Overall theory Zach Star](https://youtu.be/n2y7n6jw5d0)
[Brian Douglas](https://www.youtube.com/watch?v=ZGPtPkTft8g&list=PLUMWjy5jgHK3j74Z5Tq6Tso1fSfVWZC8L&index=5)
## Inverse laplace transform
$$ f(t) = $$ #WIP 
