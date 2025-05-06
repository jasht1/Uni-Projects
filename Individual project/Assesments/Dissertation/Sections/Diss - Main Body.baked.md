---
title: Nanomechanical Analysis of Renal Tubular Cell Cytoskeleton for the Detection of Renal Disease
subtitle: 
titlepage-logo: /home/joeashton/Sync/Obsidian/SuperVault/Core/Templates/Pandoc/attachments/UoL_logo.png
author: Joseph Ashton
authors:
  - name: Joseph Ashton
    affiliation: School of Engineering
    institution: University of Lincoln
    email: 27047440@students.lincoln.ac.uk
    address: Lincoln
acknowledgements: I would like to thank my patient amd knowledgable suporvisor Eleftherios Siamantouras
declaration: ""
abstract: This project investigates changes in mechanical properties of kidney cells when exposed to TGF-β1, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. The aim of this project is to provide insight on the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy.
---

## Abstract


This project investigates changes in mechanical properties of kidney cells when exposed to TGF-β1, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. 
The aim of this project is to develop a method to quantify the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy.

## Introduction 


The mechanical properties of cells are finely tuned to their function, especially epithelial cells who's core role is to form active structural surfaces where correct functioning is a direct result of appropriate strength, stiffness, and shape. In patients suffering from diabetic nephropathy the alterations in renal tubule cell properties are directly associated with progression of the disease and further kidney damage. 


## Background





### Relevant Physiology

%% #### Kidney %%

The human body can be understood as a complex biological machine, made up of many sub-mechanisms familiar to engineers. In this sense the filtration system of the human body is referred to as the renal system, in which the kidneys are a component about the size of a clenched fist that can be likened to a sophisticated water treatment plant combined with a feedback-controlled chemical processing unit. Each contain roughly a million multi step filter loops called nephrons [@bertramJF2011-HumanNephronNumber].  

> ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/Kidney%20and%20nephron%20-%20Labeled.jpg)
>Labeled Kidney and Nephron form National Institute of Diabetes and Digestive and Kidney Diseases, National Institutes of Health [@niddk-KidneyNephronLabeled].

%% #### Nephrons %%

The nephrons are selective, able to remove waste products while keeping desirable substances in the blood. They are able to regulating essential substances such as water, electrolytes, and pH levels to strict set points. [@ogobuiroI2025-PhysiologyRenal]

%% #### glomerulus %%

The the first step unfiltered blood enters the glomerulus and if forced through several membrane filters by hydro-static pressure. The first layer permits all solutes blocking only cells. The next is negatively charged thus blocking proteins like albumin. The final layer modulates the flow resistance to vary the hydro-static pressure gradient, this will be counter balanced by the osmotic pressure such that it can be used to effectively vary the ultra filtration coefficient. [@pavenstadtH2000-RolesPodocyteGlomerular; @ogobuiroI2025-PhysiologyRenal] Leaving the glomerulus is a blood vessel containing only cells and proteins and a fractional remainder of the other solute, and the tubule carrying all the removed solute [@lumen-NephronStructure].

%% #### Tubule %%

The glomerulus is an overly aggressive filter; much of the water and solute must be re introduced to the blood from the tubules. %%in several stages. The first stage, the proximal convoluted tubule (PCT) pumps all the glucose and amino acids as well as most of the sodium and water back into the blood [@ogobuiroI2025-PhysiologyRenal]. In the next more water is reabsorbed, and in the final the remainder of the sodium as well as potassium and chlorides get reabsorbed via osmosis [@ogobuiroI2025-PhysiologyRenal]. %% The tubules run along side blood vessels and using a combination of osmosis, active transport and controlled ionic gradients %%sodium, potassium, calcium, magnesium, chlorides%% the valuable ions and most of the water is reabsorbed over several uniquely specialised segments [@ogobuiroI2025-PhysiologyRenal].  

%% #### Tubule cell %%

> ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/Tubule%20zoom%20diagram.png)
> Simplified diagram of tubule, tubule wall and tubule cell structure.
> The structure of the tubule varies significantly across it's length to as different sections are specialised to permeate different resources, the lumen diameter and epithelial cell height values are averages of random samples [@morozovD2021-MappingKidneyTubule]. 

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

