
## 
%%[[2025-04-29]] @ 19:38%%

I would like to be able to quantify the predictive power of stiffness as a means to distinguish diabetic from non diabetic cells.

## Effect of Sample size
%%[[2025-04-29]] @ 20:18%%

With the significant overlap of the estimated groups increasing the number of independent samples would be necessary to achieve higher classification accuracy / confidence.

![[Classification Accuracy vs Sample Size.svg]]

## CI finding methods
%%[[2025-05-03]] @ 20:22%%

I have found it is important to use Chi-squared distrbution as assuming normal gives complete garbage for my small sample sets

The `get_ci` function is now in [classifier](classifier.py) It uses Chi-Squared gets significantly different results for `ci_std`.  
The old function looked like this:

```py
def get_ci(mean, std, n, alpha=0.05):
  # Confidence interval for the mean using t-distribution
  t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
  se_mean = std / np.sqrt(n)
  ci_mean = (mean - t_crit * se_mean, mean + t_crit * se_mean)
  
  # Confidence interval for the standard deviation using chi-squared distribution
  chi2_lower = stats.chi2.ppf(alpha / 2, df=n - 1)
  chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
  ci_std = (
    np.sqrt((n - 1) * std**2 / chi2_upper),
    np.sqrt((n - 1) * std**2 / chi2_lower)
  )
  
  return ci_mean, ci_std
```

vs

```py
def get_ci(mean, std, n, confidence=0.95):  # returns garbage for our small sample sets
    t_score = stats.t.ppf((1 + confidence) / 2.0, df=n - 1)
    ci_mean = (mean - t_score * std / np.sqrt(n), mean + t_score * std / np.sqrt(n))
    ci_std = (std / np.sqrt(n), std * np.sqrt(n))  # Approx range, not strict CI
    return ci_mean, ci_std
```

Given an input of:

```py
mean float64 = np.float64(457.9905818181818)
std float = 305.51955732930037
n int = 11
alpha float = 0.05
```

The first version returned `ci_std` of:
`(np.float64(213.47172203124668), np.float64(536.1665205480673))` 
whereas the normal approximation version returns: 
`(np.float64(92.1176125251605), np.float64(1013.2937377767654))`.

It is reasonable to assume that the Chi version is a better estimate.