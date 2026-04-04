# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

from genpoints import genpoints
from fcm import fcm

import matplotlib.pyplot as plt
import mplcursors
import numpy as np

np.set_printoptions(linewidth=150)


##
## Data generation and computations

N = 10
D = 2 # TODO genpoints currently requires this to be 2
C = 4
z = 2

x, _, ytarget = genpoints("clst", N, D, C)
y, d = fcm(x, N, D, C, z)


##
## Plotting

plt.figure(figsize=(10, 6))

sc_x = plt.scatter(x[0, :],
                   x[1, :],
                   facecolors="none",
                   edgecolors="lime",
                   label="Input data $x$",
                   zorder=20)
sc_y = plt.scatter(y[0, :],
                   y[1, :],
                   c="red",
                   label="Predicted clusters $y$",
                   zorder=20)
sc_ytarget = plt.scatter(ytarget[0, :],
                         ytarget[1, :],
                         marker="P",
                         c="green",
                         label="Target values for $y$",
                         zorder=30)

# line plot used to interactively show distances
plt_d, = plt.plot([], [], c="lightgrey", linestyle="dotted", zorder=0)
plt_d_curs = mplcursors.cursor([sc_x, sc_y], hover=2)
plt_d_anns = []
plt_d_ann_kwargs = { "fontsize": 8,
                     "xytext": (-8, 5),
                     "textcoords": "offset points",
                     "bbox": dict(fc="white",
                                  lw=0,
                                  alpha=0.5),
                     "zorder": 50 }

@plt_d_curs.connect("add")
def plt_d_curs_onadd(sel):
    xaxis = []
    yaxis = []

    # clear old annotations
    for ann in plt_d_anns:
        ann.remove()
    plt_d_anns.clear()

    sel_label = sel.annotation.get_text().split("\n")[0] # first line of ann.

    if sel_label == sc_x.get_label():
        # currently selecting an x-point
        for i in range(C):
            xaxis += [x[0, sel.index], y[0, i]]
            yaxis += [x[1, sel.index], y[1, i]]

            # add tracked annotation
            plt_d_anns.append(plt.annotate(f"d={d[i, sel.index]:.2f}",
                                           xy=(y[0, i], y[1, i]),
                                           **plt_d_ann_kwargs))
    else:
        # currently selecting a y-point
        for i in range(N):
            xaxis += [x[0, i], y[0, sel.index]]
            yaxis += [x[1, i], y[1, sel.index]]

            # add tracked annotation
            plt_d_anns.append(plt.annotate(f"d={d[sel.index, i]:.2f}",
                                           xy=(x[0, i], x[1, i]),
                                           **plt_d_ann_kwargs))

    plt_d.set_data(xaxis, yaxis)
    plt.show()

# show plots on one set of axes
plt.legend()
plt.title("Fuzzy c-means cluster analysis: predicted centres against data")
plt.show()
