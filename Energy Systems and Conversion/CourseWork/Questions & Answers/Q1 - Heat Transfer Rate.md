## Question 1
### a) Calculate the heat transferred in the evaporator and condenser (in Watts) for each of the water flow rates above 
[10 marks]

> [!NOTE] Ambiguity
> It should be noted that when being used as an approximation of internal energy heat is measured in joules ($J$) and so the heat transferred would be too. However it is fair to assume this question intends to ask for the heat transfer rate and not it's quantity.

The rate of heat transfer in the evaporator and condenser can be said to be equal to the change in energy of the fluid between the input and output of their respective coils *(highlighted in figure _n_ below)* if the systems are assumed to be perfectly insulated. In practice this is of course not the case as the system will inevitably loose energy to and gain energy from the environment by means of conduction, radiation and sound. If this is to be considered, with the aim of distinguishing between:
1. energy transferred within the evaporator/condenser from refrigerant to coolant and,
2. energy transfer of the evaporator/condenser to and from the environment,

then one would have to measure the energy change of the refrigerant and coolant independently. 

%% then independent measures of the energy change in the refrigerant and coolant would be necessary. %%

%% *Add Figure with coils highlighted* %%

%% The energy change of the fluid in the coils is a sum of the latent and sensible heat *! no it's not there's no state change in the coils* %%

In this case the following measures have been recorded:

| Symbol        | Label   | Description                                                                              |
| ------------- | ------- | ---------------------------------------------------------------------------------------- |
| $\dot{m}_c$   | `m/t_c` | **Mass flow rate** of the water in the heat transfer coils of the **condenser**.         |
| $\dot m_{e}$  | `m/t_e` | **Mass flow rate** of the water in the heat transfer coils of the **evaporator**.        |
| $T_{e^{in}}$  | `T1`    | **Temperature** of the water **entering** the heat transfer coils of the **evaporator**. |
| $T_{e^{out}}$ | `T2`    | **Temperature** of the water **leaving** the heat transfer coils of the **evaporator**.  |
| $T_{c^{out}}$ | `T3`    | **Temperature** of the water **leaving** the heat transfer coils of the **condenser**.   |
| $T_{c^{in}}$  | `T4`    | **Temperature** of the water **entering** the heat transfer coils of the **condenser**.  |
| $T_{E}$       | `T5`    | **Temperature** of the evaporation chamber                                               |
| $T_{C}$       | `T6`    | **Temperature** of the condensing chamber                                                |
| $p_{E}$       | `p_e`   | **Pressure** of the evaporation chamber                                                  |
| $p_{C}$       | `p_c`   | **Temperature** of the evaporation chamber                                               |
| $T_{sh}$      | `T7`    | **Temperature** of the refrigerant leaving the compressor                                |

The mass flow rates are readings taken from rotameters placed before the coils in the R634 demonstration unit. The coils in the evaporator and condenser both have thermometers measuring the fluid temperature as it enters and leaves the respective coil the difference between these readings is considered the temperature change.

%% Diagram with Rotometers highlighted %%

#### Method 1 %% - Decide on a name %%

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

#### Method 2 - PYroMat


```python title=heat_flux.py
def method_2(lab_readings): # Method 2 PYroMat for heat transfer rate

    import pyromat as pm

    """
    utilising pyromat multi phase property model based on:
      - T. Petrova, “Revised release on the iapws formulation 1995 for the
        thermodynamic properties of ordinary water substance for general
        and scientific use,” tech. rep., 2014. 
    For more information see http://pyromat.org/pdf/handbook.pdf#chapter.7
    """

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


#### Method 3 - CoolProp

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


### b) Appropriately tabulate your results. 
[10 marks]

> [!INFO] All key values calculated are tabulated in `All Data.csv` which can be found in the annex and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/attachments/SpreadSheets/All%20Data.csv)

