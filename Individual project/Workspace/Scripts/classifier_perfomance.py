import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from classifier import get_group_probability


def classification_threashold(mc_resampling=1000,pos_only=False, cbg=True):
  YM_vals = np.linspace(0, 2000, 500)
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data(path="Experiment")
  control_data = batch_data["Control"]["Young's Modulus [Pa]"]
  treated_data = batch_data["Treated"]["Young's Modulus [Pa]"]
  norm_healthy_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Control", n_samples=5, method="gaussian")
  norm_diseased_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Treated", n_samples=5, method="gaussian")
  pnorm_healthy_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Control", n_samples=5)
  pnorm_diseased_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Treated", n_samples=5)
  mc_healthy_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Control", n_samples=5, mc_resampling=mc_resampling)
  mc_diseased_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Treated", n_samples=5, mc_resampling=mc_resampling)

  # Plot
  plt.figure(figsize=(6, 4))

  plt.plot(YM_vals, norm_healthy_probs,  label="P(Healthy | YM) from Raw Data \n(assume normally distributed)", color="blue", alpha=0.5, linestyle=':')
  plt.plot(YM_vals, norm_diseased_probs, label="P(diseased | YM) from Raw Data \n(assume normally distributed)", color="red", alpha=0.5, linestyle=':')
  plt.plot(YM_vals, pnorm_healthy_probs,  label="P(Healthy | YM) from Raw Data", color="blue", alpha=0.5, linestyle='--')
  plt.plot(YM_vals, pnorm_diseased_probs, label="P(diseased | YM) from Raw Data", color="red", alpha=0.5, linestyle='--')
  plt.plot(YM_vals, mc_healthy_probs,  label="P(Healthy | YM) from Monte Carlo", color="blue")
  plt.plot(YM_vals, mc_diseased_probs, label="P(diseased | YM) from Monte Carlo", color="red")

  if pos_only:
    plt.ylim(0.5,1)
  else:
    plt.axhline(0.5, color="gray", linestyle="--", label="Decision Threshold")
  if cbg:  # colour background by priorprob
    cmap = plt.get_cmap('RdBu')
    norm = Normalize(vmin=0, vmax=1)
    colors = cmap(norm(mc_healthy_probs))
    grdnt = np.tile(colors[np.newaxis, :, :], (100, 1, 1))

    # Overlay on plot
    plt.imshow(
        grdnt,
        extent=[YM_vals.min(), YM_vals.max(), 0,1],
        aspect='auto',
        alpha=0.5,
        origin='lower'
    )
  plt.xlabel("Young's Modulus (Pa)")
  plt.ylabel("Posterior Probability")
  plt.title("Single Cell Classification Threshold Curves")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()

classification_threashold(mc_resampling=100)


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
