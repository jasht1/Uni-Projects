% Compute the average membrane potential across all neurons
mean_membrane_potential = mean(V, 1);  % Mean potential across neurons at each time step

% Perform Fourier Transform to identify frequency components
Fs = 1 / dt;  % Sampling frequency (Hz)
L = length(time);  % Length of signal
Y = fft(mean_membrane_potential);  % Fourier Transform
P2 = abs(Y / L);  % Two-sided spectrum
P1 = P2(1:floor(L/2) + 1);  % Single-sided spectrum
P1(2:end-1) = 2 * P1(2:end-1);  % Adjust spectrum

% Define frequency axis
f = Fs * (0:(floor(L/2))) / L;

% Plot the power spectrum
figure;
plot(f, P1);
title('Power Spectrum of Network Activity');
xlabel('Frequency (Hz)');
ylabel('Power');
xlim([1 8]);  % Focus on frequencies up to 50 Hz
