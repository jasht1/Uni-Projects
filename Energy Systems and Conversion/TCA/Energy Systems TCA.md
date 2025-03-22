# Question 1 
## a. What are the main sources of losses that prevent a wind turbine from operating at or near the Betz limit? 
[5 marks] 

The [[Betz limit]] is an estimate for the theoretical maximum continuous efficiency of an open flow turbine based on the optimal proportion of energy to extract from an incompressible fluid flow. In practice turbines cannot convert all the kinetic energy extracted from the mass flow to electrical energy due to:

1. Coil losses & associated inefficiencies in the alternator,
2. Non Ideal fluid flow:
   - turbulence in the flow,
   - off axis flow,

3. Frictional losses:
	- at the fluid - turbine interface,
	- in the mechanical components,

## b. An engineer boasting about the virtues of their new wind turbine claimed it has an efficiency of 65.3%. Starting from $P= \frac{1}{2} \dot{m}({v_{1}}^{2}−{v_{2}}^{2})$, with $P$ being the power output resulting from a change in wind velocity from $v_{1}$ to $v_{2}$ across turbine’s blades, show that the engineer’s claim cannot be true and calculate the number of percentage points his estimation is off by. 
[5 marks]

### Assuming the optimal case

Given we have no information on the nature of the turbine we ought avoid speculation by keeping assumptions generally applicable to any device that my be fairly described as a "wind turbine". Considering a "wind turbine" as a means to convert the kinetic energy of a wind stream into electrical energy we may assume these as the system bounds and thus the efficiency a measure of the proportion of electrical power output over the total wind power available in the axial cross sectional area of the turbine. We can also assume there is some actuator exposed to a wind stream, this actuator extracts kinetic energy from the wind stream and converts it to electrical energy. It can be assumed that this conversion is less than 100% efficient based on the 2nd law of thermodynamics thus **the electrical output power must be less than the power extracted from the wind stream**. 

Using these assumptions [[Betz limit]] can be applied which provides an estimate for the theoretical maximum continuous efficiency of an open flow turbine based on the optimal velocity change of the fluid given by a control volume analysis. 

As the kinetic energy of a wind stream is given by:

$$E = \frac{1}{2}mv^{2}$$

The power extracted from a wind stream can be found by:

$$P= \frac{1}{2} \dot{m}({v_{1}}^{2}−{v_{2}}^{2})$$

Where:
- $\dot{m}$ : mass flow rate through the swept area of the turbine ($kg/s$)
- $v_{1}$ : initial flow velocity 
- $v_{2}$ : final flow velocity

So the proportion of power extracted from the wind stream is:

$$\eta = \frac{({v_{1}}^{2}−{v_{2}}^{2})}{{v_{1}}^{2}}$$

However this doesn't give the full story as if $v_{2}$ is reduced then so too must mass flow rate and thus less power will be generated.

The mass flow rate $\dot{m}$ is the product of the functional area of the turbine $A_{T}$, the fluid density $\rho$ and the velocity over the turbine $v_{T}$. The density $\rho$ can be approximated based on a reasonable air temperature. However the functional area of the turbine $A_{T}$ and the wind velocity at the turbine are unknown so the optimal values will be considered.

### Finding velocity over the turbine in terms of initial and final velocity
%%[[2025-01-09]] @ 16:43%%

This section will prove the velocity over the turbine $v_{T}$ is the average of the incoming $v_{1}$ and outgoing $v_{2}$ velocity.

#### Setup

3 points $n$ are considered and will denoted by subscript:
1. $U$ : upstream of the rotor,
2. $T$ : at the rotor,
3. $D$ : downstream of the rotor,

each with their respective cross section area $A_{n}$ and flow speed $v_{n}$. where $v_{U}$ is equivalent to $v_{1}$ and $v_{D}$ is equivalent to $v_{2}$ as used previously. 
%% The manifold on which the cross sections are taken are normal to  %%

Conservation of mass implies mass flow rate at these 3 axial slices are equal:

$$\large \dot{m} = \rho A_{U}v_{U} = \rho A_{T}v_{T} = \rho A_{D}v_{D}$$

Where:
- $\dot{m}$ : is the fluids mass flow rate
- $\rho$ : is the the fluids density

#### First equation for power

The force on the turbine my be expressed given Newton's 3rd law:

$$F = ma \quad \to \quad F = m \frac{dv}{dt} \quad \to \quad F = \dot{m} \Delta v$$

