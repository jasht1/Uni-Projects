---
title: Nanomechanical Analysis of Renal Tubular Cell Cytoskeleton for the Detection of Renal Disease
subtitle: 
titlepage-logo: /home/joe/Documents/Obsidian/SuperVault/Core/Templates/Pandoc/attachments/UoL_logo.png
author: Joseph Ashton
authors:
  - name: Joseph Ashton
    affiliation: School of Engineering
    institution: University of Lincoln
    email: 27047440@students.lincoln.ac.uk
    address: Lincoln
acknowledgements: I would like to thank my patient amd knowledgable suporvisor Eleftherios Siamantouras
declaration: ""
abstract: This project investigates changes in mechanical properties of kidney cells when exposed to TGF-$\beta 1$, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. The aim of this project is to provide insight on the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy.
---

## Introduction 


The mechanical properties of cells are finely tuned to their function, especially epithelial cells who's core role is to form active structural surfaces where correct functioning is a direct result of appropriate strength, stiffness, and shape. In patients suffering from diabetic nephropathy the alterations in renal tubule cell properties are directly associated with progression of the disease and further kidney damage. Increased renal tubule cell stiffness has been observed in association with renal disease and may have potential as a biomarker for diagnosis or drug development. This report will investigate a potential method for associating observed cell stiffness with progression of renal disease.  

The progress of this project can be broken down into 4 successive objectives summarised in the boxes below, the methodology and results sections will reflect this structure.

![](Methodology%20Summary%20Blocks.png)

## Background





### Relevant Physiology

%% #### Kidney %%

The human body can be understood as a complex biological machine, made up of many sub-mechanisms familiar to engineers. In this sense the filtration system of the human body is referred to as the renal system, in which the kidneys are a component about the size of a clenched fist that can be likened to a sophisticated water treatment plant combined with a feedback-controlled chemical processing unit. Each contain roughly a million multi step filter loops called nephrons [@bertramJF2011-HumanNephronNumber].  

![ Labeled Kidney and Nephron form National Institute of Diabetes and Digestive and Kidney Diseases, National Institutes of Health [@niddk-KidneyNephronLabeled]](Kidney%20and%20nephron%20-%20Labeled.jpg)


%% #### Nephrons %%

The nephrons are selective, able to remove waste products while keeping desirable substances in the blood. They are able to regulating essential substances such as water, electrolytes, and pH levels to strict set points. [@ogobuiroI2025-PhysiologyRenal]

%% #### glomerulus %%

The the first step unfiltered blood enters the glomerulus and if forced through several membrane filters by hydro-static pressure. The first layer permits all solutes blocking only cells. The next is negatively charged thus blocking proteins like albumin. The final layer modulates the flow resistance to vary the hydro-static pressure gradient, this will be counter balanced by the osmotic pressure such that it can be used to effectively vary the ultra filtration coefficient. [@pavenstadtH2000-RolesPodocyteGlomerular; @ogobuiroI2025-PhysiologyRenal] Leaving the glomerulus is a blood vessel containing only cells and proteins and a fractional remainder of the other solute, and the tubule carrying all the removed solute [@lumen-NephronStructure].

%% #### Tubule %%

The glomerulus is an overly aggressive filter; much of the water and solute must be re introduced to the blood from the tubules. %%in several stages. The first stage, the proximal convoluted tubule (PCT) pumps all the glucose and amino acids as well as most of the sodium and water back into the blood [@ogobuiroI2025-PhysiologyRenal]. In the next more water is reabsorbed, and in the final the remainder of the sodium as well as potassium and chlorides get reabsorbed via osmosis [@ogobuiroI2025-PhysiologyRenal]. %% The tubules run along side blood vessels and using a combination of osmosis, active transport and controlled ionic gradients %%sodium, potassium, calcium, magnesium, chlorides%% the valuable ions and most of the water is reabsorbed over several uniquely specialised segments [@ogobuiroI2025-PhysiologyRenal].  

%% #### Tubule cell %%

![Diagram of tubule, tubule wall and tubule cell structure](Tubule%20zoom%20diagram.png)
> Simplified diagram of tubule, tubule wall and tubule cell structure.

The structure of the tubule varies significantly across it's length to as different sections are specialised to permeate different resources, the lumen diameter and epithelial cell height values are averages of random samples [@morozovD2021-MappingKidneyTubule]. 

%% Breakdown of the layers and cell types #WIP  %%

Epithelial tubule cells are the essential building blocks of tubules. They are anchored to each other and to the extra cellular matrix (ECM) by junctions tied to their cytoskeleton [@yuASL2013-Chapter12Intercellular; @zihniC2016-TightJunctions]. In this way the cytoskeleton plays an essential role in maintaining the structure of both the individual cells and the larger structure. 

%% cytoskeleton %%



### Diabetic Nephropathy (DN)

