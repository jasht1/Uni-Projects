from matplotlib import pyplot as plt

from import_data import get_paths as get_paths
from import_data import get_jpk_batch_data as get_jpk_batch_data

relative_paths = {
  'Control': "Curves/txt-export/HK2 Control/HK2 Control_processed-2025.04.18-16.35.00.tsv",
  'Treated': "Curves/txt-export/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)_processed-2025.04.18-16.25.25.tsv"
}

paths = get_paths(relative_paths)

batch_data = get_jpk_batch_data(paths)

data = []
lables = []
for dataset in batch_data:
  data.append(batch_data[dataset]["Young's Modulus [Pa]"].astype(float))
  lables.append(dataset)

plt.violinplot(data)

