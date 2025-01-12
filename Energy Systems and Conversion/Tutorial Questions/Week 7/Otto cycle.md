
# Otto Cycle

## Summary
%%[[2024-11-08]] @ 15:18%%

The [[Otto cycle]] is an idealised thermodynamic engine cycle that can be applied to reciprocating spark ignition engines.

![Otto Cycle animation](https://edxengine-projects-files.s3.amazonaws.com/1589027088.gif)

![[Otto cycle - PV chart.excalidraw]]

1. Exhaust/Intake: Isochoric cooling & pressure drop
	The hot gas is expelled and fresh air is drawn in

2. Compression Stroke: Isentropic compression
   The piston reduces the combustion chamber volume thereby increasing the pressure.

3. Ignition: Isochoric heating & pressure increase
	At top dead centre the the fuel is ignited causing a rapid increase in pressure.

4. Power Stroke: Isentropic expansion and cooling
	The pressure drives the piston increasing the volume


## Relevant Equations

### Energy balance
%%[[2024-11-10]] @ 17:37%%

$$(q_{in}-q_{out}) + (w_{in}-w_{out}) = \Delta u $$

### Efficiency
%%[[2024-11-10]] @ 17:38%%

The efficiency of an ideal [[Otto cycle]] engine is given by:
$$\eta _{th} = \frac{1}{r^{k-1}}$$

Compression ratio is simply:
$$r_{c} = \frac{v_{max}}{v_{min}}$$

Mean effective pressure is given by:
$$\bar P = \frac{W_{net}}{V_{max}-V_{min}} = \frac{w_{net}}{v_{max}-v_{min}}$$

## Example 

An ideal Otto cycle has a compression ratio of $8$. At the beginning of the compression process, air is at $100 kPa$ and $17°C$, and $800 kJ/kg$ of heat is transferred to air during the constant-volume heat-addition process. [[Lecture 7.1 - GAS POWER CYCLES.pdf#page=20|Lecture 7.1 - GAS POWER CYCLES, page 20]]

![[Otto cycle - PV chart.excalidraw]]

### Compression stroke
%%[[2024-11-08]] @ 15:59%%

#### Initial state
Air starts at:
$P = 100kPa$
$T = 17 \degree C \to 290.15 \degree K$

Given this we can find its ideal specific mass as: 
$v = 0.816 m^{3}/kg$

#### Change
It is compressed by a factor of 8:
$r_{c} = 8$
The process is approximated to be adiabatic (constant temperature) where $P V^{\gamma} = k$ applies.
Given this we can state 
$$P_{1}  V_{1}^{\gamma} = P_{2} V_{2}^{\gamma}$$
#### Final state
Final temperature and pressure can be found with:
$$\begin{align*}
T_{2} = T_{1} * r_{c}^{(\gamma - 1)} \quad &\to \quad 290.15 \times 8^{1.4-1} = 666.59\\
P_{2} = P_{1} * r_{c}^{(\gamma - 1)} \quad &\to \quad 100 \times 8^{1.4-1} = 229.74
\end{align*}$$

`290.15*8**0.4=` `$=290.15*8**0.4` 
`100*8**0.4=` `$=100*8**0.4` 

%%
Using this the final pressure can be calculated with:
*From [[combined gas law]]*

$$P_{2} = P_{1} \frac{T_{2}}{T_{2}} = 100 \times 8^{1.4-1}$$
%%

%%
I'm confused as to why the reported specific volume dosen't change for the given increases in temperature and pressure of the compression stroke.
%%

### Ignition
%%[[2024-11-08]] @ 22:12%%

It is given that the ignition should be approximated as an increase of $800 kJ/kg$ of heat to the air. So we use it's state at the end of the compression stroke to find its specific internal energy, and add 800 to find the state post ignition.

$$u_{3} = u_{2}+800$$

%%
I'm having issues getting reasonable values of internal energy, the method `e` proports to return internal energy in `unit_energy / unit_matter` which I have configured to kJ and kg respectively. 
for $T=660 \degree C$ the method returns $184$ where the [[thermodynamic property tables.pdf]] report $481.01$ so something isn't right.
%%

### Script

```python title:"compression stroke"
>>> import pyromat as pm
>>> air = pm.get('ig.air')
>>> t_intake = 290.15
>>> p_intake = 1
>>> v_intake = air.v(t_intake, p_intake)
v_intake -> array([0.83288329])

>>> pt_ratio = pow(8,air.gam(t_intake, p_intake)-1)
>>> t_tdc = t_intake*pt_ratio
t_tdc -> array([666.88134891])

>>> p_tdc = p_intake*pt_ratio
p_tdc -> array([2.29840203])

>>> v_tdc=air.v(T=t_tdc, p=p_tdc)
v_tdv -> array([0.83288329])

>>> v_ignition=v_tdc
v_ignition -> array([0.83288329])

>>> u_ignition=air.e(T=t_tdc, p=p_tdc)+800
u_ignition -> array([983.97154997])

>>> t_ignition=air.T(e=u_ignition, v=v_ignition)
```

```
import pyromat as pm
air = pm.get('ig.air')
t_intake = 290.15
p_intake = 1
air.v(t_intake, p_intake)
v_intake = air.v(t_intake, p_intake)
pt_ratio = pow(8,air.gam(t_intake, p_intake)-1)
t_tdc = t_intake*pt_ratio
p_tdc = p_intake*pt_ratio
v_tdc=air.v(T=t_tdc, p=p_tdc)+800
v_ignition=v_tdc
u_ignition=air.e(T=t_tdc, p=p_tdc)+800
t_ignition=air.T(e=u_ignition, v=v_ignition)
```
