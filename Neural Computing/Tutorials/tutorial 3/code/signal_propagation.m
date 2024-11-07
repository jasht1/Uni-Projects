% k Parameters
L = 3;                  % Length of the dendrite
Nx = 150;               % Number of spatial points
dx = L / (Nx - 1);      % Spatial step size
T = 1;                  % Total simulation time
dt = 0.00005;           % Time step size for stability
Nt = round(T / dt);     % Ensure Nt is an integer

% Cable equation parameters
lambda = 0.2;           % Increase length constant for more propagation
tau = 0.8;              % Time constant for slower temporal decay

% Initial condition: two voltage spikes with different amplitudes
V = zeros(Nx, 1);       % Voltage array
V(round(Nx/2)) = 2;     % First spike in the middle with amplitude 1
%V(round(Nx/3)) = 4;   % Second spike at one-third position with amplitude 0.9
%V(round(Nx/5)) = 8;   % Second spike at one-fifth position with amplitude 0.9

% Matrix to store the voltage over time
V_history = zeros(Nx, Nt);  % Matrix to store voltage propagation

% Simulation loop
for t = 1:Nt
  disp (t);
  V_new = V;  % To store the new values of V
  for x = 2:Nx-1
    % Update the voltage using the cable equation
    V_new(x) = V(x) + dt * (lambda^2 / dx^2) * (V(x+1) - 2*V(x) + V(x-1)) - dt/tau * V(x);
  end
  
  % Update V and store the result for this time step
  V = V_new;
  V_history(:, t) = V;
end

% Plot results with adjusted colormap
figure;
imagesc(0:dt:T, 0:dx:L, V_history);
xlabel('Time (t)');
ylabel('Position (x)');
title('Voltage propagation with two spikes');
colorbar;
clim([0 0.2]);  % Adjust the color limits to improve contrast