by substitution the identity for mass flow rate at the turbine and the change in fluid velocity across it:

$$\therefore \quad F_{T} = \rho A_{T} v_{T} (v_{U} - v_{D})$$

Work done $E$ being the product of force $F$ and distance $x$, 

$$E = Fx$$ 

And power $P$ being the rate of work done,

$$P = F \frac{dx}{dt} \quad \to \quad P = F v$$

Where change in distance by change in time $\frac{dx}{dt}$ of the working fluid can be substituted with it's velocity $v$.

The power exerted at the turbine can then be expressed in these terms:

$$P = \rho A_{T} v_{T}^{2} (v_{U} - v_{D})$$

#### Second equation for power

An alternate and equivalent equation for power can be found based on difference in kinetic energy upstream $U$ and downstream $D$, where kinetic energy is given by:

$$E = \frac{1}{2} m v^{2}$$

And power by accounting for mass flow rate $\dot{m}$ and change in velocity:

$$P = \frac{1}{2} \dot{m} \Delta v^{2}$$

Thus power at the turbine is also given by:

$$P = \frac{1}{2} \rho A_{T} v_{T} (v_{U}^{2} - v_{D}^{2})$$

#### Conclusion

By setting these identities as equal an identity for $v_{T}$ in terms of $v_{U}$ & $v_{D}$ can be found:

$$P = \rho A_{T} v_{T}^{2} (v_{U} - v_{D}) = \frac{1}{2} \rho A_{T} v_{T} (v_{U}^{2} - v_{D}^{2})$$

> [!NOTE] Workings
> 
> $$\begin{align}
> \cancel{\rho A_{T} v_{T}} v_{T} (v_{U} - v_{D}) &= \cancel{\rho A_{T} v_{T}} \frac{1}{2} (v_{U}^{2} - v_{D}^{2})\\
> v_{T} \cancel{(v_{U} - v_{D})} &= \frac{1}{2} (v_{U} + v_{D}) \cancel{(v_{U} - v_{D})}\\
> &\therefore \\
> v_{T} &= \frac{1}{2} (v_{U} + v_{D})\\
> \end{align}$$

Thus:

$$\Large \dot{m} = \rho A_{T} \frac{v_{1} + v_{2}}{2}$$

### Finding optimal velocity change
%%[[2025-01-10]] @ 00:40%%

Factoring in the identity for mass flow rate found above back into the equation for power extracted from a wind stream gives:

$$\Large P = \frac{1}{4} \rho A_{T} (v_{1} + v_{2}) ({v_{1}}^{2}−{v_{2}}^{2})$$

This equation can be rearranged slightly to emphasise the impact of the proportional velocity drop, i.e. $\frac{v_{2}}{v_{1}}$, like so:

> [!NOTE] Workings
> 
> $$\text{substituting:}\quad v_{2} = \frac{v_{2}}{v_{1}}v_{1}$$
> 
> $$P = \frac{1}{4} \rho A_{T} \left( v_{1} + \frac{v_{2}}{v_{1}} v_{1} \right) \left( {{v_{1}}^{2} - \frac{v_{2}}{v_{1}}v_{1}}^{2} \right)$$
> 
> $$P = \frac{1}{4} \rho A_{T} {v_{1}}^{3} \left( 1 + \frac{v_{2}}{v_{1}} \right) \left( 1 - \frac{v_{2}}{v_{1}}^{2} \right)$$
> 

$$\large P = \frac{1}{4} \rho A_{T} {v_{1}}^{3} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right) $$

This indicates the proportional velocity drop across a turbine $x$, where $x = v_{2}/v_{1}$, impacts power output $P$ according to the following relationship:

$$\large P \propto- x^{3} - x^{2} + x + 1 \quad \text{where} \ x = v_{2}/v_{1}$$

The maximum value Given that the turbine is extracting energy from the wind flow the velocity will go down $v_{2} < v_{1}$ and will not be negative $v_{2} > 0$ thus providing the limits. The maximum value inside of these limits the proportional velocity drop associated with the maximum continuous extract-able power:

$$P_{\text{max}} = \max(-x^{3} - x^{2} + x + 1) \quad \text{in range:} \ 0<x<1$$

