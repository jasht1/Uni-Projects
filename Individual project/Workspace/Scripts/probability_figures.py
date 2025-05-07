import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from classifier import direct_likelihood, get_ci

def group_pdf_ci_lims_figure(batch_data,lim_cases=False):
  x = np.linspace(0, 2000, 500)

  colors = {'Control': 'blue', 'Treated': 'red'}

  fig, ax = plt.subplots(figsize=(5, 3))

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



def group_pdf_by_model_figure(batch_data, models=["gaussian", "kde", "skewnorm"], lim_cases=False):
  x = np.linspace(0, 2000, 500)
  colors = {
    "gaussian": {'Control': 'tab:blue', 'Treated': 'tab:red'},
    "kde": {'Control': 'tab:cyan', 'Treated': 'tab:orange'},
    "skewnorm": {'Control': 'tab:green', 'Treated': 'tab:brown'}
  }

  fig, ax = plt.subplots(figsize=(6, 4))

  for method in models:
    for group in batch_data:
      data = batch_data[group]["Young's Modulus [Pa]"].astype(float)
      mean = data.mean()
      std = data.std()
      n = len(data)

      pdf = direct_likelihood(data, method, x, n_samples=1)
      ax.plot(x, pdf, color=colors[method][group], label=f"{group} - {method}")

      if lim_cases and method == "gaussian":
        ci_mean, ci_std = get_ci(mean, std, n)
        if group == "Treated":
          ci_mean = sorted(ci_mean, reverse=True)

        best_pdf = stats.norm.pdf(x, loc=ci_mean[0], scale=ci_std[0])
        worst_pdf = stats.norm.pdf(x, loc=ci_mean[1], scale=ci_std[1])
        ax.plot(x, best_pdf, linestyle=':', alpha=0.4, color=colors[method][group], label=f"{group} Best-Case")
        ax.plot(x, worst_pdf, linestyle='--', alpha=0.3, color=colors[method][group], label=f"{group} Worst-Case")

  ax.set_xlim(0, 2000)
  ax.set_xlabel("Young's Modulus [Pa]")
  ax.set_ylabel("Likelihood")
  ax.set_title("Likelihood PDFs by Group and Method")
  ax.legend()
  plt.tight_layout()
  plt.show()


def plot_group_pdf():
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data()
  # group_pdf_ci_lims_figure(batch_data)
  group_pdf_by_model_figure(batch_data)

plot_group_pdf()
