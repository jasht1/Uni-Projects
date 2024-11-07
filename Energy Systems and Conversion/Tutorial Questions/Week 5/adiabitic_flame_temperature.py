from pyromat import igtools as igt

fuel_mix = igt.IgtMix(C8H18=2, O2=25, N=25*3.7)
exhoust_mix = igt.IgtMix(CO2=16, H2O=18, N=25*3.7)

print (fuel_mix.h(T=25+273.15)[0])
print (exhoust_mix.h()[0])
print (fuel_mix.h(T=25+273.15)[0]-exhoust_mix.h()[0])

