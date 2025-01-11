
#definition **Betz law** : is an estimate for the theoretical maximum continuous efficiency of an open flow turbine.

## Assumptions
%%[[2025-01-07]] @ 12:43%%

- Any non idealities of the turbine are assumed to lower it's efficiency.
- The volume considered must contain all incoming and outgoing flow. 
- The flow is incompressible. 
- Behaviour is, or is equivalent to being, radially uniform.

## Proof
%%[[2025-01-07]] @ 13:24%%

3 axial slices $n$ are considered:
1. $U$ : upstream of the rotor,
2. $T$ : at the rotor,
3. $D$ : downstream of the rotor,

each with their respective cross section area $A_{n}$ and flow speed $v_{n}$.

Conservation of mass implies mass flow rate at these 3 axial slices are equal:

$$\dot{m} = \rho A_{U}v_{U} = \rho A_{T}v_{T} = \rho A_{D}v_{D}$$

Where:
- $\dot{m}$ : is the fluids mass flow rate
- $\rho$ : is the the fluids density

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

### Finding velocity over the turbine in terms of initial and final velocity
%%[[2025-01-07]] @ 13:24%%

An alternate and equivalent equation for power can be found based on difference in kinetic energy upstream $U$ and downstream $D$, where kinetic energy is given by:

$$E = \frac{1}{2} m v^{2}$$

And power by accounting for mass flow rate $\dot{m}$ and change in velocity:

$$P = \frac{1}{2} \dot{m} \Delta v^{2}$$

Thus power at the turbine is also given by:

$$P = \frac{1}{2} \rho A_{T} v_{T} (v_{U}^{2} - v_{D}^{2})$$

By setting these identities as equal an identity for $v_{T}$ in terms of $v_{U}$ & $v_{D}$ can be found:

$$P = \rho A_{T} v_{T}^{2} (v_{U} - v_{D}) = \frac{1}{2} \rho A_{T} v_{T} (v_{U}^{2} - v_{D}^{2})$$

$$\begin{align*}
\cancel{\rho A_{T} v_{T}} v_{T} (v_{U} - v_{D}) &= \cancel{\rho A_{T} v_{T}} \frac{1}{2} (v_{U}^{2} - v_{D}^{2})\\
v_{T} \cancel{(v_{U} - v_{D})} &= \frac{1}{2} (v_{U} + v_{D}) \cancel{(v_{U} - v_{D})}\\
&\therefore \\
v_{T} &= \frac{1}{2} (v_{U} + v_{D})\\
\end{align*}$$

### Finding optimal velocity change
%%[[2025-01-10]] @ 00:40%%

Factoring in the identity for flow rate at the turbine found above back into the equation for power extracted from a wind stream gives:

$$\Large P = \frac{1}{4} \rho A_{T} (v_{1} + v_{2}) ({v_{1}}^{2}−{v_{2}}^{2})$$

This equation can be rearranged slightly to emphasise the impact of the proportional velocity drop, i.e. $\frac{v_{2}}{v_{1}}$, like so:

%% Original workings
$$v_{1} = \frac{v_{1}}{v_{2}}v_{2}$$
$$P = \frac{1}{4} \rho A_{T} \left( \frac{v_{1}}{v_{2}}v_{2} + v_{2} \right) \left( {\frac{v_{1}}{v_{2}}v_{2}}^{2}−{v_{2}}^{2} \right)$$

$$P = \frac{1}{4} \rho A_{T} {v_{2}}^{3} \left( \frac{v_{1}}{v_{2}} +1 \right) \left( \frac{v_{1}}{v_{2}}^{2}−1 \right)$$

$$P = \frac{1}{4} \rho A_{T} {v_{2}}^{3} \left( \frac{v_{1}}{v_{2}}^{3} + \frac{v_{1}}{v_{2}}^{2} - \frac{v_{1}}{v_{2}} - 1 \right) $$

*This explanation may be more intuitive if I factor $v_{1}$ out instead so it's clear power is proportional with wind speed cubed.*
%%

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

%% Workings
*integrate and take the stationary points in your range then plug it back into the equation or just slap it in wolfram alpha :shrug*
%%

Which occurs at $x = 1/3$ indicating a turbine must reduce the fluid velocity by $66.\dot{6}$% to extract the maximum continuous power from a fluid flow. Thus at max efficiency $v_{2} = v_{1}/3 \ @ \ \eta_{max}$.

### Finding max efficiency
%%[[2025-01-10]] @ 02:48%%

%% First Attempt
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

%%

%% Second attempt $\downarrow$ %%
Returning to the original equation for the power extracted:

$$P = \rho A_{T} v_{T}^{2} (v_{U} - v_{D})$$

