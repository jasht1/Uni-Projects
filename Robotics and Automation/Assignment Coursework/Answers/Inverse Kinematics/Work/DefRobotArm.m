robotArm = rigidBodyTree;

% Actual Base to Base Joint
base = rigidBody('Base');
joint_base = rigidBodyJoint('joint_base', 'revolute');
setFixedTransform(joint_base, trvec2tform([0, 0, 0]));
joint_base.JointAxis = [0 0 1]; % Rotation about Z0
base.Joint = joint_base;
addBody(robotArm, base, robotArm.BaseName);

% Base to Shoulder
shoulder = rigidBody('Shoulder');
joint_shoulder = rigidBodyJoint('joint_shoulder', 'revolute');
setFixedTransform(joint_shoulder, trvec2tform([54.65, 0, 89.2]));
joint_shoulder.JointAxis = [0 1 0]; % Rotation about Y-axis
shoulder.Joint = joint_shoulder;
addBody(robotArm, shoulder, 'Base');

% Shoulder to Elbow
elbow = rigidBody('Elbow');
joint_elbow = rigidBodyJoint('joint_elbow', 'revolute');
setFixedTransform(joint_elbow, trvec2tform([0, 0, 425]));
joint_elbow.JointAxis = [0 1 0]; % Rotation about Y-axis
elbow.Joint = joint_elbow;
addBody(robotArm, elbow, 'Shoulder');

% Elbow to Wrist1
wrist1 = rigidBody('Wrist1');
joint_wrist1 = rigidBodyJoint('joint_wrist1', 'revolute');
setFixedTransform(joint_wrist1, trvec2tform([0, 0, 392]));
joint_wrist1.JointAxis = [0 1 0]; % Rotation about Y-axis
wrist1.Joint = joint_wrist1;
addBody(robotArm, wrist1, 'Elbow');

% Wrist1 to Wrist2
wrist2 = rigidBody('Wrist2');
joint_wrist2 = rigidBodyJoint('joint_wrist2', 'revolute');
setFixedTransform(joint_wrist2, trvec2tform([54.65, 0, 47.375]));
joint_wrist2.JointAxis = [0 0 1]; % Rotation about Z-axis
wrist2.Joint = joint_wrist2;
addBody(robotArm, wrist2, 'Wrist1');

% Wrist2 to Wrist3
wrist3 = rigidBody('Wrist3');
joint_wrist3 = rigidBodyJoint('joint_wrist3', 'revolute');
setFixedTransform(joint_wrist3, trvec2tform([41.25, 0, 47.375]));
joint_wrist3.JointAxis = [0 1 0]; % Rotation about Y-axis
wrist3.Joint = joint_wrist3;
addBody(robotArm, wrist3, 'Wrist2');

% Wrist3 to End-effector
end_effector = rigidBody('EndEffector');
joint_ee = rigidBodyJoint('joint_ee', 'fixed');
setFixedTransform(joint_ee, trvec2tform([41.25, 0, 0]));
end_effector.Joint = joint_ee;
addBody(robotArm, end_effector, 'Wrist3');
