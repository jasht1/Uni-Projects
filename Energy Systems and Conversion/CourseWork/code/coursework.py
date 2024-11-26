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
        os.path.dirname(__file__), '..', 
        'Lab Readings - Energy Systems Coursework.csv')

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

lab_readings = get_lab_readings()
low_e_flow = lab_readings[lab_readings['m/t e'] == 0.01].sort_values(by='m/t c')
high_e_flow = lab_readings[lab_readings['m/t e'] == 0.02].sort_values(by='m/t c')
