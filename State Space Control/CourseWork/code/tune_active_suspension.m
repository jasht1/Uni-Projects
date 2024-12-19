
create_active_suspension

%% Set Goals
settling_time_goal = TuningGoal.StepTracking('r', 'x_b', 1.5);
overshoot_goal = TuningGoal.Overshoot('r', 'x_b', 10);

%% Tune

goals = [settling_time_goal, overshoot_goal];
[tuned_suspension, performance] = systune(active_suspension, goals);

%% Results

kp_fs = getBlockValue(tuned_suspension,'kp_fs')
kd_fs = getBlockValue(tuned_suspension,'kd_fs')

