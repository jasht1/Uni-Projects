% Simulation parameters
dt = 0.01;               % Time step (ms)
T = 1000;                % Total time (ms)
time = 0:dt:T;           % Time vector
n_neurons = 6;           % Number of neurons (3 neurons per cluster)

% LIF neuron parameters
V_rest = -65;            % Resting membrane potential (mV)
V_th = -50;              % Threshold for spike (mV)
V_reset = -70;           % Reset voltage after spike (mV)
tau_m = 2;               % Membrane time constant (ms)
R_m = 3;                 % Membrane resistance (MOhms)

% Refractory period parameters
tau_ref = 2;             % Refractory period (ms)
refractory = zeros(n_neurons, 1);  % Tracks refractory state

% Synaptic weights for two clusters (3 neurons per cluster)
w = [0 0.8 0.8 -0.7 -0.7 -0.7;  % Neuron 1 (Cluster 1)
     0.8 0 0.8 -0.7 -0.7 -0.7;  % Neuron 2 (Cluster 1)
     0.8 0.8 0 -0.7 -0.7 -0.7;  % Neuron 3 (Cluster 1)
    -0.7 -0.7 -0.7 0 0.8 0.8;   % Neuron 4 (Cluster 2)
    -0.7 -0.7 -0.7 0.8 0 0.8;   % Neuron 5 (Cluster 2)
    -0.7 -0.7 -0.7 0.8 0.8 0];  % Neuron 6 (Cluster 2)

% Synaptic time constant for exponential decay
tau_syn = 10;            % Synaptic decay time constant (ms)
I_synaptic = zeros(n_neurons, length(time));  % Track synaptic currents

% External input settings for different firing patterns
% Adjusting external inputs to induce different patterns in different neurons/clusters
% Cluster 1: Regular firing with minimal noise (constant input over time)
% Cluster 2: Irregular firing and bursting with oscillating input over time
I_ext = zeros(n_neurons, length(time));  % Initialize external input matrix

% Cluster 1 neurons (1-3) get constant external input over time
I_ext(1:3, :) = repmat([7 7 7]', 1, length(time));  % Constant input for regular spiking neurons

% Cluster 2 neurons (4-6) get oscillating external input (for burst firing)
I_ext(4, :) = 10 * sin(2 * pi * 0.01 * time);  % Oscillating input for neuron 4
I_ext(5, :) = 10 * sin(2 * pi * 0.01 * time);  % Oscillating input for neuron 5
I_ext(6, :) = 10 * sin(2 * pi * 0.01 * time);  % Oscillating input for neuron 6

% Increased noise for Cluster 2 to induce variability and irregular firing
sigma_noise_cluster_1 = 0.2;  % Minimal noise for regular spiking
sigma_noise_cluster_2 = 0.8;  % Higher noise for irregular/bursting behavior

% Initialize variables
V = V_rest * ones(n_neurons, length(time));  % Membrane potential for each neuron
spike_times = cell(n_neurons, 1);            % Store spike times
spike_train = zeros(n_neurons, length(time)); % Store spike occurrences for synchrony

% Loop through time steps
for t = 2:length(time)
    for i = 1:n_neurons
        if refractory(i) > 0
            % If in refractory period, keep voltage at reset and reduce refractory time
            V(i, t) = V_reset;
            refractory(i) = refractory(i) - dt;
        else
            % Update synaptic input with exponential decay for all synapses
            I_synaptic(i, t) = I_synaptic(i, t-1) * exp(-dt / tau_syn);
            
            % Compute synaptic input from spikes of other neurons
            for j = 1:n_neurons
                if j ~= i && ~isempty(spike_times{j})
                    last_spike_time = spike_times{j}(end);
                    if time(t) - last_spike_time <= dt
                        % Spike occurred at this time step, apply synaptic weight
                        I_synaptic(i, t) = I_synaptic(i, t) + w(i, j);
                    end
                end
            end

            % Add external input current with noise
            if i <= 3  % Cluster 1 (Regular firing)
                I_noise = sigma_noise_cluster_1 * randn(1);  % Minimal Gaussian white noise
                I_total = I_ext(i, t) + I_synaptic(i, t) + I_noise;
            else  % Cluster 2 (Irregular/Burst firing)
                I_noise = sigma_noise_cluster_2 * randn(1);  % Higher noise
                I_total = I_ext(i, t) + I_synaptic(i, t) + I_noise;
            end

            % Update membrane potential with LIF dynamics
            dV = (-(V(i, t-1) - V_rest) + R_m * I_total) * (dt / tau_m);
            V(i, t) = V(i, t-1) + dV;

            % Check if the neuron fires a spike
            if V(i, t) >= V_th
                V(i, t) = 30;  % Spike (for visualization)
                spike_times{i}(end+1) = time(t);  % Record spike time
                spike_train(i, t) = 1;            % Mark spike in spike train
                refractory(i) = tau_ref;          % Enter refractory period
                V(i, t+1) = V_reset;             % Reset after spike
            end
        end
    end
end

%% Plot the Results
% 1. Membrane potentials of all neurons
figure;
for i = 1:n_neurons
    subplot(n_neurons, 1, i);
    plot(time, V(i, :));
    title(['Neuron ', num2str(i), ' Membrane Potential']);
    xlabel('Time (ms)');
    ylabel('Voltage (mV)');
    ylim([-80 40]);  % Set limits to visualize spikes clearly
end

% 2. Spike raster plot
figure;
hold on;
for i = 1:n_neurons
    for spike = 1:length(spike_times{i})
        plot([spike_times{i}(spike) spike_times{i}(spike)], [i-0.4 i+0.4], 'k');
    end
end
title('Spike Raster Plot');
xlabel('Time (ms)');
ylabel('Neuron Index');
yticks(1:n_neurons);
ylim([0.5 n_neurons + 0.5]);
hold off;

% 3. Synchrony measure - Correlation between neurons
correlation_matrix = corr(spike_train');  % Compute the correlation matrix between spike trains

% Plot the correlation matrix
figure;
imagesc(correlation_matrix);  % Visualize the matrix
title('Correlation Between Neuron Spike Trains');
xlabel('Neuron');
ylabel('Neuron');
colorbar;

% Adjust the color scale to highlight differences
caxis([-1 1]);  % Set colorbar limits to cover the full range of correlations (-1 to 1)

% Use a colormap that enhances visibility of differences (e.g., jet or parula)
colormap("jet");  % You can try different colormaps like 'parula', 'hot', etc.

% 4. Spike histograms (firing rate over time)
figure;
for i = 1:n_neurons
    subplot(n_neurons, 1, i);
    histogram(spike_times{i}, 50);  % 50 bins
    title(['Neuron ', num2str(i), ' Spike Histogram']);
    xlabel('Time (ms)');
    ylabel('Spike Count');
end