Inflammation increases production of cytokines, including TGF-β1, which trigger Epithelial to Mesenchymal Transition (EMT) [@hillsCE2012-TGFvModulatesCelltocell; @pizzinoG2017-OxidativeStress]. EMT is a process where cells which make up structural and functional surfaces (epithelial) transition into repair/maintenance cells (mesenchymal) [@kalluriR2009-BasicsEpithelialmesenchymalTransition]. In this case tubular epithelial, cells which make up the fine vessels of the kidney that filter blood, transform into myofibroblasts, repair and maintenance cells %% or undergo apoptosis (cell death) %% [@iwanoM2002-EvidenceThatFibroblasts]. This is the underlying mechanism of fibrosis, which induces atrophy and scarring in the tubules %% and results in intraglomerular hypertension %% causing progressive kidney damage [@metcalfeW2007-HowDoesEarlyChronicKidneyDiseaseProgress].




### Atomic Force Microscopy (AFM)

%% #### What is AFM? %%

Atomic Force Microscopy (AFM) is a technique for characterising nanomechanical properties and structure. It is well suited to microbiology as it allows for the study of live cells [@kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 

Atomic force microscopes use the deflection of a very fine probe on a flexible cantilever to detect contact forces ranging form nano to micro Newtons. There are a myriad of applications and operating modes of AFM [@dufreneYF2002-AtomicForceMicroscopy] but this report is primarily concerned with nano indentation. This involves advancing a fine tipped probe on the end of the cantilever into a sample cell producing a force over indentation depth curve, from which the elasticity of the cell can be calculated using a Hertz contact model [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces].

%% #### functional/mechanical description %%

The typically atomic force microscope utilise a laser focused on the free end of the cantilever such that any deflection of the probe produces an amplified deflection of the reflected beam, this is recorded by a position sensitive photodiode [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces]. 

> ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/Atomic%20Force%20Microscopy%20-%20mechanism%20diagram.png)
> Atomic force microscope functional diagram

The sample once mounted to the sample stage can be manoeuvred precisely in relative to the probe by applying voltage to piezoelectric actuators [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @giraudF2019-PiezoelectricActuatorsIntroduction] this is how the sample is advanced into the tip. Once calibrated the voltage at the actuators gives the sample stage position and the voltage at the photodiode gives the deflection of the probe, with this a force displacement curve can be produced by accounting for the stiffness of the cantilever and the relative displacement [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials].

%% #### typical force displacement curve %%

A typical force displacement curve from a nano indention experiment has the following shape seen in figure %% #WIP %% (A) below. A broadly level region where the probe is not in contact with the cell; the contact region; a sloped region where the probe is indenting the cell; the turnaround point; from which the same is repeated in reverse differing mainly at the point of separation [@kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 

> ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/fdcurve%20figure%20A%20-%20radmacherM2007-StudyingMechanicsCellular.png) ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/fdcurve%20figure%20B%20-%20radmacherM2007-StudyingMechanicsCellular.png)
> Example AFM data from Radmacher 2007, (A) shows the curve as a whole, (B) zoomed into the contact / separation region [@radmacherM2007-StudyingMechanicsCellular].

%% Contact point jump %%

The exact point of contact is often ambiguous and rarely the same as the the point of separation. On approach the cantilever will be deflected away from the cell by van der waals forces until the spring force of the cantilever overcomes and surface tension takes hold [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 
The point of separation is typically clearer as it's associated with a "jump" in cantilever deflection as the surface tension / adhesion of the cell to the probe is overcome [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials].

%% 
> ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/AFM%20contact%20point%20jump.png)
> [@buttHJ1995-MeasuringSurfaceForces]
%%



### Contact Mechanics

In order to calculate elasticity the experimental data must be fit to a theoretical mechanical model of the interaction. Below is a table outlining different model indention relationships.

