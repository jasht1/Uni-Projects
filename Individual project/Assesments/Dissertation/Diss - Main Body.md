---
title: Nanomechanical Analysis of Tubular Cell Cytoskeleton
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
%% #WIP %%

## Introduction

This project investigates changes in mechanical properties of kidney cells when exposed to TGF-β1, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. 
The aim of this project is to provide insight on the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy.

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
