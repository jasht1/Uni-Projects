
%% (*mind the pun*) %%

## Method

### Smoothing
%%[[2024-12-03]] @ 13:40%%

Gaussian smoothing with a strength of 5 seems sufficient to remove all of what appears to be noise. However i will have to see how much of a difference this actually makes in terms of [[Young's modulus]] results, but I would expect very little in this instance as; the signal/trend is very clear, proportionally the noise is fairly negligible 

### Auto subtract baseline
%%[[2024-12-06]] @ 19:05%%

This step seems redundant, the `Determine elasticity from indentation` function finds the baseline independently. 

### Auto Find contact point
%%[[2024-12-06]] @ 17:24%%

This step also seems redundant, the `Determine elasticity from indentation` function finds the contact point independently and displays it with reference to the original vertical tip position anyway. 

### Correct Height for cantilever bending
%%[[2024-12-06]] @ 22:28%%

This step is vital, as the indentation of the cell is not given by the head height but its sum with the cantilever deflection.

### Determine elasticity from indentation
%%[[2024-12-06]] @ 22:53%%

It is vital that the Tip Radius & Poisson Ratio are set to match their true values. In this case:
- Tip Radius : $5 \micro \text{m}$
- Poisson Ratio : $0.50$

Selecting `Shift Curves` maps the axis relative to the contact point and baseline determined by the models approximation.

The fitment range will affect the models result. It is important to determine a standard procedure in order to produce concordant results.

## Results
%%[[2024-12-06]] @ 22:55%%

| Data Set                                 | Fit Range | Xmax (µm) | Xmin (µm) | Contact Point (µm) | Baseline (pN) | Elastic Modulus (Pa) |
| ---------------------------------------- | --------- | --------- | --------- | ------------------ | ------------- | -------------------- |
| force-save-2014.05.23-17.50.39.jpk-force | 0         | min       | max       | 94.77              | -136.9        | 143.1                |
| force-save-2014.05.23-17.50.39.jpk-force | 1         | 93        | 97        | 94.79              | -136.9        | 139.4                |
| force-save-2014.05.23-17.50.39.jpk-force | 2         | 93        | 95        | 94.75              | -121.1        | 142.2                |
| force-save-2014.05.23-17.50.39.jpk-force | 3         | 94        | 95        | 94.78              | -125          | 138.6                |

### Full results table

[Results](../../../Workspace/Results.csv)

```dataviewjs
const Path = "Projects/Uni Projects/Individual project/Workspace/Results.csv"
const csvFile = await dv.io.load(Path);
const rows = csvFile.split("\n").map(row => row.split(","));
const headers = rows[0];
const data = rows.slice(1);

dv.table(headers, data);
```
