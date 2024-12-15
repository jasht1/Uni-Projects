
## Questions
![[Tutorial Sheet 2.pdf]]

## Q1
%%[[2024-10-25]] @ 14:12%%

[[Projects/Uni Projects/Complete/Control Systems/Bode plot]] intuition
1. D
2. A
3. B
4. C

## Q2 Finding Poles
%%[[2024-10-25]] @ 14:12%%

## Example 1
$$\dot x = \begin{bmatrix} -4 & -1.5 \\ 4 & 0 \end{bmatrix} x + \begin{bmatrix} 2 \\ 0 \end{bmatrix} u(t)$$
$$y = \begin{bmatrix} 1.5 & 0.625 \end{bmatrix} x$$

### Numerical method
%%[[2024-11-01]] @ 09:42%%

The poles%% Make note for poles and link to it [[Projects/Uni Projects/Complete/Control Systems/transfer function#Poles & Zeros]]%% of the [[Knowledge/Engineering/Modeling/State Space/State Space Representation#State Vector]] are found as the [[eigenvalue]]s of the [[Knowledge/Engineering/Modeling/State Space/State Space Representation#State Equations|A matrix]] in this case:
$$A = \begin{bmatrix} -4 & -1.5 \\ 4 & 0 \end{bmatrix}$$

Using the form $det(sI-A) = 0$ to find the [[eigenvector]],
$$sI - A = \begin{bmatrix} s+4 & 1.5 \\ -4 & s \end{bmatrix}$$
And the [[Determinant]] of this is:
$$det(sI-A) = (s+4)(s) - (1.5)(-4) = s^{2}-4s+6$$

