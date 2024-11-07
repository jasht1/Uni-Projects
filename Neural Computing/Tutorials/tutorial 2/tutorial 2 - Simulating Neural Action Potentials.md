# Simulating Neural Action Potentials Using the Hodgkin – Huxley Model in Matlab

CMP9783: Neural Computing

Workshop Title: Simulating Neural Action Potentials Using the Hodgkin – Huxley Model in Matlab

## Background

![[Hodgkin-Huxley Model]]

## Brief

### Workshop Objectives

By the end of this workshop, participants will:

1. Understand the basic principles of the Hodgkin – Huxley model for action potential generation in neurons.
2. Learn how to implement the Hodgkin – Huxley model in Matlab to simulate the dynamic behaviour of a neuron.
3. Visualize the different phases of an action potential, including depolarization, repolarization and hyperpolarization.
4. Experiment with different parameters (conductances, currents and time steps) to explore how they affect neuronal behavior.

### Task 1: Run the simulation code

1. What happens when the sodium channels open?
2. What happens when the potassium channel opens?
3. Discuss the results and their biological significance.
### Task 2: Modifications and Exploration

1. Modify the current injection change by putting the values 1, 5, 10, 15, 20. What do you observe in the action potential and the channels?
2. What happens if the sodium or potassium conductance is reduced (mimicking channel block)?
3. What is the effect of increasing the sodium conductance? Try to increase it gradually (150,200, 300, etc.). Observe how the action potential changes at each step. Pay attention to:
	- Peak membrane potential
	- Speed of depolarization
	- Duration of the action potential

4. Try decreasing the external current while keeping gNa high to see how little current is needed to trigger an action potential.
5. Test how sensitive the neuron becomes to small stimuli when sodium conductance is high.
6. Increase gNa to very high values (e.g. 500 mS/cm2) and see if you observe abnormal repetitive firing or hyper-excitability.

## Provided Matlab Code

![[HodgkinHuxleyModel.m]]

```MatLab title:"HodgkinHuxleyModel.m"
% Hodgkin-Huxley Neuron Model Simulation
clear all

% Parameters
C_m = 1.0;    % Membrane capacitance, uF/cm^2
g_Na = 150.0; % Maximum conductance of sodium (mS/cm^2)
g_K = 36.0;   % Maximum conductance of potassium (mS/cm^2)
g_L = 0.3;    % Leak conductance (mS/cm^2)
E_Na = 50;    % Sodium reversal potential (mV)
E_K = -77;    % Potassium reversal potential (mV)
E_L = -54.4;  % Leak reversal potential (mV)
V_rest = -65; % Resting membrane potential (mV)

% Time parameters
dt = 0.01;  % Time step (ms)
T = 100;    % Total time (ms)
time = 0:dt:T;  % Time vector

% External current (stimulation)
I_ext = zeros(size(time));
I_ext(500:600) = 10;  % Inject current between 5 and 6 ms (in microamps)

% Initialize variables
V = V_rest * ones(size(time));  % Membrane potential (mV)
m = 0.05;   % Sodium activation gating variable
h = 0.6;    % Sodium inactivation gating variable
n = 0.32;   % Potassium activation gating variable

% Storage for gating variables over time
m_values = zeros(size(time));
h_values = zeros(size(time));
n_values = zeros(size(time));
V_values = zeros(size(time));

% Define rate functions for gating variables
alpha_m = @(V) (0.1 * (V + 40)) / (1 - exp(-(V + 40) / 10));
beta_m = @(V) 4.0 * exp(-(V + 65) / 18);
alpha_h = @(V) 0.07 * exp(-(V + 65) / 20);
beta_h = @(V) 1.0 / (1 + exp(-(V + 35) / 10));
alpha_n = @(V) (0.01 * (V + 55)) / (1 - exp(-(V + 55) / 10));
beta_n = @(V) 0.125 * exp(-(V + 65) / 80);

% Simulation loop
for t = 2:length(time)
    % Update gating variables using Euler method
    m = m + dt * (alpha_m(V(t-1)) * (1 - m) - beta_m(V(t-1)) * m);
    h = h + dt * (alpha_h(V(t-1)) * (1 - h) - beta_h(V(t-1)) * h);
    n = n + dt * (alpha_n(V(t-1)) * (1 - n) - beta_n(V(t-1)) * n);
    
    % Compute conductances for sodium and potassium
    g_Na_t = g_Na * (m^3) * h;
    g_K_t = g_K * (n^4);
    
    % Compute ionic currents
    I_Na = g_Na_t * (V(t-1) - E_Na);
    I_K = g_K_t * (V(t-1) - E_K);
    I_L = g_L * (V(t-1) - E_L);
    
    % Update membrane potential using Euler's method
    V(t) = V(t-1) + dt * (I_ext(t) - (I_Na + I_K + I_L)) / C_m;
    
    % Store values for plotting
    m_values(t) = m;
    h_values(t) = h;
    n_values(t) = n;
    V_values(t) = V(t);
end

% Plot membrane potential over time
figure;
subplot(2,1,1);
plot(time, V_values, 'LineWidth', 2);
title('Hodgkin-Huxley Model: Membrane Potential');
xlabel('Time (ms)');
ylabel('Membrane Potential (mV)');
grid on;

% Plot gating variables over time
subplot(2,1,2);
plot(time, m_values, 'r', 'LineWidth', 1.5); hold on;
plot(time, h_values, 'g', 'LineWidth', 1.5);
plot(time, n_values, 'b', 'LineWidth', 1.5);
legend('m (Na+ activation)', 'h (Na+ inactivation)', 'n (K+ activation)');
title('Gating Variables Over Time');
xlabel('Time (ms)');
ylabel('Gating Variable');
grid on;
```


