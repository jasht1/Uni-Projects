
## Sources
%%[[2025-02-19]] @ 15:29%%

[Lecture Audio](https://blackboard.lincoln.ac.uk/ultra/courses/_200914_1/outline/file/_9913982_1)

### Videos
#### [Brian Douglas](https://www.youtube.com/@BrianBDouglas)

[Z transform](https://www.youtube.com/watch?v=XJRW6jamUHk) [@matlab2023-UnderstandingZTransform]
[Z domain](https://www.youtube.com/watch?v=7Gl4kJUjp4c) [@matlab2024-UnderstandingZPlane]

### [Youngmoo Kim](https://www.youtube.com/@youngmoo-kim)

[z domain filter design](https://www.youtube.com/watch?v=xIN5Mnj_MAk) [@youngmookim2021-AppliedDSPNo9]

## Z
%%[[2025-02-19]] @ 15:36%%

$z$ is simply an identity / function for mapping $r$ a real number and $i$ an imaginary component. 
$$\LARGE z = r \cdot e^{i\omega}$$

$$z^{-n} = e^{-i\omega n} \times r^{-n} = (r \cdot e^{i\omega})^{-n}$$

The real component is used to measure exponential behaviours and imaginary is used to measure sinusoidal behaviours.

## Z transform
%%[[2025-02-19]] @ 15:31%%

The z transform is a modified [Discrete Time Laplace Transform](Laplace%20transform.md#Discrete%20Time%20Laplace%20Transform) that better expresses exponential content.

$$\LARGE Y(z) = \sum\limits_{n=0}^{\infty} y[n] z^{-1}$$

This is only really useful for infinite data, as finite systems will not have infinite poles.

## Z domain representations
%%[[2025-02-19]] @ 15:37%%

By taking a Z transform of a signal we find the frequency domain content by multiplying by $\cos$ and $\sin$ probing signals.

Representations of systems in the Z domain gives an engineer insight into system dynamics such as: 
- Latency
- #WIP 

## Interpretations

$z^{-n}$ is equivalent to an $n$ unit time delay.

