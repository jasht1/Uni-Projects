import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from classifier import get_group_probability


def classification_threshold(mc_resampling=0, pos_only=False, cbg=True):
  from import_data import get_results_batch_data
  YM_vals = np.linspace(0, 2000, 500)
  batch_data = get_results_batch_data(path="Experiment")
  control_data = batch_data["Control"]["Young's Modulus [Pa]"]
  treated_data = batch_data["Treated"]["Young's Modulus [Pa]"]
  methods = ["gaussian", "kde", "skewnorm"]
  cmap = plt.get_cmap('tab20')

  plt.figure(figsize=(6, 4))

  for i, method in enumerate(methods):
    color = cmap(i * 2)
    probs_nomc = get_group_probability(
      YM_vals, control_data, treated_data,
      p_of_group="Treated", n_samples=5, mc_resampling=0, method=method
    )
    plt.plot(
      YM_vals, probs_nomc, label=f"{method.title()}",
      color=color, linestyle="-", linewidth=2.5, # alpha=0.7
    )

    if mc_resampling > 0 and method != "kde":
      # Monte Carlo
      color = cmap(i * 2+1)
      probs_mc = get_group_probability(
        YM_vals, control_data, treated_data,
        p_of_group="Treated",
        n_samples=5, mc_resampling=mc_resampling, method=method
      )
      plt.plot(
        YM_vals, probs_mc, label=f"{method.title()} (MC)",
        color=color, linestyle="--"
      )

  if pos_only:
    plt.ylim(0.5, 1)
  else:
    plt.axhline(0.5, color="gray", linestyle="--", label="Decision Threshold")

  if cbg:
    norm = Normalize(vmin=0, vmax=1)
    ref_probs = get_group_probability(
      YM_vals, control_data, treated_data,
      p_of_group="Treated",
      n_samples=5,
      mc_resampling=mc_resampling,
      method="gaussian"
    )
    bg_colors = plt.get_cmap('RdBu')(norm(ref_probs))
    gradient = np.tile(bg_colors[np.newaxis, :, :], (100, 1, 1))
    plt.imshow(
      gradient,
      extent=[YM_vals.min(), YM_vals.max(), 0, 1],
      aspect='auto', alpha=0.5, origin='lower'
    )

  plt.xlabel("Young's Modulus (Pa)")
  plt.ylabel("Posterior Probability (Treated)")
  plt.title("Single Cell Classification Threshold Curves \nby Distribution Modeling Method")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()

classification_threshold()


def n_samples_effect(
    ym_range=(0, 2000),
    sample_sizes=[1, 2, 5, 10, 25, 50, 100],
    n_ym_points=300,
    cmap='RdBu_r',
    mc_resampling=1000
  ):
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data(path="Experiment")
  control_data = batch_data["Control"]["Young's Modulus [Pa]"]
  treated_data = batch_data["Treated"]["Young's Modulus [Pa]"]
  YM_vals = np.linspace(*ym_range, n_ym_points)

  fig, ax = plt.subplots(figsize=(6, 4))

  norm = Normalize(vmin=0, vmax=1)
  colormap = plt.get_cmap(cmap)

  for i, n in enumerate(sample_sizes):
    probs = get_group_probability(
      YM_vals, control_data, treated_data,
      p_of_group="Treated", n_samples=n,
      mc_resampling=mc_resampling
    )

    color_column = colormap(norm(probs))[:, :3]  # (n_ym_points, 3)
    color_column_2D = np.tile(color_column[:, np.newaxis, :], (1, 20, 1))  # (height, width, RGB)
    
    ax.imshow(
      color_column_2D,
      extent=[i, i + 1, ym_range[0], ym_range[1]],
      aspect='auto', origin='lower'
    )

  # Axis formatting
  ax.set_xlim(0,len(sample_sizes))
  ax.set_ylim(ym_range[0],ym_range[1])
  ax.set_xticks(np.arange(len(sample_sizes)) + 0.5)
  ax.set_xticklabels(sample_sizes)
  ax.set_ylabel("Young's Modulus [Pa]")
  ax.set_xlabel("Number of Cells Sampled")
  ax.set_title("Classification Boundary vs Sample Size")

  # Colorbar
  sm = ScalarMappable(norm=norm, cmap=cmap)
  sm.set_array([])
  cbar = plt.colorbar(sm, ax=ax)
  cbar.set_label("P(Diseased | YM)")

  plt.tight_layout()
  plt.show()

# n_samples_effect(ym_range=(500,1500), mc_resampling=10000)
