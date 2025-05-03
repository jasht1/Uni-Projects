
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt, patches, lines

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
  data_lable=None,
  x_lable="Certianty",
  y_lable="Young's Modulus [Pa]",
  title="Young's Modulus \nConfidence",
  # y_lims='Default',
  y_lims=[0,2000],
  y_scale='linear',
  colors = {
    'datapoints':'Default', 
    'notchfill': 'blue', 
    'Bars': 'blue',
    # 'mean': 'red'
    # 'stdv': 'red'
    },
  legend_handles=[]
  ):
  # if y_lims=='Default':
  #   y_lims=[data.min(),data.max()]
  if colors['datapoints'] == 'Default':
    colors['datapoints'] = ['blue'] * len(data)
  elif isinstance(colors['datapoints'], str):
    colors['datapoints'] = [colors['datapoints']] * len(data)
  elif len(colors['datapoints']) != len(data):
    raise ValueError(f"colors['datapoints'] length ({len(colors['datapoints'])}) must match data length ({len(data)})")

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
    ax.scatter(jitter, data, alpha=0.5, c=colors['datapoints'], label=data_lable)

  ax.set_xticks([position])
  ax.set_xticklabels([x_lable])
  ax.set_ylabel(y_lable)
  ax.set_title(title)
  ax.grid(True, axis='y', linestyle='--', alpha=0.7)
  ax.set_yscale(y_scale)
  ax.set_ylim(y_lims)

  legend_handles.append(patches.Patch(color=colors['notchfill'], alpha=0.3, label='Notched \nBox Plot'))
  legend_handles.append(patches.Patch(color=colors['notchfill'], alpha=0.1, label='Bootstrapped \nBox Plot'))
  legend_handles.append(lines.Line2D([], [], color='black', linewidth=1, label='Median'))
  legend_handles.append(lines.Line2D([], [], color=colors['Bars'], linewidth=3, label='Mean'))
  if ci_mean_bars == True:
      legend_handles.append(lines.Line2D([], [], color=f"dark{colors['Bars']}", linewidth=2, label='Mean 95% \nConfidence \nInterval'))
  if ci_stdv_bars == True:
      legend_handles.append(lines.Line2D([], [], color=f"xkcd:lightish {colors['Bars']}", linewidth=3, label='Standard \nDeviation'))
      legend_handles.append(lines.Line2D([], [], color=f"xkcd:dull {colors['Bars']}", linewidth=2, label='StdDv 95% \nConfidence \nInterval'))

  ax.legend(handles=legend_handles, loc='best')
  return legend_handles

def batch_ci_notch_whisker_plot(batch_data, ci_mean_bars=True, ci_stdv_bars=True):
  fig, ax = plt.subplots(figsize=(8, 6))
  
  base_colors = {'Control': 'blue', 'Treated': 'red'}
  datapoint_colors = {'Control': 'blue', 'Treated': 'red'}

  y_lims = [0, 2000]  # Ensuring the same y-axis range across groups

  legend_handles=[]

  for i, (group, df) in enumerate(batch_data.items()):
    data = df["Young's Modulus [Pa]"].astype(float)
    legend_handles = ci_notch_whisker_plot(
      data=data,
      ax=ax,
      scatterpoints=True,
      ci_mean_bars=ci_mean_bars,
      ci_stdv_bars=ci_stdv_bars,
      position=i,
      data_lable=group,
      x_lable=group,
      y_lable="Young's Modulus [Pa]",
      title="Young's Modulus by Group with Confidence Intervals",
      y_lims=y_lims,
      colors={
          'datapoints': datapoint_colors[group],
          'notchfill': base_colors[group],
          'Bars': base_colors[group]
      },
      legend_handles=legend_handles
    )

  ax.set_xticks(range(len(batch_data)))
  ax.set_xticklabels(batch_data.keys())
  ax.set_ylim(y_lims)
  ax.set_yscale('linear')
  ax.grid(True, axis='y', linestyle='--', alpha=0.7)
  # ax.legend(title="Group", loc='center left', bbox_to_anchor=(1.02, 0.5))
  ax.legend(handles=legend_handles, ncols=2, loc='best')
  # ax.legend(ncols=2)
  plt.tight_layout()
  plt.show()

def ci_figure():
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data()
  batch_ci_notch_whisker_plot(batch_data)

ci_figure()
