# Understanding Neuronal Voltage Propagation through Cable Theory in MATLAB

CMP9783: Neural Computing
Workshop Title: Understanding Neuronal Voltage Propagation through Cable Theory in MATLAB

## Breif


### Workshop Description:

In this hands-on workshop, participants will explore how passive voltage propagation in neurons is modelled using cable theory. The focus will be on how changes in cable parameters affect voltage spread and decay along a dendrite. Participants will be given pre-written MATLAB code that simulates the cable equation, and their task will be to modify the code to explore different conditions and parameters.

The goal is for participants to understand the core concepts of cable theory, and how properties like the length constant, lambda (λ) and time constant (τ) influence the spatial and temporal behaviour of voltage propagation in neurons. By the end of the workshop, participants will be able to run simulations, analyse results, and interpret how changes in the model's parameters affect the neuron’s behaviour.

### Workshop Objectives

By the end of this workshop, participants will:

1. Understand the fundamentals of cable theory and its role in modelling neuronal voltage propagation.
2. Learn how to use MATLAB to simulate the cable equation with given code.
3. Modify the code to explore the effects of different cable parameters (e.g., lambda, τ, dendrite length).
4. Analyse and visualize the results of the simulation to draw conclusions about neuronal signal propagation.

### Tasks

#### Task 1 Modifying the Length Constant λ (20 minutes)

- Objective: Investigate how the length constant $\lambda$ affects voltage propagation along the dendrite.

1. Modify the provided code to increase and decrease $\lambda$.

2. Run the simulation and observe how the change in $\lambda$ affects how far the voltage travels before decaying.

3. Plot and compare the voltage propagation for different values of $\lambda$.

#### Task 2: Adjusting the Time Constant Adjusting the Time Constant $\tau$ (20 minutes)

- Objective: Explore the effect of the time constant τ on the temporal decay of voltage.

1. Modify the code to change τ and observe how it influences the rate of temporal decay.

2. Run the simulation with different values of τ, and visualize how quickly the voltage decays over time.

3. Discuss how the temporal decay relates to the neuron’s membrane properties.

#### Task 3 Exploring the Effect of Dendrite Length (25 minutes)

- Objective: Investigate how the length of the dendrite influences voltage propagation.

1. Modify the code to simulate voltage propagation for different dendrite lengths (e.g., L=2, L = 2.5, L = 3, L= 3.5, L = 4).

2. Run the simulation and observe how dendrite length affects voltage spread and decay.

3. Compare voltage propagation across shorter and longer dendrites and interpret the results.

#### Task 4: Introducing a Second Voltage Spike (25 minutes)

- Objective: Simulate the effect of multiple voltage spikes along the dendrite.

1. Modify the code to introduce a second voltage spike at a different location along the dendrite.

2. Observe how the voltage spikes interact and propagate along the dendrite.

3. Discuss the effect of superposition and interference between the two voltage signals.
