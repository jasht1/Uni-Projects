
![Fourier transform](Fourier%20transform.md)



$$\LARGE F(u,v) = \sum\limits^{n-1}_{x=0}\sum\limits^{m-1}_{y=0} f(x,y) e^{-j2\pi(\frac{ux}{m}+\frac{vy}{n})}$$

$$f(x,y) = \begin{bmatrix}
100 & 50 \\ 
100 & -10 \\ 
\end{bmatrix}$$

$$n_{0} m_{1}= f(x,y) e^{-j2\pi(\frac{ux}{m}+\frac{vy}{n})}$$
$$u_{0} v_{1}= [100, 50, 100, -10] e^{-j\pi([0,0,1,1])}$$

$$u_{0} v_{1}= [100, 50, 100, -10] *[1,1,-1,-1]$$
$$u_{0} v_{1}= [100, 50, -100, 10]$$
$$u_{0} v_{1}= 60$$
