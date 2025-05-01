
## Basic plots process
%%[[2025-04-18]] @ 17:23%%

### Aim
%%[[2025-04-18]] @ 17:23%%

I want to make a set of plots to compare the preliminary results of the [Batch JPK curve Processing](Batch%20JPK%20curve%20Processing%20log.md) as discussed in [Progress & Data](Progress%20&%20Data.md)

Primarily a box and whisker plot.

### Getting Batch processing data
%%[[2025-04-18]] @ 18:21%%

The JPK data processing software produces tsv tables summarising batch processes. In my case these contain the following data for each processed file.

``` datatypes
Filename                   [index, string]
Position Index             empty
X Position                 empty
Y Position                 empty
Young's Modulus [Pa]       float64
Contact Point [m]          float64
Baseline [N]               float64
Discontinuity Position     empty
Discontinuity Width [m]    0s
Adhesion [N]               0s
ResidualRMS [N]            float64
dtype: object
```

## Observation notes

### YM appears loosely correlated with RMS error
%%[[2025-04-18]] @ 18:35%%

![](Basic%20plots%20-%20YM%20vs%20RMS%20error%20(control).png)

## Box/violin Plots
%%[[2025-04-18]] @ 17:50%%

I need to compare control and treated cell young's modulus. A box plot / violin plot would be useful visualisations that account for distribution. 

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html

![](YM+Residuals_Viol_comparison_byExperiment.svg)
![](YM+Range_Viol_comparison_byCell.svg)
![](YM+Variance_Viol_comparison_byCell.svg)
See the code in [plots](plots.py) script

## Indentation vs Force
%%[[2025-04-20]] @ 01:21%%

A graph that shows indentation on x axis with force on y axis. 
Experimental data with Hertz fit overlay
Sub graph showing residual by indentation depth

%%[[2025-04-22]] @ 10:47%%

Every experiment now has an automatically generated Indentation vs Force graph displaying the accuracy of the fit.

![](Control-2011.03.22-19.12.50.svg)

![](Treated-2011.03.31-22.42.34.svg)

See the code in [fit_quality](fit_quality.py) script

## Young's Modulus FD Comparison
%%[[2025-04-22]] @ 10:49%%

The average, standard deviation, min/max, with faint traces for each fit for experimental values.
![](YM_FD_comparison_byCell.svg)
![YM_FD_comparison](YM_FD_comparison_byExperiment.svg)

