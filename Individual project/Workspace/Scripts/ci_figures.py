
import numpy as np
from scipy import stats

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

def batch_ci_figure(batch_data):

def ci_figure():
