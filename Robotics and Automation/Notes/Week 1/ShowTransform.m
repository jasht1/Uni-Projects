
body1 = rigidBody('body1');
jnt1 = rigidBodyJoint('jnt1','revolute');
body1.Joint = jnt1;
robot = rigidBodyTree;
addBody(robot,body1,'base')
% showdetails(robot)

figure;
hold on;
ax = show(robot);
view(3);
axis equal;
grid on;



%% v1
Tlen = 100

T = 1:Tlen;

for t = T
  tform = trvec2tform((t/tlen)*[0, 0, 2]);
  setFixedTransform(jnt1,tform);
  pause(0.01)
  show(robot);
  axis tight
end


% t= 0.5
% tform = trvec2tform(t*[0, 0, 2])
% setFixedTransform(jnt1,tform)


% tformHandle = hgtransform('Parent', ax);

T = linspace(0, 20, 200); % Smooth transition over 200 frames

% for t = T
%
%   jnt1.setFixedTransform = t; % Update joint angle
%   show(robot, 'Parent', ax, 'FastUpdate', true, 'PreservePlot', true);
%
%   % tform = makehgtform('translate', [0, 0, 0.2] * t); % Create transformation matrix
%   tformHandle.Matrix = tform; % Apply transformation
%   drawnow; % Update figure without flickering
%   pause(0.05);
% end

