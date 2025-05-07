
import numpy as np
import pandas as pd
from scipy import stats
from typing import Union

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

def get_group_probability(
    YM: Union[float, np.ndarray, pd.Series],
    control_data: pd.Series,
    treated_data: pd.Series,
    p_of_group: str="Treated",
    alpha: float = 0.05,
    prior_control: float = 0.5,
    n_samples: int = 1,
    mc_resampling: int = 0,
  ):
  YM = np.atleast_1d(YM) # Support scalar input

  if mc_resampling > 1 :
    def sample_params(data):
      mean = data.mean()
      std = data.std()
      n = len(data)
      ci_mean, ci_std = get_ci(mean, std, n, alpha)
      sampled_means = np.random.normal(loc=mean, scale=(ci_mean[1] - ci_mean[0]) / 2, size=mc_resampling)
      sampled_stds = np.abs(np.random.normal(loc=std, scale=(ci_std[1] - ci_std[0]) / 2, size=mc_resampling))
      return sampled_means, sampled_stds

    control_means, control_stds = sample_params(control_data)
    treated_means, treated_stds = sample_params(treated_data)

    likelihood_control = np.zeros((mc_resampling, len(YM)))
    likelihood_treated = np.zeros_like(likelihood_control)

    for i in range(mc_resampling):
      likelihood_control[i] = stats.norm.pdf(YM, loc=control_means[i], scale=control_stds[i] / np.sqrt(n_samples))
      likelihood_treated[i] = stats.norm.pdf(YM, loc=treated_means[i], scale=treated_stds[i] / np.sqrt(n_samples))

    likelihood_control = likelihood_control.mean(axis=0)
    likelihood_treated = likelihood_treated.mean(axis=0)
  else:
    likelihood_control = stats.norm.pdf(YM, loc=control_data.mean(), scale=control_data.std() / np.sqrt(n_samples))
    likelihood_treated = stats.norm.pdf(YM, loc=treated_data.mean(), scale=treated_data.std() / np.sqrt(n_samples))

  # Bayes' Rule
  p_control = prior_control
  p_treated = 1 - p_control

  if p_of_group == "Control":
    numerator = likelihood_control * p_control
    denominator = numerator + likelihood_treated * p_treated
  if p_of_group == "Treated":
    numerator = likelihood_treated * p_treated
    denominator = numerator + likelihood_control * p_control

  posterior = numerator / denominator

  return posterior
