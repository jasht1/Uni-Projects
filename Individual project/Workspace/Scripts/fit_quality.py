from matplotlib import pyplot as plt
import numpy as np

def fit_quality_plot (curve, ym, cp, bl, R = 5e-6, v = 0.5, find_cp=False, smoothing = False, zoom=7):

  curve = curve[curve["verticalTipPosition"] <= cp]

  e = (ym / (1 - v**2))
  # e = ym

  # indentation = -(curve["verticalTipPosition"] - cp)
  # actual_force = curve["vDeflection"] - bl 
  # txt exports already factor these corrections in
  indentation = -(curve["verticalTipPosition"])
  actual_force = curve["vDeflection"]  

  if smoothing:
    from scipy.signal import savgol_filter
    actual_force = savgol_filter(np.array(actual_force), 11, 3)

  if find_cp:
    model_cp = better_cp(indentation,actual_force)
  else: 
    model_cp = curve.loc[curve["vDeflection"] <= 0, "verticalTipPosition"].max()

  # model_indentation = indentation + cp - model_cp
  model_indentation = indentation

  model_force = (4/3) * e * np.sqrt(R) * model_indentation ** (3/2)

  plt.figure(figsize=(8, 6))
  plt.plot(indentation, actual_force, label='Measured Force', alpha=0.7)
  plt.plot(indentation, model_force, label='Hertz Model Fit', linestyle='--')
  plt.xlabel('Indentation [m]', fontsize=14)
  plt.ylabel('Force [N]', fontsize=14)
  plt.title('Hertz Model Fit Quality', fontsize=16)
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  if zoom:
    # plt.xlim(-1/10**zoom,indentation.max())
    zoom = 1/10**zoom
    plt.xlim(-zoom,indentation.max()+zoom)
  plt.show()

  print("yay")

def better_cp(indentation,force):
  import pwlf
  model = pwlf.PiecewiseLinFit(indentation, force)
  breaks = model.fit(2)
  
  return breaks[1]

def fit_quality_plot_for_curve(curve_fname, group='Control'):
  from import_data import get_jpk_batch_data as get_jpk_batch_data
  from import_data import get_csv_dataset

  curve = get_csv_dataset(curve_fname, group=group)
  if isinstance(curve, int):
    return 0
  
  batch_data = get_jpk_batch_data()[group]
  fit_data = batch_data[batch_data["Filename"] == curve_fname]

  ym = fit_data["Young's Modulus [Pa]"].max()
  cp = fit_data["Contact Point [m]"].max()
  bl = fit_data["Baseline [N]"].max()

  # fit_quality_plot(curve, ym, cp, bl, find_cp=True, smoothing=True)
  fit_quality_plot(curve, ym, cp, bl,smoothing=True)
  # fit_quality_plot(curve, ym, cp, bl)
  
# fit_quality_plot_for_curve("force-save-2011.03.22-20.02.34.jpk-force")

def fit_quality_plot_all():
  from import_data import get_paths as get_paths
  import os
  
  rpaths = {
      'Control': "Curves/jpk-force/HK2 Control",
      'Treated': "Curves/jpk-force/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)"
  }
  paths = get_paths(rpaths)

  for group in paths:
    for filename in os.listdir(paths[group]):
      if filename.startswith("force-save-") and filename.endswith(".jpk-force"):
        fit_quality_plot_for_curve(filename,group=group)
        
fit_quality_plot_all()
