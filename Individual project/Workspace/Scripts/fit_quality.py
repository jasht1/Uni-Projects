from matplotlib import colors as mcolors, gridspec, pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

def fit_quality_plot (curve, ym, cp, bl, rms, R = 5e-6, v = 0.5, smoothing = False, zoom=7, filename='', residuals=True, save=False):

  curve = curve[curve["verticalTipPosition"] <= cp]

  e = (ym / (1 - v**2))
  indentation = -(curve["verticalTipPosition"])
  actual_force = curve["vDeflection"]  

  if smoothing:
    from scipy.signal import savgol_filter
    actual_force = savgol_filter(np.array(actual_force), 11, 3)

  model_indentation = indentation

  model_force = (4/3) * e * np.sqrt(R) * model_indentation ** (3/2)

  if residuals == True:
    residuals = actual_force - model_force
    abs_residuals = np.abs(residuals)

    fig = plt.figure(figsize=(8, 6))
    gs = gridspec.GridSpec(2,1,height_ratios=[4,1], hspace=0.10)
    # Main plot
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(indentation, actual_force, label='Measured Force', alpha=0.7)
    ax1.plot(indentation, model_force, label='Hertz Model Fit', linestyle='--')
    ax1.set_ylabel('Force [N]', fontsize=14)
    ax1.set_title(f"{filename} Hertz Model Fit Quality", fontsize=16)
    ax1.legend(title=f"Residual RMS: {rms}")
    ax1.grid(True)

    if zoom:
      zoom_val = 1 / 10**zoom
      ax1.set_xlim(-zoom_val, indentation.max() + zoom_val)

    # Residuals subplot with multicolored line
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    norm = mcolors.Normalize(vmin=abs_residuals.min(), vmax=abs_residuals.max())
    cmap = plt.get_cmap('summer')

    line = colored_line_between_pts(
      indentation.values,
      residuals.values,
      abs_residuals.values[:-1],  # one less for segments
      ax2,
      linewidth=2,
      cmap=cmap,
      norm=norm
    )

    ax2.set_xlabel('Indentation [m]', fontsize=14)
    ax2.set_ylabel('Residual[N]', fontsize=14)
    ax2.grid(True)
    ax2.set_ylim(residuals.min(),residuals.max())

    # cbar = fig.colorbar(line, ax=ax2, orientation='vertical', pad=0.01)
    # cbar.set_label('Residual Magnitude [N]', fontsize=12)

    plt.tight_layout()

  else:
    plt.figure(figsize=(8, 6))
    plt.plot(indentation, actual_force, label='Measured Force', alpha=0.7)
    plt.plot(indentation, model_force, label='Hertz Model Fit', linestyle='--')
    plt.xlabel('Indentation [m]', fontsize=14)
    plt.ylabel('Force [N]', fontsize=14)
    plt.title(f"{filename} Hertz Model Fit Quality", fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if zoom:
      # plt.xlim(-1/10**zoom,indentation.max())
      zoom = 1/10**zoom
      plt.xlim(-zoom,indentation.max()+zoom)

  if save == True:
    plt.savefig(f"exports/{filename}.svg")
  else:
    plt.show()

def colored_line_between_pts(x, y, c, ax, **lc_kwargs):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, **lc_kwargs)
    lc.set_array(c)
    return ax.add_collection(lc)

def fit_quality_plot_for_curve(curve_fname, group='Control', save=False):
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
  rms = fit_data["ResidualRMS [N]"].max()

  fit_quality_plot(curve, ym, cp, bl,smoothing=True, filename=f"{group}-{curve_fname[11:-10]}", rms=rms, save=save)
  
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
        fit_quality_plot_for_curve(filename,group=group, save=True)
        
# fit_quality_plot_all()
