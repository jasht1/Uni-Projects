% illustrate pole placement technique in Matlab
clear all
close all
clc
% system modelling
A=[0 2;0 3];
B=[0;1];

% check controllability 
rank_ctrb=rank(ctrb(A,B))
CM=[B A*B];
check_ctrb=det(CM)
% desired poles
desired_poles=[-300 -400];

% design controller

K=place(A,B,desired_poles)
K=acker(A,B,desired_poles)
phi_A=A^2 + 7*A + 12*eye(2);
K_ackerman=[0 1]*inv(CM)*phi_A
% check the closed loop system poles are in desirable locations
Acl=A-B*K;
eig(Acl)

%%
desired_poles=[-3 -4];
des_charac=poly(desired_poles)
phi_A_new=des_charac(1)*A^2+des_charac(2)*A+ des_charac(3)*eye(2);
