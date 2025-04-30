from matplotlib import pyplot as plt
from matplotlib.cm import ScalarMappable
import matplotlib.colors as mcolors

def YM_viol_plot (batch_data, with_scatter=False, colour_by="ResidualRMS [N]"):
  data = []
  residuals = []
  lables = []

  for dataset in batch_data:
    ym = batch_data[dataset]["Young's Modulus [Pa]"].astype(float)
    cprop = batch_data[dataset]["ResidualRMS [N]"].astype(float)
    data.append(ym)
    residuals.append(cprop)
    lables.append(dataset)

  fig, ax =plt.subplots()  # just for the fussy cbar
  viols = ax.violinplot(data, showmeans=True, showmedians=True)

  viols['bodies'][1].set_facecolor('red')

  if with_scatter != False: # Plot scatter points colored by Residual cprop
    # cmap = plt.get_cmap('coolwarm')  # Blue to red
    cmap = plt.get_cmap('summer')  # green to yellow
    all_cprop = [r for cprop_list in residuals for r in cprop_list]
    norm = mcolors.Normalize(vmin=min(all_cprop), vmax=max(all_cprop))

    for i, (ym_vals, cprop_vals) in enumerate(zip(data, residuals)):
      colors = [cmap(norm(cprop)) for cprop in cprop_vals]
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

def viol_plot (by='cell', dataset='results'):
  if by == 'experiment' and dataset == 'jpk':
    from import_data import get_jpk_batch_data as get_batch_data
    batch_data = get_batch_data()
  if dataset == 'results':
    from import_data import get_results_batch_data as get_batch_data
    batch_data = get_batch_data(path=by)


  YM_viol_plot(batch_data, with_scatter=True)

viol_plot(by='cell')
