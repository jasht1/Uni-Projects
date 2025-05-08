
Given the observed data is distributed quite unevenly the choice of distribution used to model it's likelihood has a significant effect. Below are the candidate probability density functions for use in the classifier. The direct Gaussian based distributions i.e. Gaussian and skew-normal have additional dashed curves produced by Monte Carlo sampling 50,000 candidate distributions with means and standard deviations within the 95% confidence intervals of the observed distribution. These provide an indication of what a larger study would likely find.

![Comparison of Group Probability Density Functions by Distribution Model](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Group_PDFs_byModel.svg)


The single cell classification curves in the figure below show what a classifier based on each of the distribution models would rate a cell's probability of being from the treated/diseased group (1) vs the control/healthy group (0). This is valid for an average of 5 indentation tests performed as described in the experimental method a different number of tests and a different methodology would likely need additional controls or a model based on a more relevant dataset. 

%% Disease measure against YM coloured by test group %%

![Comparison of Distribution Models on Single Cell Classifier Decision Curve](Classification_Threashhold_by_Distribution_Model.svg)

The confidence of the model increases, albeit diminishingly, the more samples are taken, an average of 15 cells, each being an average of 5 tests, from a common unknown group could be classified with an average accuracy of 90%. This largely is due to reducing the uncertainty in the crossover range of $500 \text{Pa} \lt  \text{YM} \lt 1000 \text{Pa}$ where a lage portion of samples are likely to fall and for a single cell might just as well be healthy or diseased.


--- start-multi-column: ID_j1ca
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Average Classification Accuracy Threshold with n Samples, $90 \% @ \text{n}=15$ and $99 \% @ \text{n}=37$](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Classification%20Accuracy%20vs%20Sample%20Size.svg)


--- column-break ---


![Normal Distribution Classifier Boundary Classification Confidence with n Samples](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Classification_Boundry_v_Samples.svg)


--- end-multi-column


When tested on the raw experimental dataset (single test values) with model PDFs set to by experiment basis to suit the classifiers appear to perform well looking just at the average classification accuracy. However, due to the combination of control biased dataset, with $3\times$ as many control samples as test samples, and bottom biased distributions, where the majority of occurrences are lower than the average, models unfairly benefit from over confidently predicting the healthy group. This is certainly the case for the skewed-normal distribution as if the accuracy for just diseased cells is considered the models achieves less 50% average accuracy.


--- start-multi-column: ID_x54i
```column-settings
Number of Columns: 2
Largest Column: standard
```


![Classifier Performance on Raw Dataset in Colour Bars](Classifier_Performace_ColourBars_byExperiment.svg)


--- column-break ---


![Classifier Accuracy vs Sample Size for Different Likelihood Models](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Classification_Accuracy_v_Samples_byModel.svg)


--- end-multi-column


A better but still flawed initial estimate of model performance can be made by randomly sampling one of the 6, three methods for 2 groups, likelihood distributions to produce a faux sample. To reduce sampling bias this can be done many, in this case 1000 times per sample.  This method is still biased as it uses at least partially the exact same distribution to generate the samples as is being tested for it's affinity for the samples, additionally this is all still based on the same rather small experimental dataset which as was established earlier in the report embodies a high uncertainty for the real world occurrence distribution. The latter however is represented in the Monte Carlo versions indicated by "+MC", for these the sampling distributions are picked at random from 1000 candidate  distributions within the 95% confidence intervals of the observed data. However, the fact these have settled at ~0.7 is in fact a direct result of this chosen confidence interval but is still a relevant indicator of the confidence of this methodology. 