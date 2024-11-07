[[Control systems coursework brief.pdf]]
[[DC Motor Control Lab Sheet 2023.pdf]]
[University of Michigan Control Tutorials](https://ctms.engin.umich.edu/CTMS/index.php?example=MotorPosition&section=SystemModeling)
## Testing
Room: 3236
Login: students3236
Password: 3236

Technical team room: 3231
Christopher Phillopson room: 3215

# Report Plan
## 1. INTRODUCTION, BACKGROUND, ENGINEERING PRINCIPLES: 20%
*In this part, include a review of the application of DC motors in consumer products or in industry. 
In what circumstances are DC motors preferred to other types?*
**Advantages**
- Easy speed control
- High torque at low speeds
- Easy to power with batteries

*In this coursework the motor under consideration is a brushed DC motor. How does this differ from a brushless DC motor? 
How is the motor modelled?*

*Using your own words, summarise and explain the physical principles behind a brushed DC motor. You may refer to the DC motor modelling section of the University of Michigan Control Tutorials [3]: https://ctms.engin.umich.edu/CTMS/index.php?example=MotorPosition&section=SystemModeling 
A transfer function is given in this reference together with a set of parameters. It is suggested that you familiarise yourself with this transfer function, as it will be used (Model 1) in Part 2. 
There is no need to present any simulation results in this part of the coursework, but you may want to comment on the effect different physical parameters have on the open-loop step response.*

## 2. MODELLING AND SIMULATION: 20%
### Plot loaded data
``` js
%% Lab data plot
load LabData.mat Time Motor Model;
Time = Time-Time(1);
figure;
    plot(Time, Motor, 'r-','DisplayName', 'Experimental');
    hold on
    plot(Time, Model, '-','DisplayName', 'Modle');
    hold off
    title('Experimental Shaft velocity data');
    xlabel('Time (s)');
    ylabel('Veolcity (rad/s)');
    grid on;
    legend('Location', 'southeast');
```
### Model 1
"*Use the transfer function from Part 1, together with the data below in Table 2 to create “Model 1” of the DC motor plant. Where parameters are missing you should estimate them (e.g., no viscous damping constant is given) – stating clearly what you have done.*"
#### Transfer function:
$$\frac{\theta}{V}(s)=\frac{k}{s(Js+b)(Ls+R)+k^2}$$
##### Explanation
- Rotor position = (rotor velocity / s)
- Rotor velocity
$$\frac{\dot\theta}{V}(s)=\frac{k}{(Js+b)(Ls+R)+k^2}$$
The angular acceleration of the rotor shaft ($\ddot\theta$) is related to torque ($T$), inertia($J$) & damping ($b$). 
$$ T = J \ddot\theta + b \dot\theta$$
The motor torque constant ($K_t​$) and the back electromotive force constant ($K_b$​) will be treated as the motor constant($K$).
Substituting for the motor constant ($K$) with $T=Ki$, and finding current ($i$) in terms of angular velocity using $V=Ri+e$ & $e=K \dot\theta$ gives:
$$K \frac{(V−K\dot\theta)}{R} = J \ddot\theta + b\dot\theta $$
Which can be simplified & rearranged to:
$$\frac{\dot\theta}{V}(s)=\frac{k}{(Js+b)(Ls+R)+k^2}$$
and taking a Laplace transform of both sides gives position
$$\frac{\theta}{V}(s)=\frac{k}{(Js+b)(Ls+R)+k^2} \times \frac{1}{s}$$

#### Given parameters:
| symbol    | description                  | value   | unit           |
| --------- | ---------------------------- | ------- | -------------- |
| ------    | **Motor**                    | ------- | -------------- |
| $J_m$     | Rotor moment of inertia      | 1.16E-6 | $kg \cdot m^2$ |
| $b_m$     | Viscous friction constant    |         |                |
| $K_b$     | Electromotive force constant | 0.0502  | $N \cdot m/A$  | 
| $K_t$     | Motor torque constant        | 0.0502  | $N \cdot m/A$  |
| $R_m$     | Electrical resistance        | 10.6    | $\dot U$       |
| $L_m$     | Electrical inductance        | 0.82    | $mH$           |
|           | Max continuous Torque        | 0.035   | $N \cdot m$    |
|           | Power rating                 | 18      | W              |
| $M_1$     | Inertial load disk mass      | 0.068   | $kg$           |
| $r_1$     | Inertial load disk radius    | 0.0248  | m              |
| ------    | **Linear Amplifier**         | ------- | -------------- |
| $V_{max}$ | max output voltage           | 15      | V              |
|           | max output current           | 1.5     | A              |
|           | max output power             | 22      | W              |
|           | Gain                         | 3       | $V/V$          |
#### Matlab notes
2023-11-20 @ 23:25 
- Added relevant parameters 
- Added transfer function for motor position
	$\frac{\dot\theta}{V}(s)=\frac{k}{(Js+b)(Ls+R)+k^2}$
``` js
J = 1.16E-6;
b = ?; %%example:3.5077E-6
K = 0.0502;
R = 10.6;
L = 8.2E-5;
s = tf('s');
P_motor = K/(s*((J*s+b)*(L*s+R)+K^2))
```
2023-12-07 @ 05:03 
- I accounted for the inertia of the loads
``` js
M1 = 0.068;  % Inertial load disk mass (kg)
r1 = 0.0248; % Inertial load disk radius (m)

J1 = 0.5 * M1 * r1^2;  % Inertia of the load disk
```
- I got the script to output numerators & denominators for the Simulink transfer function blocks
``` js
[V_tf_n, V_tf_d] = tfdata(V_shaft, 'v');
[P_tf_n, P_tf_d] = tfdata(P_shaft, 'v');
```
- Imported the lab data
- Plotted the lab data
- added transfer function for angle as well as position
``` js
V_shaft = K/( (J_total*s+b)*(L*s+R)+K^2 );
P_shaft = K / (s * ((J_total * s + b) * (L * s + R) + K^2));
```
- messed about for ages trying to get Simulink to use the time variable form labData until I realised that didn't solve my problem anyway so just set the labData to start from 0.14s to match. `Time = Time-Time(1)+0.14;`
- Made a figure compare my model with the lab values
- predicted rotor position based on lab values for motor angle
	`position = cumtrapz(Time, Motor);`
	not sure why its cumtrapz instead of just trapz but it works
``` js
%clear, close all

%% defining variables
J = 1.16E-6; % Rotor moment of inertia
b = 3.3E-5; % Viscous friction constant
K = 0.0502; % Motor torque / back emf constant
R = 10.6;
L = 8.2E-5;
s = tf('s');

% Transfer functions
V_shaft = K/( (J*s+b)*(L*s+R)+K^2 );
P_shaft = K/(s*((J*s+b)*(L*s+R)+K^2));

%% Account for the load
M1 = 0.068;  % Inertial load disk mass (kg)
r1 = 0.0248; % Inertial load disk radius (m)

J1 = 0.5 * M1 * r1^2;  % Inertia of the load disk
J_total = J + J1;      % Total inertia

% Updated transfer functions
V_shaft = K/( (J_total*s+b)*(L*s+R)+K^2 );
P_shaft = K / (s * ((J_total * s + b) * (L * s + R) + K^2));

%% Simulink variables
[V_tf_n, V_tf_d] = tfdata(V_shaft, 'v');
[P_tf_n, P_tf_d] = tfdata(P_shaft, 'v');
load LabData.mat Time;
Time = Time-Time(1); %+0.13998
timeMatrix = [linspace(0, (length(Time)-1)*0.01, length(Time))', double(Time)];
sim MotorSim1;

load LabData.mat Motor Model;
position = cumtrapz(Time, Motor);
%% Lab data plot
figure;
    plot(Time, Motor, 'r-','DisplayName', 'Experimental');
    hold on
    plot(Time, Model, 'b-','DisplayName', 'Modle');
    hold off
    title('Experimental Shaft velocity data');
    xlabel('Time (s)');
    ylabel('Veolcity (rad/s)');
    grid on;
    legend('Location', 'southeast');
%% Model plots
figure;
	% Input voltage
	subplot(3, 1, 1);
		plot(out.Voltage, 'r-');
		title('Input voltage');
		xlabel('Time (s)');
		ylabel('Voltage (V)');
		grid on;
	% Velocity
	subplot(3, 1, 2);
		plot(Time, Motor, 'b-','DisplayName', 'Experimental');
        hold on
        plot(out.V_shaft, 'r-','DisplayName', 'Modle');
        hold off
		title('Shaft velocity model vs lab data');
		xlabel('Time (s)');
		ylabel('Veolcity (rad/s)');
		grid on;
        legend('Location', 'southeast');
	% Position
	subplot(3, 1, 3);
		plot(Time, position, 'b-','DisplayName', 'Experimental estimate');
        hold on
        plot(out.P_shaft, 'r-','DisplayName', 'Modle');
        hold off
		title('Shaft position model vs lab data');
		xlabel('Time (s)');
		ylabel('Position (rad)');
		grid on;
        legend('Location', 'southeast');
```
### Basic transfer function
"**Now create a Simulink version of the simple motor model using the signal generator and transfer function blocks. Figure 4 shows how this may look. The plant transfer function is $𝐺(𝑠) = \frac{𝐾} {𝜏𝑠+1}$ and the parameters 𝐾 and 𝜏 need to be adjusted.**
**Confirm the model gives the same or similar results as the loaded ‘Model’ data. Show a plot comparing the two signals.****
**Tune the parameters to give a good representation of the actual motor result. 
Present your results and note the values of K and τ, as well as including a brief summary of your method"**

*My summary*
- tune a basic transfer function block to look like labData.motor
- Plot your model against labData.motor
- Record your method

### Compare the two models
"**Now add the transfer function of Model 1 to the Simulink diagram, so you can compare the two, using the same input voltage.**
**Compare angular velocity and angle responses. You will need to make some adjustments since Model 1 predicts angle and Model 2 predicts speed!**
**Also compare pole locations. Comment on similarities and differences. In any case you will use Model 2 for the remainder of the assignment, since we have confidence that it represents the actual plant dynamics.**"

*My summary*
- Compare basic tf to tf based on $\frac{\dot\theta}{V}(s)=\frac{k}{(Js+b)(Ls+R)+k^2}$
- Find pole locations for both & compare
## PART 3. PID CONTROLLER DESIGN AND SIMULATION: 20%

- Expand your Simulink model (Model 2) to include a PID controller for rotor angle, 
- using the signal generator to create a square-wave reference signal, with amplitude = 1 radian and frequency 0.4 Hz. 
- Selecting the PID gains 𝑘𝑝 = 1, 𝑘𝑑 = 0, 𝑘𝑖 = 0, you should obtain the result shown in [[DC Motor Control Lab Sheet 2023.pdf#selection=0,4,16,16|figure 6]].
- manually tune the PID controller to improve tracking of the square-wave.

kp = 5
kd = 0.15
ki = 0.2

Bsp = 1
bsd = 0
tf = 0.0060

%%
kp = 7
kd = 0.175
ki = 0.2

Bsp = 1
bsd = 0
tf = 0.0060
%%
- Describe the method you use to tune the three PID gains, and how each affects control performance.
- After you obtain your best result, compare with the initial result similar to Figure 6 and point out which performance metrics have improved and by how much.
- The actual motor has a limited input voltage of 15V. use the PID Advanced tab to mimic this (set the upper and lower saturation limits to 15 and -15). How does this affect your results?
- Test your controller with another type of reference signal, e.g. a sine or What limitations are there, if any, when you the reference at 
	- (i) high frequency (5 Hz say)
	- (ii) low frequency (0.2 Hz say)?
- Include plots and brief descriptions to explain your results.

## PART 4. PID CONTROL EXPERIMENT (LAB TESTING): 20%
2023-12-07 @ 05:49 
1. test the PID controller that was designed in simulation,
2. see how real-world performance matches simulation for step changes in the reference,
3. test robustness when weights are added to the rotor. 

 PID controller in the DCMCT takes the expanded form:
 $$𝑈(𝑠) = 𝑘_𝑝 (𝑏_{𝑠𝑝}𝑅(𝑠) − 𝑌(𝑠)) + 𝑘_{𝑑𝑠}𝑠(𝑏_{𝑠𝑑}𝑅(𝑠) − 𝑌(𝑠)) + 𝑘_𝑖 \frac{1}{𝑠} (𝑅(𝑠) − 𝑌(𝑠))$$
Reference weights: $b_{sp} \ \& \ b_{sd}$ 
	The reference weights include additional direct response to the reference signal. The term 𝑏𝑠𝑝 can potentially be used to offset any steady-state error, but where integral control is used this is not required, so please always select 𝑏𝑠𝑝 = 1. The term 𝑏𝑠𝑑 would also normally also be set to 1, but there may be an advantage of setting it to zero – test this out and try to explain any difference you see. You should perform step and sinusoid tests when looking at this part.

### Recovering my lab data
2023-12-11 @ 21:59
of the 10 experiments run 6 where corrupted as the file names & automatically generated variables began with a number.
``` bash
joeashton@pop-os:~/Sync/Obsidian/SuperValult/Projects/Uni Projects/Courseworks/Control systems/myLabData$ ls
'1a weights.mat'      '2a weights.mat'      'no weights F4.mat'
'1b weight.mat'       '2b weights.mat'      'no weights.mat'
'2a weights A0.mat'   'no weights A0.mat'
'2a weights A10.mat'  'no weights A10.mat'
```
For further information see this [thread on the Matlab forum](https://uk.mathworks.com/matlabcentral/answers/421-how-do-i-access-an-invalid-named-variable-from-an-exported-mat-file-that-matlab-will-not-recognize).
#### Python script
2023-12-12 @ 22:15
From the thread I copied this python code that appears to solve the issue:
``` python
import scipy.io as sio
import pathlib
import string

def fix_name(name):
    name="".join(c for c in name if c in string.ascii_letters+string.digits+"_")
    if name[0] not in string.ascii_letters:#name must start with a letter
        name="X"+name
    name=name[:63]#names may not be longer than 63 chars
    return name

ignore_names=["__header__","__version__","__globals__"]

def fix_struct(s):
    out_struct=dict()
    for name,value in s.items():
        if name not in ignore_names:
            out_struct[fix_name(name)]=value
    return out_struct

def struct_needs_fixing(s):
    for name in s.keys():
        if name not in ignore_names:
            if fix_name(name)!=name:
                return True
    return False

root=r"C:\someplace\folder_with_the_files"
root=pathlib.Path(root)
files=list(root.glob("*.mat"))#get all the .mat data files in the directory

Overwrite=False #overwrite files in place

for f in files:
    new_f=f.parent/("fixed_"+f.name)#save the modified file with a prefix
    if Overwrite:new_f=f
    struct=sio.loadmat(str(f))
    if struct_needs_fixing(struct):
        print("fixing",str(f))
        struct=fix_struct(struct)
        sio.savemat(new_f,struct)
    else:
        print("skipping",str(f))
```
Instead of fixing the issue it just deleted all the corrupted lab data without creating any of the fixed files. 
Luckily I do all my work in a Syncthing directory that is constantly synchronised across 3 devices with staggered versioning making retrieving the lost data a non issue. 
I thought this error could be to do with the way I have my file permissions set so I temporarily `sudo chmod 777` all the relevant files & the script itself moving everything into the same directory and tried again with no luck.
Its not spitting any compile errors but I think the script is failing to import its directories through pip as it's not loading in the correct conda environment. it still fails when launched with `python3` & when launched as a bare executable with `#!/usr/bin/env python` as first line.
Made a brand new conda environment with the required dependencies and ran it in there still nothing: `(FixMatlab) joeashton@pop-os:~/Sync/Obsidian/SuperValult/Projects/Uni Projects/Courseworks/Control systems/myLabData$ python3 invalidMatFix.py` 
This isn't working I will ask some advice form a physicist friend who's more experienced in both Matlab & python.
#### MEX script
2023-12-12 @ 02:22 
There was also a C++ script on the above mentioned thread. Matlab allows the use of C++ scripts as MEX functions ([See documentation](https://uk.mathworks.com/help/matlab/cpp-mex-file-applications.html)).
##### **Method**:
terminal
`touch RetrieveData.cpp`
`chmod 777 RetrieveData.cpp`
`gedit RetrieveData.cpp`
- paste:
``` cpp
#include "mex.h"
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
  char *Name;
  mxArray *Var;

    Name = mxArrayToString(prhs[0]);
    Var  = mexGetVariable("caller", Name);
    if (Var != NULL) {
       plhs[0] = mxDuplicateArray(Var);
    } else {
       plhs[0] = mxCreateDoubleMatrix(0, 0, mxREAL);
    }
    mxFree(Name);
    return;
  }
```
- save & close;
Matlab live script
``` js
clear
mex -setup c++
mex RetrieveData.cpp
A = RetrieveData('a2 weights.mat')
```
- Output: `A = []`
```

MEX configured to use **'g++'** for C++ language compilation.

Building with 'g++'.
MEX completed successfully.

A =

     []
```
No useful output tried using underscores & backslash for space, tried some sensible edits to the function code but no luck.
#### Second Mex attempt
Found [this](https://uk.mathworks.com/matlabcentral/fileexchange/42274-loadfixnames-loads-a-mat-file-fixing-invalid-names) fairly reputable submission on a series of threads and gave it a try but it no longer compiles. With the least helpful compiler error I've seen all day:
```
Error using loadfixnames
Unable to compile loadfixnames.c
```
Makes sense it was last updated on Tue, 01 Aug 2017.
#### Second python attempt
2023-12-12 @ 04:59 
Tried using the same python script again on a different machine with the hopes I was just missing something by doing it in miniconda on Linux. This time I went full Microsoft using jupyter notebook inside VS code on windows 10.
***Finally success!***

## Results
2023-12-10 @ 16:38 
### Comparing model 1&2
**Plots I should do**
- Plot model 1 & 2 against labData.motor
- Plot avdev of model 1, 2 from labData.motor
- Do Bode & Rlocus plots for both & compare

### Real world data
**Plots I should do**
- Compare model 2 w PID against real world w PID
	- show effects of weights
		- plot both graphs of 1 weight against no weights
		- plot both 2 weights against no weights
	- Show effect of amplitude
		- Find difference in avdev
	- Show effect of frequency
		- Find difference in avdev
	- Show compounding effects of weights & frequency
		- Find difference in avdev

#### Normalising lab data
2023-12-12 @ 02:02 
I can't seem to find a Matlab function that automatically finds recurring patterns an allows you to truncate data to fit it like the screen of an oscilloscope dose automatically.
I'm going to try and figure out how to do it myself, though it could be a colossal waste of time compared to doing it manually.
##### Brainstorming
**How is this going to work?**
- run the signal generator column of the `_value` arrays by a comparator and index the array at points where it switches.
- Write a C++ script to Regex match the signal generator column of the `_value` arrays with an  array of ones and import as a MEX function.
- Look at each dataset and manually find the second instance of a negative followed by a positive in each and record this as an offset associated with each respective dataset.
**What do these have in common?**
- Need to find the index of full wavelengths
With an array of indexes for every full wavelength I can pick a set near the end of the sample to get the best data.
**One way of creating the index:**
`full_waves_index = strfind(no_weights_Value(:,2)', ones(1,49));`
I don't like this as some have 49 1s in a row and others have 50.
**Improvement**
I need something more like a comparitor,
`full_waves_index = find(diff(no_weights_Value(:, 2) > 0) > 0) + 1;`
now I want an array with 4 full wavelengths near the end
`Last_4_waves = no_weights_Value(full_waves_index(end-5):full_waves_index(end)-1,1);`
2023-12-12 @ 02:52 damn that took pretty much a whole hour, I'm really not sure about this coding for a living thing anymore.
**now as a function**
``` js
function L4w = Last_4_waves(Value)
	full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
	L4w = Value(full_waves_index(end-5):full_waves_index(end)-1,1);
end
```
can't plot without time-series may as-well add that so its consistent
``` js
function L4w = Last_4_waves(Value)
full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
L4w = [linspace(0, 10, 1000)',Value(full_waves_index(end-11):full_waves_index(end-11)+999,:)];
end
```
never mind terns out you don't need a time series scratch that.
## Conclusion
2023-12-13 @ 18:35 
- It is possible to model motors easily to a high degree of accuracy based on their specs or a sample of test data.
# Main MATLAB code
``` js
%% clear
clear
close all

%% defining variables
J = 1.16E-6; % Rotor moment of inertia
b = 3.3E-5; % Viscous friction constant
K = 0.0502; % Motor torque / back emf constant
R = 10.6;
L = 8.2E-5;
s = tf('s');

% Transfer functions
V_shaft = K/( (J*s+b)*(L*s+R)+K^2 );
P_shaft = K/(s*((J*s+b)*(L*s+R)+K^2));

%% Account for the load
M1 = 0.068;  % Inertial load disk mass (kg)
r1 = 0.0248; % Inertial load disk radius (m)

J1 = 0.5 * M1 * r1^2;  % Inertia of the load disk
J_total = J + J1;      % Total inertia

% Updated transfer functions
V_shaft = K/( (J_total*s+b)*(L*s+R)+K^2 );
P_shaft = K / (s * ((J_total * s + b) * (L * s + R) + K^2));

%% Simulink variables
[V_tf_n, V_tf_d] = tfdata(V_shaft, 'v');
[P_tf_n, P_tf_d] = tfdata(P_shaft, 'v');

%% Load lab data
Time = linspace(0.14,10.14,1000); %+0.13998 shift timeseries to fit labData
%timeMatrix = [linspace(0, (length(Time)-1)*0.01, length(Time))', double(Time)];
sim MotorSim1;
sim PIDmodel.slx;
load LabData.mat Motor Model;
position = cumtrapz(Time, Motor);

%% provided Lab data plot
figure(3);
    plot(Time, Motor, 'b-','DisplayName', 'Experimental');
    hold on
    plot(Time, Model, 'r-','DisplayName', 'Provided Modle');
    hold off
    title('Experimental Shaft velocity data');
    xlabel('Time (s)');
    ylabel('Veolcity (rad/s)');
    grid on;
    legend('Location', 'southeast');

%% Model plots
figure(2);
	% Input voltage
	subplot(3, 1, 1);
		plot(out.Voltage, 'r-');
		title('Input voltage');
		xlabel('Time (s)');
		ylabel('Voltage (V)');
		grid on;
	% Velocity
	subplot(3, 1, 2);
		plot(Time, Motor, 'b-','DisplayName', 'Experimental');
        hold on
        plot(out.V_shaft, 'r-','DisplayName', 'Theoretical Model');
        hold off
		title('Shaft velocity model vs lab data');
		xlabel('Time (s)');
		ylabel('Veolcity (rad/s)');
		grid on;
        legend('Location', 'southeast');
	% Position
	subplot(3, 1, 3);
		plot(Time, position, 'b-','DisplayName', 'Experimental Estimate');
        hold on
        plot(out.P_shaft, 'r-','DisplayName', 'Theoretical Model');
        hold off
		title('Shaft position model vs lab data');
        labels()
		% xlabel('Time (s)');
		% ylabel('Position (rad)');
		% grid on;
        % legend('Location', 'southeast');

%% Compare performance
V_shaftD = 17.491/(0.08*s+1);
figure(1);
    plot(out.Voltage1, 'g','DisplayName', 'Input signal (V)');
    hold on
    plot(out.V_TheoryModel, 'b-','DisplayName', 'Theory based model (rad/s)');
    hold on
    plot(out.V_DataModel, 'r--','DisplayName', 'Data driven model (rad/s)');
    hold off
    title('Theory vs Data Based Models');
    xlabel('Time (s)');
    ylabel('Veolcity (rad/s) / Voltage (V)');
    grid on;
    legend('Location', 'southeast');


%% load my lab data
load myLabData/'no weights.mat'
load myLabData/'no weights A0.mat'
load myLabData/'no weights A10.mat'
load myLabData/'no weights F4.mat'

load myLabData/'fixed_a1 weights.mat'
load myLabData/'fixed_b1 weight.mat'

load myLabData/'fixed_a2 weights.mat'
load myLabData/'fixed_b2 weights.mat'

load myLabData/'fixed_a2 weights A0.mat'
load myLabData/'fixed_a2 weights A10.mat'

%% My lab data plots
%% Varying amplitude
figure;
    subplot(2,2,1:2);
        plotme(no_weights_Value);
        title("Amplitude 1 (rad)");
    subplot(2,2,3);
        plotme(no_weights_A0_Value);
        title("Amplitude 0.1 (rad)");
    subplot(2,2,4);
        plotme(no_weights_A10_Value);
        title("Amplitude 10 (rad)");
    legend({'Rotor Position (rad)','Input Signal (rad)'},  'Location', 'northeastoutside');
%% Single weights
figure;
    plot(Last_10_wavesD(X_1b_weight_Value));
    hold on
    plotme(no_weights_Value);
    title("Effect of Single Weight");
    legend({'Rotor Position with brass weight (rad)','Rotor Position without brass weight (rad)','Input Signal (rad)'},  'Location', 'southeast');
%% double weights
figure;
    hold on
    plot(Last_10_wavesD(X_2b_weights_Value));
    plot(Last_10_waves(X_2a_weights_Value));
    title('Double weights response');
    labels();
    legend({'Rotor Position with 2 brass weights (rad)','Rotor Position with 2 aluminium weights (rad)','Input Signal (rad)'},  'Location', 'southeast');
%% frequency
figure;
    hold on
    plot(Last_n_waves(no_weights_F4_Value,40,199));
    title("4Hz Frequency Response");
    legend({'Rotor Position (rad)','Input Signal (rad)'},  'Location', 'northeast');
    labels();
%% Funks
function labels()
    xlabel('Time (s)');
    ylabel('Position (rad)');
	grid on;
    % legend('Location', 'southeast');
end

function Ltw = Last_10_waves(Value)
    full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
    Ltw = [Value(full_waves_index(end-11):full_waves_index(end-11)+999,:)]; %linspace(0, 10, 1000)',
end
function Ltw = Last_10_wavesD(Value)
    full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
    Ltw = [Value(full_waves_index(end-11):full_waves_index(end-11)+999,1)]; %linspace(0, 10, 1000)',
end

function Ltw = Last_n_waves(Value,n,t)
    full_waves_index = find(diff(Value(:, 2) > 0) > 0) + 1;
    Ltw = [Value(full_waves_index(end-n-1):full_waves_index(end-n-1)+t,:)]; %linspace(0, 10, 1000)',
end

function plotme(Value)
        plot(Last_10_waves(Value));
        labels();
end
```