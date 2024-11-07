% matlab for slides 8a - state observers
% examples and tutorial problems

%% example 1
clear
close all
A=[ 0 1 0
    1 0 1
    -20 -30 -10];
B=[0 0 1]';
C=[1 0 0];
D=0;
%check controllability, and observability
Cm = ctrb(A,B); test1=det(Cm)
Om = obsv(A,C); test2=det(Om)

%check open-loop poles
e=eig(A)

%set observer poles based on faster (complex) poles
p1=e(2)*2;p2=conj(p1);p3=1.5*real(p1);
P=[p1,p2,p3];

Ke=place(A',C',P);
Ke=Ke'; %gives the correct shape (column vector)
%closed-loop A-matrix for the observer
Ao=A-Ke*C;
%check the eigenvalues
ee=eig(Ao);

%after running the above we can test the model in simulink ...

%% tutorial 1
clear,close all
A=[ 0 1
    -3.42 -3.96];
B=[0 1]';
C=[372.81  407];
D=0;

%check controllability, and observability
Cm = ctrb(A,B); test1=det(Cm)
Om = obsv(A,C); test2=det(Om)

%poles
zeta=0.7;wn=100; 
sigma=zeta*wn;wd=wn*sqrt(1-zeta^2);
p1=-sigma+1j*wd;
p2=-sigma-1j*wd;

phi=A^2+140*A+10000*eye(2);
Ke=phi*inv(Om)*[0 1]'

%check via place
K=place(A',C',[p1,p2])
KKe=K';

%% tutorial q2 (with checks)
clear, close all
s=tf('s')
G=(s^2+s+1)/(s+2)/(s+3)/(s+4)
num=[1 1 1]
den=[1 9 26 24]

%comment out as desired
% A=[0 1 0;0 0 1;-24 -26 -9];B=[0 0 1]';C=[1 1 1];D=0;%CCF
A=[0 1 0;0 0 1;-24 -26 -9]';C=[0 0 1];B=[1 1 1]';D=0;%OCF
[num2,den2]=ss2tf(A,B,C,D)


%% tutorial q3 (mainly checking)
clear, close all

A=[0 1 0;0 0 1;-24 -26 -9]';C=[0 0 1];B=[1 1 1]';D=0;
s=tf('s')
phi=(s+6)*(s+8)^2 %check expansion

Ke=[360 134 13]';
Ae=A-Ke*C
eig(Ae)

%% tutorial q5 (check hand calc)
clear, close all
A=[0 10;1 0];B=[1 1]';C=[0 1]; D=0;
Ke=[160 25]';
eig(A-Ke*C)




