import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x, p = np.asarray(x), np.asarray(p)

    if not np.isclose(np.sum(p), 1, atol=1e-6):
        raise ValueError("Hello world")

    return np.sum(x * p)