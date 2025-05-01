from matplotlib import pyplot as plt
import numpy as np

indentation = np.linspace(0,5e-7,1000)

def plot_batch_fd_from_ym (batch_data, title="Elasticity Fit Comparison"):

  for group in batch_data:

    ym = batch_data[group]["Young's Modulus [Pa]"]
    # rms = batch_data[batch]["ResidualRMS [N]"]
    ym_mean = ym.mean()
    mean_mdl = hertz_model(ym_mean)
    ym_stdv = ym.std()
    stdv_up = hertz_model(ym_mean+ym_stdv)
    stdv_dn = hertz_model(ym_mean-ym_stdv)
    max_mdl = hertz_model(ym.max())
    min_mdl = hertz_model(ym.min())

    if group == 'Control':
      cmap = plt.get_cmap('Blues') 
    elif group == 'Treated':
      cmap = plt.get_cmap('Reds') 
    colour = cmap(np.linspace(0,1,5))

    for value in ym:
      plt.plot(indentation,hertz_model(value),color=colour[3],linestyle='--',alpha=0.3)

    plt.fill_between(indentation,min_mdl,max_mdl, color=colour[2], alpha=0.2, label=f"{group} range")
    plt.fill_between(indentation,stdv_up,stdv_dn, color=colour[3], alpha=0.1, label=f"{group} standard deviation")
    plt.plot(indentation,mean_mdl, color=colour[4], linewidth=4, label=f"{group} mean")

  plt.xlabel('Indentation [m]', fontsize=14)
  plt.ylabel('Force [N]', fontsize=14)
  plt.title(title, fontsize=16)
  plt.tight_layout()
  plt.legend()
  plt.show()


  print("yay")

def hertz_model(ym, R = 5e-6, v = 0.5):
  e = (ym / (1 - v**2))
  force = (4/3) * e * np.sqrt(R) * indentation ** (3/2)
  return force

def batch_fd_from_ym (by='Cell',title="Elasticity Fit Comparison"):

  if by == 'Experiment':
    from import_data import get_jpk_batch_data 
    batch_data = get_jpk_batch_data()

  if by == 'Cell':
    from import_data import get_results_batch_data 
    batch_data = get_results_batch_data()

  plot_batch_fd_from_ym(batch_data,title=title)

batch_fd_from_ym(by='Cell',title="Cell Elasticity Fits by Test Group")
# batch_fd_from_ym(by='Experiment',title="Indentation Elasticity Fits by Test Group")

# yms = np.arange(100,2000,100)
#
# for ym in yms:
#   plt.plot(indentation,hertz_model(ym),label=ym)
#
# plt.show()
