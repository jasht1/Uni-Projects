"""
Plots pressure vs temperature graphs for evaporator and condenser using colour to indicate mass flow rate
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

import matplotlib.pyplot as plt


def PvT_graph(title, pressure, temperature, flow_rate):
    scatter = plt.scatter(
        temperature, # x-axis: Temperature
        pressure/1000 - 101.325, # y-axis: Pressure
        c=flow_rate*1000, # Colors based on flow rate
    )

    cbar = plt.colorbar(scatter)
    cbar.set_label("Flow Rate (g/s)")

    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (kPa)")
    plt.title(title)

def plot_PvT(lab_readings):

    fig, axis = plt.subplots(1,2)
    plt.suptitle("Pressure vs. Temperature (Colored by Flow Rate)")

    plt.sca(axis[0])
    PvT_graph(
        "Evaporator",
        lab_readings["p e"], 
        lab_readings["T5"], 
        lab_readings["m/t e"]
    )

    plt.sca(axis[1])
    PvT_graph(
        "Condenser",
        lab_readings["p c"], 
        lab_readings["T6"], 
        lab_readings["m/t c"] 
    )

    plt.show()

def plot_PvdT(lab_readings):

    fig, axis = plt.subplots(1,2)
    plt.suptitle("Pressure vs. Temperature (Colored by Flow Rate)")

    plt.sca(axis[0])
    PvT_graph(
        "Evaporator",
        lab_readings["p e"], 
        lab_readings["T5"]-lab_readings["T1"], 
        lab_readings["m/t e"]
    )

    plt.sca(axis[1])
    PvT_graph(
        "Condenser",
        lab_readings["p c"], 
        lab_readings["T6"]-lab_readings["T4"], 
        lab_readings["m/t c"] 
    )

    plt.show()

import coursework
plot_PvT(coursework.lab_readings)
# plot_PvdT(coursework.lab_readings)
