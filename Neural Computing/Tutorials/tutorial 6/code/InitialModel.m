% LTP Simulation Parameters
dt = 0.01;                  % Time step (ms)
T = 1000;                   % Total simulation time (ms)
time = 0:dt:T;              % Time vector
firing_rate = 100;          % Firing rate of pre-synaptic neuron (Hz)
n_spikes = round(firing_rate * (T / 1000));  % Total spikes based on firing rate
spike_times = sort(randi(length(time), 1, n_spikes));  % Random spike times

% Calcium and Synaptic Weight Parameters
Ca = zeros(1, length(time));    % Calcium concentration
tau_Ca = 50;                    % Decay constant for calcium concentration (ms)
Ca_increment = 1;               % Calcium increase per spike
threshold_Ca = 3;             % Threshold calcium level for potentiation
tau_LTP = 100;                  % Time constant for synaptic weight decay (ms)
w = zeros(1, length(time));     % Synaptic weight over time
w(1) = 0.5;                     % Initial synaptic weight
alpha_LTP = 0.005;              % Learning rate for LTP (rate of synaptic weight increase)

% Simulation Loop
for t = 2:length(time)
    % Check if there's a spike at the current time
    if ismember(t, spike_times)
        % Increase calcium concentration with each spike
        Ca(t) = Ca(t-1) + Ca_increment;
    else
        % Decay calcium concentration over time
        Ca(t) = Ca(t-1) * exp(-dt / tau_Ca);
    end
    
    % Update synaptic weight based on calcium level
    if Ca(t) >= threshold_Ca
        % Increase synaptic weight for LTP
        dw = alpha_LTP * (Ca(t) - threshold_Ca);
        w(t) = w(t-1) + dw;
    else
        % Decay synaptic weight in absence of sufficient calcium
        w(t) = w(t-1) * exp(-dt / tau_LTP);
    end
end

% Plotting Results
figure;
subplot(3, 1, 1);
plot(time, Ca);
title('Calcium Concentration Over Time');
xlabel('Time (ms)');
ylabel('Calcium Level');

subplot(3, 1, 2);
plot(time, w);
title('Synaptic Weight (LTP) Over Time');
xlabel('Time (ms)');
ylabel('Synaptic Weight (w)');

subplot(3, 1, 3);
plot(time, ismember(1:length(time), spike_times));
title('Pre-Synaptic Spike Train');
xlabel('Time (ms)');
ylabel('Spike (1=Yes, 0=No)');
