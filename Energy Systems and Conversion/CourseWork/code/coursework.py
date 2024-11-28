"""
Imports experimental data
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

import os
import pandas as pd
# import matplotlib.pyplot as plt

def get_lab_readings() -> pd.DataFrame:

    lab_readings_path = os.path.join(
        os.path.dirname(__file__), '../attachments/SpreadSheets/', 
        'Lab Readings - Energy Systems and Conversion Coursework.csv')

    lab_readings = pd.read_csv(lab_readings_path)

    ## Unit conversions

    # convert temperatures from celcius to kelvin
    for i in range(1,8):
        # lab_readings[f"T{i}"] = pm.units.temperature_scale(lab_readings[f"T{i}"],'C','K') # would be more transparant to just show the addition
        lab_readings[f"T{i}"] = lab_readings[f"T{i}"]+273.15

    # convert mass flow rate from g/s to kg/s
    lab_readings['m/t e'] = lab_readings['m/t e']/1000
    lab_readings['m/t c'] = lab_readings['m/t c']/1000

    # convert pressure from kN/m^2 to N/m^s
    lab_readings['p e'] = lab_readings['p e']*1000
    lab_readings['p c'] = lab_readings['p c']*1000
    # convert relative pressure to absolute
    lab_readings['p e'] = lab_readings['p e']+101325
    lab_readings['p c'] = lab_readings['p c']+101325

    return lab_readings

def additional_values(lab_readings):
    # pressure difference between evaporator and condenser
    dp = lab_readings['p c'] - lab_readings['p e']
    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'] - lab_readings['T1'] # evaporator coil
    dT_c = lab_readings['T3'] - lab_readings['T4'] # condenser coil

    Tg_e = ((lab_readings['T1']+lab_readings['T2'])/2)-lab_readings['T5']
    Tg_c = ((lab_readings['T4']+lab_readings['T3'])/2)-lab_readings['T6']
    
    from heat_flux import method_3 as find_dQ
    dQ_e, dQ_c = find_dQ(lab_readings)

    from cop import method_1 as find_cop
    cop = find_cop(lab_readings)

    from cop import isentropic_efficiency as find_eta
    eta = find_eta(lab_readings)

    lab_readings["dp"] = dp
    lab_readings["dT_e"] = dT_e
    lab_readings["dT_c"] = dT_c
    lab_readings["Tg_e"] = Tg_e
    lab_readings["Tg_c"] = Tg_c
    lab_readings["dQ_e"] = dQ_e
    lab_readings["dQ_c"] = dQ_c
    lab_readings["cop"] = cop
    lab_readings["eta"] = eta

    return lab_readings

# DataFrames for use in other scripts
lab_readings = get_lab_readings()
all_readings = get_lab_readings().sort_values(by='m/t c')
low_e_flow = all_readings[all_readings['m/t e'] == 0.01]
high_e_flow = all_readings[all_readings['m/t e'] == 0.02]
all_data = additional_values(lab_readings)
