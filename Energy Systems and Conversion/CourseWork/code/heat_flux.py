import coursework
import pyromat as pm
# import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI 

""" utilising pyromat multi phase property model based on:
        T. Petrova, “Revised release on the iapws formulation 1995 for the
        thermodynamic properties of ordinary water substance for general
        and scientific use,” tech. rep., 2014. 
    For more information see http://pyromat.org/pdf/handbook.pdf#chapter.7"""

water = pm.get("mp.H2O")

lab_readings = coursework.get_lab_readings()

## Calculations

### Heat transfer rate

## Method 1 - $q = \dot{m} c_{p} \detla T$

def dQ_method_1(lab_readings): # Method 1 - $q = \dot{m} c_{p} \detla T$

    # temperature change of the fluid in the coolant coils
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    # energy transfer 
    dQ_e = water.cp()*dT_e*lab_readings['m/t e'].values
    dQ_c = water.cp()*dT_c*lab_readings['m/t c'].values

    return (dQ_c,dQ_e)


## Method 2

def dQ_method_2(lab_readings): # Method 2 PYroMat for heat transfer rate

    # specific internal energy change of the fluid across the coolant coils
    de_e = water.e(T=lab_readings['T2'].values) - water.e(T=lab_readings['T1'].values) # evaporator coil 
    de_c = water.e(T=lab_readings['T3'].values) - water.e(T=lab_readings['T4'].values) # condenser coil  

    # energy transfer rate (W), product of energy change and mass flow rate
    dQ_e = de_e*lab_readings['m/t e'].values
    dQ_c = de_c*lab_readings['m/t c'].values

    return (dQ_c,dQ_e)


## Method 3

def dQ_method_3(lab_readings): # Method 3 CoolProp for heat transfer rate 

    # specific internal energy change of the fluid across the coolant coils
    de_e = PropsSI('H', 'T', lab_readings['t2'].values, 'P', 101325, 'H2O') - PropsSI('H', 'T', lab_readings['t1'].values, 'P', 101325, 'H2O') # evaporator coil 
    de_c = PropsSI('H', 'T', lab_readings['T3'].values, 'P', 101325, 'H2O') - PropsSI('H', 'T', lab_readings['T4'].values, 'P', 101325, 'H2O') # condenser coil  

    # energy transfer rate (W), product of energy change and mass flow rate
    dQ_e = de_e*lab_readings['m/t e'].values
    dQ_c = de_c*lab_readings['m/t c'].values

    return (dQ_c,dQ_e)

# # heat flux (W/m^2)
# a_e = 0.068 # evaporator coil surface area in m^2
# a_c = 0.066 # condenser coil surface area in m^2
#
# q_e = dQ_e/a_e
# q_c = dQ_c/a_c

## Figures

### Table
# comparison = [dQ_c2,dQ_c1,dQ_e2,dQ_e1]
# for i in range(3):
#     print(comparison[i])
#
# # comparison = [np.subtract(dQ_c,dQ_c1),np.subtract(dQ_e,dQ_e1)]
# comparison = [dQ_c2-dQ_c1,dQ_e2-dQ_e1]
# print(comparison[0])
# print(comparison[1])
# # for i in range(len(dQ_c)):

### Plot
def plot_dQ(dQ_c,dQ_e):
    plt.plot(dQ_c)
    plt.plot(dQ_c)

    plt.plot(dQ_e*-1)
    plt.plot(dQ_e*-1)
    plt.show()