Substituting static velocity for the average of upstream and downstream velocity by the identity proven in [[#Finding velocity over the turbine in terms of initial and final velocity]] gives power in terms of $v_{U}$ & $v_{D}$ as shown: 

$$v_{T} = \frac{1}{2} (v_{U} + v_{D})$$

$$P = \rho A_{T} {\left( \frac{1}{2} (v_{U} + v_{D}) \right)}^{2} (v_{U} - v_{D})$$

$$P = \rho A_{T} {\left( \frac{1}{2} (v_{U} + v_{D}) \right)}^{2} (v_{U} - v_{D})$$

%% *This totally simplifies to the $P = \frac{1}{4} \rho A_{T} (v_{1} + v_{2}) ({v_{1}}^{2}−{v_{2}}^{2})$ I used earlier* %%

Given that the maximum continuous power that can be extracted from a wind stream occurs when $v_{2} = v_{1}/3$ then this sets an upper bound for turbine efficiency $\eta_{\text{max}}$.

$$v_{D} = v_{U}/3 \ @ \ P_{\text{max}}$$

By substituting this identity the max power $P_{\text{max}}$ can be expressed solely in terms $v_{U}$ like so:

$$P_{\text{max}} = \rho A_{T} {\left( \frac{1}{2} \left(v_{U} + \left( \frac{v_{U}}{3} \right) \right) \right)}^{2} \left(v_{U} - \left( \frac{v_{U}}{3} \right) \right)$$

Similarly the total wind power can be taken as all of the kinetic energy being extracted thus leaving the downstream at 0 velocity $v_{2} = 0$:

$$P_{\text{wind}} = \rho A_{T} {\left( \frac{1}{2} \left(v_{U} + \left( 0 \right) \right) \right)}^{2} \left(v_{U} - \left( 0 \right) \right)$$

Giving a reasonable upper limit for efficiency as:

$$\Large \eta_{\text{max}} = \frac{P_{\text{max}}}{P_{\text{wind}}} = \frac
{\rho A_{T} {\left( \frac{1}{2} \left(v_{U} + \frac{v_{U}}{3} \right) \right)}^{2} \left(v_{U} - \frac{v_{U}}{3} \right)}
{\rho A_{T} {\left( \frac{1}{2} (v_{U} +  0) \right)}^{2} (v_{U} - 0)}$$

This can then be simplified down to:

$$\eta_{\text{max}} = \frac
{\cancel{\rho A_{T}} {\left( \frac{1}{2} \left(v_{U} + \frac{v_{U}}{3} \right) \right)}^{2} \left(v_{U} - \frac{v_{U}}{3} \right)}
{\cancel{\rho A_{T}}  {\left( \frac{1}{2} (v_{U}) \right)}^{2} v_{U}}$$

$$\eta_{\text{max}} = \frac
{{\left(\frac{v_{U}}{2} + \frac{v_{U}}{6}\right)}^{2} \left(v_{U} - \frac{v_{U}}{3} \right)}
{{\frac{v_{U}}{2}}^{2} v_{U}}$$

$$\eta_{\text{max}} = \frac
{{\left( \frac{{v_{U}}^{2}}{2^{2}} +\frac{{v_{U}}^{2}}{6^{2}} +\frac{2{v_{U}}^{2}}{2 \times 6} \right)} \left(v_{U} - \frac{v_{U}}{3} \right)}
{\frac{{v_{U}}^{3}}{2^{2}}}$$

$$\eta_{\text{max}} = \frac{4}{{v_{U}}^{3}} {\left( \frac{{v_{U}}^{2}}{4} +\frac{{v_{U}}^{2}}{32} +\frac{{v_{U}}^{2}}{6} \right)} \left(v_{U} - \frac{v_{U}}{3} \right)$$

$$\eta_{\text{max}} =
\frac{4}{{v_{U}}^{3}}\left( \frac{{v_{U}}^{3}}{4} +\frac{{v_{U}}^{3}}{32} +\frac{{v_{U}}^{3}}{6} \right) - \frac{4}{{v_{U}}^{3}}\left( \frac{{v_{U}}^{3}}{12} +\frac{{v_{U}}^{3}}{96} +\frac{{v_{U}}^{3}}{18} \right)
$$

%% *That was dumb I should have done $\frac{4}{{v_{U}}^{3}}$ before expanding* %%

$$\eta_{\text{max}} = 1 +\frac{1}{8} +\frac{2}{3} -\frac{1}{3} -\frac{1}{24} -\frac{2}{9} = \frac{36}{43} = 1.9\dot{4}$$

%% Great that didn't work, it's wrong in a new way now %%
