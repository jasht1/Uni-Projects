# Dynamic system modelling
%%description%%
[[Control System terminology]]
## Types of models
2023-03-02 @ 14:52 
- [[analysis system model|Analysis]]
	Mathematical models are based on first principles, including differential equations.
- Grey-Box
	Model is developed and then parameters are inferred from experiments.
- Black-Box
	Input/Output data is used to infer a dynamic relationship.



## Differential Equation driven modelling
2023-03-02 @ 14:38 
Differential equations can model how a system changes with respect to a variable. formulas that can be arranged to equal 0 are particularly useful e.g.
- Newton’s Law
	The sum of forces on a body equals to zero; the sum of torques on a body equals zeros. 
	$\Sigma F = 0$  
- Kirchhoff’s voltage law
	The sum of voltages around a closed path equals zero. 
	$\Sigma V = 0$ 
- Kirchhoff’s current law
	The sum of electric currents flowing from a node equals zero.
	$\Sigma I = 0$ 
## [[Control System terminology#Inversion|Inversion]] based control
[[Control System terminology#Feedforward|Feedforward]] input uses system knowledge to control the output and is found using [[Control System terminology#Inversion|inversion]]. It can be combined with [[Control System terminology#Feedback|feedback]] for greater system resilience.
### When to use [[Control System terminology#Feedforward|feedforward]]
Let the Error in model be $\delta (\omega) = G_0 (\omega) - G (\omega)$
For SISO Case, Feedforward always improves output tracking for any feedback if $|\delta (\omega)| < |G_0 (\omega)|$.
	https://faculty.washington.edu/devasia/Talks/Inversion_Theory.pdf
		Ref: S. Devasia, “Should Model-based Inverse Inputs be used as Feedforward under Plant Uncertainty?” IEEE Trans. on Automatic Control, Vol. 47(11), Nov 2002.