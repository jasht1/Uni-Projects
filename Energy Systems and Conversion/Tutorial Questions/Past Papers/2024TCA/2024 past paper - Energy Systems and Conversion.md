
https://blackboard.lincoln.ac.uk/ultra/courses/_200912_1/outline/file/_9847443_1

# Question 1 
[Total: 25 marks]
## a. What are the main sources of losses that prevent a wind turbine from operating at or near the Betz limit? 
[5 marks]
%%[[2025-01-08]] @ 14:51%%

The [[Betz limit]] is an estimate for the theoretical maximum continuous efficiency of an open flow turbine based on the optimal proportion of energy to extract from an incompressible fluid flow. In practice turbines cannot convert all the kinetic energy extracted from the mass flow to electrical energy due to:

1. Coil losses & associated inefficiencies in the alternator,
2. Non Ideal fluid flow:
   - turbulence in the flow,
   - off axis flow,

3. Frictional losses:
	- at the fluid - turbine interface,
	- in the mechanical components,

## b. An engineer boasting about the virtues of their new wind turbine claimed it has an efficiency of 65.3%. Starting from $P= \frac{1}{2} \dot{m}({v_{1}}^{2}−{v_{2}}^{2})$, with $P$ being the power output resulting from a change in wind velocity from $v_{1}$ to $v_{2}$ across turbine’s blades, show that the engineer’s claim cannot be true and his efficiency value is in fact overestimated by at least 6 percentage points. 
[10 marks] 

> [!NOTE] Assumption
> Question states $P= \frac{1}{2} m({v_{1}}^{2}−{v_{2}}^{2})$ however this would not give $P$ but $E$ as $m$ must be given as $\dot{m}$ ($\frac{dm}{dt}$)

### The claim is ambiguous 

It should be stated at a minimum that the report of this claim is too ambiguous to be precisely interpret-able for several reasons. 
Firstly any claim of efficiency is only relevant in the scope of the system boundaries chosen and this has not been communicated. For example the efficiency of the system where the bounds are considered the axial wind power to the mechanical power delivered to the hub is not comparable to the efficiency where the bounds are considered the mechanical power delivered by the hub to the electrical power at the generator terminals and so on. If the claim where made to an economist then they might expect an efficiency that considered expenses and profits rather than Watts. This is to say that the claim is to ambiguous to be true or false in and of itself. There may be a justifiable interpretation that supports "an efficiency of 65.3%" depending on where the system bounds are drawn and what approximations are taken.

### Assuming the optimal case

Given we have no information on the nature of the turbine we ought avoid speculation by keeping assumptions generally applicable to any device that my be fairly described as a "wind turbine". Considering a "wind turbine" as a means to convert the kinetic energy of a wind stream into electrical energy we may assume these as the system bounds and thus the efficiency a measure of the proportion of electrical power output over the total wind power available in the axial cross sectional area of the turbine. We can also assume there is some actuator exposed to a wind stream, this actuator extracts kinetic energy from the wind stream and converts it to electrical energy. It can be assumed that this conversion is less than 100% efficient based on the 2nd law of thermodynamics thus the electrical output power must be less than the power extracted from the wind stream. 

Using these assumptions [[Betz limit]] can be applied which provides an estimate for the theoretical maximum continuous efficiency of an open flow turbine based on the optimal velocity change of the fluid given by a control volume analysis. 

As the kinetic energy of a wind stream is given by:

$$E = \frac{1}{2}mv^{2}$$

The power extracted from a wind stream can be found by:

$$P= \frac{1}{2} \dot{m}({v_{1}}^{2}−{v_{2}}^{2})$$

Where:
- $\dot{m}$ : mass flow rate through the swept area of the turbine ($kg/s$)
- $v_{1}$ : initial flow velocity 
- $v_{2}$ : final flow velocity

So the proportion of power extracted from the wind stream is:

$$\eta = \frac{({v_{1}}^{2}−{v_{2}}^{2})}{{v_{1}}^{2}}$$

However this doesn't give the full story as if $v_{2}$ is reduced then so too must mass flow rate and thus less power will be generated.

The mass flow rate $\dot{m}$ is the product of the functional area of the turbine $A_{T}$, the fluid density $\rho$ and the velocity over the turbine $v_{T}$. The density $\rho$ can be approximated based on a reasonable air temperature. However the functional area of the turbine $A_{T}$ and the wind velocity at the turbine are unknown so the optimal values will be considered.

