import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    
    if rng is not None:
        rand = rng.random(x.shape)
    else:
        rand = np.random.random(x.shape)

    keep = rand < (1 - p)

    pattern = np.where(keep, 1.0 / (1 - p), 0.0)

    output = x * pattern

    return output, pattern