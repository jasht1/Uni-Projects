
## Slides
%%[[2024-10-24]] @ 12:59%%

[[Lecture 5 - Neural Computing.pdf]]

## Types of Synapse
%%[[2024-10-24]] @ 13:00%%

Synapses can be either excitatory or inhibitory. 
When stimulated:
- excitatory synapses: increase [[membrane potential]]
- inhibitory synapses : decrease [[membrane potential]]

##
%%[[2024-10-24]] @ 13:10%%

Weight matrix has the strength and by sign type of every connection between neurons.

$$\begin{matrix}
0 &  n_{1} \to n_{2} & ...  &  n_{1} \to n_{n}  \\
n_{2} \to n_{1} & 0 & ...  &  n_{2} \to n_{n} \\ 
...  & ... & 0 & ... \\ 
n_{n}\to n_{1} & n_{n} \to n_{2} & ... & 0
\end{matrix}$$

##
```matlab
dV = (-(V(i, t-1) - V_rest) + R_m * (I_ext(i) + I_syn)) * (dt / tau_m);
```
$$\dot V_{m} = (-(V_{m} - V_{rest}) + R_{m} * (I_{ext}(i) + I_{syn})) * (dt / \tau_{m})$$

## Want to see Neurons impact each other
%%[[2024-10-24]] @ 15:22%%

for this to happen either the current needs to be higher or impact for longer. The second is prefereable to maintain realism.

I will implement a slow rise and fall type spike, I do not need to generate the spike shape every time, the spikes follow a predictable shape with the [[SynapticRiseDecayVisualization.m]], have this function vary by a few parameters, and a little stochastic noise.

I can define each 