> [!NOTE] Workings
> 
> The maximum is found by checking for stationary points within the range, being a simple quadratic we can simply apply the quadratic formula:
> 
> $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
> 
> $$\begin{align*}
> x &= \frac{-2 \pm \sqrt{2^2 - 4(3)(-1)}}{2(3)}\\
> x &= \frac{-2 \pm \sqrt{4 + 12}}{6} \\
> x &= \frac{-2 \pm \sqrt{16}}{6} \\
> x &= \frac{-2 \pm 4}{6}\\
> \\
> \therefore \quad 
> x = \frac{-2 + 4}{6} = \frac{1}{3} 
> \quad &\& \quad 
> x = \frac{-2 - 4}{6} = -1
> \end{align*}$$
> 
> Only $\frac{1}{3}$ is in the range $0<x<1$ this is the maximum continuous proportional velocity drop $\frac{v_{2}}{v_{1}}$.

Which occurs at $x = 1/3$ indicating a turbine must reduce the fluid velocity by $66.\dot{6}$% to extract the maximum continuous power from a fluid flow. Thus at max efficiency $v_{2} = v_{1}/3 \ @ \ \eta_{max}$.

### Finding max efficiency
%%[[2025-01-10]] @ 02:48%%

#### Attempt 1
Dividing the power equation by the total power of the wind stream gives the following equation for the proportion of available wind power extracted:

$$\Large \eta = \frac
{\frac{1}{4} \rho A_{T} {v_{1}}^{3} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right)}
{\frac{1}{2} \rho A_{T} \frac{v_{1} + v_{2}}{2} {v_{1}}^{2}} $$

Once the redundant terms are cancelled and the optimal proportional velocity drop is substituted this becomes:

> [!NOTE] Workings
> 
> $$\begin{align*}
> \text{Canceling redundant terms,}\\
> \eta &= \frac
> {\cancel{\frac{1}{4}} \cancel{\rho A_{T}} {v_{1}}^{\cancel{3}} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right)}
> {\cancel{\frac{1}{2}} \cancel{\rho A_{T}} \frac{v_{1} + v_{2}}{\cancel{2}} \cancel{{v_{1}}^{2}}}
> \\\\
> \eta &= \frac
> {\cancel{{v_{1}}} \left( - \frac{v_{2}}{v_{1}}^{3} - \frac{v_{2}}{v_{1}}^{2} + \frac{v_{2}}{v_{1}} + 1 \right)}
> {\cancel{v_{1}} + \frac{v_{2}}{v_{1}}}
> \\\\
> \eta &=  \frac
> {- \frac{v_{2}}{v_{1}}^{\cancel{3}2} - \frac{v_{2}}{v_{1}}^{\cancel{2}} + \cancel{\frac{v_{2}}{v_{1}}} + \cancel{1} \frac{v_{1}}{v_{2}}}
> {\cancel{\frac{v_{2}}{v_{1}}}}
> \\\\
> \eta &= -\frac{v_{2}}{v_{1}}^{2} -\frac{v_{2}}{v_{1}} + \frac{v_{1}}{v_{2}}
> \\\\
> \text{Substituting:} \ v_{2} = v_{1}/3 \ @ \ \eta_{max}
> \\
> \eta_{max} &= -\frac{(v_{1}/3)}{v_{1}}^{2} -\frac{(v_{1}/3)}{v_{1}} +\frac{v_{1}}{(v_{1}/3)}
> \\
> \eta_{max} &= -\frac{\cancel{v_{1}}}{3 \cancel{v_{1}}}^{2} -\frac{\cancel{v_{1}}}{3 \cancel{v_{1}}} +\frac{3\cancel{v_{1}}}{\cancel{v_{1}}}
> \end{align*}
> $$

$$\eta = -\frac{1}{3}^{2} -\frac{1}{3} +3 = 2.\dot{5}$$

#### Attempt 2
Where efficiency is 

$$\eta = \frac{P_\text{useful out}}{P_\text{total in}}$$

Factoring in the initial equation for power:

$$P= \frac{1}{2} \dot{m}({v_{1}}^{2}−{v_{2}}^{2})$$

With the velocity drop associated with maximum continuous power for an upper bound of useful power output $v_{2} = v_{1}/3 \ @ \ P_{max}$, and a velocity drop of 100% for total input power $v_{2} = 0 \ @ \ P_{tot}$:

$$\eta_{max} = \frac
{\frac{1}{2} \dot{m}({v_{1}}^{2}−{\left( \frac{v_{1}}{3} \right)}^{2})}
{\frac{1}{2} \dot{m}({v_{1}}^{2}−(0)^{2})}$$