## Converting to Python
%%[[2024-10-09]] @ 00:28%%

### Why?
%%[[2024-10-09]] @ 00:29%%

I'm perfectly able to do this task in Matlab, so why convert it to python?

1. I like python and want to spend more time using it. 
2. It forces me to interact with and understand the code more deeply
3. I couldn't figure out how to get a Matlab debug environment working in nvim during the lecture.
4. Would have to set up a Matlab LSP for Obsidian to get code highlighting in my notes (I'll do it eventually)

### Log

#### Don't use lambda functions where standard notation will do
%%[[2024-10-09]] @ 00:37%%

Initially I wrote out the rate functions in lambda notation:

```python
alpha_m = lambda V : (0.1 * (V + 40)) / (1 - np.exp(-(V + 40) / 10))
beta_m = lambda V : 4.0 * np.exp(-(V + 65) / 18)
alpha_h = lambda V : 0.07 * np.exp(-(V + 65) / 20)
beta_h = lambda V : 1.0 / (1 + np.exp(-(V + 35) / 10))
alpha_n = lambda V : (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))
beta_n = lambda V : 0.125 * np.exp(-(V + 65) / 80)
```

however this made following the trace backs unnecessarily verbose when dealing with the following issue [[#alpha_n div0]]

Standard notation makes things a little easier to follow in the debugger:

```python
def alpha_m(V): return (0.1 * (V + 40)) / (1 - np.exp(-(V + 40) / 10))
def beta_m(V): return 4.0 * np.exp(-(V + 65) / 18)
def alpha_h(V): return 0.07 * np.exp(-(V + 65) / 20)
def beta_h(V): return 1.0 / (1 + np.exp(-(V + 35) / 10))
def alpha_n(V): return (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))
def beta_n(V): return 0.125 * np.exp(-(V + 65) / 80)
```

#### alpha_n div0
%%[[2024-10-09]] @ 00:42%%

Error presents as 
```
Tutorials/week 2/code/hodgkin_huxley_model.py:52: RuntimeWarning: invalid value 
encountered in scalar divide
  def alpha_n(V): return (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))
Traceback (most recent call last):
  File "/home/joeashton/Sync/Obsidian/SuperVault/Projects/Uni Projects/Neural Co
mputing/Tutorials/week 2/code/hodgkin_huxley_model.py", line 94, in <module>
    V[t] = V[t-1] + dt * (I_ext[t] - (I_Na + I_K + I_L)) / C_m
    ~^^^
ValueError: cannot convert float NaN to integer
```

if `V[t]` failed to compute as it got a `NaN` value where it expected an `int` then we know one of the implied functions failed. 
We know that at some point `alpha_n()` failed, therefore we can assume the issue in `V[t]` was due to the following sequence:

1. `{python}def alpha_n(V): return (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))`
	$\downarrow$ we know that `{python}alpha_n(V[t-1]` returned `NaN`
2. `{python}n += dt * (alpha_n(V[t-1]) * (1 - n) - beta_n(V[t-1]) * n)`
	$\downarrow$ therefore `n` was set to `NaN`
3. `{python}g_K_t = g_K * (n**4)`
	$\downarrow$ making `g_K_t` set to `NaN`
4. `{python}I_K = g_K_t * (V[t-1] - E_K)`
	$\downarrow$ itself making `I_K` set to `NaN`
5. `{python}V[t] = V[t-1] + dt * (I_ext[t] - (I_Na + I_K + I_L)) / C_m`

This is confirmed by the debugger, at `t int = 509`:
   - `n float64 = nan`
   - `g_K_t float64 = nan`
   - `I_K float64 = nan`

tellingly the value of `V[t-1]` at this point is `V[508] int64 = -55`, looking at the definition of `alpha_n()` we can see that this would cause a singularity or `div0` error.

If this is the case then we must consider what this would imply in practice.

##### What dose it all mean?
%%[[2024-10-09]] @ 02:55%%

`{python} alpha_n = lambda V : (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10)) `

is to say that the rate of change of the Potassium channel conductance follows the relationship:

$$\alpha_{n} = \frac{0.01 \times (V_{m} +55)}{1-\Large{ \frac{e^{-(V_{m}+55)}}{10}}}$$

Lets have a look at what that looks like over our expected voltage range:
 
```functionplot
---
title: alpha_a vs V
xLabel: Membrane Potential (V)
yLabel: change in N+ Channel conductivity
bounds: [-100,100,0,2]
disableZoom: false
grid: true
---
f(x) = (0.01 * (x + 55)) / (1 - exp(-(x + 55) / 10))
```

Here we see a linear relationship that becomes asymptotic around $-40$. We should expect an $\alpha_{n}$ value of $0.1$ at $V = -55$. 
To get a clearer picture of why our implementation fails it is helpful to look at the numerator and denominator separately. 

```functionplot
---
title: alpha_a numerator vs denominator
xLabel: Membrane Potential (V)
yLabel: Blue = Numerator, Red = Denominator
bounds: [-100,100,-1,2]
disableZoom: false
grid: true
---
n(x) = (0.01 * (x + 55))
d(x) =(1 - exp(-(x + 55) / 10))
```

As can be seen here at exactly -55 both the numerator and denominator are $0$ the answer to which is a timeless debate that our code doesn't have the time, patience nor interest to answer sensibly. 
In our case we will simply ask it to return `0.1`.

```python
def alpha_n(V): 
    if V == -55:
        return 0.1
    else:
        return (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))
```

Looking above to the definition of $\alpha_m$:
`{python}alpha_m = lambda V : (0.1 * (V + 40)) / (1 - np.exp(-(V + 40) / 10))`
We can expect that to have a similar issue at `V = -40`

```functionplot
---
title: alpha_m numerator vs denominator
xLabel: Membrane Potential (V)
yLabel: Blue = Numerator, Red = Denominator
bounds: [-100,100,-1,2]
disableZoom: false
grid: true
---
n(x) = (0.1 * (x + 40))
d(x) = (1 - exp(-(x + 40) / 10))
f(x) = (0.1 * (x + 40)) / (1 - exp(-(x + 40) / 10))
```

So this should be handled to return `1`:

```python
def alpha_m(V): 
    if V == -40:
        return 1
    else:
        return (0.1 * (V + 40)) / (1 - np.exp(-(V + 40) / 10))
```

##### Alternative solutions considered

I considered the following alternative solutions;

exception handling, return singularity value if a runtime warning is thrown e.g.:
```python
import warnings

def alpha_n(V):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        result = (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10))
        if np.isnan(result):
            return 0.1
        return result
```

or denominator offset constant e.g.:
```python
epsilon = 1e-9  # Small value to prevent div0

def alpha_n(V):
    return (0.01 * (V + 55)) / (1 - np.exp(-(V + 55) / 10) + epsilon)

def alpha_m(V):
    return (0.1 * (V + 40)) / (1 - np.exp(-(V + 40) / 10) + epsilon)
```

However by visual inspection I wouldn't expect to face singularities at any other points with the standard rate functions, and if I wanted to make these offset values a model parameter then I would simply add that variable to the check statement. 

#### V defaults to type int
%%[[2024-10-09]] @ 03:46%%

Initially I defined the `V[]` array as:
`{python}V = np.full(len(time),V_rest)`
as `V_rest` is simply:
`{python}V_rest = -65`

pythons automatic least biggest type allocation set the `V[]` to type `int`, this resulted in a blocky stepped output. This was fixed simply by stating the type in the definition:
`{python}V = np.full(len(time),float(V_rest))`

### Python code

![[hodgkin_huxley_model.py]]

```python title:"hodgkin_huxley_model.py"
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
    I_ext = None  # Excitation profile

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

    # Default External current (stimulation)
    if I_ext is None:
        I_ext = np.zeros(len(time))
        I_ext[500:600] = 10  # Inject current between 5 and 6 ms

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
def standard_plot(time, m_values, h_values, n_values, V_values):

    # Plot Membrane potential over time
    plt.subplot(2,1,1)
    plt.plot(time, V_values, linewidth=2)
    plt.title('Hodgkin-Huxley Model: Membrane Potential')
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane Potential (mV)')
    plt.grid(True)

    # Plot gating variables over time
    plt.subplot(2,1,2)
    plt.plot(time, m_values, 'r', label='m (Na+ activation)', linewidth=1.5)
    plt.plot(time, h_values, 'g', label='h (Na+ inactivation)', linewidth=1.5)
    plt.plot(time, n_values, 'b', label='n (K+ activation)', linewidth=1.5)
    plt.legend(loc='best')
    plt.title('Gating Variables Over Time')
    plt.xlabel('Time (ms)')
    plt.ylabel('Gating Variable')
    plt.grid(True)

def plot_defaults():
    time, m_values, h_values, n_values, V_values = hodgkin_huxley()
    standard_plot(time, m_values, h_values, n_values, V_values)
    plt.show()

plot_defaults()
```
## Task 1: Run the simulation code

### Default Outputs

![[week 2 - Simulating Neural Action Potentials - Membrane Potentials (default settings).png]]

![[week 2 - Simulating Neural Action Potentials - gating variables (defaults).png]]

### 1. What happens when the sodium channels open?
%%[[2024-10-03]] @ 12:37%%

When the Sodium $Na^{+}$ channels open the membrane potential increases rapidly as $Na^{+}$ ions flood into the neuron. 

### 2. What happens when the potassium channel opens?

The [[membrane potential]] decreases rapidly as potassium $K^{+}$ ions flood out of the neuron.

### 3. Discuss the results and their biological significance.


## Task 2: Modifications and Exploration

### Vary the current injection

1. Modify the current injection change by putting the values 1, 5, 10, 15, 20. What do you observe in the action potential and the channels?

#### Code
%%[[2024-10-09]] @ 22:11%%

Including the snippet detailed above in [[#Python code]] [[hodgkin_huxley_model.py]]
This was achieved with the following scripts:

##### Static values

![[varying_current_injection_HodgkinHuxleyModel.py]]
```python title: "varying_current_injection_HodgkinHuxleyModel.py"
import numpy as np
from matplotlib import pyplot as plt 
import hodgkin_huxley_model as hh

I_stim = [1,5,10,15,20]

for n, i in enumerate(I_stim):

    plt.gcf().text(0.05, 0.82 - (n * (0.80 / len(I_stim))), 
                   f'I_stim = {i} µA/cm²', 
                   fontsize=12, 
                   va='center', 
                   ha='right', 
                   rotation=90)

    if n == 0: showtitle = True
    else: showtitle = False

    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50,I_stim=i)
    plt.subplot(5,2,2*n+1)
    hh.plot_v_by_t(time, V_values, title=showtitle)

    plt.subplot(5,2,2*n+2)
    hh.plot_gating_by_t(time, m_values, h_values, n_values, title=showtitle, legend=showtitle)

plt.show()
```

##### Animation
%%[[2024-10-10]] @ 00:30%%

```python title: "varying_current_injection_HodgkinHuxleyModel_animation.py"
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import hodgkin_huxley_model as hh  # Model file [[hodgkin_huxley_model.py]] see above

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
    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50, I_stim=I_stim)
    
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
```

#### Results
%%[[2024-10-09]] @ 22:14%%

The following are the [[membrane potential]]'s and gating variables over a $50\ ms$ window for stimuli of $1$, $5$, $10$, $15$, $20$ $\micro A$ for a $1\ ms$ burst. 

![[week 2 - Simulating Neural Action Potentials - varying stimulation current.png]]

However, to get a more dynamic view of how stimulation current affects the simulated [[action potential]] an animation is helpful.

![[week 2 - Simulating Neural Action Potentials - varying stimulation current animation.gif]]

#### Observations
%%[[2024-10-09]] @ 23:01%%

In instances where the activation threshold was met ($5\ \micro A$ and up) the the resulting [[action potential]]'s are all very similar, the key difference is a slight temporal shift due to the higher currents reaching the activation threshold more quickly.

### Vary Conductance

2. What happens if the sodium or potassium conductance is reduced (mimicking channel block)?

3. What is the effect of increasing the sodium conductance? Try to increase it gradually (150,200, 300, etc.). Observe how the action potential changes at each step. Pay attention to:
	- Peak [[membrane potential]]
	- Speed of [[action potential#Depolarisation]]
	- Duration of the [[action potential]]

4. Try decreasing the external current while keeping **gNa** high to see how little current is needed to trigger an action potential.

5. Test how sensitive the neuron becomes to small stimuli when sodium conductance is high.

6. Increase **gNa** to very high values (e.g. 500 mS/cm2) and see if you observe abnormal repetitive firing or hyper-excitability.
#### Code

Very similar to the [[#Code]] from the previous section, the key changes being the variable and the range of values investigated.

##### Sodium
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import hodgkin_huxley_model as hh  

### Static values

## Set values
g_Na = [50,100,150,200,250]

## Simulate and plot
for n, i in enumerate(g_Na):

    # plt.gcf().text(0.05, 0.82 - (n * (0.80 / len(g_Na))), f'g_Na = {i} µA/cm²', fontsize=12, va='center', ha='right', rotation=90)
    plt.gcf().text(0.03, 0.9 - (n * (0.98 / len(g_Na))), f'g_Na = {i} mS/cm²', fontsize=12, va='center', ha='right', rotation=90)

    if n == 0: showtitle = True
    else: showtitle = False

    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50,g_Na=i)
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
g2.legend(loc='upper right')

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
    g_Na = 50 + 5 * i  # Vary g_Na over time
    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(g_Na=g_Na)
    
    # Update the current g_Na value
    g1.set_title(f'Membrane Potential (g_Na = {g_Na} mS/cm²)')

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
```

##### Potassium
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import hodgkin_huxley_model as hh  

### Static values

## Set values
g_K = [10,20,30,40,50]

## Simulate and plot
for n, i in enumerate(g_K):

    # plt.gcf().text(0.05, 0.82 - (n * (0.80 / len(g_K))), f'g_K = {i} µA/cm²', fontsize=12, va='center', ha='right', rotation=90)
    plt.gcf().text(0.03, 0.9 - (n * (0.98 / len(g_K))), f'g_K = {i} mS/cm²', fontsize=12, va='center', ha='right', rotation=90)

    if n == 0: showtitle = True
    else: showtitle = False

    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50,g_K=i)
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
g2.legend(loc='upper right')

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
    g_K = 10 + 1 * i  # Vary g_K over time
    time, m_values, h_values, n_values, V_values = hh.hodgkin_huxley(T=50, g_K=g_K)
    
    # Update the current g_K value
    g1.set_title(f'Membrane Potential (g_K = {g_K} mS/cm²)')

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
```

#### Results
%%[[2024-10-10]] @ 11:52%%

##### Varying Sodium conductance
![[week 2 - Simulating Neural Action Potentials - varying Na+ conductance.png]]

![[week 2 - Simulating Neural Action Potentials - varying Na+ conductance animation.gif]]

##### Varying Potassium conductance

![[week 2 - Simulating Neural Action Potentials - varying K+ conductance.png]]

![[week 2 - Simulating Neural Action Potentials - varying K+ conductance animation.gif]]

#### Observations

##### Effects of Varying Sodium Channel Conductance
%%[[2024-10-23]] @ 15:36%%

Increasing the sodium channel conductance appears to bias the neuron towards firing, and vice versa. This is to be expected based on the design of our model where `g_Na` represents the ease with which sodium ions are allowed to pass through hydrophilic channels though the membrane wall. 




![[Hodgkin-Huxley - Membrane circuit.excalidraw]]
#WIP 
