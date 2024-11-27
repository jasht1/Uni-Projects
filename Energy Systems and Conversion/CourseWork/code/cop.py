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
    from scipy import interpolate

    flow_rate = lab_readings["m/t c"].values
    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_cond = lab_readings["T6"].values
    P_cond = lab_readings["p c"].values
    T_comp = lab_readings["T7"].values

    eta_com = isentropic_efficiency(T_evap,P_evap,T_comp,P_cond)

    ph_plt = PropertyPlot('SES36', 'PH', unit_system='KSI')

    ph_plt.xlabel("h [kJ/kg]")
    ph_plt.ylabel("P [kPa]")

    ph_plt.calc_isolines(CP.iQ)

    cycle = SimpleCompressionCycle("SES36", "PH", unit_system="KSI")

    colours = plt.cm.viridis((flow_rate-flow_rate.min())/(flow_rate.max()-flow_rate.min()))

    for i, entry in enumerate(zip(T_evap,P_evap,T_cond,P_cond, eta_com, colours)):
        cycle.simple_solve(*entry[:-1])

        sc = cycle.get_state_changes()
        colour = colours[i]
        ph_plt.draw_process(sc, line_opts={"color":colour})

    ph_plt.title("Refrigeration Cycles on P-h Diagram")
    ph_plt.grid()
    # sm = plt.cm.ScalarMappable(cmap="viridis")
    # sm.set_array([])
    # cbar = plt.colorbar(sm,ax=ph_plt.axis)
    # cbar.set_label("Flow Rate")
    ph_plt.show()

def check_state(lab_readings):
    import CoolProp.CoolProp as CP

    T_evap = lab_readings["T5"].values
    P_evap = lab_readings["p e"].values
    T_comp = lab_readings["T7"].values
    P_comp = lab_readings["p c"].values

    print(CP.PropsSI('Phase', 'T', T_evap, 'P', P_evap, "SES36"))
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    # print(CP.PhaseSI('T', T_evap[0], 'P', P_evap[0], "SES36"))
    # print(CP.PhaseSI('T', T_comp[1], 'P', P_comp[1], "SES36"))

    # Check difference for temperature adjustment
    print(T_comp)
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    T_comp_sat = (CP.PropsSI('T', 'Q', 1.0, 'P', P_comp, "SES36"))
    print(T_comp_sat)
    print(CP.PropsSI('Phase', 'T', T_comp_sat, 'P', P_comp, "SES36"))

    print (T_comp-T_comp_sat)

    # Check difference for temperature adjustment
    print(P_comp)
    print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp, "SES36"))
    P_comp_sat = (CP.PropsSI('P', 'Q', 1.0, 'T', T_comp, "SES36"))
    print(P_comp_sat)
    # print(CP.PropsSI('Phase', 'T', T_comp, 'P', P_comp_sat, "SES36"))

    print (P_comp-P_comp_sat)

def test(function = "all", dataset = "lab_readings"):
    import coursework as cw
    lab_readings = getattr(cw, dataset)


    available_functions = {
        "method_1": lambda: print(method_1(lab_readings), "success"),
        "plot_copVmfr": lambda: (plot_copVmfr(lab_readings), print("success")),
        "check_state": lambda: check_state(lab_readings),
        "eta_com": lambda: (
            print(
                isentropic_efficiency(
                    lab_readings["T5"].values,
                    lab_readings["p e"].values,
                    lab_readings["T7"].values,
                    lab_readings["p c"].values,
                )
            ),
            print("success"),
        ),
        "plot_PH": lambda: (plot_PH(lab_readings), print("success")),
    }

    if function == "all": # Call all functions if function=="all"
        for func in available_functions.values():
            func()
    else: # call a specific function
        try:
            available_functions[function]()
        except KeyError:
            print(f"Function '{function}' is not recognized.")

## To test the above funcitons uncomment the line below and run the script
# test("plot_PH","low_e_flow")
test("plot_PH")
# test("eta_com")
# test("check_state")
