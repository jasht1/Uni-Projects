
## Import curve
%%[[2025-03-24]] @ 23:00%%

1. Open the `.jpk-force` in the JPK Data Processing software.
2. Correct height for cantilever bending.
3. Fit Hertz model for Elasticity.

## Fit Ranges
%%[[2025-03-24]] @ 23:10%%

4 fit ranges per curve;
1. Full
   Use the full range of the dataset.
2. Wide
   Use from the deepest point of indentation to the flattest region such that the baseline appears at roughly the middle of the flat non contact region.
3. Medium
   Use a reasonable indentation depth (~1µm) to the flat region just past the shallow curve of the non contact interaction such that the fit most closely matches the curved region.
4. Tight
   Use a total range of ~1µm centred about contact region.
   
## Recordings
%%[[2025-03-24]] @ 23:19%%

| Lable                                            | Description                                                                            |
| ------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Data Set                                         | File name of `.jpk-force` dataset in the form: "force-save-YYYY.MM.DD.hh.mm.jpk-force" |
| Fit Range                                        | One of: [Full,Wide,Medium,Tight]<br>See [Fit Ranges](#Fit%20Ranges) for more details   |
| Xmin (µm)                                        | Lower bound of probe height used in Hertz fit range                                    |
| Xmax (µm)                                        | Upper bound of probe height used in Hertz fit range                                    |
| Contact Point (µm)                               | Estimated contact point given by Hertz fit                                             |
| Baseline (pN)                                    | Estimated baseline given by Hertz fit i.e. force in non contact region                 |
| Force (pN) [After Baseline correction]           | Peak force exerted on the cell given by Hertz fit                                      |
| Indentation depth (µm) [After height correction] | Max cell indentation depth given by Hertz fit                                          |
| Elastic Modulus (Pa)                             | Youngs module given by Hertz fit                                                       |
| Loading Force @ Xmin (pN)                        | Max cantilever deflection                                                              |
| velocity (nm/s)                                  | Indentation speed i.e. Speed at which the cantilever was advanced                      |
| Cantilever Sensitivity (nm/V)                    | AFM cantilever sensitivity                                                             |
| Tip shape                                        | AFM probe tip shape                                                                    |
| Tip radius (µm)                                  | AFM probe tip radius                                                                   |
| Poisson                                          | Poisson's ratio used in Hertz fit                                                      |
| Comments                                         | Additional Comments                                                                    |
