# PYroMat
%%[[2024-10-11]] @ 16:53%%

## Units
kJ, kg, Kelvin, bar

## Methods

| |Property|Units|
|---|---|---|
|cp|Const. pressure specific heat|unit_energy / unit_matter / unit_temperature|
|cv|Const. volume specific heat|unit_energy / unit_matter / unit_temperature|
|d*|Density|unit_matter / unit_volume|
|e*|Internal energy|unit_energy / unit_matter|
|gam|Specific heat ratio|Dimensionless.|
|h*|Enthalpy|unit_energy / unit_matter|
|mw|Molecular weight|unit_mass / unit_molar|
|p*|Pressure|unit_pressure|
|R|Ideal gas constant|unit_energy / unit_matter / unit_temperature|
|s*|Entropy|unit_energy / unit_matter / unit_temperature|
|T*|Temperature|unit_temperature|
|v*|Specific volume|unit_volume / unit_matter|
|x*|Quality (mp)|Dimensionless.|
|X|Mole fraction (igmix)|Dimensionless.|
|Y|Mass fractions (igmix)|Dimensionless.|


## Usefulls
### Mixes
`air = igt.IgtMix(N2=0.76, O2=0.23, Ar=0.01)`