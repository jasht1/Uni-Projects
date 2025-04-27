%% Params
omega_b = 5;  % Cutoff frequency (rad/s)

%% Define transfer function H(s)
num_s = omega_b^2;
den_s = [1, sqrt(2)*omega_b, omega_b^2];

H_s = tf(num_s, den_s);  % Analogue transfer function in Laplace domain

%% Plot results
figure('NumberTitle', 'off');
tiledlayout(1, 2);  % 1 row, 2 columns
sgtitle('Analogue Butterworth Low Pass Filter Response');

%%% Impulse response
% nexttile;
impulse(H_s);
title('Impulse Response');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

%%% Frequency response (magnitude and phase)
% nexttile;
bode(H_s);
title('Frequency Response');
grid on;
