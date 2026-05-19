import numpy as np

def discriminator(x, W):
    """
    Returns: np.ndarray of shape (batch, 1) with probabilities rounded to 4 decimals
    """
    x, W = np.asarray(x), np.asarray(W)
    
    return 1 / (1 + np.exp(-(x @ W)))