### Finding velocity over the turbine in terms of initial and final velocity
%%[[2025-01-09]] @ 16:43%%

This section will prove the velocity over the turbine $v_{T}$ is the average of the incoming $v_{1}$ and outgoing $v_{2}$ velocity.

#### Setup

3 points $n$ are considered and will denoted by subscript:
1. $U$ : upstream of the rotor,
2. $T$ : at the rotor,
3. $D$ : downstream of the rotor,

each with their respective cross section area $A_{n}$ and flow speed $v_{n}$. where $v_{U}$ is equivalent to $v_{1}$ and $v_{D}$ is equivalent to $v_{2}$ as used previously. 
%% The manifold on which the cross sections are taken are normal to  %%

Conservation of mass implies mass flow rate at these 3 axial slices are equal:

$$\large \dot{m} = \rho A_{U}v_{U} = \rho A_{T}v_{T} = \rho A_{D}v_{D}$$

Where:
- $\dot{m}$ : is the fluids mass flow rate
- $\rho$ : is the the fluids density

#### First equation for power

The force on the turbine my be expressed given Newton's 3rd law:

$$F = ma \quad \to \quad F = m \frac{dv}{dt} \quad \to \quad F = \dot{m} \Delta v$$

by substitution the identity for mass flow rate at the turbine and the change in fluid velocity across it:

$$\therefore \quad F_{T} = \rho A_{T} v_{T} (v_{U} - v_{D})$$

Work done $E$ being the product of force $F$ and distance $x$, 

$$E = Fx$$ 

And power $P$ being the rate of work done,

$$P = F \frac{dx}{dt} \quad \to \quad P = F v$$

Where change in distance by change in time $\frac{dx}{dt}$ of the working fluid can be substituted with it's velocity $v$.

The power exerted at the turbine can then be expressed in these terms:

$$P = \rho A_{T} v_{T}^{2} (v_{U} - v_{D})$$

#### Second equation for power

An alternate and equivalent equation for power can be found based on difference in kinetic energy upstream $U$ and downstream $D$, where kinetic energy is given by:

$$E = \frac{1}{2} m v^{2}$$

And power by accounting for mass flow rate $\dot{m}$ and change in velocity:

$$P = \frac{1}{2} \dot{m} \Delta v^{2}$$

Thus power at the turbine is also given by:

$$P = \frac{1}{2} \rho A_{T} v_{T} (v_{U}^{2} - v_{D}^{2})$$

#### Conclusion

By setting these identities as equal an identity for $v_{T}$ in terms of $v_{U}$ & $v_{D}$ can be found:

$$P = \rho A_{T} v_{T}^{2} (v_{U} - v_{D}) = \frac{1}{2} \rho A_{T} v_{T} (v_{U}^{2} - v_{D}^{2})$$

> [!NOTE] Workings
> $$\begin{align}
> \cancel{\rho A_{T} v_{T}} v_{T} (v_{U} - v_{D}) &= \cancel{\rho A_{T} v_{T}} \frac{1}{2} (v_{U}^{2} - v_{D}^{2})\\
> v_{T} \cancel{(v_{U} - v_{D})} &= \frac{1}{2} (v_{U} + v_{D}) \cancel{(v_{U} - v_{D})}\\
> &\therefore \\
> v_{T} &= \frac{1}{2} (v_{U} + v_{D})\\
> \end{align}$$

Thus:

$$\Large \dot{m} = \rho A_{T} \frac{v_{1} + v_{2}}{2}$$

%% Not the case mass flow rate should cancel out
$$\Large \eta = \frac{1}{2} \dot{m}\frac{({v_{1}}^{2}−{v_{2}}^{2})}{{v_{1}}^{2}} = \frac{1}{2} \left( \rho A_{T} \frac{v_{1} + v_{2}}{2} \right) \frac{({v_{1}}^{2}−{v_{2}}^{2})}{{v_{1}}^{2}}$$ %%

### Finding optimal velocity change
%%[[2025-01-10]] @ 00:40%%

Factoring in the identity for mass flow rate found above back into the equation for power extracted from a wind stream gives:

