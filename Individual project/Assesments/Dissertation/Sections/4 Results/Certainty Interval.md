
%% Small sample size, Group overlap, predictive power %%
%% Look at these overlapping reigions %%
%% Cohen's d = 1.2015293213102536, this shows a strong effect size, but this  %%
###### Figure: Force Indentation for Apparent Cell YM Coloured by Test Group

![[YM_FD_comparison_byCell.svg]]
%% [[YM_FD_comparison_byExperiment.svg]] %%


###### Figure: Young's Module by Group with Confidence Metrics

![](YM_CI_byGroup.svg)

In the figure above the control group is contrasted with the treated group using notched Tukey style box plots overlaid with the mean and standard deviation 95% confidence intervals as well as the apparent cell YM values for each group. 

%% Confidence Intervals, what are they and how did I calculate them %%

$$\text{CI}_\mu = \left[ \mu - t^* \cdot \frac{\sigma}{\sqrt{n}},\ \mu + t^* \cdot \frac{\sigma}{\sqrt{n}} \right]
\qquad
\text{CI}_\sigma = \left[ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{upper}}} },\ \sqrt{ \frac{(n-1) \cdot \sigma^2}{\chi^2_{\text{lower}}} } \right]
$$

%% Bootstrapping, what is it, why did I do it %%
%% Overlapping notches, what dose this mean for the usability of the metric %%

%% ![](Group_PDFs_LimCases.svg) %%