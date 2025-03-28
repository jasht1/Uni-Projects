> [!Question]-
> ![3. Consider the rotation about x of P1 to P2](Questions.md#3.%20Consider%20the%20rotation%20about%20x%20of%20P1%20to%20P2)

%% Page Break %% <div style="page-break-after: always;"></div>

### 3a. General Transformation Matrix for Simple Rotation
%%[[2025-03-25]] @ 20:45%%

The [figure](image-4-x199-y336.png) shows a simple rotation.

![image-4-x198-y90|400](image-4-x198-y90.png)

The form of the Homogeneous Transformation Matrix (HTM) for a simple rotation about the axis depends on the axis about which the rotation takes place as seen in the [equation](#^1211fc) below for the typical counter clockwise forms.

$$
\begin{matrix}
\Large{\text{HTM for Simple Rotation of Angle $\theta$}} \\
\begin{matrix}
\text{about }x &
\text{about }y &
\text{about }z \\
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & \sin(\theta) & 0 \\
0 & -\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix} &
\begin{bmatrix}
\cos(\theta) & 0 & -\sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix} &
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix} \\ 
\end{matrix}
\end{matrix}
$$

^1211fc

As the case above is about the $x$ axis the transformation can be applied as follows:

$$
P_{2} = P_{1}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & \sin(\theta) & 0 \\
0 & -\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

^ea0369

Where $\theta$ is the angle of counter clockwise rotation about the $x$ axis and $P_{1}$ & $P_{2}$ are points represented by column vectors of homogeneous coordinates in the form as previously discussed.

%% Page Break %% <div style="page-break-after: always;"></div>

### 3a. Specific Case
%%[[2025-03-25]] @ 21:41%%

The case stated in the brief is ambiguous about whether the rotation is to be take about the origin $O$ or point $P1$ and as to the direction of the rotation, however it is taken to mean;

> *If $P_{1}$ is a point at $(1,1,1)$ and point $P_{2}$ is found $30 \degree$ counter clockwise about the origin $x$ axis from $P_{1}$ find the coordinates for $P_2$.*

The general form [described above](#^ea0369) the transformation matrix could be applied as follows to find $P_{2}$ as follows:

$$
P_{2} =
\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1\end{pmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(30) & \sin(30) & 0 \\
0 & -\sin(30) & \cos(30) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\approx
\begin{pmatrix} 1 \\ -0.83\\ 1.14 \\ 1\end{pmatrix}
$$

%% Page Break %% <div style="page-break-after: always;"></div>

### 3c. MATLAB Implementation
%%[[2025-03-25]] @ 15:03%%

This simple rotation can be used to arrange the joints of of a robot in MATLABs robotics toolbox as demonstrated by the code below.

```MATLAB title="Q2b_Simple_Rotation.m"
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
```

%% Page Break %% <div style="page-break-after: always;"></div>

###### Simple Rotation about x Figure
This script generates the following figure.

![SimpleXRotationRigidBodyFigure](SimpleXRotationRigidBodyFigure.svg)
