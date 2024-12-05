[All of the code can be viewed here in the working repository](https://github.com/jasht1/Uni-Projects/tree/master/Energy%20Systems%20and%20Conversion/CourseWork/code)

## Overview

### Core functions

#### Plots

##### x y plots

###### Exponential line of best fit

```python
def plot_x_y_best_fit_cuve(x_title, x, y_title, y, subchart_title = "Condenser"):
    import numpy as np   
    from scipy.optimize import curve_fit
    def exponential(x, a, b, c):
        return c + a * np.exp(b * x)

    # Fit the data to the exponential function
    params, _ = curve_fit(exponential, x, y, p0=(250, -0.4, 700))  # Initial guess for a and b
    a, b, c= params

    plt.scatter(x, y, label="Data Points")
    plt.title(subchart_title +" "+ y_title+" against "+x_title)                      
    plt.xlabel(x_title)                                   
    plt.ylabel(y_title)

    # Generate values for the fit curve
    x_fit = np.linspace(min(x), max(x), 500)
    y_fit = exponential(x_fit, a, b, c)

    # Scatter plot of the data
    plt.plot(x_fit, y_fit, color="red", label=f"Fit: y = {c:.2f} + {a:.2f} * exp({b:.2f} * x)")
    plt.legend()

    plt.show()
```

###### Evaporator vs Condenser Comparison

```python
def plot_x_y_colourbar(x_title, x, y_title, y, c_title, c, subchart_titles = ["Evaporator", "Condenser"]):

    fig, axis = plt.subplots(1,2)
    fig.suptitle(y_title+" against "+x_title)                      

    for i, x, y, colour, subchart_title in zip(range(len(subchart_titles)), x,y,c,subchart_titles):
        plt.sca(axis[i])
        scatter = plt.scatter(x, y,c=colour)
        cbar = plt.colorbar(scatter)
        cbar.set_label(c_title)
        plt.title(subchart_title)                      
        plt.xlabel(x_title)                                   
        plt.ylabel(y_title)

    plt.show()
```

##### Carnot cycle plots

Thermodynamic cycle plots provide a visual intuition for a given process. The Carnot cycle is an idealised approximation of a refrigeration cycle like the one that occurs in the R634 unit. Below are idealised approximations of what all the cycles would have been for the flow rates tested.

![[Refrigeration_Cycle_Plots_(wo compression, linear).svg]]

To achieve this I wrote the `plot_PH` function that can be found in [plot_cycles.py](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/plot_cycles.py). It's based loosely on [this](https://stackoverflow.com/questions/70864726/put-labels-in-coolprop-chart) example I found on stack overflow[^2.3.2] utilising my `isentropic_efficiency` function mentioned above along with with the [SimpleCyclesCompression module](http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html) from coolProp[^2.3.1]. It is part of the [[cop.py]] file that can be seen in it's entirety in the annexes or [here in the repo](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/cop.py).

[^2.3.2]: “Put labels in Coolprop Chart.” [Online]. Available: https://stackoverflow.com/questions/70864726/put-labels-in-coolprop-chart. [Accessed: 26-Nov-2024].

[^2.3.1]: “CoolProp.Plots.SimpleCyclesCompression module — CoolProp 6.6.0 documentation.” [Online]. Available: http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html. [Accessed: 26-Nov-2024].

```python title=plot_cycles.py
import CoolProp.CoolProp as CP
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
import matplotlib.pyplot as plt
from scipy import interpolate

from cop import isentropic_efficiency

def plot_PH(lab_readings):
    flow_rate = lab_readings["m/t c"].values
    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_cond = lab_readings["T6"].values
    P_cond = lab_readings["p c"].values
    T_comp = lab_readings["T7"].values

    eta_com = isentropic_efficiency(T_evap,P_evap,T_comp,P_cond)

    ph_plt = PropertyPlot('SES36', 'PH', unit_system='KSI')

    ph_plt.xlabel("h [kJ/kg]")
    ph_plt.ylabel("P [kPa]")

    ph_plt.calc_isolines(CP.iQ)

    cycle = SimpleCompressionCycle("SES36", "PH", unit_system="KSI")
    cycle.set_axis_limits([0, 500, 0, 3500])
    colours = plt.cm.viridis((flow_rate-flow_rate.min())/(flow_rate.max()-flow_rate.min()))

    for i, entry in enumerate(zip(T_evap,P_evap,T_cond,P_cond, eta_com, colours)):
        cycle.simple_solve(*entry[:-1])

        sc = cycle.get_state_changes()
        colour = colours[i]
        ph_plt.draw_process(sc, line_opts={"color":colour})

    ph_plt.title("Refrigeration Cycles on P-h Diagram")
    ph_plt.grid()
    sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=2, vmax=12), cmap="viridis")
    cbar = plt.colorbar(sm,ax=ph_plt.axis)
    cbar.set_label("Flow Rate (g/s)")
    ph_plt.show()
```

> [!INFO] The full file `plot_cycles.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/plot_cycles.py)

##### Correlation maps

Correlation maps act as a key for what variables in a dataset display approximate pairwise linear corrections. each cell in the grid is coloured and labelled based on the pearson pairwise correlational factor of the variables that intersect at it.

It is a useful resource when exploring relationships between state variables in a system and deciding which variables are worth instigating together. 

Below is a Correlation map of all the key variables in this investigation:

![[corraltion_map-all_data.svg]]

This was produced using the following function:
```python title=p_map.py
def p_map(lab_readings):
    import matplotlib.pyplot as plt
    import seaborn 

    corralations = lab_readings.corr()
    pmap=seaborn.heatmap(corralations, annot=True,cmap="RdBu", cbar=False)
    pmap.xaxis.tick_top()

    plt.show()
```

> [!INFO] The full file `p_map.py` can be found in the annexes and [here in the working repository](https://github.com/jasht1/Uni-Projects/blob/master/Energy%20Systems%20and%20Conversion/CourseWork/code/p_map.py)


