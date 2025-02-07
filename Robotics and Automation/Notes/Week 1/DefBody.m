body1 = rigidBody('body1');
jnt1 = rigidBodyJoint('jnt1','revolute');
body1.Joint = jnt1;
robot = rigidBodyTree;
addBody(robot,body1,'base')
showdetails(robot)
show(robot)
axis tight
