import CoolProp.CoolProp as CP
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
import matplotlib.pyplot as plt
from scipy import interpolate

from cop import isentropic_efficiency

def plot_PH(lab_readings):
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
    cycle.set_axis_limits([0, 500, 0, 3500])
    colours = plt.cm.viridis((flow_rate-flow_rate.min())/(flow_rate.max()-flow_rate.min()))

    for i, entry in enumerate(zip(T_evap,P_evap,T_cond,P_cond, eta_com, colours)):
        cycle.simple_solve(*entry[:-1])

        sc = cycle.get_state_changes()
        colour = colours[i]
        ph_plt.draw_process(sc, line_opts={"color":colour})

    ph_plt.title("Refrigeration Cycles on P-h Diagram")
    ph_plt.grid()
    # sm = plt.cm.ScalarMappable(cmap="viridis")
    # sm = plt.cm.viridis(flow_rate)
    # sm.set_array([])
    # cbar = plt.colorbar(sm,ax=ph_plt.axis)
    cbar = plt.colorbar(flow_rate, ax=ph_plt.axis)
    cbar.set_label("Flow Rate (g/s)")
    ph_plt.show()

import coursework
plot_PH(coursework.all_readings)
