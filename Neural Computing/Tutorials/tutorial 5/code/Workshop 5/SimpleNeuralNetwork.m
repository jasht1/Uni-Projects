% Parameters of the LIF model for a network of neurons
num_neurons = 3;    % Number of neurons in the network
tau_m = 2;         % Membrane time constant (ms)
R = 10;              % Membrane resistance (MΩ)
V_rest = -65;       % Resting potential (mV)
V_th = -50;         % Threshold potential (mV)
V_reset = -70;      % Reset potential after spike (mV)
T = 200;            % Total simulation time (ms)
dt = 0.1;           % Time step (ms)
t = 0:dt:T;         % Time vector

% Refractory period
refractory_period = 5;    % Refractory period (ms)
ref_time = zeros(1, num_neurons); % Refractory time for each neuron

% Input current (external): Sinusoidal + Noise
f = 0.1;  % Frequency of the sinusoidal input (Hz)
I0 = 10; % Current Amplitude
I_sin = I0 * sin(2 * pi * f * t);  % Sinusoidal input
I_noise = 0.5 * randn(num_neurons, length(t));  % Random noise for each neuron
I_total = I_sin + I_noise;  % Total input current for each neuron

% Weight matrix for synaptic connections between neurons
% Positive values for excitatory connections, negative for inhibitory
W = [0 1 -0.5; 
     1 0 0.7; 
    -0.3 0.4 0]; % Synaptic weights between neurons

% Initialize membrane potentials for each neuron
V = V_rest * ones(num_neurons, length(t));
spike_train = zeros(num_neurons, length(t)); % To track spikes

% Simulating the network of LIF neurons
for i = 2:length(t)
    for n = 1:num_neurons
        if ref_time(n) > 0  % Check if neuron is in refractory period
            ref_time(n) = ref_time(n) - dt;  % Decrease the refractory time
            V(n, i) = V_reset;               % Hold the membrane at reset value
        else
            % Compute synaptic input from other neurons
            synaptic_input = 0;
            for m = 1:num_neurons
                if spike_train(m, i-1) == 1  % If pre-synaptic neuron fired
                    synaptic_input = synaptic_input + W(n, m);
                end
            end
            
            % Total input current for this neuron (external + synaptic)
            I = I_total(n, i) + synaptic_input;
            
            % Update membrane potential using Euler method
            dV = (-(V(n, i-1) - V_rest) + R * I) * (dt / tau_m);
            V(n, i) = V(n, i-1) + dV;
            
            % Check for spike
            if V(n, i) >= V_th
                V(n, i) = V_reset;          % Reset the potential
                spike_train(n, i) = 1;      % Record a spike
                ref_time(n) = refractory_period; % Enter refractory period
            end
        end
    end
end

% Plotting the results
figure;
for n = 1:num_neurons
    subplot(num_neurons+1,1,n);
    plot(t, V(n,:), 'LineWidth', 2);
    xlabel('Time (ms)');
    ylabel(['V_' num2str(n) ' (mV)']);
    title(['Neuron ' num2str(n) ' Membrane Potential']);
    ylim([-80 0]);
end

% Plotting spike train
subplot(num_neurons+1,1,num_neurons+1);
for n = 1:num_neurons
    hold on;
    stem(t, spike_train(n,:) * n, 'Marker', 'none');  % Spikes for each neuron
end
xlabel('Time (ms)');
ylabel('Neuron #');
title('Spike Train for Neuronal Network');
xlim([0 T]);
ylim([0 num_neurons+1]);