$$\Large P = \frac{1}{4} \rho A_{T} (v_{1} + v_{2}) ({v_{1}}^{2}−{v_{2}}^{2})$$

This equation can be rearranged slightly to emphasise the impact of the proportional velocity drop, i.e. $\frac{v_{2}}{v_{1}}$, like so:

%% Original workings
$$v_{1} = \frac{v_{1}}{v_{2}}v_{2}$$
$$P = \frac{1}{4} \rho A_{T} \left( \frac{v_{1}}{v_{2}}v_{2} + v_{2} \right) \left( {\frac{v_{1}}{v_{2}}v_{2}}^{2}−{v_{2}}^{2} \right)$$

$$P = \frac{1}{4} \rho A_{T} {v_{2}}^{3} \left( \frac{v_{1}}{v_{2}} +1 \right) \left( \frac{v_{1}}{v_{2}}^{2}−1 \right)$$

$$P = \frac{1}{4} \rho A_{T} {v_{2}}^{3} \left( \frac{v_{1}}{v_{2}}^{3} + \frac{v_{1}}{v_{2}}^{2} - \frac{v_{1}}{v_{2}} - 1 \right) $$

*This explanation may be more intuitive if I factor $v_{1}$ out instead so it's clear power is proportional with wind speed cubed.*
%%

> [!NOTE]- Workings
> 
> $$\text{substituting:}\quad v_{2} = \frac{v_{2}}{v_{1}}v_{1}$$
> 
> $$P = \frac{1}{4} \rho A_{T} \left( v_{1} + \frac{v_{2}}{v_{1}} v_{1} \right) \left( {{v_{1}}^{2} - \frac{v_{2}}{v_{1}}v_{1}}^{2} \right)$$
> 
> $$P = \frac{1}{4} \rho A_{T} {v_{1}}^{3} \left( 1 + \frac{v_{2}}{v_{1}} \right) \left( 1 - \frac{v_{2}}{v_{1}}^{2} \right)$$
> 

$$\large P = \frac{1}{4} \rho A_{T} {v_{1}}^{3} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right) $$

This indicates the proportional velocity drop across a turbine $x$, where $x = v_{2}/v_{1}$, impacts power output $P$ according to the following relationship:

$$\large P \propto- x^{3} - x^{2} + x + 1 \quad \text{where} \ x = v_{2}/v_{1}$$

The maximum value Given that the turbine is extracting energy from the wind flow the velocity will go down $v_{2} < v_{1}$ and will not be negative $v_{2} > 0$ thus providing the limits. The maximum value inside of these limits the proportional velocity drop associated with the maximum continuous extract-able power:

$$P_{\text{max}} = \max(-x^{3} - x^{2} + x + 1) \quad \text{in range:} \ 0<x<1$$

%% Workings
*integrate and take the stationary points in your range then plug it back into the equation or just slap it in wolfram alpha :shrug*
%%

Which occurs at $x = 1/3$ indicating a turbine must reduce the fluid velocity by $66.\dot{6}$% to extract the maximum continuous power from a fluid flow. Thus at max efficiency $v_{2} = v_{1}/3 \ @ \ \eta_{max}$.

### Finding max efficiency
%%[[2025-01-10]] @ 02:48%%

Dividing the power equation by the total power of the wind stream gives the following equation for the proportion of available wind power extracted:

$$\Large \eta = \frac
{\frac{1}{4} \rho A_{T} {v_{1}}^{3} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right)}
{\frac{1}{2} \rho A_{T} \frac{v_{1} + v_{2}}{2} {v_{1}}^{2}} $$

Once the redundant terms are cancelled and the optimal proportional velocity drop is substituted this becomes:

