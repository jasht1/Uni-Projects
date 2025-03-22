
% Range

wind_min = 1; %min wind speed in m/s
wind_max = 30; %max wind speed in m/s

wind_speed = wind_min:1:wind_max;

% Parameters
rho = 1.2; % air density in kg/m^3
R = 48; % rotor radius in meters
A_T = pi * R^2; % swept area in square meters
P_rated = 5e6; % rated power in watts (5 MW)
u_rated = 13; % rated wind speed in m/s
u_cutout = 25; % cut-out wind speed in m/s
eta = 0.59; % assuming turbine efficiency of betz lim

% Functions
rayleigh_pdf = @(u, ubar) (pi/2) * (u / ubar^2) .* exp(-pi * (u / ubar).^2 / 4);

nominal_P = @(u, ubar) (0.59 * 0.5 * rho * A_T * u.^3) .* rayleigh_pdf(u, ubar); % Power for u < u_rated
high_wind_P = @(u, ubar) P_rated * rayleigh_pdf(u, ubar); % Power for u_rated < u < u_cutout

% output array
income = zeros(size(wind_speed));

% main loop
for i = 1:length(wind_speed) % average wind speed (mean for the Rayleigh distribution)
  ubar = wind_speed(i);
  
  Nominal_E = integral(@(u) nominal_P(u, ubar), 0, u_rated); % Energy for u_cutin < u < u_rated in J
  high_wind_E = integral(@(u) high_wind_P(u, ubar), u_rated, u_cutout); % Energy for u_rated < u < u_cutout in J
  
  E = (Nominal_E + high_wind_E) / (60^2 * 1000); % total Energy in kWh
  
  annual_income(i) = E * 0.10 * 24*365; % income in £
  
end

% output
result_table = table(wind_speed', annual_income', 'VariableNames', {'AverageWindSpeed_m_s', 'Income_£'});
disp(result_table);
