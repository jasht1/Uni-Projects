# Question 3
![[Week 2 - Entropy - TUTORIALS - w solutions.pdf#page=6|Week 2 - Entropy - TUTORIALS - w solutions, page 6]]
# Find Entropy change in Ideal Gas compression
%%[[2024-10-07]] @ 19:45%%

## Givens
%%[[2024-10-07]] @ 19:48%%

### Constants
Medium: Air

### Initial state
Pressure $P_{1}$: $100\ kPa$
Temp $T_{1}$: $17 \degree C$

### Final State
Pressure $P_{2}$: $600\ kPa$
Temp $T_{2}$: $57 \degree C$

## Property values
%%[[2024-10-11]] @ 17:57%%

```python
from pyromat import igtools as igt

## Givens
C_to_K = 273.15
air = igt.IgtMix(N2=0.76, O2=0.23, Ar=0.01)

# initial state
T_1=17+C_to_K
p_1=1

# final state
T_2=57+C_to_K
p_2=6

delta_s = air.s(T=T_1, p=p_1)[:] - air.s(T=T_2, p=p_2)[:]
print(delta_s)
```

`>> 0.38489145`

## Assumptions

$$s_{2}- s_{1} = s_{2}- s_{1} - R \ln (\frac{P_{2}}{P_{1}})$$

## Secondary Givens
%%[[2024-10-11]] @ 15:21%%

$R = 0.2870$

from [[thermodynamic property tables.pdf#page=29|thermodynamic property tables, page 29]]

