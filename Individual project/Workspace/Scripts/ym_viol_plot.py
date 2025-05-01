from matplotlib import pyplot as plt
from matplotlib.cm import ScalarMappable
import matplotlib.colors as mcolors

def YM_viol_plot (batch_data, with_scatter=False, colour_by="ResidualRMS [N]", title="Young's Modulus Comparison"):
  data = []
  cprop = []
  lables = []

  for dataset in batch_data:
    ym = batch_data[dataset]["Young's Modulus [Pa]"].astype(float)
    cdata = batch_data[dataset][colour_by].astype(float)
    data.append(ym)
    cprop.append(cdata)
    lables.append(dataset)

  fig, ax =plt.subplots()  # just for the fussy cbar
  viols = ax.violinplot(data, showmeans=True, showmedians=True)

  viols['bodies'][1].set_facecolor('red')

  if with_scatter != False: # Plot scatter points colored by Residual cdata
    # cmap = plt.get_cmap('coolwarm')  # Blue to red
    cmap = plt.get_cmap('summer')  # green to yellow
    all_cdata = [r for cdata_list in cprop for r in cdata_list]
    norm = mcolors.Normalize(vmin=min(all_cdata), vmax=max(all_cdata))

    for i, (ym_vals, cdata_vals) in enumerate(zip(data, cprop)):
      colors = [cmap(norm(cdata)) for cdata in cdata_vals]
      x_vals = [i + 1] * len(ym_vals)  # align with violin center
      ax.scatter(x_vals, ym_vals, c=colors, alpha=0.5, s=100, edgecolors='none')

    # Add colorbar
    sm = ScalarMappable(norm=norm,cmap=cmap)
    # sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label(colour_by)

  plt.xticks([1, 2], lables)
  plt.ylabel("Young's Modulus [Pa]")
  plt.title(title)
  plt.tight_layout()
  plt.show()

def viol_plot (by='Cell', dataset='results', with_scatter=False, colour_by="ResidualRMS [N]", title="Young's Modulus Comparison"):
  if by == 'Experiment' and dataset == 'jpk':
    from import_data import get_jpk_batch_data
    batch_data = get_jpk_batch_data()
  if dataset == 'results':
    from import_data import get_results_batch_data
    batch_data = get_results_batch_data(path=by)

  if colour_by=="Cell Young's Modulus range [Pa]":
    from import_data import get_results_data
    data = get_results_data()
    data["Cell Young's Modulus range [Pa]"] = data["Max Young's Modulus [Pa]"] - data["Min Young's Modulus [Pa]"]
    batch_data={
        'Control': data[data['Group'] == "Control"],
        'Treated': data[data['Group'] == "Treated"]
    }
  if colour_by=="Cell Young's Modulus variance ±%":
    from import_data import get_results_data
    data = get_results_data()
    data["Cell Young's Modulus variance ±%"] = (data["Max Young's Modulus [Pa]"] - data["Min Young's Modulus [Pa]"])/data["Young's Modulus [Pa]"]
    batch_data={
        'Control': data[data['Group'] == "Control"],
        'Treated': data[data['Group'] == "Treated"]
    }

  YM_viol_plot(batch_data, with_scatter=True, colour_by=colour_by, title=title)

# viol_plot(colour_by="Cell Young's Modulus range [Pa]", title="Young's Modulus per Cell \n Coloured by Range Across Experiments")
viol_plot(colour_by="Cell Young's Modulus variance ±%", title="Young's Modulus per Cell \n Coloured by Variance Across Experiments")
# viol_plot(by="experiment", title="Young's Modulus per Experiment \n Coloured by Residual Fit Error")