%% #### Summary %%
Diabetic nephropathy (DN) is a common and serious complication of diabetes resulting in kidney failure due to progressive damage to the nephrons, the functional units of the kidney responsible for filtering the blood.

%% #### Epidemiology & Prognosis %%
Diabetic nephropathy develops in 30-40% of people with diabetes after 15-20 years, as the disease progresses the damage accumulates and mortality rate rises [@vargheseRT2025-DiabeticNephropathy]. Based on the risk factor of the patient treatments range from lifestyle changes and medications, to renal replacement which involves dialysis or transplantation [@vargheseRT2025-DiabeticNephropathy].

%% Stats about the number of people with it and dying of it and how that is changing over time %%

%% connecting line from mortality to pathophysiology %%

%% #### Relevant Pathophysiology %%
In type 1 diabetes a lack of insulin and in type 2 Insulin resistance cause chronic hyperglycemia a condition where there is too much glucose in the blood. Hyperglycemia causes an increased build up of reactive oxygen species (ROS) this ongoing oxidative stress causes chronic inflammation [@gonzalezP2023-HyperglycemiaOxidativeStress].

Inflammation increases production of cytokines, including TGF-$\beta 1$, which trigger Epithelial to Mesenchymal Transition (EMT) [@hillsCE2012-TGFvModulatesCelltocell; @pizzinoG2017-OxidativeStress]. EMT is a process where cells which make up structural and functional surfaces (epithelial) transition into repair/maintenance cells (mesenchymal) [@kalluriR2009-BasicsEpithelialmesenchymalTransition]. In this case tubular epithelial, cells which make up the fine vessels of the kidney that filter blood, transform into myofibroblasts, repair and maintenance cells %% or undergo apoptosis (cell death) %% [@iwanoM2002-EvidenceThatFibroblasts]. This is the underlying mechanism of fibrosis, which induces atrophy and scarring in the tubules %% and results in intraglomerular hypertension %% causing progressive kidney damage [@metcalfeW2007-HowDoesEarlyChronicKidneyDiseaseProgress].




### Atomic Force Microscopy (AFM)

%% #### What is AFM? %%

Atomic Force Microscopy (AFM) is a technique for characterising nanomechanical properties and structure. It is well suited to microbiology as it allows for the study of live cells [@kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 

Atomic force microscopes use the deflection of a very fine probe on a flexible cantilever to detect contact forces ranging form nano to micro Newtons. There are a myriad of applications and operating modes of AFM [@dufreneYF2002-AtomicForceMicroscopy] but this report is primarily concerned with nano indentation. This involves advancing a fine tipped probe on the end of the cantilever into a sample cell producing a force over indentation depth curve, from which the elasticity of the cell can be calculated using a Hertz contact model [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces].

%% #### functional/mechanical description %%

The typically atomic force microscope utilise a laser focused on the free end of the cantilever such that any deflection of the probe produces an amplified deflection of the reflected beam, this is recorded by a position sensitive photodiode [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces]. 

![Atomic force microscope functional diagram](Atomic%20Force%20Microscopy%20-%20mechanism%20diagram.png)

The sample once mounted to the sample stage can be manoeuvred precisely in relative to the probe by applying voltage to piezoelectric actuators [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @giraudF2019-PiezoelectricActuatorsIntroduction] this is how the sample is advanced into the tip. Once calibrated the voltage at the actuators gives the sample stage position and the voltage at the photodiode gives the deflection of the probe, with this a force displacement curve can be produced by accounting for the stiffness of the cantilever and the relative displacement [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials].

%% #### typical force displacement curve %%

A typical force displacement curve from a nano indention experiment has the following shape seen in figure %% #WIP %% (A) below. A broadly level region where the probe is not in contact with the cell; the contact region; a sloped region where the probe is indenting the cell; the turnaround point; from which the same is repeated in reverse differing mainly at the point of separation [@kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 


--- start-multi-column: ID_orvl
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Example AFM data from Radmacher 2007 shows the curve as a whole [@radmacherM2007-StudyingMechanicsCellular]](fdcurve%20figure%20A%20-%20radmacherM2007-StudyingMechanicsCellular.png)


--- column-break ---


![Example AFM data from Radmacher 2007 zoomed into the contact / separation region [@radmacherM2007-StudyingMechanicsCellular]](fdcurve%20figure%20B%20-%20radmacherM2007-StudyingMechanicsCellular.png)


--- end-multi-column


%% Contact point jump %%


The exact point of contact is often ambiguous and rarely the same as the the point of separation. On approach the cantilever will be deflected away from the cell by Van Der Waals forces until the spring force of the cantilever overcomes and surface tension takes hold [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials]. The point of separation is typically clearer as it's associated with a "jump" in cantilever deflection as the surface tension / adhesion of the cell to the probe is overcome [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials].




