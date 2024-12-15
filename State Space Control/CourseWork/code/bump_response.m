
QC_params

%% Simulation Paramaters

% time
t = 0.025; % Time incriment (s)
T_sim = 5; % Simulation length (s)

T = (0:t:T_sim-t); % Time array

% bump
bump_height = 0.05; % bump magnitude (m)
bump_len = 0.5; % duration of the disturbance (s)

bump = bump_height*sin(linspace(0,pi,bump_len/t)); % bump array (m)
road = cat(2,bump,zeros(1,(T_sim-bump_len)/t)); % road displacment array (m)

% actuator

if ~exist('u_f_s', 'var')
  u_f_s = zeros(1, T_sim/t); % make suspension passive if coeficients not defined
end

%% Simulation
U = cat(1,road,u_f_s);
y = lsim(plant,U,T);

%% Plot

figure
title("Response of Passive Suspension to {bump_height}m Disturbance")
plot(road, "DisplayName", "Road Disturbance");
hold on
plot(y(:,1), "DisplayName", "car body position");
plot(y(:,2), "DisplayName", "car body acceleration");
plot(y(:,3), "DisplayName", "car wheel position");
plot(y(:,4), "DisplayName", "car wheel acceleration");
hold off
legend
ylabel("Meters")
xlabel("Time (seconds)")
