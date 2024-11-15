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

%% The energy change of the fluid in the coils is a sum of the latent and sensible heat *no it's not there's no state change in the coils* %%

The energy change of the water across the coils can be found as the product of its specific heat capacity $c$, the change in temperature $\Delta T$, and the mass flow rate $\dot m$. 

$$\Large Q = c \dot m \Delta T $$

While specific heat capacity $c$ dose vary by temperature and pressure both of which will vary along the length of the coil and by the setting of the control valve, this will be ignored as the variation is negligible at less than $\pm 0.01 \ kJ / kg \cdot \! \degree \! K$. [^1] [^2] Therefore a value of $4.1813 \ kJ / kg \cdot \! \degree \! K$ will be used corresponding to the constant pressure specific heat capacity $c_{p}$ at a standard temperature and pressure of $298.15 \degree K$ and $101.33 \ kPa$ respectively. [^3]

[^1]: “Water - Properties vs. Temperature and Pressure.” [Online]. Available: https://www.engineeringtoolbox.com/water-properties-d_1258.html. [Accessed: 13-Nov-2024].

[^2]: “About | PYroMat.” [Online]. Available: http://www.pyromat.org/about.html. [Accessed: 13-Nov-2024].
	```python
	>>> import pyromat as pm
	>>> water = pm.get("mp.H2O")
	>>> water.cp(p=1, T=283.15) - water.cp(p=1.5, T=323.15)
	array([0.01393411])
	```
[^3]: “About | PYroMat.” [Online]. Available: http://www.pyromat.org/about.html. [Accessed: 13-Nov-2024].
	```python
	>>> import pyromat as pm
	>>> pm.get("mp.H2O").cp(T=298.15,p=1.01325)
	array([4.1813595])
	```

The mass flow rates are readings taken from rotameters placed before the coils in the R634 demonstration unit, 

%% Diagram with Rotometers highlighted %%



### b) Appropriately tabulate your results. 
[10 marks]

## Question 2
### a) For each flow rate in your table, determine the COP of the system. 
[10 marks]
### b) Plot the COP against the saturation or condensing temperature. 
[10 marks]
## Question 3
### a) Plot the pressure vs temperature for the evaporator and condenser at the different water flow rates. 
[10 marks]
### b) Discuss the trend and any other observations. 
[10 marks]
## Question 4
### a) Plot the evaporator and condenser heat transferred against temperature 
[10 marks]
### b) Discuss the trend and any other observations. 
[10 marks]
## Question 5
### Explain what happens if the water supplied into the unit is cooled or warmed below and above those used in tasks 1-4 above? How will the heat transferred, and COP be affected? 
[5 marks]
## Question 6
### It is proposed that water should be used as the refrigerant instead of R-134a in an air conditioner where the minimum temperature never goes below the freezing point. Would you support this proposal or not? Kindly explain. 
[5 marks]
### Pay particular attention to detail, appropriately formatting your report with a good introduction, procedure, diagrams of experimental with appropriate labelling, discussion accompanying your answers, and uncertainty analysis. 
[10 marks]