$$\eta_{max} = \frac
{\cancel{\frac{1}{2} \dot{m}}({v_{1}}^{2}−{\left( \frac{v_{1}}{3} \right)}^{2})}
{\cancel{\frac{1}{2} \dot{m}}({v_{1}}^{2}−(0)^{2})}$$

$$\eta_{max} = \frac{8}{9}$$

#### Attempt 3
Where efficiency is 

$$\eta = \frac{P_\text{useful out}}{P_\text{total in}}$$

Factoring in the initial equation for power:

$$P= \frac{1}{2} \dot{m}({v_{1}}^{2}−{v_{2}}^{2})$$
and substituting the identity for mass flow rate:

$$\dot{m} = \rho A_{T} \frac{v_{1} + v_{2}}{2}$$

With the velocity drop associated with maximum continuous power for an upper bound of useful power output $v_{2} = v_{1}/3 \ @ \ P_{max}$, and a velocity drop of 100% for total input power $v_{2} = 0 \ @ \ P_{tot}$:

$$\eta = \frac 
{\frac{1}{2} \rho A_{T} \frac{v_{1} + \left( \frac{v_{1}}{3} \right)}{2} ({v_{1}}^{2}−{\left( \frac{v_{1}}{3} \right)}^{2})} 
{\frac{1}{2} \rho A_{T} {v_{1}}^{2}({v_{1}}^{2}−(0)^{2})}$$

$$\eta = \frac 
{\cancel{\frac{1}{2} \rho A_{T}} \frac{\cancel{v_{1}} + \left( \frac{\cancel{v_{1}}}{3} \right)}{2} ({v_{1}}^{2}−{\left( \frac{v_{1}}{3} \right)}^{2})} 
{\cancel{\frac{1}{2} \rho A_{T}} \cancel{v_{1}}({v_{1}}^{2}−\cancel{(0)^{2}})}$$

$$\eta = \frac 
{{v_{1}^2}−{\left( \frac{{v_{1}^2}}{9} \right)}^{2}} 
{6\cancel{v_{1}}^2}$$

$$\eta = \frac 
{\cancel{v_{1}^2}−{\left( \frac{\cancel{v_{1}^2}}{9} \right)}^\cancel{2}} 
{6\cancel{v_{1}}^2}$$

$$\eta = \frac 
{1−{\frac{1}{9}}} 
{6}$$

$$\eta_{max} = \frac{8}{54} \approx 0.148148148$$

#### Attempt 5 

$$\eta = \frac 
{\frac{1}{2} \rho A_{T} \frac{v_{1} + \left( \frac{v_{1}}{3} \right)}{2} ({v_{1}}^{2}−{\left( \frac{v_{1}}{3} \right)}^{2})} 
{\frac{1}{2} \rho A_{T} {v_{1}}^{2}({v_{1}}^{2}−(0)^{2})}$$

$$\eta = \frac 
{\cancel{\frac{1}{2} \rho A_{T}} \frac{\cancel{v_{1}} + \left( \frac{\cancel{v_{1}}}{3} \right)}{2} ({v_{1}}^{2}−{\left( \frac{v_{1}}{3} \right)}^{2})} 
{\cancel{\frac{1}{2} \rho A_{T}} \cancel{v_{1}}({v_{1}}^{2}−\cancel{(0)^{2}})}$$

$$\eta = \frac 
{ (1+\frac{1}{3})\left({v_{1}^2}−{\left( \frac{{v_{1}^2}}{9} \right)}^{2}\right)} 
{2 v_{1}^{\cancel2}}$$

$$\eta = \frac 
{(1+\frac{1}{3})\left(\cancel{v_{1}^2}−{\frac{\cancel{v_{1}^2}}{9}}\right)} 
{6\cancel{v_{1}}^2}$$

$$\eta = \frac 
{(1+\frac{1}{3})(1−{\frac{1}{9}})} 
{6}$$

$$\eta_{max} = \frac{8}{54} \approx 0.148148148$$

#### Compromise

Okay clearly I've divided by 2 when I should have times-ed by 2 somewhere there, anyway I know this should equal $\frac{16}{27} \approx 59.3 \%$, therefore the engineer has over estimated by a minimum of $6 \%$.

