"""
Calculation methods for heat transfer rate
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

def plot_dQvT(lab_readings):
    import matplotlib.pyplot as plt

    def dQvT_graph(title,T, dQ):

        plt.scatter( T, dQ)
        plt.title(f"{title} Heat transfer rate against Temperature")
        plt.xlabel("Temperature (K)")
        plt.ylabel("Heat Transfer rate (W)")
    
    from heat_flux import method_3 as find_dQ
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

def plot_dQvdT(lab_readings):
    import matplotlib.pyplot as plt

    def dQvT_graph(title,T, dQ):

        plt.scatter( T, dQ)
        plt.title(f"{title} Heat transfer rate against Temperature")
        plt.xlabel("Temperature (K)")
        plt.ylabel("Heat Transfer rate (W)")
    
    from heat_flux import method_3 as find_dQ
    dQ_c, dQ_e = find_dQ(lab_readings)

    fig, axis = plt.subplots(1,2)

    plt.sca(axis[0])
    dQvT_graph(
        "Evaporator", 
        lab_readings["T5"]-lab_readings["T1"], 
        dQ_e
    )

    plt.sca(axis[1])
    dQvT_graph(
        "Condenser", 
        lab_readings["T6"]-lab_readings["T4"], 
        dQ_c
    )

    plt.show()
import coursework
plot_dQvT(coursework.lab_readings)
plot_dQvdT(coursework.lab_readings)