| Model                         | Force-Indentation relationship                                                                                         | Scope                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hertz                         | $$F = \frac{4}{3}E' \sqrt{R} \ \omega^{3/2}$$                                                                          | Hertz model approximates the shallow indention of two linearly elastic spheres with infinitesimal strains [@linDC2009-SphericalIndentationSoftMatterHertzianRegime; @radmacherM2007-StudyingMechanicsCellular; @jpkinstruments-JPKDataProcessing].                                                                                            |
| DMT (DerjaguinMuller-Toporov) | $$F = F_{Hertz} - F_{det}$$<br>$$\delta = \frac{a}{2} \ln \frac{R_{i}+a}{R_{i}-a}$$                                    | Depending on the depth of indentation and the material interaction it can be important to account electrostatic non contact forces, the influence of which can be modelled using the Derjaguin approximation for interaction potential [@buttHJ1995-MeasuringSurfaceForces; @jpkinstruments-JPKDataProcessing].                               |
| Fung                          | $$F = B\pi (\frac{a^5- 15Ra^4 + 75R^2a^3}{5Ra^2- 50R^2a + 125R^3})\text{exp}⁡[b(\frac{a^3- 15Ra^2}{25R^2a- 125R^3})]$$ | An exponential strain energy function based on mechanical testing of mesentery and arterial tissues, that models the non linear elasticity of cells [@fungY1967-ElasticitySoftTissues; @linDC2009-SphericalIndentationSoftMatterHertzianRegime]. This method is tangebly more precise but doesn't provide a simple value for young's modulus. |

%% Expand on obstacles with applying contact mechanics models to cells %%

## Literature Review

Developments in both understanding %% of the pathophysiology %% of kidney disease and the application of atomic force microscopy (AFM) technology [@liuS2024-AtomicForceMicroscopyDisease-relatedStudies; @dufreneYF2002-AtomicForceMicroscopy] may provide a valuable measure of the progression of kidney failure to inform the research and development of novel therapies [@parrishAR2016-CytoskeletonNovelTarget].

%% #### What we measure %%

%% Single cell stiffness %%
The mechanical properties of tubular cells are largely a result of their cytoskeletal structure [@jalilianI2015-CellElasticityRegulated; @radmacherM2007-StudyingMechanicsCellular] which is altered significantly with the progression of DN [@buckleyST2012-CytoskeletalRearrangementTGFv1induced]. 

%% Inter cellular adhesion %%

%% The stiffness of individual cells can be observed and correlated with the [@siamantourasE2016-QuantifyingCellularMechanics]. %%

%% #### Obstacles & limitations %%

%% Cell cultures aren't perfect representations of their in vitro counterparts. This can be improved with careful preparation. The elasticity of the substrate the culture is grown on can have a significant impact on cytoskelital arrangement [@wangD2022-KidneyProximalTubule; @loveH2018-SubstrateElasticityGoverns]  %%

%% Table with papers and a relevant summary #WIP %%

The below table lists several papers utilising atomic force microscopes to produce force displacement curves from a bead tipped cantilever fitted to a hertz contact model to find cell elasticity.

