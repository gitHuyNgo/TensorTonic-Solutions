import numpy as np

def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    X = np.asarray(data, dtype=float)

    col_min = X.min(axis=0)
    col_max = X.max(axis=0)

    ranges = col_max - col_min

    scaled = np.where(
        ranges == 0,
        0.0,
        (X - col_min) / ranges
    )

    return scaled.tolist()