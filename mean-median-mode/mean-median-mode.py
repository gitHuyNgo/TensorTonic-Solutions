import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    
    mean = float(np.mean(x))
    median = float(np.median(x))

    counts = Counter(x)
    max_freq = max(counts.values())

    modes = [val for val, freq in counts.items() if freq == max_freq]

    mode = float(min(modes))

    return (mean, median, mode)