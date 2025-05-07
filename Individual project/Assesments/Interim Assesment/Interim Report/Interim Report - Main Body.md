---
title: "Nanomechanical analysis of tubular cell cytoskeleton: Interim Report"
subtitle: 
titlepage-logo: /home/joeashton/Sync/Obsidian/SuperVault/Core/Templates/Pandoc/attachments/UoL_logo.png
# bibliography: /home/joeashton/Sync/Obsidian/SuperVault/.pandoc/ZotLibrary.bib
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

## Executive Summary
%% #WIP %%

## Introduction

This project investigates changes in mechanical properties of kidney cells when exposed to TGF-β1, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. 
The aim of this project is to provide insight on the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy.

### Relevant Physiology

%% #### Kidney %%

The human body can be understood as a complex biological machine, made up of many sub-mechanisms familiar to engineers. In this sense the filtration system of the human body is referred to as the renal system, in which the kidneys are a component about the size of a clenched fist that can be likened to a sophisticated water treatment plant combined with a feedback-controlled chemical processing unit. Each contain roughly a million multi step filter loops called nephrons [@bertramJF2011-HumanNephronNumber].  

> ![Close up of a nephron and its place in the kidney. Labels on the kidney cross section show where unfiltered blood enters, filtered blood leaves, and urine exits. On the nephron, the glomerulus, tubule, and collecting duct are labeled along with where unfiltered blood enters, filtered blood exits, and urine exits.|400](Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/Kidney%20and%20nephron%20-%20Labeled.jpg)
>Labeled Kidney and Nephron form National Institute of Diabetes and Digestive and Kidney Diseases, National Institutes of Health [@niddk-KidneyNephronLabeled].

%% #### Nephrons %%

The nephrons are selective, able to remove waste products while keeping desirable substances in the blood. They are able to regulating essential substances such as water, electrolytes, and pH levels to strict set points. [@ogobuiroI2025-PhysiologyRenal]

%% #### glomerulus %%

The the first step unfiltered blood enters the glomerulus and if forced through several membrane filters by hydro-static pressure. The first layer permits all solutes blocking only cells. The next is negatively charged thus blocking proteins like albumin. The final layer modulates the flow resistance to vary the hydro-static pressure gradient, this will be counter balanced by the osmotic pressure such that it can be used to effectively vary the ultra filtration coefficient. [@pavenstadtH2000-RolesPodocyteGlomerular; @ogobuiroI2025-PhysiologyRenal] Leaving the glomerulus is a blood vessel containing only cells and proteins and a fractional remainder of the other solute, and the tubule carrying all the removed solute [@lumen-NephronStructure].

%% #### Tubule %%

The glomerulus is an overly aggressive filter; much of the water and solute must be re introduced to the blood from the tubules. %%in several stages. The first stage, the proximal convoluted tubule (PCT) pumps all the glucose and amino acids as well as most of the sodium and water back into the blood [@ogobuiroI2025-PhysiologyRenal]. In the next more water is reabsorbed, and in the final the remainder of the sodium as well as potassium and chlorides get reabsorbed via osmosis [@ogobuiroI2025-PhysiologyRenal]. %% The tubules run along side blood vessels and using a combination of osmosis, active transport and controlled ionic gradients %%sodium, potassium, calcium, magnesium, chlorides%% the valuable ions and most of the water is reabsorbed over several uniquely specialised segments [@ogobuiroI2025-PhysiologyRenal].  

%% #### Tubule cell %%

> ![Diagram of tubule, tubule wall and tubule cell structure.](Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/Tubule%20zoom%20diagram.png)
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

> ![Atomic Force Microscopy - mechanism diagram|400](Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/Atomic%20Force%20Microscopy%20-%20mechanism%20diagram.png)
> Atomic force microscope functional diagram

The sample once mounted to the sample stage can be manoeuvred precisely in all directions relative to the probe by applying voltage to piezoelectric actuators [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @giraudF2019-ChapterOneIntroduction]. This is how the sample is advanced into the tip. Once calibrated the voltage at the actuators gives the sample stage position and the voltage at the photodiode gives the deflection of the probe, with this a force displacement curve can be produced by accounting for the stiffness of the cantilever and the relative displacement [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials].

%% #### typical force displacement curve %%

A typical force displacement curve from a nano indention experiment has the following shape seen in figure #WIP (A) below. A broadly level region where the probe is not in contact with the cell; the contact region; a sloped region where the probe is indenting the cell; the turnaround point; from which the same is repeated in reverse differing mainly at the point of separation [@kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 

