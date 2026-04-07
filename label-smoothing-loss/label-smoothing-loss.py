import math

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    loss = 0.0
    K = len(predictions)
    
    for i in range(K):
        q = 0.0
        if i == target:
            q = (1 - epsilon) + (epsilon / K)
        else:
            q = epsilon / K
        loss -= q * math.log(predictions[i])

    return loss