"""
Creates cross corralation maps
for Refrigeration coursework in "Energy Systems and Conversion" module
By Joseph Ashton
"""

def p_map(lab_readings):
    import matplotlib.pyplot as plt
    import seaborn 

    corralations = lab_readings.corr()
    pmap=seaborn.heatmap(corralations, annot=True,cmap="RdBu", cbar=False)
    pmap.xaxis.tick_top()

    plt.show()

