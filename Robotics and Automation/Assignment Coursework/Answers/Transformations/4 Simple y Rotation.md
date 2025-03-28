> [!Question]-
> ![4. Consider the rotation about y of P1 to P2](Questions.md#4.%20Consider%20the%20rotation%20about%20y%20of%20P1%20to%20P2)

%% Page Break %% <div style="page-break-after: always;"></div>

### 4a. Transformation Matrix for Simple Rotation about y
%%[[2025-03-25]] @ 20:45%%

The [figure below (left)](#^5e9792) shows a simple rotation about y. As the case above is about the $y$ axis the transformation can be applied as shown in the [equation below (right)](#^ea0369). Where as before $\theta$ is the angle of rotation and $P_{1}$ & $P_{2}$ are points represented by column vectors of homogeneous coordinates in the form.

--- start-multi-column: ID_ao6r
```column-settings
Number of Columns: 2
Largest Column: standard
Border:off
Shadow:off
```

![[image-5-x182-y621.png|250]] ^5e9792

--- column-break ---

$$\large
P_{2} = P_{1}
\begin{bmatrix}
\cos(\theta) & 0 & -\sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

^ea0369

--- end-multi-column

### 4b. Specific Case
%%[[2025-03-25]] @ 21:41%%

The case stated in the brief once again is ambiguous about whether the rotation is to be take about the origin $O$ or point $P1$ and as to the direction of the rotation, however for the sake of variety it is taken to mean;

> *If $P_{1}$ is a point at $(1,1,1)$ and point $P_{2}$ is found $45 \degree$ **clockwise** about the origin $y$ axis from $P_{1}$ find the coordinates for $P_2$.*

The general form [described above](#^ea0369) for counter clockwise (CCW) rotations can be adapted to the clockwise (CW) form simply by swapping the signs of the $\sin$ terms. 

$$\begin{matrix}
\Large{\text{HTM for Simple Rotation of Angle $\theta$ about }y} \\
\begin{matrix}
\text{Counter Clockwise} &
\text{Clowckwise} \\ 
\begin{bmatrix}
\cos(\theta) & 0 & \color{red}-\sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
\color{green}\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix} &
\begin{bmatrix}
\cos(\theta) & 0 & \color{green}\sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
\color{red}-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix} \\ 
\end{matrix}
\end{matrix}$$

Thus the transformation matrix could be applied to find $P_{2}$ as follows:

$$
P_{2} =
\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1\end{pmatrix}
\begin{bmatrix}
\cos(45) & 0 & \sin(45) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(45) & 0 & \cos(45) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
=
\begin{pmatrix} \sqrt2 \\ 1 \\ 0 \\ 1\end{pmatrix}
\approx
\begin{pmatrix} 1.41 \\ 1 \\ 0 \\ 1\end{pmatrix}
$$

%% Page Break %% <div style="page-break-after: always;"></div>

### 4c. MATLAB Implementation
%%[[2025-03-25]] @ 15:03%%

This simple rotation can be used to arrange the joints of of a robot in MATLABs robotics toolbox as demonstrated by the code below.

```MATLAB title="Q3b_Simple_y_Rotation.m"
% Define P1 & theta
P1 = [1, 1, 1];
theta_x = 0;
theta_y = 45;
theta_z = 0;

% Generate transformation matricies
T_P1 = trvec2tform(P1);
eul = deg2rad([theta_z,theta_y,theta_x]*-1);
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
view([0.25, 2, 0.5]); % side on view
axis equal;

% lables
P2 = tform2trvec(P_2.Joint.JointToParentTransform);
text(P1(1), P1(2), P1(3), '$P_1$', 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
text(P2(1), P2(2), P2(3), '$P_2$', 'VerticalAlignment', 'top', 'HorizontalAlignment', 'right');
title('$45^{\circ}$ CW Rotation About $y$');
set(groot,'defaultTextInterpreter','latex'); % nicer lables
fontsize(24,"points"); % bigger lables
```

%% Page Break %% <div style="page-break-after: always;"></div>

###### Simple Clockwise rotation about y figure
This script generates the following figure.

![CWYRotationRigidBodyFigure](CWYRotationRigidBodyFigure.svg)
