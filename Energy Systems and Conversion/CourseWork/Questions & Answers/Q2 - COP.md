## Question 2
### a) For each flow rate in your table, determine the COP of the system. 
[10 marks]

#### Background
[[coefficient of performance (COP)]] is a measure of performance typically associated with heat pumps and heating systems as a whole. In the case of Heat Pumps COP is the ratio of the useful heating power at the condenser per unit of electrical input power. [^1.4] $$COP = \frac{P \text{f} _{\text{Cond}}}{P_{\text{elec}}}$$
Where:
$P \text{f} _\text{Cond}$ : Heating capacity of the condenser ($kW$)
$P_{\text{elec}}$ : Input electrical power ($kW$)

Being a critical measure of energy efficiency there are strict and standardised methodologies for testing and calculating COP[^1.0]. On top of this manufacturer COP claims are often verified by 3rd party organisations via various certification schemes[^1.1] like KEYMARK[^1.2], Qlable and Eurovent[^1.3]. This is necessary as for COP values to be a useful in communicating system performance they must be comparable, like for like with other known values.

The measures available in this experiment are not sufficient to determine of electrical input power or the heating capacity of the condenser as such any approximation of COP will not be comparable with values for heat pumps taken in accordance with the standards. The COP's calculated and discussed from this point onwards apply only to the refrigeration cycle itself, and should only be compared with values based on the same system boundaries.

