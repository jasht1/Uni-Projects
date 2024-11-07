
import numpy as np

def lif(
    # Paramiters

    ## model paramiters
    dt = 0.01,  # Time step (ms)
    T = 100,    # Total time (ms)

    ## neuron properties
    tau_m = 20,        # Membrane time constant (ms)
    R = 3,             # Membrane resistance (MΩ)
    V_rest = -65,      # Resting potential (mV)
    V_th = -55,        # Threshold potential (mV) (Try lowering the threshold)
    V_reset = -70,     # Reset potential after spike (mV)


    ## Signal
    I_stim = 4
        ):

    ## Initialisation

    t = np.arange(0,T,dt)  # Time vector
    V = np.full_like(t, V_rest) # Voltage array
    spike_train = np.zeros_like(t) # To track spikes

    for i in range(len(t)):
        dV = (-(V[i-1] - V_rest) + R * I_stim) * (dt / tau_m)
        V[i] = V[i-1] + dV
    
    # Check for spike
    if V[i] >= V_th:
        V[i] = V_reset   # Reset the potential
        spike_train[i] = 1 # Record a spike
    
    return spike_train

