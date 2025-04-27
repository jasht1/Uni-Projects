
### Analogue Filter Response

The analogue Butterworth filter is simulated with MATLABs built in `impulse` function and it's frequency response is projected in terms of magnitude and phase using the `bode` function. This script can be downloaded along with the rest of the code used in this report from the github repo at [git@github.com:jasht1/Uni-Projects/Signal Processing/Assesments/CourseWork/](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%201/Q1iiAnalogueResponse.m)

```MATLAB
%% Params
omega_b = 5;  % Cutoff frequency (rad/s)

%% Define transfer function H(s)
num_s = [omega_b^2];
den_s = [1, sqrt(2)*omega_b, omega_b^2];

H_s = tf(num_s, den_s);  % Analogue transfer function in Laplace domain

%% Plot results
figure('NumberTitle', 'off');
tiledlayout(1, 2);  % 1 row, 2 columns
sgtitle('Analogue Butterworth Low Pass Filter Response');

%%% Impulse response
%nexttile;
impulse(H_s);
title('Impulse Response');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

%%% Frequency response
%nexttile;
bode(H_s);
title('Frequency Response');
grid on;
```

###### Figure 5: Analogue Butterworth filter Impulse & Frequency Response

![](Analog_BWLPF_Response.svg)

### Digital Filter Response

The `bilinear` function is used to convert a the symbolic $s$-domain transfer function object into it's $z$-domain form. The `impz` function is used to simulate an impulse response and it's frequency response is projected in terms of magnitude and phase using the `freqz` function. [Download this script from the git repo](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%201/Q1ivDigitalResponse.m).

```MATLAB
%% params
omega_b = 5;  % Cutoff frequency (rad/s)
omega_s = 10 * omega_b;  % Sampling frequency (rad/s)
Fs = omega_s / (2*pi);  % Sampling frequency (Hz)

%% Define transfer function H(s)
num_s = omega_b^2;
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

%%% Frequency response
%nexttile;
figure()
freqz(num_z, den_z, 1024, Fs);
title('Frequency Response');
```

###### Figure 6: Digital Butterworth filter Impulse & Frequency Response

![](Digital_BWLPF_Response.svg)

### Analogue vs Digital Frequency Response 

Note that the previous two figures despite being laid out in a similar format are not directly comparable given the default $x$ units of `bode` are $\text{rad}/\text{s}$ compared with `freqz` in $\text{Hz}$. Similarly while samples and seconds are analogous between analogue and digital systems it is important to avoid their conflation. The below script, [available here](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%201/Q1ivAnalogueVsDigitalResponse.m), plots the projected frequency response of the analogue and digital models onto the same axis. This shows an almost perfect match with the minor difference in the "symbolic" method likely due to truncation in the `sym2poly` method when the higher resolution symbolic variables are converted into vector floats.

```MATLAB
%% params
omega_b = 5;  % Cutoff frequency (rad/s)
omega_s = 10 * omega_b;  % Sampling frequency (rad/s)
Fs = omega_s / (2*pi);  % Sampling frequency (Hz)
T = 1/Fs;  % sampling period (s)

%% Define transfer function H(s)
num_s = omega_b^2;
den_s = [1, sqrt(2)*omega_b, omega_b^2];

H_s = tf(num_s, den_s);  % Analogue transfer function in Laplace domain

%% Bilinear transform to get H(z)

%%% Auto find
[num_z, den_z] = bilinear(num_s, den_s, Fs);

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
num_z_sym = num_z_sym / den_z_sym(1); % see if it reduces
den_z_sym = den_z_sym / den_z_sym(1);

%% values from my hand derivation
num_z_hand_deriv = [0.0675, 0.1350, 0.0675]; % Y(z)
den_z_hand_deriv = [1, -1.2765, 0.4129]; % X(z)

%% Plot and compare

[H_s_mag, w] = bode(H_s, 2*pi*linspace(0, Fs/2, 1024));
H_s_mag = squeeze(H_s_mag);  % Remove singleton dim
f = linspace(0, Fs/2, numel(H_s_mag));
hold on;
freqz(num_z_sym, den_z_sym, 512, 1/T);
freqz(num_z, den_z, 512, 1/T);
freqz(num_z_hand_deriv, den_z_hand_deriv, 512, 1/T);  % Normalized symbolic

legend('Analog H(s)', 'MATLAB Bilinear', 'Symbolic (full)', 'Manual derivation');
title('Frequency Response Comparison');
grid on;
```

###### Figure 7: Analogue vs Digital Frequency Response

![](Analog_vs_Digital_FreqResp.svg)