import numpy as np

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values = np.asarray(values)

    min_val = values.min()
    max_val = values.max()

    if min_val == max_val:
        return np.zeros_like(values, dtype=int).tolist()

    w = (max_val - min_val) / num_bins
    bins = ((values - min_val) / w).astype(np.int32)
    
    return np.minimum(bins, num_bins - 1).tolist()