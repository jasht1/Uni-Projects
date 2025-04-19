from matplotlib import pyplot as plt
from matplotlib.cm import ScalarMappable
import matplotlib.colors as mcolors

def YM_viol_plot (batch_data, with_scatter=False):
  data = []
  residuals = []
  lables = []

  for dataset in batch_data:
    ym = batch_data[dataset]["Young's Modulus [Pa]"].astype(float)
    rms = batch_data[dataset]["ResidualRMS [N]"].astype(float)
    data.append(ym)
    residuals.append(rms)
    lables.append(dataset)

  fig, ax =plt.subplots()  # just for the fussy cbar
  viols = ax.violinplot(data, showmeans=True, showmedians=True)

  viols['bodies'][1].set_facecolor('red')

  if with_scatter: # Plot scatter points colored by Residual RMS
    # cmap = plt.get_cmap('coolwarm')  # Blue to red
    cmap = plt.get_cmap('summer')  # green to yellow
    all_rms = [r for rms_list in residuals for r in rms_list]
    norm = mcolors.Normalize(vmin=min(all_rms), vmax=max(all_rms))

    for i, (ym_vals, rms_vals) in enumerate(zip(data, residuals)):
      colors = [cmap(norm(rms)) for rms in rms_vals]
      x_vals = [i + 1] * len(ym_vals)  # align with violin center
      ax.scatter(x_vals, ym_vals, c=colors, alpha=0.5, s=100, edgecolors='none')

    # Add colorbar
    sm = ScalarMappable(norm=norm,cmap=cmap)
    # sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label("Residual RMS [N]")

  plt.xticks([1, 2], lables)
  plt.ylabel("Young's Modulus [Pa]")
  plt.title("Young's Modulus Comparison")
  plt.tight_layout()
  plt.show()

def test ():
  from import_data import get_paths as get_paths
  from import_data import get_jpk_batch_data as get_jpk_batch_data

  relative_paths = {
    'Control': "Curves/txt-export/HK2 Control/HK2 Control_processed-2025.04.18-16.35.00.tsv",
    'Treated': "Curves/txt-export/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)_processed-2025.04.18-16.25.25.tsv"
  }

  paths = get_paths(relative_paths)
  batch_data = get_jpk_batch_data(paths)

  YM_viol_plot(batch_data, with_scatter=True)

test()
