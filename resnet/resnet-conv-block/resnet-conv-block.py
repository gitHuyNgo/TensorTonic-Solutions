import numpy as np

def conv_block(x, W1, W2, Ws):
    """
    Returns: np.ndarray with sum of main path output and projected shortcut
    """
    # YOUR CODE HERE
    x = np.asarray(x)
    W1, W2, Ws = np.asarray(W1), np.asarray(W2), np.asarray(Ws)
    
    h = np.maximum(0, x @ W1)
    z = h @ W2
    s = x @ Ws
    y = np.maximum(0, z + s)

    return y