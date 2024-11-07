import numpy as np
from matplotlib import pyplot as plt 

def hodgkin_huxley (
    ## Default Paramiters

    # Time parameters
    dt = 0.01,  # Time step (ms)
    T = 100,    # Total time (ms)

    # Membrane properties
    C_m = 1.0,    # Membrane capacitance, uF/cm^2
    g_Na = 150.0, # Maximum conductance of sodium (mS/cm^2)
    g_K = 36.0,   # Maximum conductance of potassium (mS/cm^2)
    g_L = 0.3,    # Leak conductance (mS/cm^2)

    # Voltage set points
    E_Na = 50,    # Sodium reversal potential (mV)
    E_K = -77,    # Potassium reversal potential (mV)
    E_L = -54.4,  # Leak reversal potential (mV)
    V_rest = -65, # Resting membrane potential (mV)

    # External current
    I_stim = 10  # Excitation profile

    ):

    ## Initialisation

    # Time array
    time = np.arange(0,T,dt)  # Time vector

    # initiating values
    V = np.full(len(time),float(V_rest)) # membrane potential (mv)
    m = 0.05   # sodium activation gating variable
    h = 0.6    # sodium inactivation gating variable
    n = 0.32   # potassium activation gating variable

    # initiating output arrays
    m_values = np.zeros(len(time))
    h_values = np.zeros(len(time))
    n_values = np.zeros(len(time))
    V_values = np.zeros(len(time))

    ## Functions

    # External current (stimulation)
    I_ext = np.zeros(len(time))
    I_ext[500:600] = I_stim  # Inject current between 5 and 6 ms

    # rate functions
    def alpha_m(V): 
        if V == -40:
            return 1
        else:
            return (0.1 * (V + 40)) / (1 - np.exp(-(V + 40) / 10))

    def alpha_n(V): 
        if V == -55:
            return 0.1
        else:
            return (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))

    def alpha_h(V): return 0.07 * np.exp(-(V + 65) / 20)

    def beta_m(V): return 4.0 * np.exp(-(V + 65) / 18)

    def beta_h(V): return 1.0 / (1 + np.exp(-(V + 35) / 10))

    def beta_n(V): return 0.125 * np.exp(-(V + 65) / 80)

    ## Main Loop

    for t in range(2,len(time),1):
        # Update Gating values with eulers method

        m += dt * (alpha_m(V[t-1]) * (1 - m) - beta_m(V[t-1]) * m)
        h += dt * (alpha_h(V[t-1]) * (1 - h) - beta_h(V[t-1]) * h)
        n += dt * (alpha_n(V[t-1]) * (1 - n) - beta_n(V[t-1]) * n)
        
        # calculate chanel conductances
        g_Na_t = g_Na * (m**3) * h
        g_K_t = g_K * (n**4)

        # ion flow current
        I_Na = g_Na_t * (V[t-1] - E_Na)
        I_K = g_K_t * (V[t-1] - E_K)
        I_L = g_L * (V[t-1] - E_L)

        # Update membrane potential using Euler's method
        V[t] = V[t-1] + dt * (I_ext[t] - (I_Na + I_K + I_L)) / C_m
        
        # Store values for plotting
        m_values[t] = m
        h_values[t] = h
        n_values[t] = n
        V_values[t] = V[t]

    return time,m_values,h_values,n_values,V_values

## Plotting

# Plot Membrane potential over time
def plot_v_by_t(time, V_values, title = True):
    plt.plot(time, V_values, linewidth=2)
    if title: plt.title('Membrane Potential')
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane Potential (mV)')
    plt.grid(True)

# Plot gating variables over time
def plot_gating_by_t(time, m_values, h_values, n_values, title = True, legend=True):
    plt.plot(time, m_values, 'r', label='m (Na+ activation)', linewidth=1.5)
    plt.plot(time, h_values, 'g', label='h (Na+ inactivation)', linewidth=1.5)
    plt.plot(time, n_values, 'b', label='n (K+ activation)', linewidth=1.5)
    if legend: plt.legend(loc='best') 
    if title: plt.title('Gating Variables Over Time')
    plt.xlabel('Time (ms)')
    plt.ylabel('Gating Variable')
    plt.grid(True)

# Plot Mebrane potential and gating variables
def standard_plot(ax1, ax2, time, m_values, h_values, n_values, V_values):
    plt.title("Hodgkin-Huxley Model:")
    plt.subplot(2,1,1)
    plot_v_by_t(time, V_values)
    plt.subplot(2,1,2)
    plot_gating_by_t(time, m_values, h_values, n_values)

# def plot_defaults():
#     time, m_values, h_values, n_values, V_values = hodgkin_huxley()
#     standard_plot(time, m_values, h_values, n_values, V_values)
#     plt.show()
#
# plot_defaults()
