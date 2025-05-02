
Experimental data was received in the form of `.jpk-force` logs of head height position against vertical deflection force along with experimental metadata. The JPK data processing software was used to calculate the probe height based on spring constant and at this point the curves where exported in text form. In order to establish "trustworthy" values for YM the function included in the JPK data processing software was used with the deepest point of indentation to 1µm past the contact point as upper and lower bounds. This was then replicated for the text exports in python using `nanite` an open source package that offers the same Hertz/Sneddon elasticity model truncated power series approximation for spherical indenters with a difference in fit optimisation methods; where JPK Data Processing uses least squared regression, Nanite utilises machine learning for fit quality estimation and optimisation. Despite not providing the "trustworthy" fits as a rated training dataset Nanite reproduced the "trustworthy" YM estimations with an average deviation of less than ±0.05%. The Hertz parabolic indenter model was also tested and compared with the Hertz/Sneddon approximation producing similar YM values but with higher average residual RMS fit error. 

%% Quantify difference in Hertz v Sneddon average residuals %%

###### Figure: Comparison in Elasticity Fit Techniques for an Example Curve
--- start-multi-column: ID_31no
```column-settings
Number of Columns: 2
Largest Column: standard
```


![](Projects/Uni%20Projects/Individual%20project/Workspace/Curves/svg-images/Hertz/Control/Control-2011.03.22-18.41.44.svg)


--- column-break ---


![](Projects/Uni%20Projects/Individual%20project/Workspace/Curves/svg-images/Sneddon/Control/Control-2011.03.22-18.41.44.svg)


--- end-multi-column

