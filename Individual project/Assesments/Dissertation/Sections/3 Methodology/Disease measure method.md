
A Bayes classifier was constructed to quantify the probability of diabetic nephropathy from cell stiffness based on the effect observed in the experimental data. 

%% The following is the general formula for normal distribution: 

$$
{\large f(x)=
\frac{1}{\sigma \sqrt{2 \pi}}
e^{\frac{-1}{2}
\left( \cfrac{x-\mu}{\sigma}\right)^{2}}
}
\qquad
\begin{align}
f(x)	&= 	\text{Probability Density Function}\\
x       &=  \text{Variable (i.e. Young's Modulus)}\\
\sigma	&= 	\text{Standard Deviation}\\
\mu	    &= 	\text{Mean}\\
\end{align}
$$ %%


%% Bayes Classifier %%  

Bayes Theorem (Eq below) enables us to quantify the probability a cell is diseased given its YM by considering the posterior probability that it is an occurrence in a group with the appropriate probability density function.

$$\large
P(G∣x) = \frac{P(x∣G) \cdot P(G)}{P(x)} 
\qquad
\begin{align}
P(G∣x)	&= 	\text{Posterior Probability}\\
P(x∣G)  &=  \text{Likleyhood}\\
P(G)	&= 	\text{Prior Probability}\\
P(x)    &= 	\text{Evidence}\\
\end{align}
​$$

If we take healthy and diseased to be exclusive groups $G_{1}$ and $G_{2}$ then the probability of a cell being diseased would be given by:

$$\large P(G_2 \mid x) = \frac{P(x \mid G_2) \cdot P(G_2)}{P(x \mid G_1) \cdot P(G_1) + P(x \mid G_2) \cdot P(G_2)}$$

Where the likelihood of a given group is based on the normal distribution implied by the mean and standard deviation of the YM observed in the experimental data. 

%% $$P(x \mid G) = \frac{1}{\sqrt{2\pi}\sigma_G} \exp\left( -\frac{(x - \mu_G)^2}{2\sigma_G^2} \right)
$$ %%

$$
{\large P(x \mid G) = 
\frac{1}{\sigma_{G} \sqrt{2 \pi}}
e^{\tfrac{-1}{2}
\left( \cfrac{x-\mu_{G}}{\sigma_{G}}\right)^{2}}
}
\qquad
\begin{align}
P(x \mid G)	&= 	\text{Group Probability Density Function}\\
x           &=  \text{Variable (i.e. Young's Modulus)}\\
\sigma_{G}	&= 	\text{Group Standard Deviation}\\
\mu_{G}	    &= 	\text{Group Mean}\\
\end{align}
$$

And the prior probabilities will depend on the application, for high throughput screening this wold be heavily biased towards the initial cell state, or in patient diagnosis this could be a function of patient specific and/or epidemiological factors. In the context of this report prior probabilities are simply the proportion of samples from each group.