% Cluster 1: Neurons 1, 2, 3
mean_membrane_cluster1 = mean(V(1:3, :), 1);  % Mean potential across Cluster 1 neurons

% Cluster 2: Neurons 4, 5, 6
mean_membrane_cluster2 = mean(V(4:6, :), 1);  % Mean potential across Cluster 2 neurons

% Perform Fourier Transform for Cluster 1
Y_cluster1 = fft(mean_membrane_cluster1);  % Fourier Transform for Cluster 1
P2_cluster1 = abs(Y_cluster1 / L);  % Two-sided spectrum
P1_cluster1 = P2_cluster1(1:floor(L/2) + 1);  % Single-sided spectrum
P1_cluster1(2:end-1) = 2 * P1_cluster1(2:end-1);  % Adjust spectrum

% Perform Fourier Transform for Cluster 2
Y_cluster2 = fft(mean_membrane_cluster2);  % Fourier Transform for Cluster 2
P2_cluster2 = abs(Y_cluster2 / L);  % Two-sided spectrum
P1_cluster2 = P2_cluster2(1:floor(L/2) + 1);  % Single-sided spectrum
P1_cluster2(2:end-1) = 2 * P1_cluster2(2:end-1);  % Adjust spectrum

% Define frequency axis
f = Fs * (0:(floor(L/2))) / L;

% Plot the power spectrum for each cluster
figure;
subplot(2, 1, 1);
plot(f, P1_cluster1);
title('Power Spectrum of Cluster 1 Activity');
xlabel('Frequency (Hz)');
ylabel('Power');
xlim([1 8]);  % Focus on frequencies up to 50 Hz

subplot(2, 1, 2);
plot(f, P1_cluster2);
title('Power Spectrum of Cluster 2 Activity');
xlabel('Frequency (Hz)');
ylabel('Power');
xlim([1 8]);  % Focus on frequencies up to 50 Hz
