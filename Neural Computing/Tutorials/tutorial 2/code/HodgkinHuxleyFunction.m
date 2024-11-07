% Hodgkin-Huxley Neuron Model Simulation

function Hodgkin_Huxley = hh_ODE(t, y, V_ext, g_Na, g_K,  g_L, E_Na, E_K, E_L, C_m)

%% State variables
V = y(1);  % Membrane potential
m = y(2);  % Sodium activation gating variable
h = y(3);  % Sodium inactivation gating variable
n = y(4);  % Potassium activation gating variable

%% Defining functions

% Define rate functions for gating variables
alpha_m = (0.1 * (V + 40)) / (1 - exp(-(V + 40) / 10));
beta_m = 4.0 * exp(-(V + 65) / 18);
alpha_h = 0.07 * exp(-(V + 65) / 20);
beta_h = 1.0 / (1 + exp(-(V + 35) / 10));
alpha_n = (0.01 * (V + 55)) / (1 - exp(-(V + 55) / 10));
beta_n = 0.125 * exp(-(V + 65) / 80);

% Compute conductances
g_Na_t = g_Na * (m^3) * h;
g_K_t = g_K * (n^4);

% Ionic currents
I_Na = g_Na_t * (V - E_Na);
I_K = g_K_t * (V - E_K);
I_L = g_L * (V - E_L);

%% ODEs

% membrane potential
dV_dt = (I_ext - (I_Na + I_K + I_L)) / C_m;

% gating variables
dm_dt = alpha_m * (1 - m) - beta_m * m;
dh_dt = alpha_h * (1 - h) - beta_h * h;
dn_dt = alpha_n * (1 - n) - beta_n * n;

% Output derivatives
Hodgkin_Huxley = [dV_dt; dm_dt; dh_dt; dn_dt];

end
