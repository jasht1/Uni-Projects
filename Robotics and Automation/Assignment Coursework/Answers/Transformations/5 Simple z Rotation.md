> [!Question]-
> ![5. Consider the rotation about z of P1 to P2](Questions.md#5.%20Consider%20the%20rotation%20about%20z%20of%20P1%20to%20P2)

%% Page Break %% <div style="page-break-after: always;"></div>

### 5a. Transformation Matrix for Simple Rotation about z
%%[[2025-03-25]] @ 20:45%%

The [figure below (left)](#^5e3465) shows a simple rotation about $z$. As the case above is about the $z$ axis the transformation can be applied as shown in the [equation below (right)](#^40803d). Where as before $\theta$ is the angle of CCW rotation and $P_{1}$ & $P_{2}$ are points represented by column vectors of homogeneous coordinates in the form.

--- start-multi-column: ID_sdhr
```column-settings
Number of Columns: 2
Largest Column: standard
Border:off
Shadow:off
```

![[image-5-x196-y392.png|250]] ^5e3465

--- column-break ---

$$\large
P_{2} = P_{1}
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

^40803d

--- end-multi-column

### 5b. Specific Case
%%[[2025-03-25]] @ 21:41%%

The case stated in the brief once again is ambiguous about whether the rotation is to be take about the origin $O$ or point $P1$ and as to the direction of the rotation, however it is taken to mean;

> *If $P_{1}$ is a point at $(1,1,1)$ and point $P_{2}$ is found $60 \degree$ counter clockwise about the origin $x$ axis from $P_{1}$, find the coordinates for $P_2$.*

Such a transformation can be applied with the HTM [equation](#^40803d) mentioned above with the $60 \degree$ angle substituted in for $\theta$ to find $P_{2}$ as shown below:

$$
P_{2} =
\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1\end{pmatrix}
\begin{bmatrix}
\cos(60) & -\sin(60) & 0 & 0 \\
\sin(60) & \cos(60) & 0 & 0 \\
1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\approx
\begin{pmatrix} -0.33 \\ 1 \\ 1.38 \\ 1\end{pmatrix}
$$

%% Page Break %% <div style="page-break-after: always;"></div>

### 5c. MATLAB Implementation
%%[[2025-03-25]] @ 15:03%%

This simple rotation can be used to arrange the joints of of a robot in MATLABs robotics toolbox as demonstrated by the code below.

```MATLAB title="Q5b_Simple_z_Rotation.m"
% Define P1 & theta
P1 = [1, 1, 1];
theta_x = 0;
theta_y = 0;
theta_z = 60;

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
view([2,0,8.5]); % side on view
axis tight;

% lables
P2 = tform2trvec(P_2.Joint.JointToParentTransform);
text(P1(1), P1(2), P1(3), '$P_1$', 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
text(P2(1), P2(2), P2(3), '$P_2$', 'VerticalAlignment', 'top', 'HorizontalAlignment', 'right');
title('$60^{\circ}$ CCW Rotation About $z$');
set(groot,'defaultTextInterpreter','latex'); % nicer lables
fontsize(24,"points"); % bigger lables

```


%% Page Break %% <div style="page-break-after: always;"></div>

###### Simple z rotation figure
This script generates the following figure.

![SimplezRotationRigidBodyFigure](SimplezRotationRigidBodyFigure.svg)
