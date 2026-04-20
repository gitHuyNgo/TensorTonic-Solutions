import numpy as np 

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    cosine_sim = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))
    
    if label == 1:
        loss = 1 - cosine_sim
    else:
        loss = max(0, cosine_sim - margin)
        
    return loss