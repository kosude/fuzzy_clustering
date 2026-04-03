# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

if __name__ == "__main__":
    exit(0)

import random
from sklearn.datasets import make_blobs
import numpy as np

def genpoints(method, N, C):
    match method:
        case "clst":
            x, c = make_blobs(n_samples=N,
                                centers=C,
                                cluster_std=0.60,
                                random_state=0)
            return np.array(x), c
        case _:
            raise Exception(f"Invalid point generation method \"{method}\"")
