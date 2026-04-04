# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

if __name__ == "__main__":
    exit(0)

from sklearn.datasets import make_blobs
import numpy as np

def genpoints(method, N, D=2, C=4):
    """
    Produce a dataset of `N` points of dimensionality `D` via the specified
    generation method, which is one of:
     - `clst` (with `C` clusters)

    Returns a tuple containing:
     - The dataset (`N` columns and `D` rows)
     - If using `clst`, cluster-wise colour mappings; otherwise, None
     - If using `clst`, cluster centres; otherwise, None
    """

    match method:
        case "clst":
            x, c, y = make_blobs(n_samples=N,
                                centers=C,
                                cluster_std=0.60,
                                random_state=0,
                                return_centers=True)
            return x.T, c, y.T
        case _:
            raise Exception(f"Invalid point generation method \"{method}\"")
