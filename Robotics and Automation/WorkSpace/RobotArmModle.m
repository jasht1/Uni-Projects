
robot = rigidBodyTree('DataFormat', 'column', 'MaxNumBodies', 6);

% Base to Joint 1
body1 = rigidBody('body1');
joint1 = rigidBodyJoint('joint1', 'revolute');
setFixedTransform(joint1, trvec2tform([0, 0, 0]));
joint1.JointAxis = [0 0 1]; % Rotation about Z0
body1.Joint = joint1;
addBody(robot, body1, 'base');

% Joint 1 to Joint 2
body2 = rigidBody('body2');
joint2 = rigidBodyJoint('joint2', 'revolute');
setFixedTransform(joint2, trvec2tform([0.305, 0, 0.740]));
joint2.JointAxis = [0 1 0]; % Rotation about Y-axis
body2.Joint = joint2;
addBody(robot, body2, 'body1');

% Joint 2 to Joint 3
body3 = rigidBody('body3');
joint3 = rigidBodyJoint('joint3', 'revolute');
setFixedTransform(joint3, trvec2tform([0, 0, 1.075]));
joint3.JointAxis = [0 0 1]; % Rotation about Z-axis
body3.Joint = joint3;
addBody(robot, body3, 'body2');

% Joint 3 to Joint 4
body4 = rigidBody('body4');
joint4 = rigidBodyJoint('joint4', 'revolute');
setFixedTransform(joint4, trvec2tform([0.305, 0, 0.250]));
joint4.JointAxis = [0 1 0]; % Rotation about Y-axis
body4.Joint = joint4;
addBody(robot, body4, 'body3');

% Joint 4 to Joint 5 (Wrist)
body5 = rigidBody('body5');
joint5 = rigidBodyJoint('joint5', 'revolute');
setFixedTransform(joint5, trvec2tform([1.275, 0, 0]));
joint5.JointAxis = [1 0 0]; % Rotation about X-axis
body5.Joint = joint5;
addBody(robot, body5, 'body4');

% Joint 5 to Joint 6 (End-effector)
body6 = rigidBody('body6');
joint6 = rigidBodyJoint('joint6', 'revolute');
setFixedTransform(joint6, trvec2tform([0.240, 0, 0]));
joint6.JointAxis = [0 1 0]; % Rotation about Y-axis
body6.Joint = joint6;
addBody(robot, body6, 'body5');

% End-effector
ee = rigidBody('end_effector');
setFixedTransform(ee.Joint, trvec2tform([0.100, 0, 0]));
addBody(robot, ee, 'body6');

% Show the robot
show(robot);
axis("tight")
