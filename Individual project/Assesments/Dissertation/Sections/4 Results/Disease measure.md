
Given the observed data is distributed quite unevenly the choice of distribution used to model it's likelihood has a significant effect. Below are the candidate probability density functions for use in the classifier. The direct Gaussian based distributions i.e. Gaussian and skew-normal have additional dashed curves produced by Monte Carlo sampling 50,000 candidate distributions with means and standard deviations within the 95% confidence intervals of the observed distribution. These provide an indication of what a larger study would likely find.

![Comparison of Group Probability Density Functions by Distribution Model](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Group_PDFs_byModel.svg)

> Comparison of Group Probability Density Functions by Distribution Model

The single cell classification curves in the figure below show what a classifier based on each of the distribution models would rate a cell's probability of being from the treated/diseased group (1) vs the control/healthy group (0). This is valid for an average of 5 indentation tests performed as described in the experimental method a different number of tests and a different methodology would likely need additional controls or a model based on a more relevant dataset. 

%% Disease measure against YM coloured by test group %%

> ![Comparison of Distribution Models on Decision Curve](Classification_Threashhold_by_Distribution_Model.svg)
> Comparison of distribution models on single cell classifier decision curve

The confidence of the model increases, albeit diminishingly, the more samples are taken, an average of 15 cells, each being an average of 5 tests, from a common unknown group could be classified with an average accuracy of 90%. This largely is due to reducing the uncertainty in the crossover range of $500 \text{Pa} \lt  \text{YM} \lt 1000 \text{Pa}$ where a lage portion of samples are likely to fall and for a single cell might just as well be healthy or diseased.


--- start-multi-column: ID_j1ca
```column-settings
Number of Columns: 2
Largest Column: standard
```


> ![Average Classification Accuracy Threshold with n Samples](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Classification%20Accuracy%20vs%20Sample%20Size.svg)
> Average classification accuracy threshold with n samples, $90 \% @ \text{n}=15$ and $99 \% @ \text{n}=37$


--- column-break ---


> ![Normal Distribution Classifier Boundary Classification Confidence with n Samples](Projects/Uni%20Projects/Individual%20project/Assesments/Dissertation/Sections/attachments/Classification_Boundry_v_Samples.svg)
> Normal distribution classifier boundary classification confidence with n samples


--- end-multi-column



