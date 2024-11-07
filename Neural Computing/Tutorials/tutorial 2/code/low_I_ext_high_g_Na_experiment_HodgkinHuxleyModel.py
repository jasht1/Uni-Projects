import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import hodgkin_huxley_model as hh  # Assuming your model is imported from hh

I_stim = [1,5,10,15,20]

for n, i in enumerate(I_stim):

    # plt.gcf().text(0.05, 0.82 - (n * (0.80 / len(I_stim))), f'I_stim = {i} µA/cm²', fontsize=12, va='center', ha='right', rotation=90)
    plt.gcf().text(0.03, 0.9 - (n * (0.98 / len(I_stim))), f'I_stim = {i} µA', fontsize=12, va='center', ha='right', rotation=90)

    if n == 0: showtitle = True
    else: showtitle = False

    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50,I_stim=i,g_Na=250)
    plt.subplot(5,2,2*n+1)
    hh.plot_v_by_t(time, V_values, title=showtitle)

    plt.subplot(5,2,2*n+2)
    hh.plot_gating_by_t(time, m_values, h_values, n_values, title=showtitle, legend=showtitle)

plt.show()

### Animation

## Initialisation

# Define the graphs
fig, (g1, g2) = plt.subplots(2, 1, figsize=(8, 6))

line1, = g1.plot([], [], lw=2)  # Membrane potential line
line2, = g2.plot([], [], 'r', label='m (Na+ activation)', lw=1.5)
line3, = g2.plot([], [], 'g', label='h (Na+ inactivation)', lw=1.5)
line4, = g2.plot([], [], 'b', label='n (K+ activation)', lw=1.5)

g1.set_title('Membrane Potential')
g1.set_xlim(0, 50)  # Time range
g1.set_ylim(-80, 50)  # Membrane potential range
g1.set_xlabel('Time (ms)')
g1.set_ylabel('Membrane Potential (mV)')
g1.grid(True)

g2.set_title('Gating Variables Over Time')
g2.set_xlim(0, 50)  # Time range
g2.set_ylim(0, 1)  # Gating variable range
g2.set_xlabel('Time (ms)')
g2.set_ylabel('Gating Variable')
g2.grid(True)
g2.legend(loc='best')

# Stores values for plotting
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    return line1, line2, line3, line4

## Updating the frames

def update(i):
    # Vary stimulation current
    I_stim = 1 + 0.5 * i  # Vary I_stim over time
    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50,I_stim=I_stim,g_Na=250)
    
    # Update the current I_stim value
    g1.set_title(f'Membrane Potential (I_stim = {I_stim:.1f} µA)')

    # Update the data for the plots
    line1.set_data(time, V_values)
    line2.set_data(time, m_values)
    line3.set_data(time, h_values)
    line4.set_data(time, n_values)
    
    return line1, line2, line3, line4

## Plotting & saving

ani = FuncAnimation(fig, update, frames=np.arange(1, 40), init_func=init, blit=True, interval=100)
ani.save('hodgkin_huxley_simulation.gif', writer='imagemagick', fps=10)

plt.show()
