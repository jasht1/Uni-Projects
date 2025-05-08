import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from classifier import direct_likelihood, get_ci

def group_pdf_ci_lims_figure(batch_data,lim_cases=False):
  x = np.linspace(0, 2000, 500)

  colors = {'Control': 'blue', 'Treated': 'red'}

  fig, ax = plt.subplots(figsize=(6, 4))

  for group in batch_data:
    data = batch_data[group]["Young's Modulus [Pa]"].astype(float)
    mean = data.mean()
    std = data.std()
    n = len(data)

    pdf = stats.norm.pdf(x, loc=mean, scale=std)
    ax.fill_between(x, pdf, alpha=0.3, color=colors[group], label=f'{group} PDF')

    if lim_cases==True:
      # best case would be means far apart tight distribution, worst is close together and wide
      ci_mean, ci_std = get_ci(mean, std, n)
      if group=='Treated':ci_mean=sorted(ci_mean, reverse=True) 

      best_pdf = stats.norm.pdf(x, loc=ci_mean[0], scale=ci_std[0])
      ax.plot(x, best_pdf, label=f'{group} Best-Case', linestyle=':', color=colors[group], alpha=0.5)

      worst_pdf = stats.norm.pdf(x, loc=ci_mean[1], scale=ci_std[1])
      ax.plot(x, worst_pdf, label=f'{group} Worst-Case', linestyle='--', color=colors[group], alpha=0.3)

  ax.set_xlim(0, 2000)
  ax.set_xlabel("Young's Modulus [Pa]")
  ax.set_ylabel("Probability Density")
  ax.set_title("Probability Density Functions of Test Groups")
  ax.legend()
  plt.tight_layout()
  plt.show()



def group_likelihood_figure(batch_data, models=["gaussian", "kde", "skewnorm"], lim_cases=False, mc_resampling=50000):
  x = np.linspace(0, 2000, 500)
  colors = {
    "gaussian": {'Control': 'tab:blue', 'Treated': 'tab:red'},
    "kde": {'Control': 'tab:cyan', 'Treated': 'tab:orange'},
    "skewnorm": {'Control': 'tab:green', 'Treated': 'tab:brown'}
  }

  # Collect all likelihoods to normalize Y axis later
  y_all = []

  fig, axes = plt.subplots(1, len(models), figsize=(5 * len(models), 4), sharex=True)
  if len(models) == 1:
    axes = [axes]  # ensure iterable

  for ax, method in zip(axes, models):
    for group in batch_data:
      data = batch_data[group]["Young's Modulus [Pa]"].astype(float)
      mean = data.mean()
      std = data.std()
      n = len(data)

      # Direct likelihood
      pdf = direct_likelihood(data, method, x)
      y_all.append(pdf)
      ax.plot(x, pdf, color=colors[method][group], label=f"{group} - {method}")

      # Monte Carlo resampling
      if method != "kde" and mc_resampling > 1:
        ci_mean, ci_std = get_ci(mean, std, n)
        sampled_means = np.random.normal(loc=mean, scale=(ci_mean[1] - ci_mean[0]) / 2, size=mc_resampling)
        sampled_stds = np.abs(np.random.normal(loc=std, scale=(ci_std[1] - ci_std[0]) / 2, size=mc_resampling))

        if method == "skewnorm":
          skew_val = (mean - np.median(data)) / std
          a_skew = np.clip(skew_val * 10, -20, 20)
        else:
          a_skew = None

        mc_stack = []
        for m, s in zip(sampled_means, sampled_stds):
          mc_pdf = direct_likelihood(data, method, x, mean=m, std=s, a_skew=a_skew)
          mc_stack.append(mc_pdf)

        mc_mean = np.mean(mc_stack, axis=0)
        y_all.append(mc_mean)
        ax.plot(x, mc_mean, linestyle='--', alpha=0.3, color=colors[method][group], label=f"{group} - {method} (MC)")

      elif method == "kde" and mc_resampling > 1:
        print(f"[INFO] MC skipped for KDE on {group}.")

      # Optional worst/best-case (only for Gaussian)
      if lim_cases and method == "gaussian":
        ci_mean, ci_std = get_ci(mean, std, n)
        if group == "Treated":
          ci_mean = sorted(ci_mean, reverse=True)
        best_pdf = stats.norm.pdf(x, loc=ci_mean[0], scale=ci_std[0])
        worst_pdf = stats.norm.pdf(x, loc=ci_mean[1], scale=ci_std[1])
        y_all.extend([best_pdf, worst_pdf])
        ax.plot(x, best_pdf, linestyle=':', alpha=0.4, color=colors[method][group], label=f"{group} Best")
        ax.plot(x, worst_pdf, linestyle='--', alpha=0.3, color=colors[method][group], label=f"{group} Worst")

    ax.set_title(f"{method.capitalize()} Likelihoods")
    ax.set_ylabel("Density")
    ax.set_xlabel("Young's Modulus [Pa]")
    ax.grid(True)
    ax.legend()

  # Set shared Y-limits
  y_max = np.max([y.max() for y in y_all])
  for ax in axes:
    ax.set_ylim(0, y_max * 1.05)

  # axes[-1].set_xlabel("Young's Modulus [Pa]")
  plt.tight_layout()
  plt.show()


def plot_group_pdf():
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data()
  group_pdf_ci_lims_figure(batch_data, lim_cases=True)
  # group_likelihood_figure(batch_data)

plot_group_pdf()
