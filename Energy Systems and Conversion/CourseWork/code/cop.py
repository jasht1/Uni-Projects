"""
Calculation method for Coefficent of performance
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton

To test the methods: uncomment the lines at the bottom of the script
"""

def method_1(lab_readings):
    from CoolProp.CoolProp import PropsSI 
    material = 'SES36'

    # Condenser enthalpy change
    P_initial = lab_readings['p c'].values
    T_initial = lab_readings['T6'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = P_initial
    T_final = T_initial

    H_final = PropsSI('H', 'T', T_final, 'P|liquid', P_final, material)

    dH_condensation = H_initial - H_final

    # Compressor ethalpy change
    P_initial = lab_readings['p e'].values
    T_initial = lab_readings['T5'].values

    H_initial = PropsSI('H', 'T', T_initial, 'P|gas', P_initial, material)

    P_final = lab_readings['p c'].values
    T_final = lab_readings['T7'].values

    H_final = PropsSI('H', 'T', T_final, 'P|gas', P_final, material)

    dH_compression = H_initial - H_final

    cop = abs(dH_condensation/dH_compression)

    return cop

def isentropic_efficiency(*args):
    import CoolProp.CoolProp as CP

    if len(args) == 1:  # if `args[0]` is `lab_readings`
        lab_readings = args[0]
        T_in = lab_readings["T5"].values
        P_in = lab_readings["p e"].values
        P_out = lab_readings["p c"].values
        T_out = lab_readings["T7"].values
    elif len(args) == 4:  # if values for T_in, P_in, T_out, P_out
        T_in, P_in, T_out, P_out = args

    h_in = CP.PropsSI('H', 'T', T_in, 'P|gas', P_in, "SES36")
    S_in =  CP.PropsSI('S', 'T', T_in, 'P|gas', P_in, "SES36")

    h_out_max = CP.PropsSI('H', 'S', S_in, 'P|gas', P_out, "SES36")
    h_out_actual = CP.PropsSI('H', 'T', T_out, 'P|gas', P_out, "SES36")

    return (h_out_max-h_in)/(h_out_actual-h_in)

def plot_copVmfr(lab_readings):
    import matplotlib.pyplot as plt

    mfr_c = lab_readings['m/t c'].values*1000
    cop = method_1(lab_readings)

    plt.plot(mfr_c,cop)
    plt.title("Flow Rate against COP")
    plt.xlabel("Condenser flow rate (g/s)")
    plt.ylabel("Cycle Coefficent of Performance")

    plt.show()

## To test the above funcitons uncomment the line below and run the script

