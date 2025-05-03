
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

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

def ci_notch_whisker_plot(
  data, 
  ax=False, 
  scatterpoints=True,
  ci_mean_bars=True, 
  ci_stdv_bars=False, 
  position=0,
  x_lable="Certianty",
  y_lable="Young's Modulus [Pa]",
  title="Young's Modulus Confidence",
  # y_lims='Default',
  y_lims=[0,2000],
  y_scale='linear',
  colors = {
    'datapoints':'Default', 
    'notchfill': 'blue', 
    'Bars': 'blue',
    # 'mean': 'red'
    # 'stdv': 'red'
    }
  ):
  # if y_lims=='Default':
  #   y_lims=[data.min(),data.max()]
  if colors['datapoints']=='Default':
    # colors['datapoints']=['blue']*data.size()
    colors['datapoints']=['blue']

  # fig, ax = plt.subplots(figsize=(10, 6))
  if ax==False:
    fig, ax = plt.subplots(figsize=(10, 6))
  
  mean = data.mean()
  std = data.std()
  n = len(data)
  ci_mean, ci_std = get_ci(mean, std, n)
  i = position

  # Boxplot at correct x position with color and transparency
  ax.boxplot(
    data,
    notch=True,
    patch_artist=True,
    widths=0.5,
    positions=[i],
    boxprops=dict(facecolor=colors['notchfill'], alpha=0.3, color=colors['notchfill']),
    whiskerprops=dict(alpha=0),
    capprops=dict(alpha=0),
    medianprops=dict(alpha=0),
    flierprops=dict(marker='')
  )
  ax.boxplot(
    data,
    notch=True,bootstrap=100,
    patch_artist=True,
    widths=0.75,
    positions=[i],
    boxprops=dict(facecolor=colors['notchfill'], alpha=0.1, color=colors['notchfill']),
    # whiskerprops=dict(color=colors['Bars']),
    # capprops=dict(color=colors['Bars']),
    medianprops=dict(color='black'),
    flierprops=dict(marker='')
  )

  if ci_mean_bars==True:
    # Mean
    ax.hlines(mean, i - 0.25, i + 0.25, color=colors['Bars'], linewidth=3)
    # CI for mean (darker)
    ax.hlines(ci_mean, i - 0.2, i, color=f"dark{colors['Bars']}", linewidth=2)
    ax.vlines(i - 0.1, ci_mean[0], ci_mean[1], color=f"dark{colors['Bars']}", linewidth=2)

  if ci_stdv_bars==True:
    # Std dev
    ax.vlines(i+0.1, mean - std, mean + std, colors=f"xkcd:lightish {colors['Bars']}", linewidth=3)
    ax.hlines(mean - std, i, i+0.2, colors=f"xkcd:lightish {colors['Bars']}", linewidth=3)
    ax.hlines(mean + std, i, i+0.2, colors=f"xkcd:lightish {colors['Bars']}", linewidth=3)
    # # CI for std dev (lighter)
    ax.vlines(i+0.1, mean + ci_std[0], mean + ci_std[1], colors=f"xkcd:dull {colors['Bars']}", linewidth=1)
    ax.vlines(i+0.1, mean - ci_std[0], mean - ci_std[1], colors=f"xkcd:dull {colors['Bars']}", linewidth=1)
    ax.hlines(mean - ci_std[0], i, i+0.2, color=f"xkcd:dull {colors['Bars']}", linewidth=2)
    ax.hlines(mean + ci_std[0], i, i+0.2, color=f"xkcd:dull {colors['Bars']}", linewidth=2)
    ax.hlines(mean - ci_std[1], i, i+0.2, color=f"xkcd:dull {colors['Bars']}", linewidth=2)
    ax.hlines(mean + ci_std[1], i, i+0.2, color=f"xkcd:dull {colors['Bars']}", linewidth=2)


  if scatterpoints==True:
    jitter = np.random.normal(loc=i, scale=0.02, size=len(data))
    ax.scatter(jitter, data, alpha=0.5, color=colors['datapoints'])

  ax.set_xticks([position])
  ax.set_xticklabels([x_lable])
  ax.set_ylabel(y_lable)
  ax.set_title(title)
  ax.grid(True, axis='y', linestyle='--', alpha=0.7)
  ax.set_yscale(y_scale)
  ax.set_ylim(y_lims)
  ax.legend()

