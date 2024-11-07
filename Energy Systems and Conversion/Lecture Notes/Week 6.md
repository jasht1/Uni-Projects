
## Slides

[[lecture 6 - Basic refrigeration, heat pumps, and air conditioning.pdf]]

## 
%%[[2024-11-01]] @ 11:20%%

Adding Pressure should add capacity to do work, entropy is a measure of capacity to do work, Increasing pressure therefore should increase entropy. If that is the case why dose the work done of the pump follow the line of constant entropy
## Tutorial Questions


![[lecture 6 - Basic refrigeration, heat pumps, and air conditioning.pdf#page=20|lecture 6 - Basic refrigeration, heat pumps, and air conditioning, page 20]]

[[thermodynamic property tables.pdf#page=47|thermodynamic property tables, page 47]]

1. 14.2 g/kg humididy ratio
2. 0.891 

## 

Refrigerant-134a enters the compressor of a refrigerator as superheated vapor at 0.14 MPa and 10°C at a rate of 0.05 kg/s and leaves at 0.8 MPa and 50°C. The refrigerant is cooled in the condenser to 26°C and 0.72 MPa and is throttled to 0.15 MPa. Disregarding any heat transfer and pressure drops in the connecting lines between the components, determine:

(a) the rate of heat removal from the refrigerated space and the power input to the compressor, 
(b) the isentropic efficiency of the compressor, and 
(c) the coefficient of performance of the refrigerator.

![[lecture 6 - Basic refrigeration, heat pumps, and air conditioning.pdf#page=23|lecture 6 - Basic refrigeration, heat pumps, and air conditioning, page 23]]

[[thermodynamic property tables.pdf#page=74|thermodynamic property tables, page 74]]



## a) the rate of heat removal from the refrigerated space and the power input to the compressor
%%[[2024-11-01]] @ 15:44%%
### Heat removal from the refrigerated space
%%[[2024-11-01]] @ 16:28%%

#### Givens

##### State 1
$P_{1} = 0.8 MPa$
$T_{1} = 50 C$
$h_{1} = 286.69 \ kJ/kg$
##### State 2
$T_{2} = 26 C$
$P_{2} = 0.72 MPa$
%% `= 88.82 + (720-700)*(92.22-88.82)/(750-700)` %%
$h_{2} = 88.82 + (720-700)\frac{92.22-88.82}{750-700} = 90.18$

%% ##### State 2
$P_{3} = 0.15 \ MPa$ %%

#### Equation

$$\dot Q = \dot m (h_{2} - h_{1})$$
%% `= 0.5*(90.18-286.69)` %%
$$\dot Q = 0.5(90.18-286.69)$$

### Power input to the compressor
%%[[2024-11-01]] @ 15:44%%
#### Givens
%%[[2024-11-01]] @ 15:21%%

Medium: R-134a 

Mass flow rate 
$\dot m = 0.05 \ kg/s$
##### State 1
Superheated vapour
$P_{1} = 0.14 MPa$
$T_{1} = -10 C$
$h_{1} = 246.36 \ kJ/kg$

v u h s
m3/kg kJ/kg kJ/kg KkJ/kg
0.14605 225.91 246.36 0.972

##### State 2
$P_{1} = 0.8 MPa$
$T_{1} = 50 C$
$h_{1} = 286.69 \ kJ/kg$

%%
Misread the pressure
$h = 0.08\frac{298.16-298.74}{0.1-0.06}$
`=0.08*(298.16-298.74)/(0.1-0.06)` 
%%
#### Calculation
$$\dot Q = \dot m (h_{2} - h_{1})$$
%% `= 0.05 * (286.69 - 246.36)` %%
$$\dot Q = 0.05 (286.69 - 246.36) = 2.016$$

## b) the isentropic efficiency of the compressor
%%[[2024-11-01]] @ 16:08%%

All work done between $\vec{2,2s}$ and $\vec{3,4}$ are considered losses, therefore instropic efficiency is:
$$COP_{R\text{, Carnot}} = \frac{1}{1-T_{L}/T_{H}}$$

where 