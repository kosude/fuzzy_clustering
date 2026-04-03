# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

from genpoints import genpoints
import matplotlib.pyplot as plt

X, y = genpoints("clst", 200)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="viridis")
plt.show()
