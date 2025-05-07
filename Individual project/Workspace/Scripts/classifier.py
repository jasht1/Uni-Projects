
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
    p_of_group: str = "Treated",
    alpha: float = 0.05,
    prior_control: float = 0.5,
    n_samples: int = 1,
    mc_resampling: int = 0,
    method: str = "kde",  # Options: 'gaussian', 'kde', 'skewnorm'
  ):
  YM = np.atleast_1d(YM)

  def sample_params(data):
    mean = data.mean()
    std = data.std()
    n = len(data)
    ci_mean, ci_std = get_ci(mean, std, n, alpha)
    sampled_means = np.random.normal(loc=mean, scale=(ci_mean[1] - ci_mean[0]) / 2, size=mc_resampling)
    sampled_stds = np.abs(np.random.normal(loc=std, scale=(ci_std[1] - ci_std[0]) / 2, size=mc_resampling))
    return sampled_means, sampled_stds

  def monte_carlo_likelihood(data, method):
    likelihood_samples = np.zeros((mc_resampling, len(YM)))
    sampled_means, sampled_stds = sample_params(data)

    if method == "skewnorm":
      data_skew = (data.mean() - data.median()) / data.std()
      a_skew = np.clip(data_skew * 10, -20, 20)
    else:
      a_skew = None

    for i in range(mc_resampling):
      likelihood_samples[i] = direct_likelihood(
          data, method, YM, n_samples=n_samples,
          mean=sampled_means[i], std=sampled_stds[i], a_skew=a_skew,
        )
      return likelihood_samples.mean(axis=0)

  def direct_likelihood(data, method, YM, n_samples=1, mean=None, std=None, a_skew=None):
    if method == "kde":
        kde = stats.gaussian_kde(data)
        return kde(YM)
    elif method == "gaussian":
        mean = data.mean() if mean is None else mean
        std = data.std() if std is None else std
        return stats.norm.pdf(YM, loc=mean, scale=std / np.sqrt(n_samples))
    elif method == "skewnorm":
      if a_skew is None:
        skew_val = (data.mean() - data.median()) / data.std()
        a_skew = np.clip(skew_val * 10, -20, 20)
      mean = data.mean() if mean is None else mean
      std = data.std() if std is None else std
      return stats.skewnorm.pdf(YM, a=a_skew, loc=mean, scale=std / np.sqrt(n_samples))

  # Choose appropriate likelihood estimation
  if mc_resampling > 1:
    likelihood_control = monte_carlo_likelihood(control_data, method)
    likelihood_treated = monte_carlo_likelihood(treated_data, method)
  else:
    likelihood_control = direct_likelihood(control_data, method, YM)
    likelihood_treated = direct_likelihood(treated_data, method, YM)

  # Bayes' Rule
  p_control = prior_control
  p_treated = 1 - p_control

  if p_of_group == "Control":
    numerator = likelihood_control * p_control
    denominator = numerator + likelihood_treated * p_treated
  else:
    numerator = likelihood_treated * p_treated
    denominator = numerator + likelihood_control * p_control

  posterior = numerator / denominator
  return posterior
