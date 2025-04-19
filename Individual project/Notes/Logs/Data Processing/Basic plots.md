
## Basic plots process
%%[[2025-04-18]] @ 17:23%%

### Aim
%%[[2025-04-18]] @ 17:23%%

I want to make a set of plots to compare the preliminary results of the [Batch JPK curve Processing](Batch%20JPK%20curve%20Processing%20log.md).

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

### Box Plots
%%[[2025-04-18]] @ 17:50%%

I need to compare control and treated cell young's modulus. A box plot / violin plot would be useful visualisations that account for distribution. 

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html

## Observation notes

### YM appears loosely correlated with RMS error
%%[[2025-04-18]] @ 18:35%%

![](Basic%20plots%20-%20YM%20vs%20RMS%20error%20(control).png)