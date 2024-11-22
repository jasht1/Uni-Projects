## Question 2
### a) For each flow rate in your table, determine the COP of the system. 
[10 marks]

#### Background
[[coefficient of performance (COP)]] is a measure typically associated with heat pumps. Being a critical measure of energy efficiency there are strict and standardised testing regimes[^1.0] and manufacturer COP claims are often verified by 3rd party organisations via various certification schemes[^1.1] like KEYMARK[^1.2], Qlable and Eurovent[^1.3]. 
COP is the ratio of useful heating energy produced per unit of electrical input power.[^1.4] $$COP = \frac{P \text{f} _{\text{Cond}}}{P_{\text{elec}}}$$
Where:
$P \text{f} _\text{Cond}$ : Heating capacity of the condenser ($kW$)
$P_{\text{elec}}$ : Input electrical power ($kW$)

%%
If not measured directly the heating capacity of the condenser is calculated with the following formula [^1.4]: $$P \text{f} _\text{Cond} = \dot{m}_{\text{ff}} \times \left( h_\text{in} - h_\text{out} \right)$$
Where:
$P \text{f} _\text{Cond}$ : Heating capacity of the condenser ($kW$)
$\dot{m}_{\text{ff}}$ : flow of liquid refrigerant in ($kg/s$)
$h_\text{in}$ : enthalpy corresponding to the inlet pressure & temperature in ($kJ/k$)
$h_\text{out}$ : enthalpy corresponding to the inlet pressure & temperature in ($kJ/k$)
%%

[^1.0]: Heating systems and water based cooling systems in buildings. Method for calculation of system energy requirements and system efficiencies. Part 4-2. Space heating generation systems, heat pump systems, BS EN 14511‐3, 2018.
	[Download](http://libgen.li/ads.php?md5=4ce494840861f0e960bfb21a1088a59b)
[^1.1]: “EHPA Certification.” [Online]. Available: https://www.ehpa.org/quality/. [Accessed: 22-Nov-2024].
[^1.2]: “Testing and Certification.” [Online]. Available: https://keymark.eu/en/products/heatpumps/testing-and-certification. [Accessed: 22-Nov-2024].
[^1.3]: “NF414 | Eurovent Certita Certification.” [Online]. Available: https://www.eurovent-certification.com/en/third-party-certification/certification-programmes/nf414. [Accessed: 22-Nov-2024].
[^1.4]: Certification reference standard NF 414, AFNOR NF 414, 2024. Available: https://www.eurovent-certification.com/media/images/349/3c3/3493c319d9de88e18e3ecea2156c1e8d6521a7d4.pdf

As the input electrical power $P_{\text{elec}}$ has not been measured directly an approximation will have to be made this is not ideal and will be a major source of uncertainty.


#### Compressor
%%[[2024-11-22]] @ 13:45%%

##### Details from [[R634 refrigeration cycle demonstration unit manual.pdf]]

> Hermetic type compressor with integral 1/2 Horsepower motor drawing approximately 810 Watts. The compressor is a single cylinder reciprocating type with a displacement of 17.4 cubic centimetres.

[[R634 refrigeration cycle demonstration unit manual.pdf#page=18&selection=7,0,42,12|R634 refrigeration cycle demonstration unit manual, page 18]]


|                                |     |     |
| ------------------------------ | --- | --- |
| Condenser Gauge Pressure (kPa) | 15  | 190 |
| Compressor Power Input (W)     | 274 | 302 |

[[R634 refrigeration cycle demonstration unit manual.pdf#page=60&selection=129,0,133,0|R634 refrigeration cycle demonstration unit manual, page 60, Table 9]]

### b) Plot the COP against the saturation or condensing temperature. 
[10 marks]
