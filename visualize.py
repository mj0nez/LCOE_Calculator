import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


def plot(x_axis, y_axis, labels):
    """
    Plots the sensitivity of the levelized cost of electricity (y_axis) for
    n:= [1:5] arguments over the parameter variation (x_axis)

    :param x_axis:  parameter variation
    :param y_axis:  LCOE for n x len(x) variations
    :param labels:
    :return:
    """
    # style settings
    style_markers = ['o', 's', '^', 'x', 'o']
    markers_fill = ['full', 'none', 'full', 'full', 'full', ]
    markers_size = [5, 6, 6, 9, 5]
    style_lines = ['-.', '-.', ':', ':', '-.']
    style_colors = ['black', 'blue', 'green', 'red', 'orange']  # for CSS pallet

    lines_of_plot = np.shape(y_axis)
    figure = plt.figure(figsize=(8, 5))

    ax = plt.axes()
    figure.add_axes(ax)
    plt.ion()

    for line in range(lines_of_plot[0]):
        # add plots line-wise to axis with label and format style
        ax.plot(x_axis, y_axis[line, :],
                label=labels[line],
                color=mcolors.CSS4_COLORS[style_colors[line]],
                linestyle=style_lines[line],
                marker=style_markers[line],
                fillstyle=markers_fill[line],
                markersize=markers_size[line])

    # add legend and labels to plot
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
              fancybox=True, ncol=lines_of_plot[0])

    plt.ylabel('LCOE [€/kWh]', fontweight='bold')
    plt.xlabel('Parameter Variation', fontweight='bold')

    # grid options
    plt.grid(which='major', axis='y', linestyle='-')
    plt.minorticks_on()
    plt.grid(which='minor', axis='y', linestyle=':')


    # window state
    mng = plt.get_current_fig_manager()
    # mng.window.state('zoomed')

    # show plot
    plt.show(block=False) # program execution continues
    # plt.show(block=True)
    figure.tight_layout()

    return figure
