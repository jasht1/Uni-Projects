
%% Physical Paramiters
m_b = 150;      % (kg)
m_w = 11;       % (kg)
b_s = 690;      % (N/m/s)
k_s = 6936;     % (N/m)
k_t = 28712;    % (N/m)

if ~exist('f_s', 'var') % make suspension passive if coeficients not defined
  f_s = 0;
end

%% State Space Representation
A = [
  0 1 0 0; % v_b
  -k_s/m_b -b_s/m_b k_s/m_b b_s/m_b; % a_b
  0 0 0 1; % v_w
  k_s/m_w b_s/m_w (-k_s-k_t)/m_w -b_s/m_w; % a_w
  ];

B = [
  0 0 0 k_t/m_w; % road displacment
  % 0 f_s/m_b 0 -f_s/m_w % actuator signal
  ]';

C = cat(1, [-k_s/m_b -b_s/m_b k_s/m_b b_s/m_b], eye(4));
% C = eye(4);
D = 0;

plant = ss(A,B,C,D);