### Contact Mechanics

In order to calculate elasticity the experimental data must be fit to a theoretical mechanical model of the interaction. Below is a table outlining different model indention relationships.


\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.0470}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.4133}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.5397}}@{}}
\toprule\noalign{}
\begin{minipage}[b]{\linewidth}\raggedright
Model
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Force-Indentation relationship
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Scope
\end{minipage} \\
\midrule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Hertz & \(F = \frac{4}{3}E' \sqrt{R} \ \omega^{3/2}\) & Hertz model
approximates the shallow indention of two linearly elastic spheres with
infinitesimal strains {[}21{]}, {[}22{]}, {[}23{]}. \\
DMT &
\begin{minipage}[t]{\linewidth}
\begin{equation*}
\begin{aligned}
F &= F_{\text{Hertz}} - F_{\text{det}} \\
\delta &= \frac{a}{2} \ln \left( \frac{R_i + a}{R_i - a} \right)
\end{aligned}
\end{equation*}
\end{minipage}
& Depending on the depth of indentation and the material interaction it
can be important to account electrostatic non contact forces, the
influence of which can be modelled using the Derjaguin approximation for
interaction potential {[}19{]}, {[}23{]}. \\
Fung &
\begin{minipage}[t]{\linewidth}
\begin{equation*}
\begin{aligned}
F = &B\pi \left( \frac{N(a)}{D(a)} \right)
\exp\left[ b \left( \frac{E(a)}{F(a)} \right) \right] \\ \\
N(a) &= a^5 - 15Ra^4 + 75R^2a^3 \\
D(a) &= 5Ra^2 - 50R^2a + 125R^3 \\
E(a) &= a^3 - 15Ra^2 \\
F(a) &= 25R^2a - 125R^3 \\
\end{aligned}
\end{equation*}
\end{minipage}
& An exponential strain energy function based on mechanical testing of
mesentery and arterial tissues, that models the non linear elasticity of
cells {[}22{]}, {[}24{]}. This method is tangebly more precise but
doesn't provide a simple value for young's modulus. \\
\end{longtable}


%% Expand on obstacles with applying contact mechanics models to cells %%

%% 
Full Fung equation 
$$F = B\pi (\frac{a^5- 15Ra^4 + 75R^2a^3}{5Ra^2- 50R^2a + 125R^3})\text{exp}[b(\frac{a^3- 15Ra^2}{25R^2a- 125R^3})]$$
Thinner Fung equation
$$
\begin{align*}
N(a) &= a^5 - 15Ra^4 + 75R^2a^3 \\
D(a) &= 5Ra^2 - 50R^2a + 125R^3 \\
E(a) &= a^3 - 15Ra^2 \\
F(a) &= 25R^2a - 125R^3 \\
\\
F =\ &B\pi \left( \frac{N(a)}{D(a)} \right) \exp\left[ b \left( \frac{E(a)}{F(a)} \right) \right]
\end{align*}
$$ 
$$ \begin{align*} N(a) &= a^5 - 15Ra^4 + 75R^2a^3 \\ D(a) &= 5Ra^2 - 50R^2a + 125R^3 \\ E(a) &= a^3 - 15Ra^2 \\ F(a) &= 25R^2a - 125R^3 \\ \\ F =\ &B\pi \left( \frac{N(a)}{D(a)} \right) \exp\left[ b \left( \frac{E(a)}{F(a)} \right) \right] \end{align*} $$ 
%%

%% Better Table

%%

Given the focus of this investigation is the elastic response of the cell membrane the non contact forces are relatively small and can be ignored by reducing the fitting strictness close to the contact point. The difference between the traditional Hertzian models and the power series approximations are not significant enough to justify the increased complexity in this case.

## Literature Review

Developments in both understanding %% of the pathophysiology %% of kidney disease and the application of atomic force microscopy (AFM) technology [@liuS2024-AtomicForceMicroscopyDisease-relatedStudies; @dufreneYF2002-AtomicForceMicroscopy] may provide a valuable measure of the progression of kidney failure to inform the research and development of novel therapies [@parrishAR2016-CytoskeletonNovelTarget].

%% #### What we measure %%

%% Single cell stiffness %%
The mechanical properties of tubular cells are largely a result of their cytoskeletal structure [@jalilianI2015-CellElasticityRegulated; @radmacherM2007-StudyingMechanicsCellular] which is altered significantly with the progression of DN [@buckleyST2012-CytoskeletalRearrangementTGFv1induced]. 

%% Inter cellular adhesion %%

%% The stiffness of individual cells can be observed and correlated with the [@siamantourasE2016-QuantifyingCellularMechanics]. %%

%% #### Obstacles & limitations %%

%% Cell cultures aren't perfect representations of their in vitro counterparts. This can be improved with careful preparation. The elasticity of the substrate the culture is grown on can have a significant impact on cytoskelital arrangement [@wangD2022-KidneyProximalTubule] [loveH2018-SubstrateElasticityGoverns]  %%

%% Table with papers and a relevant summary #WIP %%

The below table lists several papers utilising atomic force microscopes to produce force displacement curves from a bead tipped cantilever fitted to a hertz contact model to find cell elasticity.

| Paper                                                               | Cell Type                                                                            | Scope                                                                                                                                                                          | Cell Elasticity                                                                           |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Siamantouras 2016 [@siamantourasE2016-QuantifyingCellularMechanics] | HK2: immortalised human kidney proximal tubule  epithelial cell culture              | Over 30 cells each indented 5 times immediately above the nucleus producing over 150 curves.                                                                                   | control: $320 \ \text{Pa}$ <br>cells treated with TGF-$\beta 1$: $549 \ \text{Pa}$    |
| Jafari 2024 [@jafariA2024-MechanicalPropertiesHuman]                | HEK-293: immortalised human embryonic kidney cell culture                            | did not elaborate                                                                                                                                                              | $539.8 \ \text{Pa}$                                                                       |
| Shimizu 2012 [@shimizuY2012-SimpleDisplaySystem]                    | HEK-293: immortalised human embryonic kidney cell culture                            | The median of value of over 100 cells examined at 25 points each.                                                                                                              | mode value ($x_{0}$): $410 \ \text{Pa}$ <br>variance ($w$): $0.757$                       |
| Buckley 2012 [@buckleyST2012-CytoskeletalRearrangementTGFv1induced] | A549: human lung alveolar carcinoma epithelial cell culture                          | On each cell, a $4 \times 4$ grid of force-distance curves was collected in at least 5 different positions (avoiding the nucleus and the very edge) producing over 750 curves. | On Glass: 8300 $\pm$ $1100 \ \text{Pa}$<br>On collagen I: $9100 \ \pm$ $2900 \ \text{Pa}$ |
| Wyss 2011 [@wyssHM2011-BiophysicalPropertiesNormal]                 | Sprague-Dawley rat kidney glomeruli capillary wall extracted by differential sieving | 10 different glomeruli with 10 measurements each                                                                                                                               | $2,300 \ \pm$ $160 \ \text{Pa}$                                                           |



## Methodology


### Experimental Method


The experimental procedure used to produce the data used in this report is detailed thoroughly in reference [@siamantourasE2016-QuantifyingCellularMechanics]. Cells of the adult human proximal tubule kidney (HK2) cell line [@ryanMJ1994-HK-2] where purchased from the American Type Culture Collection (ATCC; Gaithersburg,  MD 20878 USA). These where maintained in Dulbecco's Modified Eagle Medium/Nutrient Mixture F-12 (DMEM/F12), 10% fetal calf serum (FCS), glutamine ($2 \ \text{mM}$), and EGF ($5 \ \text{ng/ml}$) for 48 hours. The cells where divided into 2 test groups, the "control" group and the "treated" group which where where serum starved overnight before being exposed to TBF-$\beta$, an E-cadherin antibody obtained from R&D systems, at ($10 \ \text{ng/mL}$) for a further 48 hours. 

The indentation experiments where carried out using a JPK Instruments CellHesion©200 module with a BioCell™ temperature controller to maintain a bed temperature of $37 \degree \text{C}$ on a TMC 63-530 anti-vibration table. Probes where constructed by attaching $11\ \micro \text{m}$ Polyscience PolyBeads® to Nanoworld TL-1 tipless cantilevers with a force constant of $0.03 \text{N/m}$. Each cell was indented 5 times directly above the nucleus at a constant speed of $5\ \micro \text{m / s}$ with intervals of 60 seconds. For each set of experiments the spring constant of the cantilever was calibrated using the thermal noise method and the cell's height was measured to determine an appropriate indentation depth to minimise the influence of the hard basal substrate. 

%% thermal noise method how and why %%



### Elasticity Modeling


%% How did i get ym values from the datasets %%

Experimental data was received in the form of `.jpk-force` logs of head height position against vertical deflection force along with experimental metadata. The JPK data processing software was used to calculate the probe height based on spring constant and at this point the curves where exported in text form. In order to establish "trustworthy" values for YM the function included in the JPK data processing software was used with the deepest point of indentation to $1 \ \micro m$ past the contact point as upper and lower bounds. This was then replicated for the text exports in python using `nanite` an open source package that offers the same Hertz/Sneddon elasticity model truncated power series approximation for spherical indenters with a difference in fit optimisation methods; where JPK Data Processing uses least squared regression, Nanite utilises machine learning for fit quality estimation and optimisation. Despite not providing the "trustworthy" JPK fits as a rated training dataset Nanite reproduced the YM estimations with an average deviation of less than ±0.05%. The Hertz parabolic indenter model was also tested and compared with the Hertz/Sneddon approximation. All force indentation curves where plotted alongside those implied by the fitting along with the residual fitting error to identify potential anomalies or systematic error. Attention was paid to identify any consistent trends in the residual as If the residual where to consistently deviate from generally flat noise at 0 this would imply a poorly matched elasticity model.

%% How did I determine the appropriate cell YM given the experimental data %%

As each cell was tested 5 times the apparent YM of a cell was taken to be the average average  of the Hertz/Sneddon fits. To validate the results the force indentation curves of the experiments and the implied curve of the apparent YM where plotted and inspected visually checking for cell relaxation or systematic error based on observable trends in successive experimentation or any apparent anomalies. In addition the 95% confidence interval of the apparent cell YM was calculated for the natural set and a $100 \times$ bootstrapped super set and these metrics where inspected to assert whether the apparent YM given by the average is a fair representation of the cell behaviour.

%% Confidence Intervals, what are they and how did I calculate them %%

As the apparent cell YM was taken to be the mean it's confidence intervals where those of the mean YM for the set of cell tests. 

$$\text{CI}_\mu = \left[ \mu - t^* \cdot \frac{\sigma}{\sqrt{n}},\ \mu + t^* \cdot \frac{\sigma}{\sqrt{n}} \right]
\qquad
\text{CI}_\sigma = \left[ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{upper}}} },\ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{lower}}} } \right]
$$

