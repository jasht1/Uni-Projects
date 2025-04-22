from matplotlib import pyplot as plt
import numpy as np

def fit_quality_plot (curve, ym, cp, bl, smoothing = False, R = 5e-6, v = 0.5):
  curve = curve[curve["verticalTipPosition"] <= cp]
  e = (ym / (1 - v**2))
  indentation = -(curve["verticalTipPosition"] - cp)
  actual_force = curve["vDeflection"] - bl
  model_force = (4/3) * e * np.sqrt(R) * indentation ** (3/2)

  plt.figure(figsize=(8, 6))
  plt.plot(indentation, actual_force, label='Measured Force', alpha=0.7)
  plt.plot(indentation, model_force, label='Hertz Model Fit', linestyle='--')
  plt.xlabel('Indentation [m]', fontsize=14)
  plt.ylabel('Force [N]', fontsize=14)
  plt.title('Hertz Model Fit Quality', fontsize=16)
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()

  print("yay")

def fit_quality_plot_for_curve(curve_fname, group='Control'):
  # from import_data import get_path as get_path
  from import_data import get_jpk_batch_data as get_jpk_batch_data
  from import_data import get_csv_dataset

  curve = list(get_csv_dataset(curve_fname, group=group).values())[0]
  batch_data = get_jpk_batch_data()[group]
  fit_data = batch_data[batch_data["Filename"] == curve_fname]

  ym = fit_data["Young's Modulus [Pa]"][0]
  cp = fit_data["Contact Point [m]"][0]
  bl = fit_data["Baseline [N]"][0]

  fit_quality_plot(curve, ym, cp, bl)
  
fit_quality_plot_for_curve("force-save-2011.03.22-18.41.44.jpk-force")
