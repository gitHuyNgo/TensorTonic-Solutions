import numpy as np

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    multiplier = 1.0 - (2.0 * a * lr)
    subtractor = lr * b
    
    for _ in range(steps):
        x0 = (x0 * multiplier) - subtractor

    return float(x0)