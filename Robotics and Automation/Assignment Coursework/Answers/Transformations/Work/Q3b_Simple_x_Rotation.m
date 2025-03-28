% Define P1 & theta
P1 = [1, 1, 1];
theta_x = 30;
theta_y = 0;
theta_z = 0;

% Generate transformation matricies
T_P1 = trvec2tform(P1);
eul = deg2rad([theta_z,theta_y,theta_x]);
P2 = (eul2rotm(eul)*P1')';
T_P2 = se3(eul,"eul",P2);

% Create rigidBodyTree
TransformDiagram = rigidBodyTree;
TransformDiagram.BaseName = 'O';

% Add P1
P_1 = rigidBody('$P_{1}$');
D_P1 = rigidBodyJoint('$\vec{P_{1}}');
setFixedTransform(D_P1,T_P1);
P_1.Joint = D_P1;
addBody(TransformDiagram,P_1,'O')

% Add P2
P_2 = rigidBody('$P_{2}$');
D_P2 = rigidBodyJoint('$\vec{P_{2}}');
setFixedTransform(D_P2,T_P2);
P_2.Joint = D_P2;
addBody(TransformDiagram,P_2,'O')

% Visualize using rigidBody
show(TransformDiagram);
axis equal;

% lables
P2 = tform2trvec(P_2.Joint.JointToParentTransform);
text(P1(1), P1(2), P1(3), '$P_1$', 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
text(P2(1), P2(2), P2(3), '$P_2$', 'VerticalAlignment', 'top', 'HorizontalAlignment', 'left');
title('Simple Rotation about $x$');
set(groot,'defaultTextInterpreter','latex'); % nicer lables
fontsize(24,"points"); % bigger lables

view([2, 0.25, 0.5]); % side on view
