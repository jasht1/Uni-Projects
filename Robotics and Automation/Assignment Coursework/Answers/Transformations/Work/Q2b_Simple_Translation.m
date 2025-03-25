% Define P1 & l
P1 = [1, 1, 1];
l = [1,2,3];

% Generate transformation matricies
T_P1 = trvec2tform(P1);
T_l = trvec2tform(l);

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
setFixedTransform(D_P2,T_l);
P_2.Joint = D_P2;
addBody(TransformDiagram,P_2,'$P_{1}$')

% Visualize using rigidBody
show(TransformDiagram);
axis equal;

% lables
P2=P1+l;
text(P1(1), P1(2), P1(3), '$P_1$', 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
text(P2(1), P2(2), P2(3), '$P_2$', 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
set(groot,'defaultTextInterpreter','latex'); % nicer lables
fontsize(24,"points"); % bigger lables

title('Simple Translation from $P_{1}$ to $P_{2}$');
view([2, 0.25, 0.5]); % side on view
