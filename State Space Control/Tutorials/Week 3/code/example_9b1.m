% example 9b 1 - motor position control
% data from https://ctms.engin.umich.edu/CTMS/index.php?example=MotorPosition&section=SystemModeling

%% data and ABCD matrices
clear
close all

J = 3.2284E-6;
b = 3.5077E-6;
K = 0.0274;
R = 4;
L = 2.75E-6;

A=[ 0   1   0
    0 -b/J  K/J
    0 -K/L  -R/L];
B=[0 0 1/L]';
C=[1 0 0];
D=0;

sys1=ss(A,B,C,D)
%check controllability, and observability
Cm = ctrb(A,B); test1=det(Cm)
Om = obsv(A,C); test2=det(Om)

%check open-loop poles
e=eig(A)

%transfer function coefficients
[num,den]=ss2tf(A,B,C,D)

%% initial test (step response)
close all
[y,t]=step(sys1,5);
plot(t,y), grid
xlabel('time (s)'),ylabel('rotor angle (rad)')
%% to test the model use motor speed as output
close all
sys2=ss(A,B,[0 1 0],0)
[y,t]=step(sys2,0.1);
plot(t,y), grid
xlabel('time (s)'),ylabel('angular velocity (rad/s)')