## c. A wind turbine rated at $5 \ MW$ with a rotor radius of $48 \ m$ operates in a location where the air density is $1.2 \ \text{kg}/m^{3}$. The number of hours $H$ of operation of the wind turbine at a given wind speed is given by a Rayleigh PDF distribution: $H(u) = \frac{\pi}{2} \left( \frac{u}{\bar{u}^{2}} \right) exp [- \frac{\pi}{4} \left( \frac{u}{\bar{u}}^{2} \right) ]$ The rated wind speed is $13 \ m/s$, and its cut-out wind speed is $25 \ m/s$. Calculate the annual income from this turbine if the electricity it produces is sold at $10 \ \text{p}/kWh$. 
[You are required to use Excel or MATLAB for this problem. Tabulate your results accordingly] 
[15 marks]

```matlab 

% Range

wind_min = 1; %min wind speed in m/s
wind_max = 30; %max wind speed in m/s

wind_speed = wind_min:1:wind_max;

% Parameters
rho = 1.2; % air density in kg/m^3
R = 48; % rotor radius in meters
A_T = pi * R^2; % swept area in square meters
P_rated = 5e6; % rated power in watts (5 MW)
u_rated = 13; % rated wind speed in m/s
u_cutout = 25; % cut-out wind speed in m/s
eta = 0.59; % assuming turbine efficiency of betz lim

% Functions
rayleigh_pdf = @(u, ubar) (pi/2) * (u / ubar^2) .* exp(-pi * (u / ubar).^2 / 4);

nominal_P = @(u, ubar) (0.59 * 0.5 * rho * A_T * u.^3) .* rayleigh_pdf(u, ubar); % Power for u < u_rated
high_wind_P = @(u, ubar) P_rated * rayleigh_pdf(u, ubar); % Power for u_rated < u < u_cutout

% output array
income = zeros(size(wind_speed));

% main loop
for i = 1:length(wind_speed) % average wind speed (mean for the Rayleigh distribution)
  ubar = wind_speed(i);
  
  Nominal_E = integral(@(u) nominal_P(u, ubar), 0, u_rated); % Energy for u_cutin < u < u_rated in J
  high_wind_E = integral(@(u) high_wind_P(u, ubar), u_rated, u_cutout); % Energy for u_rated < u < u_cutout in J
  
  E = (Nominal_E + high_wind_E) / (60^2 * 1000); % total Energy in kWh
  
  annual_income(i) = E * 0.10 * 24*365; % income in £
  
end

% output
result_table = table(wind_speed', annual_income', 'VariableNames', {'AverageWindSpeed_m_s', 'Income_£'});
disp(result_table);

```


| AverageWindSpeed (m/s) | Income (£) |
| ---------------------- | ---------- |
| 1                      | 1.1908     |
| 2                      | 9.5264     |
| 3                      | 32.151     |
| 4                      | 76.108     |
| 5                      | 146.01     |
| 6                      | 237.71     |
| 7                      | 339.51     |
| 8                      | 439.93     |
| 9                      | 530.97     |
| 10                     | 607.73     |
| 11                     | 667.75     |
| 12                     | 710.56     |
| 13                     | 737.26     |
| 14                     | 749.91     |
| 15                     | 751.00     |
| 16                     | 743.00     |
| 17                     | 728.18     |
| 18                     | 708.46     |
| 19                     | 685.42     |
| 20                     | 660.28     |
| 21                     | 634.01     |
| 22                     | 607.32     |
| 23                     | 580.73     |
| 24                     | 554.62     |
| 25                     | 529.24     |
| 26                     | 504.77     |
| 27                     | 481.31     |
| 28                     | 458.92     |
| 29                     | 437.63     |
| 30                     | 417.42     |

# Question 2

## a. Which is worse – putting petrol in a diesel engine or vice versa? Rationalise each scenario. 
[5 marks]

Consider the difference in the properties of diesel and petrol:
1. Diesel is an effective lubricant where petrol is not a particularly effective lubricant and tends to dissolve non-polar hydrophobic greases that are often used as lubricants.
2. Petrol has a lower flash point than diesel
3. Petrol is more viscous than diesel

#### Petrol in a diesel engine

Diesel engines tend to use the diesel itself to lubricate many mechanical components through out the system, petrol would likely cause increased stress on any such components. This probably wouldn't have any immediate effects but would probably kill the engine eventually. 

The lower flash point of petrol would cause knocking i.e. early combustion, this causes allot of strain on the engine and could cause damage quite quickly. 