Where confidence intervals where calculated for the standard deviation as is later necessary in determining the confidence in the group classifications and when montecarlo sampling, the chi distribution is used. This was originally tried using normal distributions being a generally acceptable approximation, however given the small and bottom biased experiment sample sets symmetric distribution of probable standard deviations was not a fair representation.

%% Bootstrapping, what is it, why did I do it %%



### Classification Method

A Bayes classifier was constructed to quantify the probability of diabetic nephropathy from cell stiffness based on the effect observed in the experimental data. The control group is taken as a model of healthy cell presentation and the treated group representing the onset of diabetic nephropathy. Similarly to how cell properties where estimated from several tests, the typical group properties are estimated from several cells, conversely it can also be found by taking the averages and standard deviations of the whole dataset. It is often the case that considering the whole raw dataset provides more accurate picture of the group, however in this case it is appropriate to consider by subgroups i.e. by cells, this is because the samples are not independent and not representative of the test case. As it has been observed that successive tests are not introducing systematic error their average provides a more accurate estimation of the given cell, thus classification should be considered at the cell level.

$$
{\Large  
P(G \mid x) = \frac{P(x \mid G) \mid \cdot P(G)}{P(x)}  
}  
\qquad  
\begin{align}  
P(G \mid x) &:: \text{Posterior Probability}\\
P(x \mid G) &:: \text{Likleyhood}\\
P(G)   &:: \text{Prior Probability}\\
P(x)   &:: \text{Evidence}\\
\end{align}
$$

