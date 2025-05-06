
%% How did i get ym values from the datasets %%

Experimental data was received in the form of `.jpk-force` logs of head height position against vertical deflection force along with experimental metadata. The JPK data processing software was used to calculate the probe height based on spring constant and at this point the curves where exported in text form. In order to establish "trustworthy" values for YM the function included in the JPK data processing software was used with the deepest point of indentation to $1 \ \micro m$ past the contact point as upper and lower bounds. This was then replicated for the text exports in python using `nanite` an open source package that offers the same Hertz/Sneddon elasticity model truncated power series approximation for spherical indenters with a difference in fit optimisation methods; where JPK Data Processing uses least squared regression, Nanite utilises machine learning for fit quality estimation and optimisation. Despite not providing the "trustworthy" fits as a rated training dataset Nanite reproduced the "trustworthy" YM estimations with an average deviation of less than ±0.05%. The Hertz parabolic indenter model was also tested and compared with the Hertz/Sneddon approximation. All force indentation curves where plotted alongside those implied by the fitting along with the residual fitting error to identify potential anomalies or systematic error. Attention was paid to identify any consistent trends in the residual as If the residual where to consistently deviate from generally flat noise at 0 this would imply a poorly matched elasticity model.

%% How did I determine the appropriate cell YM given the experimental data %%

As each cell was tested 5 times the apparent YM of a cell was taken to be the average average  of the Hertz/Sneddon fits. To validate the results the force indentation curves of the experiments and the implied curve of the apparent YM where plotted and inspected visually checking for cell relaxation or systematic error based on observable trends in successive experimentation or any apparent anomalies. In addition the 95% confidence interval of the apparent cell YM was calculated for the natural set and a $100 \times$ bootstrapped super set and these metrics where inspected to assert whether the apparent YM given by the average is a fair representation of the cell behaviour.

%% Confidence Intervals, what are they and how did I calculate them %%

As the apparent cell YM was taken to be the mean it's confidence intervals where those of the mean YM for the set of cell tests. 

$$\text{CI}_\mu = \left[ \mu - t^* \cdot \frac{\sigma}{\sqrt{n}},\ \mu + t^* \cdot \frac{\sigma}{\sqrt{n}} \right]
\qquad
\text{CI}_\sigma = \left[ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{upper}}} },\ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{lower}}} } \right]
$$

Where confidence intervals where calculated for the standard deviation as is later necessary in determining the confidence in the group classifications and when montecarlo sampling, the chi distribution is used. This was originally tried using normal distributions being a generally acceptable approximation, however given the small and bottom biased experiment sample sets symmetric distribution of probable standard deviations was not a fair representation.

%% Bootstrapping, what is it, why did I do it %%

