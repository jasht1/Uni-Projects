
%% Simulation Parameters

% Time
T_sim = 5; % Simulation length (s)
t = T_sim/200; % Time increment (s)
T = (0:t:T_sim-t); % Time array

% Road disturbance
road = zeros(1, length(T));

% Actuator (passive suspension if not defined)
if ~exist('u_f_s', 'var')
  u_f_s = zeros(1, T_sim/t);
end

% Initial conditions
V_i = 0.5; % Initial velocity (m/s)

%% model paramiters
type = "Passive";
QC_params
plant = ss(A, B, C, D);

% type = "Active";
% tune_active_suspension
% plant = minreal(ss(tuned_suspension));

U = [road; zeros(1, T_sim/t)];

%% Simulation and Plotting

figure
tiledlayout(2,1, "TileSpacing", "compact", "Padding", "compact");

scenarios = {...
  struct('description', "Initial Car Body Velocity", 'IC', [0, V_i, 0, 0]), ...
  struct('description', "Initial Wheel Velocity", 'IC', [0, 0, 0, V_i]) ...
  };

for scenario = scenarios
  scenario = scenario{1}; % why is matlab like this? :smh
  
  % Initial conditions for the scenario
  IC = scenario.IC;
  description = scenario.description;
  
  %% Simulation
  y = lsim(plant, U, T, IC);
  
  %% Plotting
  nexttile
  
  plot_series = {
    struct('data', road,      'label', 'Road Disturbance (m)'),
    struct('data', y(:,4),    'label', 'Wheel Displacement (m)'),
    struct('data', y(:,5),    'label', 'Wheel Velocity (m/s)'),
    struct('data', y(:,1),    'label', 'Body Displacement (m)'),
    struct('data', y(:,2),    'label', 'Body Velocity (m/s)'),
    struct('data', y(:,3),    'label', 'Body Acceleration (m/s^2)')
    };
  
  rms(y(:,3))
  hold on
  title("Response of " +type+ " Suspension to " + description + " of " + V_i + " m/s");
  for i = 1:length(plot_series)
    plot(T, plot_series{i}.data, 'DisplayName', plot_series{i}.label);
  end
  xlabel("Time (seconds)");
  ylabel("Amplitude");
  grid on;
  hold off
end
legend('Location', 'southoutside','NumColumns', 3);