#### Diesel in a petrol engine

The Diesel being thicker would cause some strain on the fuel pumping systems of petrol engines and would not flow as expected especially in thinner pipes, It could even clog up some finer arteries or the carburetor. 

Speaking of the carburetor I would expect diesel would not aresolise particularly effectively and thus burn particularly dirty. The suit produced would build up especially around the intake and exhaust valves which could get stuck.

#### Conclusion

Both would be inconvenient mistakes, but I would expect petrol in a diesel engine to cause more damage more quickly. 


## b. In an air-standard Brayton cycle (Figure 1), air enters the compressor at 100 kPa and 15 C. The exit pressure at the compressor is 1000 kPa. The maximum temperature in the cycle is 1,100 C. Assume that air behaves as an ideal gas with a constant specific heat at 300 K. Also assume that each process within the cycle is steady and no kinetic or potential energy changes occur. 
[Note that thermodynamic tables are required in this task]

### i. the temperature and pressure at each point in the cycle, 
[10 marks] 

### ii. the compressor work, turbine work, and the cycle’s efficiency. 
[10 marks] 

# Question 3

## a. Explain what is meant by stoichiometric air? 
[2 marks] 

Stoichiometric connotes an amount in proportion to it's necessity in a chemical reaction. In the context of a specific reaction in this case likely the combustion of a fuel, it would be the exact amount of air necessary to achieve complete complete combustion based on their molar proportions in a complete combustion reaction.

## b. What do you understand by lean and rich fuel mixtures? State an advantage and a disadvantage of an engine running on either. 
[8 marks]

Lean vs rich distinguish mixes that contain fuel to oxidiser ratios lower vs higher than stoichiometric respectively. 

### Lean fuel mix
Lean fuel mixes introduce more air than strictly necessary for complete combustion. This typically **improves fuel efficiency** and results in higher combustion chamber temperature & pressure. 
A well designed engine should be able to withstand the added thermal and mechanical stress, the main issues is **production of $NOX$ which is a toxic pollutant**. While the chamber temperature is in excess of 2,500 K oxides of nitrogen can form, the higher the temperature & pressure an the longer it's maintained the more oxides of nitrogen are likely to be produced.

![[Knowledge/Engineering/Energy Systems/Engines/Reciprocating/attachments/Diesel Pressure Graphs, NOX Reigion (light).png]]


### Rich fuel mix
A fuel rich mix can achieve **higher peak power** for an engine tuned to take advantage of it, however this is at the expense of **lower fuel efficiency**. The lower fuel efficiency means more emissions increasing the impact on climate change and pollution. In the EU there are strict emissions standards for vehicles so it may not be legal to sell / run the engine fuel rich depending on the application. 


## c. Producer gas which is obtained from coal with the volumetric based composition given in the table below is combusted with 20% excess air. Calculate the air-to-fuel ratio: 

| Gas             | % mass |
| --------------- | ------ |
| Methane         | 3      |
| Carbon dioxide  | 4.5    |
| Oxygen          | 0.6    |
| Carbon monoxide | 27     |
| Hydrogen        | 14     |
| Nitrogen        | 50.9   |

[Note: you may assume that the air and fuel are the same temperature and pressure.]


> [!NOTE] Interpretation note
> Assuming:
> 1. The combustion involves both the methane and the hydrogen from the producer gas
> 2. Is complete combustion


### i. On a volumetric basis and 
[10 marks] 

The volumetric air–to–fuel ratio is the proportion of the volume of air over the volume of fuel introduced to combustion chamber. Given that the proportional volume of a gas in a gaseous mix is the same as it's molar proportion this is equivalent to it's Stoichiometry:

$$\text{AFR}_{V} = \frac{V_{\text{air}}}{V_{\text{fuel}}} = \frac{n_{\text{air}}}{n_{\text{fuel}}}$$

However we know that there was 20% more air than stoichiometricaly necessary:

$$\text{AFR}_{V} = \frac{n_{\text{air}}}{n_{\text{fuel}}} = \frac{n_{O_{2}} \times \frac{120}{100}}{n_{CH_{4}} + n_{H_{2}}}$$

The complete combustion of the methane and the hydrogen would take the form:

$$q_{1} \ CH_{4} + q_{2} \ H_{2} +q_{3} \ O_{2} \to q_{4} \ CO_{2} + q_{5} \ H_{2}O$$

