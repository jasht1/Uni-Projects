% Define the initial point P1
P1 = [1; 1; 1; 1]; % Homogeneous coordinates

% Define the transformation matrix for translation
T = [1 0 0 1;
  0 1 0 2;
  0 0 1 3;
  0 0 0 1];

% Apply the transformation to find P2
P2 = T * P1;

% Extract cartesian coordinates
P1_cartesian = P1(1:3);
P2_cartesian = P2(1:3);

% Plot
figure;
hold on;
grid on;
xlabel('X');
ylabel('Y');
zlabel('Z');
axis equal;

% Plot P1
plot3(P1_cartesian(1), P1_cartesian(2), P1_cartesian(3), 'ro', 'MarkerSize', 10, 'DisplayName', '$P_{1}$');

% Plot P2
plot3(P2_cartesian(1), P2_cartesian(2), P2_cartesian(3), 'bo', 'MarkerSize', 10, 'DisplayName', '$P_{2}$');

% Draw line between P1 and P2
plot3([P1_cartesian(1), P2_cartesian(1)], ...
  [P1_cartesian(2), P2_cartesian(2)], ...
  [P1_cartesian(3), P2_cartesian(3)], 'k--', 'DisplayName', '$l$');

set(groot,'defaultTextInterpreter','latex');
legend;
title('Simple Translation from $P_{1}$ to $P_{2}$');
view([1, 1, 1]);
hold off;