> [!NOTE]- Workings
> 
> $$\begin{align*}
> \text{Canceling redundant terms,}\\
> \eta &= \frac
> {\cancel{\frac{1}{4}} \cancel{\rho A_{T}} {v_{1}}^{\cancel{3}} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right)}
> {\cancel{\frac{1}{2}} \cancel{\rho A_{T}} \frac{v_{1} + v_{2}}{\cancel{2}} \cancel{{v_{1}}^{2}}}
> \\\\
> \eta &= \frac
> {\cancel{{v_{1}}} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right)}
> {\cancel{v_{1}} + \frac{v_{2}}{v_{1}}}
> \\\\
> \eta &=  \frac
> {- \frac{v_{2}}{v_{1}}^{\cancel{3}2} - \frac{v_{2}}{v_{1}}^{\cancel{2}} + \cancel{\frac{v_{2}}{v_{1}}} + \cancel{1} \frac{v_{1}}{v_{2}}}
> {\cancel{\frac{v_{2}}{v_{1}}}}
> \\\\
> \eta &= -\frac{v_{2}}{v_{1}}^{2} -\frac{v_{2}}{v_{1}} + \frac{v_{1}}{v_{2}}
> \\\\
> \text{Substituting:} \ v_{2} = v_{1}/3 \ @ \ \eta_{max}
> \\
> \eta_{max} &= -\frac{(v_{1}/3)}{v_{1}}^{2} -\frac{(v_{1}/3)}{v_{1}} +\frac{v_{1}}{(v_{1}/3)}
> \\
> \eta_{max} &= -\frac{\cancel{v_{1}}}{3 \cancel{v_{1}}}^{2} -\frac{\cancel{v_{1}}}{3 \cancel{v_{1}}} +\frac{3\cancel{v_{1}}}{\cancel{v_{1}}}
> \end{align*}
> $$

$$\eta = -\frac{1}{3}^{2} -\frac{1}{3} +3 = 2.\dot{5}$$

## c. A horizontal axis wind turbine (HAWT) has a blade span (diameter) of 15 m and the hub is 35 m above ground level. The wind speed at 2 m height is 5 m/s. 
### i. Calculate the actual power output of the wind turbine assuming maximum efficiency. 
[5 marks] 

### ii. A wind turbine salesman while marketing their wind turbine claimed that with the dimensions above and at 50 m height, it can produce 250 kW power at 5 m/s wind speed (this wind speed is at 2 m height from the ground). Is the claim true? 
[5 marks] 

# Question 2 
[Total: 25 marks]
## a. 
### i. Name two differences between an Otto and a Diesel Cycle. 
[2 marks] 
### iii. which is worse – putting petrol in a diesel engine or vice versa? Rationalise each scenario. 
[3 marks] 
## b. A gas turbine operating on the Brayton gas cycle has one each of isentropic compression and expansion. Air is taken into the compressor at 95 kPa and ambient temperature of 22ºC. The compressor has a ratio of 6 to 1 while the compressed air is heated to 827ºC. The combustion products then go through expansion in a turbine. 
### i. Draw an annotated schematic and the T-S diagram for this cycle matching the numbering of each stream or process 
[5 marks] 

### ii. Compute the thermal efficiency of the cycle. 
[10 marks] 

### iii. Discuss the result above with respect to the compressor work and total turbine work. Your discussion should touch on what should be maximised and what should be minimised to ensure the economic viability of gas turbines. 
[5 marks] 
[Note that interpolation from thermodynamic tables is required to obtain accurate results in this task] 

# Question 3  
## a.
### i. What is Stoichiometric air?
[2 marks]
%%[[2025-01-08]] @ 16:00%%

Stoichiometric connotes an amount in proportion to it's necessity in a chemical reaction. It means nothing without context but in the context of a specific reaction in this case likely the combustion of a fuel, it would be the exact mass of air necessary to achieve complete complete combustion based on the mass of the other reactants.

### ii. What is meant by lean and rich fuel mixtures? State an advantage and a disadvantage of an engine running on either. 
[8 marks]
%%[[2025-01-08]] @ 16:05%%

Lean vs rich distinguish mixes that contain fuel to oxidiser ratios lower vs higher than stoichiometric respectively. 

Lean fuel mixes introduce more air than strictly necessary for complete combustion. This typically improves fuel efficiency and results in higher combustion chamber temperature & pressure. 
A well designed engine should be able to withstand the added thermal and mechanical stress, the main issues is production of $NOX$. While the chamber temperature is in excess of 2,500 K oxides of nitrogen can form, the higher the temperature & pressure an the longer it's maintained the more oxides of nitrogen are likely to be produced.


![[Knowledge/Engineering/Energy Systems/Engines/Reciprocating/attachments/Diesel Pressure Graphs, NOX Reigion (light).png]]

%% ![[Knowledge/Engineering/Energy Systems/Engines/Reciprocating/attachments/Diesel Pressure Graphs, NOX Reigion.png]] %%

