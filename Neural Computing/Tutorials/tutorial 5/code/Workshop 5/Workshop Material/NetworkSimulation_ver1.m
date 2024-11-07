% Simulation parameters
dt = 0.01;               % Time step (ms)
T = 1000;                % Total time (ms)
time = 0:dt:T;           % Time vector
n_neurons = 3;          % Number of neurons (this can be modified)

% LIF neuron parameters
V_rest = -65;            % Resting membrane potential (mV)
V_th = -50;              % Threshold for spike (mV)
V_reset = -70;           % Reset voltage after spike (mV)
tau_m = 20;              % Membrane time constant (ms)
R_m = 3;                 % Membrane resistance (MOhms)

% External input: Theta oscillation range (4-8 Hz) with noise
theta_frequency = 6;  % Theta frequency (6 Hz)
I_ext = zeros(n_neurons, length(time));  % Initialize external input matrix
for i = 1:n_neurons
    I_ext(i, :) = 5 * sin(2 * pi * theta_frequency * time / 1000) + 0.5 * randn(1, length(time));  % Theta input + noise
end

% Initialize variables
V = V_rest * ones(n_neurons, length(time));  % Membrane potential for each neuron
spike_times = cell(n_neurons, 1);            % Store spike times
spike_train = zeros(n_neurons, length(time)); % Store spike occurrences

% Simulation loop
for t = 2:length(time)
    for i = 1:n_neurons
        % Update membrane potential with LIF dynamics
        dV = (-(V(i, t-1) - V_rest) + R_m * I_ext(i, t)) * (dt / tau_m);
        V(i, t) = V(i, t-1) + dV;

        % Check if the neuron fires a spike
        if V(i, t) >= V_th
            V(i, t) = 30;  % Spike (for visualization)
            spike_times{i}(end+1) = time(t);  % Record spike time
            spike_train(i, t) = 1;            % Mark spike in spike train
            V(i, t+1) = V_reset;             % Reset after spike
        end
    end
end

% Create subplots for each neuron
figure;
for i = 1:n_neurons
    subplot(n_neurons, 1, i);  % Create a subplot for each neuron
    plot(time, V(i, :));
    title(['Neuron ' num2str(i)]);
    xlabel('Time (ms)');
    ylabel('Membrane Potential (mV)');
    ylim([-70 -20]);  % Adjust the y-axis limits for clear visualization of spikes
end
