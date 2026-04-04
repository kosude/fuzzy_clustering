# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

if __name__ == "__main__":
    exit(0)

import numpy as np

def fcm(x, N, D, C, z, max_itr=4, min_J=1e-5):
    """
    Cluster analysis for dataset `x`, which has `N` datapoints of
    dimensionality `D`.

    `z` is the fuzziness exponent.

    Iterates a maximum of `max_itr` times, or until the objective function
    reduces to at least `min_J`.

    Returns a tuple of:
     - `y`: set of `C` cluster centres of dimensionality `D`
     - `d`: set of `N` columns each containing distances from each datapoint to
            each of the `C` cluster centres
     - `u`: partition matrix of `N` columns, containing normalised membership
            values of each datapoint to each of the `C` clusters
     - `itr`: the amount of iterations taken
    """

    # cluster centres array
    y = np.empty((D, C))
    d = np.empty((C, N))

    # fuzzy partition matrix - values in each column must add to 1
    # initialise with random (but normalised) values
    u = np.random.rand(C, N)
    u_col_sums = u.sum(axis=0)
    u = u / u_col_sums;

    for itr in range(max_itr):
        # calculate cluster centres y
        for i in range(C):
            # i: iterate through each cluster (column in y)
            for dim in range(D):
                sum1 = np.sum(np.power(u[i, :], z) * x[dim, :])
                sum2 = np.sum(np.power(u[i, :], z))
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

        # if improvement is below min_J then break early
        if J <= min_J:
            break

    return y, d, u, itr + 1
