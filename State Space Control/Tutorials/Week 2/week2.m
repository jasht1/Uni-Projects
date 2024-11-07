close all;

A = [
    0 1 0;
    0 0 1;
    -9 -8 -7;
    ]

C = [
    2 3 4
    ]

B = [
    7;
    8;
    9;
    ]

D = 0;

F = ss(A,B,C,D)

% Question 5
figure;
t = 0:0.1:10;
step (F,t);
grid on;

% Question 6

% Question 7
sim ("week2.slx")

% Question 8
plot(out.ScopeData.time,out.ScopeData.signals.values)


