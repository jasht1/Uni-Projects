
if exist('robotArm') == 0
  DefRobotArm;
end

% squat

randomPose = randomConfiguration(robotArm);

show (robotArm, randomPose);

function squat ()
global robotArm;

% Define home configuration
homeConfig = homeConfiguration(robotArm);

% Set joint angles (in radians)
homeConfig(1).JointPosition = deg2rad(-30);  % Base to Shoulder
homeConfig(2).JointPosition = deg2rad(100);  % Shoulder to Elbow
homeConfig(4).JointPosition = deg2rad(-70);  % Wrist1 to Wrist2
homeConfig(5).JointPosition = deg2rad(90);   % Wrist2 to Wrist3

% Apply home configuration
show(robotArm, homeConfig);
end
