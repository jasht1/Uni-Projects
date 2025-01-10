
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

