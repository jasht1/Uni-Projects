
from matplotlib import pyplot as plt

def successive_testing(relative=True):
  from import_data import get_results_data
  data = get_results_data(path="Experiment")
  cells = data["Cell"].unique()
  trend = {}
  for cell in cells:
    tests = data[data["Cell"]==cell]
    cell_name = f"{tests['Group'][:-1]}{cell}"
    avg = tests["Young's Modulus [Pa]"].mean()
    devation = list(tests["Young's Modulus [Pa]"])-avg
    if relative == True:
      trend[cell_name] = devation/avg * 100
    else:
      trend[cell_name] = devation
    plt.plot(trend[cell_name])
  plt.show()

successive_testing()

