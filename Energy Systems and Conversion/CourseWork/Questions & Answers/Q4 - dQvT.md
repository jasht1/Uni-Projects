
## Question 4
### a) Plot the evaporator and condenser heat transferred against temperature 
[10 marks]

![[dQvT_graphs.svg]]

### b) Discuss the trend and any other observations. 
[10 marks]

On first inspection, the trends between heat transfer rate and phase change chamber temperature are not obvious in either the evaporator or condenser as they are not particularly strong, with Pearson pairwise correlations of close to -0.5. Specifically -0.52 and -0.49 for the evaporator and condenser respectively. This is to say the data suggests a weak negative correlation between the heat transfer rate and the temperature of the phase change chamber.

%%
It is tempting to provide the explanation that the te

The pump always provides the same amount of power - false

The refrigerant flow rate is constant - false
%%

It would be intuitive to assume that the rate of heat transfer is proportional to the temperature gradient between the phase change chamber and the thermal reservoir, and that, increasing the flow rate will increase the temperature gradient. However, as can be seen below, the experimental data shows only a very loose correlation. *(note the negative axes)*

![[dQ_v_Tgradient-(mfr).svg]]

%% why? %% 

The foundational assumption is correct that increasing the flow rate minimises the temperature change across the coil. Each gram of water is being exposed to the chamber for fewer seconds and therefore absorbing fewer Joules of energy and less energy added per unit mass means less temperature change. This is confirmed by the exponentially diminishing temperature with flow rate in the condenser graph below. 

![[dT_v_mfr-(fit).svg]]

However as can be seen by the colouring in the graphs below the relationship between temperature change across the coil and the temperature gradient is not as simple.

![[dT_v_mfr-(Tg).svg]]

This is because as the faster flow decreases the temperature of the coolant it can absorb more energy than is being released by the refrigerant as latent heat and therefore it also decreases the temperature of the chamber. This in turn means the compressor must provide a higher pressure requiring more power.

![[Tcoolant_v_Tchamber-(mfr).svg]]

Maximising the energy transfer is usually not the only objective. In the case of a heat pump the lower grade heat provided by a higher flow rate may be undesirable as not only dose it make the system and it's plumbing louder and more energy intensive but the output temperature might be too low to be useful.
