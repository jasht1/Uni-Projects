# [[week 4 Tutorial Questions.pdf]]
## 1.
%%[[2024-10-18]] @ 09:27%%

$$\frac{d^{2}y}{dt^{2}} + 2 \frac{dy}{dt} + 2y = u$$
$$$$

### 
Find [[Transfer function]] $Y(s)/U(s)$ 
$$s^{2} Y + 2s + 2$$

%% Right how do we find system poles? %%
%% clearly carrying out the numerical operations themselves is trivial, but the intuition to do so is less so. %%



##

## 
Recall that the eigenvalues of a square matrix are found from the [[determinant]] equation Find the eigenvalues of matrix from question 1 and comment.

$$|A - \lambda I| = 0$$

$$-\lambda^{2} -2\lambda - 2$$
No roots

%% I have absoloutely no intuition for what we are doing here. %%

# [[Tutorial Sheet 1.pdf]]
## 1
In this case there are 2 masses, $M_{1}$ and $M_{2}$ on a frictionless plane free to move in a single horizontal dimension;
- $M_{1}$ is connected by; 
	- damper $D$ to a fixed surface,
	- spring $K$ to $M_{2}$
- $M_{2}$ as well as being connected by spring $K$ to $M_{1}$ is acted on by time variant force $f(t)$

The state space variables in this case are;
- $y_{1}$ : displacement of $M_{1}$
- $y_{2}$ : displacement of $M_{2}$
- $\dot y_{1}$ : velocity of $M_{1}$
- $\dot y_{2}$ : velocity of $M_{2}$

Making a 4 dimensional state variable: $$x = \begin{bmatrix} x_{1}\\ x_{2} \\ x_{3} \\ x_{4} \end{bmatrix} = \begin{bmatrix} y_{1} \\ \dot y_{1} \\ y_{2} \\ \dot y_{2} \\ \end{bmatrix}$$
where we can state:
- $\dot x_{1} = x_{2}$ 
- $\dot x_{3} = x_{4}$ 

$x_{2}$ can be found as $\dot x_{2} = \frac{F_{M_{1}}}{M_{1}}$ given that the forces on mass 1: $$F_{M_{1}} = F_{D} + F_{K}$$
The components of which are:
	damper force: $$F_{D} = D(x_{1})$$
	spring force: $$F_{K} = K(x_{1}- x_{3})$$
%% I don't think we have to account for inertia explicitly that should be an emergent property %%
$x_{4}$ can be found by $\dot x_{4} = \frac{F_{M_{2}}}{M_{2}}$ given that:
The forces on mass 2: $$F_{M_{2}} = F_{K} + f(t)$$
The components of which are:
	spring force: $$F_{K} = K(x_{3}- x_{1})$$
	time variant external force: $$f(t)$$