Given that we know the ratio of methane to hydrogen it can be stated that:

$$3 q_{1} = 14 q_{2} \quad \therefore \quad q_{2} = \frac{3}{14}q_{1}$$

And given that all of the carbon will have been converted to carbon dioxide:

$$q_{4} = q_{1}$$

and all of the hydrogen to water:

$$q_{5} = \frac{2q_{2} + 4q_{1}}{2} = \frac{10}{7}q_{1}$$

The oxygen reacted is given by:

$$q_{3} = \frac{2q_{4} + q_{5}}{2} = \frac{12}{7} q_{1}$$

Therefore giving a volumetric air–to–fuel ratio of:

$$\text{AFR}_{V} = \frac{\frac{12}{10}q_{3}}{q_{1} + q_{2}} = \frac{\frac{12}{10} \times \frac{12}{7} \cancel{q_{1}}}{\cancel{q_{1}} + \frac{3}{14}\cancel{q_{1}}} = \frac{\frac{144}{70}}{1+\frac{3}{14}} = \frac{144}{85} \approx 1.69$$

### ii. On a mass basis 
[5 marks] 

The air–to–fuel mass ratio is the proportion of mass of air over the mass of fuel introduced to combustion chamber. This is given by the product of molar proportions (found previously) with their respective molar mass:

$$\text{AFR} = \frac{m_{\text{air}}}{m_{\text{fuel}}} = \frac
{n_{O_{2}} \left( \frac{21}{100}2M_{O} + \frac{79}{100}2M_{N} \right)}{n_{CH_{4}} \left( M_{C} + 4M_{H} \right) + n_{H_{2}} \left(2 M_{H}\right)}$$


Substituting in the molar masses:

$$\text{AFR} = \frac
{n_{O_{2}} \left( \frac{21}{100}2(16) + \frac{79}{100}2(14) \right)}{n_{CH_{4}} \left( (12) + 4(1) \right) + n_{H_{2}} \left(2 (1)\right)} = \frac
{n_{O_{2}} \left( \frac{721}{25} \right)}{n_{CH_{4}} ( 16) + n_{H_{2}} (2)}$$

Substituting in the molar proportions:

$$\text{AFR} =  \frac
{\frac{144}{70} \times \frac{721}{25}}
{1 \times 16 + \frac{3}{14} \times 2} = \frac{51912}{14375} \approx 3.61$$


Giving a air–to–fuel mass ratio of $3.61$


# Question 5

## a. Exergy and energy are very important quantities in the analysis and design of new power generation systems. As an engineer in a reputable company, a student on placement came to you with a question as they would like to know the difference between the two. Give them 3 differences, using equations where necessary.
[6 marks]

### Conservation

**Energy is always conserved whereas exergy is not**, in fact exergy is almost always destroyed when work is done.

### Exergy is dependent on the environment

Energy a measure of potential to do work relative to an arbitrary frame of reference, whereas exergy is always relative to the equilibrium state of the system with it's environment. 

$$E=(U-U_{0}​)+(V-V_{0}​)-(S-S_{0}​)$$
vs

$$B=(U-U_{0}​)+P_{0}​(V-V_{0}​)-T_{0}​(S-S_{0}​)$$

Where:

- $U_{0}$,$V_{0}$,$S_{0}$ ​: Internal energy, volume, and entropy at equilibrium with surroundings.
- $P_{0}$,$T_{0}$ ​: Ambient pressure and temperature.


## b. Engineers at Boxhall’s engineers have designed a new 5-passenger compact SUV with fuel economy in mind and have named it Boxhall Compact. The Boxhall Compact has a frontal area of 2.55 m2, a drag coefficient of 0.31, rolling resistance coefficient of 0.01, a weight of 1205 kg, maximum tractive force at low speeds of 2998 N, and tractive power at maximum speed of 30.5 kW. It has rear end space for storage. Assuming air density of 1.1 kg/m3, calculate: i. the tractive or cruising power requirement at 97 km/h [5 marks] ii. the maximum speed (you may use a spreadsheet solver tool e.g., Goal Seek or a programmable calculator) [5 marks] iii. the maximum gradeability and explain what it means [5 marks] iv. Time to reach 96 km/h accelerating from rest. (Assume acceleration in a vacuum with zero friction, and the maximum low speed traction force is maintained over the whole range of speeds) [4 marks