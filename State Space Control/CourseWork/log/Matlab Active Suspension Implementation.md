
## Log
### Plan for Active suspension Implementation
%%[[2024-12-18]] @ 19:37%%

I looked at `hinfsyn` based on [this tutorial](https://www.mathworks.com/help/robust/gs/active-suspension-control-design.html) but it dosen't really look like what I need, we haven't been asked to deal with any uncertainty etc. 

I want to be able to use matlabs `systune` function to meet the briefs goals: 
- 5% settling time equal to 1.5s
- overshoot equal to 10%

Just a note on those goals, there is no specified max power of this actuator, this system could just have perfect performance if the actuator could exert infinite force with no latency.

[Guide](https://www.mathworks.com/help/control/ug/tuning-control-systems-with-systune.html)
[MATLAB systune docs](https://www.mathworks.com/help/control/ref/dynamicsystem.systune.html)

### Implementation
%%[[2024-12-18]] @ 21:48%%

That was actually really easy.

I added a script [[create_active_suspension.m]] to take the [[QC_params.m]] and add a controller with proportional and derivative gain, then made a [[tune_active_suspension.m]] that tunes the gains to to meet the targets. It was probably less than a dozen lines of code all in.