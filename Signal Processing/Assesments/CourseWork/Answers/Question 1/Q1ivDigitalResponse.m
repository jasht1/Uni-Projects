%% params
omega_b = 5;                 % Cutoff frequency (rad/s)
omega_s = 10 * omega_b;      % Sampling frequency (rad/s)
Fs = omega_s / (2*pi);       % Sampling frequency (Hz)

%% Define transfer function H(s)
num_s = [omega_b^2];
den_s = [1, sqrt(2)*omega_b, omega_b^2];

H_s = tf(num_s, den_s);  % Analogue transfer function in Laplace domain

%% Bilinear transform to get H(z)
[num_z, den_z] = bilinear(num_s, den_s, Fs);

%% Plot results
figure('NumberTitle', 'off');
tiledlayout(1, 2);  % 1 row, 2 columns
sgtitle('Digital Butterworth Low Pass Filter');

%%% Impulse response
%nexttile;
impz(num_z, den_z);
title('Impulse Response');
xlabel('n (samples)');
ylabel('Amplitude');
grid on;

%%% Frequency response (magnitude and phase)
%nexttile;
figure()
freqz(num_z, den_z, 1024, Fs); % creates it's own figure ANNOYING
title('Frequency Response');