Bayes Theorem (Eq above) enables us to quantify the probability a cell is diseased given its YM by considering the posterior probability that it is an occurrence in a group with the appropriate probability density function. If we take healthy and diseased to be exclusive groups $G_{1}$ and $G_{2}$ then the probability of a cell being diseased would be given by the proportional instance probability of it's YM for the treated group over the control and treated groups all multiplied by their prior probability.

$$\large \hat{P}(G_2 \mid x) = \frac{P(x \mid G_2) \cdot P(G_2)}{P(x \mid G_1) \cdot P(G_1) + P(x \mid G_2) \cdot P(G_2)}$$

Where the likelihood of a given group is determined based on fitting the observed occurrences to a probability density function. 3 distribution modelling methods will be tested: 1) Gaussian, 2) Kernel Density Estimation, 3) Skewed normal. 
Gaussian is the familiar normal distribution implied by the mean and standard deviation of the YM observed in the experimental data. It assumes an ideal symmetrical probability density function like one that would be observed by taking infinite samples of a single true value obscured by white noise. 

$$
{\large  
\hat{P}(x \mid G) =  
\frac{1}{\sigma_{G} \sqrt{2 \pi}}  
e^{\tfrac{-1}{2}  
\left( \tfrac{x-\mu_{G}}{\sigma_{G}}\right)^{2}}  
}
\qquad  
\begin{align}  
\hat{P}(x \mid G) &:: \text{Group Probability Density Function}\\
x           &:: \text{Observation (i.e. Young's Modulus)}\\
\sigma_{G}  &:: \text{Group Standard Deviation}\\
\mu_{G}     &:: \text{Group Mean}\\
\end{align}
$$

Skew-Normal is an extension of the Gaussian distribution that allows for asymmetric bias i.e. most of the observations occurring just to one side of the mean and a few occurring far out to the other. It dose this by multiplying the Gaussian as seen above, by the cumulative distribution function (CDF) of it's z-score multiplied by a skewness parameter. A CFD simply provides the probability of finding a value below a given threshold, and in this case that threshold is set by the distance of each observation from the mean biased by a skew parameter for it's shape. 

$$
{\large
\hat{P}(x \mid G) =  
\phi\left(x; \mu_G, \sigma_G \right)
\cdot  
\Phi\left(  
\alpha_G \cdot \frac{x - \mu_G}{\sigma_G}  
\right)
}
\qquad
\begin{align}
\phi(x; \mu, \sigma) &:: \text{Normal PDF evaluated at } x \\
\alpha_G          &:: \text{Group Skew Parameter} \\
\Phi(z)           &:: \text{Standard Normal CDF}
\end{align}
$$

Kernel Density Estimation (KDE) on the other hand is more observation focused producing a probability density function that more closely mimics the shape of the observed data without pre-supposing a particular form. It achieves this by producing a Gaussian for every single point centred at it's location with a fixed spread, these are then summed to produce a single complex curve.

$$
{\large  
\hat{P}(x \mid G) =  
\frac{1}{n h} \sum_{i=1}^{n} K\left( \frac{x - x_{i_G}}{h} \right)  
}  
\qquad  
\begin{align}  
x_{i_G}           &:: \text{Observed Data Points from Group G}\\
n                 &:: \text{Number of Observations}\\
K(\cdot)          &:: \text{Kernel Function (i.e. Gaussian)}\\
h                 &:: \text{Bandwidth (Smoothing Parameter)}\\
\end{align}
$$

Each of these distribution fitting methods will be tested in Bayesian classifier and prediction accuracy for the experimental dataset will be compared.
The prior probabilities depend on the application, for high throughput screening this wold be heavily biased towards the initial cell state, or in patient diagnosis this could be a function of patient specific and/or epidemiological factors. In the context of this report prior probabilities are simply the proportion of samples from each group.

## Results


### Elasticity Modeling


The difference between the Hertz elasticity model for a parabolic indentation and the Hertz/Sneddon spherical indentation where minor producing effectively indistinguishable estimates for YM however the Hertz parabolic model resulted in a slightly but consistently higher residual fit error with it's slightly more progressive curvature. For this reason the values from the Hertz/Sneddon spherical where preferred for all subsequent analysis.
Below are representative examples of each fit for the same force indentation curve showing just how similar they are in practice.

%% Quantify difference in Hertz v Sneddon average residuals %%

%% ###### Figure: Comparison in Elasticity Fit Techniques for an Example Curve %%

--- start-multi-column: ID_31no
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Hertz/Sneddon spherical indentation model fit](Fit%20Quality/Experiments/Sneddon/Control/Control-2011.03.22-18.41.44.svg)


--- column-break ---


![Hertz parabolic indentation model fit](Fit%20Quality/Experiments/Hertz/Control/Control-2011.03.22-18.41.44.svg)


--- end-multi-column

There where some trends observed in the general shape of the residual error, specifically; 1) an initial hump at the contact point likely unaccounted for electrostatic non contact forces due to Van der Waals effect,  2) a middle dip and final flick where fit's are shallower than the actual force indention behaviour implying an under estimation of YM or a non linear elasticity. The first effect of non contact forces is not relevant to this study of cytoskelital and thus a high tolerance for error near the contact region is tolerated and expected. For cells displaying non linear elastic behaviour the best single approximation was taken. Both of these effects are particularly pronounced in the following fitting (below left) for this dataset this would be considered a bad fit.



