import numpy as np

def relu(x: np.ndarray) -> np.ndarray:
    """
    ReLU activation: f(x) = max(0, x)
    """
    # YOUR CODE HERE
    x = np.asarray(x)
    
    relu_x = np.maximum(0, x)

    return relu_x