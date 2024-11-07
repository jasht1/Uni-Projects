import numpy as np

def signal_propagation(
    ## Default Parameters

    # Model Paramiters
    t = 1,                  # Total simulation time
    Nx = 150,               # Number of spatial points
    dt = 0.00005,           # Time step size for stability

    # Signal
    V = np.zeros(150),

    # Neuron Propertys
    s = 3,                  # Length of the dendrite

    # Cable equation parameters
    k_l = 0.2,           # Increase length constant for more propagation
    tau = 0.8               # Time constant for slower temporal decay
    ):

    ## Initialisation
    dx = s // (Nx - 1)      # Spatial step size
    Nt = (t // dt),     # Ensure Nt is an integer
    V[Nx//2] = 2    # First spike in the middle with amplitude 1
    #V[Nx//3] = 4   # Second spike at one-third position with amplitude 0.9
    #V[Nx//5] = 8   # Second spike at one-fifth position with amplitude 0.9

    # Initial condition: two voltage spikes with different amplitudes
    V = np.zeros(Nx);       # Voltage array

    # Matrix to store the voltage over time
    V_history = np.zeros(Nx, Nt)  # Matrix to store voltage propagation

    # Simulation loop
    for t in np.arange(1,Nt):
        V_new = V  # To store the new values of V
        for x in np.arange(2,Nx-1):
            # Update the voltage using the cable equation
            V_new(x) = V(x) + dt * (k_l^2 / dx^2) * (V(x+1) - 2*V(x) + V(x-1)) - dt/tau * V(x)
    
    # Update V and store the result for this time step
    V = V_new
    V_history(:, t) = V
