ik = inverseKinematics('RigidBodyTree', robot);
qSol = ik(endEffector, poseTF, weights, qInitial);

weights = [0 0 0 1 1 1];
intitialguess = homeConfiguration(robot);

