import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.asarray(anchor)
    positive, negative = np.asarray(positive), np.asarray(negative)
    
    def distance(x, y):
        return np.sum((x - y) ** 2, axis=-1)

    losses = np.maximum(0, distance(anchor, positive) - distance(anchor, negative) + margin)
    
    return float(np.mean(losses))