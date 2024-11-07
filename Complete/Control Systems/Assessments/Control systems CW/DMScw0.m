%% clear
clear
close all

%% defining variables
J = 1.16E-6; % Rotor moment of inertia
b = 3.3E-5; % Viscous friction constant
K = 0.0502; % Motor torque / back emf constant
R = 10.6;
L = 8.2E-5;
s = tf('s');

% Transfer functions
V_shaft = K/( (J*s+b)*(L*s+R)+K^2 );
P_shaft = K/(s*((J*s+b)*(L*s+R)+K^2));

%% Account for the load
M1 = 0.068;  % Inertial load disk mass (kg)
r1 = 0.0248; % Inertial load disk radius (m)

J1 = 0.5 * M1 * r1^2;  % Inertia of the load disk
J_total = J + J1;      % Total inertia

% Updated transfer functions
V_shaft = K/( (J_total*s+b)*(L*s+R)+K^2 );
P_shaft = K / (s * ((J_total * s + b) * (L * s + R) + K^2));

%% Simulink variables
[V_tf_n, V_tf_d] = tfdata(V_shaft, 'v');
[P_tf_n, P_tf_d] = tfdata(P_shaft, 'v');

%% Load lab data
Time = linspace(0.14,10.14,1000); %+0.13998 shift timeseries to fit labData
%timeMatrix = [linspace(0, (length(Time)-1)*0.01, length(Time))', double(Time)];
sim MotorSim1;
sim PIDmodel.slx;
load LabData.mat Motor Model;
position = cumtrapz(Time, Motor);

%% provided Lab data plot
figure(3);
    plot(Time, Motor, 'b-','DisplayName', 'Experimental');
    hold on
    plot(Time, Model, 'r-','DisplayName', 'Provided Modle');
    hold off
    title('Experimental Shaft velocity data');
    xlabel('Time (s)');
    ylabel('Veolcity (rad/s)');
    grid on;
    legend('Location', 'southeast');

%% Model plots
figure(2);
	% Input voltage
	subplot(3, 1, 1);
		plot(out.Voltage, 'r-');
		title('Input voltage');
		xlabel('Time (s)');
		ylabel('Voltage (V)');
		grid on;
	% Velocity
	subplot(3, 1, 2);
		plot(Time, Motor, 'b-','DisplayName', 'Experimental');
        hold on
        plot(out.V_shaft, 'r-','DisplayName', 'Theoretical Model');
        hold off
		title('Shaft velocity model vs lab data');
		xlabel('Time (s)');
		ylabel('Veolcity (rad/s)');
		grid on;
        legend('Location', 'southeast');
	% Position
	subplot(3, 1, 3);
		plot(Time, position, 'b-','DisplayName', 'Experimental Estimate');
        hold on
        plot(out.P_shaft, 'r-','DisplayName', 'Theoretical Model');
        hold off
		title('Shaft position model vs lab data');
        labels()
		% xlabel('Time (s)');
		% ylabel('Position (rad)');
		% grid on;
        % legend('Location', 'southeast');

%% Compare performance
V_shaftD = 17.491/(0.08*s+1);
figure(1);
    plot(out.Voltage1, 'g','DisplayName', 'Input signal (V)');
    hold on
    plot(out.V_TheoryModel, 'b-','DisplayName', 'Theory based model (rad/s)');
    hold on
    plot(out.V_DataModel, 'r--','DisplayName', 'Data driven model (rad/s)');
    hold off
    title('Theory vs Data Based Models');
    xlabel('Time (s)');
    ylabel('Veolcity (rad/s) / Voltage (V)');
    grid on;
    legend('Location', 'southeast');


%% load my lab data
load myLabData/'no weights.mat'
load myLabData/'no weights A0.mat'
load myLabData/'no weights A10.mat'
load myLabData/'no weights F4.mat'

load myLabData/'fixed_a1 weights.mat'
load myLabData/'fixed_b1 weight.mat'

load myLabData/'fixed_a2 weights.mat'
load myLabData/'fixed_b2 weights.mat'

load myLabData/'fixed_a2 weights A0.mat'
load myLabData/'fixed_a2 weights A10.mat'

%% My lab data plots
%% Varying amplitude
figure;
    subplot(2,2,1:2);
        plotme(no_weights_Value);
        title("Amplitude 1 (rad)");
    subplot(2,2,3);
        plotme(no_weights_A0_Value);
        title("Amplitude 0.1 (rad)");
    subplot(2,2,4);
        plotme(no_weights_A10_Value);
        title("Amplitude 10 (rad)");
    legend({'Rotor Position (rad)','Input Signal (rad)'},  'Location', 'northeastoutside');
%% Single weights
figure;
    plot(Last_10_wavesD(X_1b_weight_Value));
    hold on
    plotme(no_weights_Value);
    title("Effect of Single Weight");
    legend({'Rotor Position with brass weight (rad)','Rotor Position without brass weight (rad)','Input Signal (rad)'},  'Location', 'southeast');
%% double weights
figure;
    hold on
    plot(Last_10_wavesD(X_2b_weights_Value));
    plot(Last_10_waves(X_2a_weights_Value));
    title('Double weights response');
    labels();
    legend({'Rotor Position with 2 brass weights (rad)','Rotor Position with 2 aluminium weights (rad)','Input Signal (rad)'},  'Location', 'southeast');
%% frequency
figure;
    hold on
    plot(Last_n_waves(no_weights_F4_Value,40,199));
    title("4Hz Frequency Response");
    legend({'Rotor Position (rad)','Input Signal (rad)'},  'Location', 'northeast');
    labels();
%% Funks
function labels()
    xlabel('Time (s)');
    ylabel('Position (rad)');
	grid on;
    % legend('Location', 'southeast');
end

function Ltw = Last_10_waves(Value)
    full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
    Ltw = [Value(full_waves_index(end-11):full_waves_index(end-11)+999,:)]; %linspace(0, 10, 1000)',
end
function Ltw = Last_10_wavesD(Value)
    full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
    Ltw = [Value(full_waves_index(end-11):full_waves_index(end-11)+999,1)]; %linspace(0, 10, 1000)',
end

function Ltw = Last_n_waves(Value,n,t)
    full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
    Ltw = [Value(full_waves_index(end-n-1):full_waves_index(end-n-1)+t,:)]; %linspace(0, 10, 1000)',
end

function plotme(Value)
        plot(Last_10_waves(Value));
        labels();
end