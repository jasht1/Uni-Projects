# Question 2

## Question

![[Week 2 - Entropy - TUTORIALS - w solutions.pdf#page=4|Week 2 - Entropy - TUTORIALS - w solutions, page 4]]

# Find the entropy change $\Delta s$ for an Isobaric process

## Givens

Isobaric process (constant pressure)

Constants:
- $m = 1.5 \ kg$
- $P = 150 \ kPa$

Initial state: 
- Compressed liquid water
- $T_{1} = 20 \degree C$

Change:
- $\Delta Q = 4000 kJ$

### Secondary Givens

Given that:
- Pressure $P$ is constant,
- $P = 150 \ kPa$

We can consult the [[thermodynamic property tables.pdf]] saturated water table A-5,
to find the:
- saturation temperature @ $150 \ kPa$: $T_{sat} = 111.35 \degree C$ 

And,

Given that:
- Compressed Liquid Water
- $T_{1} = 20 \degree C$
- $P = 150 \ kPa$

As the pressure is fairly low we can approximate the entropy and enthalpy with the values for saturated water of the same temperature.
We can consult the [[thermodynamic property tables.pdf]] saturated water table A-5,
to find the:
- Initial entropy $s_{1}$: $s_{f} = 0.2965\ kJ\! \cdot \! kg^{-1} \! \cdot \! K^{-1}$ @ $20 \degree C$ 
- Initial enthalpy $h_{1}$: $h_{f} = 83.915 \ kJ \! \cdot \! kg^{-1}$ @ $20 \degree C$ 

## Finding final entropy

We can find the final entropy based on the final enthalpy $h_{2}$ as we know the initial enthalpy $h_{1}$, the energy added $\Delta Q$ and the mass $m$.

$$h_{2} = h_{1} + \frac{\Delta Q }{m}$$
`83.915+4000/1.5 =` `=83.915+4000/1.5` 
$$h_{2} = 83.915 \ (kJ \! \cdot \! kg^{-1}) + \frac{4000 \ (kJ)}{1.5 \ (kg)} = 2750.582 \ (kJ \! \cdot \! kg^{-1})$$

Checking the [[thermodynamic property tables.pdf]] saturated water pressure table A-5 entry for $150 \ kPa$ we can see an enthalpy of $2750.582 \ kJ \! \cdot \! kg^{-1}$ is higher than the enthalpy of saturated vapour $h_{g} \ @ 150 \ kPa = 2693.1 \ kJ \! \cdot \! kg^{-1}$ so we know it reaches the Super-heated state. 

To find the final entropy we must check the [[thermodynamic property tables.pdf]] Super-heated water table A-6. The closest entries to our final enthalpy $h_{2}$ of $2750.582 \ kJ \! \cdot \! kg^{-1}$ are for $100 \degree C$ and $150 \degree C$, which are $2675.8 \ kJ \! \cdot \! kg^{-1}$ and $2776.6 \ kJ \! \cdot \! kg^{-1}$ respectively. 

As the enthalpy we are looking for is very close to the higher of these, we can approximate it with linear interpolation to extrapolate backwards from it.

$$s_{actual}\approx s_{higher} - (h_{higher} - h_{actual}) \times \frac{s_{higher}-s_{lower}}{h_{higher} - h_{lower}}$$

This essentially reduces the the entropy value at $150 \degree C$ $(s_{higher})$ by the difference in our enthalpy $(h_{actual})$ and the enthalpy at $150 \degree C$ $(h_{higher})$ multiplied by the rise over run gradient implied by the known entropys and enthalpys for $100 \degree C$ and $150 \degree C$.

`7.6148-(2776.6-2750.582)((7.6148-7.3611)/(2776.6-2675.8))=` `=7.6148-(2776.6-2750.582)*((7.6148-7.3611)/(2776.6-2675.8))`

$$s_{actual} \approx 7.6148-(2776.6-2750.582) \times\frac{(7.6148-7.3611)}{(2776.6-2675.8)} = 7.5493$$
$$\therefore$$
$$s_{2} \approx  7.5493\ kJ\! \cdot \! kg^{-1} \! \cdot \! K^{-1}$$

## Finding entropy change

Entropy change is now simply the difference between initial entropy $s_1$ and final entropy $s_{2}$
$$\Delta s = | s_{2} - s_{1} |$$
`7.5493-0.2965=` `=7.5493-0.2965`

$$\Delta s \approx | 7.5493 - 0.2965| = 7.2528$$

$$\Delta s \approx 7.2528\ kJ\! \cdot \! kg^{-1} \! \cdot \! K^{-1}$$
