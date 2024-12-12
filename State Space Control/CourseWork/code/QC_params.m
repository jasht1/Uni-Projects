
%% Physical Paramiters
m_b = 150;      % $\text{kg}$
m_w = 11;       % $\text{kg}$
b_s = 690;      % $\text{N} \! \cdot \! \text{m}^{-1} \! \cdot \! \text{s}$
k_s = 6936;     % $\text{N} \! \cdot \! \text{m}^{-1}$
k_t = 28712;    % $\text{N} \! \cdot \! \text{m}^{-1}$

if ~exist('k_f_s', 'var')
  k_f_s = zeros(1, 4); % make suspension passive if coeficients not defined
end

%% State Space Representation
A = [
  0 1 0 0;
  -k_s/m_b -b_s/m_b k_s/m_b b_s/m_b;
  0 0 0 1;
  k_s/m_w b_s/m_w (k_t-k_s)/m_w -b_s/m_w;
  ];

B = [0 0 0 k_t/m_w;k_f_s]';

C = [0 -1 0 0];
D = 0;

plant = ss(A,B,C,D);
