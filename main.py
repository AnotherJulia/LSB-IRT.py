import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import FormatStrFormatter


import os

xcount = 711
zcount = 343

# Import the IT.dat data
filepath = "IT.dat"
raw_irt_data = np.genfromtxt(filepath, skip_header=1, delimiter=",")
# print(raw_irt_data)

"""
First column: x/c is the x-axis
Second column: z/c is the z-axis (x/c and z/c make a top down view of the airfoil)
Third column: is the infrared radiation intensity
"""

# Process this data into something we can work it
xc = raw_irt_data[:,0]
zc = raw_irt_data[:,1]

xmin = xc.min()
xmax = xc.max()
zmin = zc.min()
zmax = zc.max()

flat_ir = raw_irt_data[:,2]
ir = flat_ir.reshape(zcount, xcount)

# Plot the data in a heatmap
def plot_ir_heatmap():
    fig_hm, ax_hm = plt.subplots()
    ir_heatmap = ax_hm.imshow(ir[:-1], origin="lower", extent=(raw_irt_data[0,0], raw_irt_data[-1,0], raw_irt_data[0,1], raw_irt_data[-1,1]), interpolation="nearest", aspect="auto")
    plt.colorbar(ir_heatmap, label="infrared radiation intensity", location="bottom")
    ax_hm.set_xlabel("x/c [-]")
    ax_hm.set_ylabel("z/c [-]")

    # TODO: Add more points to the x/z axes (more substeps in on the axis)

    plt.show()

plot_ir_heatmap()

