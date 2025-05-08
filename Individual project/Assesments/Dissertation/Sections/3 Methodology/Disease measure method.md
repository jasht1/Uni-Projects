A Bayes classifier was constructed to quantify the probability of diabetic nephropathy from cell stiffness based on the effect observed in the experimental data. The control group is taken as a model of healthy cell presentation and the treated group representing the onset of diabetic nephropathy. Similarly to how cell properties where estimated from several tests, the typical group properties are estimated from several cells, conversely it can also be found by taking the averages and standard deviations of the whole dataset. It is often the case that considering the whole raw dataset provides more accurate picture of the group, however in this case it is appropriate to consider by subgroups i.e. by cells, this is because the samples are not independent and not representative of the test case. As it has been observed that successive tests are not introducing systematic error their average provides a more accurate estimation of the given cell, thus classification should be considered at the cell level.

$$
{\Large  
P(G \mid x) = \frac{P(x \mid G) \mid \cdot P(G)}{P(x)}  
}  
\qquad  
\begin{align}  
P(G \mid x) &:: \text{Posterior Probability}\\
P(x \mid G) &:: \text{Likleyhood}\\
P(G)   &:: \text{Prior Probability}\\
P(x)   &:: \text{Evidence}\\
\end{align}
$$

Bayes Theorem (Eq above) enables us to quantify the probability a cell is diseased given its YM by considering the posterior probability that it is an occurrence in a group with the appropriate probability density function. If we take healthy and diseased to be exclusive groups $G_{1}$ and $G_{2}$ then the probability of a cell being diseased would be given by the proportional instance probability of it's YM for the treated group over the control and treated groups all multiplied by their prior probability.

$$\large \hat{P}(G_2 \mid x) = \frac{P(x \mid G_2) \cdot P(G_2)}{P(x \mid G_1) \cdot P(G_1) + P(x \mid G_2) \cdot P(G_2)}$$

Where the likelihood of a given group is determined based on fitting the observed occurrences to a probability density function. 3 distribution modelling methods will be tested: 1) Gaussian, 2) Kernel Density Estimation, 3) Skewed normal. 
Gaussian is the familiar normal distribution implied by the mean and standard deviation of the YM observed in the experimental data. It assumes an ideal symmetrical probability density function like one that would be observed by taking infinite samples of a single true value obscured by white noise. 

$$
{\large  
\hat{P}(x \mid G) =  
\frac{1}{\sigma_{G} \sqrt{2 \pi}}  
e^{\tfrac{-1}{2}  
\left( \cfrac{x-\mu_{G}}{\sigma_{G}}\right)^{2}}  
}  
\qquad  
\begin{align}  
\hat{P}(x \mid G) &:: \text{Group Probability Density Function}\\
x           &:: \text{Observation (i.e. Young's Modulus)}\\
\sigma_{G}  &:: \text{Group Standard Deviation}\\
\mu_{G}     &:: \text{Group Mean}\\
\end{align}
$$

Skew-Normal is an extension of the Gaussian distribution that allows for asymmetric bias i.e. most of the observations occurring just to one side of the mean and a few occurring far out to the other. It dose this by multiplying the Gaussian as seen above, by the cumulative distribution function (CDF) of it's z-score multiplied by a skewness parameter. A CFD simply provides the probability of finding a value below a given threshold, and in this case that threshold is set by the distance of each observation from the mean biased by a skew parameter for it's shape. 

$$
{\large
\hat{P}(x \mid G) =  
\phi\left(x; \mu_G, \sigma_G \right)
\cdot  
\Phi\left(  
\alpha_G \cdot \frac{x - \mu_G}{\sigma_G}  
\right)
}
\qquad
\begin{align}
\phi(x; \mu, \sigma) &:: \text{Normal PDF evaluated at } x \\
\alpha_G          &:: \text{Group Skew Parameter} \\
\Phi(z)           &:: \text{Standard Normal CDF}
\end{align}
$$

Kernel Density Estimation (KDE) on the other hand is more observation focused producing a probability density function that more closely mimics the shape of the observed data without pre-supposing a particular form. It achieves this by producing a Gaussian for every single point centred at it's location with a fixed spread, these are then summed to produce a single complex curve.

$$
{\large  
\hat{P}(x \mid G) =  
\frac{1}{n h} \sum_{i=1}^{n} K\left( \frac{x - x_{i_G}}{h} \right)  
}  
\qquad  
\begin{align}  
x_{i_G}           &:: \text{Observed Data Points from Group G}\\
n                 &:: \text{Number of Observations}\\
K(\cdot)          &:: \text{Kernel Function (i.e. Gaussian)}\\
h                 &:: \text{Bandwidth (Smoothing Parameter)}\\
\end{align}
$$

Each of these distribution fitting methods will be tested in Bayesian classifier and prediction accuracy for the experimental dataset will be compared.
The prior probabilities depend on the application, for high throughput screening this wold be heavily biased towards the initial cell state, or in patient diagnosis this could be a function of patient specific and/or epidemiological factors. In the context of this report prior probabilities are simply the proportion of samples from each group.