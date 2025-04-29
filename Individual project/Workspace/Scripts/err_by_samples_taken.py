import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Observed Group parameters
mu_control = 482.63
mu_treated = 983.46
sd_control = 301.24
sd_treated = 506.70

sample_sizes = np.arange(1, 51)

def misclassification_error_unequal_var(n, mu1, mu2, sd1, sd2):
    # Standard error of the difference of means by variances
    se_diff = np.sqrt((sd1**2 + sd2**2) / n)
    z = abs(mu2 - mu1) / se_diff
    error = 1 - norm.cdf(z / 2)
    return error

errors = []
for n in sample_sizes:
    errors.append(
        misclassification_error_unequal_var(
            n, 
            mu_control, 
            mu_treated, 
            sd_control, 
            sd_treated
            )
        )

accuracies = [1 - 2 * e for e in errors]  # two-tailed misclassification

# Plotting
plt.figure(figsize=(6, 4))
plt.plot(sample_sizes, accuracies, '-o', label="Classification Accuracy")
plt.axhline(0.99, color='red', linestyle='--', label="99% Accuracy Threshold")
plt.xlabel("Number of Samples (n)")
plt.ylabel("Expected Classification Accuracy")
plt.title("Classification Accuracy vs. Sample Size")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