> ![fdcurve figure A - radmacherM2007-StudyingMechanicsCellular|350](Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/fdcurve%20figure%20A%20-%20radmacherM2007-StudyingMechanicsCellular.png) ![fdcurve figure B - radmacherM2007-StudyingMechanicsCellular|350](Projects/Uni%20Projects/Individual%20project/Assesments/Interim%20Assesment/Interim%20Report/attachments/fdcurve%20figure%20B%20-%20radmacherM2007-StudyingMechanicsCellular.png)
> Example AFM data from Radmacher 2007, (A) shows the curve as a whole, (B) zoomed into the contact / separation region [@radmacherM2007-StudyingMechanicsCellular].

%% Contact point jump %%

The exact point of contact is often ambiguous and rarely the same as the the point of separation. On approach the cantilever will be deflected away from the cell by van der waals forces until the spring force of the cantilever overcomes and surface tension takes hold [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials]. 
The point of separation is typically clearer as it's associated with a "jump" in cantilever deflection as the surface tension / adhesion of the cell to the probe is overcome [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces; @kilpatrickJI2015-NanomechanicsCellsBiomaterials].

%% 
> ![AFM contact point jump|400](AFM%20contact%20point%20jump.png)
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

## Project 

### Progress Overview

%% What did I state in my proposal %%

In my [Project Proposal](https://github.com/jasht1/Uni-Projects/blob/master/Individual%20project/Key%20Documents/Diabetic%20nephropathy%20Individual%20Project%20Proposal.pdf) I stated:

> [!quote] Deliverables
> The first stage of this project that broadly lines up with the first semester will be spent on research and processing the data into force displacement curves and will conclude in an interim report and oral presentation.
> 
> The second stage of this project that takes place over the second semester will be focused on extracting insights from the force displacement curves with numerical calculations for young's modulus and identification of features that may prove useful for distinguishing healthy from diseased samples. This will be presented in a dissertation like report along with an academic poster.

%% What have I done since %%

Since, my supervisor has advised me that I have a sufficient understanding of the background to proceed with the curve analysis.
I have begun working with the experimental data to begin putting together a suitable methodology for accurately assessing indentation curves.

### Research
%% Ultralearning %%

The main workload of this project thus far has been in familiarising myself with the background and context of the project. As going into this project I had no background in biology or microscopy with which to interoperate the single cell indentation data. I am now quite comfortable with the background and my reading has moved on to areas of potential progress and developments in the field. 

### Data Processing 

%% Learning Curve %%

I have familiarised myself with the JPK data processing software. I have gone through the relevant documentation and applied the understanding I have gained from the literature review to produce my first set of results and a process file. I have shared these along with a log of my methods with my supervisor and we will meet to discuss improvements. Once myself and Dr Siamantouras are happy with it these process files can be used to batch process experimental data. 

My log and results for this process can be seen on the working repository with the links below and in the annex.
- [Learning Curve Log](https://github.com/jasht1/Uni-Projects/blob/0744dc65cdd17b54bfb0e6cb28642035fd4155fb/Individual%20project/Notes/Logs/Data%20Processing/Learning%20Curve%20log.md)
- [Results.csv](https://github.com/jasht1/Uni-Projects/blob/45f03a3ad8d47985c7ff29ca28c1ddcb26cfcf45/Individual%20project/Workspace/Results.csv)

### Project Management

%% Obsidian Academic research & writing improvements %%

I have done several independent progress reviews, and keep a thorough logbook using obsidian. This contains:
- progress logs where I record my work; 
- meeting logs with meeting minuets and associated notes;
- literature notes, these contains my highlights and sticky notes from zotero and further elaboration for especially useful references;

My logbook can either be downloaded as a self hosting html site and viewed in your browser, or viewed in raw markdown on github. The downloadable version is updated less frequently but may provide a better user experience.
- [Downloadable Log Book (HTML)](https://universityoflincoln-my.sharepoint.com/:f:/g/personal/27047440_students_lincoln_ac_uk/EpLyFaGZXrdEpWxGMmkhhlgBkQwebvzmgBRP1TMNOh1UXw?e=r9awaK)
- [Live github repo](https://github.com/jasht1/Uni-Projects/tree/master/Individual%20project)

### Future Plans

%% What is my end goal %%

The aim of the project remains to identify of features of AFM indention curves of renal cells that may prove useful for distinguishing healthy from diseased samples.

%% What will I do next %%

In the immediate future I will continue to work with my supervisor to refine my curve processing in JPK. Once this is to a sufficient standard I will be able to produce a reliable set of young's moduli associated with the curves.

These results will be assessed for predictive power in distinguishing healthy from diseased cells and if effective a methodology will be proposed for doing so.