| Paper                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Cell Type                                                                            | Scope                                                                                                                                                                   | Cell Elasticity                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [@siamantourasE2016-QuantifyingCellularMechanics]  E. Siamantouras, C. E. Hills, P. E. Squires, and K.-K. Liu, ‘Quantifying cellular mechanics and adhesion in renal tubular injury using single cell force spectroscopy’, _Nanomedicine: Nanotechnology, Biology and Medicine_, vol. 12, no. 4, pp. 1013–1021, May 2016, doi: [10.1016/j.nano.2015.12.362](https://doi.org/10.1016/j.nano.2015.12.362).                                              | HK2: immortalised human kidney proximal tubule  epithelial cell culture              | Over 30 cells each indented 5 times immediately above the nucleus producing over 150 curves.                                                                            | **control**: 320Pa <br>cells treated with TGF-β1: 549 Pa          |
| [@jafariA2024-MechanicalPropertiesHuman]  A. Jafari, A. Sadeghi, and M. Lafouti, ‘Mechanical properties of human kidney cells and their effects on the atomic force microscope beam vibrations’, _Microsc. Res. Tech._, vol. 87, no. 8, pp. 1704–1717, 2024, doi: [10.1002/jemt.24543](https://doi.org/10.1002/jemt.24543).                                                                                                                           | HEK-293: immortalised human embryonic kidney cell culture                            | did not elaborate                                                                                                                                                       | 539.8 Pa                                                          |
| [@shimizuY2012-SimpleDisplaySystem]  Y. Shimizu, T. Kihara, S. M. A. Haghparast, S. Yuba, and J. Miyake, ‘Simple Display System of Mechanical Properties of Cells and Their Dispersion’, _PLOS ONE_, vol. 7, no. 3, p. e34305, Mar. 2012, doi: [10.1371/journal.pone.0034305](https://doi.org/10.1371/journal.pone.0034305).                                                                                                                          | HEK-293: immortalised human embryonic kidney cell culture                            | The median of value of over 100 cells examined at 25 points each.                                                                                                       | mode value ($x_{0}$): 410 Pa <br>variance ($w$): 0.757            |
| [@buckleyST2012-CytoskeletalRearrangementTGFv1induced]  S. T. Buckley, C. Medina, A. M. Davies, and C. Ehrhardt, ‘Cytoskeletal re-arrangement in TGF-β1-induced alveolar epithelial-mesenchymal transition studied by atomic force microscopy and high-content analysis’, _Nanomedicine: Nanotechnology, Biology and Medicine_, vol. 8, no. 3, pp. 355–364, Apr. 2012, doi: [10.1016/j.nano.2011.06.021](https://doi.org/10.1016/j.nano.2011.06.021). | A549: human lung alveolar carcinoma epithelial cell culture                          | On each cell, a 4 × 4 grid of force-distance curves was collected in at least 5 different positions (avoiding the nucleus and the very edge) producing over 750 curves. | On Glass: 8300 $\pm$ 1100 Pa<br>On collagen I: 9100 $\pm$ 2900 Pa |
| [@wyssHM2011-BiophysicalPropertiesNormal]  H. M. Wyss _et al._, ‘Biophysical properties of normal and diseased renal glomeruli’, _Am J Physiol Cell Physiol_, vol. 300, no. 3, pp. C397–C405, Mar. 2011, doi: [10.1152/ajpcell.00438.2010](https://doi.org/10.1152/ajpcell.00438.2010).                                                                                                                                                               | Sprague-Dawley rat kidney glomeruli capillary wall extracted by differential sieving | 10 different glomeruli with 10 measurements each                                                                                                                        | 2,300 $\pm$ 160 Pa                                                |



## Methodology



The experimental procedure used to produce the data used in this report is detailed thoroughly in reference [@siamantourasE2016-QuantifyingCellularMechanics]. Cells of the adult human proximal tubule kidney (HK2) cell line [@ryanMJ1994-HK-2] where purchased from the American Type Culture Collection (ATCC; Gaithersburg,  MD 20878 USA). These where maintained in Dulbecco's Modified Eagle Medium/Nutrient Mixture F-12 (DMEM/F12), 10% fetal calf serum (FCS), glutamine (2mM), and EGF (5ng/ml) for 48 hours. The cells where divided into 2 test groups, the "control" group and the "treated" group which where where serum starved overnight before being exposed to TBF-β, an E-cadherin antibody obtained from R&D systems, at (2-10ng/mL) for a further 48 hours. 

The indentation experiments where carried out using a JPK Instruments CellHesion©200 module with a BioCell™ temperature controller to maintain a bed temperature of 37°C on a TMC 63-530 anti-vibration table. Probes where constructed by attaching 11µm Polyscience PolyBeads® to Nanoworld TL-1 tipless cantilevers with a force constant of 0.03N/m. Each cell was indented 5 times directly above the nucleus at a constant speed of 5µm/s with intervals of 60 seconds. For each set of experiments the spring constant of the cantilever was calibrated using the thermal noise method and the cell's height was measured to determine an appropriate indentation depth to minimise the influence of the hard basal substrate. 

%% thermal noise method how and why %%

%% on a Nikon eclipse TE 300 inverted microscope. The AFM bed was maintained at 37°C using a JPK Instruments BioCell™ temperature controller. %%




%% How did i get ym values from the datasets %%

Experimental data was received in the form of `.jpk-force` logs of head height position against vertical deflection force along with experimental metadata. The JPK data processing software was used to calculate the probe height based on spring constant and at this point the curves where exported in text form. In order to establish "trustworthy" values for YM the function included in the JPK data processing software was used with the deepest point of indentation to 1µm past the contact point as upper and lower bounds. This was then replicated for the text exports in python using `nanite` an open source package that offers the same Hertz/Sneddon elasticity model truncated power series approximation for spherical indenters with a difference in fit optimisation methods; where JPK Data Processing uses least squared regression, Nanite utilises machine learning for fit quality estimation and optimisation. Despite not providing the "trustworthy" fits as a rated training dataset Nanite reproduced the "trustworthy" YM estimations with an average deviation of less than ±0.05%. The Hertz parabolic indenter model was also tested and compared with the Hertz/Sneddon approximation. All force indentation curves where plotted alongside those implied by the fitting along with the residual fitting error to identify potential anomalies or systematic error. Attention was paid to identify any consistent trends in the residual as If the residual where to consistently deviate from generally flat noise at 0 this would imply a poorly matched elasticity model.

%% How did I determine the appropriate cell YM given the experimental data %%

As each cell was tested 5 times the apparent YM of a cell was taken to be the average average  of the Hertz/Sneddon fits. To validate the results the force indentation curves of the experiments and the implied curve of the apparent YM where plotted and inspected visually checking for cell relaxation or systematic error based on observable trends in successive experimentation or any apparent anomalies. In addition the 95% confidence interval of the apparent cell YM was calculated for the natural set and a $100 \times$ bootstrapped super set this was inspected on log scales given that the error margin increases proportionally with higher YM, however for consistency with the rest of the report figures included in the results section maintain linear YM axis of 0,2000.

%% Confidence Intervals, what are they and how did I calculate them %%

As the apparent cell YM was taken to be the mean it's confidence intervals where those of the mean YM for the set of cell tests. 

$$\text{CI}_\mu = \left[ \mu - t^* \cdot \frac{\sigma}{\sqrt{n}},\ \mu + t^* \cdot \frac{\sigma}{\sqrt{n}} \right]
\qquad
\text{CI}_\sigma = \left[ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{upper}}} },\ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{lower}}} } \right]
$$

