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
% Positive intra-cluster connections, weaker negative inter-cluster connections
w_intra = 0.5;  % Strong intra-cluster connections
w_inter = -0.2; % Weaker or inhibitory inter-cluster connections
weight = zeros(n_neurons,n_neurons);
for i = 1:n_neurons
    for j = 1:n_neurons
        if (i ~= j)
            if (i <= 3 && j <= 3) || (i > 3 && j > 3)
                weight(i,j) = w_intra;  % Intra-cluster connections
            else
                weight(i,j) = w_inter;  % Inter-cluster connections
            end
        end
    end
end

% Synaptic time constant for exponential decay
tau_syn = 10;            % Synaptic decay time constant (ms)
I_synaptic = zeros(n_neurons, length(time));  % Track synaptic currents

% External input (for stimulation) - Equal external input for both clusters
I_ext = [10 10 10 10 10 10];  % Equal external input for all neurons
sigma_noise = 0.5;            % Standard deviation of noise (nA)

% Oscillatory input parameters
A = 2;                       % Amplitude of oscillatory input
freq = 10;                   % Frequency of oscillation (in Hz)
I_oscillatory = A * sin(2 * pi * freq * time / 1000);  % Oscillatory input over time

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
                        I_synaptic(i, t) = I_synaptic(i, t) + weight(i, j);
                    end
                end
            end

            % Add external input current with noise and oscillatory input
            I_noise = sigma_noise * randn(1);  % Gaussian white noise
            I_total = I_ext(i) + I_synaptic(i, t) + I_noise + I_oscillatory(t);

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
