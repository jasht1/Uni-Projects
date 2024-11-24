"""
Calculation methods for heat transfer rate
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

import pandas as pd

## Method 1 - $q = \dot{m} c_{p} \detla T$

def method_1(lab_readings): # Method 1 - $q = \dot{m} c_{p} \detla T$

    c_p = 4181.3  # constant pressure specific heat capacity of water @ 101325 Pa, 298.15 K

    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    # energy transfer (W) product of mass flow rate, temperature change & specific heat capacity
    dQ_e = c_p*dT_e*lab_readings['m/t e'].values
    dQ_c = c_p*dT_c*lab_readings['m/t c'].values

    return (dQ_c,dQ_e)


## Method 2

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

    return (dQ_c,dQ_e)


## Method 3

def method_3(lab_readings): # Method 3 CoolProp for heat transfer rate 

    from CoolProp.CoolProp import PropsSI 

    # specific internal energy change of the fluid across the coolant coils (J)
    de_e = PropsSI('H', 'T', lab_readings['T2'].values, 'P', 101325, 'H2O') - PropsSI('H', 'T', lab_readings['T1'].values, 'P', 101325, 'H2O') # evaporator coil 
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

def compare_methods(lab_readings):
    import matplotlib.pyplot as plt

    data = pd.DataFrame({
        "condenser flow rate (g/s)" : lab_readings['m/t c']*1000
    })
    data['dQ_c-m1'], data['dQ_e-m1'] = method_1(lab_readings)
    data['dQ_c-m2'], data['dQ_e-m2'] = method_2(lab_readings)
    data['dQ_c-m3'], data['dQ_e-m3'] = method_3(lab_readings)

    data.plot(x="condenser flow rate (g/s)", y=["dQ_c-m1","dQ_c-m2","dQ_c-m3"])
    plt.ylabel("condenser coil energy transfer rate (W)")
    plt.title("Condenser coil flow rate against energy transfer rate")
    data.plot(x="condenser flow rate (g/s)", y=["dQ_e-m1","dQ_e-m2","dQ_e-m3"])
    plt.ylabel("evaporator coil energy transfer rate (W)")
    plt.title("Condenser coil flow rate against energy transfer rate in evaporator coil")

    plt.show()