Where confidence intervals where calculated for the standard deviation as is later necessary in determining the confidence in the group classifications and when montecarlo sampling, the chi distribution is used. This was originally tried using normal distributions being a generally acceptable approximation, however given the small and bottom biased experiment sample sets assuming symmetric distribution of probable standard deviations was not a fair representation.

%% Bootstrapping, what is it, why did I do it %%



A Bayes classifier was constructed to quantify the probability of diabetic nephropathy from cell stiffness based on the effect observed in the experimental data. The control group is taken as a model of healthy cell presentation and the treated group representing the onset of diabetic nephropathy. Similarly to how cell properties where estimated from several tests, the typical group properties are estimated from several cells, conversely it can also be found by taking the averages and standard deviations of the whole dataset. It is often the case that considering the whole raw dataset provides more accurate picture of the group, however in this case it is appropriate to consider by subgroups i.e. by cells, this is because the samples are not independent and not representative of the test case. As it has been observed that successive tests are not introducing systematic error their average provides a more accurate estimation of the given cell, thus classification should be considered at the cell level. 


%% The following is the general formula for normal distribution: 

$$
{\large f(x)=
\frac{1}{\sigma \sqrt{2 \pi}}
e^{\frac{-1}{2}
\left( \cfrac{x-\mu}{\sigma}\right)^{2}}
}
\qquad
\begin{align}
f(x)	&= 	\text{Probability Density Function}\\
x       &=  \text{Variable (i.e. Young's Modulus)}\\
\sigma	&= 	\text{Standard Deviation}\\
\mu	    &= 	\text{Mean}\\
\end{align}
$$ %%


%% Bayes Classifier %%  

Bayes Theorem (Eq below) enables us to quantify the probability a cell is diseased given its YM by considering the posterior probability that it is an occurrence in a group with the appropriate probability density function.

$$\large
P(G∣x) = \frac{P(x∣G) \cdot P(G)}{P(x)} 
\qquad
\begin{align}
P(G∣x)	&= 	\text{Posterior Probability}\\
P(x∣G)  &=  \text{Likleyhood}\\
P(G)	&= 	\text{Prior Probability}\\
P(x)    &= 	\text{Evidence}\\
\end{align}
​$$

If we take healthy and diseased to be exclusive groups $G_{1}$ and $G_{2}$ then the probability of a cell being diseased would be given by:

$$\large P(G_2 \mid x) = \frac{P(x \mid G_2) \cdot P(G_2)}{P(x \mid G_1) \cdot P(G_1) + P(x \mid G_2) \cdot P(G_2)}$$

Where the likelihood of a given group is based on the normal distribution implied by the mean and standard deviation of the YM observed in the experimental data. 

%% $$P(x \mid G) = \frac{1}{\sqrt{2\pi}\sigma_G} \exp\left( -\frac{(x - \mu_G)^2}{2\sigma_G^2} \right)
$$ %%

$$
{\large P(x \mid G) = 
\frac{1}{\sigma_{G} \sqrt{2 \pi}}
e^{\tfrac{-1}{2}
\left( \cfrac{x-\mu_{G}}{\sigma_{G}}\right)^{2}}
}
\qquad
\begin{align}
P(x \mid G)	&= 	\text{Group Probability Density Function}\\
x           &=  \text{Variable (i.e. Young's Modulus)}\\
\sigma_{G}	&= 	\text{Group Standard Deviation}\\
\mu_{G}	    &= 	\text{Group Mean}\\
\end{align}
$$

And the prior probabilities will depend on the application, for high throughput screening this wold be heavily biased towards the initial cell state, or in patient diagnosis this could be a function of patient specific and/or epidemiological factors. In the context of this report prior probabilities are simply the proportion of samples from each group.

## Results



The difference between the Hertz elasticity model for a parabolic indentation and the Hertz/Sneddon spherical indentation where minor producing effectively indistinguishable estimates for YM however the Hertz parabolic model resulted in a slightly but consistently higher residual fit error with it's slightly more progressive curvature.  Below are representative examples of each fit for the same force indentation curve.

%% Quantify difference in Hertz v Sneddon average residuals %%

###### Figure: Comparison in Elasticity Fit Techniques for an Example Curve


![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Experiments/Sneddon/Control/Control-2011.03.22-18.41.44.svg)





![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Experiments/Hertz/Control/Control-2011.03.22-18.41.44.svg)




There where some trends observed in the general shape of the residual error, specifically; 1) an initial hump at the contact point likely due to unaccounted for electrostatic non contact forces due to the van der walls effect,  2) a middle dip and final flick where fit's are shallower than the actual force indention behaviour implying an under estimation of YM or a non linear elasticity. Both of these effects are particularly pronounced in the following fitting for this dataset this would be considered a bad fit.

![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Experiments/Sneddon/Control/Control-2011.03.22-19.35.48.svg)

%% Figure showing all residual curves faintly with smoothed average of all and grouped %%


%% Checking for cell relaxation or systematic error based on observed trends in successive experimentation %%

There where no general trends observed across successive tests meaning there was no need to control for cell relaxation. The majority of cells showed strong agreement across tests resulting in tight confidence intervals and representative apparent YM values. The examples below are emblematic of typical samples from each group.

###### Figure: Example Cell Fittings for Control vs Treated Group


_xdg9


![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell6.svg)





![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Treated-Cell12.svg)





There where cells that displayed significantly higher variation between experiments from both groups however this was not constantly associated with the order of the tests. Given the shallow depth of the indention this is not likely the influence of stiffer organelles but could perhaps be due to the probing site interacting with cytoskelital structures such as the microvilli force sensing/transducing elements or structural anchor points, however It would require more advanced imaging techniques to explain these variations with confidence. Notably cells in the treated group tended to have one test with a significantly lower apparent elasticity but strong agreement in the other 4 as is the case below. 

_2ugn



![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell4.svg)





![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Treated-Cell7.svg)








%% ### Validity of results %%

The treated cells where found to be on average twice as stiff as the untreated cells with a 500 Pa higher average young's modulus in addition the treated group shows a 77% higher variance with a standard deviation of 541 Pa.  


_3r15



###### Figure: Cell Young's Modulus by test group

![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/YM+Variance_Viol_comparison_byCell.svg)

###### Table: Cell Young's Modulus (Pa) statistics by test group

| Group   | Mode   | Min    | Max     | Median | Mean   | StDev  |
| ------- | ------ | ------ | ------- | ------ | ------ | ------ |
| Control | 154.96 | 143.85 | 982.09  | 392.04 | 457.99 | 305.52 |
| Treated | 524.65 | 524.65 | 1761.58 | 807.94 | 975.53 | 540.96 |





###### Figure: Experiment-wise Young's Modulus (Pa) by test group

![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/YM+Residuals_Viol_comparison_byExperiment.svg)

###### Table: Experiment-wise Young's Modulus (Pa) statistics by test group

| Group   | Mode    | Min     | Max     | Median  | Mean   | StDev  |
| ------- | ------- | ------- | ------- | ------- | ------ | ------ |
| Control | 160.643 | 137.977 | 1161.76 | 385.253 | 482.63 | 301.24 |
| Treated | 605.979 | 381.52  | 1964.58 | 833.028 | 983.46 | 506.70 |







%% Small sample size, Group overlap, predictive power %%
%% Look at these overlapping reigions %%
%% Cohen's d = 1.2015293213102536, this shows a strong effect size, but this  %%
###### Figure: Force Indentation for Apparent Cell YM Coloured by Test Group

![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/YM_FD_comparison_byCell.svg)
%% ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/YM_FD_comparison_byExperiment.svg) %%


###### Figure: Young's Module by Group with Confidence Metrics

![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/YM_CI_byGroup.svg)

In the figure above the control group is contrasted with the treated group using notched Tukey style box plots overlaid with the mean and standard deviation 95% confidence intervals as well as the apparent cell YM values for each group. 


%% Overlapping notches, what dose this mean for the usability of the metric %%

%% ![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Group_PDFs_LimCases.svg) %%

## Discussion



%% Best and worst cases based on confidence intervals %%

The sample sizes used in this report are not sufficient to produce a classifier suitable for use in industry or for diagnosis, considering the the confidence intervals of the groups established it is possible that a larger experimental dataset my prove this method to be significantly more or less effective than has been estimated here. By considering the limit cases of the 95% confidence intervals of the most distinct best case i.e. furthest means and smallest standard deviations this method may prove highly accurate requiring very few samples in contrast the worst case least distinct i.e. closest means and wisest spread would render this method completely ineffective.  

###### Figure: Best vs Worst Case Probability Density Functions

![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Group_PDFs_LimCases.svg)


It should be noted that with the small sample size of the treated group n=4, these metrics are significantly brought upward by the results of a single cell. However, other than the substantially higher Young's Module values there is no reason to expect this cell or it's experiments to be erroneous. The Hetz fit's appear representative of the observed cell response with residuals similar to average across all fits 2e-11 N.

In both the Control and the Treated group the majority of cells consistently exhibit YM lower than the group average with a few very high YM cells with higher inter experiment range. However, the range in YM increases linearly with with higher average YM values, when variance is considered proportionally there is no correlation, so this can likely be considered systematic error.



Due to the unexplained variance in the range of YM across tests of single cells the possibility of it's relation to the diseased state has not been ruled out Introducing the possibility that method increases classification accuracy at the cell level but potentially sacrifices it at the population level. This provides an argument to establish group characteristics on the experiment level rather than the cell level for use cases where many samples are being taken from single unknown group as might be the case in a biopsy for example.

## Conclusion




## Annexes


### Control
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell1.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell2.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell3.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell4.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell5.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell6.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell7.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell8.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell9.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell10.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Control-Cell11.svg)

### Treated
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Treated-Cell5.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Treated-Cell6.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Treated-Cell7.svg)
![](file:///home/joe/Documents/Obsidian/SuperVault/Projects/Uni%20Projects/Individual%20project/Workspace/Figures/Fit%20Quality/Cells/Treated-Cell12.svg)

