
[Solutions](https://blackboard.lincoln.ac.uk/ultra/courses/_200916_1/outline/file/_9755069_1)

# Question 1
%%[[2024-10-16]] @ 13:06%%

Given the system below:

![[week 1 - question 1 diagram.png]]

![[Question 1 m1 fbd.excalidraw]]

To describe force $F(t)$ on block $M_1$ find a system of linear equations that describe the states of the system above, 
where the states of interest are the positions of $m_{1}$ and $m_{2}$, denoted by $y_{1}$ and $y_{2}$ respectively. By [[derivative]] the velocity's and acceleration's can be represented.

Constructing a state variable $x$ as:
$$x = \begin{bmatrix} x_{1}\\ x_{2} \\ x_{3} \\ x_{4} \end{bmatrix} = \begin{bmatrix} y_{1} \\ \dot y_{1} \\ y_{2} \\ \dot y_{2} \\ \end{bmatrix}$$
where we can state:
- $\dot x_{1} = x_{2}$ 
- $\dot x_{3} = x_{4}$ 

consider the forces at play:
- $F_{K_{1}}$ : a spring acting equal and opposite on $m_1$ and $m_{2}$ proportional to their relative displacements. $$F_{K_{1}} (y_{1}, y_{2}) = k_{K_{1}}(y_{1}-y_{2})$$
- $F_{B_{1}}$ : a damper acting equal and opposite on $m_1$ and $m_{2}$ proportional to their relative velocities. $$F_{B_{1}} (\dot y_{1},\dot y_{2}) = k_{B_{1}}(\dot y_{1} - \dot y_{2})$$
- $F_{K_{2}}$ : a spring acting on $m_{2}$ proportional to its displacement from the origin. $$F_{K_{2}} (y_{2}) = k_{K_{2}} (y_{2})$$
- $F_{B_{2}}$ : a spring acting on $m_{2}$ proportional to its velocity. $$F_{B_{2}} (\dot y_{2}) = k_{K_{2}} (\dot y_{2})$$

Given this we can construct equations for the forces on $m_{1}$ and $m_{2}$:
$$\large \begin{align*}
F_{m_{1}} &= F_{K_{1}}(x_{1},x_{2}) + F_{B_{1}}(\dot y_{1},\dot y_{2}) \\
F_{m_{2}} &= F_{K_{1}}(x_{1},x_{2}) + F_{B_{1}}(\dot y_{1},\dot y_{2}) + F_{K_{2}} (y_{2}) + F_{B_{2}} (\dot y_{2})
\end{align*} $$

Given that $F = m a$ we can get functions for acceleration by dividing net force by mass giving functions for $\dot x_{2}$ and $\dot x_{4}$.
$$\dot x_{2} = \frac{F_{m_{1}}}{m_{1}} \quad \& \quad \dot x_{4} = \frac{F_{m_{2}}}{m_{2}}$$


# Question 2
