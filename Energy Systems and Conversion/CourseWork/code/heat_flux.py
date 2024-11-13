import os
import pandas as pd

def get_lab_readings() -> pd.DataFrame:
    lab_readings_path = os.path.join(
        os.path.dirname(__file__), '..', 
        'Lab Readings - Energy Systems Coursework.csv')

    lab_readings = pd.read_csv(lab_readings_path)

    return lab_readings

lab_readings = get_lab_readings()

lab_readings.loc['condenser water mass flow rate (g/s)',
                'evaporator water mass flow rate (g/s)',
                'evaporation chamber temperature (C) ',
                'evaporating coil inlet temperature (C) ',
                'evaporating coil outlet temperature (C)',
                'condensing chamber temperature (C) ',
                'condensing coil inlet temperature (C) ',
                'condensing coil outlet temperature (C)',
                'compressor discharge temperature (C) ', 
                'condenser pressure (kPa)',
                'evaporator pressure (kPa)']

data = lab_readings[
                'evaporating coil inlet temperature (C) ',
                'evaporating coil outlet temperature (C)',
                'condensing coil inlet temperature (C) ',
                'condensing coil outlet temperature (C)'] + 273.15

data = lab_readings['evaporating coil inlet temperature (C) ', 'evaporating coil outlet temperature (C)', 'condensing coil inlet temperature (C) ', 'condensing coil outlet temperature (C)'] + 273.15