A fuel rich mix can achieve higher peak power for an engine tuned to take advantage of it, however this is at the expense of lower fuel efficiency 

## b. A gaseous fuel ($C_{8}H_{18}$) is burned in the presence of air that is assumed completely dry. Volumetric analysis of the gaseous products on a dry basis revealed the following composition:

| Name            | Proportion |
| --------------- | ---------- |
| Carbon dioxide  | 10%        |
| Oxygen          | 5.6%       |
| Carbon monoxide | 0.9%       |
| Nitrogen        | 83.5%      |

### i. Calculate the air–to–fuel ratio 
[5 marks]
%%[[2025-01-10]] @ 15:04%%

The air–to–fuel ratio is the proportion of mass of air over the mass of fuel introduced to combustion chamber.

$$\text{AFR} = \frac{m_{\text{air}}}{m_{\text{fuel}}}$$

Assuming that the dry air is 21% $O_{2}$ and 79% $N_{2}$ it's mass is equivalent to:

$$m_{\text{air}} = n_{\text{air}} \left( \frac{21}{100}M_{O_{2}} + \frac{79}{100} M_{N_{2}} \right)$$

Similarly the fuel mass can be substituted for number of moles and molar mass:

$$\text{AFR} = \frac {\frac{21}{100}2M_{O} + \frac{79}{100} 2M_{N}}{8 M_{C} + 18 M_{H}} \times \frac{n_{\text{air}}}{n_{\text{fuel}}}$$

^c733f8

Where the number of moles of air $n_{\text{air}}$ is implied by the number of moles of oxygen $n_{O_{2}}$:

$$n_{\text{air}} = \frac{100}{21} n_{O_{2}}$$

Assuming that all of the fuel reacted the number of moles of fuel $n_{\text{fuel}}$ can be found as a proportion to the moles of oxygen $n_{O_{2}}$ based on the gaseous products produced.   

however, not all of the oxygen was reacted as it is still present in the gaseous product and the amount of gas in the product is not that of the initial air so the proportions provided are not directly comparable. 

Given that no new nitrogen was introduced and no oxides of nitrous appear in the in the gaseous product analysis we may assume the amount of $N_{2}$ is unchanged. However dry air is assumed to be 79% $N_{2}$ not 83.5% indicating the change in the amount of gaseous substance. This will be due to $O_{2}$ being removed in the form of water as well as additional $CO_{2}$ & $CO$ being introduced as combustion products. 
This giving a means of translating the proportion of oxygen in the gaseous product to it's equivalent proportion in the initial dry air.

$$\large \frac{O_{2}\text{ un-reacted}} {O_{2} \text{ total}} = \frac{21 - \left( 5.6 \times\frac{83}{79} \right)}{21}$$

Therefore the total oxygen can be found based on the amount reacted:

$$\large n_{O_{2}} \text{ total} = n_{O_{2}} \text{ reacted} \left(1 + \frac{5.6 \times\frac{83}{79}}{21} \right)$$

Based on the gaseous products present the combustion equation must have the following form:

%% Overly involved method for such a simple equation

$$C_{8}H_{18} + O_{2} \to CO_{2} + CO + H_{2}O$$

This can be represented in matrix form as:

$$\begin{bmatrix} Q_{C_{8}H_{18}}  & Q_{O_{2}}\end{bmatrix} 
\begin{bmatrix}8 & 18 & 0 \\ 0 & 0 & 2\end{bmatrix}
= 
\begin{bmatrix}Q_{CO_{2}} + Q_{CO} + Q_{H_{2}O} \end{bmatrix}
\begin{bmatrix}1 & 0 & 2 \\ 1 & 0 & 1 \\ 0 & 2 & 1\end{bmatrix}$$
%%

$$q_{1} \ C_{8}H_{18} + q_{2} \ O_{2} \to q_{3} \ CO_{2} + q_{4} \ CO + q_{5} \ H_{2}O$$

Where:

- $q_{1} = n_{\text{fuel}} \text{ reacted}$ 
- $q_{2} = n_{O_{2}} \text{ reacted}$ 

As the fuel $C_{8}H_{18}$ contains 18 hydrogen's and this was entirely converted to water $H_{2}O$ with 2 hydrogens each it must have done so in a $1:9$ ratio.

$$q_{5} = 8 q_{1}$$