--- start-multi-column: ID_iwtt
```column-settings
Number of Columns: 2
Largest Column: standard
```



![Example of a poor fit to a non linear elastic response](Fit%20Quality/Experiments/Sneddon/Control/Control-2011.03.22-19.35.48.svg)

%% Figure showing all residual curves faintly with smoothed average of all and grouped %%

--- column-break ---


![Plot showing trend in average variation across experiments](SuccessiveTest_trends_absolute.svg)


--- end-multi-column


%% Checking for cell relaxation or systematic error based on observed trends in successive experimentation %%


There was a slight negative trend observed across successive tests indicative of cell relaxation with the first test indicating a 10% higher YM on average, however this was not deemed necessary to control for. The majority of cells showed strong agreement across tests resulting in tight confidence intervals and representative apparent YM values. The examples below are typical samples from each group.

%% ###### Figure: Example Cell Fittings for Control vs Treated Group %%


--- start-multi-column: ID_xdg9
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Typical control group cell elsasticity approximation](Fit%20Quality/Cells/Control-Cell6.svg)


--- column-break ---


![Typical treated group cell elasticity approximation](Fit%20Quality/Cells/Treated-Cell12.svg)


--- end-multi-column


There where cells that displayed significantly higher variation between experiments from both groups, this was not constantly associated with the order of the tests but did correlate with higher overall YM and only a sporadic effect. Given the shallow depth of the indention this is unlikely to be the influence of stiffer organelles but could perhaps be due to the probing site interacting with cytoskeletal structures such as the microvilli force sensing/transducing elements or structural anchor points, however It would require more advanced imaging techniques to explain these variations with confidence. Notably cells in the treated group tended to have one test with a significantly lower apparent elasticity but strong agreement in the other 4 as is the case below, this neither was consistently associated with test order. 

