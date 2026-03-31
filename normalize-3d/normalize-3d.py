import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v, dtype=float)

    norm = np.linalg.norm(v, axis=-1, keepdims=True)

    return np.divide(v, norm, out=np.zeros_like(v), where=norm > 1e-6)