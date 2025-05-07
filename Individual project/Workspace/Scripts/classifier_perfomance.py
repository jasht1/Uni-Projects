import numpy as np
from matplotlib import pyplot as plt
from classifier import get_group_probability


def classification_threashold(pos_only=False, cbg=True):
  YM_vals = np.linspace(0, 2000, 500)
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data(path="Experiment")
  control_data = batch_data["Control"]["Young's Modulus [Pa]"]
  treated_data = batch_data["Treated"]["Young's Modulus [Pa]"]
  healthy_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Control", n_samples=5)
  deseased_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Treated", n_samples=5)
  mc_healthy_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Control", n_samples=5, mc_resampling=10000)
  mc_deseased_probs = get_group_probability(YM_vals, control_data, treated_data, p_of_group="Treated", n_samples=5, mc_resampling=10000)

  # Plot
  plt.figure(figsize=(6, 4))

  plt.plot(YM_vals, healthy_probs,  label="P(Healthy | YM) from Raw Data", color="blue", alpha=0.5, linestyle='--')
  plt.plot(YM_vals, deseased_probs, label="P(Deseased | YM) from Raw Data", color="red", alpha=0.5, linestyle='--')
  plt.plot(YM_vals, mc_healthy_probs,  label="P(Healthy | YM) from Monte Carlo", color="blue")
  plt.plot(YM_vals, mc_deseased_probs, label="P(Deseased | YM) from Monte Carlo", color="red")

  if pos_only:
    plt.ylim(0.5,1)
  else:
    plt.axhline(0.5, color="gray", linestyle="--", label="Decision Threshold")
  if cbg:  # colour background by priorprob
    from matplotlib.colors import Normalize

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
  plt.title("Classification Threshold Curves")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()

# classification_threashold(pos_only=True)
classification_threashold(pos_only=False)
