import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns: np.ndarray with bottleneck residual block output (compress, process, expand + skip)
    """
    # YOUR CODE HERE
    x = np.asarray(x)
    W1, W2, W3, Ws = np.asarray(W1), np.asarray(W2), np.asarray(W3), np.asarray(Ws)
    
    if Ws is None:
        shortcut = x
    else:
        shortcut = x @ Ws

    out = np.maximum(0, x @ W1)
    out = np.maximum(0, out @ W2)
    out = out @ W3

    out = out + shortcut
    out = np.maximum(0, out)

    return out