
## Abstract

%%Table of Contents%%

### Symbols
%%[[2024-11-26]] @ 14:00%%

![[Table of Symbols]]


## Introduction
### Background

#### Coefficient of Performance COP
Coefficient of performance ($COP$) is a measure of efficiency typically associated with heat pumps and heating systems as a whole. In the case of Heat Pumps COP is the ratio of the useful heating power at the condenser per unit of electrical input power. [^1.4] $$COP = \frac{P \text{f} _{\text{Cond}}}{P_{\text{elec}}}$$
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

### Aims

## Methodology
### Experimental Methodology

All testing was done using a stock version of the R634 refrigeration cycle demonstration unit from P. A. HILTON LTD. 

![[Table of Symbols#Experimental variables]]

The main independent variable is condenser flow rate ($\dot m_c$) with evaporator flow rate ($\dot m_c$) being a secondary independent variable. 

The condenser flow rate ($\dot m_c$) was tested at regular intervals between $2 \ \text{g/s}$ to $12 \ \text{g/s}$ at a low and a high evaporator flow rate ($\dot m_c$), being $10 \ \text{g/s}$ and $20 \ \text{g/s}$ respectively.

The mass flow rates determined by readings taken from rotameters placed before the coils in the R634 demonstration unit. The coils in the evaporator and condenser both have thermometers measuring the fluid temperature as it enters and leaves the respective coil the difference between these readings is considered the temperature change.

![[R634 Demonstration Unit Diagram (SVG) - Energy Systems and Conversion Coursework.svg]]

The tests was carried out as follows:

1. Carry out the initial setup for the R634 unit as described in the [[R634 refrigeration cycle demonstration unit manual.pdf]] which can be accessed [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/attachments/Resources/R634%20refrigeration%20cycle%20demonstration%20unit%20manual.pdf). Set the evaporator flow rate ($\dot m_c$) flow rate to $20\ \text{g/s}$ and condenser flow rate ($\dot m_c$) to $12 \ \text{g/s}$ and monitor the temperatures until they have remained constant for 5 minuets.
2. Carry out a reading, record all the variables listed in [[Table of Symbols#Experimental variables]]
3. Reduce the condenser flow rate ($\dot m_c$) by $2 \ \text{g/s}$ and allow system to stabilise as described in step 1 and repeat from step 2 until condenser flow rate ($\dot m_c$) is at it's minimum or the unit approaches a maximum condenser pressure of $150 \ kN/m^{2}$.
3. Set the evaporator flow rate ($\dot m_c$) to $10 \ \text{g/s}$ and repeat from step 2.

### Analytical Methodology 

#### Efficiency

##### COP
As discussed in the [[#Background#Coefficient of Performance COP]] section COP depends heavily on the system boundaries chosen. This methodology defines the system boundaries at: 
- Input: work done to refrigerant by the compressor
- Output: work done by the refrigerant in the condenser

Making COP a measure of:
$$\Large COP = \frac{\dot Q _\text{condensation} }{P_{\text{compression}}}$$
Where:
$\dot Q _\text{condensation}$ : rate of heat released by the refrigerant in the condenser
$P_{\text{compression}}$ : effective power of the compressor

Under the assumption that all work done in the condenser is converted to heat, which is a reasonable approximation, $Q$ becomes $W$. Further all work done to and by the refrigerant $W$ is to be represented by the sum of it's change in enthalpy $H$, and time $t$.
$$COP = \frac{\dot Q _\text{condensation} }{P_{\text{compression}}} \triangleq \frac{\delta H_{\text{cond}} \times t}{\delta H_{\text{comp}} \times t}$$
As the the refrigerant is in an essentially closed system that has been allowed to reach a steady state, the mass flow rate is uniform through out. As such we can cancel it out from numerator and denominator to give: $$\frac{\delta H_{\text{cond}} \times t}{\delta H_{\text{comp}} \times t} \div \frac{mt^{-1}}{mt^{-1}} = \frac{\delta h_{\text{cond}}} {\delta h_{\text{comp}}}$$
The enthalpy of the refrigerant in this case SES36 can be found based on it's temperature and pressure using a thermodynamic chart, table or model. The source used to predict the enthalpy will effect the values as in all cases they are approximations. It is important to verify that the model is sufficiently accurate in the temperature/pressure range you are working in and that it is from a reputable source. In this case the model is based on:

> Monika Thol, Eric W. Lemmon, and Roland Span. Equation of State for a Refrigerant Mixture of R365mfc (1,1,1,3,3-Pentafluorobutane) and Galden HT 55 (Perfluoropolyether). Unpublished, 2012.[^2.1]

[^2.1]:  Monika Thol, Eric W. Lemmon, and Roland Span. Equation of State for a Refrigerant Mixture of R365mfc (1,1,1,3,3-Pentafluorobutane) and Galden HT 55 (Perfluoropolyether). Unpublished, 2012.

Despite being unpublished this was chosen based on recognition of one of the authors Eric W. Lemmon who is prolific in the field having developed 2 of the most predominant methodologies for identifying equations of state[^2.2] as well as RefProp the NIST's thermodynamic property calculator[^2.3]. It was also verified by visualy comparing the P-H diagram it produces against the one included in the annexes of the [[R634 refrigeration cycle demonstration unit manual.pdf]].

[^2.2]:  E. W. Lemmon and R. Tillner-Roth, “A Helmholtz energy equation of state for calculating the thermodynamic properties of fluid mixtures,” 04-Nov-1999. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0378381299002629. [Accessed: 28-Nov-2024].

[^2.3]: “Eric W. Lemmon,” 09-Oct-2019. [Online]. Available: https://www.nist.gov/people/eric-w-lemmon. [Accessed: 28-Nov-2024].

By assuming no change in temperature enthalpy change in the condenser can be found as the difference between the enthalpy of the refrigerant SES36 at saturated vapour vs saturated liquid.
%% Similarly to find the work done to the refrigerant by the compressor  %%By assuming that the temperature and pressure of the refrigerant at the inlet of the compressor are the same as they where at the evaporator, and that the refrigerant is in a state of saturated vapour the initial enthalpy can be found. The final enthalpy is the same but based on the compressor discharge temperature and the condenser pressure.

This was implemented problematically using CoolProp[^2.4] as seen below:

[^2.4]: “SES36 — CoolProp 6.6.0 documentation.” [Online]. Available: http://www.coolprop.org/fluid_properties/fluids/SES36.html. [Accessed: 28-Nov-2024].

```python title="cop.py"
def method_1(lab_readings):
    from CoolProp.CoolProp import PropsSI 
    material = 'SES36'

    # Condenser enthalpy change
    P_initial = lab_readings['p c'].values
    T_initial = lab_readings['T6'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = P_initial
    T_final = T_initial

    H_final = PropsSI('H', 'T', T_final, 'P|liquid', P_final, material)

    dH_condensation = H_initial - H_final

    # Compressor ethalpy change
    P_initial = lab_readings['p e'].values
    T_initial = lab_readings['T5'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = lab_readings['p c'].values
    T_final = lab_readings['T7'].values

    H_final = PropsSI('H', 'T', T_final, 'P|gas', P_final, material)

    dH_compression = H_initial - H_final

    cop = abs(dH_condensation/dH_compression)

    return cop

```

> [!INFO] The full file `cop.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/cop.py)

##### Isentropic Compressor Efficiency
Isentropic compressor Efficiency ($\eta_s$) is a measure of performance based on the ratio of the work necessary to achieve the compression isentropically (the ideal case where no entropy is added) over the actual work done. $$\Large \eta_{s}= \frac{W_\text{isentropic}}{W_\text{actual}}$$

This was implemented pragmatically with the function seen below:

```python title="cop.py"
def isentropic_efficiency(T_in, P_in, T_out, P_out):
    import CoolProp.CoolProp as CP

    h_in = CP.PropsSI('H', 'T', T_in, 'P|gas', P_in, "SES36")
    S_in =  CP.PropsSI('S', 'T', T_in, 'P|gas', P_in, "SES36")

    h_out_max = CP.PropsSI('H', 'S', S_in, 'P|gas', P_out, "SES36")
    h_out_actual = CP.PropsSI('H', 'T', T_out, 'P|gas', P_out, "SES36")

    return (h_out_max-h_in)/(h_out_actual-h_in)
```

> [!INFO] The full file `cop.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/cop.py)

## Results

![[Refrigeration_Cycle_Plots_(wo compression, linear).svg]]

## References