% Hodgkin-Huxley Neuron Model Simulation

% Parameters
V_stim = 10; % external current (A)
C_m = 1.0;    % Membrane capacitance, uF/cm^2
g_Na = 150.0; % Maximum conductance of sodium (mS/cm^2)
g_K = 36.0;   % Maximum conductance of potassium (mS/cm^2)
g_L = 0.3;    % Leak conductance (mS/cm^2)
E_Na = 50;    % Sodium reversal potential (mV)
E_K = -77;    % Potassium reversal potential (mV)
E_L = -54.4;  % Leak reversal potential (mV)
V_rest = -65; % Resting membrane potential (mV)

% Initial variable states
V = V_rest * ones(size(time));  % Membrane potential (mV)
m = 0.05;   % Sodium activation gating variable
h = 0.6;    % Sodium inactivation gating variable
n = 0.32;   % Potassium activation gating variable

y0 = [V;m;h;n];

% Time parameters
dt = 0.01;  % Time step (ms)
T = 100;    % Total time (ms)
time = 0:dt:T;  % Time vector

