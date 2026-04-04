# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

if __name__ == "__main__":
    exit(0)

import numpy as np

def fcm(x, N, D, C, z):
    """
    Cluster analysis for dataset `x`, which has `N` datapoints of
    dimensionality `D`.

    `z` is the fuzziness exponent.

    Returns a tuple of:
     - `y`: set of `C` cluster centres of dimensionality `D`
     - `d`: set of `N` columns each containing distances from each datapoint to
            each of the `C` cluster centres
    """

    # cluster centres array
    y = np.empty((D, C))
    d = np.empty((C, N))

    # fuzzy partition matrix - values in each column must add to 1
    # initialise with random (but normalised) values
    u = np.random.rand(C, N)
    u_col_sums = u.sum(axis=0)
    u = u / u_col_sums;

    # calculate cluster centres y
    for i in range(C):
        # i: iterate through each cluster (column in y)
        for dim in range(D):
            sum1 = 0
            sum2 = 0
            for j in range(N):
                # j: iterate through each datapoint
                sum1 += (u[i, j] ** z) * x[dim, j]
                sum2 += u[i, j] ** z
            y[dim, i] = sum1 / sum2

    # calculate node-to-cluster distances d
    for i in range(C):
        y_i = y[:, i]
        for j in range(N):
            x_j = x[:, j]

            d[i, j] = np.sqrt(np.sum((x_j - y_i) ** 2))

    # update fuzzy partition matrix
    for i in range(C):
        for j in range(N):
            d_ij = d[i, j]

            sum1 = 0
            for k in range(N):
                d_ik = d[i, k]
                sum1 += (d_ij / d_ik) ** (2 / (z - 1))

            u[i, j] = np.reciprocal(sum1)

    # get objective function value
    J = 0
    for i in range(C):
        for j in range(N):
            J += (u[i, j] ** z) * (d[i, j] ** 2)

    return y, d
