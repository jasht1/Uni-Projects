
### Elasticity

$$F(\delta) = \frac{4}{3} \cdot \frac{E}{1 - \nu^2} \cdot \sqrt{R} \cdot \delta^{3/2}
$$
$$
\begin{align*}
  F & \text{::Force}\\
  E & \text{::Young's Modulus}\\
  v & \text{::Poisson's Ratio}\\
  R & \text{::Indenter Radius}\\
  \delta & \text{::Indentation depth}\\
\end{align*}
$$
  The Hertz/Sneddon spherical indentation model is matched to the force indentation curve to find the apparent elasticity of an experiment.
  
### Classifier
  
$$\hat{P}(G_2 \mid x) = \frac{P(x \mid G_2) \cdot P(G_2)}{P(x \mid G_1) \cdot P(G_1) + P(x \mid G_2) \cdot P(G_2)}$$
  
The Bayesian classifier is a function based on Bayes theorem that finds a posterior probability (the probability of a precondition given the result).
$$\begin{align*}  
P(G \mid x) & \text{::Posterior}\\
P(x \mid G) & \text{::Likleyhood}\\
P(G)        & \text{::Prior}\\
P(x)        & \text{::Evidence}\\
\end{align*}$$


Where the likelihood of a given group is determined by fitting the observed occurrences to a distribution / Probability Density Function (PDF). 3 distribution models are tested: Gaussian, Skewed Normal, and Kernel Density Estimation.


$$
  \hat{P}(x \mid G) =  
  \frac{1}{\sigma_{G} \sqrt{2 \pi}}  
  e^{\tfrac{-1}{2}  
  \left( \tfrac{x-\mu_{G}}{\sigma_{G}}\right)^{2}}  
$$

$$
  \hat{P}(x \mid G) =  
  \phi\left(x; \mu_G, \sigma_G \right)
  \cdot  
  \Phi\left(  
  \alpha_G \cdot \frac{x - \mu_G}{\sigma_G}  
  \right)
$$

$$
  \hat{P}(x \mid G) =  
  \frac{1}{n h} \sum_{i=1}^{n} K\left( \frac{x - x_{i_G}}{h} \right)  
$$

$$\begin{align*}
  \hat{P}(x \mid G)     &:: \text{Group Probability Density Function}\\
  x                     &:: \text{Observation (i.e. Young's Modulus)}\\
  \sigma_{G}            &:: \text{Group Standard Deviation}\\
  \mu_{G}               &:: \text{Group Mean}\\
  \phi(x; \mu, \sigma)  &:: \text{Normal PDF evaluated at } x \\
  \alpha_G              &:: \text{Group Skew Parameter} \\
  \Phi(z)               &:: \text{Standard Normal CDF} \\
  x_{i_G}               &:: \text{Observed Data Points from Group G}\\
  n                     &:: \text{Number of Observations}\\
  K(\cdot)              &:: \text{Kernel Function (i.e. Gaussian)}\\
  h                     &:: \text{Bandwidth (Smoothing Parameter)}\\
\end{align*}$$
