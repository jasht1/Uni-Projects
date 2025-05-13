
from matplotlib import pyplot as plt, cm
import numpy as np

def successive_testing(relative=True):
  from import_data import get_results_batch_data
  batch_data = get_results_batch_data(path="Experiment")
  plt.figure(figsize=(6,4))

  global_trend = []

  for group in batch_data:
    data=batch_data[group]
    cells = data["Cell"].unique()
    cmap = cm.Blues if group.lower() == "control" else cm.Reds
    colours = cmap(np.linspace(0.4, 0.9, len(cells)+1))
    group_trend = []

    for i, cell in enumerate(cells):
      cell_name = f"{group}{cell}"
      ym = data[data["Cell"]==cell]["Young's Modulus [Pa]"]
      avg = sum(ym)/len(ym)
      if relative == True:
        deviation = list((ym-avg)/avg * 100)
      else:
        deviation = list(ym-avg)
      # plt.plot(deviation, label=cell_name, alpha=0.3,c=colours[i])
      plt.plot(deviation, alpha=0.3,c=colours[i])
      if len(deviation)==5:
        group_trend.append(deviation)

    group_avg = np.nanmean(np.vstack(group_trend), axis=0)
    plt.plot(group_avg, color=colours[-1], linewidth=3, label=f"{group} avg")
    global_trend.append(group_trend)

  overall_avg = np.nanmean(np.vstack(global_trend), axis=0)
  plt.plot(overall_avg, color='black', linestyle='--', linewidth=2.5, label="Overall avg")

  plt.gca().set_xticks(range(1,5))
  plt.xlabel("Test Index")
  plt.ylabel("Relative Deviation [%]" if relative else "Absolute Deviation [Pa]")
  plt.title("Successive Test Deviation per Cell")
  plt.axhline(0, color="gray", linestyle="--", linewidth=1)
  plt.legend(ncols=3)
  plt.tight_layout()
  plt.grid(True)
  plt.show()

successive_testing(relative=True)
# successive_testing(relative=False)

