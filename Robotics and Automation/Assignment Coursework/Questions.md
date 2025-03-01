## 1. Discussion Questions
> [!Note] Your answer to each question should be no more than 150 words in length. Remember to reference any sources you use appropriately. Please use IEEE style.
### 1a. What are the main types of robotic systems? What tasks can they perform?
[5 marks]
### 1b. What are the types of joints in a robot? What motions can they provide?
[5 marks]
### 1c. What are the differences between forward kinematics and inverse kinematics?
[5 marks]
### 1d. What are the common sensors in a typical robotic system?
[5 marks]

## 2. Consider the translation P1 to P2
[15 marks] 

![image-4-x199-y336|400](image-4-x199-y336.png)

### 2a. Determine the homogeneous transformation matrix
Determine the homogeneous transformation matrix ($4 \times 4$) to translate $P1$ to $P2$ as shown in figure (along $x, y, z$ axes for distance $l (x,y,z)$). 
[5 marks]
### 2b. Find case

$$\text{If} \quad l \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3\end{pmatrix} \quad \text{and} \quad P1 \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1\end{pmatrix}, \quad \text{then calculate} \quad P2\begin{pmatrix} x \\ y \\ z \end{pmatrix}.$$

[5 marks]
### 2c. Do the calculations in MATLAB 
Do the calculations in MATLAB and use rigiBody to visualise (both P1 and P2). Show your code (copy and paste here) and result (save as figure the insert here, not screen capture).
[5 marks]

## 3. Consider the rotation about x of P1 to P2
[15 marks] 

![image-4-x198-y90|400](image-4-x198-y90.png)
### 3a. Determine the homogeneous transformation matrix (4 × 4) to rotate P1 to P2 around axis x for angle θ as shown in below figure.
### 3b. if θ = 30° and x1 = 1, y1 = 1, z1 = 1, calculate x2, y2, z2.
### 3c. Do the calculations in MATLAB and use rigiBody to visualise (both P1 and P2). Show your code (copy and paste here) and result (save as figure the insert here, not screen capture).

## 4. Consider the rotation about y of P1 to P2
[15 marks] 

![image-5-x182-y621|400](image-5-x182-y621.png)
### 4a. Determine the homogeneous transformation matrix (4 × 4) to rotate P1 to P2 around axis y for angle θ as shown in below figure. 
### 4b. if θ = 45° and x1 = 1, y1 = 1, z1 = 1, calculate x2, y2, z2. 
### 4c. Do the calculations in MATLAB and use rigiBody to visualise (both P1 and P2). Show your code (copy and paste here) and result (save as figure the insert here, not screen capture).
## 5. Consider the rotation about z of P1 to P2
[15 marks] 
![image-5-x196-y392|400](image-5-x196-y392.png)
### 5a. Determine the homogeneous transformation matrix (4 × 4) to rotate P1 to P2 around axis z for angle θ as shown in below figure. 
### 5b. if θ = 60° and x1 = 1, y1 = 1, z1 = 1, calculate x2, y2, z2. 
### 5c. Do the calculations in MATLAB and use rigiBody to visualise (both P1 and P2). Show your code (copy and paste here) and result (save as figure the insert here, not screen capture).

## 6. 
In some cases, the kinematic model of a robot might not be available, and you would need to derive this yourself. The figure below shows the dimensions for a six-degrees-of-freedom robotic manipulator to be modelled.
![image-6-x101-y549|400](image-6-x101-y549.png)
### 6a. Assign appropriate frames to the given robot (on the given figure or your own sketch).
[5 marks]

> [!Note] It is sufficient to show only 2 axes for each frame since the third axis can be deduced. Briefly comment on how you assigned the frames.
### 6b. Now that you have assigned appropriate frames, model this robot in MATLAB, show your code (copy and paste here) and result (save as figure the insert here, not screen capture).
[10 marks]
### 6c. Assign a random configuration (angles) to this robot, using MATLAB, show your code (copy and paste here) and result (save as figure the insert here, not screen capture).
[5 marks]
 
> [!Note] You can use other programming language such as Python/C/C++.
