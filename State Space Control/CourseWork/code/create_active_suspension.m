
%% Setup Controller
fs = 1;

kp = tunableGain('kp_fs', 1);
kd = tunableGain('kd_fs', 1);

s = tf('s');
controller = kp + kd * s;

%% Setup New passive_suspension
run QC_params;

passive_suspension = ss(A, B, C, D);

active_suspension = feedback(passive_suspension, controller, 1,1);

active_suspension.InputName = {'r'};
active_suspension.OutputName = {'x_b','v_b','a_b','x_w','v_w'};
