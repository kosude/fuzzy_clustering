# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

from genpoints import genpoints
from fcm import fcm

import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(linewidth=150, )

N = 200
D = 2 # TODO genpoints currently requires this to be 2
C = 4
z = 2

x, colours = genpoints("clst", N, C)
x = x.T # column 1: X values, column 2: Y values
v = fcm(x, N, D, C, z)

plt.scatter(x[0, :], x[1, :], c=colours, cmap="viridis")
# plt.scatter(v[0, :], v[1, :])
plt.show()
