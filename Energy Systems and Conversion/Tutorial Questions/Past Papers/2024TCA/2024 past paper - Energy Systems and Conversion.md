
https://blackboard.lincoln.ac.uk/ultra/courses/_200912_1/outline/file/_9847443_1

# Question 1 
[Total: 25 marks]
## a. What are the main sources of losses that prevent a wind turbine from operating at or near the Betz limit? 
[5 marks]
%%[[2025-01-08]] @ 14:51%%

The [[Betz law]] is an estimate for the theoretical maximum continuous efficiency of an open flow turbine based on the optimal proportion of energy to extract from an incompressible fluid flow. In practice turbines cannot convert all the kinetic energy extracted from the mass flow to electrical energy due to:

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
Firstly any claim of efficiency is only relevant in the scope of the system boundaries chosen and this has not been communicated. For example the efficiency of the system where the bounds are considered the axial wind power to the mechanical power delivered to the hub is not comparable to the efficiency where the bounds are considered the mechanical power delivered hub to the electrical power at the generator terminals and so on. If the claim where made to an economist then they might expect an efficiency that considered expenses and profits rather than Watts. This is to say that the claim is to ambiguous to be true or false in and of itself. There may be a justifiable interpretation that supports "an efficiency of 65.3%" depending on where the system bounds are drawn and what approximations are taken.

### Assuming the optimal case

Given we have no information on the nature of the turbine we ought avoid speculation by keeping assumptions generally applicable to any device that my be fairly described as a "wind turbine". Considering a "wind turbine" as a means to convert the kinetic energy of a wind stream into electrical energy we may assume these as the system bounds and thus the efficiency a measure of the proportion of electrical power output over the total wind power available in the axial cross sectional area of the turbine. We can also assume there is some actuator exposed to a wind stream, this actuator extracts kinetic energy from the wind stream and converts it to electrical energy. It can be assumed that this conversion is less than 100% efficient based on the 2nd law of thermodynamics thus the electrical output power must be less than the power extracted from the wind stream. 

Using these assumptions [[Betz law]] can be applied which provides an estimate for the theoretical maximum continuous efficiency of an open flow turbine based on the optimal velocity change of the fluid given by a control volume analysis. 

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

each with their respective cross section area $A_{n}$ and flow speed $v_{n}$. where $v_{U}$ is equivalent to $v_{1}$ and $v_{D}$ is equivalent to $v_{2}$ as used previously. The manifold on which the cross sections are taken are normal to 

Conservation of mass implies mass flow rate at these 3 axial slices are equal:

$$\dot{m} = \rho A_{U}v_{U} = \rho A_{T}v_{T} = \rho A_{D}v_{D}$$

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

$$\begin{align*}
\cancel{\rho A_{T} v_{T}} v_{T} (v_{U} - v_{D}) &= \cancel{\rho A_{T} v_{T}} \frac{1}{2} (v_{U}^{2} - v_{D}^{2})\\
v_{T} \cancel{(v_{U} - v_{D})} &= \frac{1}{2} (v_{U} + v_{D}) \cancel{(v_{U} - v_{D})}\\
&\therefore \\
v_{T} &= \frac{1}{2} (v_{U} + v_{D})\\
\end{align*}$$

Thus:

$$\Large \dot{m} = \rho A_{T} \frac{v_{1} + v_{2}}{2}$$

%% Not the case mass flow rate should cancel out
$$\Large \eta = \frac{1}{2} \dot{m}\frac{({v_{1}}^{2}−{v_{2}}^{2})}{{v_{1}}^{2}} = \frac{1}{2} \left( \rho A_{T} \frac{v_{1} + v_{2}}{2} \right) \frac{({v_{1}}^{2}−{v_{2}}^{2})}{{v_{1}}^{2}}$$ %%

### Finding optimal velocity change
%%[[2025-01-10]] @ 00:40%%

Factoring in the identity for mass flow rate found above back into the equation for power extracted from a wind stream gives:

$$\Large P = \frac{1}{4} \rho A_{T} (v_{1} + v_{2}) ({v_{1}}^{2}−{v_{2}}^{2})$$

This equation can be rearranged slightly to emphasise the impact of velocity change, i.e. $\frac{v_{1}}{v_{2}}$, like so:

%% Workings
$$v_{1} = \frac{v_{1}}{v_{2}}v_{2}$$
$$P = \frac{1}{4} \rho A_{T} \left( \frac{v_{1}}{v_{2}}v_{2} + v_{2} \right) \left( {\frac{v_{1}}{v_{2}}v_{2}}^{2}−{v_{2}}^{2} \right)$$

$$P = \frac{1}{4} \rho A_{T} {v_{2}}^{3} \left( \frac{v_{1}}{v_{2}} +1 \right) \left( \frac{v_{1}}{v_{2}}^{2}−1 \right)$$
%%

$$P = \frac{1}{4} \rho A_{T} {v_{2}}^{3} \left( \frac{v_{1}}{v_{2}}^{3} + \frac{v_{1}}{v_{2}}^{2} - \frac{v_{1}}{v_{2}} - 1 \right) $$


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

## b. A gaseous fuel (C8H18) is burned in the presence of air that is assumed completely dry. Volumetric analysis of the gaseous products on a dry basis revealed the following composition:

| Name            | Proportion |
| --------------- | ---------- |
| Carbon dioxide  | 10%        |
| Oxygen          | 5.6%       |
| Carbon monoxide | 0.9%       |
| Nitrogen        | 83.5%      |

### i. Calculate the air–to–fuel ratio 
[5 marks]

### ii. What is the percentage of theoretical air used, and 
[5 marks]

### iii. Determine the quantity of water vapour that condenses as the products are cooled to 25°C at atmospheric pressure. 
[5 marks]
Note: you may take atmospheric pressure to be 105 Pa.
