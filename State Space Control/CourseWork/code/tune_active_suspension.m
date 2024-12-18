create_active_suspension

%% Set Goals
settling_time_goal = TuningGoal.StepTracking('r', 'x_b', 1.5);
overshoot_goal = TuningGoal.Overshoot('r', 'x_b', 10);
% control_effort_goal = TuningGoal.Gain('r', 'u', 1);


%% Tune

goals = [settling_time_goal, overshoot_goal];
[Gtuned, fSoft] = systune(active_suspension, goals);
