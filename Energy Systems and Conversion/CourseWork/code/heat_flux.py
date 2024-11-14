import os
import pandas as pd

def get_lab_readings() -> pd.DataFrame:
    lab_readings_path = os.path.join(
        os.path.dirname(__file__), '..', 
        'Lab Readings - Energy Systems Coursework.csv')

    lab_readings = pd.read_csv(lab_readings_path)

    return lab_readings

lab_readings = get_lab_readings()

data = pd.DataFrame({
    'evaporating coil temperature difference (K)': lab_readings['evaporating coil inlet temperature (C)'] - lab_readings['evaporating coil outlet temperature (C)'],
    'condensing coil temperature difference (K)': lab_readings['condensing coil inlet temperature (C)'] - lab_readings['condensing coil outlet temperature (C)']
})

lab_readings[
                'evaporating coil inlet temperature (C) ',
                'evaporating coil outlet temperature (C)',
                'condensing coil inlet temperature (C) ',
                'condensing coil outlet temperature (C)'] + 273.15

data = lab_readings['evaporating coil inlet temperature (C) ', 'evaporating coil outlet temperature (C)', 'condensing coil inlet temperature (C) ', 'condensing coil outlet temperature (C)'] + 273.15
