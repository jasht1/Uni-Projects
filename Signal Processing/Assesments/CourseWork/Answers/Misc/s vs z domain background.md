
The $s$ and $z$ variables and their respective domains allow engineers to analyse both linear and oscillatory system dynamics intuitively. The $s$-domain is well suited for the analysis of analogue systems operating in continuous time where the $z$-domain suits digital systems in discrete time steps.
$$\large s = \sigma + j\omega \qquad z = r e^{j\Omega}$$
The $s$ variable exists in a Cartesian space with it's real part $\sigma$ representing exponential growth, or decay if negative, and it's imaginary component $j\omega$ representing oscillations and their frequency. A systems natural modes sum to determine how it will react to any kind of input and can be understood by where it's poles lay in the $s$-domain. 
A system with a positive real component grows exponentially out of control but the more negative it is the faster it will settle down. Likewise large imaginary poles indicate a tendency for the system to oscillate violently whereas a system with small imaginary components will have slow manageable oscillations. In filter design, the precise placement of poles allows for deliberate shaping of the system's frequency response. For example, placing poles closer to the imaginary axis allows narrowband filters with sharp frequency selectivity, while placing them farther left results in smoother, faster-decaying filters. 
In contrast the $z$ variable is a polar coordinate where the exponential growth/decay is captured by the radius $r$ and the frequency is represented by the angle $\Omega$. Similarly to the $s$-domain Poles with low $\Omega$ near the real axis correspond to lower frequency behaviour and those further away correspond to higher frequency oscillations. In contrast the rate of decay decreases with distance from the origin with stability is indicated by whether the pole exists inside the unit circle.
This can be seen in [Fig 1](#Figure%201%20s-domain%20Impulse%20Response), [Fig 2](#Figure%202%20s-domain%20Frequency%20Response), [Fig 3](#Figure%203%20z-domain%20Impulse%20Response) and [Fig 4](#Figure%204%20z-domain%20Frequency%20Response) below showing various $s$ and $z$ poles with their implied impulse response and magnitude vs frequency response. The code for which can be found in annex !%% annex num %%.

%%
| ![400](s_Impulse_Response.svg)                | ![400](s_MagvFreq_Response.svg)                 |
| --------------------------------------------- | ----------------------------------------------- |
| ![z_Impulse_Response](z_Impulse_Response.svg) | ![z_MagvFreq_Response](z_MagvFreq_Response.svg) |
%%


--- start-multi-column: ID_51ek
```column-settings
Number of Columns: 2
Largest Column: left
Border:off
Shadow:off
```


###### Figure 1: s-domain Impulse Response

![|500](s_Impulse_Response.svg)

--- column-break ---

###### Figure 2: s-domain Frequency Response

![|300](s_MagvFreq_Response.svg) 

--- end-multi-column







--- start-multi-column: ID_mqhl
```column-settings
Number of Columns: 2
Largest Column: right
Border:off
Shadow:off
```

###### Figure 3: z-domain Impulse Response

![z_Impulse_Response|300](z_Impulse_Response.svg)

--- column-break ---

###### Figure 4: z-domain Frequency Response

![z_MagvFreq_Response|500](z_MagvFreq_Response.svg)

--- end-multi-column

