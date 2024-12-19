Active suspension implementation

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

### Initial condition Testing #bug-report 
%%[[2024-12-19]] @ 00:46%%

I'm having an issue trying to simulate my active suspension, I don't seem to be able to give the `tuned_suspension` model initial conditions in the same way I could with the `passive_suspension`. I've added another 2 rows to account for the additional state variables but it won't run.

The error I get when I try to run it is:

```matlab
Warning: The input signal is undersampled. Use a sampling period smaller than 7.8e-03. 
> In DynamicSystem.checkLsimInputs (line 100)
In DynamicSystem/lsim (line 65)
In initial_velocity_response (line 47) 
Error using DynamicSystem/lsim
Cannot simulate state trajectory for models with singular E matrix. Use the "isproper" command to check
if the model is proper and to extract an equivalent explicit representation.

Error in initial_velocity_response (line 47)
  y = lsim(plant, U, T, IC);
```

The `tuned_suspension` is as follows:

```matlab
>> ss(tuned_suspension)

ans =
 
  A = 
           x1      x2      x3      x4      x5      x6
   x1       0       1       0       0       0       0
   x2  -46.24    -4.6   46.24     4.6       0       0
   x3       0       0       0       1       0       0
   x4   625.3   62.73   -3241  -62.73   -4051       0
   x5       0       0       0       0       1       0
   x6      -1       0       0       0       0       1
 
  B = 
          r
   x1     0
   x2     0
   x3     0
   x4  2610
   x5     0
   x6     0
 
  C = 
            x1      x2      x3      x4      x5      x6
   x_b       1       0       0       0       0       0
   v_b       0       1       0       0       0       0
   a_b  -46.24    -4.6   46.24     4.6       0       0
   x_w       0       0       1       0       0       0
   v_w       0       0       0       1       0       0
 
  D = 
        r
   x_b  0
   v_b  0
   a_b  0
   x_w  0
   v_w  0
 
  E = 
       x1  x2  x3  x4  x5  x6
   x1   1   0   0   0   0   0
   x2   0   1   0   0   0   0
   x3   0   0   1   0   0   0
   x4   0   0   0   1   0   0
   x5   0   0   0   0   0   1
   x6   0   0   0   0   0   0
 
Continuous-time state-space model.
```

This seems to be a issue as was faced [here](https://www.mathworks.com/matlabcentral/answers/1984559-cannot-use-lsim-function-properly) when I use `feedback` in [[create_active_suspension.m]] it adds a descriptor matrix `E`. I'm not sure how to or if I can get rid of this `E` matrix. 
I have tried running it through the `ss` constructor again to see if that simplifies it back down to an `[A,B,C,D]` form but it did not.

### Initial condition Testing #fix_log 
%%[[2024-12-19]] @ 00:58%%

After some playing about I found that if I run the `ss` constructor again followed by a `minreal` transform it magically works. 

`{matlab}plant = minreal(ss(tuned_suspension));
`
See the [[initial_velocity_response.m]] script associated with this commit for the full code.

### Incorrect B matrix being generated #bug-report 
%%[[2024-12-19]] @ 01:15%%

I'm finding that the switch statement in [[QC_params.m]] that is supposed to generate a `B` matrix with 2 inputs when `fs` is declared is not triggering as expected.

```matlab
if ~exist('fs', 'var') % make suspension passive if coeficients not defined
  B = [
    0 0 0 k_t/m_w; % road displacment
    0 fs/m_b 0 -fs/m_w % actuator signal
    ]';
else
  B = [
    0 0 0 k_t/m_w; % road displacment
    ]';
end
```

### Incorrect B matrix being generated #fix_log 
%%[[2024-12-19]] @ 01:26%%

First of all I had a "not" `~` present when I shouldn't have, and secondly it turns out stating the name of a script is different to calling `run` on that script. I assumed it was just a short hand but apparently just using it's name doesn't run it in the same workspace and while you can access all the globals from the script your importing all the variables in the current script are out of scope. 

`QC_params;` $\neq$ `run QC_params;` 

