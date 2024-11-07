
# Question 1

![[Week 2 - Entropy - TUTORIALS - w solutions.pdf#page=2|Week 2 - Entropy - TUTORIALS - w solutions, page 2]]

## Givens
Primary Givens:
Isochoric process 
	statics:
$m = 5 kg$
	Changes:
$T_{1} = 20 \degree C$
$p_{1} = 140 kPa$

$p_{2} = 100kPa$

find: 
$\delta S$

secondary givens:
[[thermodynamic property tables.pdf]]
%% How is this value found?
In the [[thermodynamic property tables.pdf]] table A-12 Entropy is 
0.11087 @ 140 kPa
however the saturation temp is below $T_{1}$ so we check the super heated table
%%
$S_{ssf} = 1.0624 \ kj \cdot kg^{-1} \! \cdot k^{-1} \ @ 0.14 MPa$
$v = 0.16544 \ m^{3} \cdot kg^{-1} \ @ 0.14 MPa$

in order to find the $S_{ssf} \ @ T_{2}$ we must find $T_{2}$ 


## Using Combined gas law

![[combined gas law#Summary]]

$$\frac{P_{1}V}{T_{1}} \div V = \frac{P_{2}V}{T_{2}} \div V$$
$$\frac{P_{1}}{T_{1}} \div P_{2} = \frac{P_{2}}{T_{2}} \div P_{2}$$
$$\frac{P_{1}}{T_{1}P_{2}}^{-1} = {T_{2}}^{-1}$$
$$\frac{T_{1}P_{2}}{P_{1}}= {T_{2}}$$
substituting the values in we get:
$$\frac{293.15 \times 100}{140} = 209.39$$
`=293.15*100000/140000`

which is $-63.76 \degree C$

This is too low

$S_{ssf}= $

## Using Volume
%%[[2024-10-04]] @ 15:56%%

Given that this is an isochoric process the volume is constant:
$$V_{1} = V_{2} = V$$
As the mass is also constant the specific volume must also be constant.

We can find the specific volume at state 1 from the steam tables as:
$$v_{1} = 0.16544 \ m^{3} \cdot kg^{-1} \ @ 0.14 MPa$$
This is between the specific volume of saturated liquid and volume:
$$\begin{align*}
v_{f} \ @ 100kPa &= 0.0007259\\
v_{g} \ @ 100kPa &= 0.19254
\end{align*}$$
Therefore we know it will be a saturated liquid vapour mixture.
$$S_{f} = 0.07188$$



$$V = m \times v$$
