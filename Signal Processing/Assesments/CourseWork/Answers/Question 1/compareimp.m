% Parameters
omega_b = 5;                    % Cutoff frequency (rad/s)
omega_s = 10 * omega_b;         % Sampling frequency (rad/s)
Fs = omega_s / (2*pi);          % Sampling frequency (Hz)
T = 1 / Fs;                     % Sampling period (s)
N = 50;                         % Number of samples for impulse response

% Continuous-time transfer function H(s)
num_s = omega_b^2;
den_s = [1, sqrt(2)*omega_b, omega_b^2];
H_s = tf(num_s, den_s);         % Analog system

% Get continuous impulse response
t_cont = (0:N-1)*T;             % Continuous time vector aligned with sample rate
y_cont = impulse(H_s, t_cont);  % Impulse response

% Discrete-time coefficients from earlier derived system
b = [0.0675, 0.1350, 0.0675];
a = [1, -1.2765, 0.4129];
x_impulse = [1, zeros(1, N-1)];
y_disc = filter(b, a, x_impulse);  % Discrete impulse response

% Plot comparison
figure;
stem(t_cont, y_disc, 'filled', 'DisplayName', 'Discrete-time (Filter Output)');
hold on;
plot(t_cont, y_cont, 'LineWidth', 1.5, 'DisplayName', 'Continuous-time (H(s))');
legend;
xlabel('Time (s)');
ylabel('Amplitude');
title('Impulse Response Comparison');
grid on;
