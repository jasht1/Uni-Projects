
## Abstract

This report discusses a practical demonstration of a refrigeration cycle using the R634 Demonstration unit. It focuses on the impact of flow rate of coolant in the condenser.

This report dose not explicitly address the questions in the brief but in the annexes there are specific answers to each question posed.

>[!SUMMARY] Table of Contents
>    - [[Report - Energy Systems and Conversion Coursework#Abstract|Abstract]]
>        - [[Report - Energy Systems and Conversion Coursework#Symbols|Symbols]]
>    - [[Report - Energy Systems and Conversion Coursework#Introduction|Introduction]]
>        - [[Report - Energy Systems and Conversion Coursework#Background|Background]]
>            - [[Report - Energy Systems and Conversion Coursework#Carnot Cycle|Carnot Cycle]]
>            - [[Report - Energy Systems and Conversion Coursework#R634 Demonstration unit|R634 Demonstration unit]]
>                - [[Report - Energy Systems and Conversion Coursework#The role of water|The role of water]]
>            - [[Report - Energy Systems and Conversion Coursework#Coefficient of Performance COP|Coefficient of Performance COP]]
>        - [[Report - Energy Systems and Conversion Coursework#Aims|Aims]]
>    - [[Report - Energy Systems and Conversion Coursework#Methodology|Methodology]]
>        - [[Report - Energy Systems and Conversion Coursework#Experimental Methodology|Experimental Methodology]]
>        - [[Report - Energy Systems and Conversion Coursework#Analytical Methodology |Analytical Methodology ]]
>            - [[Report - Energy Systems and Conversion Coursework#State Variables|State Variables]]
>                - [[Report - Energy Systems and Conversion Coursework#Reservoir heat transfer rate |Reservoir heat transfer rate ]]
>                    - [[Report - Energy Systems and Conversion Coursework#Method 1 - Control |Method 1 - Control ]]
>                    - [[Report - Energy Systems and Conversion Coursework#Method 2 - PYroMat|Method 2 - PYroMat]]
>                    - [[Report - Energy Systems and Conversion Coursework#Method 3 - CoolProp|Method 3 - CoolProp]]
>            - [[Report - Energy Systems and Conversion Coursework#Efficiency Metrics|Efficiency Metrics]]
>                - [[Report - Energy Systems and Conversion Coursework#COP|COP]]
>                - [[Report - Energy Systems and Conversion Coursework#Isentropic Compressor Efficiency|Isentropic Compressor Efficiency]]
>            - [[Report - Energy Systems and Conversion Coursework#Carnot cycle plots|Carnot cycle plots]]
>    - [[Report - Energy Systems and Conversion Coursework#Results|Results]]
>    - [[Report - Energy Systems and Conversion Coursework#References|References]]


### Symbols
%%[[2024-11-26]] @ 14:00%%

![[Table of Symbols]]

## Introduction
### Background

#### Carnot Cycle

The Carnot cycle is an idealised thermodynamic cycle that can be used to estimate the behaviour of the refrigeration cycles used in chillers and heat pumps.

#### R634 Demonstration unit

##### The role of water
The water supplied to the unit is used as a thermal reservoir to absorb and release thermal energy predictably, that is to say without changing temperature. Naturally when water absorbs / releases energy in the condenser / evaporator respectively it dose change temperature but, by the fact that it is flowing, the system reaches a steady state with a constant and predictable temperature gradient. This average temperature at steady state is the effective temperature of the thermal reservoir.
In the experiment detailed in this report, the flow rate has been used as an independent variable to affect the system. This works by changing the effective temperature of the thermal reservoir and thus effecting the the rate at which it absorbs and emits energy.
If the temperature of the water supplied to the unit is change it will have a similar effect, varying the effective temperature of the thermal reservoirs i.e. the heat exchange coils in the evaporator and condenser.

> [!NOTE] Disambiguation
> In the R634 demonstration unit water is used to transfer heat to and from the evaporator and condenser respectively, and as such it can be seen as playing different roles depending on if it is interoperated as demonstrating a chiller or a heat pump. Throughout this report it is referred to as coolant as a linguistic compromise. At points you may prefer to translate this in your head to "heat source" "thermal transfer medium".

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

The mass flow rates determined by readings taken from rotameters placed before the coils in the R634 demonstration unit. The coils in the evaporator and condenser both have thermometers measuring the fluid temperature as it enters and leaves the respective coil as well as thermometers measuring the ambient temperature of the phase change chamber.

![[R634 Demonstration Unit Diagram (SVG) - Energy Systems and Conversion Coursework.svg]]

The tests was carried out as follows:

1. Carry out the initial setup for the R634 unit as described in the [[R634 refrigeration cycle demonstration unit manual.pdf]] which can be accessed [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/attachments/Resources/R634%20refrigeration%20cycle%20demonstration%20unit%20manual.pdf). Set the evaporator flow rate ($\dot m_c$) flow rate to $20\ \text{g/s}$ and condenser flow rate ($\dot m_c$) to $12 \ \text{g/s}$ and monitor the temperatures until they have remained constant for 5 minuets.
2. Carry out a reading, record all the variables listed in [[Table of Symbols#Experimental variables]]
3. Reduce the condenser flow rate ($\dot m_c$) by $2 \ \text{g/s}$ and allow system to stabilise as described in step 1 and repeat from step 2 until condenser flow rate ($\dot m_c$) is at it's minimum or the unit approaches a maximum condenser pressure of $150 \ kN/m^{2}$.
3. Set the evaporator flow rate ($\dot m_c$) to $10 \ \text{g/s}$ and repeat from step 2.

### Analytical Methodology 

#### State Variables

##### Reservoir heat transfer rate 

The rate of heat transfer in the evaporator and condenser can be said to be equal to the change in energy of the fluid between the input and output of their respective coils if the systems are assumed to be perfectly insulated. In practice this is of course not the case as the system will inevitably loose energy to and gain energy from the environment by means of conduction, radiation and sound.

As this is a fairly straightforward value to compute it was taken as an opportunity to compare several methodologies. 

There are many means of identifying fluid properties ranging in their ease and accuracy. In this module we are taught to seek out property tables which can be impractical at scale and prone to human error. As such I set out to understand the alternatives, of the options I found 2 stood out Pyromat and CoolProp. 

> [!Info] See [[Finding fluid properties]] in the annexes or [here in my module repo](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/Misc%20Notes/Finding%20fluid%20properties.md) for more details 

###### Method 1 - Control 

The energy change of the water across the coils can be found as the product of its specific heat capacity $c$, the change in temperature $\Delta T$, and the mass flow rate $\dot m$. 

$$\Large Q = c \dot m \Delta T $$

While specific heat capacity $c$ dose vary by temperature and pressure both of which will vary along the length of the coil and by the setting of the control valve, this will be ignored as the variation is negligible at less than $\pm 0.01 \ kJ / kg \cdot \! \degree \! K$. [^1] [^2] Therefore a value of $4.1813 \ kJ / kg \cdot \! \degree \! K$ will be used corresponding to the constant pressure specific heat capacity $c_{p}$ at a standard temperature and pressure of $298.15 \degree K$ and $101.33 \ kPa$ respectively. [^3]

[^1]: “Water - Properties vs. Temperature and Pressure.” [Online]. Available: https://www.engineeringtoolbox.com/water-properties-d_1258.html. [Accessed: 13-Nov-2024].

[^2]: “About | PYroMat.” [Online]. Available: http://www.pyromat.org/about.html. [Accessed: 13-Nov-2024].
	```python
	>>> import pyromat as pm
	>>> water = pm.get("mp.H2O")
	>>> water.cp(p=1, T=283.15) - water.cp(p=1.5, T=323.15)
	array([0.01393411]) # The variation in c_p
	```
[^3]: “About | PYroMat.” [Online]. Available: http://www.pyromat.org/about.html. [Accessed: 13-Nov-2024].
	```python
	>>> import pyromat as pm
	>>> pm.get("mp.H2O").cp(T=298.15,p=1.01325)
	array([4.1813595]) # c_p @ STP
	```

This was implemented pragmatically in python with the function seen below:

```python title=heat_flux.py
def method_1(lab_readings): # Method 1 - $q = \dot{m} c_{p} \detla T$

    c_p = 4181.3  # constant pressure specific heat capacity of water @ 101325 Pa, 298.15 K

    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    # energy transfer (W) product of mass flow rate, temperature change & specific heat capacity
    dQ_e = c_p*dT_e*lab_readings['m/t e'].values
    dQ_c = c_p*dT_c*lab_readings['m/t c'].values

    return (dQ_e,dQ_c)
```

> [!INFO] The full file `heat_flux.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/heat_flux.py)

###### Method 2 - PYroMat

PYroMat[^dQ.4] is a intuitive and lightweight python library, It's simple to make thermodynamic property queries and perfect for quick and scrappy use in the console. I could recommend 90% of the time.

[^dQ.4]: “Home | PYroMat.” [Online]. Available: http://pyromat.org/. [Accessed: 15-Nov-2024].

The function below utilises PYroMat's multi phase property model based on:

> T. Petrova, “Revised release on the iapws formulation 1995 for the thermodynamic properties of ordinary water substance for general and scientific use,” tech. rep., 2014.[^dQ.5]

[^dQ.5]: T. Petrova, “Revised release on the iapws formulation 1995 for the thermodynamic properties of ordinary water substance for general and scientific use,” tech. rep., 2014.

For more information see http://pyromat.org/pdf/handbook.pdf#chapter.7 [^dQ.6]

[^dQ.6]: "Chapter 7 Multi-phase substance models | PYroMat Handbook." [Online]. Available: http://pyromat.org/pdf/handbook.pdf#chapter.7. [Accessed: 15-Nov-2024].

```python title=heat_flux.py
def method_2(lab_readings): # Method 2 PYroMat for heat transfer rate
    import pyromat as pm

    water = pm.get("mp.H2O")  # fetches multiphase thermodynamic property model

    # specific internal energy change of the fluid across the coolant coils (kJ)
    de_e = water.e(T=lab_readings['T2'].values) - water.e(T=lab_readings['T1'].values) # evaporator coil 
    de_c = water.e(T=lab_readings['T3'].values) - water.e(T=lab_readings['T4'].values) # condenser coil  

    # energy transfer rate (W) product of energy change and mass flow rate
    dQ_e = de_e*lab_readings['m/t e'].values*1000
    dQ_c = de_c*lab_readings['m/t c'].values*1000

    return (dQ_e,dQ_c)
```

> [!INFO] The full file `heat_flux.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/heat_flux.py)


###### Method 3 - CoolProp

CoolProp[^dQ.7] is a free open source C++ implementation of REFPROP[^dQ.8] the NIST's thermodynamic property calculator. It has both high and low level functionality. It also has wrappers for anything your likely to want to use even excel. For the sake of consistency this report will only use Python.

[^dQ.7]:“Welcome to CoolProp — CoolProp 6.6.0 documentation.” [Online]. Available: http://www.coolprop.org/. [Accessed: 28-Nov-2024].

[^dQ.8]: “REFPROP,” 18-Apr-2013. [Online]. Available: https://www.nist.gov/srd/refprop. [Accessed: 28-Nov-2024].

CoolProp is slightly more involved and less convenient for quick queries but is far more capable.

```python title=heat_flux.py
def method_3(lab_readings): # Method 3 CoolProp for heat transfer rate 

    from CoolProp.CoolProp import PropsSI 

    # specific internal energy change of the fluid across the coolant coils (J)
    de_e = PropsSI('H', 'T', lab_readings['T2'].values, 'P', 101325, 'H2O') - PropsSI('H', 'T', lab_readings['T1'].values, 'P', 101325, 'H2O') # evaporator coil 
    de_c = PropsSI('H', 'T', lab_readings['T3'].values, 'P', 101325, 'H2O') - PropsSI('H', 'T', lab_readings['T4'].values, 'P', 101325, 'H2O') # condenser coil  

    # energy transfer rate (W), product of energy change and mass flow rate
    dQ_e = de_e*lab_readings['m/t e'].values
    dQ_c = de_c*lab_readings['m/t c'].values

    return (dQ_e,dQ_c)
```

> [!INFO] The full file `heat_flux.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/heat_flux.py)

#### Efficiency Metrics

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