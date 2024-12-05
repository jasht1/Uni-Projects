
### plot_cycles.py
[View here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/plot_cycles.py)

#### Plotting Cycles over SES36 Iso Lines on a PH diagram
%%[[2024-11-26]] @ 19:35%%

For some more intuition It's worth seeing what the cycles look like, below are idealised approximations of what all the cycles would have been for the flow rates tested.

![[Refrigeration_Cycle_Plots_(wo compression, linear).svg]]

To achieve this I wrote the `plot_PH` function that can be found in [plot_cycles.py](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/plot_cycles.py). It's based loosely on [this](https://stackoverflow.com/questions/70864726/put-labels-in-coolprop-chart) example I found on stack overflow[^2.3.2] utilising my `isentropic_efficiency` function mentioned above along with with the [SimpleCyclesCompression module](http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html) from coolProp[^2.3.1]. It is part of the [[cop.py]] file that can be seen in it's entirety in the annexes or [here in the repo](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/cop.py).

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

%% #WIP update to latest code %%

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

As I cant get it to complete the cycles I'm going to sacrifice the compression & sub-cooling stages as this is likely the least accurate. This allows me to have better plots for condensation, expansion and evaporation.

I also added:
- cubic interpolation with numpy to fix the top of the isolines.
- colour cycles by flow rate
- colour bar legend
- linear pressure axis option
- large labels for readability 

![[Refrigeration_Cycle_Plots_(wo compression, zoom out).svg]]