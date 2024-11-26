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

def isentropic_efficiency(T_in,P_in,T_out,P_out):
    import CoolProp.CoolProp as CP

    h_in = CP.PropsSI('H', 'T', T_in, 'P|gas', P_in, "SES36")
    S_in =  CP.PropsSI('S', 'T', T_in, 'P|gas', P_in, "SES36")

    h_out_max = CP.PropsSI('H', 'S', S_in, 'P|gas', P_out, "SES36")
    h_out_actual = CP.PropsSI('H', 'T', T_out, 'P|gas', P_out, "SES36")

    return (h_out_max-h_in)/(h_out_actual-h_in)

def plot_PH(lab_readings):
    import CoolProp.CoolProp as CP
    from CoolProp.Plots import PropertyPlot
    from CoolProp.Plots import SimpleCompressionCycle
    import matplotlib.pyplot as plt

    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_comp = lab_readings["T7"].values
    P_comp = lab_readings["p c"].values

    eta_com = isentropic_efficiency(T_evap,P_evap,T_comp,P_comp)

    ph_plt = PropertyPlot('SES36', 'PH', unit_system='KSI')

    ph_plt.xlabel("h [kJ/kg]")
    ph_plt.ylabel("P [kPa]")

    ph_plt.calc_isolines(CP.iQ, num=11)

    cycle = SimpleCompressionCycle("SES36", "PH", unit_system="KSI")

    for entry in zip(T_evap,P_evap,T_comp,P_comp, eta_com):
        cycle.simple_solve(*entry)

        sc = cycle.get_state_changes()
        ph_plt.draw_process(sc, line_opts={"label": f"flow rate", "lw": 1.5})

    # ph_plt.legend(loc="upper left")
    ph_plt.title("Refrigeration Cycles on P-h Diagram")
    ph_plt.grid()
    ph_plt.show()


def test(function = "all", dataset = "low_e_flow"):
    import coursework as cw
    lab_readings = getattr(cw, dataset)

    # import coursework.lab_readings as lab_readings

    if function == "all" or "method_1":
        cop = method_1(lab_readings)
        print (cop)
        print ("sucess")

    if function == "all" or "plot_copVmfr":
        plot_copVmfr(lab_readings)
        print ("sucess")

    if function == "all" or "eta_com":
        T_evap = lab_readings["T5"].values
        P_evap = lab_readings["p e"].values
        T_comp = lab_readings["T7"].values
        P_comp = lab_readings["p c"].values

        eta_com = isentropic_efficiency(T_evap,P_evap,T_comp,P_comp)
        print (eta_com)
        print ("sucess")

    if function == "all" or "plot_PH":
        plot_PH(lab_readings)
        print ("sucess")

## To test the above funcitons uncomment the line below and run the script
test("plot_PH")
