%% params
omega_b = 5;  % Cutoff frequency (rad/s)
omega_s = 10 * omega_b;  % Sampling frequency (rad/s)
Fs = omega_s / (2*pi);  % Sampling frequency (Hz)
T = 1/Fs;  % sampling period (s)

%% Define transfer function H(s)
num_s = [omega_b^2];
den_s = [1, sqrt(2)*omega_b, omega_b^2];

H_s = tf(num_s, den_s);  % Analogue transfer function in Laplace domain

%% Bilinear transform to get H(z)

%%% Auto find
[num_z, den_z] = bilinear(num_s, den_s, Fs)

%%% Manual~ish find
syms s z % symbolic for subs and simplifications
omega_b_pw = (2/T) * tan(omega_b * T / 2); % frequency pre warp
bilinear_identity = 2 / T * (1 - z^-1) / (1 + z^-1);
Hs = omega_b_pw^2 / (s^2 + sqrt(2)*omega_b_pw*s + omega_b_pw^2); % Analogue TF but symbolic
Hz = simplify(subs(Hs, s, bilinear_identity)); 
Hz = collect(Hz, z^-1);
[N_sym, D_sym] = numden(Hz); % symbolic to numeric
N_sym = expand(N_sym);
D_sym = expand(D_sym);
num_z_sym = sym2poly(N_sym);
den_z_sym = sym2poly(D_sym);
num_z_sym = num_z_sym / den_z_sym(1) % see if it reduces
den_z_sym = den_z_sym / den_z_sym(1)

%% Plot and compare

[H_s_mag, w] = bode(H_s, 2*pi*linspace(0, Fs/2, 1024));
H_s_mag = squeeze(H_s_mag);  % Remove singleton dim
f = linspace(0, Fs/2, numel(H_s_mag));
hold on;
freqz(num_z_sym, den_z_sym, 512, 1/T);
hold on;
freqz(num_z, den_z, 512, 1/T);
% legend('Analog H(s)', 'Symbolic Bilinear H(z)', 'MATLAB Bilinear H(z)');
% title('Frequency Response Comparison');

% values from my sketchy derivation
hold on;
num_z_hand_deriv = [1, 2, 1];
den_z_hand_deriv = [14.8065, -18.9021, 6.1138];
freqz(num_z_hand_deriv, den_z_hand_deriv, 512, 1/T);  % Normalized symbolic

legend('Analog H(s)', 'MATLAB Bilinear', 'Symbolic (full)', 'Manual derivation');
title('Frequency Response Comparison');
grid on;
