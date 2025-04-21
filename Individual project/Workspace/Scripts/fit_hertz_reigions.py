import numpy as np

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

def hertz_reigions(curve, smoothing = False, R = 5e-6, v = 0.5, reigions = 3):
    import pwlf  # or ruptures
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

def elastic_linearity(curve, smoothing = False, R = 5e-6):
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

    plt.plot(delta,force, 'go-', label='force v indentation', linewidth=2)
    plt.plot(x,y, 'rs', label='indentation normalised', linewidth=2)

def test():
    from import_data import get_csv_datasets
    csv_path = '/home/joe/Documents/Obsidian/SuperVault/Projects/Uni Projects/Individual project/Workspace/Curves/csv-force-indentation/untreated'
    data = get_csv_datasets(csv_path)
    # learning_curve = data['force-depth-2014.05.23-17.50.39']
    # elastic_linearity(learning_curve)
    for dataset in data:
        elasticity_model = hertz_reigions(data[dataset])
        print(elasticity_model)
    return True

test()

# import matplotlib.pyplot as plt
