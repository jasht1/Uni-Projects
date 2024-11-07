# 1
## 1.1
2024-01-17 @ 13:35 
![[Q11.excalidraw|650]]
## 1.2
2024-01-17 @ 18:32 
When $x=0$ $cos(n\pi x) =1$ and for all even values of $n$ $cos(n\pi) =1$ while all odd values of $n$ $cos(n\pi) =-1$ 
therefore 
$$f(0) = \frac{a_{0}}{2}+\sum_{n=1}^\infty \frac{6cos(\pi n)-2}{\pi^{2}n^{2}}
$$
can be represented as
$$f(0) = \frac{a_{0}}{2}+\sum_{n=1}^\infty \frac{6cos(\pi 2n)-2}{\pi^{2}(2n)^{2}}+\frac{6cos(\pi 2n-1)-2}{\pi^{2}(2n-1)^{2}}$$
$$f(0) = \frac{a_{0}}{2}+\sum_{n=1}^\infty \frac{4}{\pi^{2}n^{2}}+\frac{-8}{\pi^{2}n^{2}}$$


# 2
Determine the value of $y(1.3)$ using 2 different numerical methods for the initial value problem $y' = x + y$ and initial condition $y_{0} = 1$, $x_{0} = 1$:
## 2.1 - Euler
2024-01-17 @ 15:56 
With the conditions:
$$\begin{align} 
y' &= x + y \\
x_{0}&=1 \\
y_{0}&=1 \\
h &= 0.1
\end{align}$$
using Euler equation
$$y_{h+1} = y_{n}+h\times y'(x_{n}\ ,\ y_n)$$
$$y_{h+1} = y_{n}+h(x_{n}+ y_n)$$

| $n$ | $x$ | $y$ |
| ---- | ---- | ---- |
| 0 | 1 | 1 |
| 1 | 1.1 | $$1+0.1(1+1) =1.2$$ |
| 2 | 1.2 | $$1.2+0.1(1.1+1.2) = 1.43$$ |
| 3 | 1.3 | $$1.43+0.1(1.2+1.43) = 1.693$$ |
Giving final answer
$$y(1.3) = 1.693$$
## 2.2 -Runge Kutta
2024-01-17 @ 16:14 
With the conditions:
$$\begin{align} 
y' &= x + y \\
x_{0}&=1 \\
y_{0}&=1 \\
h &= 0.1
\end{align}$$
With the Runge Kutta formula
$$y_{n+1} = y_{n} + \frac{h}{b}(k_{1}+2k_{2}+ 2k_{3}+ k_{4})$$
with 6 decimal place approximation

| $n$ | $x$ | $y$ | $k_1$ | $k_2$ | $k_3$ | $k_4$ |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | 1 | 1 | 2 | 2.15 | 2.1575 | 2.31575 |
| 1 | 1.1 | 1.215512 | 2.31551 | 2.48129 | 2.48958 | 2.66447 |
| 2 | 1.2 | 1.464208 | 2.66421 | 2.84742 | 2.85658 | 3.04987 |
| 3 | 1.3 | 1.749575 |  |  |  |  |
Giving final answer
$$y(1.3) = 1.749575$$
# 3
For the linear system which is $AX = \lambda X$ where $A = \pmatrix{4 & 3 \\ −4 & −4}$  
## 3.1
2024-01-17 @ 14:09 
From def
$$A \vec v= I\lambda \vec v$$
$$\text {det} (A-\lambda I)=0$$
factoring in our values for $A$
$$\text {det} (A-\lambda I)= \pmatrix{4 -\lambda  & 3 \\ −4 & −4 - \lambda } = (λ−2)(λ+2)=0$$
Therefore
$$\lambda= \pm 2$$
## 3.2
2024-01-17 @ 14:17 
### for $\lambda = 2$
$$\text {det} (A-\lambda I)= \pmatrix{4 -2  & 3 \\ −4 & −4 - 2 } = \pmatrix{2  & 3 \\ −4 & -6 }$$
Solve by G elimination
$$\left(\begin{matrix}
\frac{2}{2} & \frac{3}{2} &\\
-4+4 & -6+4\frac{3}{2}
\end{matrix}\right) = \pmatrix{1 &\frac{3}{2} \\ 0 & 0}$$
therefore 
$$x_{1}+ \frac{3}{2} x_{2} = 0$$
giving 
$$x_{1}= -\frac{3}{2}x_{2}$$
Making the lowest common denominator of all eigenvectors of  $\lambda_{1} = 2$
$$v_{1} = \pmatrix{-\frac{3}{2} \\1}$$

### for $\lambda = -2$
$$\text {det} (A-\lambda I)= \pmatrix{4 +2  & 3 \\ −4 & −4 + 2 } = \pmatrix{6  & 3 \\ −4 & -2 }$$
Solve by G elimination
$$\left(\begin{matrix}
\frac{6}{6} & \frac{3}{6} &\\
-4+4 & -6+4\frac{3}{6}
\end{matrix}\right) = \pmatrix{1 &\frac{1}{2} \\ 0 & 0}$$
therefore 
$$x_{1}+ \frac{1}{2} x_{2} = 0$$
giving 
$$x_{1}= -\frac{1}{2}x_{2}$$
Making the lowest common denominator of all eigenvectors of  $\lambda_{2} = -2$
$$v_{2} = \pmatrix{-\frac{1}{2} \\1}$$

# 4
## 4.1
2024-01-17 @ 14:35 

| 𝒚′′′ + 𝒚′′ = 𝐬𝐢𝐧 (𝒙) | linear |
| ---- | ---- |
| 𝟐𝒙𝒚′′ + 𝟓𝒚′ = 𝟎 | linear |
| $𝒙^{𝟐}𝒚'' + 𝟓𝒚' = 𝟎$ | non linear |
## 4.2
$$y'' + 5y' + 2y = 0$$
### 4.2.1
2024-01-17 @ 15:24 
let $y' =v$ and express the equation
$$v' +5v +2y =0$$
we can solve for $y''$ by rearranging the original equation and factoring $v$ into it
$$\matrix{
y'' = -5y' - 2y \\
v' = - 5v - 2y
}$$
These can now be put first order linear identities like so
$$\begin{align}
y' &=v \\ v'&= - 2y - 5v 
\end{align}$$
### 4.2.2
putting the identities found in [[#4.2.1]] into matrix form we get
$$\pmatrix{y' \\ u'} = \pmatrix{0&1\\-2&-5}\pmatrix{y\\u} $$