[^1.0]: Heating systems and water based cooling systems in buildings. Method for calculation of system energy requirements and system efficiencies. Part 4-2. Space heating generation systems, heat pump systems, BS EN 14511‐3, 2018.
	[Download](http://libgen.li/ads.php?md5=4ce494840861f0e960bfb21a1088a59b)
[^1.1]: “EHPA Certification.” [Online]. Available: https://www.ehpa.org/quality/. [Accessed: 22-Nov-2024].
[^1.2]: “Testing and Certification.” [Online]. Available: https://keymark.eu/en/products/heatpumps/testing-and-certification. [Accessed: 22-Nov-2024].
[^1.3]: “NF414 | Eurovent Certita Certification.” [Online]. Available: https://www.eurovent-certification.com/en/third-party-certification/certification-programmes/nf414. [Accessed: 22-Nov-2024].
[^1.4]: Certification reference standard NF 414, AFNOR NF 414, 2024. Available: https://www.eurovent-certification.com/media/images/349/3c3/3493c319d9de88e18e3ecea2156c1e8d6521a7d4.pdf

#### Methodology
%%[[2024-11-24]] @ 13:44%%

This methodology defines the system boundaries at: 
- Input: work done to refrigerant by the compressor
- Output: work done by the refrigerant in the condenser

Making COP a measure of:
$$COP = \frac{\dot Q _\text{condensation} }{P_{\text{compression}}}$$
Where:
$\dot Q _\text{condensation}$ : rate of heat released by the refrigerant in the condenser
$P_{\text{compression}}$ : effective power of the compressor

Under the assumption that all work done in the condenser is converted to heat, which is a reasonable approximation, $Q$ becomes $W$. Further all work done to and by the refrigerant $W$ is to be represented by the sum of it's change in enthalpy $H$, and time $t$.
$$COP = \frac{\dot Q _\text{condensation} }{P_{\text{compression}}} \triangleq \frac{\delta H_{\text{cond}} \times t}{\delta H_{\text{comp}} \times t}$$
As the the refrigerant is in an essentially closed system that has been allowed to reach a steady state the mass flow rate is uniform through out. As such we can divide it from numerator and denominator to give: $$\frac{\delta H_{\text{cond}} \times t}{\delta H_{\text{comp}} \times t} \div \frac{mt^{-1}}{mt^{-1}} = \frac{\delta h_{\text{cond}}} {\delta h_{\text{comp}}}$$
If the condenser is assumed to be be perfectly insulated the 
Where the COP of the refrigeration cycle is: $$COP = \frac{h_{2} - h_{3}}{h_{2} - h_{1}}$$
```python title="cop.py"
def method_1(lab_readings):

    from CoolProp.CoolProp import PropsSI 

    material = 'SES36'

    P_initial = lab_readings['p e'].values
    T_initial = lab_readings['T5'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = lab_readings['p c'].values
    T_final = lab_readings['T7'].values

    H_final = PropsSI('H', 'T', T_final, 'P|gas', P_final, material)

    dH_compression = H_initial - H_final

    P_initial = lab_readings['p c'].values
    T_initial = lab_readings['T6'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = P_initial
    T_final = T_initial

    H_final = PropsSI('H', 'T', T_final, 'P|liquid', P_final, material)

    dH_condensation = H_initial - H_final

    cop = abs(dH_condensation/dH_compression)

    return cop
```

%% 
#### Removed Sections

##### Approximating Condenser Power
If not measured directly the heating capacity of the condenser is calculated with the following formula [^1.4]: $$P \text{f} _\text{Cond} = \dot{m}_{\text{ff}} \times \left( h_\text{in} - h_\text{out} \right)$$
Where:
$P \text{f} _\text{Cond}$ : Heating capacity of the condenser ($kW$)
$\dot{m}_{\text{ff}}$ : flow of liquid refrigerant in ($kg/s$)
$h_\text{in}$ : enthalpy corresponding to the inlet pressure & temperature in ($kJ/k$)
$h_\text{out}$ : enthalpy corresponding to the inlet pressure & temperature in ($kJ/k$)

##### Approximating Compressor Power
[[2024-11-22]] @ 13:45  

As the input electrical power $P_{\text{elec}}$ has not been measured directly an approximation will have to be made this is not ideal and will be a major source of uncertainty.

##### Details from [[R634 refrigeration cycle demonstration unit manual.pdf]]

> Hermetic type compressor with integral 1/2 Horsepower motor drawing approximately 810 Watts. The compressor is a single cylinder reciprocating type with a displacement of 17.4 cubic centimetres.

[[R634 refrigeration cycle demonstration unit manual.pdf#page=18&selection=7,0,42,12|R634 refrigeration cycle demonstration unit manual, page 18]]


|                                |     |     |
| ------------------------------ | --- | --- |
| Condenser Gauge Pressure (kPa) | 15  | 190 |
| Compressor Power Input (W)     | 274 | 302 |

[[R634 refrigeration cycle demonstration unit manual.pdf#page=60&selection=129,0,133,0|R634 refrigeration cycle demonstration unit manual, page 60, Table 9]]
%%

### b) Plot the COP against the saturation or condensing temperature. 
[10 marks]

#### Plotting Cycles over SES36 Iso Lines on a PH diagram
%%[[2024-11-26]] @ 19:35%%

For some more intuition It's worth seeing what the cycles look like, below are idealised approximations of what all the cycles would have been for the flow rates tested.

![[Incomplete Refrigeration Cycle Plots.svg]]

To achieve this I wrote the following `plot_PH` function. It's based on [this](https://stackoverflow.com/questions/70864726/put-labels-in-coolprop-chart) example I found on stack overflow[^2.3.2] utilising my `isentropic_efficiency` function mentioned above along with with the [SimpleCyclesCompression module](http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html) from coolProp[^2.3.1]. It is part of the [[cop.py]] file that can be seen in it's entirety in the annexes or [here in the repo](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/cop.py).

[^2.3.2]: “Put labels in Coolprop Chart.” [Online]. Available: https://stackoverflow.com/questions/70864726/put-labels-in-coolprop-chart. [Accessed: 26-Nov-2024].

[^2.3.1]: “CoolProp.Plots.SimpleCyclesCompression module — CoolProp 6.6.0 documentation.” [Online]. Available: http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html. [Accessed: 26-Nov-2024].

```python title=plot_PH
def plot_PH(lab_readings):
    import CoolProp.CoolProp as CP
    from CoolProp.Plots import PropertyPlot
    from CoolProp.Plots import SimpleCompressionCycle
    import matplotlib.pyplot as plt

    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_comp = lab_readings["T7"].values
    P_comp = lab_readings["p c"].values

    eta_com = isentropic_efficiency(T_evap,P_evap,T_comp,P_comp)

    ph_plt = PropertyPlot('SES36', 'PH', unit_system='KSI')

    ph_plt.xlabel("h [kJ/kg]")
    ph_plt.ylabel("P [kPa]")

    ph_plt.calc_isolines(CP.iQ)

    cycle = SimpleCompressionCycle("SES36", "PH", unit_system="KSI")

    print(CP.PropsSI('Phase', 'T', T_evap, 'P', P_evap, "SES36"))
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    print(CP.PhaseSI('T', T_evap[0], 'P', P_evap[0], "SES36"))
    print(CP.PhaseSI('T', T_comp[1], 'P', P_comp[1], "SES36"))

    for entry in zip(T_evap,P_evap,T_comp,P_comp, eta_com):
        cycle.simple_solve(*entry)
        sc = cycle.get_state_changes()
        ph_plt.draw_process(sc)

    ph_plt.title("Refrigeration Cycles on P-h Diagram")
    ph_plt.grid()
    ph_plt.show()
```

##### Issues
%%[[2024-11-26]] @ 19:35%%

I'm having some trouble getting the `SimpleCOmpressionCycle.simple_solver` method to complete the cycles. It will only plot the compression stage points provided failing to find the values for the liquid states. 
![[Incomplete Refrigeration Cycle Plots.svg]]

Note that only 7 of the 23 cycles are complete.

If I add a few lines to check the predicted state of the refrigerant at the values indicated for compressor inlet and outlet, pressure and temperature:
```python
    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_comp = lab_readings["T7"].values
    P_comp = lab_readings["p c"].values

    print(CP.PropsSI('Phase', 'T', T_evap, 'P', P_evap, "SES36"))
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
```

It ouputs the following for;
- Inlet: `[5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]`
- Outlet: `[0. 0. 5. 5. 5. 5. 5. 5. 5. 5. 5. 0. 5. 0. 0. 0. 5. 0. 5. 5. 5. 5. 5.]`

where `5` indicates gas, and `0` indicates liquid. Interestingly also 7 instances where the outlet phase was predicted to be liquid. Of course the pump can't be dealing with phase changes else there would be cavitation and all sorts of issues. 

I wrote a quick function to check how much I would have to change the values to push them all into liquid phase:

```python
def check_state(lab_readings):
    import CoolProp.CoolProp as CP

    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_comp = lab_readings["T7"].values
    P_comp = lab_readings["p c"].values

    print(CP.PropsSI('Phase', 'T', T_evap, 'P', P_evap, "SES36"))
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    print(CP.PhaseSI('T', T_evap[0], 'P', P_evap[0], "SES36"))
    print(CP.PhaseSI('T', T_comp[1], 'P', P_comp[1], "SES36"))

    # Check difference for temperature adjustment
    print(T_comp)
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    T_comp_sat = (CP.PropsSI('T', 'Q', 1.0, 'P', P_comp, "SES36"))
    print(T_comp_sat)
    print(CP.PropsSI('Phase', 'T', T_comp_sat, 'P', P_comp, "SES36"))

    print (T_comp-T_comp_sat)

    # Check difference for temperature adjustment
    print(P_comp)
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    P_comp_sat = (CP.PropsSI('P', 'Q', 1.0, 'T', T_comp, "SES36"))
    print(P_comp_sat)
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp_sat, "SES36"))

    print (P_comp-P_comp_sat)
```

and this is what it spat out:
- For outlet Temperature:
	- Current values are:
		`[333.9  333.9  333.4  334.15 334.65 341.15 342.15 341.15 342.15 342.15 342.15 335.15 335.15 332.15 332.15 332.15 333.15 337.15 335.15 335.15 335.15 337.15 337.15] `
	- Adjusted values would be:
	  `[336.32859836 334.58300919 333.3785215  333.3785215  333.3785215 339.09075948 336.04252383 334.13530266 333.3785215  333.07199452 332.60800168 336.47093127 334.58300919 333.22553503 332.76323261 332.29581558 332.13885048 338.4163316  335.02608424 333.3785215 332.91789529 332.29581558 331.9812973 ]`
	- Possible with a adjustments of:
		`[-2.42859836 -0.68300919  0.0214785   0.7714785   1.2714785   2.05924052 6.10747617  7.01469734  8.7714785   9.07800548  9.54199832 -1.32093127 0.56699081 -1.07553503 -0.61323261 -0.14581558  1.01114952 -1.2663316 0.12391576  1.7714785   2.23210471  4.85418442  5.1687027 ]`
- For Outlet Pressure:
	- Current values are:
		`[241325 229325 221325 221325 221325 261325 239325 226325 221325 219325 216325 242325 229325 220325 217325 214325 213325 256325 232325 221325 218325 214325 212325] `
	- Adjusted values would be:
		`[224760.84184103 224760.84184103 221465.68359062 226422.98611947 229776.59909676 277069.49076882 284979.85730193 277069.49076882 284979.85730193 284979.85730193 284979.85730193 233169.57068941 233169.57068941 213395.90881022 213395.90881022 213395.90881022 219832.59212109 247141.29339878 233169.57068941 233169.57068941 233169.57068941 247141.29339878 247141.29339878]`
	- Possible with a adjustments of:
		`[ 16564.15815897   4564.15815897   -140.68359062  -5097.98611947 -8451.59909676 -15744.49076882 -45654.85730193 -50744.49076882 -63654.85730193 -65654.85730193 -68654.85730193   9155.42931059 -3844.57068941   6929.09118978   3929.09118978    929.09118978 -6507.59212109   9183.70660122   -844.57068941 -11844.57068941 -14844.57068941 -32816.29339878 -34816.29339878]`

Based on this I've figured that instead of using the compressor discharge temperature I should use the condenser temperature so that the little super-cooling between will push it past the critical point.