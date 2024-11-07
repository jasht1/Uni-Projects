% Simulation parameters
dt = 0.01;               % Time step (ms)
T = 1000;                % Total time (ms)
time = 0:dt:T;           % Time vector (1 second)
n_neurons = 6;           % Number of neurons (3 neurons per cluster)

% LIF neuron parameters
V_rest = -65;            % Resting membrane potential (mV)
V_th = -50;              % Threshold for spike (mV)
V_reset = -70;           % Reset voltage after spike (mV)
tau_m = 20;              % Membrane time constant (ms)
R_m = 6;                 % Membrane resistance (MOhms)

% Refractory period parameters
tau_ref = 2;             % Refractory period (ms)
refractory = zeros(n_neurons, 1);  % Tracks refractory state

% Synaptic weights for two clusters (3 neurons per cluster)
w_intra = 0.5;  % Strong intra-cluster connections
w_inter = -0.2; % Weaker or inhibitory inter-cluster connections
weight = zeros(n_neurons, n_neurons);
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
tau_syn = 20;            % Synaptic decay time constant (ms)
I_synaptic = zeros(n_neurons, length(time));  % Track synaptic currents

% External input (for stimulation) - Equal external input for both clusters
I_ext = [1 4 1 4 1 4];  % Equal external input for all neurons
sigma_noise = 0.5;            % Standard deviation of noise (nA)

% Oscillatory input parameters
A = 6;                       % Amplitude of oscillatory input
freq = 6;                   % Frequency of oscillation (in Hz)
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

%% Summing the cumulative activity of all neurons
cumulative_spike_train = sum(spike_train, 1);  % Summing spike trains of all neurons

%% Visualization

% 1. Cumulative activity (Time Domain)
figure;
plot(time, cumulative_spike_train);
title('Cumulative Activity of All Neurons (Summed Spike Trains)');
xlabel('Time (ms)');
ylabel('Spike Count');

% 2. Frequency Domain: Spectrogram of Cumulative Activity

figure;
window_size = 256;
overlap = round(window_size * 0.75);  % 75% overlap
nfft = window_size;  % Number of FFT points
spectrogram(cumulative_spike_train, window_size, overlap, nfft, 1/dt, 'yaxis');
title('Spectrogram of Cumulative Network Activity');
xlabel('Time (ms)');
ylabel('Frequency (Hz)');
colorbar;
colormap('parula');  % Alternatively, you can try 'jet'
grid on;

% 3. Frequency Domain: Power Spectral Density of Cumulative Activity
% Define desired frequency bin resolution (0.5 Hz per bin)
freq_bin_resolution = 0.5;  % Hz
sampling_freq = 1 / dt;     % Sampling frequency (Hz)
% Calculate the required window length to achieve 0.5 Hz resolution
window_length = round(sampling_freq / freq_bin_resolution);  % Window size to achieve 0.5 Hz resolution
overlap = round(window_length * 0.75);  % 75% overlap for smoother PSD
% Compute the PSD using pwelch with the desired window length and overlap
[pxx, f] = pwelch(cumulative_membrane_potential, window_length, overlap, [], sampling_freq);
% Plot the PSD with frequency bins, limited to 10 Hz
figure;
plot(f, 10*log10(pxx), 'LineWidth', 1.5);  % Plot in decibels (dB)
title('Power Spectral Density of Summed Membrane Potentials (0.5 Hz Bins)');
xlabel('Frequency (Hz)');
ylabel('Power (dB)');
grid on;
% Limit the x-axis to show frequencies only up to 10 Hz
xlim([0 10]);  % Limit the frequency range to 10 Hz
xticks(0:0.5:10);  % Set x-ticks at 0.5 Hz intervals for clarity



%% 4. Summing the membrane potentials of all neurons
cumulative_membrane_potential = sum(V, 1);  % Sum membrane potentials of all neurons
%% Visualization of Summed Membrane Potentials (Time Domain)
figure;
plot(time, cumulative_membrane_potential, 'LineWidth', 1.5);
title('Summed Membrane Potentials (Electrode Recording Simulation)');
xlabel('Time (ms)');
ylabel('Summed Voltage (mV)');
grid on;
