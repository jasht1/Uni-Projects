[[EGR2010M-TCA-75-2223_last year.pdf]]
# Q1
## a)
2024-01-08 @ 00:48 
Prove that the eigenvalues and eigenvectors of the system $AX = 𝜆X$ are
$𝜆_1 = 7, \ 𝜆_2 = −1$ and $X_1 = \left(\array{1 \\ \frac{1}{3}}\right)$, $X_2 = \left(\array{1\\-1}\right)$ where matrix $A= \left[\array{ 5 && 6 \\ 2 && 1}\right]$.
 ![[DMS TCA 2023 q1 a.excalidraw]]
## b
2024-01-08 @ 10:33 
Find the general and particular solutions of the following [[Systems of differential equations|System of differential equations]].

$$x_{1}' = 5x_{1}+6x_{2}$$
$$x_{2}' = 2x_{1}+x_{2}$$
$$\text{where } x(0) = \pmatrix{3\\1}$$
![[DMS-TCA23-Q1b.excalidraw]]
 Factoring into the above mentioned equation
 $$x(t)= a_1 \pmatrix{1\\-1}e^{7t} + a_2 \pmatrix{3\\1} e^{7 t}$$
Solving for $x(0) = \pmatrix{3\\1}$
 $$x(t)= a_1 \pmatrix{1\\-1}e^{7\times0} + a_2 \pmatrix{3\\1} e^{7\times0}$$
 $$\matrix{a_{1}+3a_{2}=3 \\ -a_{1}+a_{2} = 1} \rightarrow \matrix{a_{1} = 0 \\ a_{2}= 1}$$
Simplifying general solution:
$$x(t) = \pmatrix{3 \\1} e^{7t}$$
## c 
2024-01-13 @ 17:29 
**Let $𝜆$ be an eigenvalue of the $n\times n$ matrix $𝐶$. Show that $𝜆^{2}$ is an eigenvalue of $𝐶^{2}$**
___
The eigenvalue $\lambda$ will be related to the matrix $C$ by 
$$C \vec v= \lambda \vec v$$
where $\vec v$ is the corresponding [[Eigenvalues & Eigenvectors#Eigenvectors|Eigenvector]].
multiplying both sides of the equation by $C$ we get
$$C^{2} \vec v= \lambda C \vec v$$
which can be written as
$$C (C \vec v)= \lambda (C \vec v)$$
showing that the product of $C \vec v$ can be treated as an [[Eigenvalues & Eigenvectors#Eigenvectors|Eigenvector]] of $C$ with eigenvalue $\lambda$ 
The term $C \vec v$ can also be substituted with the original equation $C \vec v= \lambda \vec v$ giving
$$C (C \vec v)= \lambda (\lambda \vec v)$$
simplifying to
$$C^2 \vec v= \lambda^{2} \vec v$$
proving that for an eigenvalue $\lambda$ of the matrix $𝐶$, $𝜆^{2}$ is an eigenvalue of $𝐶^{2}$

# 2
## 2.1
