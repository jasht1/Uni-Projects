
%% Physical Paramiters
m_b = 150;      % (kg)
m_w = 11;       % (kg)
b_s = 690;      % (N/m/s)
k_s = 6936;     % (N/m)
k_t = 28712;    % (N/m)

%% Initial Conditions

if ~exist('IC', 'var')
  IC = zeros(1, 4);
end

%% State Space Matricies
A = [
  0 1 0 0; % v_b
  -k_s/m_b -b_s/m_b k_s/m_b b_s/m_b; % a_b
  0 0 0 1; % v_w
  k_s/m_w b_s/m_w (-k_s-k_t)/m_w -b_s/m_w; % a_w
  ];

if exist('fs', 'var') % make suspension passive if coeficients not defined
  B = [
    0 0 0 k_t/m_w; % road displacment
    0 fs/m_b 0 -fs/m_w; % actuator signal
    ]';
else
  B = [
    0 0 0 k_t/m_w; % road displacment
    ]';
end

C = [
  1 0 0 0; % x_b
  0 1 0 0; % v_b
  -k_s/m_b -b_s/m_b k_s/m_b b_s/m_b; % a_b
  0 0 1 0; % x_w
  0 0 0 1; % v_w
  % k_s/m_w b_s/m_w (-k_s-k_t)/m_w -b_s/m_w; % a_w
  ];

D = zeros(height(C),width(B));

