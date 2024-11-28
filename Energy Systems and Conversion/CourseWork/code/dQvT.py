"""
Calculation methods for heat transfer rate
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

import matplotlib.pyplot as plt
from heat_flux import method_3 as find_dQ

def plot_dQvT(lab_readings):
    import matplotlib.pyplot as plt

    def dQvT_graph(title,T, dQ):

        plt.scatter( T, dQ)
        plt.title(f"{title} Heat transfer rate against Temperature")
        plt.xlabel("Temperature (K)")
        plt.ylabel("Heat Transfer rate (W)")
    
    dQ_e, dQ_c = find_dQ(lab_readings)

    fig, axis = plt.subplots(1,2)

    plt.sca(axis[0])
    dQvT_graph(
        "Evaporator", 
        lab_readings["T5"],
        dQ_e
    )

    plt.sca(axis[1])
    dQvT_graph(
        "Condenser", 
        lab_readings["T6"],
        dQ_c
    )

    plt.show()

def plot_x_y(x_title, x, y_title, y, subchart_title = "Condenser"):

    plt.scatter(x, y, label="Data Points")
    plt.title(subchart_title +" "+ y_title+" against "+x_title)                      
    plt.xlabel(x_title)                                   
    plt.ylabel(y_title)

    plt.show()

def plot_x_y_best_fit_cuve(x_title, x, y_title, y, subchart_title = "Condenser"):

    plt.scatter(x, y, label="Data Points")
    plt.title(subchart_title +" "+ y_title+" against "+x_title)                      
    plt.xlabel(x_title)                                   
    plt.ylabel(y_title)

    import numpy as np
    # coeffs = np.polyfit(x, y, 2)
    # poly = np.poly1d(coeffs)
    # x_fit = np.linspace(min(x), max(x), 500)
    # y_fit = poly(x_fit)
    # plt.plot(x_fit, y_fit, color="red", label=f"Fit: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
        
    from scipy.optimize import curve_fit
    def exponential(x, a, b, c):
        return c + a * np.exp(b * x)

    # Fit the data to the exponential function
    params, _ = curve_fit(exponential, x, y, p0=(250, -0.4, 700))  # Initial guess for a and b
    a, b, c= params

    # Generate values for the fit curve
    x_fit = np.linspace(min(x), max(x), 500)
    y_fit = exponential(x_fit, a, b, c)

    # Scatter plot of the data
    plt.plot(x_fit, y_fit, color="red", label=f"Fit: y = {c:.2f} + {a:.2f} * exp({b:.2f} * x)")
    plt.legend()

    plt.show()

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

def plot_dQvdT(lab_readings):
    mfr_c = lab_readings['m/t c'].values*1000
    mfr_e = lab_readings['m/t e'].values*1000

    dQ_e, dQ_c = find_dQ(lab_readings)

    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    plot_x_y_colourbar(
        "Temperature change across coil ($\degree$K)",[dT_e,dT_c], 
        "Coil energy transfer rate (W)",[dQ_e,dQ_c],
        "Flow rate (g/s)",[mfr_e,mfr_c]
    )

def plot_dQ_v_mfr(lab_readings):
    mfr_c = lab_readings['m/t c'].values*1000
    mfr_e = lab_readings['m/t e'].values*1000

    dQ_e, dQ_c = find_dQ(lab_readings)

    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    plot_x_y_colourbar(
        "Flow rate (g/s)",[mfr_e,mfr_c],
        "Coil energy transfer rate (W)",[dQ_e,dQ_c],
        "Temperature change across coil ($\degree$K)",[dT_e,dT_c], 
    )

def plot_Tcoolant_v_Tchamber(lab_readings):

    Tcoolant = [
        (lab_readings['T1']+lab_readings['T2'])/2,
        (lab_readings['T4']+lab_readings['T3'])/2
    ]
    Tchamber = [
        lab_readings['T5'],
        lab_readings['T6']
    ]
    mfr = [
        lab_readings['m/t e'],
        lab_readings['m/t c']*1000
    ]
    plot_x_y_colourbar(
        "Flow rate (g/s)",mfr,
        "Chamber temperature ($\degree$K)", Tchamber,
        "Average water temperature ($\degree$K)",Tcoolant,
    )


def plot_Tgradient_v_mfr(lab_readings):

    Tgradient = [
        ((lab_readings['T1']+lab_readings['T2'])/2)-lab_readings['T5'],
        ((lab_readings['T4']+lab_readings['T3'])/2)-lab_readings['T6']
    ]
    mfr = [
        lab_readings['m/t e'],
        lab_readings['m/t c']*1000
    ]

    dQ = find_dQ(lab_readings)

    plot_x_y_colourbar(
        "Flow rate (g/s)",mfr,
        "Temperature gradient ($\degree$K)",Tgradient,
        "Coil energy transfer rate (W)",dQ,
    )

def plot_dQ_div_mfr_v_Tgradient(lab_readings):

    Tgradient = [
        ((lab_readings['T1']+lab_readings['T2'])/2)-lab_readings['T5'],
        ((lab_readings['T4']+lab_readings['T3'])/2)-lab_readings['T6']
    ]
    mfr = [
        lab_readings['m/t e'],
        lab_readings['m/t c']*1000
    ]

    dQ = find_dQ(lab_readings)

    dQ_div_mfr = [
        dQ[0]/mfr[0],
        dQ[1]/mfr[1]
    ]
    mfr = [
        lab_readings['m/t c'],
        lab_readings['m/t e']*1000
    ]
    plot_x_y(
        "Temperature gradient ($\degree$K)",Tgradient[1],
        "Coil energy transfer rate / Flow rate (J/g)",dQ_div_mfr[1],
    )

def plot_dQ_v_Tgradient(lab_readings):

    Tgradient = [
        ((lab_readings['T1']+lab_readings['T2'])/2)-lab_readings['T5'],
        ((lab_readings['T4']+lab_readings['T3'])/2)-lab_readings['T6']
    ]
    mfr = [
        lab_readings['m/t e'],
        lab_readings['m/t c']*1000
    ]

    dQ = find_dQ(lab_readings)

    plot_x_y_colourbar(
        "Temperature gradient ($\degree$K)",Tgradient,
        "Coil energy transfer rate (W)",dQ,
        "Flow rate (g/s)",mfr,
    )

def plot_dT_v_mfr(lab_readings):

    dT = [
        lab_readings['T2'].values - lab_readings['T1'].values, # evaporator coil
        lab_readings['T3'].values - lab_readings['T4'].values, # condenser coil
    ]
    mfr = [
        lab_readings['m/t e'],
        lab_readings['m/t c']*1000
    ]
    Tgradient = [
        ((lab_readings['T1']+lab_readings['T2'])/2)-lab_readings['T5'],
        ((lab_readings['T4']+lab_readings['T3'])/2)-lab_readings['T6']
    ]

    # dQ = find_dQ(lab_readings)

    plot_x_y_colourbar(
        "Flow rate (g/s)",mfr,
        "Temperature change across coil ($\degree$K)",dT, 
        "Temperature gradient ($\degree$K)",Tgradient,
        # "Coil energy transfer rate (W)",dQ,
    )

def plot_dT_v_mfr_lbf(lab_readings):

    dT = lab_readings['T3'].values - lab_readings['T4'].values # condenser coil
    mfr = lab_readings['m/t c']*1000
    Tgradient = ((lab_readings['T4']+lab_readings['T3'])/2)-lab_readings['T6']

    # dQ = find_dQ(lab_readings)

    plot_x_y_best_fit_cuve(
        "Flow rate (g/s)",mfr,
        "Temperature change across coil ($\degree$K)",dT, 
        # "Temperature gradient ($\degree$K)",Tgradient,
        # "Coil energy transfer rate (W)",dQ,
    )

def plot_PdivT_v_mfr(lab_readings):
    PdivT = [
        lab_readings["p e"]/lab_readings["T5"],
        lab_readings["p c"]/lab_readings["T6"] 
    ]   
    mfr = [
        lab_readings['m/t e'],
        lab_readings['m/t c']*1000
    ]

    plot_x_y(
        "Flow rate (g/s)",mfr,
        "Pressure/Temperature (kPa/$\degree$K)",PdivT,
    )

def plot_PdivT_v_mfr_lbf(lab_readings):
    PdivT = (lab_readings["p c"]/1000)/lab_readings["T6"] 
    mfr = lab_readings['m/t c']*1000

    plot_x_y_best_fit_cuve(
        "Flow rate (g/s)",mfr,
        "Pressure/Temperature (kPa/$\degree$K)",PdivT,
    )

import coursework
lab_readings = coursework.lab_readings
# lab_readings = coursework.low_e_flow
# lab_readings = coursework.high_e_flow
# plot_dQvT(lab_readings)
# plot_dQvdT(lab_readings)
# plot_dQ_v_mfr(lab_readings)
# plot_dQ_v_Tgradient(lab_readings)
# plot_dT_v_mfr(lab_readings)
# plot_dQ_div_mfr_v_Tgradient(lab_readings)
# plot_dT_v_mfr_lbf(lab_readings)
plot_Tcoolant_v_Tchamber(lab_readings)
# plot_Tgradient_v_mfr(lab_readings)
# plot_PdivT_v_mfr_lbf(lab_readings)
