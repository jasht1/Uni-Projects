
## Meeting Preparation

### Suggested Reading

#### Data Processing Software manual
[[JPK Data Processing Software MANUAL-6.0b.pdf]]

> [!QUOTE] Simarantos advice
> Chapter 6 Force Curve Processing and Analysis (p.63)
> 
> - 6.1 Practice opening a curve.
> - 6.2 Familiarise yourself with the Force curve window.
> 	- 6.2.1 Familiarise with the tabs and functions described View tab, 
> 	- 6.2.2 Display toolbar and zooming,
> 	- 6.2.3 Info tab.
> - 6.3 Learn how to save and export curves as images or ASCII text.
> - 6.4 Force curve processing operations
> 	- 6.4.1 NOT NEEDED UNLESS SPECIFIED - All data were recorded using calibrated sensors. 
> 	- 6.4.2 - 6.4.5 Learn about functions described
> 	- 6.4.7 Very important function - must be applied before modelling. Please make sure you understand this function well.
> 	- 6.4.10 Elasticity - fit experimental data to calculate Elastic modulus
> - 6.5 Batch Processing - This Operation is used for loading a set of curves. 
> - 6.7 Elasticity fit equations for different geometries (Hertz model)
> 
> 
> THEORY
> Please use the manual as a starting point to familiarise with Young's or Elastic Modulus.
> 
> The formula used in the software is for Spherical indenter. Please learn the model very well, and develop a working knowledge of all the variables and constants of the equation in relation to changes in the fitting parameters of the Elasticity fitting. 

## Meeting 

### General process for processing curve
%%[[2024-12-05]] @ 12:49%%

- Load Curve
- Smooth if necessary
- Set baseline
	- Auto Subtract baseline
	- Adjust by eye if necessary
	- Tilt if necessary 
- Adjust offset to contact point
	- Auto adjust x offset
- Determine elasticity from indentation
	- Test multiple fitting ranges
- Record results and assumptions in the following template:

#### Template

| Cell | Loading Force (nN) | Fit Range | Xmax () | Xmin () | Force (nN) | Contact Point () | Baseline () | Indentation depth () [After height correction] | Elastic Modulus () | Comments | velocity   |
| ---- | ------------------ | --------- | ------- | ------- | ---------- | ---------------- | ----------- | ---------------------------------------------- | ------------------ | -------- | ---------- |
| 1    |                    | 1         |         |         |            |                  |             |                                                |                    |          | spring     |
| 1    |                    | 2         |         |         |            |                  |             |                                                |                    |          | Tip shape  |
| 1    |                    | 3         |         |         |            |                  |             |                                                |                    |          | Tip radius |
|      |                    |           |         |         |            |                  |             |                                                |                    |          | Poisson    |

### ToDo
%%[[2024-12-05]] @ 12:54%%

- [x] Find [[Young's modulus]] of learning curve for several fit ranges ✅ 2024-12-06 [[Learning Curve log]]
- [x] Asses difference in [[Young's modulus]] when curve is tilted [[Curve Tilt]] ✅ 2024-12-09
- [x] Record all readings and assumptions in a table ✅ 2024-12-06 [[Results.csv]]
