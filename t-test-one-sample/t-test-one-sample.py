import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    n = len(x)

    mean_x = np.mean(x)
    s = np.sqrt(np.sum((x - mean_x) ** 2) / (n - 1))

    t = (mean_x - mu0) / (s / np.sqrt(n))

    return t