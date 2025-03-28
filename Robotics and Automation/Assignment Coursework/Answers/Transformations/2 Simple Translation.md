> [!Question]-
> ![2. Consider the translation P1 to P2](Questions.md#2.%20Consider%20the%20translation%20P1%20to%20P2)

%% Page Break %% <div style="page-break-after: always;"></div>

### 2a. General Transformation Matrix for Simple Translation
%%[[2025-03-18]] @ 15:36%%

The [figure](image-4-x199-y336.png) shows a simple translation. 

![image-4-x199-y336|400](image-4-x199-y336.png)

This would be represented by the following Homogeneous Transformation Matrix (HTM):

$$\large \text{Simple Translation HTM:} \quad \begin{bmatrix}
1 & 0 & 0 & x_{1}-x_{2} \\ 
0 & 1 & 0 & y_{1}-y_{2} \\ 
0 & 0 & 1 & z_{1}-z_{2} \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}$$

That could be applied in the form:

$$P_{2} = P_{1} \begin{bmatrix}
1 & 0 & 0 & l_{x} \\ 
0 & 1 & 0 & l_{y} \\ 
0 & 0 & 1 & l_{z} \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}$$

Where $l (x,y,z)$ is the vector $\vec{l} = P_{2} - P_{1}$ and $P_{1}$ & $P_{2}$ are points represented by column vectors of homogeneous coordinates in the form:

$$\begin{pmatrix}
\newcommand{\G}[1]{{\color{green}#1}}
\newcommand{\S}{{\color{red}s}}
\begin{array}{c}
\G{x}/\S \\ 
\G{y}/\S \\ 
\G{z}/\S \\
\end{array}\\
\color{red}
\S \\
\end{pmatrix}
\quad 
\begin{align*}
& \text{where} 
{\color{green} \begin{pmatrix} x \\ y \\ z \end{pmatrix}}
\ \text{are cartesean coordinates denoting displacemnt from origin} \ O. \\
& \text{and} \ {\color{red} s }\ \text{is a scalar typically 1 or the lowest common denominator of ${\color{green} (x,y,z)}$.}
\end{align*}
$$

%% Page Break %% <div style="page-break-after: always;"></div>

### 2b. Specific Case 
%%[[2025-03-18]] @ 15:47%%

If the euclidean distance from points $P_{1}$ to $P_{2}$ is $l$ where:

$$l \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3\end{pmatrix} 
\quad \text{and} \quad 
P_{1} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1\end{pmatrix}
, \quad \text{then calculate} \quad 
P_{2}\begin{pmatrix} x \\ y \\ z \end{pmatrix}
.$$

--- start-multi-column: ID_zxbq
```column-settings
Number of Columns: 2
Largest Column: left
border:off
Shadow:off
```

Applying the general form described above in [2a](#2a.%20General%20Transformation%20Matrix%20for%20Simple%20Translation) the transformation matrix would be as shown in the [equation](#^78aa37) to the right.

--- column-break ---

$$\begin{bmatrix}
1 & 0 & 0 & 1 \\ 
0 & 1 & 0 & 2 \\ 
0 & 0 & 1 & 3 \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}$$

^78aa37

--- end-multi-column

And could be be applied as follows to find $P_{2}:$
$$P_{2} = 
\begin{pmatrix} 1 \\ 1 \\ 1 \\ 1\end{pmatrix}
\begin{bmatrix}
1 & 0 & 0 & 1 \\ 
0 & 1 & 0 & 2 \\ 
0 & 0 & 1 & 3 \\ 
0 & 0 & 0 & 1 \\ 
\end{bmatrix}
=
\begin{pmatrix} 2 \\ 3 \\ 4 \\ 1\end{pmatrix}
$$

%% Page Break %% <div style="page-break-after: always;"></div>

### 2c. MATLAB Implementation
%%[[2025-03-25]] @ 15:03%%

This simple translation can be used to arrange the joints of of a robot in MATLABs robotics toolbox as demonstrated by the code below.

```MATLAB title="Q2b_Simple_Translation.m"
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
```

%% Page Break %% <div style="page-break-after: always;"></div>

###### Simple Translation Figure
This script generates the following figure.

![SimpleTranslationRigidBodyFigure](SimpleTranslationRigidBodyFigure.svg)