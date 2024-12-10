
> [!NOTE] See [[Diabetic nephropathy Individual Project Proposal#Project Proposal|Project Proposal]] for live draft 

# Planning
## Marking Criteria

> [!ATTENTION] Due on the [[2024-11-07]]

1. MEETING LOG: has the student scheduled a satisfactory number of meetings with the supervisor? Were these meetings productive?
2. PROJECT DESCRIPTION: does the student present a description of the project, its context and its relevance? Does the student demonstrate an initial understanding of the relevant theory/processes involved? 
3. OBJECTIVES AND DELIVERABLES: does the student demonstrate a clear understanding of the purpose of the project? Are the objectives carefully formulated and properly expressed?
4. PROJECT REQUIREMENTS: has the student identified what resources they will need and when they will be required?
5. PROJECT PLANNING: does the student present an appropriate & realistic work breakdown structure? Is this supported by a well-formatted Gantt Chart?
6. ETHICS: Has an ethics application been submitted? The assessment is marked as fail and the student cannot continue their work if an application has not been made.

If a fail is to be recorded a mark of zero should be reported and a suitable marking note provided. Feedback on the other elements


## Project Description
### Draft 1
Diabetic nephropathy is a serious complication of diabetes resulting in end-stage kidney failure, a life-threatening condition that requires dialysis or kidney transplantation. Progression of the disease is associated with complex defects at the cellular and molecular level of the kidney’s filtering unit, the nephron. The condition ultimately leads to dysfunction of the tubular structure of the nephron that is responsible for filtration, with devastating effects for the organ.

This project is an investigation into the qualitative effects of 

### Draft 2
%%[[2024-10-31]] @ 14:55%%

Diabetic nephropathy is a serious complication of both type 1 and 2 diabetes resulting in kidney failure due to progressive damage to the nephrons, structural units responsible for filtering the blood. One mechanism that contributes to this damage are mechanical alterations to the F-actin cytoskeleton that provide the structure of the renal tubules, a component of the nephron, these fine vessels line blood vessels and allow desirable molecules and ions to diffuse back into the blood. The cytoskeleton is a semisolid gel layer within the cell comprised of bundles of actin proteins held together by binding proteins providing mechanical structure and support to the cell. End stage diabetic nephropathy is associated with changes in the expression of actin binding proteins which in turn change the mechanical properties of the cytoskeleton of tubules. As Diabetes is also associated with high blood pressure and inflammation these potentially weakened structures are under additional stress. An improved understanding of the changes of the mechanical properties of tubular cell cytoskeleton can lead to novel understanding of the disease and development of single cell diagnostics and therapies related to nanomedicine.

This project aims to quantify the change in tubular cell elasticity in healthy and diabetic states though analysis of nanoscale force-displacement data from AFM-single cell force spectroscopy (SCFS) measurements on individual cells. This project will require fine processing of nanoscale data, numerical analysis, development of data sets and statistical comparison.

## Objectives and deliverables

### Should it include
- Number of curves to analyse?
- Young's modulus value or curve?
- Statistical analysis or finite element analysis?

### Clarifications in [[Reviewing project proposal]]
%%[[2024-11-05]] @ 17:44%%

- Identify and Understand the relevant Hertzian contact mechanics model
- How the model applies to nano indentation force displacement curves
- Conduct brief literature review on force displacement curves on single cell experiments
- Process raw force displacement data,
	- Identify errors and correct/reject curves as appropriate
		- systematic
		- recording
	- Identify contact point
		- Identify contact with cell membrane
	- Identify Linear reigion
	- Identify molecular structure that correspond with features of the curve
	- Apply model
- Calculation of Young's modulus
	- Refine parameters
- Statistical analysis
	- Graphs between healthy and diseased cells
	- Which parameters are most effective for diagnosis
	- Identify Optimal indentation depth 

## Requirements

### Familiarity with
#### Contact mechanics
Hertzian contact model

#### JPK Signal Processing software

#### Data Analysis

### Reading list

> ![[IndProj Reading List]]


## Ethics

Sent to Siamantouras for review on [[2024-11-01]]

# Working Draft

## Executive Summary
#WIP 


%% table of contents %%

## Background

Diabetic nephropathy is a serious complication of both type 1 and 2 diabetes resulting in kidney failure due to progressive damage to the nephrons, functional units responsible for filtering the blood.[^1] One mechanism that contributes to this damage are mechanical alterations to the F-actin cytoskeleton that provide the structure of the renal tubules[^2], a component of the nephron, these fine vessels line blood vessels and allow desirable molecules and ions to diffuse back into the blood.[^1] The cytoskeleton is a semisolid gel layer within the cell comprised of bundles of actin proteins held together by binding proteins providing mechanical structure and support to the cell.[^2] late stage diabetic nephropathy is associated with changes in the expression of actin binding proteins which in turn change the mechanical properties of the cytoskeleton of tubules. These changes can include reduced cell adhesion, cell coupling and cell-to-cell communication which have profound effects on overall integrity and function of the tubule.[^3] As Diabetes is also associated with high blood pressure and inflammation these potentially weakened structures are under additional stress promoting kidney failure. 

An improved understanding of the changes of the mechanical properties of tubular cell cytoskeleton can lead to novel understanding of the disease and development of single cell diagnostics and therapies related to nanomedicine.
 
%% #WIP Section on Single Cell AFM %%

The study of the physical properties of living cells is challenging, most techniques that would provide suitable resolution require manipulations like staining drying or freezing which compromise the validity of the results. Atomic force microscopy provides a non destructive means of observing single cells close to their native state. [^4]


<div style="page-break-after: always;"></div>    %% Page Break %%

## Project Summary

This project aims to quantify the change in tubular cell elasticity in healthy and diabetic states though analysis of nanoscale force-displacement data from AFM-single cell force spectroscopy (SCFS) measurements on individual cells. This project will require fine processing of nanoscale data, numerical analysis, development of data sets and statistical comparison.

## Objectives
%%[[2024-11-06]] @ 01:09%%

- Research
	- Identify the relevant Hertzian contact mechanics model and understand how the model applies to nano indentation force displacement curves
	- Conduct brief literature review on force displacement curves on single cell experiments
- Process raw data into force displacement curves
	- Identify errors and correct/reject curves as appropriate
	- Identify features such as:
		- contact/separation points
		- Linear region
		- features of the curve that correspond with the molecular structure.
- Statistical analysis
	- Calculation of Young's modulus
	- Graphs comparing healthy and diseased cells
	- If viable any parameters that may be effective for diagnosis along with Identifying Optimal indentation depth for tests

## Deliverables
%%[[2024-11-06]] @ 20:19%%

The first stage of this project that broadly lines up with the first semester will be spent on research and processing the data into force displacement curves and will conclude in an interim report and oral presentation.

The second stage of this project that takes place over the second semester will be focused on extracting insights from the force displacement curves with numerical calculations for young's module and identification of features that may prove useful for distinguishing healthy from diseased samples. This will be presented in a dissertation like report along with an academic poster. 

<div style="page-break-after: always;"></div>    %% Page Break %%

## Project Outline

### Gantt Chart

``` mermaid
gantt
title Project Timeline

dateFormat YYYY-MM-DD
excludes Christmas: 2024-12-20 to 2025-01-07, Exam week 1: 2025-01-14 to 2025-01-24, Exam week 2: 2025-04-15 to 2025-04-26

section Project Admin
	Ethics Subforms :crit, done, 2024-10-25, 4d
	Project Proposal :crit, active, 2024-10-27, 2024-11-07
	Book Interim Presentation : milestone, 2024-12-02, 1d
	Interim Report :crit, 2024-12-25, 2025-02-06
	Final Report :crit, 2025-04-01, 2025-05-08
	Poster : 2025-05-01, 2025-05-12

section Research
	Anatomy & Physiology :active, 2024-10-13, 2M
	Contact Models :active, 2024-10-28, 3M
	FD curve analysis: 2025-01-27, 45d

section Investigation
	Data Processing :2024-11-18 , 2024-12-25
	Data Analysis :2025-01-27, 2M

```

### Research / Project Requirements
%%[[2024-11-05]] @ 23:58%%

%%
- Research
	- Identify and Understand the relevant Hertzian contact mechanics model
	- How the model applies to nano indentation force displacement curves
	- Conduct brief literature review on force displacement curves on single cell experiments
%%

%% Background %%

During the first month of the project some time will be dedicated to the broader background of the project, putting into context the data that will be analysed. This means a rudimentary understanding of atomic force microscopy, the means by which the data was produced, as well as a working understanding of the relevant physiology.

%% Data analysis with software %%

In order to process the data into a form conducive to this investigation I will need to build a working knowledge of the JPK signal processing software package along with developing my data processing skill set in general.

%% contact mechanics %%

In order to interoperate the results a suitable model for the interaction must be developed. This will involve building a working knowledge of the various mathematical models of the behaviours at play and an appreciation for their respective strengths and weaknesses.

%% data presentation skills %%

<div style="page-break-after: always;"></div>    %% Page Break %%

### Data Processing
%%[[2024-11-06]] @ 00:15%%

%%
- Process raw force displacement data,
	- Identify errors and correct/reject curves as appropriate
		- systematic
		- recording
	- Identify contact point
		- Identify contact with cell membrane
	- Identify Linear reigion
	- Identify molecular structure that correspond with features of the curve
	- Apply model
%%

The raw data must be scrutinised for validity & viability, where systematic or recording errors are found the datasets will be corrected or rejected as appropriate.

The datasets must be converted to representative force displacement curves. Key features of the curves must be identified such as; 
- the point of contact with the cell membrane, 
- the region of linear elastic deformation, 
- features that describe the molecular structure, 
- any influential non-idealities.

### Analysis
%%[[2024-11-06]] @ 00:40%%

%%
- Statistical analysis
	- Calculation of Young's modulus
		- Refine parameters
	- Graphs between healthy and diseased cells
	- Which parameters are most effective for diagnosis
	- Identify Optimal indentation depth 
%%

The the linear regions of the curves, produced in the [[#Data Processing]] stage, are investigated using an appropriate contact model, as found in the [[#Research]] stage. This will be to to determine young's module, first of the graphs, then the cells, then healthy vs diseased. 

Visualisations will be produced in order to compare the behaviours of healthy and diseased cells. This will be in the hopes of identifying parameters that could be useful in single cell diagnosis. 

<div style="page-break-after: always;"></div>    %% Page Break %%

## References

[^1]: A. Madrazo-Ibarra and P. Vaitla, “Histology, Nephron,” 01-Jan-2024. [Online]. Available: https://www.ncbi.nlm.nih.gov/books/NBK554411/. [Accessed: 31-Oct-2024].

[^2]: G. M. Cooper, “Structure and Organization of Actin Filaments,” 01-Jan-2000. [Online]. Available: https://www.ncbi.nlm.nih.gov/books/NBK9908/. [Accessed: 31-Oct-2024].

[^3]: C. E. Hills, E. Siamantouras, S. W. Smith, P. Cockwell, K.-K. Liu, and P. E. Squires, “TGFβ modulates cell-to-cell communication in early epithelial-to-mesenchymal transition,” 01-Mar-2012. [Online]. Available: https://link.springer.com/article/10.1007/s00125-011-2409-9#Sec1. [Accessed: 06-Nov-2024].

[^4]: Y. F. Dufrêne, “Atomic Force Microscopy, a Powerful Tool in Microbiology,” 01-Oct-2002. [Online]. Available: https://journals.asm.org/doi/10.1128/jb.184.19.5205-5213.2002. [Accessed: 06-Nov-2024].
