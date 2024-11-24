## Question 2
### a) For each flow rate in your table, determine the COP of the system. 
[10 marks]

#### Background
[[coefficient of performance (COP)]] is a measure of performance typically associated with heat pumps and heating systems as a whole. In the case of Heat Pumps COP is the ratio of the useful heating power at the condenser per unit of electrical input power. [^1.4] $$COP = \frac{P \text{f} _{\text{Cond}}}{P_{\text{elec}}}$$
Where:
$P \text{f} _\text{Cond}$ : Heating capacity of the condenser ($kW$)
$P_{\text{elec}}$ : Input electrical power ($kW$)

Being a critical measure of energy efficiency there are strict and standardised methodologies for testing and calculating COP[^1.0]. On top of this manufacturer COP claims are often verified by 3rd party organisations via various certification schemes[^1.1] like KEYMARK[^1.2], Qlable and Eurovent[^1.3]. This is necessary as for COP values to be a useful in communicating system performance they must be comparable, like for like with other known values.

The measures available in this experiment are not sufficient to determine of electrical input power or the heating capacity of the condenser as such any approximation of COP will not be comparable with values taken in accordance with the standards and should not be taken as an example of how to calculate a Heat Pump's COP. 
The COP's calculated and discussed from this point onwards apply only within a system who's boundaries are defined: 
- Input: work done to refrigerant by the compressor
- Output: heat transferred to the coolant by the condenser

Making COP a measure of:
$$COP = \frac{Q _\text{Coolant} }{W_{\text{compression}}}$$
Where:
$Q _\text{Coolant}$ : heat transferred to the coolant by the condenser
$W_{\text{compression}}$ : work done to refrigerant by the compressor

[^1.0]: Heating systems and water based cooling systems in buildings. Method for calculation of system energy requirements and system efficiencies. Part 4-2. Space heating generation systems, heat pump systems, BS EN 14511‐3, 2018.
	[Download](http://libgen.li/ads.php?md5=4ce494840861f0e960bfb21a1088a59b)
[^1.1]: “EHPA Certification.” [Online]. Available: https://www.ehpa.org/quality/. [Accessed: 22-Nov-2024].
[^1.2]: “Testing and Certification.” [Online]. Available: https://keymark.eu/en/products/heatpumps/testing-and-certification. [Accessed: 22-Nov-2024].
[^1.3]: “NF414 | Eurovent Certita Certification.” [Online]. Available: https://www.eurovent-certification.com/en/third-party-certification/certification-programmes/nf414. [Accessed: 22-Nov-2024].
[^1.4]: Certification reference standard NF 414, AFNOR NF 414, 2024. Available: https://www.eurovent-certification.com/media/images/349/3c3/3493c319d9de88e18e3ecea2156c1e8d6521a7d4.pdf

#### Methodology
%%[[2024-11-24]] @ 13:44%%



%% 
#### Removed Sections

##### Approximating Condenser Power
If not measured directly the heating capacity of the condenser is calculated with the following formula [^1.4]: $$P \text{f} _\text{Cond} = \dot{m}_{\text{ff}} \times \left( h_\text{in} - h_\text{out} \right)$$
Where:
$P \text{f} _\text{Cond}$ : Heating capacity of the condenser ($kW$)
$\dot{m}_{\text{ff}}$ : flow of liquid refrigerant in ($kg/s$)
$h_\text{in}$ : enthalpy corresponding to the inlet pressure & temperature in ($kJ/k$)
$h_\text{out}$ : enthalpy corresponding to the inlet pressure & temperature in ($kJ/k$)

##### Approximating Compressor Power
%%[[2024-11-22]] @ 13:45%%

As the input electrical power $P_{\text{elec}}$ has not been measured directly an approximation will have to be made this is not ideal and will be a major source of uncertainty.

##### Details from [[R634 refrigeration cycle demonstration unit manual.pdf]]

> Hermetic type compressor with integral 1/2 Horsepower motor drawing approximately 810 Watts. The compressor is a single cylinder reciprocating type with a displacement of 17.4 cubic centimetres.

[[R634 refrigeration cycle demonstration unit manual.pdf#page=18&selection=7,0,42,12|R634 refrigeration cycle demonstration unit manual, page 18]]


|                                |     |     |
| ------------------------------ | --- | --- |
| Condenser Gauge Pressure (kPa) | 15  | 190 |
| Compressor Power Input (W)     | 274 | 302 |

[[R634 refrigeration cycle demonstration unit manual.pdf#page=60&selection=129,0,133,0|R634 refrigeration cycle demonstration unit manual, page 60, Table 9]]
%%

### b) Plot the COP against the saturation or condensing temperature. 
[10 marks]
