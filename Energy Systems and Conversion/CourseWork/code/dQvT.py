"""
Calculation methods for heat transfer rate
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

from heat_flux import method_3 as find_dQ

def plot_dQvT(lab_readings):
    import matplotlib.pyplot as plt

    def dQvT_graph(title,T, dQ):

        plt.scatter( T, dQ)
        plt.title(f"{title} Heat transfer rate against Temperature")
        plt.xlabel("Temperature (K)")
        plt.ylabel("Heat Transfer rate (W)")
    
    dQ_c, dQ_e = find_dQ(lab_readings)

    fig, axis = plt.subplots(1,2)

    plt.sca(axis[0])
    dQvT_graph(
        "Evaporator", 
        lab_readings["T5"],
        dQ_e
    )

    plt.sca(axis[1])
    dQvT_graph(
        "Condenser", 
        lab_readings["T6"],
        dQ_c
    )

    plt.show()

def plot_x_y_colourbar(x_title, x, y_title, y, c_title, c, subchart_titles = ["Evaporator", "Condenser"]):
    import matplotlib.pyplot as plt

    fig, axis = plt.subplots(1,2)
    fig.suptitle(y_title+" against "+x_title)                      

    for i, x, y, colour, subchart_title in zip(range(len(subchart_titles)), x,y,c,subchart_titles):
        plt.sca(axis[i])
        scatter = plt.scatter(x, y,c=colour)
        cbar = plt.colorbar(scatter)
        cbar.set_label(c_title)
        plt.title(subchart_title)                      
        plt.xlabel(x_title)                                   
        plt.ylabel(y_title)

    plt.show()

def plot_dQvdT(lab_readings):
    import matplotlib.pyplot as plt

    # def dQvdT_graph(title,T, dQ):
    #
    #     plt.scatter( T, dQ)
    #     plt.title(f"{title} Heat transfer rate against Temperature change")
    #     plt.xlabel("Temperature Change across coil ($\degree$ C)")
    #     plt.ylabel("Heat Transfer rate (W)")
    # 
    # dQ_c, dQ_e = find_dQ(lab_readings)
    #
    # fig, axis = plt.subplots(1,2)
    #
    # plt.sca(axis[0])
    # dQvdT_graph(
    #     "Evaporator", 
    #     lab_readings["T5"]-lab_readings["T1"], 
    #     dQ_e
    # )
    #
    # plt.sca(axis[1])
    # dQvdT_graph(
    #     "Condenser", 
    #     lab_readings["T6"]-lab_readings["T4"], 
    #     dQ_c
    # )
    #
    # plt.show()

    mfr_c = lab_readings['m/t c'].values*1000
    mfr_e = lab_readings['m/t e'].values*1000

    dQ_c_m3, dQ_e_m3 = find_dQ(lab_readings)

    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    plot_x_y_colourbar(
        "Temperature change across coil ($\degree$ C)",[dT_e,dT_c], 
        "Coil energy transfer rate (W)",[dQ_e_m3,dQ_c_m3],
        "Flow rate (g/s)",[mfr_e,mfr_c]
    )

def plot_dQ_v_mfr(lab_readings):
    import matplotlib.pyplot as plt

    
    mfr_c = lab_readings['m/t c'].values*1000
    mfr_e = lab_readings['m/t e'].values*1000

    dQ_c_m3, dQ_e_m3 = find_dQ(lab_readings)

    # temperature change of the fluid in the coolant coils (K)
    dT_e = lab_readings['T2'].values - lab_readings['T1'].values  # evaporator coil
    dT_c = lab_readings['T3'].values - lab_readings['T4'].values  # condenser coil

    fig, axis = plt.subplots(1,2)

    plt.sca(axis[0])
    scatter = plt.scatter(mfr_e, dQ_e_m3,c=dT_e)
    cbar = plt.colorbar(scatter)
    cbar.set_label("Temperature Change across coil ($\degree$ C)")
    plt.title("evaporator coil flow rate against energy transfer rate")                      
    plt.xlabel("evaporator flow rate (g/s)")                                   
    plt.ylabel("evaporator coil energy transfer rate (W)")

    plt.sca(axis[1])
    scatter = plt.scatter(mfr_c, dQ_c_m3,c=dT_c)
    cbar = plt.colorbar(scatter)
    cbar.set_label("Temperature Change across coil ($\degree$ C)")
    plt.title("condenser coil flow rate against energy transfer rate")                      
    plt.xlabel("condenser flow rate (g/s)")                                   
    plt.ylabel("condenser coil energy transfer rate (W)")                                   

    plt.show()

import coursework
lab_readings = coursework.lab_readings.sort_values(by="m/t c")
# plot_dQvT(coursework.lab_readings)
plot_dQvdT(lab_readings)
# plot_dQ_v_mfr(lab_readings)
