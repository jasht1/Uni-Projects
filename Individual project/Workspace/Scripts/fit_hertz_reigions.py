import numpy as np
import pwlf  # or ruptures

def hertz_reigions(curve, smoothing = False, R = 5e-6):
    # Sample transformation

    # curve = curve.dropna()

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
    breaks = model.fit(3)
    slopes = model.slopes

    # Back out Young's modulus from each slope
    E = [ (3/4) * a / np.sqrt(R) for a in slopes ]

    output = {
        "E": E,
        "Breaks": breaks
    }

    return output


def test():
    from import_data import get_csv_datasets
    csv_path = '/home/joeashton/Sync/Obsidian/SuperVault/Projects/Uni Projects/Individual project/Workspace/Curves/csv-force-indentation/untreated/'
    data = get_csv_datasets(csv_path)
    learning_curve = data['force-depth-2014.05.23-17.50.39']
    elasticity_model = hertz_reigions(learning_curve)
    print(elasticity_model)
    return True

test()

# import matplotlib.pyplot as plt