--- start-multi-column: ID_2ugn
```column-settings
Number of Columns: 2
Largest Column: standard
```


![High inter experimental range control cell](Fit%20Quality/Cells/Control-Cell4.svg)


--- column-break ---


![High inter experimental range treated cell](Fit%20Quality/Cells/Control-Cell7.svg)


--- end-multi-column




### Determine Effect Strength


%% ### Validity of results %%

The treated cells where found to be on average twice as stiff as the untreated cells with a $517 \ \text{Pa}$ higher average young's modulus. Both groups where fairly broad with standard deviations of $306$ and $541 \ \text{Pa}$ for control and treated respectively, while this gives the treated group a $77\%$ higher variance, as a proportion of average YM they are similar being $55\%$ and $67\%$ of their respective means. Considering range as a proportion of of median 

%%
stdv/mean 
`=305.52/457.99*100`
`=540.96/975.53*100`
median/mean 
`=392.04/457.99*100`
`=807.94/975.53*100`
range/mean
`=( 982.09 - 143.85) / 457.99*100`
`=(1761.58 - 524.65) / 975.53*100`
range/median
`=( 982.09 - 143.85) / 392.04*100`
`=(1761.58 - 524.65) / 807.94*100`
%%

--- start-multi-column: ID_3r15
```column-settings
Number of Columns: 2
Largest Column: standard
```


%% ###### Figure: Population Shape of Cell Young's Modulus by group %%

