---
title: "Nanomechanical analysis of tubular cell cytoskeleton: Interim Report"
subtitle: 
titlepage-logo: /home/joeashton/Sync/Obsidian/SuperVault/Core/Templates/Pandoc/attachments/UoL_logo.png
bibliography: /home/joeashton/Sync/Obsidian/SuperVault/.pandoc/ZotLibrary.bib
author: "Joseph Ashton"
authors:
  - name: "Joseph Ashton"
    affiliation: "School of Engineering"
    institution: "University of Lincoln"
    email: "27047440@students.lincoln.ac.uk"
    address: "Lincoln"
acknowledgements: "I would like to thank my patient amd knowledgable suporvisor Eleftherios Siamantouras"
declaration: ""
abstract: "This project investigates changes in mechanical properties of kidney cells when exposed to TGF-β1, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. The aim of this project is to provide insight on the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy."
---

## Executive Summary
%% #WIP %%

## Introduction

This project investigates changes in mechanical properties of kidney cells when exposed to TGF-β1, which is known to induce renal disease [@gentleME2013-EpithelialCellTGFv]. 
The aim of this project is to provide insight on the progression of diabetic nephropathy from a mechanical perspective based on changes in mechanical properties observed in single cells using atomic force microscopy.

### Relevant Physiology

%% #### Kidney %%

%% Basically a blood filter %%

The human body can be understood as a complex biological machine, made up of many sub-mechanisms familiar to engineers. In this sense the filtration system of the human body is referred to as the renal system, in which the kidneys are a component about the size of a clenched fist that can be likened to a sophisticated water treatment plant combined with a feedback-controlled chemical processing unit. Each contain roughly a million multi step filter loops called nephrons [@bertramJF2011-HumanNephronNumber].  

> ![Kidney and nephron - Labeled|400](Kidney%20and%20nephron%20-%20Labeled.jpg)
> Kidney and Nephron form National Institute of Diabetes and Digestive and Kidney Diseases, National Institutes of Health. %% https://www.niddk.nih.gov/news/media-library/11236 %%

%% #### Nephrons %%

The nephrons are selective, able to remove waste products while keeping desirable substances in the blood. They are able to regulating essential substances such as water, electrolytes, and pH levels to strict set points. [@ogobuiroI2025-PhysiologyRenal]

%% ##### glomerulus %%

The the first step unfiltered blood enters the glomerulus and if forced through several membrane filters by hydro-static pressure. The first layer permits all solutes blocking only cells. The next is negatively charged thus blocking proteins like albumin. The final layer modulates the flow resistance to vary the hydro-static pressure gradient, this will be counter balanced by the osmotic pressure such that it can be used to effectively vary the ultra filtration coefficient. [@pavenstadtH2000-RolesPodocyteGlomerular; @ogobuiroI2025-PhysiologyRenal] Leaving the glomerulus is a blood vessel containing only cells and proteins and a fractional remainder of the other solute, and the tubule carrying all the removed solute [@lumen-NephronStructure].

%% ##### Tubule %%

The glomerulus is an overly aggressive filter such that much of the water and solute must be re introduced to the blood from the tubules. %%in several stages. The first stage, the proximal convoluted tubule (PCT) pumps all the glucose and amino acids as well as most of the sodium and water back into the blood [@ogobuiroI2025-PhysiologyRenal]. In the next more water is reabsorbed, and in the final the remainder of the sodium as well as potassium and chlorides get reabsorbed via osmosis [@ogobuiroI2025-PhysiologyRenal]. %% The tubules run along side blood vessels and using a combination of osmosis, active transport and controlled ionic gradients %%sodium, potassium, calcium, magnesium, chlorides%% the valuable ions and most of the water is reabsorbed over several specialised segments [@ogobuiroI2025-PhysiologyRenal].  

%% Breakdown of the layers and cell types %%

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

Atomic force microscopes use the deflection of a very fine probe on a flexible cantilever to detect contact forces ranging form nano to micro Newtons. By advancing a fine tipped probe on the end of the cantilever into a sample cell, a force over indentation depth curve can be produced from which the elasticity of the cell can be calculated using a Hertz contact model. [@dufreneYF2002-AtomicForceMicroscopy; @buttHJ1995-MeasuringSurfaceForces]

### Observing Fibrosis with AFM 

Developments in both understanding of the pathophysiology of kidney disease and the diagnostic application of atomic force microscopy (AFM) technology [@liuS2024-AtomicForceMicroscopyDisease-relatedStudies; @dufreneYF2002-AtomicForceMicroscopy] may provide a novel means of measuring the progression of kidney failure [@siamantourasE2016-QuantifyingCellularMechanics].

%% Need to know how easy it is to get hold of affected tubular cells from patients, is this non invasive? %%

The mechanical properties of tubular cells are largely a result of their cytoskeletal structure [@jalilianI2015-CellElasticityRegulated] which is altered significantly with the progression of DN [@buckleyST2012-CytoskeletalRearrangementTGFv1induced]. 

%% Inter cellular adhesion %%

## Literature Review

%% Table with papers and a relevant summary %%

## Project 

### Progress Overview

### Data Processing 

%% Learning Curve %%

### Project Management

%% Obsidian Academic research & writing improvements %%

### Research Methodology
%% Ultralearning %%

The main workload of this project thus far has been in familiarising myself with the background and context of the project. As going into this project I had no significant background in biology and to effectively interoperate the single cell indentation data an applied understanding of cytology, histology and microscopy are prerequisite.

## Self Evaluation Form

[STUDENT:: Joseph Ashton]

[STUDENT ID:: 27047440]

[SUPERVISOR:: Eleftherios Siamantouras]

[PROJECT TITLE:: Nanomechanical analysis of tubular cell cytoskeleton]

### Evaluation Criteria

> _The following criteria are intended to guide discussions around student understanding, project progress and future plans. Please evaluate yourself against these five criteria by ticking the relevant box under each heading._

Where:
1. Unsatisfactory,
2. Weak Pass,
3. Good,
4. Very Good,
5. Excellent.

| Please place a tick in the box that best evaluates your performance                                               | 1   | 2   | 3   | 4   | 5   |
| ----------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
| I would rate my understanding of the context and theoretical background to the project as…                        |     |     |     | X   |     |
| My work programme reflects the project aims, and has helped me meet my objectives                                 |     |     | X   |     |     |
| I would rate my technical progress against the work programme as…                                                 |     |     | X   |     |     |
| I have a clear plan for completing the project and I understand what I must do to complete the project            |     |     |     | X   |     |
| I have scheduled and attended all required meetings with my supervisor, and documented my progress in my log book |     |     |     | X   |     |

### Reflection

> *Use this space to write a brief reflection on your progress so far. Consider what aspects of your work have gone well and what aspects have been less successful.*

### Signature

Student Signature:
![Digital signiture|250](signature.png)

Date: 2025-02-05