def batch_ci_notch_whisker_plot(batch_data, ci_bars=False):
  fig, ax = plt.subplots(figsize=(10, 6))
  colors = {'Control': 'blue', 'Treated': 'red'}

  for i, group in enumerate(batch_data):
    data = batch_data[group]["Young's Modulus [Pa]"].astype(float)
    mean = data.mean()
    std = data.std()
    n = len(data)
    ci_mean, ci_std = get_ci(mean, std, n)

    # Boxplot at correct x position with color and transparency
    ax.boxplot(
      data,
      notch=True,
      patch_artist=True,
      positions=[i],
      widths=0.5,
      boxprops=dict(facecolor=colors[group], alpha=0.3, color=colors[group]),
      whiskerprops=dict(alpha=0),
      capprops=dict(alpha=0),
      medianprops=dict(alpha=0),
      flierprops=dict(marker='')
    )
    ax.boxplot(
      data,
      notch=True,bootstrap=1000,
      patch_artist=True,
      positions=[i],
      widths=0.75,
      boxprops=dict(facecolor=colors[group], alpha=0.1, color=colors[group]),
      # whiskerprops=dict(color=colors[group]),
      # capprops=dict(color=colors[group]),
      medianprops=dict(color='black'),
      flierprops=dict(marker='')
    )

    if ci_bars==True:
      # Mean
      ax.hlines(mean, i - 0.25, i + 0.25, color=colors[group], linewidth=3)
      # Std dev
      ax.vlines(i+0.1, mean - std, mean + std, colors=f"xkcd:lightish {colors[group]}", linewidth=3)
      ax.hlines(mean - std, i, i+0.2, colors=f"xkcd:lightish {colors[group]}", linewidth=3)
      ax.hlines(mean + std, i, i+0.2, colors=f"xkcd:lightish {colors[group]}", linewidth=3)

      # CI for mean (darker)
      ax.hlines(ci_mean, i - 0.2, i, color=f"dark{colors[group]}", linewidth=2)
      ax.vlines(i - 0.1, ci_mean[0], ci_mean[1], color=f"dark{colors[group]}", linewidth=2)
      # CI for std dev (lighter)
      ax.vlines(i+0.1, mean + ci_std[0], mean + ci_std[1], colors=f"xkcd:dull {colors[group]}", linewidth=1)
      ax.vlines(i+0.1, mean - ci_std[0], mean - ci_std[1], colors=f"xkcd:dull {colors[group]}", linewidth=1)
      ax.hlines(mean - ci_std[0], i, i+0.2, color=f"xkcd:dull {colors[group]}", linewidth=2)
      ax.hlines(mean + ci_std[0], i, i+0.2, color=f"xkcd:dull {colors[group]}", linewidth=2)
      ax.hlines(mean - ci_std[1], i, i+0.2, color=f"xkcd:dull {colors[group]}", linewidth=2)
      ax.hlines(mean + ci_std[1], i, i+0.2, color=f"xkcd:dull {colors[group]}", linewidth=2)


    # Jittered data points
    jitter = np.random.normal(loc=i, scale=0.02, size=len(data))
    ax.scatter(jitter, data, alpha=0.5, color=colors[group])

  ax.set_xticks(range(len(batch_data)))
  ax.set_xticklabels(batch_data.keys())
  ax.set_ylabel("Young's Modulus [Pa]")
  ax.set_title("Young's Modulus by Group with Confidence Intervals")
  ax.grid(True, axis='y', linestyle='--', alpha=0.7)
  ax.set_ylim(0,2000)
  plt.tight_layout()
  plt.show()


def ci_figure():
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data()
  batch_ci_notch_whisker_plot(batch_data,ci_bars=True)

# ci_figure()
