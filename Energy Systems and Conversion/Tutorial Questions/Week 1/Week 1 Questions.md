# Questions

$e = mc^{2}$

## Pressure to mass calculation
%%[[2024-09-27]] @ 11:24%%

![[Lecture 1 - Basic principles.pdf#page=15|Week 1 - Basic principles, page 15]]

$T = 190 + 273.15 \degree K$
$p = 200 bar + 1 bar (atm)$ 
$V = 10 m^{3}$

The gas constant $R$ is $8.314 J / mol·K$

$m = pV/RT$

the gas constant of methane is $518.28 g/mol$ 

$$\frac{p((201.03) \times 10^{5}Pa) \times V(10)m^{3}}{R(518.28)J \cdot kg^{-1} \cdot K \times T (463.15)\degree K} = 838.61 kg$$
`=(201.3*1000000)/(518.28*463.15)` 


# Questions to think about

## 1. What are the units of: $\frac{p}{R \cdot T}$?
%%[[2024-09-27]] @ 17:41%%

1. What are the units of: $\frac{p}{R \cdot T}$?

This is rearrangement of the gas law, $pV = nRT$
$$\frac{P}{R \cdot T} = \frac{n}{V}$$ 

$p$ is Pressure typically in kPa however the SI unit would be $N/m^{2}$
$T$ is temperature that will be in $\degree K$ 

$V$ is Volume in $m^{3}$
$n$ is moles of gas present,.

to find the units of $R$ the ideal gas constant we can substitute the units into this equation:

$$\frac{Nm^{-2}}{\degree K \cdot ?}= \frac{mol}{m^{3}}$$

rearranging for $R$

$$\frac{Nm^{-2} \cdot m^{3}}{\degree K \cdot mol}= ? = \frac{Nm}{mol \cdot K}$$

Given $Nm$ can be simplified to $J$,
R is the gas constant this will have the units $J/mol \cdot K$

## 2. Speed of sound in a gas is given by:
%%[[2024-09-27]] @ 17:40%%

2. Speed of sound in a gas is given by:
    $\sqrt{\gamma \cdot R \cdot T}$ 
    where:
    - $\gamma$ = ratio of specific heats 
    - $R$ = gas constant 
    - $T$ = Temperature
      
	what are the units?

$\gamma$ is unitless
$R$ in in units $J \cdot kg^{-1} \cdot K^{-1}$
T is in $K$

therefore the unit of the equation is 

$$\sqrt{\frac{J \cdot \cancel{K}}{kg \cdot \cancel{K}}} = \sqrt{J \cdot kg^{-1}}$$
as $J$ can be expressed as $Nm$ this can become
$$\sqrt{Nm \cdot kg^{-1}}$$
as $N$ can be expressed as $ma$ where mass $m$ is in $kg$ and $a$ can be expressed as $ms^{-2}$this can become
$$\sqrt{\cancel{kg} \cdot m \cdot s^{-2} \cdot \cancel{kg^{-1}} } = \sqrt{m^{2}s^{-2}} = m/s$$

## 3. Show rotational speed x Torque = power
%%[[2024-09-27]] @ 17:42%%

3. Show rotational speed x Torque = power

Rotational speed $\omega$ has the si units $s^{-1}$ 
Torque has si units $Nm$ 

Power $W$ has si units $kg \cdot m^{2} \cdot s^{-3}$ 

Making the initial equation:
$$\omega T \quad \text{in units} \quad s^{-1} \cdot Nm$$

therefore:
$$s^{-1} \cdot Nm = kg \cdot m^{2} \cdot s^{-3}$$

given $F=ma$, 
$N$ can be expressed as $kg \cdot m \cdot s^-2$ 
we can substitute that in to see the equality above holds true.

## 4. What are the units of $m \times C_{p}(\Delta T)$. 
%%[[2024-09-27]] @ 17:42%%

4. What are the units of $m \times C_{p}(\Delta T)$. 

   - $m$ is mass 
   - $C_{p}$ = specifc heat at const pressure 
   - $\Delta T$ = differential temperature

## 5. Are the units of Ut the same as ½ ft2? U = initial velocity f = acceleration t = time
%%[[2024-09-27]] @ 17:44%%

5. Are the units of Ut the same as ½ ft2? U = initial velocity f = acceleration t = time

   where:
    - $p$ = Pressure
    - $T$ = Temperature 
    - $\rho$ = density

For the equation
$$\frac{p}{T \cdot \rho}$$

$p$ is Pressure typically in kPa however the SI unit would be $N/m^{2}$
$T$ is temperature that will be in $\degree K$ 
$\rho$ is the density which will be in $kg \cdot m^{-3}$

The ideal gas constant $R$ is in units $J \cdot mol^{-1} \cdot K$
The Ideal gas constant is based on the assumption that intra-molecular energy capacity is negligible. Therefore the specific properties of the gas are not needed to find $R$. 

However given the molar weight of gasses varies an assumption would have to be made to convert the mass $kg$, implied by the density $p$, into $mol$. 

Given the ideal gas law $pV = nRT$, where since we are not interested 

$m$ molar mass is 

## 7. A tractor is pulling a plough at 2 m/s with a drag force of 500N what are the units and result?
%%[[2024-09-27]] @ 17:43%%

7. A tractor is pulling a plough at 2 m/s with a drag force of 500N what are the units and result?

8. What is the gas const R for air and its units
9. Which has the highest heat capacity at constant pressure air or steam @ 300K?
10. What is γ for air at 1000K?
11. From table A2 p913 calculate Cp for Acetylene C2H2 at 1000K
12. What is the lowest temperature a mercury in glass thermometer can read?
13. Can you float molten glass on liquid lead?
14. Which freezes first apples or tomatoes?
15. At what temperature would the dead sea freeze (20% sodium chlorate in water)?
16. How much energy is needed to convert 1kg of water into steam @ a pressure of 1.013bar?
17. This is given as hfg What is the specific density of liquid water [m3/kg] at 10,000 kPa? (& what is kPa ?)
18. Do you need extra oxygen and heating at 10,000 metres altitude?(temp & pressure)
19. How much higher could you jump as a % from sea level?
20. What is the lower and higher heating vales of gasoline fuel?
21. It takes 3 min to fill a 50litre tank with diesel on my car what is the energy transfer rate in kJ/s
22. What would be the equivalent current (amps) for this energy transfer rate if this were to charge a 12Volt battery for an electric vehicle?