![Population Shape of Cell Young's Modulus by group](YM+Range_Viol_comparison_byCell.svg)


--- column-break ---


%% ###### Figure: Population Shape of Test Young's Modulus (Pa) by group %%

![Population Shape of Test Young's Modulus (Pa) by group](YM+Residuals_Viol_comparison_byExperiment.svg)


--- end-multi-column


By grouping the raw test data by cell and producing group characteristics cell wise rather than with the whole raw dataset provides more distinguishable groups with more distant means and tighter standard deviations.


| Group             | Mode    | Min     | Max     | Median  | Mean   | StDev  |
| ----------------- | ------- | ------- | ------- | ------- | ------ | ------ |
| Control, By Cells | 154.96  | 143.85  | 982.09  | 392.04  | 457.99 | 305.52 |
| Control, By tests | 160.643 | 137.977 | 1161.76 | 385.253 | 482.63 | 301.24 |
| Treated, By Cells | 524.65  | 524.65  | 1761.58 | 807.94  | 975.53 | 540.96 |
| Treated, By tests | 605.979 | 381.52  | 1964.58 | 833.028 | 983.46 | 506.70 |


### Construct Classifiers


Given the observed data is distributed quite unevenly the choice of distribution used to model it's likelihood has a significant effect. Below are the candidate probability density functions for use in the classifier. The direct Gaussian based distributions i.e. Gaussian and skew-normal have additional dashed curves produced by Monte Carlo sampling 50,000 candidate distributions with means and standard deviations within the 95% confidence intervals of the observed distribution. These provide an indication of what a larger study would likely find.

![Comparison of Group Probability Density Functions by Distribution Model](Group_PDFs_byModel.svg)


The single cell classification curves in the figure below show what a classifier based on each of the distribution models would rate a cell's probability of being from the treated/diseased group (1) vs the control/healthy group (0). This is valid for an average of 5 indentation tests performed as described in the experimental method a different number of tests and a different methodology would likely need additional controls or a model based on a more relevant dataset. 

%% Disease measure against YM coloured by test group %%

![Comparison of distribution models on single cell classifier decision curve](Classification_Threashhold_by_Distribution_Model.svg)

The confidence of the model increases, albeit diminishingly, the more samples are taken, an average of 15 cells, each being an average of 5 tests, from a common unknown group could be classified with an average accuracy of 90%. This largely is due to reducing the uncertainty in the crossover range of $500 \text{Pa} \lt  \text{YM} \lt 1000 \text{Pa}$ where a lage portion of samples are likely to fall and for a single cell might just as well be healthy or diseased.


--- start-multi-column: ID_j1ca
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Average classification accuracy threshold with n samples, $90 \% @ \text{n}=15$ and $99 \% @ \text{n}=37$](Classification%20Accuracy%20vs%20Sample%20Size.svg)


--- column-break ---


![Normal Distribution Classifier Boundary Classification Confidence with n Samples](Classification_Boundry_v_Samples.svg)


--- end-multi-column





## Discussion



%% Best and worst cases based on confidence intervals %%

The sample sizes used in this report are not sufficient to produce a classifier suitable for use in industry or for diagnosis, considering the the confidence intervals of the groups established it is possible that a larger experimental dataset my prove this method to be significantly more or less effective than has been estimated here. By considering the limit cases of the 95% confidence intervals of the most distinct best case i.e. furthest means and smallest standard deviations this method may prove highly accurate requiring very few samples in contrast the worst case least distinct i.e. closest means and wisest spread would render this method completely ineffective.  



--- start-multi-column: ID_llj8
```column-settings
Number of Columns: 2
Largest Column: standard
```


%% ###### Figure: Best vs Worst Case Probability Density Functions %%

![Best vs Worst Case Probability Density Functions](Group_PDFs_LimCases.svg)

--- column-break ---


![Young's Module by Group with Confidence Metrics](YM_CI_byGroup.svg)


--- end-multi-column

%% > (Right) Group mean and standard deviation 95% confidence intervals overlayed on notched Tukey style box plots showing overlap, an indication of poor statistical significance. %%

It should be noted that with the small sample size of the treated group $n=4$, these metrics are significantly brought upward by the results of a single cell and removing it significantly diminishes the statistical significance of the stiffening effect relied upon in this method. However, other than the substantially higher Young's Module values there is no reason to expect this cell or it's experiments to be erroneous. The Hertz fit's appear representative of the observed cell response with residuals similar to average across all fits $2 \ \text{pN}$. The relevant metrics for the cell in question are below and the reader is encouraged to judge to their own satisfaction whether the conclusions drawn from the full dataset are sufficiently supported or if the influence of this single observation undermines the findings. 


![Apparent cell 7 YM classification; (Left Axis) all elasticity tests compared with estimate for apparent YM, (Right Axis) characterisation uncertainty: mean with 90% confidence intervals overlyed on notched box plot of raw data (darker) and $100 \times$ bootstrapped (lighter).](Fit%20Quality/Cells/Treated-Cell7.svg)




--- start-multi-column: ID_3tbo
```column-settings
Number of Columns: 2
Largest Column: standard
```



![Test 61 Elasticity Model Fit](Fit%20Quality/Experiments/Sneddon/Treated/Treated-2011.03.31-22.53.24.svg)


--- column-break ---


![Test 62 Elasticity Model Fit](Fit%20Quality/Experiments/Sneddon/Treated/Treated-2011.03.31-22.54.49.svg)



--- end-multi-column




%% > Cell 7 fitting characteristics; (top) Apparent cell YM classification, (rest) elasticity model fittings for each test, (middle left) Test 61, (middle right) Test 62 fit, (bottom left) Test 63 fit, (bottom middle) Test 64 fit, (bottom right) Test 65 fit. %%



--- start-multi-column: ID_2qgu
```column-settings
Number of Columns: 3
Largest Column: standard
```



![Test 63 Elasticity Model Fit](Fit%20Quality/Experiments/Sneddon/Treated/Treated-2011.03.31-22.56.13.svg)


--- column-break ---


![Test 64 Elasticity Model Fit](Fit%20Quality/Experiments/Sneddon/Treated/Treated-2011.03.31-22.57.37.svg)


--- column-break ---


![Test 65 Elasticity Model Fit](Fit%20Quality/Experiments/Sneddon/Treated/Treated-2011.03.31-22.59.01.svg)


--- end-multi-column










In both the Control and the Treated group the majority of cells consistently exhibit YM lower than the group average with a few very high YM cells with higher inter experiment range. The range in YM increases linearly with with higher average YM values, however when range is considered as a proportion of average YM there is no correlation. This is unlikely to be a product of fitting error or the dimensionality of YM emphasising experimental inaccuracy based on how well the fittings match the observed cell responses, the cells are exhibiting a fixed linear elasticity within a given test but a range of different elasticises across tests and that range increases proportionally with the average. Neither is this a case of the higher average being a result of cells displaying higher variance in elasticity from a fixed minimum as the lower bound of even the $1000\times$ bootstrapped confidence intervals rise in tandem with the average YM. 

%% This is likely due to %%


--- start-multi-column: ID_11ib
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Cell inter test range in YM against apparent cell YM](YM_RangeByApparentVal.svg)


--- column-break ---


![Cell relative inter test range in YM against apparent cell YM](YM_RelRangeByApparentVal.svg)


--- end-multi-column



Due to the unexplained variance in the range of YM across tests of single cells the possibility of it's relation to the diseased state has not been ruled out Introducing the possibility that method increases classification accuracy at the cell level but potentially sacrifices it at the population level. This provides an argument to establish group characteristics on the experiment level rather than the cell level for use cases where many samples are being taken from single unknown group as might be the case in a biopsy for example.

## Conclusion




## Bibliography

