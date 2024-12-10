
## Other Ideas
### Old List
2023-09-30 @ 07:01 
![[EGR3024 project list student version.pdf]]

### My Ideas

2024-03-24 @ 20:43 
Battery recycling
	Writing a report to advocate for UK policy like [this](https://www.mdpi.com/2313-0105/9/7/360)
	inspired by [this video](https://www.youtube.com/watch?v=HW5b8_KBtT8)

A protocol for grid balancing and electricity exchange
	https://bmrs.elexon.co.uk/

Control systems for district heating with house

Grid forming inverter control system
	Could be modelled 

## Staff Project Proposals
%%[[2024-09-14]] @ 14:43%%

[Idea List](https://universityoflincoln-my.sharepoint.com/:x:/r/personal/phniknam_lincoln_ac_uk/_layouts/15/Doc.aspx?sourcedoc=%7B39EC4BC0-D924-486C-B7A1-23DB0CFCDEBA%7D&file=EGR3024-Staff%20project%20proposal-2425_R0.xlsx&action=default&mobileredirect=true)

### Preliminary reading
%%[[2024-09-14]] @ 14:45%%

[[2024-09-13|Yesterday]] I went through the list briefly, [[2024-09-14]] I want to pull out the ideas that appeal to me.

#### P5: Engineering and Medical Applications of Electrospun Materials: Integrating Machine Learning and Artificial Intelligence
%%[[2024-09-14]] @ 14:48%%

what is this on about? What dose AI have to Electrospun Materials? 

> [!QUOTE] Suggested Projects
> 1.	Electrospun Polymeric Bone Scaffolds with Bioactive Bone Regeneration
> 2.	Fabrication of Electrospun Vascular Grafts
> 3.	Application of AI in Designing Tissue Engineering Scaffolds
> 4.	Electrospun Filters: AI-Optimized Designs for Industrial Applications
> 5.	Deep Learning Techniques for Assessing Porosity and Fibre Diameter in Electrospun Scaffolds
> 6.	Machine Learning Techniques for Optimization of the Electrospinning Process
> 7.	Drug Delivery Optimization Using Machine Learning Techniques
> 8.	Electrical Conductivity of Electrospun Scaffolds
> 9.	Sustainable Food Packaging through Electrospun Fibre

#### P15: Nanoscale mechanical analysis of biological cells in diabetic nephropathy
%%[[2024-09-14]] @ 14:56%%

Mad! A whole other world of complexity. 

> [!QUOTE] Breif
>Diabetic nephropathy is a serious complication of diabetes resulting in end-stage kidney failure, a life-threatening condition that requires dialysis or kidney transplantation. Progression of the disease is associated with complex defects at the cellular and molecular level of the kidney’s filtering unit, the nephron. The condition ultimately leads to dysfunction of the tubular structure of the nephron that is responsible for filtration, with devastating effects for the organ.
> 
> This project focuses on the investigation of mechanical alterations of tubular cells, which are responsible for the structural integrity of the nephron. Nanomechanical analysis at single cell level in healthy and diseased conditions, contains valuable information about the dynamic behaviour of the cellular network, called the cytoskeleton, which maintains the physiological structure of cells. Analysis of the mechanical changes of the cytoskeleton in diabetic nephropathy can lead to novel understanding of the disease and development of single cell diagnostics and therapies related to nanomedicine.
> 
> However, due to the intricate nature of the cell at the molecular level, mechanical data are often complex, requiring fine processing, iterative modelling and sound statistical analysis. The aim of this project is to quantify mechanical properties of biological cells in healthy and diseased states by developing analytical methods to process nanoscale force-displacement measurements and calculate the mechanical properties of cells using mathematical models. The experimental data are available in a raw form and tasks include fine processing of nanoscale data, numerical analysis, development of data sets and statistical comparison between two or more variables. The results of the statistical analysis will be associated with the underlying molecular changes of the cytoskeleton during diabetic nephropathy and the potential for mechanical diagnostic information at the cellular level will be addressed.

If I understand this correctly this involves applying engineering principles to model the behaviour of healthy vs permuted tubular cells. 

A fascinating challenge surely but is it one I can feasibly take on?

##### Recommended reading

Section, TGF-β1 significantly  
increases single cell stiffness:  
https://www.sciencedirect.com/science/article/abs/pii/S1549963415006073?via%3Dihub  
Section, Hertz Model:  
https://link.springer.com/article/10.1007/s12195-0

#### P23: The generation of a low voltage high quality three-phase supply waveform
%%[[2024-09-14]] @ 15:44%%

Yes! This might be exactly what I'm looking for!

> [!QUOTE] Breif
> In order to test a symmetrical component filter a good quality three-phase waveform is required. Three-phase voltage waveforms in buildings, even when reduced to low voltage using a transformer tend to be unequal (due to unbalanced loads) and distorted (due to the presence of non-linear loads).

I do think Grid forming inverters are a huge area of potential, and would be so valuable in a world without stable large electrical grids. This would be an opportunity to get a firm grasp on the underlying concepts with a bunch of tabletop experimentation!

##### Recommended Background reading
[Wildi, T.: Electrical Machines, Drives and Power Systems](https://archive.org/details/electrical-power-technology-wildi-theodore/page/81/mode/2up)

[Mancini, R.: Op Amps for Everyone: Design Reference](https://web.mit.edu/6.101/www/reference/op_amps_everyone.pdf)

#### P25 Detecting unbalanced loads on a motor

> [!QUOTE] Brief
> Motors running with unbalanced loads may fail due to a variety of mechanical or electrical problems. Being able to detect unbalance and act on this could increase motor life.

An unbalanced load on a 3 phase motor will appear as reactive power.
Unbalanced loads will likely cause harmonic behaviour, this will distort the observable ractive power in relation to the actual load.
A control system would have to adapt the control signal to the motor in line with the actual load. this will require an algorithm that detects the possible load imbalances that 

#### P30: Model the effect of increasing the proportion of bioethanol in pump petrol on greenhouse gas emissions from personal transport in the UK

Interesting research problem.

> [!QUOTE] Breif
> Pump petrol is current 10% bioethanol. If the proportion was increased, what effect would it have on the environmental impact of driving a car?
> 
> What is the limit of addition of ethanol to pump fuel before engine modifications are needed? Where can sufficient quantities of bioethanol be sourced? You are expected to construct a quantified model of the effects of the addition of bioethanol to pump petrol.


#### P37: Drone/Robotic Empowered Communication Systems

> [!QUOTE] Breif
> Short Description: There has been an increasing interest in the exploitation of mobility and mobile robots (MRs) to improve the communication performance of wireless sensor networks (WSNs), e.g. routing, energy balancing, and improving security. MRs can also be used as data ferries to collect data from sensor networks. This is a suitable solution to reduce the energy consumption of the WSN when the sensing nodes are located far from the fusion center (FC), and the sensors are powered by batteries. 

That's cool, the drones can fly out over the sensors to receive lower power signals than would otherwise be necessary. They could also play a role in recharging the sensor stations if they dock there.
