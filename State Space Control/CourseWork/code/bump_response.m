
%% Simulation Paramaters

% time
t = 0.025; % Time incriment (s)
T_sim = 3; % Simulation length (s)

T = (0:t:T_sim-t); % Time array

% bump
bump_height = 0.05; % bump magnitude (m)
bump_len = 0.5; % duration of the disturbance (s)

bump = bump_height*sin(linspace(0,pi,bump_len/t)); % bump array (m)

if exist('bump', 'var')
  road = cat(2,bump,zeros(1,(T_sim-bump_len)/t)); % road displacment array (m)
else
  bump_height = 0
  road = zeros(1,length(T));
end

% actuator

if ~exist('u_fs', 'var')
  u_fs = zeros(1, T_sim/t); % make suspension passive if coeficients not defined
end

%% Simulation

type = "Passive";
QC_params
plant = ss(A,B,C,D);

% type = "Active";
% tune_active_suspension
% plant = tuned_suspension;

U = [road; u_fs];
y = lsim(plant,U,T);

%% Plot

plot_series = {
  struct('data', road,      'label', 'Road Disturbance (m)'),
  struct('data', y(:,4),    'label', 'Wheel Displacement (m)'),
  struct('data', y(:,5),    'label', 'Wheel Velocity (m/s)'),
  struct('data', y(:,1),    'label', 'Body Displacement (m)'),
  struct('data', y(:,2),    'label', 'Body Velocity (m/s)'),
  struct('data', y(:,3),    'label', 'Body Acceleration (m/s^2)'),
  % struct('data', y(:,6),    'label', 'Wheel Acceleration (m/s^2)'),
  };

%%% all on the same chart
% figure
% hold on
% title("Response of " +type+ " Suspension to " + bump_height + "m Disturbance")
% for i = 1:length(plot_series)
%   plot(T, plot_series{i}.data, 'DisplayName', plot_series{i}.label);
%   ylabel(plot_series{i}.label);
%   xlabel('Time (seconds)');
%   legend;
%   grid on;
% end
% ylabel("Meters")
% xlabel("Time (seconds)")
% hold off

%%% subplots for each
figure

sgtitle("Response of " +type+ " Suspension to " + bump_height + "m Disturbance");

tiledlayout(length(plot_series),1,"TileSpacing","compact", 'Padding', 'compact');
for i = 1:length(plot_series)
  nexttile
  plot(T, plot_series{i}.data);
  ylabel(plot_series{i}.label);
  grid on;
end
xlabel('Time (seconds)');

%%% new figure for each
% for i = 1:length(plot_series)
%   figure
%   title("Response of " +type+ " Suspension to " + bump_height + "m Disturbance")
%   plot(T, plot_series{i}.data);
%   ylabel(plot_series{i}.label);
%   xlabel('Time (seconds)');
%   grid on;
% end

