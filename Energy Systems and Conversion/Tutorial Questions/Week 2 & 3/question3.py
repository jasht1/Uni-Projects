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
