% Parameters
t_spike = 10;                % Time of spike occurrence (ms)
I_0 = 1;                     % Amplitude of synaptic input (nA)
T = 100;                     % Total time for simulation (ms)
dt = 0.1;                    % Time step (ms)
time = 0:dt:T;               % Time vector

% Different synaptic decay constants
tau_syn_fast = 5;            % Fast decay (ms)
tau_syn_slow = 20;           % Slow decay (ms)

% Synaptic input calculations using the simple exponential decay formula
I_syn_fast = I_0 * exp(-(time - t_spike) / tau_syn_fast) .* (time >= t_spike);  % Input for fast decay
I_syn_slow = I_0 * exp(-(time - t_spike) / tau_syn_slow) .* (time >= t_spike);  % Input for slow decay

% Synaptic input with rise and decay (alpha function)
I_syn_rise_fast = I_0 * (time - t_spike) ./ tau_syn_fast .* exp(-(time - t_spike) / tau_syn_fast) .* (time >= t_spike);
I_syn_rise_slow = I_0 * (time - t_spike) ./ tau_syn_slow .* exp(-(time - t_spike) / tau_syn_slow) .* (time >= t_spike);

% Plotting the results
figure;
% Plot fast and slow decay (exponential only)
plot(time, I_syn_fast, 'r', 'LineWidth', 2); hold on;
plot(time, I_syn_slow, 'b', 'LineWidth', 2);

% Plot rise and decay (alpha function)
plot(time, I_syn_rise_fast, '--r', 'LineWidth', 2);  % Dashed line for rise and decay (fast)
plot(time, I_syn_rise_slow, '--b', 'LineWidth', 2);  % Dashed line for rise and decay (slow)

% Labels and legend
title('Synaptic Input Decay with and without Rise Over Time');
xlabel('Time (ms)');
ylabel('Synaptic Input I_{syn}(t)');
legend('Fast Decay (\tau_{syn} = 5 ms)', 'Slow Decay (\tau_{syn} = 20 ms)', ...
       'Fast Rise & Decay', 'Slow Rise & Decay');
grid on;