As $CO_{2}$ and $CO$ are negligible in the starting air and exist in the gaseous products in a $100:9$ ratio with no other carbon based products then:

$$q_{3} = \frac{100}{100+9}q_{1}$$

$$q_{4} = \frac{9}{100+9}q_{1}$$

Now oxygen can be accounted for in terms of $q_{1}$ as a stoichiometric sum of the products:

$$q_{2} = \left( \frac{2q_{3}+ q_{4}+ q_{5}}{2} \right) q_{1} = \left( \frac{2\left( \frac{100}{109} \right) +\left(\frac{9}{109}\right) +(8)}{2} \right) q_{1} = \frac{1081}{218}q_{1}$$

%% Redundant
Thus the combustion can be represented as:

$$C_{8}H_{18} + 4\frac{209}{218} O_{2} \to \frac{100}{109} CO_{2} + \frac{9}{109} CO + 8 H_{2}O$$


*while it is best practice to split this representation up into* 

*$$C_{8}H_{18} + O_{2} \to CO + H_{2}O$$*
*$$C_{8}H_{18} + O_{2} \to CO_{2} + H_{2}O$$*

*and indicate the proportionality of the 2 reactions but this doesn't serve our means in this case as all we care about is $q_{2}/q_{1}$ i.e. oxygen to fuel ratio.*
%%

Therefore the moles of fuel $n_{\text{fuel}}$ can be represented in terms of moles of oxygen reacted $n_{O_{2}} \text{ reacted} = q_{2}$ along with moles of air $n_{\text{air}}$:

$$\large n_{\text{fuel}} = \frac{218}{1081} q_{2} \quad \& \quad n_{\text{air}} = \frac{100}{21} q_{2} \left(1 + \frac{5.6 \times\frac{83}{79}}{21} \right)$$

Substituting these identities into the [[#^c733f8|AFR equation found earlier]] air to fuel ratio is equal to:

$$\large \text{AFR} = \frac
{\frac{21}{100}2M_{O} + \frac{79}{100} 2M_{N}}
{8 M_{C} + 18 M_{H}} 
\times \frac
{\frac{100}{21} q_{2} \left(1 + \frac{5.6 \times\frac{83}{79}}{21} \right)}
{\frac{218}{1081} q_{2}}$$

Substituting the values for $M_{O}$, $M_{N}$, $M_{C}$, and $M_{H}$ the left hand fraction ($\text{LHF}$) can be reduced: 

$$\text{LHF} = \frac
{\frac{21}{100}2(16) + \frac{79}{100} 2(28)}
{8 (12) + 18 (1)} $$
$$\text{LHF} = \frac
{\frac{21}{100}32 + \frac{79}{100}56}
{96 + 18}$$
$$\text{LHF} = \frac
{21 \times 32 + 79 \times 56}
{114 \times 100}$$
$$\text{LHF} = \frac
{21 \times 32 + 79 \times 56}
{114 \times 100}$$
$$\text{LHF} = \frac{5096}{11400} = \frac{637}{1425}$$

In the right hand fraction ($\text{RHF}$) $q_{2}$ can be cancelled out and reduced:

$$\text{RHF} = \frac
{\frac{100}{21} \cancel{q_{2}} \left(1 + \frac{5.6 \times\frac{83}{79}}{21} \right)}
{\frac{218}{1081} \cancel{q_{2}}}$$
$$\text{RHF} = \frac
{1081 \times 100 \left(1 + \frac{5.6 \times 83}{79 \times 21} \right)}
{21 \times 218}$$
$$\text{RHF} = \frac
{108100 + \frac{108100 \times 5.6 \times 83}
{1659}}{4578}$$
$$\text{RHF} = \frac{108100}{4578} + \frac{108100 \times 5.6 \times 83}{4578 \times 1659}$$
$$\text{RHF} = \frac{16398770}{542493}$$

Substituting the reduced fractions back in:

$$\large \text{AFR} = \frac{637}{1425} \times \frac{16398770}{542493} = \frac{298457614}{22087215} \approx 13.5$$


### ii. What is the percentage of theoretical air used
[5 marks]

### iii. Determine the quantity of water vapour that condenses as the products are cooled to 25°C at atmospheric pressure. 
[5 marks]
Note: you may take atmospheric pressure to be 105 Pa.
