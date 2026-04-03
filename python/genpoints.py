# Copyright (c) 2026 Jack Bennett.
# All Rights Reserved.
#
# See the LICENCE file for more information.

if __name__ == "__main__":
    exit(0)

from sklearn.datasets import make_blobs

def genpoints(method, n):
    match method:
        case "clst":
            pts, y = make_blobs(n_samples=n,
                                centers=4,
                                cluster_std=0.60,
                                random_state=0)
            return pts, y
