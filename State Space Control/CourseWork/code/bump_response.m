
%% Physical Paramiters
m_b = 150;      % (kg)
m_w = 11;       % (kg)
b_s = 690;      % (N/m/s)
k_s = 6936;     % (N/m)
k_t = 28712;    % (N/m)

if ~exist('f_s', 'var') % make suspension passive if coeficients not defined
  f_s = 0;
end

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

%% State Space Representation
A = [
  0 1 0 0;
  -k_s/m_b -b_s/m_b k_s/m_b b_s/m_b;
  0 0 0 1;
  k_s/m_w b_s/m_w (k_t-k_s)/m_w -b_s/m_w;
  ];

B = [
  0 0;
  0 f_s/m_b;
  0 0;
  k_t/m_w -f_s/m_w
  ];

C = eye(4);
D = 0;

plant = ss(A,B,C,D);

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
