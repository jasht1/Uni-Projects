# Week 8
2023-11-13 @ 15:22 
## Odd vs even functions
![[Odd vs Even function 2023-11-13 15.06.59.excalidraw]]

## [[Fourier transform]]
### Example 1
![[DMS raw notes exmpl1 2023-11-13 15.40.35.excalidraw]]
Using [[Fourier transform]]
$$F(\omega)= \int^\infty _{-\infty} f(t) e^{-j\omega t} dt$$
withing the range $-1<t<1$ where $f(t) = 3$:
$$F(\omega)= \int^1 _{-1} 3 e^{-j\omega t} dt$$
Evaluating the integral gives:
$$F(w) = \left[ \begin{array}{ccc}
\frac{3e^{-j\omega t}}{-j\omega}
\end{array} \right]^1_{-1}$$
$$F(w) = \frac{3e^{j\omega}-3e^{-j\omega}}{j\omega}$$
Using ![[Euler]]
This can be simplified to:
$$F(\omega)= 6 \frac{sin(\omega)}{\omega}$$
