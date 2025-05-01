import numpy as np
import pwlf

# def hertz(curve, smoothing = False, R = 5e-6, v = 0.5):
#     # Sample transformation
#     delta = np.array(curve['verticalTipPosition'])  # indentation
#     delta = delta - np.min(delta) + 1e-6  # avoid negative / zero
#     force = np.array(curve['vDeflection'])  # force
#
#     if smoothing:
#         from scipy.signal import savgol_filter
#         delta_smooth = savgol_filter(delta, 11, 3)
#         force_smooth = savgol_filter(force, 11, 3)
#         x = delta_smooth ** (3/2)
#         y = force_smooth
#     else:
#         x = delta ** (3/2)
#         y = force
#
#

def hertz_reigions(curve, smoothing = False, R = 5e-6, v = 0.5, reigions = 2):

    # Sample transformation
    delta = np.array(curve['verticalTipPosition'])  # indentation
    delta = delta - np.min(delta) + 1e-6  # avoid negative / zero
    force = np.array(curve['vDeflection'])  # force

    if smoothing:
        from scipy.signal import savgol_filter
        delta_smooth = savgol_filter(delta, 11, 3)
        force_smooth = savgol_filter(force, 11, 3)
        x = delta_smooth ** (3/2)
        y = force_smooth
    else:
        x = delta ** (3/2)
        y = force

    # Piecewise linear fit
    model = pwlf.PiecewiseLinFit(x, y)
    breaks = model.fit(reigions)
    slopes = model.slopes

    # Back out Young's modulus from each slope
    E = [ ((3/4) * a / np.sqrt(R))/(1-v) for a in slopes ]

    output = {
        "E": E,
        "Breaks": breaks
    }

    return output

def elastic_linearity(curve, smoothing = False, R = 5e-6, reigions = 2):
    import matplotlib.pyplot as plt
    # Sample transformation
    delta = np.array(curve['verticalTipPosition'])  # indentation
    delta = delta - np.min(delta) + 1e-6  # avoid negative / zero
    force = np.array(curve['vDeflection'])  # force

    if smoothing:
        from scipy.signal import savgol_filter
        delta_smooth = savgol_filter(delta, 11, 3)
        force_smooth = savgol_filter(force, 11, 3)
        x = delta_smooth ** (3/2)
        y = force_smooth
    else:
        x = delta ** (3/2)
        y = force

    plt.plot(x,y, 'r-', label='indentation normalised', linewidth=2)

    model = pwlf.PiecewiseLinFit(x, y)
    breaks = model.fit(reigions)
    xHat = np.linspace(min(x), max(x), num=10000)
    yHat = model.predict(xHat)
    plt.plot(xHat, yHat, '-', label='linear fits')

    plt.plot(delta,force, 'g-', label='force v indentation', linewidth=2)
    xHertz = xHat ** (2/3)
    yHertz = yHat
    plt.plot(xHertz, yHertz, '-', label='hertz fits')

    plt.show()

def fit_all_curves():
  from import_data import get_csv_datasets
  from import_data import get_paths as get_paths
  
  rpaths = {
      'Control': "Curves/csv-force-indentation/Control",
      'Treated': "Curves/csv-force-indentation/Treated"
  }
  paths = get_paths(rpaths)

  for path in paths:
    data = get_csv_datasets(paths[path])
    for dataset in data:
        elasticity_model = hertz_reigions(data[dataset])
        # print(f"{data[dataset][]}{elasticity_model})
        print(f"{elasticity_model}")
    return True

def single_curve():
    from import_data import get_csv_dataset
    # curve = 'force-depth-2014.05.23-17.50.39.csv'
    # curve = 'force-depth-2011.03.22-19.34.24.csv'
    curve = "force-save-2011.03.22-18.41.44.jpk-force"
    curve = get_csv_dataset(curve)
    elastic_linearity(curve,smoothing=True,reigions=2)

fit_all_curves()

# import matplotlib.pyplot as plt
