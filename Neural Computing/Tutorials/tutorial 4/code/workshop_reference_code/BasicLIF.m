% Parameters of the LIF model
tau_m = 20;        % Membrane time constant (ms)
R = 3;             % Membrane resistance (MΩ)
V_rest = -65;      % Resting potential (mV)
V_th = -55;        % Threshold potential (mV) (Try lowering the threshold)
V_reset = -70;     % Reset potential after spike (mV)
I = 4;             % Input current (nA) (Increase current)
T = 100;           % Total simulation time (ms)
dt = 0.1;          % Time step (ms)
t = 0:dt:T;        % Time vector

% Initialize membrane potential
V = V_rest * ones(1, length(t)); 
spike_train = zeros(1, length(t)); % To track spikes

% Simulating the LIF neuron
for i = 2:length(t)
    % Update membrane potential using Euler method
    dV = (-(V(i-1) - V_rest) + R * I) * (dt / tau_m);
    V(i) = V(i-1) + dV;
    
    % Check for spike
    if V(i) >= V_th
        V(i) = V_reset;   % Reset the potential
        spike_train(i) = 1; % Record a spike
    end
end

% Plotting the results
figure;
subplot(2,1,1);
plot(t, V, 'LineWidth', 2);
xlabel('Time (ms)','FontSize',14);
ylabel('Membrane Potential (mV)','FontSize',14);
title('Leaky Integrate-and-Fire Model','FontSize',24);
ylim([-80 -40]);

% Plotting spike train
subplot(2,1,2);
stem(t, spike_train, 'Marker', 'none');
xlabel('Time (ms)','FontSize',14);
ylabel('Spike','FontSize',14);
title('Spike Train','FontSize',24);
xlim([0 T]);

