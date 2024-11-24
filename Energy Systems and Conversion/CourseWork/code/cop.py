"""
Calculation method for Coefficent of performance
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton

To test the methods: uncomment the lines at the bottom of the script
"""

def method_1(lab_readings):

    from CoolProp.CoolProp import PropsSI 

    material = 'SES36'

    P_initial = lab_readings['p e'].values
    T_initial = lab_readings['T5'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = lab_readings['p c'].values
    T_final = lab_readings['T7'].values

    H_final = PropsSI('H', 'T', T_final, 'P|gas', P_final, material)

    dH_compression = H_initial - H_final

    P_initial = lab_readings['p c'].values
    T_initial = lab_readings['T6'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = P_initial
    T_final = T_initial

    H_final = PropsSI('H', 'T', T_final, 'P|liquid', P_final, material)

    dH_condensation = H_initial - H_final

    cop = abs(dH_condensation/dH_compression)

    return cop

def plot_copVmfr(lab_readings):
    import matplotlib.pyplot as plt

    mfr_c = lab_readings['m/t c'].values*1000
    cop = method_1(lab_readings)

    plt.plot(mfr_c,cop)
    plt.title("Flow Rate against COP")
    plt.xlabel("Condenser flow rate (g/s)")
    plt.ylabel("Cycle Coefficent of Performance")

    plt.show()

def plot_PH(lab_readings):
    from CoolProp.Plots import PropertyPlot
    from CoolProp.Plots import SimpleCompressionCycle
    # import matplotlib.pyplot as plt

    ph_plt = PropertyPlot('SES36', 'PH', unit_system='KSI')

    ph_plt.xlabel("h [kJ/kg]")
    ph_plt.ylabel("P [kPa]")

    cycle = SimpleCompressionCycle('SES36', 'PH', unit_system='KSI')


## To test the above funcitons uncomment the 3 lines below and run the script
import coursework as cw
lab_readings = cw.low_e_flow
# import coursework.lab_readings as lab_readings
plot_copVmfr(lab_readings)
# cop = method_1(lab_readings)
# print(cop)


